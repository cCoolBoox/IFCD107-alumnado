# Autoevaluación y coevaluación · «El mejor modelo, demostrado» (Sprint 15)

> Hoja de **ejemplo** de una persona (Marta) del equipo de referencia. Cada persona sube la suya con su nombre.

## 1. Autoevaluación

**Nombre:** Marta

**Repaso rápido:**

| Pregunta | Mi respuesta |
|---|---|
| ¿Hay baseline + ≥ 3 modelos + 1 neuronal (o LLM/RAG) con la **misma** partición? | Sí: 2 baselines, regresión lineal, bosque, boosting y una red con 3 semillas, todos con los mismos 5 bloques temporales |
| ¿La validación no tiene fuga (temporal en series; sin mezclar fotos del mismo objeto)? | Sí, por bloques temporales; la validación barajada de la IA la descartamos |
| ¿`registro.csv` tiene todas las pruebas y al menos una fila por persona? | Sí: 18 filas de las cuatro personas |
| ¿Semilla y versiones anotadas; el notebook se ejecuta de arriba abajo? | Sí: SEMILLA = 42 y el diccionario ENTORNO; se ejecuta entero en unos 3 minutos |
| ¿El candidato está elegido con justificación (rendimiento, coste, explicabilidad)? | Sí, con el empate explicado y desempatado por simplicidad |
| ¿El test se evaluó una sola vez, después de elegir? | Sí, en una sola celda; no volvimos a elegir |
| ¿Hay modelo guardado y primera explicación? | Sí: `.joblib`, `metadatos.json` y el gráfico de permutación |
| ¿Roles rotados, tablero actualizado y retro con acción concreta? | Sí: la acción de la retro del S14 (15 min por decisión) se cumplió; la retro del S15 queda escrita en el backlog |

**Puntúate de 1 a 4:**

| Criterio | Mi puntuación (1–4) | Por qué (una frase) | Qué haría para subir un punto |
|---|---|---|---|
| Corrección técnica | 4 | Análisis por franjas que enseña dónde falla el candidato | Está en el máximo |
| Reproducibilidad | 4 | Todas las filas llevan `datos_hash` y semilla y se anota el coste | Está en el máximo |
| Análisis y comunicación al cliente | 3 | Explica el ruido y el test sin jerga, pero no sé traducir el error a euros | Pedir el coste de una bici mal colocada y calcular el ahorro en euros |
| IA responsable | 4 | Cuento la validación barajada de la IA con números y un límite de la explicación | Está en el máximo |

- **Lo que más me costó fue** entender por qué la red neuronal sale peor que el baseline, **porque** esperaba que ganara y tardé en aceptar que con una tabla de 15.000 filas los árboles aprovechan mejor la información.
- **He usado IA para** el código de la red y de la validación, **y lo que he comprobado a mano es** que la validación barajaba las horas: daba un error de 26,7 y el mismo modelo validado por fechas daba 40,8.

---

## 2. Coevaluación

**Trabajo revisado de (persona o equipo):** equipo «Los Roques» (ejemplo)  **Revisado por (yo):** Marta

| Entregable | ¿Está y se entiende? | Comentario breve |
|---|---|---|
| `registro.csv` | ✔ | Tiene filas de las tres personas y el baseline en la primera |
| `03_modelos.ipynb` | ✘ | Reparten las filas al azar y no hay comprobación de fugas |
| `justificacion_candidato.md` | ✔ | Dice cuál elige y por qué, pero no si la diferencia puede ser ruido |

| Criterio | Puntuación | Comentario breve |
|---|---|---|
| Corrección técnica | 2 | Los modelos no usan la misma partición |
| Reproducibilidad | 3 | Hay semilla y versiones, pero el cuaderno falla en la celda 12 |
| Análisis y comunicación al cliente | 2 | Tabla sin desviaciones: no se sabe si la diferencia es real |
| IA responsable | 2 | Dice que usaron IA pero no qué revisaron |

- **Lo que está muy bien:** el registro está limpio y cada persona tiene sus filas.
- **Lo que yo cambiaría, y por qué:** usaría la misma validación para todos los modelos, porque ahora no se pueden comparar los números.

> Se valora el **trabajo**, no a la persona.
