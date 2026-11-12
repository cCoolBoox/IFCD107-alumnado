# Autoevaluación y coevaluación · «Duelo de modelos»

> Hoja de **ejemplo** de una persona (Marta) del equipo de referencia. Cada persona sube la suya con su nombre.

## 1. Autoevaluación

**Nombre:** Marta

**Repaso rápido:**

| Pregunta | Mi respuesta |
|---|---|
| ¿El leaderboard tiene ≥ 6 modelos de al menos 4 familias? | Sí: 8 modelos de 6 familias (referencia, lineal, árbol, bosque, boosting y SVM) |
| ¿Hay búsqueda de hiperparámetros con CV sobre train para al menos dos familias? | Sí: rejilla para el bosque y búsqueda aleatoria para LightGBM, las dos con 5 folds sobre train |
| ¿El campeón se justifica con los tres criterios y se probó la sensibilidad de los pesos? | Sí: apartado 3 de la *model card*, con cuatro conjuntos de pesos |
| ¿El AUC de test se calculó una sola vez, solo para el campeón? | Sí: `auc_test` tiene valor solo en la fila de `logistica` |
| ¿La model card está completa (usos, datos, métricas, limitaciones, IA responsable, mantenimiento)? | Sí, los diez apartados con cifras del cuaderno |
| ¿El cuaderno se ejecuta entero y el README tiene versiones? | Sí; lo probé en una sesión nueva de Colab |

**Puntúate de 1 a 4:**

| Criterio | Mi puntuación (1–4) | Por qué (una frase) | Qué haría para subir un punto |
|---|---|---|---|
| Corrección técnica | 3 | Todo lo estándar está hecho y el test se usó una vez | Repetir el duelo con varias semillas y dar la incertidumbre del campeón |
| Reproducibilidad | 3 | Otra persona obtuvo el mismo campeón siguiendo el README | Indicar cuánto tarda cada búsqueda en Colab |
| Análisis y comunicación al cliente | 3 | Explicamos que el campeón cambia con los pesos y que la ventaja es corta | Pasar el AUC a euros con los costes del Sprint 7 |
| IA responsable | 3 | El README dice qué se pidió, qué se revisó y qué se cambió, y hay tasa de aviso por canal | Medir qué pasa con el comportamiento de los clientes cuando se les llama |

- **Lo que más me costó fue** entender por qué los modelos ajustados no ganaban, **porque** la mejora era de milésimas, menor que la desviación de los folds.
- **He usado IA para** entender la diferencia entre rejilla y búsqueda aleatoria, **y lo que he comprobado a mano es** que los números de la *model card* son los del último «Reiniciar y ejecutar todo».

---

## 2. Coevaluación

**Trabajo revisado de (persona o equipo):** equipo «Las Palmeras» (ejemplo)  **Revisado por (yo):** Marta

| Entregable | ¿Está y se entiende? | Comentario breve |
|---|---|---|
| `leaderboard_S08.csv` | ✔ | Seis modelos de cuatro familias; `auc_test` en una sola fila |
| `model_card.md` | ✘ | Faltan los usos NO previstos y el mantenimiento |
| `reto_S08.ipynb` | ✔ | Se ejecuta entero; falta la celda de versiones |

| Criterio | Puntuación | Comentario breve |
|---|---|---|
| Corrección técnica | 2 | Cumple el mínimo; sin búsqueda de hiperparámetros |
| Reproducibilidad | 2 | El README no dice las versiones |
| Análisis y comunicación al cliente | 2 | Explican el campeón, pero no si cambia con otros pesos |
| IA responsable | 1 | No dice si se usó IA ni nombra riesgos |

- **Lo que está muy bien:** el leaderboard está limpio y los pesos tienen una razón escrita.
- **Lo que yo cambiaría, y por qué:** añadiría los usos NO previstos, porque es lo que protege a los clientes de decisiones automáticas.

> Se valora el **trabajo**, no a la persona.
