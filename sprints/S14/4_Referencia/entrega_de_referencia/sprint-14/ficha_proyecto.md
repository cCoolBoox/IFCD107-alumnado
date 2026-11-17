# Ficha de proyecto (1 página) · Anexo A

**Equipo (nombre de la consultora):** Las Palmeras IA · **Fecha:** 26/11/2026 (versión 2: 27/11/2026, tras el *go / no-go* y el EDA) · **Versión:** 2

## 1. Equipo y roles iniciales
| Persona | Rol en el Sprint 14 | Rotación prevista (S15 / S16) |
|---|---|---|
| Marta (A) | Scrum Master | Responsable técnica / Responsable de datos |
| Persona B | Responsable técnico | Responsable de datos / Responsable de IA responsable |
| Persona C | Responsable de datos | Responsable de IA responsable / Scrum Master |
| Persona D | Responsable de IA responsable | Scrum Master / Responsable técnico |

## 2. Brief elegido y pregunta de negocio
- **Brief:** **Libre**, inspirado en el brief 4 (previsión de una serie horaria). Cumple R1–R11: datos reales con licencia, serie temporal, comparación con *baseline* y una red neuronal, demostrador.
- **Pregunta de negocio en una frase:** «¿Podemos prever cuántas bicis se alquilarán en cada hora de mañana para que el operador del sistema pueda decidir cuántas recolocar en cada turno?»

## 3. Cliente y decisión que se apoyará
- **Quién usará el resultado:** la persona responsable de operaciones de un sistema de bicis compartidas (el caso real: Washington D. C., 2011–2012).
- **Decisión concreta que mejorará:** cuántas bicis y cuántas personas de redistribución poner en cada franja de mañana. **Hoy, sin el modelo,** se repite lo de la semana pasada y se falla en 69,5 bicis por hora de media (24 % de lo alquilado) y en 133 en hora punta.

## 4. Datos
| Fuente (enlace) | Licencia | Tamaño | Variables clave | Limitaciones previstas |
|---|---|---|---|---|
| [UCI Bike Sharing](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset) (`hour.csv`) | CC BY 4.0 | 17.379 filas, 17 columnas, 1,1 MB | `cnt` (alquileres), hora, día, festivo, clima | Una ciudad y un operador; 2011–2012; el clima real no se conoce de antemano |

## 5. Métrica de éxito y baseline
- **Métrica de negocio:** evitar errores de previsión: con el umbral de éxito se ahorran al menos **17 bicis de error por hora**, unas **408 bicis mal planificadas al día**.
- **Métrica técnica:** MAE (bicis por hora); apoyo: WAPE y MAE en hora punta (laborables 7–9 h y 17–19 h).
- **Umbral de éxito acordado:** bajar el MAE del *baseline* **al menos un 25 %** en validación (de 69,5 a ≤ 52,1).
- **Baseline previsto:** «igual que la misma hora de la semana pasada». Resultado en validación: MAE **69,5**, WAPE 24 %, hora punta 133.
- **Partición de los datos:** temporal (sin barajar): entrenamiento hasta 31/8/2012 · validación sep–oct 2012 · test nov–dic 2012 (no se toca hasta el candidato). Escrita en el cuaderno **antes** de calcular el *baseline*.

## 6. Modelos previstos (≥ 3, incluyendo redes neuronales según el brief)
- **Enfoque elegido y por qué:** datos en tabla, 17.379 filas, hay que poder explicar qué pesa → árboles con boosting; la red sirve de comparación.
1. *Baseline* de la semana pasada · 2. Regresión lineal (Ridge) · 3. Boosting de árboles (sin clima y con clima) · 4. Red neuronal (MLP) con las mismas variables.

## 7. Demostrador previsto
- **Tecnología:** Streamlit. **Qué hará:** el usuario elige una fecha y el clima previsto y ve las bicis esperadas hora a hora con un aviso de incertidumbre.
- **Plan B si falla la demo:** vídeo de 90 s.

## 8. Riesgos y mitigación
| Riesgo | Tipo (datos / modelo / uso / legal / técnico) | Mitigación |
|---|---|---|
| Se usa el clima real como si fuera una previsión (fuga suave) | datos | Modelo con y sin clima; en S16, error simulado en la previsión |
| El huracán Sandy (29/10/2012, 22 alquileres en el día) distorsiona la evaluación | datos | Mirarlo aparte en la evaluación |
| Se usa la previsión para recortar servicio sin revisión humana | uso | Aviso de incertidumbre y supervisión humana en el demostrador |

*Clasificación preliminar AI Act: **riesgo mínimo** (predice demanda agregada, no decide sobre personas) · ¿Datos personales? **no***

## 9. Backlog inicial (13 historias) y objetivo de cada sprint
- **Historias principales:** definir la métrica (H1), plan de datos (H2), EDA (H3), *baseline* (H4), ≥ 4 modelos comparados (H5), red neuronal (H6), evaluación por subgrupos con mitigación (H8), demostrador (H9), memoria (H10), defensa (H11). Completo en `backlog_y_sprints.md`.
- **Objetivo S14:** pregunta, datos con licencia, EDA y *baseline* de 69,5 bicis/hora · **S15:** un candidato con MAE ≤ 52,1 en validación · **S16:** test mirado una vez, demo con tests y memoria congelada · **S17:** defensa en 12 diapositivas.

**Cambios de la versión 2:** tras el EDA, la métrica incluye la **hora punta** (el *baseline* falla 1,9 veces más allí) y el clima pasa de «extra» a variable principal, con un modelo sin clima como comparación.

---
**Firmas del equipo:** Marta, Persona B, Persona C, Persona D · **Respuesta del docente:** ☐ GO ☑ GO con cambios ☐ NO-GO — Comentarios: «Declarad que el clima es una previsión y añadid la hora punta a la métrica.»
