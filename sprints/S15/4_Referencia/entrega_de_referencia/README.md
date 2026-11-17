# Sprint 15 · Reto «El mejor modelo, demostrado» · Equipo de ejemplo

Entrega de referencia del docente: sirve de modelo de lo que hay que subir a `sprint-15/`. Es una forma correcta de hacerlo, no la única. Para ver qué se pide, [entrega y rúbrica](../../3_Reto/2_Entregar/entrega_y_rubrica.md).

Proyecto del equipo de ejemplo: **BiciPrevisión** (prever las bicis alquiladas en cada hora de mañana; datos de la UCI, CC BY 4.0). Parte de la ficha, el plan de datos y el *baseline* del [Sprint 14](../../../S14/4_Referencia/entrega_de_referencia/README.md).

## Qué se entrega
- [`03_modelos.ipynb`](03_modelos.ipynb): el cuaderno, ejecutado de arriba abajo, con el registro, la partición, los modelos, la comprobación de fugas, la elección, el test (una vez), el guardado y la explicación.
- [`registro.csv`](registro.csv): una fila por prueba (18 filas, de las cuatro personas, con el *baseline* en la primera).
- [`justificacion_candidato.md`](justificacion_candidato.md): la página con la tabla comparativa, el candidato razonado, el test, la explicación, el uso de IA y la «Revisión con la rúbrica».
- [`modelo_candidato.joblib`](modelo_candidato.joblib) y [`metadatos.json`](metadatos.json): el modelo y sus datos (versión, fecha, métricas, variables). Los genera el cuaderno.
- [`explicacion_modelo.png`](explicacion_modelo.png): importancia de variables por permutación. La genera el cuaderno.
- `README.md`: este fichero.
- [`autoevaluacion_marta.md`](autoevaluacion_marta.md): la hoja de **una** persona (cada persona sube la suya).

Un equipo de cuatro personas sube **6 + 4 = 10** ficheros (más el README del repositorio, que se actualiza).

## Quién hizo qué (reparto de ejemplo)
- Marta (responsable técnica): parte común, *baselines*, boosting con y sin clima, test y guardado.
- Persona B: red neuronal con 3 semillas y la validación barajada que propuso la IA.
- Persona C: ajuste de hiperparámetros, fuga a propósito y prueba del clima con error.
- Persona D: regresión lineal, bosque, repetición de una prueba de Marta y revisión con la rúbrica.

## Cómo se repite
1. Abrir `03_modelos.ipynb` en Google Colab (*Archivo → Subir cuaderno*) con `bicis_horas.csv` junto al cuaderno o en `datos/` (si no está, la primera celda lo descarga).
2. *Entorno de ejecución → Reiniciar y ejecutar todo* (unos 3 minutos). El registro se rehace entero.
3. Deben salir los mismos MAE: el candidato `HGB_prof6` con **40,6 ± 6,8** en validación cruzada, **42,2** en sep–oct y **44,0** en test. Los tiempos de la columna `tiempo_s` cambian de un ordenador a otro, y las fechas del registro están fijadas en el ejemplo.

Versiones: Python 3.13.18, numpy 2.5.3, pandas 2.3.3, scikit-learn 1.9.1. Semilla: `SEMILLA = 42`. Huella de los datos: `95d6bcad`.

## Uso de IA
- **Qué se pidió:** el código de la red neuronal, de la validación cruzada y de la importancia por permutación (marcado en `notas` del registro).
- **Qué se revisó:** cada línea; las cifras de la justificación son las de la celda «Cifras para la justificación»; no hay claves ni datos personales.
- **Qué se cambió:** la validación de la IA barajaba las horas y daba un error de 26,7, demasiado bueno; se sustituyó por bloques temporales y la prueba quedó en el registro como «NO CANDIDATO».
- (Ejemplo de referencia: cada equipo cuenta lo que hizo de verdad, incluidos los fallos concretos de la IA que detecte.)

## Revisión con la rúbrica
Está al final de [`justificacion_candidato.md`](justificacion_candidato.md), hecha por Persona D el 03/12/2026: 4 / 4 / 3 / 4.
