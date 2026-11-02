# Sprint 3 · Reto «Primer modelo en producción» · Entrega y rúbrica

> **Qué se sube y cómo se evalúa.** Se lee **una vez**, antes de entregar, y se vuelve a la rúbrica cuando el equipo revisa su trabajo. Mientras trabajáis no hace falta: para eso está [el reto en una página](../1_Trabajar/Reto_Sprint_03_una_pagina.md).
>
> - Volver al [README del sprint](../../README.md) · [ficha del reto](../3_Consultar/Reto_Sprint_03.md), para consultar.
> - Vuestra hoja personal: [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md).
> - Cómo subir a GitHub paso a paso, con capturas: [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md).

Esta hoja responde a **dos preguntas distintas**, una tabla para cada una:

**Tabla A · Los ficheros:** qué ficheros hay, de dónde sale cada uno (ya hecho, lo modificáis, lo creáis o lo genera el programa) y **cuáles se suben y adónde**.

**Tabla B · Los requisitos:** qué tiene que cumplir lo que entregáis y hasta dónde llegar (🟢 mínimo, 🟡 estándar, 🔴 extra). **Es lo que se evalúa.**

**En total, al final del sprint se suben a `sprint-03/`:** **2 ficheros del equipo** (`informe_modelo.md` y `captura_cierre.png`) **+ 1 autoevaluación y coevaluación por persona**, es decir, **2 + tantos ficheros como personas haya en el equipo** (un equipo de 3 sube 5). «El reto» no es un fichero aparte: es ese informe, que reúne las tres partes (modelo, llamada a la API y recursos y costes). Si entregáis el informe en PDF, la captura va pegada dentro y se suben **1 + N**. El cuaderno de Colab solo se sube si queréis el nivel 🔴. La *review* y la *retro* se hacen de palabra: no se suben.

## 1 · 📦 Tabla A · Los ficheros: de dónde sale cada uno y cuáles se suben

Todo lo que se sube va al repositorio privado del equipo (`ifcd107-equipo-…`), en la carpeta **`sprint-03/`**.

| Fichero | Origen | Qué hacéis vosotros | ¿Se sube? |
|---|---|---|---|
| `informe_modelo.md` | **Lo creáis a partir de una plantilla.** Os damos [`plantilla_informe_modelo.md`](../1_Trabajar/plantillas/plantilla_informe_modelo.md) con siete apartados | Copiarla con ese nombre, sustituir los `______` por cifras de **vuestro** cuaderno, borrar las notas en cursiva y rellenar al final la revisión con la rúbrica. Máximo 4 páginas (la revisión no cuenta). Si preferís PDF, `informe_modelo.pdf` (exportado desde Word o Google Docs), solo uno de los dos | **Sí** · `sprint-03/` |
| `captura_cierre.png` | **Lo creáis.** Una captura de pantalla | Hacerla después de *Entorno de ejecución → Desconectar y eliminar entorno de ejecución*, con la sesión ya cerrada y sin datos personales a la vista | **Sí** · `sprint-03/`. Si el informe es PDF, va pegada dentro y no se sube aparte |
| `S3.5_lab_autogluon.ipynb` (vuestra copia, con las salidas) | **Ya hecho.** Es el cuaderno del laboratorio | Nada: se ejecuta y, para el nivel 🔴, se baja con *Archivo → Descargar → Descargar .ipynb* | Solo si queréis el nivel 🔴 de Reproducibilidad · `sprint-03/` |
| `reservas_turisdata.csv` y `turisdata.db` | **Ya hecho.** Datos sintéticos de TurisData | Nada: se usan sin cambiarlos | **No**: ya están en el repositorio del curso |
| `modelo_cancelaciones` (carpeta) | **Lo genera el cuaderno** al entrenar | Nada. Pesa unos 225 MB y desaparece al cerrar Colab | **No** se sube |
| `api_cancelaciones.py` | **Ya hecho.** El cuaderno lo descarga solo | Nada | **No** se sube |
| Autoevaluación y coevaluación (`autoevaluacion_nombre.md`) | **Ya hecha, en blanco** | Cada persona copia la plantilla con su nombre y la rellena; la coevaluación va **dentro del mismo fichero** | **Sí**, **una por persona** (no una por equipo) · `sprint-03/` |
| Hoja de apuntes del equipo (frase del cliente, tabla de columnas, importes) | **Lo creáis** en papel, pizarra o pantalla | Servirse de ella para escribir el informe; no hay formato | **No se sube** |

---

## 2 · ✅ Tabla B · Los requisitos: qué tiene que cumplir y hasta dónde llegar

| Requisito | Qué se pide exactamente | Nivel | Dónde se comprueba |
|---|---|---|---|
| **Problema y variable objetivo** | Una frase que diga qué se predice y para qué lo usará el equipo de reservas, y la variable objetivo (`cancelada`) | 🟢 Mínimo | `informe_modelo.md` (apartado 1) |
| **Modelos comparados** | Tres modelos del *leaderboard* con su `score_test` y cuál elegís | 🟢 Mínimo | `informe_modelo.md` (apartado 2) |
| **Métrica elegida** | Qué métrica miráis (ROC-AUC) y por qué, con vuestras palabras | 🟢 Mínimo | `informe_modelo.md` (apartado 1) |
| **Importes y umbral** | Vuestros dos importes en euros (no los del cuaderno) y el umbral elegido | 🟢 Mínimo | `informe_modelo.md` (apartado 2) |
| **Llamada a la API** | El texto de la petición y la respuesta (probabilidad, alerta y umbral), sin claves | 🟢 Mínimo | `informe_modelo.md` (apartado 4) |
| **Recursos y costes** | La tabla de recursos con cuándo se creó, tiempo usado, coste y si está cerrado | 🟢 Mínimo | `informe_modelo.md` (apartado 5) |
| **Un riesgo citado** | Al menos un riesgo de IA responsable (por ejemplo, datos sintéticos) | 🟢 Mínimo | `informe_modelo.md` (apartado 6) |
| **Partición por fecha** | Entrenar con las reservas más antiguas y evaluar con las más recientes, con las fechas y las filas de cada parte | 🟡 Estándar | `informe_modelo.md` (apartado 2) |
| **Columnas revisadas** | Las 18 columnas razonadas una a una («¿se conoce al reservar?») y las excluidas explicadas | 🟡 Estándar | `informe_modelo.md` (apartado 1) |
| **Umbral comparado** | El coste del umbral elegido frente a «avisar a todos» y «no avisar nunca», con la razón de cada importe | 🟡 Estándar | `informe_modelo.md` (apartado 2) |
| **Frase para un directivo** | Qué cuesta cada error, cuántas cancelaciones se detectan y cuántas alertas serán falsas, sin jerga | 🟡 Estándar | `informe_modelo.md` (apartado 2) |
| **Se puede repetir** | Datos, versión de AutoGluon, preset, límite de tiempo, semilla, partición y umbral del servicio | 🟡 Estándar | `informe_modelo.md` (apartado 3) |
| **Cierre con prueba** | Una captura con la sesión de Colab desconectada y sin datos personales | 🟡 Estándar | `captura_cierre.png` |
| **Riesgos con medida** | Al menos dos riesgos, cada uno con lo que veis en vuestro caso y una medida; sin claves ni datos personales | 🟡 Estándar | `informe_modelo.md` (apartado 6) |
| **Recomendación al cliente** | Qué hacer con una alerta, para qué sirve el modelo y para qué no, y qué debe validar TurisData | 🟡 Estándar | `informe_modelo.md` (apartado 7) |
| **Informe único de 4 páginas** | Las tres partes (modelo, API y recursos) en un solo documento de 4 páginas como máximo | 🟡 Estándar | `informe_modelo.md` |
| **Revisión y autoevaluación** | Alguien que **no escribió esa parte** revisa el informe con la rúbrica (justo debajo de estas tablas) y anota nivel y prueba al final del informe; cada persona sube su hoja de autoevaluación y coevaluación; el equipo hace la review y la retro | 🟡 Estándar | Final de `informe_modelo.md` y `sprint-03/` |
| **Más modelos o ajustes** | Comparar más modelos o ajustes (otro límite de tiempo o preset) y explicar la diferencia | 🔴 Extra | `informe_modelo.md` (apartado 2) |
| **Datos imposibles** | Probar que la API rechaza una reserva imposible (`noches` = 0, código 422) y explicar qué significa | 🔴 Extra | `informe_modelo.md` (apartado 4) |
| **Cuaderno en el repositorio** | `S3.5_lab_autogluon.ipynb` con sus salidas, y el informe dice qué resultado debería salir | 🔴 Extra | `sprint-03/` y `informe_modelo.md` (apartado 3) |
| **Beneficio en euros** | Estimar el beneficio frente a no hacer nada y proponer cómo medirlo cuando el modelo esté en marcha | 🔴 Extra | `informe_modelo.md` (apartado 7) |
| **Sesgo comprobado con datos** | Mirar si el riesgo o las falsas alertas cambian por canal o país y decir qué se haría si saliera desigual | 🔴 Extra | `informe_modelo.md` (apartado 6) |

---

## 3 · 🧭 Rúbrica del reto · cómo se puntúa y cómo se revisa

La usan **dos veces**: el equipo, para revisar el informe antes de entregar, y el docente, para puntuar el sprint. Se mira **cada criterio por separado** y se pone el nivel de la columna cuyo texto **se cumple entero**: si lo de un nivel se cumple a medias, es el nivel de abajo. **0** significa que no se ha entregado nada de ese criterio.

Orientación: lo que pide el nivel 🟢 mínimo sale en un **2**, el 🟡 estándar en un **3** y los 🔴 extras en un **4**.

| Criterio | 1 · Empezado | 2 · Mínimo | 3 · Estándar | 4 · Extra |
|---|---|---|---|---|
| **Corrección técnica** (¿funciona y está bien planteado?) | Hay un modelo, pero se evaluó con los mismos datos con los que se entrenó, o no hay llamada a la API | Se compararon modelos y la API responde, pero la partición es al azar, no se revisaron las columnas que «delatan» la respuesta o falta la prueba de cierre | **Partición por fecha**; columnas excluidas explicadas; métrica coherente con el problema; umbral elegido con **vuestros importes** y comparado con «avisar a todos» y «no avisar nunca»; la API devuelve probabilidad y alerta; recursos cerrados **con captura** | Además, compara más modelos o ajustes y explica la diferencia, o prueba que la API rechaza una reserva con datos imposibles |
| **Reproducibilidad** (¿lo puede repetir otra persona?) | No se sabe con qué datos ni ajustes se entrenó | Se dice la herramienta y los datos, pero faltan ajustes (versión, preset, límite de tiempo, semilla o partición) | Otra persona puede repetir el experimento con el informe: **datos, versión, ajustes, semilla, partición** y los pasos para publicar el servicio | Además, el cuaderno está en el repositorio y el informe dice qué resultado debería salir |
| **Análisis y comunicación al cliente** (¿lo entiende quien no es técnico?) | Solo cifras o técnica, sin explicar | Explica la métrica y el umbral, pero con palabras que un directivo no entendería | Un directivo entiende qué modelo se eligió, **qué cuesta cada error** y **qué hacer con una alerta y con qué límites**; las tres partes caben en 4 páginas | Además, estima el beneficio en euros frente a no hacer nada y propone cómo medirlo cuando esté en marcha |
| **IA responsable** (¿se ven los riesgos y las medidas?) | No menciona riesgos | Cita un riesgo (por ejemplo, datos sintéticos) sin medida | **Al menos dos riesgos** (datos sintéticos, falsas alertas que molestan a clientes, sesgos por país o canal), cada uno con **una medida**; sin claves ni datos personales en el informe | Además, comprueba un sesgo con los datos (por ejemplo, falsas alertas por país o canal) y dice qué se haría si saliera desigual; una persona decide siempre ante la alerta |

**Cómo se revisa** (unos 10 minutos, antes de entregar; lo hace **una persona que no escribió esa parte**):

1. **Contar las partes:** el modelo (apartados 1 a 3, 6 y 7), la llamada a la API (4) y los recursos y costes (5), y que todo cabe en 4 páginas.
2. **Leer la parte del modelo con tres preguntas:** ¿se partió por fecha?, ¿se dicen las columnas excluidas y por qué?, ¿la métrica y el umbral se explican con importes?
3. **Mirar la evidencia:** en el apartado 4 se ven la petición y la respuesta **sin claves**; en `captura_cierre.png` se ve que **ya no hay sesión conectada**.
4. **Probar la reproducibilidad:** sin preguntar a nadie, ¿sabrías qué datos, versión, preset, semilla y partición se usaron?
5. **Leer como si fueras el director de TurisData:** ¿sabes qué hacer cuando llega una alerta y qué límites tiene?
6. **Poner un nivel (1 a 4) en cada criterio, con una frase de prueba** (por ejemplo: «2 · la partición es al azar»). Sin prueba escrita, el nivel no vale.
7. **Apuntar el resultado** en la tabla «Revisión con la rúbrica» del final del informe y corregir lo más fácil de arreglar. Lo demás se anota como mejora.

Cada persona, además, se puntúa a sí misma en su hoja de [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md) con **esta misma rúbrica**.
