# Sprint 10 · Reto «¿Vale la pena la red?» · Equipo de ejemplo

Entrega de referencia del docente: sirve de modelo de lo que hay que subir a `sprint-10/`. Es una forma correcta de hacerlo, no la única. Para ver qué se pide, [entrega y rúbrica](../../3_Reto/2_Entregar/entrega_y_rubrica.md).

## Qué se entrega
- [`reto_vale_la_pena.ipynb`](reto_vale_la_pena.ipynb): el cuaderno, ejecutado de arriba abajo: partición única, boosting de referencia, MLP con tres semillas, tres variantes (elegidas con la validación), curvas, prueba una sola vez, *bootstrap* y aviso por canal.
- [`informe_comparativo.md`](informe_comparativo.md): el informe de 1–2 páginas, con la recomendación en la primera frase y la «Revisión con la rúbrica».
- [`curvas_aprendizaje.png`](curvas_aprendizaje.png): la figura de las curvas, que genera el cuaderno y el informe enlaza (opcional).
- `README.md`: este fichero.
- [`autoevaluacion_marta.md`](autoevaluacion_marta.md): la hoja de **una** persona (cada persona del equipo sube la suya).

El CSV no va a `sprint-10/`: el cuaderno lo descarga solo. Un equipo de cuatro personas sube **3 + 4 = 7** ficheros.

## Quién hizo qué (reparto de ejemplo)
- Persona A: partición, función `evaluar`, boosting y tabla de prueba.
- Persona B: MLP con tres semillas, variantes y curvas con el diagnóstico.
- Persona C: *bootstrap*, aviso por canal y cifras del informe.
- Persona D: informe, README y revisión con la rúbrica.

## Cómo se repite
1. Abrir `reto_vale_la_pena.ipynb` en Google Colab (*Archivo → Subir cuaderno*).
2. *Entorno de ejecución → Reiniciar y ejecutar todo* (unos dos minutos). La primera celda descarga `reservas_turisdata.csv` del repositorio del curso.
3. Debe salir el mismo AUC de validación del MLP (0,744 ± 0,001) y la tabla de prueba del informe: boosting 0,738 y MLP 0,744 de AUC.

Versiones: Python 3.13.18, numpy 2.5.3, pandas 2.3.3, scikit-learn 1.9.1, tensorflow 2.21.0. En Colab saldrán otras: el AUC puede variar en el último decimal y los tiempos cambian siempre. Semillas: `SEMILLA = 42` para las particiones y 1, 2 y 3 para las redes.

## Uso de IA
- **Qué se pidió:** explicar el *bootstrap* y por qué un intervalo que contiene el 0 es «empate»; revisar la redacción del informe.
- **Qué se revisó:** las cifras del informe son las de la última ejecución completa; la prueba no se usó para elegir épocas ni variantes; los datos son sintéticos y no hay claves ni datos personales.
- **Qué se cambió:** una frase de la IA decía «la red es mejor»; con un intervalo que incluye el 0 no se puede afirmar.
- (Ejemplo de referencia: cada equipo cuenta lo que hizo de verdad, incluidos los fallos concretos de la IA que detecte.)

## Revisión con la rúbrica
Está al final del [informe](informe_comparativo.md#revisión-con-la-rúbrica).
