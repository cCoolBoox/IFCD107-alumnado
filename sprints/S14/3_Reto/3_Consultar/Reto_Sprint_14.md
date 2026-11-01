# Sprint 14 · Reto «Proyecto final: definir, tener datos y un punto de partida»

> **Ficha completa del reto, para consultar.** Para trabajar, [el reto en una página](../1_Trabajar/Reto_Sprint_14_una_pagina.md). Qué se sube y cómo se evalúa: [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md).
>
> - Volver al [README del sprint](../../README.md).
> - Si es vuestro primer reto: [Cómo se trabaja un reto](../../../../material/4.%20Como_se_trabaja_un_reto.md).
> - Reglas del proyecto final (requisitos R1–R11, rúbrica de 100 puntos, anexos A y B): [`briefs_y_rubrica.md`](../../../../proyecto-final/briefs_y_rubrica.md).

## Ficha del reto

### 1 · 🎯 Qué os pide el cliente

**Qué os pide el cliente.** Sois una **consultora de IA** y el docente es el **cliente y Product Owner**. En los sprints 14 a 17 vais a hacer **un proyecto completo de principio a fin**: elegir un problema, conseguir datos reales, construir modelos, evaluarlos con honestidad y defenderlo. Este es el **primer sprint de los cuatro** y en él **todavía no se entrena el mejor modelo**: se decide **qué** vais a hacer y **cómo vais a demostrar que funciona**. Lo que decidáis ahora condiciona los otros tres sprints, así que conviene pensar antes de programar. Al terminar tendréis: un problema bien definido (la **ficha de proyecto**), **datos reales con licencia**, un primer análisis de esos datos (**EDA**), un modelo de referencia muy sencillo (**baseline**), un **backlog** (lista de tareas ordenada), un **registro de riesgos éticos** y un repositorio ordenado.

**Cómo se trabaja.** No hay un guion con pruebas como en otros retos: **vosotros decidís** el alcance, los datos concretos y las técnicas, dentro de unos mínimos. Elegís uno de **cuatro briefs** (demanda turística, salud de cultivos con imágenes, asistente de FP con un modelo de lenguaje o demanda eléctrica) o proponéis uno propio. Os damos **plantillas** para la ficha, el plan de datos, el backlog, el registro de riesgos y el README; vuestro trabajo es rellenarlas con criterio. En clase tenéis **tres jornadas** (600 minutos de sprint): día 1, elegir brief, validar datos y entregar la ficha **antes de las 14:30**; día 2, el docente responde **go / no-go** y hacéis el EDA y el baseline; día 3, backlog, riesgos, README, entrega, review y retro. El equipo decide hasta dónde llega: 🟢 mínimo, 🟡 estándar o 🔴 extra.

---

### 2 · 🧰 Recursos del reto

| Recurso | Para qué lo usaréis | Dónde está |
|---|---|---|
| **Las reglas del proyecto**: [`briefs_y_rubrica.md`](../../../../proyecto-final/briefs_y_rubrica.md) | Saber qué se evalúa (R1–R11), leer los cuatro briefs y la rúbrica de 100 puntos | Léelo antes del planning; subrayad lo que no entendáis |
| **Presentación S14.1** [Lanzamiento del proyecto final](../../1_Teoria/S14.1_Lanzamiento_del_proyecto_final.pdf) y sus [apuntes](../../1_Teoria/apuntes/apuntes_formular_un_proyecto_de_ia.md) | Aprender a formular un proyecto de IA con un *canvas* (un esquema de una página) | El docente la explica el día 1 (25 minutos) |
| **Plantilla de la ficha** [`plantilla_ficha_proyecto.md`](../1_Trabajar/plantillas/plantilla_ficha_proyecto.md) | Resumir el proyecto en una página (anexo A) | Copiadla como `ficha_proyecto.md` |
| **Plantilla del plan de datos** [`plantilla_plan_datos_licencias.md`](../1_Trabajar/plantillas/plantilla_plan_datos_licencias.md) | Documentar fuente, licencia, variables, calidad, linaje y partición | Copiadla como `plan_datos_licencias.md` |
| **Plantilla del backlog** [`plantilla_backlog_y_sprints.md`](../1_Trabajar/plantillas/plantilla_backlog_y_sprints.md) | Historias de usuario, objetivo de cada sprint y retrospectivas | Copiadla como `backlog_y_sprints.md` |
| **Plantilla del registro de riesgos** [`plantilla_registro_riesgos_eticos.md`](../1_Trabajar/plantillas/plantilla_registro_riesgos_eticos.md) | Checklist ético, clasificación RGPD / AI Act y registro de riesgos | Copiadla como `riesgos_eticos.md` |
| **Plantilla del README** [`plantilla_README_repositorio.md`](../1_Trabajar/plantillas/plantilla_README_repositorio.md) | Explicar el proyecto para que otra persona lo ejecute solo con ese README | Copiadla como `README.md`. Al final lleva la sección «Revisión con la rúbrica» |
| **Fuentes de datos candidatas** (ISTAC, Frontur-Canarias, datos.gob.es, AEMET, REData, PlantVillage, catálogo oficial de FP) | Encontrar datos reales y legales | En la tabla de briefs del paso 2. **Entrad vosotros en la web y leed la licencia** |
| **Acceso gratuito a modelos de lenguaje** | Solo si elegís el brief 3 (asistente de FP) | [Guía de acceso](../../../../material/Acceso_modelos_de_lenguaje.md) |
| **Google Colab** (o vuestro Python) | Escribir y ejecutar `01_eda.ipynb` y `02_baseline.ipynb` | Colab no necesita instalar nada. Este sprint no tiene cuadernos de práctica propios; os sirven de apoyo los de pandas y limpieza del Sprint 6 (`S06_01` y `S06_02`) |
| **Tablero del equipo** (Trello o similar) | Cargar las historias del backlog y mover las tareas | El del equipo. Si no existe, es lo primero que se crea |
| **Cómo entregar en GitHub** | Subir los ficheros a `sprint-14/` | [Guía de entrega](../../../../material/5.%20Como_entregar_en_GitHub.md) |
| **Autoevaluación y coevaluación** | Cada persona rellena su hoja | [Hoja del sprint](../2_Entregar/autoevaluacion_y_coevaluacion.md) |
| **Un asistente de IA** (opcional) | Ideas, borradores y revisión | Con las reglas de la «Ayuda 1» del paso a paso |

---

### 3 · 🪜 Guía paso a paso

Son siete pasos, de **600 minutos en total** (200 por jornada, tres jornadas). Las jornadas de proyecto duran **6 horas completas (250 minutos de trabajo al día)**: los pasos de esta ficha ocupan unos 200 y los **50 minutos restantes de cada día son «subir de nivel»** (pasar del mínimo al estándar con la rúbrica en la mano). Cada uno dice **qué hacéis** (la lista corta), **cómo se hace** con el detalle, **qué deberíais ver** y **cuándo está hecho**. Las ayudas (IA, errores, atascos) están al final. Si el tiempo aprieta, completad el nivel mínimo y dejad lo demás para casa. **No tengáis prisa por programar:** en este sprint lo importante es pensar bien.

**Cada paso tiene su propia página.** Abrid la que toque y volved aquí cuando acabéis:

- [Paso 1 · Planning, píldora y taller (día 1, 75 minutos)](Reto_Sprint_14_paso_1.md)
- [Paso 2 · Elegir el brief (día 1, 15 minutos)](Reto_Sprint_14_paso_2.md)
- [Paso 3 · Buscar y validar datos (día 1, 60 minutos)](Reto_Sprint_14_paso_3.md)
- [Paso 4 · Ficha del proyecto y entrega (día 1, 50 minutos)](Reto_Sprint_14_paso_4.md)
- [Paso 5 · Go / no-go, EDA, calidad del dato y baseline (día 2, 200 minutos)](Reto_Sprint_14_paso_5.md)
- [Paso 6 · Backlog, plan ético y repositorio (día 3, 140 minutos)](Reto_Sprint_14_paso_6.md)
- [Paso 7 · Revisión, entrega, review y retro (día 3, 60 minutos)](Reto_Sprint_14_paso_7.md)

#### Ayuda 1 · Cómo usar la IA en este reto

En un proyecto largo la IA puede ayudar mucho, pero **la responsabilidad es vuestra** y **puede inventar fuentes, licencias y enlaces**. Reglas:
- **Nunca inventéis una fuente o una licencia.** Si la IA os da un enlace, entrad y comprobadlo.
- **Que el proyecto sea vuestro:** la idea, la pregunta y la métrica salen del equipo. No se acepta copiar un cuaderno de internet.
- **Declarad el uso de IA** en el apartado 7 del README: qué pedisteis y qué comprobasteis a mano.
- **Nada de datos personales ni claves** en una IA ni en el repositorio.

| Para qué | Ejemplo de petición | Qué comprobáis |
|---|---|---|
| Encontrar fuentes de datos | «Dame fuentes abiertas de datos de llegada de turistas a Canarias y qué licencias suelen tener» | **Entrad vosotros en la web**, leed la licencia y comprobad que los datos existen |
| Redactar la ficha | «Ayúdame a convertir estas notas en una pregunta de negocio clara con una métrica» | Que sea **vuestra** idea, no una genérica |
| Planificar | «Convierte este objetivo en 5 historias de usuario pequeñas» | Que son realizables en el tiempo que tenéis |
| Revisar riesgos | «Para un proyecto de [vuestro brief], ¿qué riesgos éticos y de protección de datos debería considerar?» | Que se aplican a **vuestro** caso y que vuestras medidas son reales |

#### Ayuda 2 · Errores frecuentes (y cómo evitarlos)

| Error | Por qué ocurre | Cómo evitarlo |
|---|---|---|
| Elegir un problema demasiado grande | Ambición | Preguntaos: ¿se puede hacer en unas 54 horas de proyecto? |
| Elegir datos sin mirar la licencia | Se quiere avanzar | La licencia es lo primero que se comprueba |
| Definir la métrica después de ver los resultados | «Para que salga bien» | Escribidla en la ficha y no la cambiéis |
| Baseline demasiado complicado | Se quiere lucir | El baseline es **lo más simple posible** |
| Mezclar pasado y futuro al partir los datos | Se parte al azar una serie de tiempo | Con series, partid **por fechas**: entrenad con el pasado y evaluad con el futuro |
| Backlog con 40 tareas vagas | Se apunta todo | 10 a 15 historias concretas con criterio de aceptación |
| Riesgos éticos genéricos («cuidado con los sesgos») | Prisa | Cinco riesgos específicos de **vuestros** datos; si valen para cualquier proyecto, no valen |
| Un solo *commit* del responsable técnico | Es más rápido | Todas las personas hacen *commits* con su cuenta |
| Dejar la ficha para el final | «Primero los datos» | Entregadla antes de las 14:30 del día 1; sin ella, el docente no puede dar el *go* |

#### Ayuda 3 · Si os atascáis

1. **No nos ponemos de acuerdo en el brief:** votad con criterios (datos disponibles, interés, tiempo) y puntuad cada opción de 1 a 5.
2. **No encontramos datos con licencia:** probad primero con las fuentes de la tabla de briefs y consultad al docente **cuanto antes el día 1**, no por la tarde.
3. **El *go / no-go* pide cambios:** es normal; corregid la ficha ese mismo día y seguid.
4. **El cuaderno da error:** leed el mensaje completo, probad la celda con un trozo pequeño de los datos y preguntad al equipo y, después, al docente.
5. Más ayuda: [Cómo se trabaja un reto](../../../../material/4.%20Como_se_trabaja_un_reto.md).
