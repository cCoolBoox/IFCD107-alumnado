# Autoevaluación y coevaluación · «Informe visual para dirección»

> Hoja de **ejemplo** de una persona (Marta) del equipo de referencia. Cada persona sube la suya con su nombre.

## 1. Autoevaluación

**Nombre:** Marta

**Repaso rápido:**

| Pregunta | Mi respuesta |
|---|---|
| ¿Es una sola página con titular-decisión, 3 o 4 gráficos, 3 viñetas y pie? | Sí: titular con euros, 4 gráficos, 3 viñetas y pie |
| ¿Cada gráfico tiene título-conclusión y ejes con nombre? | Sí, los títulos salen de las variables del cuaderno |
| ¿Las barras empiezan en 0, sin 3D y con 3–4 colores con sentido? | Sí: azul, gris y verde; sin 3D |
| ¿Las métricas están calculadas sobre el test? | Sí, con las 1.500 reservas que el modelo no vio |
| ¿Indicamos con cuántos datos, qué modelo y qué límites? | Sí, en el pie y en la tercera viñeta |
| ¿El cuaderno se ejecuta de arriba abajo con semillas fijas? | Sí: el mismo PNG y las mismas cifras al reiniciar |
| ¿Otro equipo entendió la decisión en 30 segundos? | Sí: Los Roques entendió «avisar y pedir depósito a las de riesgo alto» |
| ¿Está guardado en el repositorio del equipo como semilla de la memoria? | Sí, en `sprint-13/` |

**Puntúate de 1 a 4:**

| Criterio | Mi puntuación (1–4) | Por qué (una frase) | Qué haría para subir un punto |
|---|---|---|---|
| Corrección técnica | 4 | Cuatro gráficos sobre el test y dos umbrales y dos modelos comparados con los costes | Está en el máximo; lo siguiente sería calibrar las probabilidades |
| Reproducibilidad | 4 | Mismo PNG al reiniciar y versiones en el pie | Está en el máximo |
| Análisis y comunicación al cliente | 3 | El titular lleva euros, pero escribí «AUC» en el gráfico 2 y solo lo expliqué en el texto | Cambiar la leyenda del gráfico por «acierto frente al azar» para llegar al 4 |
| IA responsable | 4 | Riesgo por canal con cifra y medida | Está en el máximo; mediría también por tipo de tarifa |

- **Lo que más me costó fue** escribir un título que dijese algo discutible y no solo describiese, **porque** «Curva ROC» no es una conclusión y hubo que decidir qué conclusión sacar del AUC.
- **He usado IA para** entender la importancia por permutación y revisar títulos, **y lo que he comprobado a mano es** que las cifras de los títulos salen de las variables y que el título de la IA sobre el depósito afirmaba una causa que el gráfico no muestra.

---

## 2. Coevaluación

**Trabajo revisado de (persona o equipo):** equipo «Los Roques» (ejemplo)  **Revisado por (yo):** Marta

| Entregable | ¿Está y se entiende? | Comentario breve |
|---|---|---|
| `informe_visual.md` | ✔ | El titular dice qué hacer, a quién y con qué efecto |
| `informe_visual_panel.png` | ✘ | Los títulos de los gráficos describen («Curva ROC») en vez de concluir |
| `informe_visual.ipynb` | ✔ | Se ejecuta de arriba abajo; falta anotar las versiones |

| Criterio | Puntuación | Comentario breve |
|---|---|---|
| Corrección técnica | 2 | Tres gráficos sobre el test, pero el eje de los euros no empieza en 0 |
| Reproducibilidad | 3 | Sale el mismo PNG; el pie indica datos, modelo, umbral y semilla |
| Análisis y comunicación al cliente | 2 | Hay titular y viñetas, pero queda «AUC» sin explicar |
| IA responsable | 2 | Dicen «puede haber sesgos» sin un riesgo concreto ni medida |

- **Lo que está muy bien:** el titular lleva la cifra en euros y las viñetas se leen en 30 segundos.
- **Lo que yo cambiaría, y por qué:** empezaría el eje de los euros en 0 y reescribiría los títulos como conclusiones, porque una barra recortada exagera el ahorro.

> Se valora el **trabajo**, no a la persona.
