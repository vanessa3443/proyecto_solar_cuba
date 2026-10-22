# Mercado solar en Cuba: salarios vs. precio de paneles

Proyecto de Ciencia de Datos — primer año.

## Pregunta de investigación

**¿Cuántos meses de salario necesita un trabajador en Cuba para comprar un panel
solar, y cómo ha evolucionado esa cifra entre 2016 y 2025?**

Métrica central:

```
meses de salario = precio del panel (CUP) / salario medio mensual (CUP)
```

Comparar dos series que "suben" no basta: hay que medir quién sube más rápido.

## Estructura

```
mercado_solar/
├── data/raw/          datos originales (no se modifican)
├── data/processed/    datos limpios y unificados
├── figures/           gráficos exportados por los notebooks
├── notebooks/         análisis, en orden
│   ├── 01_exploracion.ipynb
│   ├── 02_limpieza.ipynb
│   ├── 03_encuestas.ipynb
│   └── 04_conclusiones.ipynb
├── plantillas/        guion de encuesta
├── src/               funciones reutilizables
├── requirements.txt
└── README.md
```

## Cómo ejecutar

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
jupyter notebook
```

Luego abrir los notebooks en orden (`01` → `04`).

## Estado de los datos

| Archivo | Contenido | Estado |
|---|---|---|
| `data/raw/salarios_cuba.csv` | salario medio por año (ONEI) | 2016-2025 cargados |
| `data/raw/precios_paneles.csv` | observaciones de precio (2021, 2026) | 4 casos precargados, faltan encuestas |
| `data/raw/ipc_cuba.csv` | índice anual del IPC (para deflactar) | PENDIENTE 2016–2026 |
| `data/raw/ipc_mensual_cuba.csv` | variaciones mensuales/interanuales 2026 | 3 observaciones (ONEI + TradingEconomics) |
| `data/raw/tipo_cambio_cup_usd.csv` | CUP por USD por año | 2026 = 815 (mercado); resto PENDIENTE |
| `storytelling.md` | narrativa y guion de exposición | con datos actuales |
| `data/raw/encuestas_percepcion.csv` | encuestas de percepción (12 cuestionario + 13 audio) | 25 casos cargados |
| `data/raw/transcripciones_calle.txt` | transcripciones verbatim de las entrevistas | E13–E25 |
| `plantillas/encuesta_paneles.md` | guion de la encuesta | usada en campo |

## Fuentes previstas

| Dato | Fuente |
|---|---|
| Salarios | ONEI — Anuario Estadístico de Cuba |
| IPC / precios | ONEI — índice de precios al consumidor |
| Tipo de cambio | ONEI / Banco Central de Cuba |
| Precio de paneles en Cuba | TiendML, Revolico, catálogos EGESA/Centropex (scraping) |
| Precio internacional $/Wp | World Bank *Tracking the Sun* / NREL |

## Reglas del proyecto

1. Cada fila de `data/raw/` lleva columna `fuente`.
2. Los datos crudos nunca se editan: la limpieza vive en `src/limpieza.py`.
3. Todo gráfico lleva título, ejes etiquetados y unidad.
4. Las conclusiones citan sus números.
