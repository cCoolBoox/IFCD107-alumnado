# Solucionario AutoML paso a paso · S03 (cuaderno `S3.5_lab_autogluon`)

> **Para quién:** alumnado de IFCD107. **Qué es:** las respuestas a las preguntas del laboratorio de AutoML, explicadas **paso a paso**, con **lo que debe salir** y los errores más típicos. Va con la [guía en parejas](guia_automl_en_parejas.md) y el [listado de pasos](listado_pasos_automl.md). Para entender **el código** línea a línea, mirad el [código explicado](codigo_explicado_automl.md).

## Cómo usar este solucionario

1. **Primero intentadlo vosotros** (en pareja, con el ciclo de 5 pasos de la guía). Si miráis la respuesta antes, no aprendéis a interpretar, solo a copiar frases.
2. Cuando la celda haya terminado, comparad **«Qué debe salir»** con vuestra pantalla. Los números pueden variar **un poco** entre equipos; la **forma** (qué modelo gana, qué variables pesan) debe parecerse.
3. Leed **«Cómo pensarlo»** y contrastad con **vuestra** respuesta.
4. **Importante para el reto:** lo de aquí son **ideas para entender**, no un informe que se pueda copiar. El informe del reto debe llevar **vuestros** números, **vuestros** costes y **vuestras** palabras.

**Los datos:** [`reservas_turisdata.csv`](../../Reto_S03/laboratorio_automl/reservas_turisdata.csv), 6.000 reservas y 18 columnas, **sintéticas** (inventadas). Las columnas están en el [esquema de turisdata.db](../esquema_turisdata/esquema_turisdata.md). Son las mismas reservas de las que habláis en SQL y NoSQL: `2.754` canceladas en total.

**Una advertencia sobre las cifras:** todas las que salen aquí vienen de una ejecución real con `LIMITE_TIEMPO = 120` en un ordenador sin redes neuronales. En **Colab** pueden aparecer más modelos en el leaderboard y los números moverse algo.

---

## Paso 1 · Cargar los datos

**Qué debe salir:** `(6000, 18)` y las 5 primeras filas.

**Cómo pensarlo:**

1. Cada fila es **una reserva**; cada columna, una característica suya.
2. Todas las columnas menos una (`cancelada`) se conocen **el día que se hace la reserva**. Esa es la que queremos predecir.
3. `id_reserva` es un número de serie: no explica nada, así que el cuaderno la **quita** antes de entrenar (si no, el modelo podría «aprenderse» filas concretas).

---

## Paso 2 · Explorar y calidad del dato

**Qué debe salir:**

- Las columnas `fecha_reserva` y `fecha_llegada` aparecen como `datetime64`.
- Nulos: solo **`pais_origen` con 138**.
- `Proporción de cancelaciones: 0.459`.

**Pregunta: ¿está desbalanceada la clase objetivo? ¿Qué métrica conviene?**

- Un **45,9 %** de canceladas (2.754 de 6.000) es una clase **casi equilibrada**: no es como un fraude que ocurre una vez entre mil.
- Aun así, la **exactitud** (porcentaje de aciertos) engaña: en la parte de prueba, decir «nadie cancela» acertaría un **51,9 %** sin haber aprendido nada. Por eso el cuaderno entrena con **ROC-AUC** (mide si el modelo **ordena** bien las reservas de más a menos riesgo) y luego mira **precisión y recall** al elegir el umbral.

**Pregunta: ¿qué columnas podrían provocar fuga de datos?**

Una **fuga de datos** es usar para predecir algo que **no sabríamos cuando hay que decidir**.

- **En estos datos no hay fuga evidente:** todas las columnas (canal, tarifa, depósito, antelación, noches, país…) se conocen **al reservar**. `antelacion_dias` es simplemente `fecha_llegada − fecha_reserva`, también conocida ese día. Y `cancelaciones_previas` cuenta cancelaciones **de antes**, no de esta reserva.
- **Ejemplos que sí serían fuga** si existieran: una columna `fecha_cancelacion`, `importe_reembolsado`, `motivo_cancelacion` o `estado_final`. Solo existen **después** de cancelar, y harían que el modelo pareciera perfecto... y fuera inútil en la vida real.
- **Truco para detectarla:** preguntad por cada columna *«¿la tendría ya el día que quiero dar la alerta?»*. Si no, fuera. Y desconfiad de una variable que **por sí sola** lo explica todo.

**Ojo con:** pensar que los 138 nulos hay que «arreglarlos» a mano. AutoGluon los trata solo; lo importante es **saber que están** y apuntarlo en el informe.

---

## Paso 3 · Partición temporal

**Qué debe salir:**

```
Entrenamiento: 4800 filas (2024-01-01 a 2025-08-06)
Prueba:        1200 filas (2025-08-06 a 2025-12-30)
```

**Pregunta: ¿por qué por fechas y no al azar?**

1. **En la vida real, el modelo se usa en el futuro.** El día que lo pongamos en marcha, solo conoceremos reservas pasadas y tendrá que predecir las nuevas.
2. **Repartir al azar mezcla pasado y futuro.** El modelo vería en el entrenamiento reservas de la misma semana que las de prueba (temporada, ofertas, eventos) y saldría **más optimista** de lo que será en realidad.
3. **Así la prueba es honesta:** simula lo que pasará. Fijaos en que la tasa de cancelación del periodo de prueba (**48,1 %**) no es la del entrenamiento (**45,4 %**): el mundo **cambia**, y el modelo tiene que aguantar ese cambio.

**Ojo con:** quitar el `sort_values("fecha_reserva")`. Sin ordenar, el «20 % final» sería un trozo cualquiera del archivo.

---

## Paso 4 · Entrenar

**Qué debe salir:** mucho texto (un bloque por cada modelo que prueba) y al final:

```
AutoGluon training complete ... Best model: WeightedEnsemble_L2
Tiempo de entrenamiento: 36 s
```

**Cómo pensarlo:**

1. `eval_metric="roc_auc"`: le decimos con qué «nota» elegir al mejor.
2. `time_limit`: el máximo de segundos. Con 120 s tarda **unos 36**, porque le basta con probar todos los modelos. Con `15` sale **el mismo orden de modelos** (en nuestra prueba, idénticos resultados), así que para un ensayo basta.
3. `presets="medium_quality"`: equilibrio entre rapidez y calidad.

**Ojo con:** pensar que «más tiempo = mejor modelo». Aquí no: pasada la barrera de probar todo, más segundos no mejoran nada.

---

## Paso 5 · Leaderboard

**Qué debe salir (ejecución de referencia):**

| Modelo | `score_test` | `score_val` | `fit_time` |
|---|---|---|---|
| **WeightedEnsemble_L2** | **0,722** | 0,779 | 10,3 s |
| CatBoost | 0,719 | 0,777 | 7,5 s |
| XGBoost | 0,719 | 0,761 | 0,7 s |
| LightGBMXT | 0,717 | 0,774 | 2,1 s |
| LightGBM | 0,715 | 0,763 | 0,5 s |
| ExtraTreesEntr | 0,705 | 0,752 | 1,4 s |
| … | … | … | … |
| RandomForestGini | 0,691 | 0,743 | 7,0 s |

**Pregunta: ¿el mejor modelo es un ensamblado? ¿Cuánto tarda cada uno? ¿Merece la pena?**

- **Sí.** `WeightedEnsemble_L2` **combina** varios (en esta ejecución, sobre todo CatBoost, LightGBMXT y algo de XGBoost) y reparte el voto.
- **Pero la ventaja es mínima:** 0,722 frente a 0,719 de CatBoost y 0,719 de XGBoost. Una diferencia de tres milésimas **no es relevante** con 1.200 reservas de prueba.
- **Y cuesta más:** el ensamblado necesita **todos** sus componentes (tiempo y espacio), mientras que XGBoost entrena en menos de **1 segundo** y casi empata. Si el servicio tuviera que ir en un servidor pequeño o responder muy rápido, **un modelo simple podría ser la mejor decisión**.
- **Qué responder en el informe:** «el ensamblado gana por muy poco; elegimos X porque…» y justificarlo con tiempo, tamaño o sencillez, no solo con el número.

**Pregunta: ¿por qué `score_val` (0,78) es mayor que `score_test` (0,72)?**

1. `score_val` se calcula con una parte de **las propias reservas de entrenamiento** que AutoGluon se guarda para elegir modelos: **mismo periodo** que lo que ha aprendido.
2. `score_test` usa el **futuro** (agosto–diciembre de 2025), que no se parece del todo al pasado.
3. Por eso la nota baja: es lo que pasa cuando el modelo se enfrenta a algo de verdad nuevo. **La cifra honesta es `score_test`**; la de validación es optimista.

**Ojo con:** presumir en el informe del 0,78. Un directivo que despliegue el modelo esperando un 0,78 se llevará una sorpresa.

---

## Paso 6 · Evaluar con dos umbrales

**Qué debe salir:**

```
Umbral 0.5: precisión=0.643 recall=0.601 F1=0.621
Umbral 0.3: precisión=0.567 recall=0.882 F1=0.691
ROC-AUC: 0.722
```

**Cómo leer la matriz de confusión (umbral 0,5):**

| | Dijo «no cancela» | Dijo «cancela» |
|---|---|---|
| **No canceló** (623 reservas) | **430** aciertos | **193** alertas falsas |
| **Canceló** (577 reservas) | **230** no previstas | **347** aciertos |

- **Precisión = 347 ÷ (347 + 193) = 0,64.** De cada 100 alertas, 64 eran cancelaciones de verdad.
- **Recall = 347 ÷ (347 + 230) = 0,60.** De cada 100 cancelaciones que ocurrieron, avisamos de 60 y **se nos escaparon 40**.
- **Exactitud = (430 + 347) ÷ 1.200 = 0,65.** Solo un poco mejor que el 0,52 de «nadie cancela».

**Pregunta de negocio: ¿qué cuesta más, una cancelación no prevista o una alerta falsa? ¿Qué umbral elegir?**

1. Una **cancelación no prevista** significa una habitación vacía que no hemos tratado de vender de nuevo: pérdida de ingreso.
2. Una **alerta falsa** significa que hemos actuado sin necesidad (llamar al cliente, ofrecer un descuento, sobrevender una habitación).
3. Normalmente **la primera cuesta más**, así que conviene **bajar el umbral**: con 0,3 detectamos el **88 %** de las cancelaciones (frente al 60 %), a cambio de una precisión algo menor (57 %).
4. **No hay un umbral «correcto» sin saber cuánto cuesta cada error.** Eso se calcula en el paso 6b.

**Ojo con:** quedarse con el 0,5 por ser «el normal». Es solo el valor por defecto.

---

## Paso 6b · Umbral con costes

**Con 100 € por cancelación no prevista y 40 € por alerta falsa, debe salir:**

| Umbral | Alertas | No previstas | Falsas | Coste |
|---|---|---|---|---|
| 0,1 | 1.156 | 4 | 583 | 23.720 € |
| **0,2** | 1.044 | 24 | 491 | **22.040 €** |
| 0,3 | 897 | 68 | 388 | 22.320 € |
| 0,4 | 717 | 137 | 277 | 24.780 € |
| 0,5 | 540 | 230 | 193 | 30.720 € |
| 0,6 | 380 | 316 | 119 | 36.360 € |
| 0,7 | 240 | 389 | 52 | 40.980 € |

Debajo, el cuaderno imprime: **umbral con menos coste: 0,2**; **umbral teórico: 0,29**; **no avisar nunca: 57.700 €**; **avisar a todos: 24.920 €**.

**Cómo se calcula el coste de una fila (por ejemplo, 0,5):** `100 € × 230 + 40 € × 193 = 23.000 + 7.720 = 30.720 €`.

**De dónde sale el umbral teórico 0,29:** dar la alerta compensa cuando
`probabilidad × 100 €  >  (1 − probabilidad) × 40 €`. Despejando: `probabilidad > 40 ÷ (100 + 40) = 0,29`. Es decir, **avisamos si la probabilidad supera 0,29**.

**Cómo pensarlo:**

1. Con estos costes, el umbral por defecto (0,5) cuesta **8.680 € más** que el mejor probado (0,2) y **8.400 € más** que 0,3.
2. Entre 0,2 y 0,3 la diferencia es de solo 280 €: **es una zona plana**. Da igual elegir 0,25 que 0,3; lo que importa es **no quedarse en 0,5**.
3. Que el mejor probado sea 0,2 y el teórico 0,29 **no es contradicción**: el teórico supone probabilidades perfectamente calibradas; el modelo real no lo está del todo.

**Pregunta: ¿gana el modelo a «avisar a todos»?**

Con 100 € y 40 €: **sí, pero por poco.** El modelo en su mejor umbral cuesta **22.040 €** y avisar a todos, **24.920 €** (un 13 % más). Y mucho mejor que no avisar nunca (57.700 €).

**Pregunta: ¿y si la alerta falsa costara 5 € en vez de 40?**

1. El umbral teórico baja a `5 ÷ (100 + 5) =` **0,05**: merece la pena avisar casi a cualquiera.
2. Los costes con 5 € de alerta falsa:

| Estrategia | Coste |
|---|---|
| Modelo con umbral 0,1 (el mejor probado) | 3.315 € |
| Modelo con umbral 0,5 | 23.965 € |
| **Avisar a todos** | **3.115 €** |
| No avisar nunca | 57.700 € |

3. **Conclusión:** si la alerta casi no cuesta, **avisar a todos gana al modelo**. El modelo solo aporta algo cuando **la alerta es cara o la capacidad es limitada** (por ejemplo, el hotel solo puede llamar a 100 clientes al día: entonces hay que elegir **a quiénes**, y para eso sirve ordenar por riesgo).
4. **Lección para el reto:** antes de decir «el modelo vale», **comparadlo con la alternativa tonta** (avisar a todos o a nadie). Un modelo que no gana a la alternativa tonta no justifica su coste.

**Ojo con:** copiar los 100 € y 40 € del cuaderno en el informe sin justificarlos. Son un **ejemplo**: el reto pide vuestras hipótesis y una frase que las explique.

---

## Paso 7 · Qué variables pesan más

**Qué debe salir (orientativo):**

| Variable | Importancia |
|---|---|
| `antelacion_dias` | ~0,07 |
| `deposito` | ~0,06 |
| `canal` | ~0,04 |
| `tarifa` | ~0,02 |
| El resto (`peticiones_especiales`, `cancelaciones_previas`, `noches`, `tipo_habitacion`, `regimen`, `ninos`…) | casi 0 |

**Cómo se calcula:** el cuaderno **baraja** una columna y mira cuánto empeora el modelo. Si empeora mucho, esa columna importaba.

**Pregunta: ¿tienen sentido para el negocio? ¿Alguna sospechosa de fuga?**

Los datos de la tabla lo confirman. Cancela más, en el CSV:

| Si… | …cancela |
|---|---|
| Se reserva con más de 90 días de antelación | **60 %** (con menos de 15 días, **26 %**) |
| No hay depósito | **54 %** (con depósito total, **26 %**) |
| El canal es `web_intermediaria` | **54 %** (`directo`, **32 %**) |
| La tarifa es `flexible` | **52 %** (`no_reembolsable`, **37 %**) |

1. **Tiene sentido:** quien reserva con meses de antelación, sin pagar nada y con tarifa flexible, **tiene muy poco que perder** al cancelar. Quien ha pagado un depósito y no puede recuperarlo, sí.
2. **No hay fuga:** las cuatro variables se conocen al reservar. Una sospechosa sería una que solo existe tras el desenlace.
3. **Matiz:** «importante» no es «causa». Que `canal` pese no demuestra que cambiar de canal evite cancelaciones; solo que **ayuda a predecir** (puede ser, por ejemplo, que ese canal atraiga a clientes distintos).

---

## Pasos 8 y 9 · Guardar, recargar y predecir

**Qué debe salir:**

```
Modelo recargado. Probabilidades de ejemplo: [0.457, 0.644, 0.543, 0.352, 0.123]
Ejemplo de predicción: {'probabilidad_cancelacion': 0.457, 'alerta': False}
```

**Cómo pensarlo:**

1. Guardar el modelo es lo que permite **usarlo sin volver a entrenarlo**. Es la idea de «desplegar»: el servicio solo **carga** la carpeta `modelo_cancelaciones`.
2. Se recarga para **comprobar** que lo guardado funciona: si las probabilidades del modelo recargado coinciden con las del original, todo bien.
3. `predecir_cancelacion` recibe **una reserva** (un diccionario) y devuelve su probabilidad y si hay alerta (`probabilidad ≥ 0,5`).

**Ojo con:** el `0,5` está **escrito en la función**. Si habéis elegido otro umbral en el paso 6b, no basta con decirlo en el informe: hay que reflejarlo (en la API, con la variable de entorno `UMBRAL`).

---

## Paso 10 · La API

**Qué debe salir:**

```
{'estado': 'ok', 'modelo': 'modelo_cancelaciones'}
200 {'probabilidad_cancelacion': 0.7907, 'alerta': True, 'umbral': 0.5}
```

(La probabilidad puede ser 0,78 o 0,79 según el equipo.)

**Cómo pensarlo:**

1. `GET /salud` pregunta «¿estás vivo?» y confirma que el modelo se ha cargado.
2. `POST /predecir` manda una reserva en formato JSON y devuelve probabilidad, alerta y el umbral usado.
3. La reserva de ejemplo es **de alto riesgo**: canal `web_intermediaria`, tarifa `flexible`, `sin_deposito` y 73 días de antelación. Justo lo que el paso 7 decía que empuja a cancelar, y el modelo responde **0,79**.
4. Una reserva de bajo riesgo (canal `directo`, tarifa `no_reembolsable`, depósito total, 10 días de antelación) da una probabilidad de **~0,06** y no hay alerta.

**Pregunta: probad `"noches": 0`.**

La API responde **422** con un mensaje como `Input should be greater than or equal to 1`. Es la **validación de datos** (pydantic): el servicio **rechaza** los datos imposibles **antes** de llegar al modelo, en vez de dar una predicción absurda. Un 422 aquí **no es un fallo**: es la API haciendo su trabajo.

---

## Paso 11 · Informe de recursos

**Qué debe salir:**

```
Tiempo de entrenamiento: 36 s (límite fijado: 120 s)
Tamaño del modelo en disco: ~225 MB
Coste económico: 0 EUR
```

**Cómo pensarlo:**

1. **Tiempo:** medio minuto de entrenamiento y coste de 0 €. En una nube de pago el reloj **corre** mientras haya algo encendido, aunque no lo uséis.
2. **Tamaño:** 225 MB para un modelo que acierta el 65 %: el ensamblado guarda **todos** los modelos que lo componen.
3. **Cerrar:** en Colab, *Entorno de ejecución → Desconectar y eliminar entorno de ejecución*. En una nube de pago, lo que se deja encendido **se factura**; el hábito de cerrar y **dejar prueba** es lo que se evalúa en el reto.

**Tabla de recursos, ejemplo orientativo** (rellenad la vuestra con fechas y datos reales):

| Recurso | Cuándo se creó | Tiempo usado | Coste | Cerrado | Prueba |
|---|---|---|---|---|---|
| Sesión de Colab | (fecha y hora) | (≈ 100 min) | 0 € | Sí | Captura de «Desconectar» |
| Carpeta `modelo_cancelaciones` | (fecha y hora) | — | 0 € | Sí (no se sube al repositorio) | Captura del repositorio sin esa carpeta |

---

## Ideas para el informe (no copiar: adaptad con vuestros números)

Un esquema de cómo se enlazan las ideas, con frases **orientativas**:

1. **Planteamiento:** *«Queremos avisar al hotel de qué reservas es probable que se cancelen, para actuar antes. Usamos 6.000 reservas de 2024–2025; entrenamos con las más antiguas y probamos con las más recientes porque en producción el modelo se enfrentará al futuro.»*
2. **Resultado:** *«El mejor modelo es X, con AUC de Y sobre datos no vistos. La nota de validación era más alta (Z) porque…»*
3. **Umbral:** *«Suponiendo que una cancelación no prevista cuesta A € porque… y una alerta falsa B € porque…, el umbral que minimiza el coste es C. Con él ahorramos D € frente a no avisar nunca y E € frente a avisar a todos.»*
4. **Explicabilidad:** *«Pesan sobre todo la antelación, el depósito y el canal, lo cual tiene sentido porque… No hay fuga porque todas se conocen al reservar.»*
5. **Límites:** *«Son datos sintéticos; el modelo acierta ~65 %, y no demuestra causas.»*

---

## Resumen: los errores más típicos del laboratorio

| Error | Por qué ocurre | Cómo evitarlo |
|---|---|---|
| Darse por satisfecho con el AUC de validación (0,78) | Es optimista: usa el mismo periodo | Citar siempre el de **prueba** (0,72) |
| Dejar el umbral en 0,5 | Es el valor por defecto | Calcularlo con **costes** (paso 6b) |
| Decir «el mejor umbral es 0,2» sin costes | El umbral depende de ellos | Siempre «con A € y B €…» |
| No comparar con «avisar a todos» | Se olvida la alternativa tonta | Calcularla (el cuaderno ya lo hace) |
| Elegir el ensamblado «porque gana» | La diferencia es de milésimas | Mirar tiempo, tamaño y sencillez |
| Pensar que importancia es causa | Se confunde predecir con explicar | Escribir «ayuda a predecir», no «provoca» |
| Quitar la partición por fechas | Parece un detalle | Sin ella, el resultado es demasiado optimista |
| No cerrar la sesión | Se olvida al terminar | Desconectar y **dejar captura** |
