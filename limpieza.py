"""Limpieza y unificacion de series temporales.

Responsabilidades:
  - convertir los PENDIENTE a NaN (asi pandas los trata como faltantes)
  - pasar valores nominales a precios constantes con el IPC
  - unir salarios y precios en una sola tabla para graficar
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"
PROCESSED_DIR = Path(__file__).resolve().parents[1] / "data" / "processed"

ANIO_BASE = 2023


SUFIJOS_NUMERICOS = ("_cup", "_usd", "_wp", "_indice", "_pct")


def es_columna_numerica(columna: str) -> bool:
    """Decide si una columna debe ser numero: anio, *_cup, *_usd, *_wp, *_indice."""
    return columna == "anio" or columna.endswith(SUFIJOS_NUMERICOS)


def cargar(nombre: str) -> pd.DataFrame:
    """Lee un CSV crudo y convierte 'PENDIENTE' en NaN.

    Solo se convierten a numero las columnas que deben serlo (ver
    es_columna_numerica); el resto se deja como texto para no perder
    informacion como el nombre del vendedor o la fuente.
    """
    df = pd.read_csv(RAW_DIR / nombre)
    df = df.replace("PENDIENTE", pd.NA)
    for col in df.columns:
        if es_columna_numerica(col):
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def precio_en_cup(precios: pd.DataFrame) -> pd.Series:
    """Devuelve el precio en CUP: usa precio_cup o convierte precio_usd.

    Si una fila solo trae precio en USD, se multiplica por el tipo de cambio
    de ese anio (data/raw/tipo_cambio_cup_usd.csv).
    """
    tipo_cambio = cargar("tipo_cambio_cup_usd.csv").set_index("anio")[
        "tipo_cambio_cup_por_usd"
    ]
    convertido = precios["precio_usd"] * precios["anio"].map(tipo_cambio)
    return precios["precio_cup"].where(precios["precio_cup"].notna(), convertido)


def indice_ipc(base: int = 2025) -> pd.Series:
    """Indice encadenado de precios con base 100 en el anio `base`.

    Se construye con las variaciones anuales del IPC de
    data/raw/inflacion_cuba.csv: nivel(anio) = nivel(anio anterior) * (1 + tasa).
    Solo devuelve los anios cuya variacion esta publicada (faltan 2016-2019).
    """
    infl = cargar("inflacion_cuba.csv").dropna(subset=["variacion_ipc_pct"])
    anios = sorted(int(a) for a in infl["anio"])
    tasas = (infl.set_index("anio")["variacion_ipc_pct"] / 100).astype(float)

    nivel: dict[int, float] = {}
    anterior = None
    for anio in anios:
        nivel[anio] = 100.0 if anterior is None else nivel[anterior] * (1 + tasas.loc[anio])
        anterior = anio

    serie = pd.Series(nivel, dtype=float, name=f"indice_ipc_base_{base}")
    if base in serie.index:
        serie = serie / serie[base] * 100
    return serie.sort_index()


def salario_real(
    df: pd.DataFrame,
    columna: str = "salario_medio_cup",
    base: int = 2025,
) -> pd.Series:
    """Pasa una serie en pesos nominales a pesos constantes del anio `base`.

    salario_real = salario_nominal * indice(base) / indice(anio)
    Devuelve NaN en los anios sin variacion de IPC publicada.
    """
    indice = indice_ipc(base)
    factor = indice[base] / indice.reindex(df["anio"].astype(int))
    return df[columna] * factor.to_numpy()


def a_precios_constantes(df: pd.DataFrame, columna: str) -> pd.Series:
    """Deflacta una serie monetaria al anio_base usando el IPC."""
    ipc = cargar("ipc_cuba.csv").set_index("anio")["ipc_indice"]
    factor = ipc[ANIO_BASE] / ipc[df["anio"]]
    return df[columna] * factor


def precios_por_tipo() -> pd.DataFrame:
    """Una fila por observacion, con precio en CUP y precio por vatio (CUP/Wp).

    Se usa porque un modulo suelto y un sistema completo no son comparables;
    promediarlos seria un error metodologico.
    """
    precios = cargar("precios_paneles.csv")
    precios["precio_estimado_cup"] = precio_en_cup(precios)
    precios["precio_por_wp"] = precios["precio_estimado_cup"] / precios["potencia_wp"]
    return precios[
        [
            "anio",
            "fecha_medicion",
            "tipo",
            "potencia_wp",
            "precio_estimado_cup",
            "precio_por_wp",
            "vendedor",
            "fuente",
            "verificado",
        ]
    ].sort_values(["anio", "tipo"]).reset_index(drop=True)


def unificar() -> pd.DataFrame:
    """Une salarios, precios de paneles e IPC en una tabla por anio."""
    salarios = cargar("salarios_cuba.csv")
    precios = cargar("precios_paneles.csv")
    ipc = cargar("ipc_cuba.csv").rename(
        columns={"fuente": "fuente_ipc", "verificado": "verificado_ipc"}
    )

    precios["precio_estimado_cup"] = precio_en_cup(precios)
    precios["precio_por_wp"] = precios["precio_estimado_cup"] / precios["potencia_wp"]

    precios = precios.groupby("anio", as_index=False).agg(
        precio_panel_cup=("precio_estimado_cup", "mean"),
        precio_por_wp=("precio_por_wp", "mean"),
        tipo_producto=("tipo", "first"),
        fuente_precio=("fuente", "first"),
    )

    df = salarios.merge(precios, on="anio", how="outer").merge(ipc, on="anio", how="outer")
    df = df.sort_values("anio").reset_index(drop=True)
    return df


def guardar(df: pd.DataFrame, nombre: str = "serie_unificada.csv") -> Path:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    destino = PROCESSED_DIR / nombre
    df.to_csv(destino, index=False, encoding="utf-8")
    return destino


if __name__ == "__main__":
    print(unificar())
