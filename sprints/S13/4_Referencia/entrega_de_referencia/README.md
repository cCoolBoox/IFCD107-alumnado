# Sprint 13 · Reto «Informe visual para dirección» · Equipo de ejemplo

Entrega de referencia del docente: sirve de modelo de lo que hay que dejar en `sprint-13/`. Es una forma correcta de hacerlo, no la única. Para ver qué se pide, [entrega y rúbrica](../../3_Reto/2_Entregar/entrega_y_rubrica.md).

## Qué se entrega
- [`informe_visual.md`](informe_visual.md): la página para dirección, con el titular-decisión en la primera línea, el panel, tres viñetas, la IA responsable, el pie y la «Revisión con la rúbrica».
- [`informe_visual_panel.png`](informe_visual_panel.png): el panel de cuatro gráficos, que genera el cuaderno (no se edita a mano) y el informe enlaza.
- [`informe_visual.ipynb`](informe_visual.ipynb): el cuaderno, ejecutado de arriba abajo, a partir de la plantilla del curso: modelo elegido, costes de los errores, test, panel y cifras del informe.
- `README.md`: este fichero (el `README.md` de `sprint-13/`, que ya existe en el repositorio del equipo: se rellena, no se sube aparte).
- [`autoevaluacion_marta.md`](autoevaluacion_marta.md): la hoja de **una** persona (cada persona del equipo sube la suya).

El CSV no va a `sprint-13/`: el cuaderno lo descarga solo. Un equipo de cuatro personas sube **3 + 4 = 7** ficheros.

## Quién hizo qué (reparto de ejemplo)
- Persona A: carga del modelo, costes de los errores y umbral en el cuaderno.
- Persona B: los cuatro gráficos y sus títulos-conclusión.
- Persona C: cifras del informe, comparación de umbrales y modelos, y mirada por canal y por país.
- Persona D: informe, README y revisión con la rúbrica.

## Cómo se repite
1. Abrir `informe_visual.ipynb` en Google Colab (*Archivo → Subir cuaderno*).
2. *Entorno de ejecución → Reiniciar y ejecutar todo*. La primera celda descarga `reservas_turisdata.csv` del repositorio del curso.
3. Debe salir el mismo panel y las mismas cifras del informe: AUC 0,74, umbral 0,35 y un ahorro de 16.590 € por cada 1.500 reservas del test.

Versiones: Python 3.13.18, numpy 2.5.3, pandas 2.3.3, scikit-learn 1.9.1, matplotlib 3.11.2, seaborn 0.13.2. En Colab saldrán otras: las cifras pueden variar en el último decimal. Semilla: `SEMILLA = 42`.

## Uso de IA
- **Qué se pidió:** explicar la importancia por permutación y revisar la redacción de los títulos.
- **Qué se revisó:** cada cifra sale de las variables del cuaderno y todo se calcula con el test; los datos son sintéticos y no hay claves ni datos personales.
- **Qué se cambió:** un título de la IA decía «el depósito evita las cancelaciones»; el gráfico muestra lo que pesa en el modelo, no la causa.
- (Ejemplo de referencia: cada equipo cuenta lo que hizo de verdad, incluidos los fallos concretos de la IA que detecte.)

## Revisión con la rúbrica
Está al final del [informe](informe_visual.md#revisión-con-la-rúbrica).
