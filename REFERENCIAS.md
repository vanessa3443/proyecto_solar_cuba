# Fuentes y referencias

Cada dato del proyecto debe aparecer aquí. Formato: **autor, título, fecha, tipo
de fuente (primaria/secundaria), qué aporta**.

## Fuentes primarias (cifras oficiales)

1. **ONEI** — *Anuario Estadístico de Cuba*, salarios medios mensuales 2016–2025.
   Aporta: `data/raw/salarios_cuba.csv`.
   Pendiente: anotar tabla y página de cada año.
   *Completar con año de edición y URL.*

2. **ONEI** — nota de prensa, 14/04/2026, *IPC de marzo de 2026*.
   Aporta: variación mensual 2,19 %, acumulada 5,54 %, interanual 13,42 %.
   (`data/raw/ipc_mensual_cuba.csv`)

3. **Auditoría en campo de la estudiante** (octubre 2026).
   Aporta: precios Copextel 2021, UNE 2026, Correos de Cuba 2026,
   10 cotizaciones de paneles en USD (`data/raw/precios_paneles.csv`).

4. **Encuesta propia** (octubre 2026), n = 25, muestra de conveniencia.
   Aporta: `data/raw/encuestas_percepcion.csv` + `transcripciones_calle.txt`.

## Fuentes secundarias (interpretación y apoyo)

5. **TradingEconomics** (datos oficiales cubanos) — inflación de Cuba, ago/2026:
   interanual 25,19 %, mensual 4,92 %, julio 2026: 20,70 %.
   `https://es.tradingeconomics.com/cuba/inflation-cpi`
   *Nota: usar la fuente oficial (ONEI) si se publica; TradingEconomics es el
   intermediario.*

6. **Análisis del IPC y del mercado de consumo cubano, 2015–2022** —
   AUTOR: __________ / TÍTULO: __________ / PUBLICACIÓN: __________ / FECHA: __________.
   Aporta (citas textuales usadas en las conclusiones):
   - 2022: **caída drástica del poder adquisitivo del salario medio** de los cubanos.
   - El aumento del consumo en 2021–2022 respondió al **alza de precios, no de cantidades**.
   - 70 % del consumo de 2022 en el mercado estatal = **control cuasi monopólico**, no mayor oferta.
   - Las **mipymes** cubren parte del consumo con **"precios casi prohibitivos"**
     para el bolsillo promedio.
   *Pendiente: completar la cita; sin autor y fecha no se puede usar en la entrega.*

7. **La Joven Cuba** — *Inflación: una nueva aceleración* (FECHA: ________).
   Aporta (`data/raw/inflacion_cuba.csv` y `tipo_cambio_observaciones.csv`):
   - Inflación anual: 2020 18,5 % | 2022 39,1 % | 2025 14,1 % (2021, 2023, 2024 pendientes).
   - 2026: IPC +15,1 % entre dic-2025 y jul-2026; julio = **581,56 puntos**.
   - Expectativa de modelo para 2026: **12,1 %** (superada).
   - Tipo de cambio informal jun-2026: **550 → 648**; oficial Segmento III: 502,6 → 554,3.
   - **Aumento salarial desde julio 2026** en el sector presupuestado (1,2 millones de trabajadores).
   - Limitación metodológica propia del ONEI: las ponderaciones del IPC siguen el patrón de 2010.
   *Pendiente: título exacto, fecha y URL del artículo.*

8. **EFE / Swissinfo** (10 nov, **año a confirmar: 2025**) — parte desde La Habana
   sobre el IPC de octubre (datos ONEI) y estimación de Pavel Vidal.
   Aporta (`data/raw/inflacion_cuba.csv`, `ipc_mensual_cuba.csv`):
   - Serie anual oficial: **2021 77,3 % | 2022 39,07 % | 2023 31,34 % | 2024 24,88 %**.
   - IPC de oct-2025: interanual 15,41 %, mensual 0,96 %, acumulada 11,94 %;
     en oct-2024 había sido 28,09 %.
   - Pavel Vidal: la **inflación real de 2025 "rondaría el 70 %"** si se incluye el
     mercado informal (el IPC oficial solo mide el mercado formal).
   - PIB: −1,1 % en 2024; caída acumulada de 11 % en cinco años.
   *Pendiente: confirmar el año de publicación para citarlo correctamente.*

## Cómo citar en el informe

```
Apellido, Nombre (fecha). Título. Publicación. URL.
```

Regla del proyecto: **sin fuente completa, el dato no entra en la conclusión.**
