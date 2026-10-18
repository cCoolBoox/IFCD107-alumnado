# Sprint 14 · Reto «Proyecto final: definir, tener datos y un punto de partida»

> **Esta es la ficha completa del reto, explicada paso a paso** para quien nunca ha trabajado con esta metodología ni con IA. Léela entera **antes de empezar** y vuelve a ella cuando tengas dudas.
>
> - Si es tu primer reto, lee antes [Cómo se trabaja un reto](../../../material/4.%20Como_se_trabaja_un_reto.md).
> - Volver al [README del sprint](../README.md) · [Guía del sprint en PDF](Guia_Sprint_14.pdf) · [versión ecofriendly para imprimir](Guia_Sprint_14_ecofriendly.pdf).
> - **Este reto en PDF:** [a color](Reto_Sprint_14.pdf) · [ecofriendly, para imprimir](Reto_Sprint_14_ecofriendly.pdf).

## Ficha del reto

### En pocas palabras (léelo primero)

**Qué es el proyecto final.** Hasta ahora habéis resuelto retos con un guion. En los **sprints 14 a 17** vais a hacer **un proyecto completo de principio a fin**, igual que en una consultora: elegir un problema, conseguir datos reales, construir modelos, evaluarlos con honestidad, documentarlo y **defenderlo ante un cliente**. Aquí **vosotros decidís** el alcance, los datos concretos y las técnicas, dentro de unos mínimos.

**Qué es este sprint (el primero de los cuatro).** Aquí **no se entrena todavía el mejor modelo**. Se decide **qué** vais a hacer y **cómo vais a demostrar que funciona**. Lo que decidáis ahora condiciona los otros tres sprints, así que **conviene dedicar tiempo a pensar y no tener prisa por programar**. Al final tendréis: un problema bien definido, datos reales con licencia, un primer análisis y un modelo de referencia (*baseline*).

**Qué vais a hacer, en siete pasos:**
1. **Elegir un brief** (de los cuatro propuestos o uno propio) y escribir una **[ficha de proyecto](../plantillas/plantilla_ficha_proyecto.md) de una página**.
2. **Encontrar datos reales** que podáis usar legalmente y documentar su fuente y licencia ([plan de datos y licencias](../plantillas/plantilla_plan_datos_licencias.md)).
3. **Hacer el EDA** (análisis exploratorio) y un **informe de calidad del dato**.
4. **Construir un baseline**: el modelo más sencillo posible, con una métrica definida **antes** de ver resultados.
5. **Planificar con Scrum**: [backlog](../plantillas/plantilla_backlog_y_sprints.md) de 10–15 historias y objetivos para cada sprint.
6. **Anticipar riesgos éticos y legales** ([plan ético](../plantillas/plantilla_registro_riesgos_eticos.md), RGPD y AI Act).
7. **Montar el repositorio** con [README](../plantillas/plantilla_README_repositorio.md) y commits de todas las personas.

**Hitos que no se pueden perder:**
- **26/11:** elección de brief (antes de las 10:00) y **entrega de la ficha antes de las 14:30**.
- **27/11:** **go / no-go** del docente sobre vuestra ficha.
- **30/11:** review y retro.

**Qué vais a aprender haciéndolo:** a **formular un proyecto de IA** (pregunta de negocio, decisión que apoya, métricas), a **documentar datos** y a **planificar** con Scrum.

**Cuánto tiempo:** 19 horas (25 al 30/11), de las que 15 son de proyecto.

### Palabras que van a aparecer en este reto

| Palabra | Qué significa, en sencillo |
|---|---|
| **Brief** | El enunciado de un proyecto: qué problema, qué cliente y qué se espera |
| **Ficha de proyecto** | Una página que resume tu proyecto: pregunta, decisión, datos, métricas, riesgos |
| **Métrica de negocio** | Lo que le importa al cliente, en sus términos (euros ahorrados, horas, errores evitados) |
| **Métrica técnica** | Lo que mide el modelo (MAE, AUC, F1…). Se define **antes** de mirar resultados |
| **Datos abiertos** | Datos que se pueden usar libremente gracias a una licencia (ISTAC, datos.gob.es, REData…) |
| **Licencia** | El permiso que dice qué podéis hacer con unos datos. Sin licencia clara, no se usan |
| **Linaje (procedencia) del dato** | De dónde viene, quién lo generó y qué transformaciones ha sufrido |
| **EDA** | Análisis exploratorio: tablas y gráficos para entender los datos |
| **Informe de calidad** | Resumen de nulos, duplicados, sesgos y límites del dato |
| **Baseline** | Modelo muy simple de referencia. Todo modelo posterior debe superarlo |
| **Go / no-go** | La decisión del docente: «adelante» o «hay que cambiar esto» |
| **Backlog** | Lista de tareas (historias) pendientes, ordenadas por importancia |
| **Historia de usuario** | Una tarea escrita desde el punto de vista de quien se beneficia: «Como cliente, quiero…» |
| **Plan ético / registro de riesgos** | Lista de riesgos éticos y legales, con su gravedad y su medida |
| **RGPD / AI Act** | Normas europeas de protección de datos y de inteligencia artificial |
| **Partición temporal** | Entrenar con el pasado y evaluar con el futuro. Obligatoria si hay series temporales |

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

### Guía paso a paso para principiantes

#### Antes de empezar: leed las reglas
Leed [`briefs_y_rubrica.md`](../../../proyecto-final/briefs_y_rubrica.md): las reglas comunes, los **requisitos R1–R11**, la **rúbrica de 100 puntos** y los anexos A y B. Es el documento que dice qué se va a evaluar. **Subrayad** lo que no entendáis y llevadlo al planning.

#### Paso 1 · Planning y taller (25/11)
1. Roles del sprint: Scrum Master, responsable técnico, **responsable de datos** y **responsable de IA responsable**. Rotan cada sprint.
2. En la **píldora de teoría** aprenderéis a formular el proyecto con un *canvas* (un esquema de una página).
3. En el **taller de Design Thinking** pensad: ¿qué problema real y cercano os interesa? ¿Quién lo sufre? Salid con **uno o dos briefs candidatos**.

#### Paso 2 · Elegir el brief (26/11 por la mañana, antes de las 10:00)
Los cuatro briefs:

| Brief | Pregunta guía | Pensad en… |
|---|---|---|
| **1 · Demanda turística** | ¿Podemos predecir la llegada de turistas con 3–6 meses de antelación y qué factores la explican? | Series temporales. Carga de cómputo baja |
| **2 · Salud de cultivos (visión)** | ¿Con qué fiabilidad se distingue una hoja sana de una enferma y cuándo no fiarnos? | Imágenes. Carga alta (GPU) |
| **3 · Asistente de FP (LLM/RAG)** | ¿Puede un asistente responder sin inventar y cómo lo medimos? | Texto. Carga media |
| **4 · Demanda eléctrica** | ¿Predecimos la demanda de las próximas 24 h mejor que un modelo de referencia? | Series temporales con calendario. Carga media |

**Cómo elegir:** el brief que os interese, para el que haya **datos reales accesibles** y que se pueda terminar en el tiempo que hay. **Dos equipos pueden elegir el mismo brief**, pero cada uno define **su propia pregunta y métrica**. También podéis proponer un **brief libre**, con ficha antes del 26/11 y cumpliendo R1–R11.

#### Paso 3 · Buscar y validar datos (26/11)
Para cada fuente candidata, responded:
- **¿Tiene licencia que permita usarla?** (si no está clara, no se usa).
- **¿Se puede descargar?** Y ¿podemos repetir la descarga con un enlace o un script?
- **¿Qué tamaño tiene?** ¿Cabe en nuestro ordenador o en Colab?
- **¿Qué variables y qué periodo?** ¿Responden a nuestra pregunta?
- **¿Hay datos personales?** (si los hay y son sensibles, **no se aceptan**).

Rellenad la plantilla [`plantilla_plan_datos_licencias.md`](../plantillas/plantilla_plan_datos_licencias.md).

**No se aceptan proyectos «a la espera de datos».** Los datos han de estar identificados y accesibles.

#### Paso 4 · Ficha del proyecto y entrega (26/11, antes de las 14:30)
Rellenad [`plantilla_ficha_proyecto.md`](../plantillas/plantilla_ficha_proyecto.md) (anexo A del documento de briefs), con:
1. **Pregunta de negocio** y **decisión que apoyará** el proyecto.
2. **Métricas** (de negocio y técnica).
3. **Datos** (fuente, licencia).
4. **Enfoque** previsto (baseline + ≥ 3 modelos + 1 neuronal o LLM/RAG).
5. **Riesgos principales.**
6. **Equipo y roles.**

**Entregadla antes de las 14:30 del 26/11.** El docente responderá con el **go / no-go** al día siguiente por la mañana.

#### Paso 5 · EDA, calidad del dato y baseline (27/11)
1. **Leed el go / no-go** y corregid la ficha si hace falta.
2. En `notebooks/01_eda.ipynb`: describid los datos, buscad nulos, duplicados, valores raros y **sesgos de muestreo** (¿quién o qué falta en los datos?). Terminad con un **informe de calidad del dato**.
3. **Definid la partición** de datos (temporal si hay series) y la **métrica técnica ANTES de mirar resultados**.
4. En `notebooks/02_baseline.ipynb`: construid el **modelo más simple posible** (por ejemplo, «predecir lo mismo que ayer», la media, o la clase más frecuente) y calculad su métrica. Es el **suelo** que vais a intentar superar.

#### Paso 6 · Backlog, plan ético y repositorio (30/11)
1. **Backlog** con [`plantilla_backlog_y_sprints.md`](../plantillas/plantilla_backlog_y_sprints.md): entre 10 y 15 historias con objetivos para los sprints 15, 16 y 17. Cargadlas en el tablero.
2. **Plan ético:** actualizad el [checklist del Sprint 1](../../S01/plantillas/checklist_etico_v1.md) y rellenad [`plantilla_registro_riesgos_eticos.md`](../plantillas/plantilla_registro_riesgos_eticos.md) con **al menos 5 riesgos específicos** de vuestro proyecto (no genéricos), y una primera clasificación RGPD / AI Act.
3. **Repositorio:** README con [`plantilla_README_repositorio.md`](../plantillas/plantilla_README_repositorio.md), `requirements.txt`, notebooks, datos o script de descarga. **Commits de todas las personas.**
4. **Coevaluación breve** de la primera semana.

#### Paso 7 · Review (30/11)
5 minutos por equipo: (1) pregunta de negocio y decisión que apoyará; (2) datos y **un hallazgo del EDA que cambia el enfoque**; (3) baseline y su métrica; (4) tres riesgos éticos; (5) backlog de los próximos sprints. Después, retro de 15 minutos.

### Cómo usar la IA en este reto

En un proyecto largo, la IA puede ayudar mucho, pero **la responsabilidad es vuestra**.

| Para qué | Ejemplo de petición | Qué tenéis que comprobar |
|---|---|---|
| Encontrar fuentes de datos | «Dame fuentes abiertas de datos de llegada de turistas a Canarias y qué licencias suelen tener» | **Entrad vosotros en la web**, leed la licencia y comprobad que los datos existen. Una IA puede inventar fuentes |
| Redactar la ficha | «Ayúdame a convertir estas notas en una pregunta de negocio clara con una métrica» | Que sea **vuestra** idea, no una genérica |
| Planificar | «Convierte este objetivo en 5 historias de usuario pequeñas» | Que son realizables en el tiempo que tenéis |
| Revisar riesgos | «Para un proyecto de [vuestro brief], ¿qué riesgos éticos y de protección de datos debería considerar?» | Que se aplican a **vuestro** caso y vuestras medidas son reales |

**Reglas del reto:**
- **Nunca inventéis una fuente o una licencia.** Si la IA os da un enlace, entrad y comprobadlo.
- **No subáis datos personales ni claves** al repositorio.
- Declarad en el README del proyecto el uso de IA.
- Se exige un proyecto **propio**: no se acepta copiar un notebook de internet.

### Errores frecuentes (y cómo evitarlos)

| Error | Por qué ocurre | Cómo evitarlo |
|---|---|---|
| Elegir un problema demasiado grande | Ambición | Preguntaos: ¿se puede hacer en ~55 horas de proyecto? |
| Elegir datos sin mirar la licencia | Se quiere avanzar | La licencia es lo primero que se comprueba |
| Definir la métrica después de ver resultados | «Para que salga bien» | Escribidla en la ficha y no la cambiéis |
| Baseline demasiado complicado | Se quiere lucir | El baseline es **lo más simple posible** |
| Backlog con 40 tareas vagas | Se apunta todo | 10–15 historias concretas |
| Riesgos éticos genéricos («cuidado con los sesgos») | Prisa | Cinco riesgos específicos de **vuestros** datos |
| Un solo commit del responsable técnico | Es más rápido | Todas las personas hacen commits |

### Un buen resultado se parece a…

- **Pregunta de negocio:** «¿Podemos predecir la ocupación hotelera de Gran Canaria con 3 meses de antelación con un error menor del 8 %, para planificar plantilla y compras?».
- **Decisión que apoya:** «Cuándo contratar refuerzo en temporada media».
- **Baseline:** «Predecir lo mismo que el año anterior en la misma semana → error del 14 %».
- **Un riesgo específico:** «Los datos son de hoteles grandes: no representan a pequeños alojamientos rurales».

### Antes de entregar: autoevaluación rápida

| Pregunta | Sí / No |
|---|---|
| ¿La ficha se entregó antes del 27/11 y tiene el **go** del docente? | |
| ¿Los datos son reales, con **fuente y licencia**, y el script o enlace de descarga funciona? | |
| ¿El EDA incluye informe de calidad (nulos, duplicados, sesgos, linaje)? | |
| ¿El baseline usa una métrica técnica definida **antes** de mirar resultados? | |
| ¿La partición evita fugas (temporal si hay series)? | |
| ¿Hay un backlog de 10–15 historias y el tablero está actualizado? | |
| ¿El registro de riesgos tiene ≥ 5 riesgos específicos? | |
| ¿El repositorio tiene README, `requirements.txt` y commits de todas las personas? | |
| ¿Hemos hecho coevaluación breve y retro? | |

### Si os atascáis

- **No nos ponemos de acuerdo en el brief:** votad con criterios (datos disponibles, interés, tiempo) y puntuad cada opción de 1 a 5.
- **No encontramos datos con licencia:** probad primero con las fuentes de la tabla de candidatos (ISTAC, datos.gob.es, REData, PlantVillage…) y consultad al docente **antes del 26/11**.
- **El go / no-go pide cambios:** es normal; corregid la ficha el mismo día.
- Más ayuda: [Cómo se trabaja un reto](../../../material/4.%20Como_se_trabaja_un_reto.md).

### Qué se enseña en la review (30/11)
Cada equipo enseña en 5 minutos: (1) la pregunta de negocio y la decisión que apoyará; (2) los datos y un hallazgo del EDA que cambia el enfoque; (3) el baseline y su métrica; (4) tres riesgos éticos; (5) el backlog de los próximos sprints. Después, retrospectiva de 15 minutos.

## Definition of Done (lista de comprobación)

Si queda una casilla sin marcar, **el reto no está terminado**.

- [ ] Ficha de proyecto entregada antes del 27/11 y con **go** del docente.
- [ ] Datos reales con **fuente y licencia** documentadas; el script o enlace de descarga funciona desde el README.
- [ ] EDA con informe de calidad del dato (nulos, duplicados, sesgos de muestreo, linaje).
- [ ] Baseline evaluado con una **métrica técnica** definida antes de mirar resultados.
- [ ] Partición de datos definida (y **temporal** si hay series) para evitar fugas.
- [ ] Backlog de 10-15 historias, objetivos por sprint y tablero actualizado.
- [ ] Checklist ético actualizado y registro de riesgos con ≥ 5 riesgos específicos.
- [ ] Repositorio con README, `requirements.txt` y *commits* de **todos** los integrantes.
- [ ] Coevaluación breve de la primera semana y retrospectiva realizadas.
