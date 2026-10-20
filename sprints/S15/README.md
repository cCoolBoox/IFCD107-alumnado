# Sprint 15 · Proyecto · Modelado y experimentos
**Pregunta guía:** ¿qué modelo es el mejor para nuestro problema y cómo lo demostramos sin engañarnos?
**Fechas:** 1–3/12 · **Horas:** 18 h (1 T · 3 P · 14 PBL) · **Hito:** 3/12 modelo candidato elegido

> 🎯 **Reto de este sprint: «El mejor modelo, demostrado».** 👉 [**Ver el reto completo, explicado paso a paso**](guia/Reto_Sprint_15.md) · [Reto en PDF](guia/Reto_Sprint_15.pdf) ([ecofriendly](guia/Reto_Sprint_15_ecofriendly.pdf)) · [PDF de la guía](guia/Guia_Sprint_15.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

📄 **Este README en PDF:** [a color](README_Sprint_15.pdf) · [ecofriendly, para imprimir](README_Sprint_15_ecofriendly.pdf) (descárgalo para que funcionen los enlaces; la vista previa de GitHub no los abre).

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_15.pdf`](guia/Guia_Sprint_15.pdf) · [versión ecofriendly para imprimir](guia/Guia_Sprint_15_ecofriendly.pdf)
- 🎯 **Reto completo, paso a paso:** [`Reto_Sprint_15.md`](guia/Reto_Sprint_15.md)
- 🖼️ **Infografías del reto (2 láminas: el reto de un vistazo y cómo se trabaja y se evalúa):** [`infografias/`](infografias/)
- 🖥️ **S15.1 · Pildora seguimiento de experimentos:** [`S15.1_Pildora_seguimiento_de_experimentos.pdf`](presentaciones/S15.1_Pildora_seguimiento_de_experimentos.pdf)

**📁 En esta carpeta:** [`infografias/`](infografias/) láminas ilustradas del reto · [`guia/`](guia/) PDF de la guía (normal y para imprimir) y el reto explicado paso a paso · [`presentaciones/`](presentaciones/) diapositivas de cada sesión · [`notebooks/`](notebooks/) prácticas para abrir en Colab · [`plantillas/`](plantillas/) plantillas para el reto

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

📖 teoría (diapositivas) · 💻 práctica (cuaderno de Colab o actividad) · 🎯 reto en equipo · 🔔 ceremonia de Scrum

**Martes 1/12**

1. 📖 **Teoría**: [**Píldora: seguimiento de experimentos**](presentaciones/S15.1_Pildora_seguimiento_de_experimentos.pdf) · _30 min_
2. 💻 **Práctica**: [Práctica de seguimiento de experimentos](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S15/notebooks/S15_01_seguimiento_experimentos.ipynb) · _50 min_
3. 🎯 **Reto**: **Proyecto:** modelo de referencia y primer modelo mejor. Anota todo en el [registro de experimentos](plantillas/registro_experimentos_plantilla.csv) · _2 h_

**Miércoles 2/12**

4. 🎯 **Reto**: **Proyecto:** prueba modelos (clásico, red o LLM/RAG, según tu brief) · _1 h 40 min_
5. 🎯 **Reto**: Continúa con los experimentos. **Tutoría técnica de 20 min por equipo** (el docente indica tu franja) · _1 h 40 min_

**Jueves 3/12**

6. 🎯 **Reto**: **Comparativa** de modelos y elección del **candidato** · _1 h 10 min_
7. 🎯 **Reto**: **Evaluación única en test:** una sola vez, con el candidato elegido · _40 min_
8. 🔔 **Ceremonia**: Entrega en `sprint-15/` de tu repo + autoevaluación y coevaluación · _30 min_
9. 🔔 **Ceremonia**: Review (5 min de demo por equipo) y retro: ¿qué mantenemos?, ¿qué cambiamos? · _1 h_

<!--orden:fin-->

## Qué aprenderás
- A **comparar modelos con rigor**: baseline, ≥ 3 modelos, validación cruzada y test reservado.
- A **registrar experimentos** (semillas, versiones, hiperparámetros, métricas) para poder repetirlos.
- A **detectar y evitar la fuga de datos**.
- A **elegir el modelo candidato** por rendimiento, coste, simplicidad y explicabilidad.

## Prácticas
| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| `S15_01_seguimiento_experimentos` | Semillas, registro en CSV, validación cruzada, fuga de datos, MLflow local *(opcional)* | 1 h 15 | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S15/notebooks/S15_01_seguimiento_experimentos.ipynb) |

- [`plantillas/registro_experimentos_plantilla.csv`](plantillas/registro_experimentos_plantilla.csv) · cabecera del registro; copiadla a `experimentos/registro.csv` en vuestro repositorio.

Sesiones: 1/12 planning, píldora y primeras iteraciones · 2/12 tutorías de 15 min por equipo y modelos · 3/12 comparativa final, **modelo candidato**, review y retro.

## Entrega / Reto · «El mejor modelo, demostrado»

👉 **[Ver el reto completo, explicado paso a paso](guia/Reto_Sprint_15.md)** (qué se pide, cómo hacerlo, cómo usar la IA, errores frecuentes y autoevaluación).

**Contexto:** el cliente (el docente) quiere saber qué modelo recomendáis y por qué. No basta «el que tiene mejor número»: ¿la mejora sobre el baseline justifica el coste? ¿Generaliza? ¿Se puede repetir?
**Entregáis** (carpeta `sprint-15/` del repositorio del equipo):
- Baseline + ≥ 3 modelos comparados con la misma partición, uno al menos neuronal (o LLM/RAG en el brief 3).
- `experimentos/registro.csv` (≥ 12 filas, con filas de todas las personas).
- Justificación de 1 página del modelo candidato: tabla comparativa, coste/beneficio y por qué gana.
- `notebooks/03_modelos.ipynb` ejecutable de arriba abajo con semillas fijas.
- Primera explicación del modelo (importancia, SHAP o Grad-CAM).
**Reglas:**
- El test se usa **una sola vez**, con el modelo ya elegido.
- Semillas fijas y versiones anotadas; sin claves ni datos personales.
- Definid antes qué vais a probar: nada de «200 combinaciones y la mejor».
**Se valora:** criterios C, D, F y G de la rúbrica del proyecto final (`proyecto-final/briefs_y_rubrica.md`).

## ✅ Antes de cerrar el sprint
- [ ] Baseline + ≥ 3 modelos + 1 neuronal comparados con la misma partición, sin fuga.
- [ ] `experimentos/registro.csv` con al menos una fila por persona.
- [ ] Semilla fija; el notebook se ejecuta de arriba abajo.
- [ ] Modelo candidato elegido y justificado; test evaluado una sola vez.
- [ ] Roles rotados, tablero actualizado y retro con acción concreta.
- [ ] Entregable subido a la carpeta `sprint-15/` del repositorio del equipo.
