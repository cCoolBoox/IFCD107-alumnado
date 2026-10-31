# Sprint 8 · Reto «Duelo de modelos» · en una página

> Versión corta para **trabajar con ella abierta**. La ficha completa (pasos detallados, rúbrica, uso de la IA, errores frecuentes) sigue en [Reto_Sprint_08.md](../2_Ficha_completa/Reto_Sprint_08.md); las plantillas están en [`model_card_plantilla.md`](../4_Plantillas_y_entrega/model_card_plantilla.md) y [`leaderboard_plantilla.csv`](../4_Plantillas_y_entrega/leaderboard_plantilla.csv); el cuaderno del reto, [`S08_06`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_06_leaderboard_plantilla.ipynb).

**El cliente.** TurisData ya sabe predecir cancelaciones. Ahora pregunta: **¿qué modelo ponemos en producción?** ¿El más preciso, el que se entiende o el más barato de mantener? Hay que enfrentar modelos con las mismas reglas y **elegir un campeón con argumentos**.
**Qué entregáis (no cambia):** `leaderboard_S08.csv`, `model_card.md`, el cuaderno `reto_S08.ipynb` y `README.md`. **Regla de oro: el test se usa una sola vez, solo con el campeón.**
**Tiempo:** unos 150 min de equipo. En clase: planning 10 min (día 1) · reto 75 min · entrega, review y retro 35 min (día 2). Los 65 min que faltan, en la consolidación y la 6.ª hora del día 2 (subida hasta las 14:30); lo demás, a casa.

## Tres niveles: el equipo decide hasta dónde llega

| Nivel | Qué hay que tener | Nota* |
|---|---|---|
| 🟢 **Mínimo** (todos los equipos) | Pesos de los tres criterios (rendimiento, explicabilidad, coste) escritos y justificados · **leaderboard con 6 modelos** medidos igual (referencia, logística, árbol, bosque, *boosting* y SVM) · campeón elegido con una frase de argumento · AUC de test calculado **una sola vez** · *model card* corta · README corto | 2 |
| 🟡 **Estándar** | Búsqueda de hiperparámetros con validación cruzada **en dos familias**, solo con train · análisis de sensibilidad: ¿cambia el campeón si cambian los pesos? · `model_card.md` completa (datos, métricas, límites, riesgos, mantenimiento) · README con versiones, semilla y uso de IA | 3 |
| 🔴 **Extra** | Importancia de variables del campeón explicada al cliente · comparación con incertidumbre (varias semillas) · plan de mantenimiento del modelo | 4 |

\*Orientativo; puntúa el docente con la rúbrica del curso (0–4 en cada criterio). El mínimo es una entrega válida y evaluable; la «Definition of Done» de la ficha completa describe el nivel **estándar**.

## Reparto sugerido de los 150 minutos

| Min | Qué | Se sabe que está hecho cuando… |
|---|---|---|
| 20 | Pesos de los criterios, justificados (día 1) | Pesos escritos que suman 100 % |
| 30 | Copia del cuaderno `reto_S08.ipynb` y 4 primeros modelos (día 2) | Leaderboard con referencia, logística, árbol y bosque |
| 25 | *Boosting*, SVM y búsqueda en dos familias (día 2) | 6 a 8 modelos, de 4 familias o más |
| 45 | Puntuación global, sensibilidad y test del campeón | `auc_test` en una sola fila |
| 30 | *Model card*, README, revisión con la rúbrica y subida | Otra persona podría ejecutarlo con el README |

## Frases para la model card y el README

- «Pesos acordados con el cliente: rendimiento …, explicabilidad …, coste …, porque …»
- «El campeón es … (AUC de validación … ± …). Lo elegimos porque …, aunque … es un poco más preciso, ya que …»
- «Si los pesos cambian a …, el campeón pasa a ser … (o se mantiene).»
- «Usos previstos: … No debe usarse para …» · «Hemos usado IA para …; lo hemos revisado …; no hemos pegado datos personales.»

## Antes de entregar
- **Archivos subidos en `sprint-08/`:** `leaderboard_S08.csv` · `model_card.md` · `reto_S08.ipynb` · `README.md` · `autoevaluacion_nombre.md` (**uno por persona**) = 4 + N ficheros
- [ ] ≥ 6 modelos en el leaderboard · [ ] AUC de test calculado **una sola vez** · [ ] Pesos justificados y sensibilidad probada · [ ] Cuaderno ejecutable (*Reiniciar y ejecutar todo*)
- [ ] `model_card.md` y README completos, con la «Revisión con la rúbrica» anotada · [ ] CSV descargado de Colab y todo subido a `sprint-08/`
- [ ] [Autoevaluación y coevaluación](../4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md): **una por persona**, subida a `sprint-08/`
