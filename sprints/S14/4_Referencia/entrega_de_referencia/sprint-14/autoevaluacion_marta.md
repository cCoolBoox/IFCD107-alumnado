# Autoevaluación y coevaluación · «Ficha y datos» (Sprint 14)

> Hoja de **ejemplo** de una persona (Marta) del equipo de referencia. Cada persona sube la suya con su nombre.

## 1. Autoevaluación

**Nombre:** Marta

**Repaso rápido:**

| Pregunta | Mi respuesta |
|---|---|
| ¿La ficha se entregó antes de las 14:30 del día 1 y tiene el **go** del docente? | Sí: entregada a las 13:50 y con «GO con cambios» (versión 2) |
| ¿Los datos son reales, con **fuente y licencia**, y el script o enlace de descarga funciona? | Sí: UCI, CC BY 4.0; el script se probó desde cero |
| ¿El EDA incluye informe de calidad (nulos, duplicados, sesgos, linaje)? | Sí, con la acción tomada en cada hallazgo |
| ¿El baseline usa una métrica técnica definida **antes** de mirar resultados? | Sí: el MAE y el umbral están escritos al principio del cuaderno |
| ¿La partición evita fugas (temporal si hay series)? | Sí, por fechas, con una aserción |
| ¿Hay un backlog de 10–15 historias y el tablero está actualizado? | Sí: 13 historias |
| ¿El registro de riesgos tiene ≥ 5 riesgos específicos? | Sí: 7 |
| ¿El repositorio tiene README, `requirements.txt` y commits de todas las personas? | Sí |
| ¿Hemos hecho coevaluación breve y retro? | Sí; la acción de la retro es el límite de 15 minutos por decisión |

**Puntúate de 1 a 4:**

| Criterio | Mi puntuación (1–4) | Por qué (una frase) | Qué haría para subir un punto |
|---|---|---|---|
| Corrección técnica | 4 | Hallazgo del EDA (hora punta) reflejado en la ficha | Está en el máximo |
| Reproducibilidad | 4 | El script de descarga funciona desde cero y comprueba la huella | Está en el máximo |
| Análisis y comunicación al cliente | 3 | Dice qué decisión mejora, pero el valor en euros no lo sabemos; solo en bicis de error | Pedir al docente un coste por bici mal colocada para llegar a euros |
| IA responsable | 4 | 7 riesgos con medida y un caso concreto de fallo de la IA | Está en el máximo |

- **Lo que más me costó fue** decidir la métrica antes de ver nada, **porque** me daban ganas de mirar primero el resultado del baseline y luego elegir la métrica que mejor quedaba.
- **He usado IA para** listar variables y entender el WAPE, **y lo que he comprobado a mano es** la licencia en la página de la UCI y el número de filas del fichero, que la IA se había inventado.

---

## 2. Coevaluación

**Trabajo revisado de (persona o equipo):** equipo «Los Roques» (ejemplo)  **Revisado por (yo):** Marta

| Entregable | ¿Está y se entiende? | Comentario breve |
|---|---|---|
| `ficha_proyecto.md` | ✔ | La pregunta cabe en una frase y dice qué decisión apoya |
| `plan_datos_licencias.md` | ✘ | La licencia dice «abierta» sin decir cuál; hay que citar la fuente de verdad |
| `01_eda.ipynb` | ✔ | Tiene informe de calidad; faltan los sesgos de muestreo |

| Criterio | Puntuación | Comentario breve |
|---|---|---|
| Corrección técnica | 2 | El *baseline* se calculó antes de escribir la métrica |
| Reproducibilidad | 2 | El README no dice cómo descargar los datos |
| Análisis y comunicación al cliente | 3 | La ficha dice qué pasa hoy sin el modelo |
| IA responsable | 2 | Tres riesgos genéricos sin P ni I |

- **Lo que está muy bien:** la ficha dice con claridad qué decisión mejora y qué pasa hoy sin el modelo.
- **Lo que yo cambiaría, y por qué:** escribiría la métrica antes de calcular el *baseline*, porque si se elige después se puede elegir la que mejor quede.

> Se valora el **trabajo**, no a la persona.
