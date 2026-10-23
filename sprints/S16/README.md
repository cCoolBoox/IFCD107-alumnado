# README Sprint S16 · Proyecto · Evaluación, IA responsable y entrega

**Pregunta guía:** ¿es nuestro modelo lo bastante bueno, justo y seguro para entregarlo, y puede otra persona reproducirlo?
**Fechas:** 4–10/12 (clases 4, 9 y 10/12; no hay clase el 7 y el 8) · **Horas:** 18 h (1 T · 3 P · 14 PBL)
**Hito: 10/12 a las 14:30 · congelación del repositorio y de la memoria**

📄 **Este README en PDF:** [a color](README_Sprint_16.pdf) · [ecofriendly, para imprimir](README_Sprint_16_ecofriendly.pdf) (descárgalo para que funcionen los enlaces; la vista previa de GitHub no los abre).

## Qué aprenderás
1. **Evaluar a fondo el modelo candidato:** métricas adecuadas, análisis de errores y visualizaciones (curvas, matriz de confusión, importancia, SHAP o Grad-CAM) que comunican incertidumbre (R5).
2. **Analizar sesgos y limitaciones** por subgrupos y **aplicar y medir medidas de mitigación** (R6).
3. **Clasificar el riesgo** del sistema (RGPD y AI Act) y cerrar el registro de riesgos.
4. **Construir un demostrador ejecutable** con validación de entradas, aviso de incertidumbre y plan B (R7).
5. **Documentar:** model card, README reproducible y **memoria técnica de 10-15 páginas** (R8, R10).

## Requisitos previos
- Modelo candidato elegido el 3/12 y registro de experimentos.
- Plan ético del Sprint 14 (`registro_riesgos_eticos`) y notebook `S13_02` (plantilla de informe visual).
- Píldora de teoría de este sprint: despliegue de un demostrador y documentación técnica.

## 📎 Materiales del sprint

**Documentos del curso** (PDF y .md; las actividades van en la tabla siguiente)

| Material | Tema | Tiempo | Cuándo |
|---|---|---|---|
| [Guía del sprint (PDF)](guia/Guia_Sprint_16.pdf) · [ecofriendly](guia/Guia_Sprint_16_ecofriendly.pdf) | Resumen del sprint: qué aprenderás, temario, material, reto y conclusión | 2 páginas | Antes de empezar |
| [Reto completo, paso a paso (.md)](guia/Reto_Sprint_16.md) · [PDF](guia/Reto_Sprint_16.pdf) · [ecofriendly](guia/Reto_Sprint_16_ecofriendly.pdf) | Qué pide el cliente, pasos, rúbrica, ayudas y errores frecuentes | — | Antes del planning y durante el reto |
| [Resumen del sprint en una página](infografias/S16_00_resumen_del_sprint.png) | Lámina con la pregunta del cliente, los pasos, lo que se entrega y lo que se aprende | — | Antes del planning |
| [Esquema del contenido y su relación con el reto](infografias/S16_07_esquema_contenido_y_reto.png) | Qué presentación prepara cada pieza del entregable, con el material que se reutiliza después | — | Antes del planning y como guía durante el reto |
| [Infografías del reto](infografias/) | 4 láminas ilustradas del reto | — | Reto |
| [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md) | El método de trabajo de todos los retos | — | Antes del primer reto |
| [`S16.1_Pildora_demostrador_y_documentacion.pdf`](presentaciones/S16.1_Pildora_demostrador_y_documentacion.pdf) | Despliegue y documentación | 20 min | Teoría · viernes 4/12 |

**Material de las actividades**

| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| `S16_01_demostrador` | Demostrador: modelo + metadatos, lógica separada, pruebas, Streamlit, widgets y API (opcional) | 1 h 15 | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S16/notebooks/S16_01_demostrador.ipynb) |

- [`plantilla_esqueleto_memoria_tecnica.md`](plantillas/plantilla_esqueleto_memoria_tecnica.md) · memoria de 10-15 páginas.
- [`plantilla_model_card.md`](plantillas/plantilla_model_card.md) · tarjeta del modelo.
- [`plantilla_coevaluacion.md`](plantillas/plantilla_coevaluacion.md) · coevaluación individual.
- [`checklist_congelacion.md`](plantillas/checklist_congelacion.md) · lo que debe estar hecho antes del 10/12 a las 14:30.
- [`plantillas/demostrador/`](plantillas/demostrador/) · `logica.py`, `app.py`, `api.py`, `requirements.txt` y `README_demostrador.md`.

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

**Viernes 4/12**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 1 | 🔔 Ceremonia | **Planning del Sprint 16:** lee el [README del Sprint 16](README.md) y reparte tareas | 10 min |
| 2 | 📖 Teoría | [**Despliegue y documentación**](presentaciones/S16.1_Pildora_demostrador_y_documentacion.pdf) | 20 min |
| 3 | 💻 Práctica | [Práctica del demostrador](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S16/notebooks/S16_01_demostrador.ipynb) | 45 min |
| 4 | 🎯 Reto | **Tutoría de sesgos y visualización** (franja por equipo) | 40 min |
| 5 | 🎯 Reto | **Memoria técnica:** [esqueleto](plantillas/plantilla_esqueleto_memoria_tecnica.md) y [*model card*](plantillas/plantilla_model_card.md) | 1 h 25 min |

**Miércoles 9/12**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 6 | 🎯 Reto | **Mitigar sesgos** detectados y volver a medir | 1 h 5 min |
| 7 | 🎯 Reto | Anota los resultados en el registro de experimentos | 15 min |
| 8 | 🎯 Reto | **Demostrador:** pulir y probarlo en limpio | 40 min |
| 9 | 🎯 Reto | **Model card** del modelo final | 35 min |
| 10 | 🎯 Reto | **Memoria técnica** | 45 min |

**Jueves 10/12**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 11 | 🎯 Reto | **Memoria y verificación en limpio:** clona tu repo en un Colab nuevo y comprueba que todo se ejecuta ([`checklist_congelacion.md`](plantillas/checklist_congelacion.md)) | 1 h |
| 12 | 🎯 Reto | Corrige lo que haya fallado | 20 min |
| 13 | 🎯 Reto | **Vídeo de reserva** de la demo (por si falla internet el día de la defensa) | 30 min |
| 14 | 🎯 Reto | **Checklist de congelación** y [coevaluación](plantillas/plantilla_coevaluacion.md) | 35 min |
| 15 | 🔔 Ceremonia | Review (5 min de demo por equipo) y retro: ¿qué mantenemos?, ¿qué cambiamos? | 35 min |
| 16 | 🔔 Ceremonia | 🔒 **Congelación a las 14:30:** último *push*. Lo que no esté subido, no cuenta (los 30 min finales son el margen) | 20 min |

<!--orden:fin-->

## Entrega / Reto · «Entrega final: evaluar, demostrar y documentar»

📄 [Reto en PDF](guia/Reto_Sprint_16.pdf) · [ecofriendly](guia/Reto_Sprint_16_ecofriendly.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

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
