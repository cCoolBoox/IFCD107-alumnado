# Sprint 12 · Reto «Escuchar al cliente» · Equipo de ejemplo «Las Palmeras»

Entrega de referencia del docente: sirve de modelo de lo que hay que subir a `sprint-12/`. Es una forma correcta de hacerlo, no la única. Para ver qué se pide, [entrega y rúbrica](../../3_Reto/2_Entregar/entrega_y_rubrica.md).

## Cómo ejecutar todo (cinco líneas)
1. Los datos del curso van a `data/` (`resenas.csv`, `ocupacion_diaria.csv`, `politica_alojamiento.md`, `preguntas_referencia.csv`); si faltan, la primera celda de cada cuaderno los descarga.
2. Abrir y ejecutar **en este orden**, cada uno con *Entorno de ejecución → Reiniciar y ejecutar todo* (menos de un minuto cada uno): `resenas.ipynb`, `ocupacion.ipynb`, `asistente_rag.ipynb`. Con los datos presentes no hace falta internet y no hay ninguna clave.
3. `resenas.ipynb` guarda `grafico_resenas.png` y `asistente_rag.ipynb` guarda `evaluacion_asistente.csv`; el informe y la nota usan sus cifras.
4. Debe salir: exactitud de prueba **0,992**; MAE a 7 días **3,18** (SARIMAX) frente a **4,45** (mejor *baseline*) y 4,21 (GRU); asistente con **24 aciertos de 25**, 0 alucinaciones, y 3 ataques que prosperan sin defensa y ninguno con el filtro.
5. Semilla `SEMILLA = 42` (la GRU usa 42, 43 y 44). Versiones: Python 3.13.18, numpy 2.5.3, pandas 2.3.3, statsmodels 0.15.0, tensorflow 2.21.0; scikit-learn 1.9.1.

## Qué se entrega
[`informe_resenas.md`](informe_resenas.md) · [`grafico_resenas.png`](grafico_resenas.png) · [`resenas.ipynb`](resenas.ipynb) · [`ocupacion.ipynb`](ocupacion.ipynb) · [`asistente_rag.ipynb`](asistente_rag.ipynb) · [`evaluacion_asistente.csv`](evaluacion_asistente.csv) · [`nota_ia_responsable.md`](nota_ia_responsable.md) · `LEEME.md` (este fichero) · [`autoevaluacion_marta.md`](autoevaluacion_marta.md) (la hoja de **una** persona; cada persona del equipo sube la suya). Un equipo de cuatro personas sube **8 + 4 = 12** ficheros.

## Quién hizo qué (reparto de ejemplo)
- Persona A: `resenas.ipynb`, gráfico y temas.
- Persona B: `ocupacion.ipynb` (*baselines*, SARIMAX, GRU y previsión).
- Persona C: `asistente_rag.ipynb`, evaluación y ataques.
- Persona D: informe, nota de IA responsable, este `LEEME.md` y la revisión con la rúbrica.

## Uso de IA
- **Qué se pidió:** explicar qué es SARIMAX y la estacionalidad semanal; un primer borrador de las frases del filtro; revisar la redacción del informe.
- **Qué se revisó:** cada cifra del informe y de la nota es la de la última ejecución completa de los cuadernos; el escalado de la GRU se ajusta solo con el entrenamiento; los datos son sintéticos y no hay claves ni datos personales.
- **Qué se cambió:** la IA sugirió un umbral de 0,5 para el asistente; al medirlo, solo acertaba 14 de 25 y se descartó por 0,15.

## Revisión con la rúbrica

**Revisado por:** Persona D (no escribió esa parte) · **Fecha:** 25/11/2026

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
|---|---|---|
| Corrección técnica | 4 | El MAE del modelo (3,18) y el del mejor *baseline* (4,45) están en la misma tabla, junto a SARIMAX frente a GRU (4,21) y cinco umbrales; exactitud 0,992 con matriz; 25 preguntas evaluadas que suman 25; 3 ataques probados |
| Reproducibilidad | 3 | Reiniciar y ejecutar todo con este LEEME dio los mismos números en los tres cuadernos; en Colab la GRU puede cambiar en el último decimal (otras versiones de TensorFlow), por eso no llega al 4 |
| Análisis y comunicación al cliente | 4 | Informe de 2 páginas que se entiende sin programar; 3 recomendaciones con qué, quién y cómo sabremos; temas criticados y valorados con cifras y ejemplos; cada recomendación apoyada en una cifra; falta el coste en euros de un mal turno |
| IA responsable | 4 | Cada riesgo tiene su medida y la medida se mide («bloqueó 3 de 3 ataques y 0 de las 25 preguntas legítimas»); la nota dice qué no cubre y que el generador es simulado |

**Lo primero que mejoraríamos:** arreglar el empate de la recuperación del desayuno, repetir los 3 ataques con otras formulaciones y probar el asistente con un modelo de lenguaje real.
