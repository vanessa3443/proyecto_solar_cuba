"""Recoleccion de precios de paneles solares desde paginas publicas.

Reglas del scraping:
  1. Leer robots.txt del sitio antes de raspar.
  2. Pocas peticiones, con pausa entre ellas.
  3. Solo datos publicos; nada de iniciar sesion ni eludir controles.
  4. Guardar siempre la URL de origen para poder citarla.
"""

from __future__ import annotations

import csv
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup

RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"
SALIDA = RAW_DIR / "precios_paneles.csv"

HEADERS = {
    "User-Agent": "proyecto-estudiantil-mercado-solar/1.0 (uso academico)"
}
PAUSA_SEGUNDOS = 2


def revisar_robots(url_base: str, user_agent: str = "*") -> bool:
    """Devuelve True si el robots.txt del sitio permite rastrear esa ruta."""
    try:
        resp = requests.get(
            f"{url_base.rstrip('/')}/robots.txt",
            headers=HEADERS,
            timeout=10,
        )
        if resp.status_code != 200:
            return True
        bloqueando = False
        for linea in resp.text.splitlines():
            if linea.lower().startswith("user-agent:"):
                bloqueando = linea.split(":", 1)[1].strip() in (user_agent, "*")
            elif bloqueando and linea.lower().startswith("disallow:"):
                ruta = linea.split(":", 1)[1].strip()
                if ruta and ruta != "/":
                    return False
        return True
    except requests.RequestException:
        return False


def obtener_html(url: str) -> str | None:
    """Descarga una pagina. Devuelve None si falla, en vez de lanzar error."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        time.sleep(PAUSA_SEGUNDOS)
        return resp.text
    except requests.RequestException as exc:
        print(f"[aviso] no se pudo descargar {url}: {exc}")
        return None


def extraer_precio(html: str, selector: str) -> str | None:
    """Extrae el texto de un elemento CSS. TODO: ajustar al sitio real."""
    soup = BeautifulSoup(html, "lxml")
    nodo = soup.select_one(selector)
    return nodo.get_text(strip=True) if nodo else None


def agregar_fila(fila: dict) -> None:
    """Anade una fila a data/raw/precios_paneles.csv sin tocar las existentes."""
    existe = SALIDA.exists()
    with SALIDA.open("a", newline="", encoding="utf-8") as fh:
        escritor = csv.DictWriter(fh, fieldnames=fila.keys())
        if not existe:
            escritor.writeheader()
        escritor.writerow(fila)


if __name__ == "__main__":
    print("Este modulo se completa en la Fase 3 del proyecto.")
    print(f"Salida prevista: {SALIDA}")
