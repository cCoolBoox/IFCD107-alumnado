# Sprint 7 · Reto «Precio y cancelación» · Equipo de ejemplo

Entrega de referencia del docente: sirve de modelo de lo que hay que subir a `sprint-07/`. Es una forma correcta de hacerlo, no la única. Para ver las respuestas paso a paso, el [solucionario del reto](../Solucionario_reto.md); para ver qué se pide, [entrega y rúbrica](../../2_Entregar/entrega_y_rubrica.md).

## Qué se entrega
- [`reto_S07.ipynb`](reto_S07.ipynb): el cuaderno, ejecutado de arriba abajo. Un modelo de **precio** y otro de **cancelación**, cada uno con su *baseline*, métricas, umbral, sensibilidad y un k-NN extra.
- [`informe_modelado.md`](informe_modelado.md): el informe para el gerente, con euros, las hipótesis de coste y la «Revisión con la rúbrica» al final.
- `README.md`: este fichero.
- [`autoevaluacion_marta.md`](autoevaluacion_marta.md): la hoja de **una** persona (cada persona del equipo sube la suya).
- `reservas_turisdata.csv` (datos): ya está en el repositorio del curso; en `data/` del equipo solo si aún no está, sin cambios.

Un equipo de tres personas sube **3 + 3 = 6** ficheros.

## Cómo se reproduce
1. Abrir `reto_S07.ipynb` en Google Colab (*Archivo → Subir cuaderno*).
2. *Entorno de ejecución → Reiniciar y ejecutar todo*. La primera celda descarga `reservas_turisdata.csv` del repositorio del curso si no está.
3. Cifras de control: 6000 filas · precio: MAE **7,24 €**, RMSE 9,70 €, R² 0,915 · umbral **0,25** · coste en test **58 331 €** frente a 156 484 € sin modelo · AUC 0,746.

Versiones: Python 3.13, scikit-learn 1.9.1, pandas 2.3.3, numpy 2.5.3 (en Colab saldrán otras; las cifras pueden variar en el último decimal). Semilla: `SEMILLA = 42`. Solo librerías del curso.

## Quién hizo qué
- Persona A: precio por noche (*baseline*, lineal, interacciones y coeficientes en euros).
- Persona B: cancelación, umbral con validación cruzada, sensibilidad y curvas.
- Persona C: informe, README, revisión con la rúbrica y subida a GitHub.
- (Reparto de ejemplo; cada equipo pone sus nombres.)

## Uso de la IA
- **Qué se pidió:** explicar qué es un *odds ratio*; entender el error de un `KeyError` al crear las variables; revisar si el resumen para el gerente se entiende sin saber qué es el AUC.
- **Qué se revisó:** cada línea se ejecutó y se entiende; las cifras del informe salen del cuaderno, no de la IA; **los costes (284 € y 103 €) y el umbral los decidió el equipo**, con su razón escrita.
- **Qué se cambió:** la IA propuso elegir el umbral mirando el test; se descartó, porque el test se usa una sola vez y el umbral sale de la validación cruzada sobre *train*. Los datos son sintéticos: no hay datos personales ni claves.
- (Ejemplo de referencia: cada equipo cuenta lo que hizo de verdad, incluidos los fallos concretos de la IA que detecte.)
