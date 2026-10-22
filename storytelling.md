# Storytelling: ¿cuánto cuesta el sol en Cuba?

Archivo narrativo para preparar la exposición. Los números salen de los notebooks
01–03; las cifras se pueden regenerar ejecutándolos.

---

## 1. La pregunta

> Un panel solar promete electricidad en un país con apagones. Pero en Cuba **el
> obstáculo rara vez es la tecnología: es el precio**. Este proyecto mide cuánto
> cuesta el sol, cuánto tarda un trabajador en pagarlo y qué piensa la gente.

Fórmula central:

```
meses de salario = precio del panel (CUP) / salario medio mensual (CUP)
```

---

## 2. Los datos (lo que se puede defender)

| Fuente | Qué aporta | Cantidad |
|---|---|---|
| ONEI | salario medio mensual por año | 10 años (2016–2025) |
| ONEI (nota 14/04/2026) | IPC marzo 2026: +13,42 % interanual | 1 dato |
| TradingEconomics (datos oficiales) | inflación ago/2026: **+25,19 %** interanual, +4,92 % mensual | 2 datos |
| Auditoría en tiendas | precios Copextel, UNE, Correos de Cuba | 4 observaciones |
| Observación de mercado | 10 paneles cotizados en USD | 10 observaciones |
| Encuesta propia | percepción del precio y del acceso | 25 personas |

Sin fuente no hay dato: cada fila del CSV crudo lleva su procedencia.

---

## 3. Acto I — No existe "el precio del panel"

Diez paneles cotizados hoy, convertidos a pesos (1 USD = 815 CUP, cotización de
mercado informada en campo):

| Potencia | Precio USD | Precio CUP | CUP por vatio |
|---|---|---|---|
| 225 W | 100 | 81 500 | 362 |
| 600 W | 135 | 110 025 | 183 |
| 620 W bifacial | 145 | 118 175 | 191 |
| 625 W | 158 | 128 770 | 206 |
| 550 W / 535 W | 180 | 146 700 | 267–274 |
| 500 W | 190 | 154 850 | 310 |
| 580 W | 200 | 163 000 | 281 |
| 615 W | 260 | 211 900 | 345 |

**Hallazgo 1:** el precio por vatio va de **183 a 362 CUP/Wp** (de 0,23 a 0,44
USD/Wp). Un panel "barato" y uno "caro" del mismo tamaño pueden costar el doble.
Comparar precios en bruto, sin dividir entre vatios, no sirve: por eso el
proyecto usa **CUP por vatio** como unidad común.

---

## 4. Acto II — ¿Cuánto cuesta en vidas, no en dinero?

Salario medio mensual: **6 930 CUP (2025, ONEI)**.

| Qué se compra | Precio | Meses de salario |
|---|---|---|
| Módulo oficial UNE 800 W | 75 200 CUP | **10,9 meses** |
| Panel privado 225 W (el más barato) | 81 500 CUP | 11,8 meses |
| Panel privado mediano (180 USD) | 146 700 CUP | **21,2 meses** |
| Panel privado 615 W (el más caro) | 211 900 CUP | 30,6 meses |
| Sistema completo 5 kW | 2 530 000 CUP | 365 meses |

**Hallazgo 2:** el panel del mercado privado cuesta **entre 1,5 y 2,5 años de
salario medio entero**, sin gastar nada en comida, transporte ni aseo.

**Hallazgo 2 bis — el sueldo se mueve para atrás:** la inflación interanual
pasó de **13,42 % en marzo de 2026 a 25,19 % en agosto de 2026**, con los
alimentos subiendo 36,01 %. Si los precios crecen a ese ritmo y el salario no
sigue el paso, **el panel se encarece en términos reales incluso si su precio
en pesos no cambia**. Eso convierte a la "espera" en una mala estrategia.

**Hallazgo 3 (la paradoja):** el módulo oficial de la UNE cuesta **94 CUP/Wp
frente a 270 CUP/Wp del mercado privado: 65 % más barato por vatio**. Pero la
venta es "para trabajadores priorizados": **el precio accesible existe, el
acceso no**. El problema no es solo cuánto cuesta, sino quién puede comprarlo.

> Corrección metodológica: al usar una cotización provisional (240 CUP/USD) la
> comparación salía al revés. Con la cotización de mercado real (815) el orden se
> invierte. Es un ejemplo de por qué **la fuente del tipo de cambio cambia la
> conclusión**.

---

## 5. Acto III — La calle lo confirma

25 encuestas (12 por cuestionario, 13 por audio), muestra de conveniencia en La Habana:

- **44 %** (11/25) dice que **nunca** podría comprarlo; otros 4 dicen 3 años o más.
- **68 %** señala el obstáculo **económico** (precio, dinero o salario); solo 20 % el robo.
- Solo **3 de 23** conocen el precio real del sistema del Estado.
- En los audios el peso del obstáculo económico sube al **85 %**: conversando la gente llega antes al grano.
- Testimonio (E19, Regla): *compré un panel a 360 USD; hoy lo veo entre 150 y 170 USD* → indicio de caída de precios en el mercado privado.

**Triangulación:** el cálculo dice 10,9 meses guardando el **100 %** del salario;
la gente, que no puede ahorrar todo, responde "3-5 años" o "nunca". **Los dos
métodos dicen lo mismo desde ángulos distintos.**

---

## 6. Las cuatro conclusiones

1. **No hay un precio, hay un rango**: 183–362 CUP/Wp según tamaño y vendedor.
2. **En términos humanos el panel cuesta 1,5 a 2,5 años de salario medio**; el kit oficial, 10,9 meses.
3. **El canal oficial es más barato por vatio pero no es libre**: acceso restringido.
4. **La barrera que reporta la población es el ingreso (68 %), no la tecnología.**

---

## 7. Lo que NO se puede decir (limitaciones)

- Muestra no probabilística (n=25, mayoría La Habana): no representa a Cuba.
- Solo hay **3 observaciones de inflación 2026** (marzo, julio, agosto) y **ningún índice anual 2016–2025**: por eso la serie de salarios está en **pesos nominales, sin deflactar**. Es la deuda pendiente del proyecto.
- Solo 2 años con precios de paneles: no hay tendencia histórica aún, solo comparación 2021 vs 2026.
- Cotización de 815 CUP/USD es de mercado, no la tasa oficial: cambia el resultado en CUP (y así se demostró).
- Faltan salario 2026 e IPC anual de 2016–2025.

---

## 8. Preguntas abiertas

- ¿Sigue bajando el precio en USD (150–180 USD) mientras sube el dolar (815)?
- ¿Cuántos de los 25 encuestados podrían comprar si existiera crédito o facición?
- ¿El precio oficial de la UNE se mantiene si crece la demanda?

---

## 9. Guion de 90 segundos para exponer

1. **Gancho:** "Les voy a decir cuánto cuesta el sol: entre 10 y 30 meses de salario."
2. **Problema:** en Cuba el panel no se lo compra quien lo quiere, se lo compra quien puede.
3. **Método:** salarios ONEI + 14 precios levantados en campo + 25 encuestas.
4. **Dato 1:** precio por vatio varía ×2 (183 vs 362 CUP/Wp) → importa comparar bien.
5. **Dato 2:** el oficial es 65 % más barato por vatio, pero solo para priorizados.
6. **Dato 3:** 44 % dice "nunca podría"; 68 % culpa al dinero.
7. **Cierre:** la energía solar en Cuba es un problema de precios e ingresos, no de ciencia.
