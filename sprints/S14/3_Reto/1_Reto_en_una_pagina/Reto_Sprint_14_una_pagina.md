# Sprint 14 · Reto «Proyecto final: definir, tener datos y un punto de partida» · en una página

> Versión corta para **trabajar con ella abierta**. La ficha completa (recursos, rúbrica, guía paso a paso, uso de la IA y errores frecuentes) sigue en [Reto_Sprint_14.md](../2_Ficha_completa/Reto_Sprint_14.md); las plantillas están en [`4_Plantillas_y_entrega`](../4_Plantillas_y_entrega/).

**El cliente.** Sois una consultora de IA y el docente es el cliente. Elegís un brief (turismo, cultivos, asistente de FP o energía) o proponéis uno propio. **Aquí todavía no se busca el mejor modelo:** se decide qué hacer, con qué datos y cómo se demostrará que funciona.
**Qué entregáis (no cambia):** ficha de proyecto, plan de datos con licencia, EDA, baseline, backlog y registro de riesgos éticos, más el README y `requirements.txt` del repositorio. **Al final del sprint se suben a `sprint-14/` del repositorio del equipo: 6 ficheros del equipo + 1 autoevaluación y coevaluación por persona** (`autoevaluacion_nombre.md`).
**Tiempo en clase:** 3 jornadas (600 min). Hitos: día 1, brief **antes del descanso** y ficha **antes de las 14:30** · día 2, *go / no-go* · día 3, review y retro.

## Tres niveles: el equipo decide hasta dónde llega

| Nivel | Qué hay que tener | Nota* |
|---|---|---|
| 🟢 **Mínimo** (todos los equipos) | Brief elegido y ficha a tiempo (equipo, pregunta, decisión, métricas) · plan de datos con fuente y licencia · EDA básico (nulos y duplicados) y baseline con su métrica · tres riesgos y clasificación AI Act en la ficha · README corto con el uso de IA | 2 |
| 🟡 **Estándar** | Métrica y partición escritas **antes** de ver resultados, sin fugas · informe de calidad (valores raros, sesgos, linaje) · backlog de 10 a 15 historias con objetivo por sprint y tablero · registro con **5 o más riesgos específicos** y RGPD / AI Act · `requirements.txt` y *commits* de todas las personas · revisión con la rúbrica, coevaluación y retro | 3 |
| 🔴 **Extra** | EDA por subgrupos con un hallazgo que cambia el enfoque · backlog con criterios, tamaño y responsable en todas las historias · mitigaciones de riesgos enlazadas a historias | 4 |

\*Orientativo; puntúa el docente con la rúbrica del reto (0–4 en cada criterio). El mínimo es una entrega válida y evaluable; la «Definition of Done» describe el nivel **estándar**.

## Reparto sugerido de los 600 minutos

| Min | Qué | Se sabe que está hecho cuando… |
|---|---|---|
| 75 | Día 1 · planning, píldora y taller | Roles y uno o dos briefs candidatos |
| 15 | Día 1 · elegir el brief (antes del descanso) | Brief elegido |
| 60 | Día 1 · buscar y validar datos | Una fuente con licencia clara y descarga posible |
| 50 | Día 1 · ficha del proyecto | Subida a `sprint-14/` antes de las 14:30 |
| 200 | Día 2 · *go / no-go*, EDA con informe de calidad y baseline | Métrica y partición escritas antes; los dos cuadernos se ejecutan |
| 140 | Día 3 · backlog, plan ético y README | 10–15 historias, 5 riesgos y un README que otra persona pueda seguir |
| 60 | Día 3 · revisión con la rúbrica, entrega, review (5 min por equipo) y retro | Todo subido y revisión anotada en el README |

## Frases para la ficha (completad los huecos)

- «¿Podemos … con … de antelación y un error menor del …, para que … pueda …?»
- «Hoy, sin el modelo, … decide …; con él podrá …»
- «Nuestro baseline es … y su métrica es …; la definimos **antes** de ver los resultados.»
- «Riesgo: nuestros datos … no representan a …; lo mitigamos …»

## Antes de entregar
- **Archivos subidos en `sprint-14/`:** `ficha_proyecto.md` · `plan_datos_licencias.md` · `01_eda.ipynb` · `02_baseline.ipynb` · `backlog_y_sprints.md` · `riesgos_eticos.md` · `autoevaluacion_nombre.md` (**uno por persona**) = 6 + N ficheros
- [ ] Fuente y licencia de cada dato comprobadas en la web · [ ] los dos cuadernos se ejecutan de arriba abajo · [ ] ≥ 5 riesgos específicos de vuestros datos
- [ ] `README.md` y `requirements.txt` en la raíz, con «Revisión con la rúbrica» rellena · [ ] *commits* de todas las personas, sin claves ni datos personales
- [ ] [Autoevaluación y coevaluación](../4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md): **una por persona**, subida a `sprint-14/`
