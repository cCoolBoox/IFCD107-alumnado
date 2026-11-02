# Sprint 3 · Reto «Primer modelo en producción» · en una página

> Versión corta para **trabajar con ella abierta**. La ficha completa (qué pide el cliente, recursos, uso de la IA y errores frecuentes) sigue en [Reto_Sprint_03.md](../3_Consultar/Reto_Sprint_03.md) y cada paso, explicado, en su propio archivo (enlaces tras el reparto de minutos). Qué se sube y la rúbrica: [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md). Se trabaja con el [cuaderno del laboratorio](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S03/2_Practica/laboratorio_automl/S3.5_lab_autogluon.ipynb) y la plantilla del informe en [`plantillas/`](plantillas/).

- **El cliente.**
    - TurisData pierde dinero cuando una reserva se cancela a última hora y la habitación se queda vacía.
    - Quiere un modelo que avise de las reservas con más riesgo de cancelarse y que su equipo consulte desde otra aplicación.
    - Os da 6.000 reservas sintéticas.
- **Qué entregáis (no cambia):**
    - Un único informe de 4 páginas como máximo: el mejor modelo con su umbral y sus costes, la llamada a la API y los recursos con la prueba de cierre.
    - Los riesgos de IA responsable y una recomendación al cliente.
    - Al final se suben a `sprint-03/` del repositorio del equipo (lista completa en «Antes de entregar»).
- **Tiempo en clase:**
    - Planning: 10 min (día 1).
    - Día 2: laboratorio de AutoML, 35 min; reto, 80 min; entrega, review y retro, 40 min.
    - Lo que no quepa, a casa esa tarde.

## Tres niveles: el equipo decide hasta dónde llega

| Nivel | Qué hay que tener | Nota* |
|---|---|---|
| 🟢 **Mínimo** (todos los equipos) | Frase del problema y variable objetivo · tres modelos con su `score_test` y la métrica elegida · **vuestros** importes y umbral · petición y respuesta de la API · tabla de recursos · un riesgo citado | 2 |
| 🟡 **Estándar** | Partición por fecha y 18 columnas razonadas · umbral comparado con «avisar a todos» y «no avisar nunca» · frase para un directivo · ajustes para repetirlo · captura de cierre · **2 o más riesgos con medida** y recomendación · 4 páginas · revisión con la rúbrica | 3 |
| 🔴 **Extra** | Más modelos o ajustes comparados · prueba con datos imposibles (código 422) · cuaderno en el repositorio · beneficio en euros · sesgo comprobado con datos | 4 |

\*Orientativo; puntúa el docente con la rúbrica del reto (0–4 en cada criterio). El mínimo es una entrega válida y evaluable.

## Reparto sugerido (80 minutos de reto + 40 de entrega)

| Min | Qué | Se sabe que está hecho cuando… |
|---|---|---|
| 10 | Paso 1: problema y datos (SQL por canal, 18 columnas) | Frase del cliente, % por canal y columnas razonadas |
| 10 | Paso 2: comparar modelos y ver qué pesa | Mejor modelo con su `score_test`, métrica y ajustes anotados |
| 25 | Paso 3: elegir el umbral con vuestros costes | Importes con su razón, umbral elegido y frase para el directivo |
| 10 | Paso 4: publicar el servicio y hacer una llamada | Respuesta con vuestro umbral guardada (extra: la prueba del 422) |
| 10 | Paso 5: cerrar y borrar | Tabla de recursos y `captura_cierre.png` |
| 15 | Paso 6: redactar el informe | Siete apartados rellenos |
| 40 | Entrega: revisión con la rúbrica, review (demo de 5 min con la llamada en directo) y retro | Todo subido y revisión anotada |

**Cada paso, explicado al detalle:** [Paso 1](../3_Consultar/Reto_Sprint_03_paso_1.md) · [Paso 2](../3_Consultar/Reto_Sprint_03_paso_2.md) · [Paso 3](../3_Consultar/Reto_Sprint_03_paso_3.md) · [Paso 4](../3_Consultar/Reto_Sprint_03_paso_4.md) · [Paso 5](../3_Consultar/Reto_Sprint_03_paso_5.md) · [Paso 6](../3_Consultar/Reto_Sprint_03_paso_6.md)

## Frases para el informe (completad los huecos)

- «Queremos predecir ___ para que el equipo de reservas pueda ___.»
- «Recomendamos alertar cuando el riesgo supere el ___ %: detectamos ___ de cada 10 cancelaciones, aunque ___ de cada 10 alertas serán falsas.»
- «Con una no prevista valorada en ___ € y una falsa en ___ €, el coste baja a ___ €, frente a ___ € si avisamos a todos y ___ € si no avisamos nunca.»
- «Un riesgo es ___ y lo mitigamos con ___ . Ante una alerta, una persona ___ antes de actuar: la alerta no cambia nada sola.»

## Antes de entregar
- **Archivos subidos en `sprint-03/`:** `informe_modelo.md` · `captura_cierre.png` · `autoevaluacion_nombre.md` (**uno por persona**) = 2 + N ficheros
- [ ] Las tres partes caben en 4 páginas y no queda ningún `______` · [ ] Importes vuestros y umbral comparado con las dos referencias
- [ ] Petición y respuesta de la API, sin claves · [ ] Recursos cerrados y `captura_cierre.png` sin datos personales
- [ ] 2 o más riesgos con medida y una recomendación · [ ] «Revisión con la rúbrica» rellena al final del informe
- [ ] [Autoevaluación y coevaluación](../2_Entregar/autoevaluacion_y_coevaluacion.md): **una por persona**, subida a `sprint-03/`
