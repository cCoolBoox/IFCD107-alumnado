# Autoevaluación y coevaluación · «Precio y cancelación»

> Hoja de **ejemplo** de una persona (Marta) del equipo de referencia. Cada persona sube la suya con su nombre.

## 1. Autoevaluación

**Nombre:** Marta

**Repaso rápido:**

| Pregunta | Mi respuesta |
|---|---|
| ¿La regresión tiene baseline y métricas en euros (MAE, RMSE) y R²? | Sí: referencia, lineal e interacciones, con MAE, RMSE y R² |
| ¿La clasificación tiene baseline, matriz de confusión, AUC/AP y umbral justificado? | Sí: matriz con el umbral 0,25, AUC 0,746, AP 0,729 y umbral elegido con validación cruzada |
| ¿Los costes de FN y FP son hipótesis explícitas con análisis de sensibilidad? | Sí: 284 € y 103 €, cada uno con su razón, y una tabla con cuatro hipótesis |
| ¿La recomendación tiene cifras y límites? | Sí: 98 153 € de ahorro en test y límites de datos sintéticos y costes supuestos |
| ¿No hay fuga de datos y el test se usó una sola vez? | Sí: `cancelada` no entra en el precio y el umbral sale de *train* |
| ¿El cuaderno se ejecuta entero y el README tiene versiones y semilla? | Sí; lo probé en una sesión nueva de Colab |
| ¿Está subido a Git, con autoevaluación y coevaluación? | Sí, con *commits* de tres personas |

**Puntúate de 1 a 4:**

| Criterio | Mi puntuación (1–4) | Por qué (una frase) | Qué haría para subir un punto |
|---|---|---|---|
| Corrección técnica | 3 | Todo lo estándar está hecho y el test se usó una vez | Añadir *overbooking* con su ahorro en euros |
| Reproducibilidad | 3 | Otra persona obtuvo las mismas cifras siguiendo el README | Indicar cuánto tarda en ejecutarse el cuaderno |
| Análisis y comunicación al cliente | 3 | El resumen está en euros y la recomendación tiene límites | Probar el resumen con alguien que no sepa de IA |
| IA responsable | 3 | El README dice qué se pidió, qué se revisó y qué se cambió, y hay tasa de aviso por canal | Medir qué pasa con el comportamiento de los clientes cuando se les llama |

- **Lo que más me costó fue** elegir los costes, **porque** no hay un dato que diga cuánto cuesta una falsa alarma y hubo que razonarlo y probar la sensibilidad.
- **He usado IA para** entender qué es un *odds ratio*, **y lo que he comprobado a mano es** que cada cifra del informe es la del último «Reiniciar y ejecutar todo».

---

## 2. Coevaluación

**Trabajo revisado de (persona o equipo):** equipo «Las Palmeras» (ejemplo)  **Revisado por (yo):** Marta

| Entregable | ¿Está y se entiende? | Comentario breve |
|---|---|---|
| `reto_S07.ipynb` | ✔ | Se ejecuta entero; el umbral se elige mirando el test |
| `informe_modelado.md` | ✘ | El resumen solo da el AUC, sin euros |
| `README.md` | — | No dice la semilla ni las versiones |

| Criterio | Puntuación | Comentario breve |
|---|---|---|
| Corrección técnica | 1 | Umbral elegido con el test (celda 18) |
| Reproducibilidad | 2 | El README dice cómo ejecutar, pero faltan semilla y versiones |
| Análisis y comunicación al cliente | 1 | Solo métricas técnicas, sin pasarlas a euros |
| IA responsable | 1 | No dice si se usó IA |

- **Lo que está muy bien:** el cuaderno es claro y tiene comentarios en cada celda.
- **Lo que yo cambiaría, y por qué:** elegiría el umbral con validación cruzada sobre *train*, porque si se elige con el test, el coste en test deja de ser una prueba honesta.

> Se valora el **trabajo**, no a la persona.
