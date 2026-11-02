# Sprint 15 · Reto «El mejor modelo, demostrado» · en una página

> Versión corta para **trabajar con ella abierta**. La ficha completa (qué pide el cliente, recursos, uso de la IA y errores frecuentes) sigue en [Reto_Sprint_15.md](../3_Consultar/Reto_Sprint_15.md) y cada paso, explicado, en su propio archivo (enlaces tras el reparto de minutos); la plantilla del registro está en [`registro_experimentos_plantilla.csv`](plantillas/registro_experimentos_plantilla.csv). **Probad antes la [demo interactiva](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S15/3_Reto/1_Trabajar/S15_demo_reto.html)** (una página, sin instalar nada).

- **El cliente.**
    - El docente quiere saber **qué modelo recomendáis y por qué**, no solo cuál tiene el número más alto.
    - Quiere saber:
        - Si la mejora frente al *baseline* compensa el coste.
        - Si el modelo funciona con datos nuevos.
        - Si se puede repetir.
- **Qué entregáis (no cambia):**
    - El registro de experimentos.
    - El cuaderno `03_modelos.ipynb`.
    - La justificación de una página del candidato.
    - El modelo guardado con sus metadatos y una primera explicación del modelo.
    - Al final se suben a `sprint-15/` del repositorio del equipo (lista completa en «Antes de entregar»).
- **Tiempo en clase:**
    - Reto: 470 min (130 el día 1, 200 el día 2 y 140 el día 3) + 50 min diarios para subir de nivel (jornadas de 6 h).
    - Review y retro: 60 min. El test se usa **una sola vez**.

## Tres niveles: el equipo decide hasta dónde llega

| Nivel | Qué hay que tener | Nota* |
|---|---|---|
| 🟢 **Mínimo** (todos los equipos) | Una misma partición para todos · *baseline* en la primera fila del registro y 3 modelos con media ± desviación · una fila de cada persona · candidato elegido **sin mirar el test** y justificado · test evaluado una sola vez · modelo y `metadatos.json` guardados | 2 |
| 🟡 **Estándar** | Además, un modelo neuronal (vale `MLPClassifier`) o LLM/RAG · 1–2 hiperparámetros ajustados solo con validación · lista de fugas contestada · registro de ≥ 12 filas · primera explicación (importancia, SHAP o Grad-CAM) · cuaderno reproducible, 3 *commits* de personas distintas · uso de IA declarado · revisión con la rúbrica anotada | 3 |
| 🔴 **Extra** | Hipótesis de **por qué gana** el candidato, contrastada con la explicación · análisis de errores o curvas · MLflow en local | 4 |

\*Orientativo; puntúa el docente con la rúbrica del curso (0–4 en cada criterio). El mínimo es una entrega válida y evaluable; la «Definition of Done» describe el nivel **estándar**.

## Reparto sugerido de los 470 minutos

| Min | Qué | Se sabe que está hecho cuando… |
|---|---|---|
| 130 (día 1) | Semilla, versiones, registro, partición común, *baseline* y primer modelo | El registro tiene el *baseline* y otro modelo |
| 140 (día 2) | Resto de modelos clásicos, red (o LLM/RAG) y ajuste de hiperparámetros | Cada persona tiene al menos una fila |
| 60 (día 2) | Lista de fugas y tutoría de 20 min con el docente | Cinco respuestas escritas y registro limpio |
| 70 (día 3) | Media ± desviación, coste y elección del candidato | `justificacion_candidato.md` con tabla y candidato razonado |
| 70 (día 3) | Test una vez, modelo guardado, explicación, revisión y subida | Los ficheros están en `sprint-15/` |

**Cada paso, explicado al detalle:** [Paso 1](../3_Consultar/Reto_Sprint_15_paso_1.md) · [Paso 2](../3_Consultar/Reto_Sprint_15_paso_2.md) · [Paso 3](../3_Consultar/Reto_Sprint_15_paso_3.md) · [Paso 4](../3_Consultar/Reto_Sprint_15_paso_4.md) · [Paso 5](../3_Consultar/Reto_Sprint_15_paso_5.md)

## Frases para la justificación (completad los huecos)

- «Elegimos … (… ± …) frente a … (… ± …): la diferencia (sí / no) puede ser ruido porque …»
- «Pesa más … que … en tiempo (…) y en explicabilidad (…), así que …»
- «Evaluado una sola vez en test: …. No hemos vuelto a elegir con ese resultado.»
- «Hemos usado IA para …; lo hemos revisado …; la fuga que detectamos fue …»

## Antes de entregar
- **Archivos subidos en `sprint-15/`:** `registro.csv` · `03_modelos.ipynb` · `justificacion_candidato.md` · `modelo_candidato.joblib` · `metadatos.json` · `explicacion_modelo.png` · `autoevaluacion_nombre.md` (**uno por persona**) = 6 + N ficheros
- [ ] Registro con una fila de cada persona · [ ] Test evaluado una sola vez, después de elegir · [ ] Cuaderno ejecutable de arriba abajo
- [ ] Revisión con la rúbrica anotada al final de la justificación · [ ] [Autoevaluación y coevaluación](../2_Entregar/autoevaluacion_y_coevaluacion.md): **una por persona**, subida a `sprint-15/`
