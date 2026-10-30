# Informe de calidad del dato · reservas_sucio.csv

**Equipo:** … · **Fecha:** … · **Versión de los datos:** reservas_sucio.csv (nº de filas: …, columnas: …)

## 1. Resumen para el gerente (máx. 5 líneas)
¿Se puede confiar en el fichero? ¿Qué fracción de las filas necesita corrección? ¿Qué es lo más grave?

## 2. Tabla de defectos

| Nº | Defecto | Columna(s) | Filas afectadas | Cómo lo detectamos | Causa probable | Tratamiento aplicado | Por qué (y riesgo) |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| … | | | | | | | |

Categorías de defecto a revisar: duplicados · tipos incorrectos · formatos de fecha · categorías inconsistentes · valores imposibles · *outliers* · nulos · incoherencias entre columnas.

## 3. Antes y después
Tabla con filas, duplicados, nulos por columna y nº de categorías, antes y después de la limpieza.

## 4. Pipeline y modelo de referencia
- Columnas numéricas y categóricas, y tratamiento de cada una.
- Qué se hace **dentro** del pipeline (y por qué) y qué se hace **antes** (reglas fijas).
- Baseline frente a modelo: métrica, validación cruzada (media ± desviación).

## 5. Preguntas para el cliente
Al menos 3 (p. ej.: ¿por qué hay precios con coma?, ¿el 0 en precio significa "gratis" o "sin dato"?, ¿qué hace el sistema con el país cuando reserva una agencia?).

## 6. IA responsable
Riesgos específicos de este dataset (p. ej., uso del país de origen, imputaciones que puedan sesgar) y medidas que hemos aplicado.

## 7. Cómo reproducirlo
Versión de Python y librerías, orden de ejecución, ficheros.

## Revisión con la rúbrica
<Rúbrica completa en la ficha del reto, apartado 3. Rellena quien revisa y **no escribió esa parte**: ejecutar el cuaderno con «Reiniciar y ejecutar todo» siguiendo solo el README, leer el informe como el gerente, mirar el código (¿algún `fit` usa el test?), poner nivel con prueba.>

**Revisado por:** <nombre> · **Fecha:** <dd/mm/aaaa>

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
|---|---|---|
| Corrección técnica | <1–4> | <p. ej. «el cuaderno corre entero y el pipeline se ajusta solo con train, pero falta el docstring de `limpiar_reservas`»> |
| Reproducibilidad | <1–4> | <¿obtienes las mismas cifras siguiendo solo el README? ¿están las versiones?> |
| Análisis y comunicación al cliente | <1–4> | <¿se entiende qué está mal, cuántas filas afecta y qué se ha hecho con cada defecto?> |
| IA responsable | <1–4> | <¿responde con ejemplos a la pregunta del país de origen y dice qué se pidió a la IA y qué se revisó?> |

**Lo primero que mejoraríamos:** <una cosa concreta>
