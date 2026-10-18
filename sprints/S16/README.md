# Sprint 16 · Proyecto · Evaluación, IA responsable y entrega
**Pregunta guía:** ¿es nuestro modelo lo bastante bueno, justo y seguro para entregarlo, y puede otra persona reproducirlo?
**Fechas:** 4–10/12 (clases 4, 9 y 10/12; no hay clase el 7 y el 8) · **Horas:** 18 h (1 T · 3 P · 14 PBL)
**Hito: 10/12 a las 14:30 · congelación del repositorio y de la memoria**

> 🎯 **Reto de este sprint: «Entrega final: evaluar, demostrar y documentar».** 👉 [**Ver el reto completo, explicado paso a paso**](guia/Reto_Sprint_16.md) · [Reto en PDF](guia/Reto_Sprint_16.pdf) ([ecofriendly](guia/Reto_Sprint_16_ecofriendly.pdf)) · [PDF de la guía](guia/Guia_Sprint_16.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_16.pdf`](guia/Guia_Sprint_16.pdf) · [versión ecofriendly para imprimir](guia/Guia_Sprint_16_ecofriendly.pdf)
- 🎯 **Reto completo, paso a paso:** [`Reto_Sprint_16.md`](guia/Reto_Sprint_16.md)
- 🖥️ **S16.1 · Pildora demostrador y documentacion:** [`S16.1_Pildora_demostrador_y_documentacion.pdf`](presentaciones/S16.1_Pildora_demostrador_y_documentacion.pdf)

**📁 En esta carpeta:** [`guia/`](guia/) PDF de la guía (normal y para imprimir) y el reto explicado paso a paso · [`presentaciones/`](presentaciones/) diapositivas de cada sesión · [`notebooks/`](notebooks/) prácticas para abrir en Colab · [`plantillas/`](plantillas/) plantillas para el reto

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

📖 teoría (diapositivas) · 💻 práctica (cuaderno de Colab o actividad) · 🎯 reto en equipo · 🔔 ceremonia de Scrum

**4/12**

1. 📖 **Teoría**: [Píldora: demostrador y documentación](presentaciones/S16.1_Pildora_demostrador_y_documentacion.pdf) · _1 h_
2. 🎯 **Reto**: [Evaluación final y análisis de errores (paso 1)](guia/Reto_Sprint_16.md) · _resto de la jornada_

**9/12 (no hay clase el 7 y el 8)**

3. 💻 **Práctica**: [Demostrador](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S16/notebooks/S16_01_demostrador.ipynb) (carpeta [`plantillas/demostrador/`](plantillas/demostrador/)) · _1 h 15 min_
4. 🎯 **Reto**: [Mitigación de sesgos, demostrador, pruebas, ficha del modelo y borrador de la memoria (paso 2)](plantillas/plantilla_model_card.md) · _resto de la jornada_

**10/12 · congelación a las 14:30**

5. 🎯 **Reto**: [Memoria completa de 10–15 páginas, prueba de reproducibilidad y vídeo plan B (paso 3)](plantillas/plantilla_esqueleto_memoria_tecnica.md) · _mañana_
6. 🎯 **Reto**: [Lista de congelación y etiqueta `v1.0-entrega` **antes de las 14:30**](plantillas/checklist_congelacion.md) · _antes de las 14:30_
7. 🎯 **Reto**: [Coevaluación individual (cada persona entrega la suya)](plantillas/plantilla_coevaluacion.md) · _antes de las 14:30_

<!--orden:fin-->

## Qué aprenderás
- A **evaluar a fondo** el modelo candidato: errores, gráficos e incertidumbre.
- A **analizar sesgos** por subgrupos y a medir una medida de mitigación.
- A **clasificar el riesgo** del sistema (RGPD y AI Act).
- A **construir un demostrador** ejecutable y a documentar con model card y memoria técnica.

## Prácticas
| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| `S16_01_demostrador` | Demostrador: modelo + metadatos, lógica separada, pruebas, Streamlit, widgets y API (opcional) | 1 h 15 | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S16/notebooks/S16_01_demostrador.ipynb) |

- [`plantilla_esqueleto_memoria_tecnica.md`](plantillas/plantilla_esqueleto_memoria_tecnica.md) · memoria de 10-15 páginas.
- [`plantilla_model_card.md`](plantillas/plantilla_model_card.md) · tarjeta del modelo.
- [`plantilla_coevaluacion.md`](plantillas/plantilla_coevaluacion.md) · coevaluación individual.
- [`checklist_congelacion.md`](plantillas/checklist_congelacion.md) · lo que debe estar hecho antes del 10/12 a las 14:30.
- [`plantillas/demostrador/`](plantillas/demostrador/) · `logica.py`, `app.py`, `api.py`, `requirements.txt` y `README_demostrador.md`.

## Entrega / Reto · «Entrega final: evaluar, demostrar y documentar»

👉 **[Ver el reto completo, explicado paso a paso](guia/Reto_Sprint_16.md)** (qué se pide, cómo hacerlo, cómo usar la IA, errores frecuentes y autoevaluación).

**Contexto:** el cliente (el docente) recibirá vuestro trabajo como un entregable real: clonará el repositorio, seguirá el README, probará el demostrador y leerá la memoria. **La congelación es lo que esté subido al repositorio del equipo a las 14:30 del 10/12.**
**Entregáis** (carpeta `sprint-16/` del repositorio del equipo):
- `notebooks/04_evaluacion.ipynb`: evaluación final en test, gráficos y análisis de errores.
- Análisis de sesgos por subgrupos con mitigación aplicada y medida; registro de riesgos cerrado y clasificación RGPD / AI Act.
- Demostrador ejecutable con entradas erróneas gestionadas, aviso de incertidumbre y vídeo plan B.
- README reproducible, `requirements.txt` con versiones, model card y memoria técnica (10-15 páginas, PDF en `docs/`).
- Coevaluación individual de cada integrante.
**Reglas:**
- Se evalúa lo que esté en el repositorio a las 14:30 del 10/12.
- El demostrador debe funcionar desde cero en otro equipo.
- Sin datos personales, claves ni credenciales.
**Se valora:** criterios C, D, E, F, G y H de la rúbrica del proyecto final (`proyecto-final/briefs_y_rubrica.md`).

## ✅ Antes de cerrar el sprint
- [ ] Evaluación en test hecha **una sola vez**, con gráficos y análisis de errores.
- [ ] Rendimiento por subgrupos y mitigación aplicada y medida.
- [ ] Registro de riesgos cerrado; demostrador probado desde cero, con vídeo plan B.
- [ ] README reproducible probado por otra persona; model card y memoria en `docs/`.
- [ ] Coevaluación entregada por cada integrante.
- [ ] Entregable subido a la carpeta `sprint-16/` del repositorio del equipo antes de las 14:30 del 10/12.
