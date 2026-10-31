# Sprint 14 · Reto «Proyecto final: definir, tener datos y un punto de partida»

> **Ficha completa del reto, para consultar.** Leedla entera antes de empezar y volved a ella cuando tengáis dudas.
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
| **Plantilla de la ficha** [`plantilla_ficha_proyecto.md`](../4_Plantillas_y_entrega/plantilla_ficha_proyecto.md) | Resumir el proyecto en una página (anexo A) | Copiadla como `ficha_proyecto.md` |
| **Plantilla del plan de datos** [`plantilla_plan_datos_licencias.md`](../4_Plantillas_y_entrega/plantilla_plan_datos_licencias.md) | Documentar fuente, licencia, variables, calidad, linaje y partición | Copiadla como `plan_datos_licencias.md` |
| **Plantilla del backlog** [`plantilla_backlog_y_sprints.md`](../4_Plantillas_y_entrega/plantilla_backlog_y_sprints.md) | Historias de usuario, objetivo de cada sprint y retrospectivas | Copiadla como `backlog_y_sprints.md` |
| **Plantilla del registro de riesgos** [`plantilla_registro_riesgos_eticos.md`](../4_Plantillas_y_entrega/plantilla_registro_riesgos_eticos.md) | Checklist ético, clasificación RGPD / AI Act y registro de riesgos | Copiadla como `riesgos_eticos.md` |
| **Plantilla del README** [`plantilla_README_repositorio.md`](../4_Plantillas_y_entrega/plantilla_README_repositorio.md) | Explicar el proyecto para que otra persona lo ejecute solo con ese README | Copiadla como `README.md`. Al final lleva la sección «Revisión con la rúbrica» |
| **Fuentes de datos candidatas** (ISTAC, Frontur-Canarias, datos.gob.es, AEMET, REData, PlantVillage, catálogo oficial de FP) | Encontrar datos reales y legales | En la tabla de briefs del paso 2. **Entrad vosotros en la web y leed la licencia** |
| **Acceso gratuito a modelos de lenguaje** | Solo si elegís el brief 3 (asistente de FP) | [Guía de acceso](../../../../material/Acceso_modelos_de_lenguaje.md) |
| **Google Colab** (o vuestro Python) | Escribir y ejecutar `01_eda.ipynb` y `02_baseline.ipynb` | Colab no necesita instalar nada. Este sprint no tiene cuadernos de práctica propios; os sirven de apoyo los de pandas y limpieza del Sprint 6 (`S06_01` y `S06_02`) |
| **Tablero del equipo** (Trello o similar) | Cargar las historias del backlog y mover las tareas | El del equipo. Si no existe, es lo primero que se crea |
| **Cómo entregar en GitHub** | Subir los ficheros a `sprint-14/` | [Guía de entrega](../../../../material/5.%20Como_entregar_en_GitHub.md) |
| **Autoevaluación y coevaluación** | Cada persona rellena su hoja | [Hoja del sprint](../4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md) |
| **Un asistente de IA** (opcional) | Ideas, borradores y revisión | Con las reglas de la «Ayuda 1» del paso a paso |

---

### 3 · 📦 Qué entregar

Este apartado responde a **dos preguntas distintas**, una tabla para cada una:

**Tabla A · Los ficheros:** qué ficheros hay, de dónde sale cada uno (ya hecho, lo modificáis, lo creáis o lo genera el programa) y **cuáles se suben y adónde**.

**Tabla B · Los requisitos:** qué tiene que cumplir lo que entregáis y hasta dónde llegar (🟢 mínimo, 🟡 estándar, 🔴 extra). **Es lo que se evalúa.**

**En total, al final del sprint se suben a `sprint-14/`:** **6 ficheros del equipo** (`ficha_proyecto.md`, `plan_datos_licencias.md`, `01_eda.ipynb`, `02_baseline.ipynb`, `backlog_y_sprints.md`, `riesgos_eticos.md`) **+ 1 autoevaluación y coevaluación por persona**, es decir, **6 + tantos ficheros como personas haya en el equipo** (un equipo de 3 sube 9). «El reto» no es un fichero aparte: son esos seis documentos y cuadernos. Además, el `README.md` y el `requirements.txt` van a la **raíz** del repositorio del equipo (no a `sprint-14/`), y los datos van a `data/` solo si la licencia lo permite. El tablero se enseña en la review y la *review* y la *retro* se hacen de palabra: no se suben.

#### Tabla A · Los ficheros: de dónde sale cada uno y cuáles se suben

Todo lo que se sube va al repositorio privado del equipo (`ifcd107-equipo-…`), en la carpeta **`sprint-14/`**, salvo lo que la última columna indica.

| Fichero | Origen | Qué hacéis vosotros | ¿Se sube? |
|---|---|---|---|
| `ficha_proyecto.md` | **Lo creáis a partir de una plantilla.** Os damos `plantilla_ficha_proyecto.md` con los nueve apartados | Copiarla con ese nombre y rellenarla en una página; borrar las notas en cursiva | **Sí** · `sprint-14/`. El día 1 antes de las 14:30; si el *go / no-go* pide cambios, se vuelve a subir corregida |
| `plan_datos_licencias.md` | **Lo creáis a partir de una plantilla.** Os damos `plantilla_plan_datos_licencias.md` | Copiarla y rellenar fuentes, variables, calidad, linaje, partición y privacidad | **Sí** · `sprint-14/` |
| `01_eda.ipynb` | **Lo creáis.** Cuaderno nuevo de Colab: no hay plantilla | Describir los datos, buscar nulos, duplicados, valores raros y sesgos, y cerrar con el informe de calidad | **Sí** · `sprint-14/` |
| `02_baseline.ipynb` | **Lo creáis.** Cuaderno nuevo de Colab: no hay plantilla | Dividir los datos, construir el modelo más simple y calcular su métrica | **Sí** · `sprint-14/` |
| `backlog_y_sprints.md` | **Lo creáis a partir de una plantilla.** Os damos `plantilla_backlog_y_sprints.md` con historias de ejemplo | Copiarla, adaptar las historias a vuestro proyecto (10 a 15) y fijar el objetivo de cada sprint | **Sí** · `sprint-14/` |
| `riesgos_eticos.md` | **Lo creáis a partir de una plantilla.** Os damos `plantilla_registro_riesgos_eticos.md` (checklist, clasificación normativa y registro) | Copiarla y rellenar la columna S14 del checklist, la clasificación RGPD / AI Act y al menos 5 riesgos específicos | **Sí** · `sprint-14/` |
| `README.md` | **Lo creáis a partir de una plantilla.** Os damos `plantilla_README_repositorio.md` | Copiarla como `README.md` y rellenar lo que ya sabéis (apartados 1, 3, 4, 6, 7, 8 y 9); los resultados finales y el demostrador se rellenan en los sprints 15 y 16 | **Sí** · raíz del repositorio (no en `sprint-14/`) |
| `requirements.txt` | **Lo creáis.** Una librería por línea, con su versión | Escribir `nombre==versión` de las librerías que usan los cuadernos | **Sí** · raíz del repositorio |
| Datos descargados | **Ya hecho.** Son datos de una fuente externa con licencia | Nada: se guardan sin cambiar; la limpieza se hace y se explica en el cuaderno | Solo si la licencia permite redistribuirlos y pesan poco · `data/` |
| `descargar_datos.py` (o un enlace de descarga en el README) | **Lo creáis.** Un script corto que descarga los datos | Escribirlo o, si hay enlace directo, apuntarlo en el README | Solo si no subís los datos · `sprint-14/` |
| Autoevaluación y coevaluación (`autoevaluacion_nombre.md`) | **Ya hecha, en blanco** | Cada persona copia la plantilla con su nombre y la rellena; la coevaluación va **dentro del mismo fichero** | **Sí**, **una por persona** (no una por equipo) · `sprint-14/` |
| *Canvas* borrador y puntuación de briefs | **Lo creáis** en papel, pizarra o pantalla | Servirse de ellos para decidir; no hay formato | **No se suben** |

#### Tabla B · Los requisitos: qué tiene que cumplir y hasta dónde llegar

| Requisito | Qué se pide exactamente | Nivel | Dónde se comprueba |
|---|---|---|---|
| **Brief y pregunta de negocio** | Un brief elegido (uno de los cuatro o uno libre que cumpla R1–R11) y la pregunta de negocio en **una frase**, con el cliente y la decisión que apoyará | 🟢 Mínimo | `ficha_proyecto.md` (apartados 2 y 3) |
| **Ficha a tiempo** | Ficha de una página subida **antes de las 14:30 del día 1**; el *go / no-go* se lee el día 2 y, si hace falta, se corrige | 🟢 Mínimo | `ficha_proyecto.md` y su historial de subidas |
| **Equipo y roles** | Scrum Master, responsable técnico, responsable de datos y responsable de IA responsable, con la rotación prevista | 🟢 Mínimo | `ficha_proyecto.md` (apartado 1) |
| **Datos con fuente y licencia** | Cada fuente con enlace, licencia, tamaño, variables, periodo y si hay datos personales. Sin licencia clara, no se usa. Nada de «a la espera de datos» | 🟢 Mínimo | `plan_datos_licencias.md` (apartado 1) |
| **Métrica de éxito** | Métrica de negocio, métrica técnica, umbral de éxito y baseline previsto | 🟢 Mínimo | `ficha_proyecto.md` (apartado 5) |
| **EDA básico** | Describir los datos (filas, columnas, periodo, tipos), contar nulos y duplicados y enseñar al menos tres gráficos o tablas que respondan a la pregunta | 🟢 Mínimo | `01_eda.ipynb` |
| **Baseline con su métrica** | El modelo más simple posible, ejecutado de arriba abajo, con la métrica calculada | 🟢 Mínimo | `02_baseline.ipynb` |
| **Riesgos en la ficha** | Tres riesgos con su mitigación y una clasificación preliminar del AI Act | 🟢 Mínimo | `ficha_proyecto.md` (apartado 8) |
| **Informe de calidad del dato** | Nulos, duplicados, valores raros, **sesgos de muestreo** (¿quién o qué falta?), desequilibrios, posibles fugas y linaje, cada hallazgo con la acción tomada | 🟡 Estándar | `01_eda.ipynb` y `plan_datos_licencias.md` (apartados 3 y 4) |
| **Métrica y partición antes de ver resultados** | La métrica técnica y la partición (temporal si hay series) se escriben **antes** de calcular el baseline y no se cambian después | 🟡 Estándar | `plan_datos_licencias.md` (apartado 5), `ficha_proyecto.md` y `02_baseline.ipynb` |
| **Backlog y objetivos** | Entre 10 y 15 historias con objetivo para los sprints 15, 16 y 17, cargadas en el tablero | 🟡 Estándar | `backlog_y_sprints.md` y el tablero |
| **Plan ético** | Checklist actualizado (columna S14), clasificación RGPD / AI Act justificada y **al menos 5 riesgos específicos** de vuestro proyecto, con probabilidad, impacto, medida y responsable | 🟡 Estándar | `riesgos_eticos.md` |
| **Repositorio** | README con lo que ya sabéis, `requirements.txt` y *commits* con mensaje claro de **todas las personas**, sin claves ni datos personales | 🟡 Estándar | `README.md` y el historial del repositorio |
| **Uso de IA** | Qué se pidió a la IA, qué fuentes y licencias se comprobaron a mano y qué se cambió | 🟢 Mínimo | `README.md` (apartado 7) |
| **Revisión y autoevaluación** | Alguien que **no escribió esa parte** revisa el trabajo con la rúbrica (justo debajo de estas tablas) y anota nivel y prueba en el README; cada persona sube su hoja de autoevaluación y coevaluación; el equipo hace la review y la retro | 🟡 Estándar | `README.md` (sección «Revisión con la rúbrica»), `backlog_y_sprints.md` (retro) y `sprint-14/` |
| **EDA ampliado** | Además, el análisis por subgrupos (por isla, mes, clase o tipo de pregunta, según el brief) y un hallazgo que **cambia el enfoque** y queda reflejado en la ficha | 🔴 Extra | `01_eda.ipynb` y `ficha_proyecto.md` |
| **Backlog más detallado** | Todas las historias con criterios de aceptación, tamaño, responsable y sprint, y un objetivo medible para cada sprint; las mitigaciones de riesgos enlazadas a historias | 🔴 Extra | `backlog_y_sprints.md` y `riesgos_eticos.md` |

#### Rúbrica del reto · cómo se puntúa y cómo se revisa

La usan **dos veces**: el equipo, para revisar su propio trabajo antes de entregar (es lo que dice la *Definition of Done*), y el docente, para puntuar el sprint. Se mira **cada criterio por separado** y se pone el nivel de la columna cuyo texto **se cumple entero**: si lo de un nivel se cumple a medias, es el nivel de abajo. **0** significa que no se ha entregado nada de ese criterio.

Orientación: lo que pide el nivel 🟢 mínimo sale en un **2**, el 🟡 estándar en un **3** y los 🔴 extras en un **4**. La nota del **proyecto** final usa además la rúbrica de 100 puntos de `briefs_y_rubrica.md`.

| Criterio | 1 · Empezado | 2 · Mínimo | 3 · Estándar | 4 · Extra |
|---|---|---|---|---|
| **Corrección técnica** (¿está bien hecho?) | Hay documentos, pero falta la pregunta o la métrica, o los cuadernos no se ejecutan | La ficha tiene pregunta, decisión y las dos métricas; `01_eda.ipynb` y `02_baseline.ipynb` se ejecutan de arriba abajo y el baseline da una métrica | La métrica y la partición se escribieron **antes** de ver resultados y no hay fuga (temporal si hay series); el informe de calidad tiene nulos, duplicados, valores raros y sesgos; el baseline es lo más simple posible | Además, un EDA por subgrupos con un hallazgo que cambia el enfoque y aparece en la ficha |
| **Reproducibilidad** (¿lo puede repetir otra persona?) | No se sabe de dónde salen los datos o los cuadernos solo funcionan en un ordenador | El plan de datos tiene fuente, enlace y licencia, pero el README no dice cómo descargarlos o ejecutar los cuadernos en orden | Otra persona descarga los datos y obtiene **la misma métrica del baseline** siguiendo solo el README; hay `requirements.txt` y *commits* de todas las personas, sin claves ni datos personales | Además, el linaje está completo (descarga, limpieza, partición), el README indica versión de Python y semilla, y el script de descarga funciona desde cero |
| **Análisis y comunicación al cliente** (¿lo entiende quien no programa?) | La pregunta es vaga («analizar el turismo») y no dice qué decisión apoya | La pregunta cabe en una frase y hay cliente, pero la decisión o la métrica de negocio no están claras | La ficha dice **qué decisión mejora y qué pasa hoy sin el modelo**, con un umbral de éxito en términos del cliente; en la review se explica el hallazgo del EDA y el baseline sin jerga | Además, cuantifica el valor para el cliente (euros, horas o errores evitados) y explica qué cambió de la ficha tras el *go / no-go* o el EDA |
| **IA responsable** (¿se sabe qué hizo la IA y qué riesgos hay?) | No dice si se ha usado IA ni hay riesgos | Dice que se ha usado IA sin detalle; la ficha tiene tres riesgos y una clasificación AI Act, aunque sean genéricos | Dice **qué se pidió, qué se comprobó a mano y qué se cambió**; el registro tiene al menos 5 riesgos específicos de vuestros datos con probabilidad, impacto, medida y responsable, y la clasificación RGPD / AI Act está justificada | Además, cada riesgo alto tiene una medida enlazada a una historia del backlog y se cuenta un caso concreto en que la IA inventó o falló en algo y cómo lo detectasteis |

**Cómo se revisa** (unos 10 minutos, antes de la review; lo hace **una persona que no escribió esa parte**):

1. **Ejecutar**, en una carpeta o un Colab limpios, lo que dice el README: descargar los datos y ejecutar `01_eda.ipynb` y `02_baseline.ipynb` en orden. Anotar si algo no funciona o si la métrica del baseline no sale igual.
2. **Leer la ficha como si fuera el cliente**: ¿se entiende la pregunta, la decisión que apoya y cuándo se considerará un éxito? Subrayar lo que no se entienda.
3. **Comprobar los datos y los riesgos**: abrir el enlace de cada fuente, leer la licencia y comprobar que coincide con el plan de datos; leer los cinco riesgos y ver si podrían valer para cualquier otro proyecto (si sí, son genéricos).
4. **Poner un nivel (1 a 4) en cada criterio, con una frase de prueba** (por ejemplo: «3 · la métrica se escribió antes, pero falta el informe de duplicados»; «2 · el README no dice cómo descargar los datos»). Sin prueba escrita, el nivel no vale.
5. **Apuntar el resultado** en la sección «Revisión con la rúbrica» del `README.md` y corregir lo más fácil de arreglar. Lo demás se anota como mejora.

Cada persona, además, se puntúa a sí misma en su hoja de [autoevaluación y coevaluación](../4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md) con **esta misma rúbrica**.

---

### 4 · 🪜 Guía paso a paso

Son siete pasos, de **600 minutos en total** (200 por jornada, tres jornadas). Las jornadas de proyecto duran **6 horas completas (250 minutos de trabajo al día)**: los pasos de esta ficha ocupan unos 200 y los **50 minutos restantes de cada día son «subir de nivel»** (pasar del mínimo al estándar con la rúbrica en la mano). Cada uno dice **qué hacéis** (la lista corta), **cómo se hace** con el detalle, **qué deberíais ver** y **cuándo está hecho**. Las ayudas (IA, errores, atascos) están al final. Si el tiempo aprieta, completad el nivel mínimo y dejad lo demás para casa. **No tengáis prisa por programar:** en este sprint lo importante es pensar bien.

#### Paso 1 · Planning, píldora y taller (día 1, 75 minutos)
1. Leer las reglas del proyecto y repartir los roles del sprint.
2. Escuchar la píldora de teoría sobre cómo formular un proyecto de IA.
3. Hacer el taller de Design Thinking y salir con uno o dos briefs candidatos y un *canvas* borrador.

**Cómo se hace**
- **Las reglas (10 minutos de planning).** Abrid [`briefs_y_rubrica.md`](../../../../proyecto-final/briefs_y_rubrica.md) y leed las reglas comunes, los requisitos **R1 a R11** y la rúbrica de 100 puntos. Subrayad lo que no entendáis y preguntadlo ahora.
- **Los roles.** Hay cuatro: **Scrum Master** (cuida el trabajo del equipo y el tablero), **responsable técnico** (que todo se pueda repetir), **responsable de datos** (fuentes, licencias y calidad) y **responsable de IA responsable** (riesgos y ética). Con tres personas, una asume dos. Los roles **rotan cada sprint**: apuntad quién empieza y quién pasa a qué en el 15 y el 16.
- **La píldora (25 minutos).** El docente explica el *canvas*: la pregunta de negocio, quién usa el resultado, la decisión que mejora, los datos y la métrica. Los apuntes están en [`apuntes_formular_un_proyecto_de_ia.md`](../../1_Teoria/apuntes/apuntes_formular_un_proyecto_de_ia.md).
- **El taller (40 minutos).** Pensad en un problema **real y cercano**: ¿quién lo sufre?, ¿qué decisión se toma hoy sin datos? Escribid preguntas del tipo «¿Cómo podríamos…?». Quedaos con **uno o dos briefs candidatos** y rellenad un *canvas* borrador en papel o en una pizarra.

**Qué deberíais ver.** Cuatro roles con nombre y apellidos en una nota del equipo, y un *canvas* con la pregunta, el cliente, la decisión, los datos posibles y la métrica, aunque sea a lápiz.

**Hecho cuando:** cada persona sabe su rol y tenéis uno o dos briefs candidatos.

#### Paso 2 · Elegir el brief (día 1, 15 minutos)
1. Comparar los briefs candidatos con tres criterios.
2. Decidir y apuntar el brief elegido, **antes del descanso**: es el primer hito del día.

**Cómo se hace.** Los cuatro briefs son:

| Brief | Pregunta guía | Pensad en… |
|---|---|---|
| **1 · Demanda turística** | ¿Podemos predecir la llegada de turistas con 3–6 meses de antelación y qué factores la explican? | Series temporales. Carga de cómputo baja |
| **2 · Salud de cultivos (visión)** | ¿Con qué fiabilidad se distingue una hoja sana de una enferma y cuándo no fiarnos? | Imágenes. Carga alta (GPU) |
| **3 · Asistente de FP (LLM/RAG)** | ¿Puede un asistente responder sin inventar y cómo lo medimos? | Texto. Carga media |
| **4 · Demanda eléctrica** | ¿Predecimos la demanda de las próximas 24 h mejor que un modelo de referencia? | Series temporales con calendario. Carga media |

- **Cómo elegir.** Puntuad cada brief de 1 a 5 en tres criterios: **¿hay datos reales accesibles?**, **¿nos interesa?** y **¿se puede terminar en el tiempo que hay?** (unas 54 horas de proyecto en los tres primeros sprints). Elegid el que más puntos sume.
- **Dos equipos pueden elegir el mismo brief**, pero cada uno define **su propia pregunta y su propia métrica**.
- **Brief libre.** Podéis proponer uno propio si lo presentáis en la ficha **antes del 26/11**, cumple R1–R11, tiene datos reales ya identificados, una dificultad parecida a la de los otros y no usa datos personales sensibles.

**Qué deberíais ver.** Una tabla con vuestras puntuaciones y un brief marcado como elegido.

**Hecho cuando:** el equipo ha elegido su brief y todo el mundo sabe cuál es.

#### Paso 3 · Buscar y validar datos (día 1, 60 minutos)
1. Hacer una lista de fuentes candidatas para vuestro brief.
2. Responder, para cada fuente, a cinco preguntas de validación.
3. Rellenar `plan_datos_licencias.md` con lo que sabéis y quedaros con las fuentes que valen.

**Cómo se hace**
- **Las cinco preguntas.** Para cada fuente candidata (en la tabla de briefs de la ficha tenéis candidatas como ISTAC, Frontur-Canarias, datos.gob.es, AEMET, REData, PlantVillage o el catálogo oficial de FP):
  - ¿Tiene una **licencia** que permita usarla? Si no está clara, **no se usa**.
  - ¿Se puede **descargar**, y podemos repetir la descarga con un enlace o un script?
  - ¿Qué **tamaño** tiene? ¿Cabe en nuestro ordenador o en Colab?
  - ¿Qué **variables y qué periodo** trae? ¿Responden a nuestra pregunta?
  - ¿Hay **datos personales**? Si los hay y son sensibles, **no se aceptan**.
- **Reparto.** El responsable de datos lleva la plantilla; las demás personas buscan y validan una fuente cada una. **Entrad vosotros en la web y leed la licencia**: no os fiéis de lo que diga una IA.
- **La plantilla.** Copiad `plantilla_plan_datos_licencias.md` como `plan_datos_licencias.md`. Hoy rellenad el apartado 1 (inventario de fuentes), el 2 (variables) y el 6 (privacidad); el resto se completa el día 2 con el EDA. Las licencias más frecuentes (CC BY, CC BY-SA, CC BY-NC, CC0) están explicadas en la propia plantilla.
- **Brief 3.** Si elegís el asistente de FP, mirad la [guía de acceso gratuito a modelos de lenguaje](../../../../material/Acceso_modelos_de_lenguaje.md).
- **Regla de oro.** No se aceptan proyectos «a la espera de datos»: los datos han de estar identificados y accesibles hoy.

**Qué deberíais ver.** Una tabla con al menos una fuente validada (enlace, licencia, tamaño, variables y «datos personales: no») y, si descartasteis alguna, la razón escrita.

**Hecho cuando:** tenéis al menos una fuente con licencia clara, descargable y sin datos personales sensibles.

#### Paso 4 · Ficha del proyecto y entrega (día 1, 50 minutos)
1. Copiar `plantilla_ficha_proyecto.md` como `ficha_proyecto.md` y rellenar los nueve apartados en una página.
2. Revisarla entre todos: ¿se entiende sin explicaciones?
3. Subirla a `sprint-14/` **antes de las 14:30**.

**Cómo se hace**
- **Qué escribís en cada apartado.** La plantilla es corta; cada apartado pide una cosa:

| Apartado de la ficha | Qué escribís |
|---|---|
| 1 · Equipo y roles | Los cuatro roles con su nombre y la rotación prevista |
| 2 y 3 · Brief, pregunta, cliente y decisión | La pregunta de negocio en **una frase**, quién usará el resultado y qué decisión mejora (y qué pasa hoy sin el modelo) |
| 4 · Datos | Las fuentes validadas en el paso 3: enlace, licencia, tamaño, variables y limitaciones |
| 5 · Métrica y baseline | Métrica de negocio, **métrica técnica**, umbral de éxito, baseline previsto y cómo partiréis los datos |
| 6 y 7 · Modelos y demostrador | Al menos tres modelos (uno neuronal, o un LLM con RAG en el brief 3) y qué hará el demostrador |
| 8 y 9 · Riesgos y backlog | Tres riesgos con su mitigación, una clasificación AI Act preliminar y las historias principales con el objetivo de cada sprint |

- **Un buen resultado se parece a esto.** Pregunta: «¿Podemos predecir la ocupación hotelera de Gran Canaria con 3 meses de antelación con un error menor del 8 %, para planificar plantilla y compras?». Decisión que apoya: «Cuándo contratar refuerzo en temporada media». Baseline: «Predecir lo mismo que el año anterior en la misma semana». Un riesgo específico: «Los datos son de hoteles grandes: no representan a pequeños alojamientos rurales».
- **La métrica, ahora.** Escribid la métrica técnica y el umbral **ahora** y no los cambiéis cuando veáis los resultados.
- **Subirla.** Seguid la [guía de entrega](../../../../material/5.%20Como_entregar_en_GitHub.md): entrad en la carpeta `sprint-14` del repositorio del equipo, *Add file → Upload files* (o *Create new file* y pegar el texto), mensaje corto y **Commit changes**. El nombre, en minúsculas y sin espacios. El docente la lee en el repositorio y responde con el *go / no-go* **el día siguiente por la mañana**.

**Qué deberíais ver.** Una ficha de una página, sin notas en cursiva, y `ficha_proyecto.md` dentro de `sprint-14/` en GitHub con la hora de la subida anterior a las 14:30.

**Hecho cuando:** la ficha está subida antes de las 14:30 y el docente puede abrirla.

#### Paso 5 · Go / no-go, EDA, calidad del dato y baseline (día 2, 200 minutos)
1. Leer el *go / no-go* del docente y corregir la ficha si hace falta.
2. Hacer el EDA y el informe de calidad del dato en `01_eda.ipynb`.
3. Fijar la partición de los datos y la métrica técnica **antes** de mirar resultados.
4. Construir el baseline en `02_baseline.ipynb` y calcular su métrica.

**Cómo se hace.** Reparto sugerido de los 200 minutos:

| Bloque | Qué hacéis | Minutos |
|---|---|---|
| 5.1 | Leer el *go / no-go* y corregir la ficha | 20 |
| 5.2 | EDA e informe de calidad | 90 |
| 5.3 | Partición y métrica | 20 |
| 5.4 | Baseline y subida de los cuadernos | 70 |

##### 5.1 · El go / no-go (20 minutos)

Hay tres respuestas posibles: **GO** (adelante), **GO con cambios** o **NO-GO** (hay que cambiar el enfoque). Un *no-go* o un cambio es **normal**: corregid la ficha ese mismo día, subid la versión 2 a `sprint-14/` con otro mensaje de *commit* y seguid. Si el docente cambia el alcance, apuntadlo en la ficha.

##### 5.2 · EDA e informe de calidad (90 minutos)

En Colab, abrid un cuaderno nuevo y guardadlo como `01_eda.ipynb`. La primera celda carga los datos con el enlace o el script del plan de datos. Después, un EDA con estas preguntas:

| Orden | Qué miráis | Qué escribís |
|---|---|---|
| 1 | Qué trae el conjunto: filas, columnas, periodo y tipos | Una tabla o un resumen de tres líneas |
| 2 | **Nulos** y **duplicados** | Cuántos hay y qué hacéis con ellos |
| 3 | **Valores raros** (imposibles o muy extremos) | Qué son y si los quitáis o los dejáis, y por qué |
| 4 | **Sesgo de muestreo**: ¿quién o qué falta en los datos? | Una frase, por ejemplo «solo hay hoteles grandes» |
| 5 | Tres gráficos o tablas que respondan a **vuestra pregunta** | Un título y una frase de conclusión por gráfico |
| 6 | **Fugas posibles**: variables que no se conocen en el momento de decidir | Cuáles hay y si se descartan |

En el brief 2 mirad cuántas imágenes hay por clase; en el brief 3, cuántos documentos hay y cómo de largos son. Terminad con el **informe de calidad del dato**: rellenad el apartado 3 de `plan_datos_licencias.md` (hallazgo y acción tomada, uno por fila) y el apartado 4 (**linaje**: de dónde viene el dato y qué le habéis hecho). Elegid **un hallazgo que cambie el enfoque** para contarlo en la review.

##### 5.3 · Partición y métrica (20 minutos)

Antes de ejecutar ningún modelo, escribid en el apartado 5 de `plan_datos_licencias.md` y en el apartado 5 de la ficha:
- **Cómo partís los datos:** si hay series de tiempo, **por fechas** (entrenar con el pasado y evaluar con el futuro); si no, aleatoria y estratificada. Y por qué así se evitan las fugas.
- **Qué tamaño tiene cada parte:** entrenamiento, validación y test. **El test no se toca hasta el final del proyecto.**
- **La métrica técnica** (por ejemplo MAE, MAPE, F1 o aciertos sobre 40 preguntas) y el umbral de éxito.

##### 5.4 · Baseline (70 minutos)

Abrid `02_baseline.ipynb`. Construid el **modelo más simple posible**: «predecir lo mismo que ayer o que el año anterior», la media, la clase más frecuente o una búsqueda por palabras clave. Calculad su métrica sobre la **validación** y dejad escrita una frase: «Nuestro baseline tiene [métrica] de [valor]». Es el **suelo** que intentaréis superar en los sprints siguientes; no lo compliquéis. Después, en cada cuaderno, *Entorno de ejecución → Reiniciar y ejecutar todo*, *Archivo → Descargar → Descargar .ipynb* y subid el fichero a `sprint-14/` (cada cuaderno, una persona distinta).

**Qué deberíais ver.** La ficha con el *go* (o corregida), un `01_eda.ipynb` que termina con la tabla de calidad, la partición y la métrica escritas, y un `02_baseline.ipynb` que acaba con un número.

**Hecho cuando:** los dos cuadernos se ejecutan de arriba abajo sin errores, la métrica y la partición están escritas antes del baseline y los cuadernos están en `sprint-14/`.

#### Paso 6 · Backlog, plan ético y repositorio (día 3, 140 minutos)
1. Hacer el backlog de 10 a 15 historias y fijar el objetivo de cada sprint.
2. Rellenar el plan ético con al menos 5 riesgos específicos.
3. Montar el repositorio: README, `requirements.txt` y *commits* de todas las personas.

**Cómo se hace.** Reparto sugerido de los 140 minutos: 45 el backlog, 45 el plan ético y 50 el repositorio. Cada parte la lidera una persona distinta, y otra la revisa.

##### 6.1 · Backlog (45 minutos)

Copiad `plantilla_backlog_y_sprints.md` como `backlog_y_sprints.md`. La plantilla trae doce historias de ejemplo: **adaptadlas** a vuestro proyecto y añadid las vuestras hasta tener entre **10 y 15**.

| Orden | Qué hacéis | Pista |
|---|---|---|
| 1 | Escribir cada historia como «**Como** [rol] **quiero** [qué] **para** [beneficio]» | Una historia = una tarea que cabe en unas horas |
| 2 | Añadir criterios de aceptación, tamaño (S, M o L), sprint y responsable | Si no sabéis cómo comprobarla, no está bien definida |
| 3 | Escribir el **objetivo de cada sprint** (14, 15, 16 y 17) en una frase medible | Con los hitos: 3/12 modelo candidato, 10/12 a las 14:30 congelación y 14/12 defensa |
| 4 | Cargar las historias en el **tablero** | El Scrum Master lo mantiene al día |

##### 6.2 · Plan ético (45 minutos)

Copiad `plantilla_registro_riesgos_eticos.md` como `riesgos_eticos.md`. Este documento **actualiza el checklist de IA responsable del Sprint 1** (`checklist_etico_v1.md`): si lo tenéis, pasad vuestras respuestas a la columna S1.
- **Parte A.** Rellenad la columna **S14** del checklist con ✔, ◐, ✘ o n/a y la evidencia (por ejemplo, el plan de datos o el EDA).
- **Parte B.** Contestad si hay datos personales, si haría falta una evaluación de impacto, el **nivel de riesgo del AI Act** y qué obligaciones se derivan.
- **Parte C.** Escribid **al menos 5 riesgos específicos de vuestros datos** (no «cuidado con los sesgos»), con probabilidad y impacto de 1 a 3 (nivel = P × I), la medida y el responsable. Mirad los ejemplos por brief al final de la parte C, pero no los copiéis: ajustadlos con vuestras cifras. Dejad vacía la última columna («cómo se evaluó la mitigación»): se rellena en el sprint 16.

##### 6.3 · Repositorio (50 minutos)

- Copiad `plantilla_README_repositorio.md` como `README.md` y rellenad lo que ya sabéis: el problema en tres líneas (apartado 1), la estructura del repositorio (apartado 3: el árbol ya muestra las carpetas `sprint-14/` a `sprint-17/`; hoy solo existe la de este sprint, y las demás se crean en su momento), **cómo reproducirlo** (apartado 4: descargar los datos y ejecutar los cuadernos en orden), los datos y licencias (6), el resumen de IA responsable (7), el equipo (8) y el tablero (9). La tabla de resultados y el demostrador se rellenan en los sprints 15 y 16.
- Escribid `requirements.txt`: una librería por línea con su versión, como `nombre==versión`. La versión sale con `pip show nombre` o, en Colab, con `!pip freeze` y buscando el nombre.
- Comprobad que **todas las personas** tienen al menos un *commit* (mensajes del tipo `docs: añado backlog`, `data: añado plan de datos`). Ningún dato personal ni claves.
- En el apartado 7 del README, **declarad el uso de IA**: qué pedisteis y qué comprobasteis a mano.

**Qué deberíais ver.** `backlog_y_sprints.md` con entre 10 y 15 historias y cuatro objetivos de sprint, `riesgos_eticos.md` con cinco filas rellenas, un `README.md` y un `requirements.txt` en la raíz y un tablero con las historias.

**Hecho cuando:** los cuatro documentos están escritos, el tablero tiene las historias y otra persona podría descargar los datos y ejecutar los cuadernos solo con el README.

#### Paso 7 · Revisión, entrega, review y retro (día 3, 60 minutos)
1. Revisar el trabajo con la rúbrica, por alguien que no escribió esa parte, y anotar el resultado en el README.
2. Subir lo que falte a `sprint-14/` y cada persona su autoevaluación y coevaluación.
3. Enseñar el sprint en la review: 5 minutos por equipo.
4. Hacer la retro (15 minutos) y apuntarla.

**Cómo se hace**
- **La revisión con la rúbrica (10 minutos).** Quien revisa sigue los cinco pasos de «Cómo se revisa» (apartado 3) y rellena la sección **«Revisión con la rúbrica»** del final del `README.md`: un nivel de 1 a 4 por criterio y **una frase de prueba**. Si hay tiempo, arreglad lo más fácil; lo demás queda como «lo primero que mejoraríamos».
- **Subir los ficheros.** Con la [guía de entrega](../../../../material/5.%20Como_entregar_en_GitHub.md): los seis ficheros del equipo a `sprint-14/` y el `README.md` y el `requirements.txt` a la raíz, **en subidas hechas por personas distintas**. Cada persona sube también su `autoevaluacion_nombre.md` (el nombre en minúsculas, sin espacios ni tildes) a `sprint-14/`. En la parte de coevaluación, una **valoración breve de la primera semana**.
- **La review (5 minutos por equipo).** Contad: (1) la pregunta de negocio y la decisión que apoyará; (2) los datos y **un hallazgo del EDA que cambia el enfoque**; (3) el baseline y su métrica; (4) tres riesgos éticos; (5) el backlog de los próximos sprints. Los cambios de alcance después del *go* se negocian en la review.
- **La retro (15 minutos).** Una cosa que seguir haciendo, una que cambiar y **una acción concreta** para el sprint 15. Anotadla en el apartado 5 de `backlog_y_sprints.md` y comprobad en cada retro si cumplisteis la acción anterior.

**Qué deberíais ver.** En `sprint-14/` del repositorio, los seis ficheros del equipo y una hoja de autoevaluación por persona (**6 + N**); en la raíz, el README con la sección de revisión rellena; y en el historial (el icono del reloj), *commits* de todas las personas.

**Hecho cuando:** la sección «Revisión con la rúbrica» está rellena, todos los ficheros están subidos, cada persona ha subido su autoevaluación y coevaluación y habéis hecho la review y la retro.

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
