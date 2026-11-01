# Sprint 14 · Reto «Proyecto final: definir, tener datos y un punto de partida» · Entrega y rúbrica

> **Qué se sube y cómo se evalúa.** Se lee **una vez**, antes de entregar, y se vuelve a la rúbrica cuando el equipo revisa su trabajo. Mientras trabajáis no hace falta: para eso está [el reto en una página](../1_Trabajar/Reto_Sprint_14_una_pagina.md).
>
> - Volver al [README del sprint](../../README.md) · [ficha del reto](../3_Consultar/Reto_Sprint_14.md), para consultar.
> - Vuestra hoja personal: [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md).
> - Cómo subir a GitHub paso a paso, con capturas: [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md).

Esta hoja responde a **dos preguntas distintas**, una tabla para cada una:

**Tabla A · Los ficheros:** qué ficheros hay, de dónde sale cada uno (ya hecho, lo modificáis, lo creáis o lo genera el programa) y **cuáles se suben y adónde**.

**Tabla B · Los requisitos:** qué tiene que cumplir lo que entregáis y hasta dónde llegar (🟢 mínimo, 🟡 estándar, 🔴 extra). **Es lo que se evalúa.**

**En total, al final del sprint se suben a `sprint-14/`:** **6 ficheros del equipo** (`ficha_proyecto.md`, `plan_datos_licencias.md`, `01_eda.ipynb`, `02_baseline.ipynb`, `backlog_y_sprints.md`, `riesgos_eticos.md`) **+ 1 autoevaluación y coevaluación por persona**, es decir, **6 + tantos ficheros como personas haya en el equipo** (un equipo de 3 sube 9). «El reto» no es un fichero aparte: son esos seis documentos y cuadernos. Además, el `README.md` y el `requirements.txt` van a la **raíz** del repositorio del equipo (no a `sprint-14/`), y los datos van a `data/` solo si la licencia lo permite. El tablero se enseña en la review y la *review* y la *retro* se hacen de palabra: no se suben.

## 1 · 📦 Tabla A · Los ficheros: de dónde sale cada uno y cuáles se suben

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

---

## 2 · ✅ Tabla B · Los requisitos: qué tiene que cumplir y hasta dónde llegar

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

---

## 3 · 🧭 Rúbrica del reto · cómo se puntúa y cómo se revisa

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

Cada persona, además, se puntúa a sí misma en su hoja de [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md) con **esta misma rúbrica**.
