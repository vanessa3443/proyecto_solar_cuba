"""Graficos del proyecto. Cada funcion devuelve la figura para poder guardarla."""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd

ANIO_BASE = 2016


def indice_rebase(df: pd.DataFrame, columnas: list[str]) -> pd.DataFrame:
    """Reescala cada serie a 100 en el anio base (compara tasas de crecimiento)."""
    base = df.loc[df["anio"] == ANIO_BASE, columnas].iloc[0]
    return df[["anio"]].join(df[columnas] / base * 100)


def graficar_indice(df: pd.DataFrame, columnas: list[str], titulo: str):
    fig, ax = plt.subplots(figsize=(9, 5))
    for col in columnas:
        ax.plot(df["anio"], df[col], marker="o", label=col)
    ax.axvline(ANIO_BASE, color="gray", linestyle="--", linewidth=1)
    ax.set_title(titulo)
    ax.set_xlabel("Anio")
    ax.set_ylabel(f"Indice ({ANIO_BASE} = 100)")
    ax.legend()
    ax.grid(alpha=0.3)
    fig.tight_layout()
    return fig


def graficar_meses_de_salario(df: pd.DataFrame):
    """Grafico de barras: meses de salario necesarios para comprar un panel."""
    df = df.assign(
        meses=df["precio_panel_cup"] / df["salario_medio_cup"]
    )
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(df["anio"], df["meses"], color="tab:orange")
    ax.set_title("Meses de salario para comprar un panel solar")
    ax.set_xlabel("Anio")
    ax.set_ylabel("Meses de salario")
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    return fig
