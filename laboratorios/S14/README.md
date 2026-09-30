# Sprint 14 · Proyecto · Reto, equipo y datos

> **Pregunta guía:** ¿qué problema vamos a resolver, con qué datos y cómo sabremos que lo hemos resuelto?
> **Fechas:** 25 al 30 de noviembre · **Horas:** 19 h (1 h teoría · 3 h práctica · 15 h PBL)
> **Módulo:** M9 · Proyecto final (primer sprint de cuatro)
> **Hitos:** **26/11** elección de brief · **27/11** ficha aprobada por el docente (go / no-go)

En este sprint **no hay notebooks de práctica**: es el sprint en el que el equipo decide *qué* va a hacer y *cómo lo va a demostrar*. Todo lo que se decide aquí condiciona los otros tres sprints. Al terminar, tu equipo tendrá un problema bien definido, datos reales con licencia, un primer análisis y un modelo de referencia (*baseline*).

## Qué aprenderás
1. **Formular un proyecto de IA:** pregunta de negocio, decisión que apoya, métrica de negocio y métrica técnica.
2. **Documentar datos reales:** fuente, licencia, linaje, calidad y limitaciones (requisito R2).
3. **Hacer un EDA orientado a la decisión** y un **baseline** simple con el que comparar los modelos después.
4. **Planificar con Scrum:** backlog de 10-15 historias, objetivo de cada sprint y reparto de roles.
5. **Anticipar riesgos éticos y legales** (RGPD, AI Act) desde el primer día con un plan ético.

## Requisitos previos
- Equipos formados en el Sprint 0 (pueden reajustarse **una sola vez, hasta el 26/11**).
- Haber leído `proyecto-final/briefs_y_rubrica.md` (reglas comunes, requisitos R1-R11, rúbrica y anexos A y B).
- Checklist ético del Sprint 1 y mapa de empatía del Sprint 0 (los retomaréis).
- Repositorio Git y tablero (Trello o similar) del equipo creados. Si no están, es lo primero.

## Cómo se organiza el sprint
No hay tabla de notebooks; hay **sesiones y plantillas**.

| Fecha | Horas | Qué hacéis | Plantilla / resultado |
|---|---|---|---|
| **25/11** | 3 h | *Planning* del sprint (30 min). **Píldora de teoría (1 h):** cómo formular un proyecto de IA: canvas y criterios de éxito. **Taller de Design Thinking (1 h 30):** empatía, «Cómo podríamos…», elegir 1-2 briefs candidatos. | Canvas del proyecto (borrador) |
| **26/11** | 6 h | *Daily* (10 min). **Hito: elección de brief** (antes de las 10:00). Búsqueda y validación de datos (licencia, tamaño, acceso). **Taller de backlog (1 h):** historias de usuario y objetivos por sprint. **Entrega de la ficha antes de las 14:30.** | `plantilla_ficha_proyecto.md`, `plantilla_plan_datos_licencias.md` |
| **27/11** | 6 h | *Daily*. **Hito: go / no-go de la ficha** (el docente responde por la mañana). EDA con informe de calidad del dato. Empezar el baseline. | EDA en notebook, informe de calidad |
| **30/11** | 4 h | Baseline terminado y registrado. Repositorio y README. Plan ético. Backlog completo. **Review y retrospectiva (última hora).** | `plantilla_README_repositorio.md`, `plantilla_registro_riesgos_eticos.md`, `plantilla_backlog_y_sprints.md` |

*Los cambios de alcance después del 27/11 se negocian con el docente en la review del sprint.*

---

## Ficha del reto PBL · «Proyecto final: definir, tener datos y un punto de partida»

### El cliente
Sois una **consultora de IA**. El docente es el **cliente y Product Owner**. Los briefs son abiertos a propósito: vosotros decidís alcance, datos concretos y técnicas dentro de los mínimos. Los cuatro briefs son:

| Brief | Pregunta guía | Datos candidatos (validar) | Carga de cómputo |
|---|---|---|---|
| **1 · Demanda turística** | ¿Podemos predecir la llegada de turistas con 3-6 meses de antelación y qué factores la explican? | ISTAC, Frontur-Canarias, datos.gob.es, AEMET | Baja |
| **2 · Salud de cultivos (visión)** | ¿Con qué fiabilidad se distingue una hoja sana de una enferma, y cuándo no fiarnos? | PlantVillage + fotos propias del equipo | Alta (GPU) |
| **3 · Asistente de FP (LLM/RAG)** | ¿Puede un asistente responder sin inventar, y cómo lo medimos? | Catálogo oficial de FP y FAQ del centro | Media |
| **4 · Demanda eléctrica** | ¿Predecimos la demanda de las próximas 24 h mejor que un modelo de referencia? | REData, AEMET, calendario laboral | Media |

También podéis presentar un **brief libre** (ficha antes del 26/11), que debe cumplir R1-R11, tener datos reales ya identificados, dificultad comparable y no usar datos personales sensibles.

### Qué se entrega
Al cierre del sprint (30/11), en el repositorio del equipo:
1. **Ficha de proyecto de 1 página** (anexo A) — entrega antes del 27/11 para el go / no-go.
2. **Plan de datos y licencias** (fuente, licencia, tamaño, variables, limitaciones, linaje).
3. **Datos + EDA** en un notebook (`notebooks/01_eda.ipynb`) con **informe de calidad del dato**.
4. **Baseline** simple con su métrica (`notebooks/02_baseline.ipynb`).
5. **Backlog** (10-15 historias) con objetivos por sprint, y tablero con las primeras evidencias Scrum.
6. **Plan ético:** checklist del Sprint 1 actualizado y registro de riesgos inicial.
7. **Repositorio** con README (plantilla), requisitos y commits de todas las personas.

### Restricciones
- 19 h en total; ~55 h de proyecto en los 3 primeros sprints. Se descartan problemas triviales o irrealizables.
- **Datos reales, accesibles y con licencia.** No se aceptan proyectos «a la espera de datos». No datos personales sensibles ni de terceros sin autorización.
- Dos equipos pueden elegir el mismo brief, pero cada uno define **su propia pregunta y métrica**.
- Equipos de 3-4 personas; los roles (Scrum Master, responsable técnico, de datos y de IA responsable) **rotan** cada sprint.

### Criterios de evaluación
El proyecto se evalúa con la **rúbrica de 100 puntos** (documento de briefs, sección 5). En este sprint se evidencian:

| Criterio del proyecto | Qué se mira en el Sprint 14 |
|---|---|
| **A · Problema y valor de negocio (10)** | Pregunta clara, decisión del cliente, métricas de negocio y técnica coherentes |
| **B · Datos y EDA (10)** | Fuente y licencia documentadas, EDA orientado a la decisión, calidad del dato |
| **C · Modelado (20)** | Baseline razonable y plan de ≥ 3 modelos (incluye redes neuronales o LLM/RAG) |
| **E · IA responsable (10)** | Plan ético inicial con riesgos específicos y clasificación RGPD / AI Act preliminar |
| **G · Equipo y metodología (10)** | Tablero, backlog, planning y primera retro; commits de todos |

Además, para la nota de sprint se usan los cuatro criterios de los retos (corrección técnica, reproducibilidad, análisis y comunicación al cliente, IA responsable).

### Pasos sugeridos (resumen día a día)
| Día | Paso |
|---|---|
| 25/11 | Planning; píldora; taller DT; 2 briefs candidatos; canvas borrador. |
| 26/11 | Elegir brief; buscar y validar datos (¿licencia?, ¿descarga?, ¿tamaño?); rellenar ficha y plan de datos; **entregar la ficha antes de las 14:30**. |
| 27/11 | Leer el go / no-go; corregir la ficha si hace falta; EDA con calidad del dato; primer baseline. |
| 30/11 | Baseline registrado; plan ético; backlog completo; README; review y retro. |

### Qué se enseña en la review (30/11)
Cada equipo enseña en 5 minutos: (1) la pregunta de negocio y la decisión que apoyará; (2) los datos y un hallazgo del EDA que cambia el enfoque; (3) el baseline y su métrica; (4) tres riesgos éticos; (5) el backlog de los próximos sprints. Después, retrospectiva de 15 minutos.

### Definition of Done del sprint
- [ ] Ficha de proyecto entregada antes del 27/11 y con **go** del docente.
- [ ] Datos reales con **fuente y licencia** documentadas; el script o enlace de descarga funciona desde el README.
- [ ] EDA con informe de calidad del dato (nulos, duplicados, sesgos de muestreo, linaje).
- [ ] Baseline evaluado con una **métrica técnica** definida antes de mirar resultados.
- [ ] Partición de datos definida (y **temporal** si hay series) para evitar fugas.
- [ ] Backlog de 10-15 historias, objetivos por sprint y tablero actualizado.
- [ ] Checklist ético actualizado y registro de riesgos con ≥ 5 riesgos específicos.
- [ ] Repositorio con README, `requirements.txt` y *commits* de **todos** los integrantes.
- [ ] Coevaluación breve de la primera semana y retrospectiva realizadas.

## Plantillas de este sprint (en esta carpeta)
- `plantilla_ficha_proyecto.md` — la ficha de 1 página (anexo A).
- `plantilla_plan_datos_licencias.md` — inventario de datos, licencias y linaje.
- `plantilla_registro_riesgos_eticos.md` — checklist ético del Sprint 1 actualizado + registro de riesgos + clasificación RGPD / AI Act.
- `plantilla_README_repositorio.md` — README del repositorio del equipo.
- `plantilla_backlog_y_sprints.md` — historias de usuario, objetivos por sprint y ceremonias.

## Recursos
- `proyecto-final/briefs_y_rubrica.md` (obligatorio): requisitos R1-R11, rúbrica y anexos.
- Portales de datos abiertos: ISTAC, datos.gob.es, Open Data Canarias, REData (Red Eléctrica), AEMET OpenData, Kaggle y TensorFlow Datasets.
- Guía de licencias: Creative Commons (<https://creativecommons.org/licenses/>) y la licencia de datos abiertos de cada portal.
- Agencia Española de Protección de Datos (aepd.es): guías sobre RGPD y anonimización.
- Guía del usuario de Scrum (scrumguides.org) para repasar las ceremonias.
