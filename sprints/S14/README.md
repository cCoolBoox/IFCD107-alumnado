# README Sprint S14 · Proyecto · Reto, equipo y datos

**Pregunta guía:** ¿qué problema vamos a resolver, con qué datos y cómo sabremos que lo hemos resuelto?
**Fechas:** 26 al 30 de noviembre · **Horas:** 18 h (1 h teoría · 3 h práctica · 14 h PBL) · **Hitos:** 26/11 elección de brief · 27/11 ficha aprobada (go / no-go)

📄 **Este README en PDF:** [a color](README_Sprint_14.pdf) · [ecofriendly, para imprimir](README_Sprint_14_ecofriendly.pdf) (descárgalo para que funcionen los enlaces; la vista previa de GitHub no los abre).

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
- Haber hecho (o leído) la guía [«¿Cuántos sprints tiene el proyecto?»](../S13/plantillas/guia_cuantos_sprints_tiene_el_proyecto.md): son 4 sprints fijos (14–17) y lo que se decide es qué cabe en ellos.
- Repositorio Git y tablero (Trello o similar) del equipo creados. Si no están, es lo primero.

## 📎 Materiales del sprint

**Documentos del curso** (PDF y .md; las actividades van en la tabla siguiente)

| Material | Tema | Tiempo | Cuándo |
|---|---|---|---|
| [Guía del sprint (PDF)](guia/Guia_Sprint_14.pdf) · [ecofriendly](guia/Guia_Sprint_14_ecofriendly.pdf) | Resumen del sprint: qué aprenderás, temario, material, reto y conclusión | 2 páginas | Antes de empezar |
| [Reto completo, paso a paso (.md)](guia/Reto_Sprint_14.md) · [PDF](guia/Reto_Sprint_14.pdf) · [ecofriendly](guia/Reto_Sprint_14_ecofriendly.pdf) | Qué pide el cliente, pasos, rúbrica, ayudas y errores frecuentes | — | Antes del planning y durante el reto |
| [Resumen del sprint en una página](infografias/S14_00_resumen_del_sprint.png) | Lámina con la pregunta del cliente, los pasos, lo que se entrega y lo que se aprende | — | Antes del planning |
| [Infografías del reto](infografias/) | 3 láminas ilustradas del reto | — | Reto |
| [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md) | El método de trabajo de todos los retos | — | Antes del primer reto |
| [`S14.1_Lanzamiento_del_proyecto_final.pdf`](presentaciones/S14.1_Lanzamiento_del_proyecto_final.pdf) | Lanzamiento del proyecto final: cómo formular un proyecto de IA (canvas y criterios de éxito) | 25 min | Teoría · jueves 26/11 |

**Material de las actividades**

Este sprint no tiene notebooks: hay sesiones y plantillas (todas en esta carpeta).

| Fecha | Qué hacéis |
|---|---|
| 26/11 | Planning, píldora «cómo formular un proyecto de IA» y taller de Design Thinking; **elección de brief (antes del descanso, hacia las 11:00)**; datos y licencias; ficha **antes de las 14:30**. |
| 27/11 | **Go / no-go** de la ficha; EDA con informe de calidad; baseline terminado y registrado. |
| 30/11 | Plan ético, backlog y README; entrega, review y retrospectiva (últimos 80 min). |

- [`plantilla_ficha_proyecto.md`](plantillas/plantilla_ficha_proyecto.md) · ficha de 1 página.
- [`plantilla_plan_datos_licencias.md`](plantillas/plantilla_plan_datos_licencias.md) · fuentes, licencias y linaje.
- [`plantilla_registro_riesgos_eticos.md`](plantillas/plantilla_registro_riesgos_eticos.md) · riesgos éticos y RGPD / AI Act.
- [`plantilla_README_repositorio.md`](plantillas/plantilla_README_repositorio.md) · README del repositorio.
- [`plantilla_backlog_y_sprints.md`](plantillas/plantilla_backlog_y_sprints.md) · historias y objetivos por sprint.

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

**Jueves 26/11**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 1 | 📖 Teoría | [Lanzamiento del proyecto final: cómo formular un proyecto de IA (canvas y criterios de éxito)](presentaciones/S14.1_Lanzamiento_del_proyecto_final.pdf) | 25 min |
| 2 | 🔔 Ceremonia | Planning del sprint: leer las reglas y repartir roles | 10 min |
| 3 | 💻 Práctica | Taller de Design Thinking: empatía, «Cómo podríamos…», dos briefs candidatos y canvas borrador | 40 min |
| 4 | 🎯 Reto | [Elegir el brief](guia/Reto_Sprint_14.md) (**antes del descanso**, hito del día) | 15 min |
| 5 | 🎯 Reto | Buscar y validar datos (licencia, tamaño, acceso; plan de datos: [plantilla](plantillas/plantilla_plan_datos_licencias.md)) | 1 h |
| 6 | 🎯 Reto | [Ficha del proyecto y entrega **antes de las 14:30**](plantillas/plantilla_ficha_proyecto.md) | 50 min |

**Viernes 27/11 · hito: ficha aprobada (go / no-go)**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 7 | 🎯 Reto | [Leer el go / no-go del docente y, si hace falta, corregir la ficha](guia/Reto_Sprint_14.md) | 20 min |
| 8 | 🎯 Reto | [EDA, calidad del dato y *baseline* (paso 5)](guia/Reto_Sprint_14.md) | 3 h |

**Lunes 30/11**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 9 | 🎯 Reto | [Backlog y sprints](plantillas/plantilla_backlog_y_sprints.md), [registro de riesgos éticos](plantillas/plantilla_registro_riesgos_eticos.md) y [README del repositorio](plantillas/plantilla_README_repositorio.md) (paso 6) | 2 h 20 min |
| 10 | 🔔 Ceremonia | Entrega en `sprint-14/`, autoevaluación y coevaluación, review (paso 7: 5 min por equipo) y retrospectiva | 1 h |

<!--orden:fin-->

## Entrega / Reto · «Proyecto final: definir, tener datos y un punto de partida»

📄 [Reto en PDF](guia/Reto_Sprint_14.pdf) · [ecofriendly](guia/Reto_Sprint_14_ecofriendly.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

👉 **[Ver el reto completo, explicado paso a paso](guia/Reto_Sprint_14.md)** (qué se pide, cómo hacerlo, cómo usar la IA, errores frecuentes y autoevaluación).


**Contexto:** sois una consultora de IA y el docente es el cliente. Elegís uno de los 4 briefs de `proyecto-final/briefs_y_rubrica.md` (demanda turística, salud de cultivos, asistente de FP, demanda eléctrica) o presentáis un brief libre (ficha antes del 26/11). Si elegís el brief 3 (asistente con LLM), mirad antes la guía de acceso gratuito a modelos: [`material/Acceso_modelos_de_lenguaje.md`](../../material/Acceso_modelos_de_lenguaje.md).

**Entregáis** (usad el repositorio del equipo, carpeta `sprint-14/`):
- Ficha de proyecto de 1 página y plan de datos y licencias.
- `notebooks/01_eda.ipynb` con informe de calidad del dato y `notebooks/02_baseline.ipynb` con su métrica.
- Backlog (10-15 historias) y tablero; plan ético con ≥ 5 riesgos específicos.
- README del repositorio con `requirements.txt` y commits de todas las personas.

**Reglas:**
- Datos reales, accesibles y con licencia; sin datos personales sensibles.
- Equipos de 3-4; los roles rotan cada sprint (reajuste de equipo solo una vez, hasta el 26/11).
- Cambios de alcance tras el 27/11: se negocian en la review.

**Se valora:** criterios A, B, C, E y G de la rúbrica del proyecto final (`proyecto-final/briefs_y_rubrica.md`).

## ✅ Antes de cerrar el sprint
- [ ] Ficha entregada antes del 27/11 y con **go** del docente.
- [ ] Datos con fuente y licencia documentadas; el enlace o script de descarga funciona.
- [ ] EDA con informe de calidad y baseline con métrica definida antes de ver resultados.
- [ ] Backlog de 10-15 historias y tablero actualizado.
- [ ] Registro de riesgos con ≥ 5 riesgos específicos.
- [ ] Entregable subido a la carpeta `sprint-14/` del repositorio del equipo.
