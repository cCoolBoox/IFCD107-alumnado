# Sprint 8 · Reto «Duelo de modelos» · en una página

> Versión corta para **trabajar con ella abierta**. La ficha completa sigue en [Reto_Sprint_08.md](Reto_Sprint_08.md); plantillas: [`leaderboard_plantilla.csv`](leaderboard_plantilla.csv) y [`model_card_plantilla.md`](model_card_plantilla.md).

**El cliente.** TurisData ya sabe predecir cancelaciones. Ahora pregunta: **¿qué modelo ponemos en producción?** ¿El más preciso, el que se entiende o el más barato de mantener? Hay que enfrentar modelos con las mismas reglas y **elegir un campeón con argumentos**.
**Qué entregáis (no cambia):** `leaderboard_S08.csv`, `model_card.md`, el cuaderno `reto_S08.ipynb` y `README.md`.
**Tiempo en clase:** planning 10 min · reto 75 min · entrega, review y retro 35 min.

## Tres niveles: el equipo decide hasta dónde llega

| Nivel | Qué hay que tener | Nota* |
|---|---|---|
| 🟢 **Mínimo** (todos los equipos) | Pesos de los tres criterios (rendimiento, explicabilidad, coste) acordados y escritos · **leaderboard con 6 modelos** medidos igual (baseline, logística, árbol, bosque, boosting y SVM) · campeón elegido con una frase de argumento · AUC de test calculado **una sola vez** | 2 |
| 🟡 **Estándar** | Búsqueda de hiperparámetros con validación cruzada **en dos familias** (guía de `S08_05`) · análisis de sensibilidad: ¿cambia el campeón si cambian los pesos? · `model_card.md` completa (usos, datos, métricas, limitaciones, IA responsable, mantenimiento) | 3 |
| 🔴 **Extra** | Importancia de variables del campeón explicada al cliente · comparación con incertidumbre (varias semillas) · plan de mantenimiento del modelo | 4 |

\*Orientativo; puntúa el docente con la rúbrica del curso (0–4 en cada criterio). El mínimo es una entrega válida y evaluable; la «Definition of Done» de la ficha completa describe el nivel **estándar**.

## Frases para la model card y el README

- «Pesos acordados con el cliente: rendimiento …, explicabilidad …, coste …, porque …»
- «El campeón es … (AUC de validación … ± …). Lo elegimos porque …, aunque … es un poco más preciso, ya que …»
- «Si los pesos cambian a …, el campeón pasa a ser … (o se mantiene).»
- «Usos previstos: … No debe usarse para …»

## Antes de entregar
- [ ] ≥ 6 modelos en el leaderboard · [ ] AUC de test calculado **una sola vez** · [ ] Pesos justificados y sensibilidad probada
- [ ] `model_card.md` completa · [ ] Cuaderno ejecutable · [ ] Subido a Git, [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md) rellenadas
