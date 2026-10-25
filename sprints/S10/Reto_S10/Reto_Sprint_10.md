# Sprint 10 · Reto «¿Vale la pena la red?»

> **Esta es la ficha completa del reto, explicada paso a paso** para quien nunca ha trabajado con esta metodología ni con IA. Léela entera **antes de empezar** y vuelve a ella cuando tengas dudas.
>
> - Si es tu primer reto, lee antes [Cómo se trabaja un reto](../../../material/4.%20Como_se_trabaja_un_reto.md).
> - Volver al [README del sprint](../README.md) · [Guía del sprint en PDF](../guia/Guia_Sprint_10.pdf) · [versión ecofriendly para imprimir](../guia/Guia_Sprint_10_ecofriendly.pdf).
> - **Este reto en PDF:** [a color](Reto_Sprint_10.pdf) · [ecofriendly, para imprimir](Reto_Sprint_10_ecofriendly.pdf).

## Ficha del reto

### En pocas palabras (léelo primero)

**Qué os pide el cliente.** La dirección de TurisData oye hablar de **redes neuronales** en todas partes y pregunta si debe **sustituir su modelo de cancelaciones por una red**. No quiere una opinión: quiere **evidencias, con el coste incluido**, para decidir si merece la pena el cambio.

**La pregunta guía del reto:** *¿una red neuronal mejora al aprendizaje automático clásico, y a qué precio?* Y la respuesta puede ser **«no»**. Un resultado honesto de «no compensa» es tan válido y útil como un «sí».

**Qué vais a hacer, en seis pasos:**
1. **Elegir un problema** (cancelaciones o precio) y reproducir vuestro modelo de referencia (el campeón del Sprint 8 o el boosting del cuaderno).
2. **Entrenar una red neuronal sencilla** (un MLP) con el mismo conjunto de datos.
3. **Probar 2 o 3 variantes** (tamaño, *dropout*, regularización L2, tasa de aprendizaje), mirando **solo la validación**.
4. **Diagnosticar el sobreajuste** con curvas de aprendizaje.
5. **Comparar de forma justa** con el modelo clásico (varias semillas, con incertidumbre).
6. **Escribir un informe** de 1–2 páginas con una recomendación: «Recomendamos… porque…».

**Qué vais a entregar:** un cuaderno ejecutable (basado en [`S10_04`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/notebooks/S10_04_reto_vale_la_pena.ipynb)) y un informe comparativo *ML clásico frente a MLP*.

**Qué vais a aprender haciéndolo:** a **entrenar una red sin que memorice**, a leer **curvas de aprendizaje**, y a **comparar con honestidad** (que un número sea mayor no basta).

**Cuánto tiempo:** unas 2 horas y 15 minutos entre el planning, el reto (≈ 2 h 15 min) y la entrega (días 1 y 2). El reto se hace en la segunda jornada, con el esqueleto del cuaderno [`S10_04`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/notebooks/S10_04_reto_vale_la_pena.ipynb) y lo practicado el lunes.

**Núcleo y extra.** Núcleo: un único problema: reproducir la referencia y una mejora con la red, bien medida. Extra: más experimentos y las prácticas «en casa».

### Palabras que van a aparecer en este reto

| Palabra | Qué significa, en sencillo |
|---|---|
| **Red neuronal / MLP** | Modelo formado por capas de «neuronas» artificiales que combinan los datos. MLP = red de capas totalmente conectadas |
| **Capa** | Un nivel de neuronas. Una red tiene una capa de entrada, capas ocultas y una de salida |
| **Época** | Una pasada completa de la red por todos los datos de entrenamiento |
| **Sobreajuste** | La red «memoriza» los ejemplos de entrenamiento y falla con datos nuevos |
| **Curva de aprendizaje** | Gráfico del error en entrenamiento y en validación a lo largo de las épocas |
| **Dropout** | Truco que «apaga» neuronas al azar al entrenar para que la red no memorice |
| **Regularización L2** | Penalización para que los números internos de la red no crezcan demasiado y no memorice |
| **Tasa de aprendizaje** | Tamaño de cada paso al ajustar la red |
| **Early stopping** | Parar el entrenamiento cuando la validación deja de mejorar |
| **Validación** | Datos usados para **decidir** cosas (variantes, parada). No son el test |
| **Test** | Datos guardados que se miran **una sola vez** al final |
| **Semilla** | Número que fija el azar. Las redes dan resultados distintos con semillas distintas, por eso se prueban varias |

**Contexto del cliente.** La dirección de TurisData Canarias oye hablar de redes neuronales en todas partes y pregunta si debe
sustituir su modelo de cancelaciones por una. No quiere una opinión: quiere evidencias, coste incluido, para decidir si
merece la pena el cambio.

**Qué se entrega y en qué formato**

1. **Notebook** ejecutable de principio a fin (basado en [`S10_04`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/notebooks/S10_04_reto_vale_la_pena.ipynb)), con semillas fijas.
2. **Informe comparativo** de 1–2 páginas (PDF o Markdown) *ML clásico frente a MLP*: tabla de resultados, curvas de aprendizaje y recomendación.

**Restricciones**

- Un solo problema a elegir: cancelaciones (`cancelada`) **o** precio (`precio_noche`). El otro es opcional.
- Misma partición para todos los modelos; la prueba se usa **una sola vez**.
- Modelo de referencia: tu campeón del Sprint 8 (o el boosting que trae el notebook).
- Máximo 40 épocas por entrenamiento y modelos pequeños (se ejecuta en CPU en pocos minutos).
- Sin fugas de datos: el escalador se ajusta solo con el entrenamiento.

**Criterios de evaluación** (0–4, la media alimenta "ejercicios y entregas")

| Criterio | Qué buscamos aquí |
|---|---|
| **Corrección técnica** | Partición correcta, preprocesado sin fuga, MLP regularizado, comparación justa (varias semillas o intervalo), curvas bien interpretadas. |
| **Reproducibilidad** | Se ejecuta desde el README; semillas y versiones fijadas; datos y script incluidos. |
| **Análisis y comunicación al cliente** | Respuesta clara a "¿vale la pena?": métricas con incertidumbre, coste (tiempo, complejidad, explicabilidad) y recomendación accionable con sus límites. |
| **IA responsable** | Riesgos concretos: datos sintéticos, umbral y coste de errores (overbooking), posibles sesgos por país o canal; medidas aplicadas y evaluadas. |

**Pasos sugeridos**

- **Día 1:** planning (15 min); las prácticas 01–03 os dan la red base, el MLP en Keras y la regularización.
- **Día 2 (2 h 15 min de reto):** ejecuta [`S10_04`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/notebooks/S10_04_reto_vale_la_pena.ipynb), entiende cada bloque, elige el problema y reproduce tu modelo de referencia; entrena el MLP y prueba 2 variantes (tamaño, *dropout*, L2 o tasa) mirando **solo la validación**.
- **También el martes:** diagnostica el sobreajuste con curvas y compara con la referencia (3 semillas, media ± desviación).
- **Cierre del martes:** informe de una página y presentación de 5 minutos; entrega, autoevaluación y coevaluación; **review + retrospectiva** (última hora).

### Guía paso a paso para principiantes

#### Paso 1 · Elegir el problema y reproducir la referencia (día 2, 15 minutos)
1. Elegid **un problema**: cancelaciones (`cancelada`) **o** precio (`precio_noche`). El otro es opcional.
2. Abrid [`S10_04_reto_vale_la_pena`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/notebooks/S10_04_reto_vale_la_pena.ipynb) y ejecutadlo bloque a bloque, **entendiendo cada uno** (si no lo entendéis, preguntad antes de seguir).
3. **Reproducid el modelo de referencia** (vuestro campeón del Sprint 8 o el boosting que trae el cuaderno) y anotad su métrica.
4. **Fijad la partición** entrenamiento / validación / prueba y no la cambiéis nunca más. **La prueba se usa una sola vez.**

#### Paso 2 · Primera red (día 2, 25 minutos)
1. Escalad los datos **ajustando el escalador solo con el entrenamiento** (si no, hay fuga).
2. Entrenad un MLP pequeño (por ejemplo, 2 capas ocultas de 32 neuronas), **máximo 30 épocas**. Se ejecuta en CPU en pocos minutos.
3. Dibujad la **curva de aprendizaje**: error en entrenamiento y en validación.

#### Paso 3 · Variantes (día 2, 25 minutos)
1. Probad **2 variantes**: más o menos neuronas, *dropout*, L2, otra tasa de aprendizaje, *early stopping*.
2. **Compararlas mirando solo la validación.** El test no se toca.
3. Anotad qué ha mejorado y qué no. Una tabla pequeña basta: *variante · error en entrenamiento · error en validación*.

#### Paso 4 · Diagnosticar el sobreajuste (día 2, 20 minutos)
Mirad vuestras curvas:
- **Entrenamiento baja y validación sube:** la red memoriza (sobreajuste). Soluciones: más regularización, menos neuronas, parar antes.
- **Las dos curvas están altas y juntas:** la red es demasiado simple (subajuste).
- **Las dos bajan y se estabilizan juntas:** buen ajuste.

Escribid **una frase de diagnóstico** para vuestra mejor red.

#### Paso 5 · Comparación justa (día 2, 25 minutos)
1. **Repetid el entrenamiento con varias semillas** (por ejemplo, 3) para el MLP y para el modelo clásico.
2. Calculad **media ± desviación** (o un intervalo) de la métrica.
3. Comparad: **si los intervalos se solapan, no podéis decir que uno sea mejor**.
4. Evaluad en el test **una sola vez**, con el MLP elegido y con el modelo clásico, y registrad ambos.
5. Añadid el **coste**: tiempo de entrenamiento, complejidad, explicabilidad. Una red puede mejorar un 1 % pero tardar 20 veces más y ser opaca.

#### Paso 6 · Informe y presentación (día 2, 35 minutos)
Informe de 1 página:
1. **Pregunta y respuesta en una frase** («Recomendamos mantener el boosting porque…»).
2. **Tabla de resultados** (media ± desviación) de ambos enfoques.
3. **Curva de aprendizaje comentada.**
4. **Coste** (tiempo, complejidad, explicabilidad).
5. **Riesgos de IA responsable** (al menos dos específicos) con medidas.
6. **Límites.**

### Cómo usar la IA en este reto

| Para qué | Ejemplo de petición | Qué tenéis que comprobar |
|---|---|---|
| Entender conceptos | «Explícame qué es el sobreajuste en una red neuronal con una analogía de estudiar para un examen memorizando» | Que lo explicáis con vuestras palabras |
| Interpretar una curva | «Mi pérdida de entrenamiento baja pero la de validación sube a partir de la época 12. ¿Qué significa y qué puedo probar?» | Que probáis lo que sugiere y compruebas el efecto |
| Entender un error de Keras | «Me da este error: *[mensaje]* con este código: *[código]*» | Que entendéis la causa |
| Revisar el informe | «Léelo como un directivo y dime qué no se entiende» | Que no cambie cifras |

**Reglas del reto:**
- **Solo se compara con las mismas métricas y la misma partición.** No vale cambiar la referencia para que la red gane.
- **Las variantes se eligen con la validación**, nunca con el test.
- Declarad dónde habéis usado IA y qué habéis comprobado.

**Pista de IA responsable:** datos sintéticos; qué pasa con el umbral y el coste de los errores (*overbooking*); posibles sesgos por país o canal. Elegid dos y proponed medidas.

### Errores frecuentes (y cómo evitarlos)

| Error | Por qué ocurre | Cómo evitarlo |
|---|---|---|
| Escalar con todos los datos | Se olvida la fuga | `fit` del escalador solo con entrenamiento |
| Mirar el test para elegir la variante | «Para saber cuál va mejor» | Solo validación; el test, una sola vez |
| Comparar con una sola semilla | «Ya ha salido mejor» | Varias semillas y media ± desviación |
| Entrenar 500 épocas | «Cuanto más, mejor» | Máximo 40 épocas y *early stopping* |
| Concluir «la red es mejor» por 0,3 puntos | Se mira solo el número | Comparad los intervalos y añadid el coste |
| Informe sin recomendación | Se queda en los números | Terminad con «Recomendamos… porque…» |

### Un buen resultado se parece a…

> *«Recomendamos mantener el boosting. El MLP alcanza un AUC de 0,77 ± 0,02 frente a 0,78 ± 0,01 del boosting: la diferencia no es significativa. Además, la red tarda 12 veces más en entrenar y es más difícil de explicar. Solo compensaría con muchos más datos o con imágenes o texto. Riesgos: …»* (Cifras de ejemplo.)

### Antes de entregar: autoevaluación rápida

Repasad estas preguntas y rellenad después la hoja [autoevaluacion_y_coevaluacion.md](autoevaluacion_y_coevaluacion.md) (cada persona sube la suya con su entrega).

| Pregunta | Sí / No |
|---|---|
| ¿El cuaderno se ejecuta de arriba abajo, con semillas fijas? | |
| ¿La partición es única y la prueba se usa una sola vez? | |
| ¿Hay al menos un MLP y un modelo de árboles/boosting comparados con las mismas métricas? | |
| ¿Hay curvas de aprendizaje y un diagnóstico explícito de sobreajuste? | |
| ¿La comparación tiene incertidumbre (varias semillas o bootstrap)? | |
| ¿El informe recomienda algo concreto, con coste y límites? | |
| ¿Hay al menos dos riesgos de IA responsable específicos? | |

### Si os atascáis

- **La red no aprende (la pérdida no baja):** revisad que los datos estén escalados y probad una tasa de aprendizaje menor.
- **Las curvas son ruidosas:** es normal en datos pequeños; usad varias semillas y promediad.
- **No entendemos las curvas:** repasad [`S10_03_regularizacion`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/notebooks/S10_03_regularizacion.ipynb), que tiene un ejemplo comentado.
- Más ayuda: [Cómo se trabaja un reto](../../../material/4.%20Como_se_trabaja_un_reto.md).

**Qué se enseña en la *review*.** La tabla comparativa, una curva de aprendizaje comentada y la recomendación en una frase
("Recomendamos… porque…"), con el coste y los riesgos.

## Definition of Done (lista de comprobación)

Si queda una casilla sin marcar, **el reto no está terminado**.

- [ ] El notebook se ejecuta de arriba abajo sin errores y con semillas fijas.
- [ ] La partición entrenamiento/validación/prueba es única y la prueba se usa una sola vez.
- [ ] Hay al menos un MLP y un modelo de árboles/boosting comparados con las mismas métricas.
- [ ] Incluye curvas de aprendizaje y un diagnóstico explícito de sobreajuste.
- [ ] La comparación tiene en cuenta la incertidumbre (varias semillas o bootstrap).
- [ ] El informe recomienda algo concreto, con coste y límites.
- [ ] Se mencionan al menos dos riesgos de IA responsable específicos de este caso.
- [ ] [Autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md) rellenadas (cada persona sube su hoja).
