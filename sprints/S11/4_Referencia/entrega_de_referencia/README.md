# Sprint 11 · Reto «Visión artificial para el cliente» · Equipo de ejemplo

Entrega de referencia del docente: sirve de modelo de lo que hay que subir a `sprint-11/`. Es una forma correcta de hacerlo, no la única. Para ver qué se pide, [entrega y rúbrica](../../3_Reto/2_Entregar/entrega_y_rubrica.md).

## Qué se entrega
- [`reto_vision_cliente.ipynb`](reto_vision_cliente.ipynb): el cuaderno, ejecutado de arriba abajo, con el modelo, la evaluación, la lista de errores, el umbral y el demostrador `clasificar_foto`.
- [`analisis_errores.md`](analisis_errores.md): el informe de 1–2 páginas con los seis apartados.
- [`errores_prueba.png`](errores_prueba.png): la figura de los errores, que genera el cuaderno y el informe enlaza.
- `README.md`: este fichero.
- [`autoevaluacion_marta.md`](autoevaluacion_marta.md): la hoja de **una** persona (cada persona del equipo sube la suya).

No se suben las imágenes (el cuaderno las genera) ni el modelo `.keras` (el cuaderno lo reproduce). Un equipo de tres personas sube **3 + 3 = 6** ficheros.

## Quién hizo qué (reparto de ejemplo)
- Persona A: conjunto de datos, partición y modelo con *transfer learning*.
- Persona B: referencia «desde cero», métricas por clase y matriz de confusión.
- Persona C: errores, umbral y demostrador.
- Persona D: informe, README y revisión con la rúbrica.

## De dónde salen las fotos
Del conjunto **sintético** del curso: dibujos esquemáticos generados por el script del curso (`generar_dataset_sintetico.py`, que el cuaderno ya incluye), con 60 imágenes por clase. **No son fotos reales** y no hay personas, autores ni licencias que citar. Si un equipo usa fotos propias, aquí apunta de dónde salen, quién las hizo y con qué licencia.

## Cómo se repite
1. Abrir `reto_vision_cliente.ipynb` en Google Colab (*Archivo → Subir cuaderno*).
2. *Entorno de ejecución → Reiniciar y ejecutar todo* (unos minutos). El cuaderno crea las imágenes, entrena y evalúa.
3. Debe salir la misma exactitud en prueba (transfer + fine-tuning 0,750, desde cero 0,683) y los mismos 15 errores.

Versiones: Python 3.13.18, numpy 2.5.3, scikit-learn 1.9.1, tensorflow 2.21.0. En Colab saldrán otras y las cifras pueden variar en el último decimal. Semilla: `SEMILLA = 42`.

## Uso de IA
- **Qué se pidió:** explicar qué es el *fine-tuning* y proponer hipótesis para los errores.
- **Qué se revisó:** cada hipótesis se comprobó mirando la foto (la IA propuso «iluminación», que en dibujos no tiene sentido); las cifras del informe son las de la celda «Cifras para el informe»; no hay claves ni datos personales.
- **Qué se cambió:** se descartaron las hipótesis que no se veían en la foto y se añadió que las etiquetas pueden estar mal.
- (Ejemplo de referencia: cada equipo cuenta lo que hizo de verdad, incluidos los fallos concretos de la IA que detecte.)

## Revisión con la rúbrica

**Revisado por:** Persona D (no escribió el informe) · **Fecha:** 20/11/2026

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
|---|---|---|
| Corrección técnica | 3 | Se ejecuta entero con SEMILLA = 42; transfer congelado + ajuste fino frente a «desde cero»; la prueba se mira una vez; el umbral se eligió con la validación; `clasificar_foto` devuelve «revisar a mano» con confianza baja |
| Reproducibilidad | 3 | Reiniciar y ejecutar todo dio la misma exactitud en prueba (transfer 0,750, desde cero 0,683) y los mismos 15 errores; el README dice cómo se generan las imágenes |
| Análisis y comunicación al cliente | 3 | El informe dice que 8 de los 10 errores más seguros parecen etiquetas mal puestas y recomienda revisarlas antes de fiarse de las cifras; falta probar la mejora |
| IA responsable | 3 | Tres riesgos de este caso con medida (etiquetas dudosas, dibujos que no son fotos, fotos reales con personas y licencias); el README dice qué se pidió a la IA y qué se comprobó |

**Lo primero que mejoraríamos:** Corregir las etiquetas dudosas y volver a medir, para ver cuánto del error era del modelo y cuánto de las etiquetas.
