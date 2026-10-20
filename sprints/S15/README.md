# Sprint 15 · Proyecto · Modelado y experimentos
**Pregunta guía:** ¿qué modelo es el mejor para nuestro problema y cómo lo demostramos sin engañarnos?
**Fechas:** 1–3/12 · **Horas:** 18 h (1 T · 3 P · 14 PBL) · **Hito:** 3/12 modelo candidato elegido

> 🎯 **Reto de este sprint: «El mejor modelo, demostrado».** 👉 [**Ver el reto completo, explicado paso a paso**](guia/Reto_Sprint_15.md) · [Reto en PDF](guia/Reto_Sprint_15.pdf) ([ecofriendly](guia/Reto_Sprint_15_ecofriendly.pdf)) · [PDF de la guía](guia/Guia_Sprint_15.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

📄 **Este README en PDF:** [a color](README_Sprint_15.pdf) · [ecofriendly, para imprimir](README_Sprint_15_ecofriendly.pdf) (descárgalo para que funcionen los enlaces; la vista previa de GitHub no los abre).

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_15.pdf`](guia/Guia_Sprint_15.pdf) · [versión ecofriendly para imprimir](guia/Guia_Sprint_15_ecofriendly.pdf)
- 🎯 **Reto completo, paso a paso:** [`Reto_Sprint_15.md`](guia/Reto_Sprint_15.md)
- 🖥️ **S15.1 · Pildora seguimiento de experimentos:** [`S15.1_Pildora_seguimiento_de_experimentos.pdf`](presentaciones/S15.1_Pildora_seguimiento_de_experimentos.pdf)

**📁 En esta carpeta:** [`guia/`](guia/) PDF de la guía (normal y para imprimir) y el reto explicado paso a paso · [`presentaciones/`](presentaciones/) diapositivas de cada sesión · [`notebooks/`](notebooks/) prácticas para abrir en Colab · [`plantillas/`](plantillas/) plantillas para el reto

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

📖 teoría (diapositivas) · 💻 práctica (cuaderno de Colab o actividad) · 🎯 reto en equipo · 🔔 ceremonia de Scrum

**1/12**

1. 📖 **Teoría**: [Píldora: seguimiento de experimentos](presentaciones/S15.1_Pildora_seguimiento_de_experimentos.pdf) · _40 min_
2. 💻 **Práctica**: [Semillas, registro de experimentos, validación cruzada y fuga de datos](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S15/notebooks/S15_01_seguimiento_experimentos.ipynb) · _1 h_
3. 🎯 **Reto**: [Preparar el terreno y el registro de experimentos (paso 1)](plantillas/registro_experimentos_plantilla.csv) · _resto de la jornada_

**2/12**

4. 🎯 **Reto**: [Modelos clásicos y red neuronal (paso 2) → comprobar que no hay fugas de datos, **antes de elegir** (paso 3)](guia/Reto_Sprint_15.md) · _jornada completa_

**3/12 · hito: modelo candidato elegido**

5. 🎯 **Reto**: [Elegir el candidato (paso 4) → test **una sola vez** y explicación (paso 5)](guia/Reto_Sprint_15.md) · _jornada completa_

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
