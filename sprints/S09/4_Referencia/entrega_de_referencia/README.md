# Sprint 9 · Reto «Conocer al huésped» · Equipo de ejemplo

Entrega de referencia del docente: sirve de modelo de lo que hay que subir a `sprint-09/`. Es una forma correcta de hacerlo, no la única. Para ver qué se pide, [entrega y rúbrica](../../3_Reto/2_Entregar/entrega_y_rubrica.md); para los pasos, [la ficha del reto](../../3_Reto/3_Consultar/Reto_Sprint_09.md).

## Qué se entrega
- [`reto_S09_conocer_al_huesped.ipynb`](reto_S09_conocer_al_huesped.ipynb): el cuaderno, ejecutado de arriba abajo. Segmentación con k-means, mapa PCA, recomendador comparado y la declaración del uso de la IA.
- [`ficha_segmentos.md`](ficha_segmentos.md): la ficha para Lucía, con los cuatro segmentos, el recomendador, la nota de IA responsable y la «Revisión con la rúbrica».
- [`mapa_pca.png`](mapa_pca.png): el mapa, que genera el cuaderno y la ficha enlaza.
- [`autoevaluacion_marta.md`](autoevaluacion_marta.md): la hoja de **una** persona (cada persona del equipo sube la suya).
- `README.md`: este fichero (no se sube: es la explicación de la carpeta).

Los datos no se suben: ya están en el repositorio del curso. Un equipo de tres personas sube **2 + 3 = 5** ficheros (más el mapa, si lo pone en la ficha).

## Quién hizo qué (reparto de ejemplo)
- Persona A: preparación de datos, silueta y elección de `k`.
- Persona B: mapa PCA, perfiles y mapa de calor.
- Persona C: nombres, acciones, ficha y nota de IA responsable.
- Persona D: recomendador y `recomendar`; revisó la ficha con la rúbrica.

## Cómo se reproduce
1. Abrir `reto_S09_conocer_al_huesped.ipynb` en Google Colab (*Archivo → Subir cuaderno*).
2. *Entorno de ejecución → Reiniciar y ejecutar todo* (tarda menos de un minuto). La primera celda descarga los datos.
3. Debe salir `k = 4` con silueta 0,431, los tamaños 194, 402, 317, 287 y la tabla RMSE / precision@3 de la ficha.

Versiones con las que se ejecutó: Python 3.13.18, numpy 2.5.3, pandas 2.3.3, scikit-learn 1.9.1. En Colab saldrán otras: los números de grupo pueden permutarse y las cifras cambiar en el último decimal (por eso los nombres se ponen mirando el perfil).
