# Sprint 3 · Reto «Primer modelo en producción»

> **Esta es la ficha completa del reto, explicada paso a paso** para quien nunca ha trabajado con esta metodología ni con IA. Léela entera **antes de empezar** y vuelve a ella cuando tengas dudas.
>
> - Si es tu primer reto, lee antes [Cómo se trabaja un reto](../../../material/4.%20Como_se_trabaja_un_reto.md).
> - Volver al [README del sprint](../README.md) · [Guía del sprint en PDF](../guia/Guia_Sprint_03.pdf) · [versión ecofriendly para imprimir](../guia/Guia_Sprint_03_ecofriendly.pdf).
> - **Este reto en PDF:** [a color](Reto_Sprint_03.pdf) · [ecofriendly, para imprimir](Reto_Sprint_03_ecofriendly.pdf).

## Ficha del reto

### En pocas palabras (léelo primero)

**Qué os pide el cliente.** TurisData ha perdido dinero porque algunas reservas se cancelan a última hora y la habitación se queda vacía. Os envía su histórico de reservas y os pide: *«¿Se puede construir algo que avise de qué reservas tienen más riesgo de cancelarse, y que mi equipo de reservas lo consulte desde otra aplicación?»* Es decir: **un modelo de IA funcionando como un servicio**, no solo un experimento.

**Este es vuestro primer modelo.** No hace falta saber programar: usaréis una plataforma de **AutoML** (una herramienta que prueba varios modelos por vosotros y os muestra los resultados). Vuestro trabajo es **entender lo que hace**, **elegir bien** y **explicárselo al cliente**.

**Qué vais a hacer, en seis pasos:**
1. **Mirar los datos** con SQL (los [scripts de práctica](../actividades/sql/)) y decidir qué se quiere predecir.
2. **Revisar las columnas** una a una: ¿se conocen en el momento de reservar? Si no, no pueden entrar (eso se llama *fuga de datos*).
3. **Lanzar un experimento** de AutoML y comparar los modelos que salgan.
4. **Elegir un umbral** (cuándo decimos «esta reserva tiene riesgo alto») pensando en dinero, no en números sueltos.
5. **Publicar el modelo como servicio (API)**, hacer una llamada al servicio, y **cerrar y borrar** todo lo que hayáis creado.
6. **Redactar el informe** (4 páginas máximo) con todo lo anterior.

**El laboratorio de AutoML y este reto.** El [laboratorio de AutoML](../actividades/automl/guia_automl_en_parejas.md) os da la **parte técnica**: partición por fecha, modelos, métrica, umbral con costes, API y cierre de recursos. Lo que **añade el reto** y el cuaderno no hace: mirar los datos con SQL, razonar cada columna, poner **vuestros** costes, los riesgos de IA responsable, la recomendación al cliente y el informe de 4 páginas.

**Qué vais a entregar:** un único documento de máximo 4 páginas con tres partes: informe del mejor modelo, evidencia de la llamada a la API e informe de recursos y costes.

**Qué vais a aprender haciéndolo:** el recorrido completo de un proyecto de IA, **del dato al servicio**, incluida una parte que mucha gente olvida: **vigilar el coste y cerrar los recursos**.

**Cuánto tiempo:** unas 2 horas y 10 minutos entre el planning, el reto y la entrega (días 1 y 2).

**Núcleo y extra.** Núcleo: el mejor modelo con su umbral (con vuestros costes), la llamada al servicio, el cierre y borrado de recursos (0 €) y el informe con riesgos y recomendación. Extra: comparar más modelos en AutoML y los scripts SQL 05–06 de CRUD e índices (en casa).

### Palabras que van a aparecer en este reto

| Palabra | Qué significa, en sencillo |
|---|---|
| **AutoML** | Herramienta que entrena y compara varios modelos automáticamente |
| **Variable objetivo** | Lo que queremos predecir. Aquí: si la reserva se cancela (sí / no) |
| **Variable** (o columna) | Cada dato de una reserva: canal, tarifa, antelación, país… |
| **Fuga de datos** | Cuando el modelo usa información que **no se conocería a la hora de decidir**. Hace trampa y sus resultados parecen mejores de lo que son |
| **Partición temporal** | Entrenar con reservas **antiguas** y evaluar con reservas **más recientes**, como pasaría en la realidad |
| **Métrica** | Un número que dice lo bien o mal que lo hace el modelo (por ejemplo, la exactitud o el AUC) |
| **Umbral** | El punto de corte. Si el modelo dice «70 % de riesgo» y el umbral es 60 %, se da la alerta |
| **Falsa alarma** | El modelo avisa de cancelación y la reserva se mantiene |
| **Cancelación no detectada** | El modelo no avisa y la reserva se cancela |
| **API** | Una puerta por la que otra aplicación puede preguntar al modelo y recibir una respuesta |
| **Recurso (en la nube)** | Todo lo que creáis en la plataforma: datos subidos, experimentos, servicios activos. **Consumen cuota o dinero** |
| **Explicabilidad** | Saber **qué variables** pesan más en la decisión del modelo |

### Contexto del cliente
*TurisData Canarias* nos ha enviado el histórico de sus reservas. Cada cancelación de última hora le deja una habitación vacía y le cuesta ingresos. Quiere saber si un modelo puede **avisar de las reservas con más riesgo de cancelarse** y que su equipo de reservas lo consulte desde otra aplicación. Vosotros sois el equipo que lo pone en marcha, de los datos al servicio.

### Qué tenéis que entregar
Un único documento (Markdown o PDF, máximo 4 páginas) con tres partes:
1. **Informe del mejor modelo:** cómo se ha planteado el problema, qué modelos se compararon, métrica elegida y por qué, resultados en datos no vistos, umbral de decisión elegido con su justificación de negocio y variables más influyentes.
2. **Evidencia de la llamada a la API:** captura o texto de una petición real al servicio del modelo, con la respuesta (probabilidad de cancelación y alerta). Sin claves ni credenciales visibles.
3. **Informe de recursos y costes:** qué recursos se han creado, cuánto tiempo y capacidad se han usado, cuánto ha costado o cuánto habría costado, y **prueba de que se han cerrado o eliminado** todos.

### Restricciones
- **Tiempo:** unas 1 h 30 min de reto en clase, más la entrega y la review (dentro de las 12 h del sprint).
- **Datos:** solo los datos sintéticos de TurisData. No subáis datos personales reales.
- **Recursos:** se trabaja con el límite de uso que indique el docente; todo recurso creado debe quedar cerrado o eliminado al terminar.
- **Seguridad:** nunca pongáis claves, contraseñas ni cadenas de conexión en el informe ni en repositorios.
- **Evitar la fuga de datos:** el modelo solo puede usar información disponible en el momento de hacer la reserva.

### Criterios de evaluación (rúbrica del curso, 0–4 en cada criterio)
| Criterio | Qué se mirará en este reto |
|---|---|
| **Corrección técnica** | Partición de datos adecuada, métrica coherente con el problema, comparación de modelos, umbral justificado, la API responde. |
| **Reproducibilidad** | Otra persona puede repetir el experimento con vuestro informe: datos, ajustes, versiones y pasos. |
| **Análisis y comunicación al cliente** | Conclusiones claras para alguien no técnico y recomendación accionable: qué hacer con una alerta y con qué límites. |
| **IA responsable** | Riesgos identificados (datos sintéticos, falsas alertas que perjudican a clientes, sesgos por país o canal) y medidas propuestas. |

### Pasos sugeridos
- **Día 1 (15 min):** planning del reto; el resto del día son las clases y las prácticas de SQL y NoSQL, que ya os dan el dato conocido.
- **Día 2 (2 h 35 min):** revisad el dato (SQL), decidid la variable objetivo y revisad las columnas (¿se conocen al reservar?); lanzad el experimento, comparad modelos, evaluad con una partición temporal y elegid el umbral; publicad el servicio, haced la llamada y cerrad todo.
- **Cierre del martes (40 min):** completad el informe de recursos, revisad con la rúbrica, entregad y haced la review y la retro. El informe se remata en casa esa tarde si hace falta.

### Guía paso a paso para principiantes

#### Paso 1 · Entender el problema y los datos (día 2, 20 minutos)
1. Releed la escena del cliente y respondeos con una frase: *«Queremos predecir ______ para que el equipo de reservas pueda ______»*.
2. Abrid [`turisdata.db`](../../../datos/turisdata.db) en DB Browser for SQLite, mirad `reservas` y calculad con `GROUP BY` el **% de cancelaciones** por canal.
3. **Decidid la variable objetivo** (la columna `cancelada`, sí/no).
4. **Revisad las columnas una a una** y respondeos para cada una: **¿la conoceríamos en el momento de hacer la reserva?** Si no (por ejemplo, un dato que solo existe después de cancelar), no puede entrar en el modelo.
5. **Ojo:** en este CSV no existen columnas que delaten la cancelación (como `fecha_cancelacion`): lo normal es excluir solo `id_reserva`, un simple identificador. Aun así, **razonadlo columna a columna y anotadlo: es parte del informe**.
6. Preparad la plataforma que indique el docente. Para el laboratorio con AutoGluon, abrid el [cuaderno en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S03/Reto_S03/laboratorio_automl/S3.5_lab_autogluon.ipynb) y seguid la [guía en parejas](../actividades/automl/guia_automl_en_parejas.md) (el resumen de una página es [`Guia_AutoML_AutoGluon.pdf`](../guia/Guia_AutoML_AutoGluon.pdf)). Los archivos del laboratorio (cuaderno, tres `.py`, `requirements.txt` y el CSV de reservas) están en [`laboratorio_automl/`](laboratorio_automl/).

#### Paso 2 · Lanzar el experimento y comparar modelos (día 2, 30 minutos; laboratorio AutoML)
1. **Partid los datos por fecha:** las reservas antiguas para entrenar, las más recientes para evaluar. (Si barajáis las filas al azar, el modelo «ve el futuro» y los resultados parecen mejores de lo que serían en la realidad.)
2. Lanzad el experimento y **apuntad los ajustes** para poder repetirlo: versión, preset, límite de tiempo, semilla y partición.
3. Cuando termine, mirad la **tabla de modelos**. No elijáis solo por el número más alto: apuntad qué métrica usáis y **por qué es la adecuada para este problema** (por ejemplo: si solo hay un 20 % de cancelaciones, un modelo que dice «nadie cancela» acierta el 80 % y no sirve para nada).
4. Mirad las **variables más influyentes** (explicabilidad). ¿Tienen sentido para el negocio?
5. Para el informe: la versión sale de `!pip show autogluon.tabular`; el cuaderno usa `medium_quality`, semilla 42 y partición 80/20 por fecha. Respetad el límite de tiempo y de uso que indique el docente y anotadlo.

#### Paso 3 · Elegir el umbral con criterio de negocio (día 2, 20 minutos; laboratorio AutoML)
1. Pensad en las dos formas de equivocarse:
   - **Falsa alarma:** se actúa sobre una reserva que no se iba a cancelar (cuesta una llamada, o molestar a un cliente).
   - **Cancelación no detectada:** se pierde la oportunidad de revender la habitación (cuesta una noche vacía).
2. Poned **vuestros importes** para cada error (los 100 € y 40 € del cuaderno son solo un ejemplo) y elegid un umbral. Explicadlo con una frase que entienda un directivo.
3. Comparad con **«avisar a todos»** y **«no avisar nunca»**: si el modelo no los mejora, no compensa. Puede pasar si la falsa alarma cuesta muy poco.
4. Evaluad el modelo con el umbral elegido en los datos que **no ha visto**.

#### Paso 4 · Publicar el servicio y hacer una llamada (día 2, 20 minutos; laboratorio AutoML)
1. Publicad el modelo como servicio siguiendo la guía (en el laboratorio, una API con FastAPI).
2. Haced **una llamada al servicio**: enviad los datos de una reserva ficticia y recibid la **probabilidad de cancelación** y la alerta.
3. **Ojo:** en el cuaderno la llamada la hace `TestClient`, dentro del propio cuaderno y sin red. Preguntad al docente si vale como evidencia o si hay que levantar el servicio con `uvicorn`.
4. **Capturad la petición y la respuesta**, pero **sin claves ni contraseñas visibles**. Si aparece una clave en la captura, tapadla.

#### Paso 5 · Cerrar y borrar (día 2, 10 minutos; importante, laboratorio AutoML)
1. **Parad y eliminad** el servicio publicado, el experimento y los datos subidos. Lo que se deja encendido **gasta cuota (o dinero)**.
2. En Colab: *Entorno de ejecución → Desconectar y eliminar entorno*, y capturad la pantalla como prueba.
3. Anotad en el informe: qué recursos creasteis, cuánto tiempo y capacidad usaron, cuánto ha costado o **habría costado** y **la prueba de que se han cerrado** (captura de la lista vacía de recursos).
4. Si algo no se puede borrar, **avisad al docente**.

#### Paso 6 · Redactar el informe (20 minutos en clase y el resto en la entrega; 4 páginas máximo)
Estructura recomendada:
1. **El problema y la métrica** (media página), con las columnas **excluidas** y por qué.
2. **Qué modelos se compararon y cuál ganó**, con el umbral y su razón de negocio (con **vuestros** importes).
3. **Variables que pesan más** y **cómo repetirlo**: datos, versión, ajustes y semilla.
4. **Evidencia de la llamada a la API.**
5. **Informe de recursos y costes**, con la prueba de cierre.
6. **Riesgos de IA responsable** (al menos dos: datos sintéticos, falsas alertas, sesgos por país o canal) y **una medida** para cada uno.
7. **Recomendación al cliente:** qué hacer con una alerta y con qué límites.

### Cómo usar la IA en este reto

| Para qué | Ejemplo de petición | Qué tenéis que comprobar |
|---|---|---|
| Entender el SQL | «Explícame esta consulta SQL línea por línea: *[pega tu consulta]*» | Ejecutadla y comprobad que hace lo que dice |
| Escribir una consulta | «Dada una tabla `reservas(id, canal, cancelada)`, escribe una consulta que calcule el % de cancelaciones por canal» | Que los nombres de columnas sean los **vuestros** y que el resultado tenga sentido |
| Interpretar una métrica | «Explícame qué es el AUC con un ejemplo de hotel, sin fórmulas» | Que podáis explicarlo vosotros |
| Redactar para un directivo | «Reescribe este párrafo para alguien que no sabe estadística: *[párrafo]*. No cambies las cifras» | Que las cifras sean idénticas |

**Muy importante:** **nunca peguéis claves de la plataforma, contraseñas ni cadenas de conexión** en una IA ni en el informe ni en el repositorio. Si por error ocurre, avisad al docente y **cambiad la clave**.

**No uséis la IA para inventar resultados:** todo número del informe debe salir de vuestro experimento.

### Errores frecuentes (y cómo evitarlos)

| Error | Por qué ocurre | Cómo evitarlo |
|---|---|---|
| Resultados «demasiado buenos» (casi 100 %) | Fuga de datos: una columna delata la respuesta | Revisad cada columna: ¿se conocería al reservar? |
| Elegir el modelo solo por la métrica más alta | Es lo más visible | Explicad **por qué esa métrica** y qué significa en euros |
| Barajar las filas al azar antes de partir | Es lo que se hace «de normal» | Aquí hay tiempo: **entrenad con lo antiguo, evaluad con lo reciente** |
| Dejar el servicio encendido | Se olvida | Cread una tarjeta «Cerrar recursos» en el tablero y hacedla en el último rato |
| Capturas con claves visibles | Prisa | Revisad la captura antes de subirla |
| Informe que solo habla de técnica | Se escribe para el docente | Releed como si fuerais el director de TurisData |

### Un buen resultado se parece a…

- **Una frase de recomendación:** *«Recomendamos alertar cuando el riesgo supere el 30 %: así detectamos casi 9 de cada 10 cancelaciones, aunque algo más de 4 de cada 10 alertas serán falsas. Con una cancelación no detectada valorada en 100 € y una falsa alarma en 40 €, el coste baja a unos 22.300 €, frente a 24.920 € si avisamos a todos y 57.700 € si no avisamos nunca.»* (Son las cifras del ejemplo del cuaderno: las vuestras cambiarán con vuestros importes. Fijaos en que el ahorro frente a «avisar a todos» es pequeño; decidlo con honestidad, es un límite del modelo.)
- **Columnas excluidas:** «Revisamos todas las columnas y solo excluimos `id_reserva`, que es un número de identificación y no explica nada. El resto se conoce al hacer la reserva».
- **Cómo repetirlo:** «AutoGluon (versión …), `medium_quality`, 120 s, semilla 42; el 80 % más antiguo para entrenar y el 20 % más reciente para evaluar».
- **Informe de recursos:** una tabla con *recurso · cuándo se creó · tiempo usado · coste · cerrado (sí/no) · prueba*.

### Antes de entregar: autoevaluación rápida

Repasad estas preguntas y rellenad después la hoja [autoevaluacion_y_coevaluacion.md](autoevaluacion_y_coevaluacion.md) (cada persona sube la suya con su entrega).

| Pregunta | Sí / No |
|---|---|
| ¿El informe tiene las tres partes y cabe en 4 páginas? | |
| ¿La métrica y el umbral están explicados en lenguaje de negocio? | |
| ¿Hay evidencia de una llamada a la API (petición y respuesta), sin credenciales? | |
| ¿Explicamos qué variables hemos excluido y por qué? | |
| ¿Hemos cerrado y eliminado todos los recursos y lo demostramos? | |
| ¿Hay al menos dos riesgos de IA responsable y una medida? | |
| ¿Otra persona ha revisado el informe con la rúbrica? | |

### Si os atascáis

- **El experimento falla o tarda mucho:** reducid el tamaño de los datos o el tiempo máximo, y avisad al docente.
- **No sabemos qué columna es una trampa:** haced una lista con todas las columnas y, a su lado, «¿se conoce al reservar? sí/no». Discutidla en equipo (en este CSV lo normal es que solo sobre `id_reserva`).
- **No encontramos cómo cerrar un recurso:** buscad en la plataforma «recursos» o «facturación»; si no lo veis, preguntad.
- Más ayuda: [Cómo se trabaja un reto](../../../material/4.%20Como_se_trabaja_un_reto.md).

### Qué se enseña en la review
Una demo de 5 minutos: (1) el problema y la métrica, (2) el mejor modelo y su umbral, (3) una llamada en directo a la API, (4) el informe de recursos con la prueba de cierre, (5) una recomendación para el cliente y un límite del modelo.

## Definition of Done (lista de comprobación)

Si queda una casilla sin marcar, **el reto no está terminado**.

- [ ] El informe tiene las tres partes y cabe en 4 páginas.
- [ ] La métrica y el umbral están justificados en lenguaje de negocio.
- [ ] Hay evidencia de una llamada a la API (petición y respuesta), sin credenciales.
- [ ] Se explica qué columnas se revisaron y cuáles se excluyeron (y por qué).
- [ ] Se indica cómo repetir el experimento (versión, ajustes, semilla).
- [ ] Todos los recursos creados están cerrados o eliminados y hay prueba.
- [ ] Se mencionan al menos dos riesgos de IA responsable y una medida.
- [ ] Otra persona del grupo ha revisado el informe con la rúbrica.
- [ ] [Autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md) rellenadas (cada persona sube su hoja).
