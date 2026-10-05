# Sprint 16 · Proyecto · Evaluación, IA responsable y entrega

## 📎 Material del sprint

- 🖥️ **S16.1 · Pildora demostrador y documentacion:** [`S16.1_Pildora_demostrador_y_documentacion.pdf`](presentaciones/S16.1_Pildora_demostrador_y_documentacion.pdf)

> **Pregunta guía:** ¿es nuestro modelo lo bastante bueno, justo y seguro para entregarlo, y puede otra persona reproducirlo?
> **Fechas:** 4 al 10 de diciembre · **Horas:** 18 h (1 h teoría · 3 h práctica · 14 h PBL)
> **Módulo:** M9 · Proyecto final (tercer sprint)
> **Hito: 10/12 a las 14:30 · congelación del repositorio y de la memoria**

Sesiones de clase: **4/12, 9/12 y 10/12** (6 h cada una). *No hay clase el 7 y el 8/12.* Si el equipo trabaja esos días, que lo planifique, pero el plan del sprint cabe en las 18 h.

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

## Sesiones y prácticas

| Fecha | Horas | Qué hacéis |
|---|---|---|
| **4/12** | 6 h | Planning (30 min). Píldora (1 h) y notebook `S16_01` (1 h 15). **Tutoría de evaluación de sesgos y visualización (3 h de práctica repartidas por equipos).** Evaluación final del candidato, análisis de errores y de sesgos. |
| **9/12** | 6 h | Daily. Mitigación de sesgos y medición del efecto. Demostrador (Streamlit, Gradio, widgets o API). Model card y borrador de memoria. |
| **10/12** | 6 h | Daily. Cierre de la memoria, pruebas del demostrador desde cero, vídeo plan B. **Congelación a las 14:30** (checklist en esta carpeta). Review y retro *(antes de las 14:30 si es posible; si no, la retro puede hacerse el 11/12)*. |

| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| `S16_01_demostrador` | Plantilla de demostrador: modelo + metadatos, lógica separada, pruebas, Streamlit (`app.py`), widgets y API (opcional) | 1 h 15 | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S16/S16_01_demostrador.ipynb) |

Plantillas de esta carpeta:
- `plantilla_esqueleto_memoria_tecnica.md` — memoria de 10-15 páginas con presupuesto de páginas y mapa R1-R11.
- `plantilla_model_card.md` — tarjeta del modelo.
- `plantilla_coevaluacion.md` — formulario de coevaluación (anexo B).
- `checklist_congelacion.md` — lo que debe estar hecho antes del 10/12 a las 14:30.
- `plantillas/demostrador/` — `logica.py`, `app.py`, `api.py`, `requirements.txt` y `README_demostrador.md` (generados y comprobados con el notebook `S16_01`).

---

## Ficha del reto PBL · «Entrega final: evaluar, demostrar y documentar»

### El cliente
El cliente (el docente) va a **recibir vuestro trabajo como si fuera un entregable real**: quiere clonar el repositorio, seguir el README, ver funcionar el demostrador, leer una memoria de 10-15 páginas y entender los riesgos antes de decidir si lo adopta.

### Qué se entrega (todo congelado el 10/12 a las 14:30)
1. **Evaluación final** del modelo candidato en el test, con **visualizaciones** y **análisis de errores** (`notebooks/04_evaluacion.ipynb`).
2. **Análisis de sesgos y limitaciones** por subgrupos, con **medida de mitigación aplicada y evaluada**.
3. **Registro de riesgos éticos cerrado** y clasificación RGPD / AI Act.
4. **Demostrador ejecutable** (Streamlit / Gradio / notebook interactivo / endpoint), con manejo de errores del usuario, aviso de incertidumbre y **plan B en vídeo**.
5. **Repositorio reproducible:** README, `requirements.txt` con versiones fijas, datos o script de descarga, pruebas, commits de todos.
6. **Model card** y **memoria técnica** (10-15 páginas, PDF).
7. **Coevaluación** individual (anexo B) rellenada por cada persona.

### Restricciones
- **A las 14:30 del 10/12 se congela el repositorio y la memoria.** Se evaluará lo que haya en la rama principal en ese momento (etiqueta `v1.0-entrega`).
- Memoria de **10 a 15 páginas** (los anexos no cuentan). Autocontenida y propia (no copiada).
- El demostrador debe funcionar **desde cero** en otro equipo.
- Sin datos personales, claves ni credenciales en el repositorio.

### Criterios de evaluación
Rúbrica del proyecto (100 puntos). En este sprint pesan:

| Criterio | Qué se mira |
|---|---|
| **D · Evaluación y visualización (10)** | Análisis de errores, gráficos claros, interpretación del modelo, incertidumbre |
| **E · IA responsable (10)** | Sesgos, limitaciones, riesgo RGPD / AI Act, mitigación aplicada **y evaluada** |
| **F · Demostrador y reproducibilidad (10)** | Funciona, se reproduce desde el README, versiones fijas, pruebas, errores del usuario |
| **G · Equipo (10)** | Sprints completos, roles rotados, commits repartidos, mejora entre retros, coevaluación |
| **H · Memoria (5)** | Completa, clara, con figuras, referencias y conclusiones accionables |
| **C · Modelado (20)** | Rigor de la comparativa y de la justificación (se cierra aquí) |

*La coevaluación y el historial de commits ajustan la nota individual con un factor de 0,8 a 1,1.*

### Pasos sugeridos
| Cuándo | Paso |
|---|---|
| 4/12 | Evaluación final en test (una sola vez). Gráficos de la plantilla `S13_02` adaptados. Métricas por subgrupos. Lista de errores más frecuentes con ejemplos. |
| 9/12 | Mitigación de sesgos + medición del efecto. Demostrador funcionando con la plantilla de `S16_01`. Model card. Borrador de la memoria (secciones 1-6). |
| 10/12 | Memoria completa; **prueba de reproducibilidad en un ordenador limpio**; vídeo plan B; checklist de congelación; coevaluación; retro. |

### Qué se enseña en la review
Demostración de 4 minutos del demostrador (con una entrada errónea a propósito), una diapositiva con el análisis de sesgos y la medida aplicada, y la lista de riesgos altos con su estado. El docente propone **una entrada difícil** para probar el demostrador en directo.

### Definition of Done del sprint
- [ ] Evaluación final en test hecha **una sola vez**, con gráficos y análisis de errores.
- [ ] Rendimiento **por subgrupos** y medida de mitigación aplicada y medida.
- [ ] Registro de riesgos cerrado; clasificación RGPD / AI Act justificada.
- [ ] Demostrador funcionando desde cero, con entradas erróneas gestionadas y aviso de incertidumbre.
- [ ] Pruebas (`pytest -q`) y vídeo plan B.
- [ ] `requirements.txt` con versiones; README reproducible probado por otra persona del equipo.
- [ ] Model card y memoria (10-15 páginas) en PDF dentro de `docs/`.
- [ ] Etiqueta `v1.0-entrega` creada antes de las 14:30 del 10/12.
- [ ] Coevaluación entregada por **cada** integrante; retro hecha.

## Recursos
- Notebook `S16_01_demostrador` y carpeta `plantillas/demostrador/`.
- Documentación de Streamlit (<https://docs.streamlit.io>) y de FastAPI (<https://fastapi.tiangolo.com>, opcional).
- «Model Cards for Model Reporting», Mitchell et al. (2019): origen del formato de la model card.
- Agencia Española de Protección de Datos (aepd.es) y texto del Reglamento Europeo de IA en EUR-Lex (verifica el calendario de aplicación con el docente).
- Guía de SHAP (<https://shap.readthedocs.io>) o de Grad-CAM (según vuestro caso).
