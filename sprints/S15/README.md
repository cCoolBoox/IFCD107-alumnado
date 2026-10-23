# README Sprint S15 · Proyecto · Modelado y experimentos

**Pregunta guía:** ¿qué modelo es el mejor para nuestro problema y cómo lo demostramos sin engañarnos?
**Fechas:** 1–3/12 · **Horas:** 18 h (1 T · 3 P · 14 PBL) · **Hito:** 3/12 modelo candidato elegido

📄 **Este README en PDF:** [a color](README_Sprint_15.pdf) · [ecofriendly, para imprimir](README_Sprint_15_ecofriendly.pdf) (descárgalo para que funcionen los enlaces; la vista previa de GitHub no los abre).

## Qué aprenderás
1. **Comparar modelos con rigor:** baseline, ≥ 3 modelos, validación cruzada y test reservado (R3).
2. **Registrar experimentos** para que cualquiera pueda reproducirlos: semillas, versiones, hiperparámetros y métricas.
3. **Detectar y evitar la fuga de datos**, especialmente en series y en imágenes del mismo objeto.
4. Integrar **al menos un modelo neuronal** (o LLM/RAG en el brief 3) y justificar si vale la pena (R4).
5. **Elegir el modelo candidato** con criterios de rendimiento, coste, simplicidad y explicabilidad.

## Requisitos previos
- Sprint 14 completado: ficha con go, datos documentados, EDA, baseline y backlog.
- Notebooks de los Sprints 7, 8, 10, 11 y 12 (según vuestro brief) como material de consulta.
- Repositorio del equipo con la estructura de `plantilla_README_repositorio.md`.

## 📎 Materiales del sprint

**Documentos del curso** (PDF y .md; las actividades van en la tabla siguiente)

| Material | Tema | Tiempo | Cuándo |
|---|---|---|---|
| [Guía del sprint (PDF)](guia/Guia_Sprint_15.pdf) · [ecofriendly](guia/Guia_Sprint_15_ecofriendly.pdf) | Resumen del sprint: qué aprenderás, temario, material, reto y conclusión | 2 páginas | Antes de empezar |
| [Reto completo, paso a paso (.md)](guia/Reto_Sprint_15.md) · [PDF](guia/Reto_Sprint_15.pdf) · [ecofriendly](guia/Reto_Sprint_15_ecofriendly.pdf) | Qué pide el cliente, pasos, rúbrica, ayudas y errores frecuentes | — | Antes del planning y durante el reto |
| [Resumen del sprint en una página](infografias/S15_00_resumen_del_sprint.png) | Lámina con la pregunta del cliente, los pasos, lo que se entrega y lo que se aprende | — | Antes del planning |
| [Esquema del contenido y su relación con el reto](infografias/S15_07_esquema_contenido_y_reto.png) | Qué presentación prepara cada pieza del entregable, con el material que se reutiliza después | — | Antes del planning y como guía durante el reto |
| [Infografías del reto](infografias/) | 4 láminas ilustradas del reto | — | Reto |
| [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md) | El método de trabajo de todos los retos | — | Antes del primer reto |
| [`S15.1_Pildora_seguimiento_de_experimentos.pdf`](presentaciones/S15.1_Pildora_seguimiento_de_experimentos.pdf) | Píldora: seguimiento de experimentos | 20 min | Teoría · martes 1/12 |

**Material de las actividades**

| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| `S15_01_seguimiento_experimentos` | Semillas, registro en CSV, validación cruzada, fuga de datos, MLflow local *(opcional)* | 1 h 15 | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S15/notebooks/S15_01_seguimiento_experimentos.ipynb) |

- [`plantillas/registro_experimentos_plantilla.csv`](plantillas/registro_experimentos_plantilla.csv) · cabecera del registro; copiadla a `experimentos/registro.csv` en vuestro repositorio.

Sesiones: 1/12 planning, píldora y primeras iteraciones · 2/12 tutorías de 15 min por equipo y modelos · 3/12 comparativa final, **modelo candidato**, review y retro.

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

**Martes 1/12**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 1 | 📖 Teoría | [**Píldora: seguimiento de experimentos**](presentaciones/S15.1_Pildora_seguimiento_de_experimentos.pdf) | 20 min |
| 2 | 💻 Práctica | [Práctica de seguimiento de experimentos](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S15/notebooks/S15_01_seguimiento_experimentos.ipynb) | 50 min |
| 3 | 🎯 Reto | **Proyecto:** modelo de referencia y primer modelo mejor. Anota todo en el [registro de experimentos](plantillas/registro_experimentos_plantilla.csv) | 2 h 10 min |

**Miércoles 2/12**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 4 | 🎯 Reto | **Proyecto:** prueba modelos (clásico, red o LLM/RAG, según tu brief) | 1 h 40 min |
| 5 | 🎯 Reto | Continúa con los experimentos. **Tutoría técnica de 20 min por equipo** (el docente indica tu franja) | 1 h 40 min |

**Jueves 3/12**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 6 | 🎯 Reto | **Comparativa** de modelos y elección del **candidato** | 1 h 10 min |
| 7 | 🎯 Reto | **Evaluación única en test:** una sola vez, con el candidato elegido | 40 min |
| 8 | 🔔 Ceremonia | Entrega en `sprint-15/` de tu repo + autoevaluación y coevaluación | 30 min |
| 9 | 🔔 Ceremonia | Review (5 min de demo por equipo) y retro: ¿qué mantenemos?, ¿qué cambiamos? | 1 h |

<!--orden:fin-->

## Entrega / Reto · «El mejor modelo, demostrado»

📄 [Reto en PDF](guia/Reto_Sprint_15.pdf) · [ecofriendly](guia/Reto_Sprint_15_ecofriendly.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

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
