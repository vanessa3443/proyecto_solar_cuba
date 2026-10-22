# Encuesta: mercado de paneles solares en Cuba

Plantilla para levantar datos hoy. **No escribas en el CSV mientras hablas**:
graba el audio, transcribe después y luego pasamos las respuestas a filas.

## Datos de la entrevista (al principio)

| Campo | Valor |
|---|---|
| Fecha | |
| Lugar (municipio/provincia) | |
| Perfil del encuestado | trabajador / técnico / vendedor / usuario / otro |
| ID anónimo | E01, E02, E03... (**nunca nombres completos**) |

## Preguntas

1. ¿Tiene usted hoy algún sistema solar? ¿Sí / No / En instalación?
2. ¿Qué tiene exactamente? (panel suelto, sistema con inversor, con batería, etc.)
3. ¿De cuántos vatios (W) o cuántos kW es?
4. ¿En qué año lo compró y **cuánto le costó** (CUP)?
5. ¿A quién se lo compró? (tienda, Copextel, UNE, Correos de Cuba, conocido, mercado privado)
6. ¿Tuvo que hacer fila, permiso o trámite para comprarlo?
7. ¿Qué le faltó o qué tuvo que comprar aparte? (batería, cable, instalación)
8. ¿Cuánto le han cotizado **ahora** el mismo sistema o uno parecido?
9. ¿Qué le parece el precio: justo, caro, inasequible? ¿Cuánto debería costar?
10. ¿Cuánto le ahorra al mes o qué aparatos le mueve? (opcional)
11. ¿Conoce a alguien que haya comprado uno recientemente? ¿A qué precio?

## Reglas

- **Pregunta 10 es opcional**: no insistas si no quiere decirlo.
- **Sin nombres**: usa el ID E01, E02... El nombre solo si da permiso expreso y es para la ficha, nunca para el CSV.
- Anota siempre **año + precio + potencia**: sin esos tres datos el caso no sirve.
- Si da el precio en USD, apunta USD **y** el tipo de cambio que mencione.
- Graba con permiso de la persona. Si dice no, solo apuntas sus respuestas.

## Qué hacer al llegar

1. Transcribe los audios a texto.
2. Pega los textos aquí: `data/raw/encuestas_paneles.csv` (columna `transcripcion`).
3. Pásame los casos con `año + precio + potencia` y los convierto en filas de `precios_paneles.csv`.
