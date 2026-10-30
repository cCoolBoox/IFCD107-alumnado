# Sprint 10 · Reto «¿Vale la pena la red?»

> **Ficha completa del reto, para consultar.** Para trabajar con ella abierta, usad [el reto en una página](../1_Reto_en_una_pagina/Reto_Sprint_10_una_pagina.md).
>
> - Volver al [README del sprint](../../README.md) · [README del sprint en PDF](../../pdf/README_Sprint_10.pdf) · [ecofriendly](../../pdf/README_Sprint_10_ecofriendly.pdf)
> - **Esta ficha en PDF:** [a color](pdf/Reto_Sprint_10.pdf) · [ecofriendly, para imprimir](pdf/Reto_Sprint_10_ecofriendly.pdf)
> - Si es vuestro primer reto: [Cómo se trabaja un reto](../../../../material/4.%20Como_se_trabaja_un_reto.md).

## Ficha del reto

### 1 · 🎯 Qué os pide el cliente

**Qué os pide el cliente.** La dirección de TurisData oye hablar de **redes neuronales** en todas partes y pregunta si debe **sustituir su modelo de cancelaciones por una red**. No quiere una opinión: quiere **evidencias, con el coste incluido**, para decidir si merece la pena el cambio. La pregunta del reto es *¿una red neuronal mejora al aprendizaje automático clásico, y a qué precio?*, y la respuesta puede ser **«no»**: un «no compensa» bien demostrado es tan válido y útil como un «sí». Vais a entrenar una red sencilla (un MLP, una red de capas de neuronas artificiales), a compararla con un modelo clásico de árboles (el *boosting*) y a escribir un **informe de 1–2 páginas** que termine en «Recomendamos… porque…».

**Cómo se trabaja.** No hace falta experiencia previa: os damos un **cuaderno de Colab casi hecho** (`S10_04`, con cuatro ejercicios con hueco y comprobaciones automáticas que os dicen si lo que escribís es correcto) y vuestro trabajo es completarlo, probar variantes, mirar las curvas, comparar con honestidad (con varias semillas, para que un número más alto no os engañe) y contarlo en el informe. En clase tenéis 10 minutos de planning (día 1) y unos **90 minutos de reto + 40 de entrega, review y retro** (día 2). Los seis pasos suman 145 minutos de trabajo: lo que no quepa en clase va a casa o a la 6.ª hora. El equipo decide hasta dónde llega: 🟢 mínimo, 🟡 estándar o 🔴 extra.

---

### 2 · 🧰 Recursos del reto

| Recurso | Para qué lo usaréis | Dónde está |
|---|---|---|
| **El cuaderno del reto** [`S10_04_reto_vale_la_pena`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/2_Practica/S10_04_reto_vale_la_pena.ipynb) | Es el esqueleto: partición, boosting de referencia, MLP con 3 semillas, curvas, comparación con intervalo y la variante de precio | Colab (basta con CPU; no hace falta GPU). Su [código explicado](../../2_Practica/codigo_explicado/S10_04_reto_vale_la_pena.md) lo cuenta celda a celda |
| **Cuadernos de práctica** [`S10_02`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/2_Practica/S10_02_mlp_keras.ipynb) y [`S10_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/2_Practica/S10_03_regularizacion.ipynb) | Las pistas: cómo se construye un MLP en Keras y cómo se ven y se combaten el sobreajuste, el *dropout*, la L2 y la parada temprana | Colab; su [código explicado](../../2_Practica/codigo_explicado/README.md) |
| **Presentación** [`S10.3`](../../1_Teoria/S10.3_Entrenamiento_y_regularizacion.pdf) y [apuntes de redes neuronales](../../1_Teoria/apuntes/apuntes_redes_neuronales.md) | Repasar las curvas de aprendizaje y la regularización (las diapositivas 6–7 son de este reto) | Carpeta de teoría del sprint |
| **Los datos** [`reservas_turisdata.csv`](../../../../datos/reservas_turisdata.csv) | 6000 reservas **sintéticas** (inventadas), con la columna `cancelada` y el `precio_noche` | El cuaderno los descarga solo en su primera celda; no hace falta tocarlos |
| **Google Colab** (Python, Keras y scikit-learn ya instalados) | Ejecutar el cuaderno sin instalar nada | colab.research.google.com; al terminar, *Archivo → Descargar → Descargar .ipynb* |
| **Cómo entregar en GitHub** | Subir el cuaderno, el informe y el README a `sprint-10/` desde el navegador | [Guía de entrega](../../../../material/5.%20Como_entregar_en_GitHub.md) |
| **Autoevaluación y coevaluación** | Cada persona rellena su hoja | [Hoja del sprint](../4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md) |
| **Un asistente de IA** (opcional) | Entender conceptos, curvas y errores de Keras | Con las reglas de la «Ayuda 1» del paso a paso |

---

### 3 · 📦 Qué entregar

Este apartado responde a **dos preguntas distintas**, una tabla para cada una:

**Tabla A · Los ficheros:** qué ficheros hay, de dónde sale cada uno (ya hecho, lo modificáis, lo creáis o lo genera el programa) y **cuáles se suben y adónde**.

**Tabla B · Los requisitos:** qué tiene que cumplir lo que entregáis y hasta dónde llegar (🟢 mínimo, 🟡 estándar, 🔴 extra). **Es lo que se evalúa.**

**En total, al final del sprint se suben a `sprint-10/`:** **3 ficheros del equipo** (`reto_vale_la_pena.ipynb`, `informe_comparativo.md`, `README.md`) **+ 1 autoevaluación y coevaluación por persona**, es decir, **3 + tantos ficheros como personas haya en el equipo** (un equipo de 4 sube 7). «El reto» no es un fichero aparte: son esos tres ficheros (el cuaderno ejecutado, el informe y el README que dice cómo repetirlo). Los datos no van a `sprint-10/`: el CSV va a `data/` si aún no está, y los extras solo si los hacéis. La *review* y la *retro* se hacen de palabra: no se suben.

#### Tabla A · Los ficheros: de dónde sale cada uno y cuáles se suben

Todo lo que se sube va al repositorio privado del equipo (`ifcd107-equipo-…`), en la carpeta **`sprint-10/`**, salvo el CSV.

| Fichero | Origen | Qué hacéis vosotros | ¿Se sube? |
|---|---|---|---|
| `reto_vale_la_pena.ipynb` | **Lo modificáis.** Parte del cuaderno `S10_04`, que trae el esqueleto y cuatro ejercicios con hueco | Completáis los ejercicios, añadís vuestras variantes y vuestro diagnóstico, y lo descargáis con **todas las celdas ejecutadas** (nombre en minúsculas y sin espacios) | **Sí** · `sprint-10/` |
| `informe_comparativo.md` | **Lo creáis.** No hay plantilla: su estructura está en el paso 6 | Escribís el informe de 1–2 páginas *ML clásico frente a MLP* y, al final, la sección «Revisión con la rúbrica» | **Sí** · `sprint-10/` |
| `README.md` | **Lo modificáis.** Ya está creado en `sprint-10/` con la plantilla del repositorio del equipo | Lo rellenáis: qué se entrega, quién hizo qué y cómo repetirlo (abrir en Colab y ejecutar de arriba abajo) | **Sí** · `sprint-10/` |
| `reservas_turisdata.csv` | **Ya hecho.** Los datos del curso (sintéticos) | Nada: el cuaderno los descarga solo; no se modifican | **Sí**, sin cambios · `data/` (si aún no está) |
| Autoevaluación y coevaluación (`autoevaluacion_nombre.md`) | **Ya hecha, en blanco** | Cada persona copia la plantilla con su nombre y la rellena; la coevaluación va **dentro del mismo fichero** | **Sí**, **una por persona** (no una por equipo) · `sprint-10/` |
| `curvas_aprendizaje.png` (opcional) | **Lo generáis** guardando desde el cuaderno el dibujo de las curvas | Solo si queréis ver la imagen dentro del informe | Solo si lo hacéis · `sprint-10/` |
| `mlp_final.keras` (extra) | **Lo genera** el cuaderno al guardar el MLP elegido | Solo si el equipo llega al nivel extra (guardar el modelo y probarlo recargado) | Solo si lo hacéis · `sprint-10/` |

#### Tabla B · Los requisitos: qué tiene que cumplir y hasta dónde llegar

| Requisito | Qué se pide exactamente | Nivel | Dónde se comprueba |
|---|---|---|---|
| **Cuaderno que se ejecuta** | De arriba abajo y sin errores, con semillas fijas, y con los cuatro ejercicios (`evaluar`, `aucs_mlp_val`, `diagnostico`, `hay_diferencia` y `mejor_modelo`) pasando sus comprobaciones | 🟢 Mínimo | `reto_vale_la_pena.ipynb` |
| **Partición única** | Una sola división entrenamiento / validación / prueba, igual para todos los modelos, que no se cambia; el escalador se ajusta **solo con el entrenamiento** | 🟢 Mínimo | `reto_vale_la_pena.ipynb` (sección 1) |
| **Referencia y MLP, con las mismas métricas** | Un modelo de referencia (el boosting del cuaderno o el campeón del Sprint 8) y un MLP de un solo problema (cancelaciones **o** precio), medidos con las mismas métricas y la misma partición; máximo 40 épocas | 🟢 Mínimo | `reto_vale_la_pena.ipynb` y la tabla del informe |
| **Curvas y diagnóstico** | Curva de aprendizaje del MLP (error en entrenamiento y en validación) y **una frase** que diga si hay sobreajuste, subajuste o buen ajuste | 🟢 Mínimo | `reto_vale_la_pena.ipynb` (sección 5) e informe |
| **La prueba, una sola vez** | El conjunto de prueba se mira una única vez, al final, con el modelo elegido y con la referencia | 🟢 Mínimo | `reto_vale_la_pena.ipynb` (sección 6) |
| **Recomendación en una frase** | «Recomendamos… porque…», al principio del informe | 🟢 Mínimo | `informe_comparativo.md` |
| **README del sprint** | Qué se entrega, quién hizo qué y cómo repetirlo | 🟢 Mínimo | `README.md` |
| **2–3 variantes del MLP** | Probar 2 o 3 variantes (tamaño, *dropout*, L2, tasa de aprendizaje o parada temprana), **elegidas mirando solo la validación**, con una tabla pequeña de resultados | 🟡 Estándar | `reto_vale_la_pena.ipynb` (sección 4) e informe |
| **Comparación con incertidumbre** | Varias semillas (por ejemplo, 3) con media ± desviación, o intervalo *bootstrap*; si los intervalos se solapan, no se dice que uno sea mejor | 🟡 Estándar | `reto_vale_la_pena.ipynb` (sección 6) e informe |
| **Coste** | Tiempo de entrenamiento, complejidad y explicabilidad de cada enfoque | 🟡 Estándar | `informe_comparativo.md` |
| **Informe completo** | Las seis partes del paso 6 (pregunta y respuesta, tabla con media ± desviación, curva comentada, coste, riesgos y límites) en 1–2 páginas, sin jerga que no se explique | 🟡 Estándar | `informe_comparativo.md` |
| **IA responsable** | Al menos **dos riesgos específicos de este caso** (datos sintéticos, umbral y coste de los errores por *overbooking*, posibles sesgos por país o canal) con una medida para cada uno; qué se pidió a la IA y qué se comprobó | 🟡 Estándar | `informe_comparativo.md` |
| **Revisión y autoevaluación** | Alguien que **no escribió esa parte** revisa cuaderno e informe con la rúbrica (justo debajo de estas tablas) y anota nivel y prueba en el informe; cada persona sube su hoja de autoevaluación y coevaluación | 🟡 Estándar | `informe_comparativo.md` (sección «Revisión con la rúbrica») y `sprint-10/` |
| **Extras** | Variante de regresión (precio por noche) con el mismo rigor · comparar el coste de entrenar y mantener cada modelo · guardar el modelo y probarlo recargado | 🔴 Extra | `reto_vale_la_pena.ipynb` (sección 7) · `informe_comparativo.md` · `mlp_final.keras` |

#### Rúbrica del reto · cómo se puntúa y cómo se revisa

La usan **dos veces**: el equipo, para revisar su propio trabajo antes de entregar, y el docente, para puntuar. Se mira **cada criterio por separado** y se pone el nivel de la columna cuyo texto **se cumple entero**: si lo de un nivel se cumple a medias, es el nivel de abajo. **0** significa que no se ha entregado nada de ese criterio.

Orientación: lo que pide el nivel 🟢 mínimo sale en un **2**, el 🟡 estándar en un **3** y los 🔴 extras en un **4**.

| Criterio | 1 · Empezado | 2 · Mínimo | 3 · Estándar | 4 · Extra |
|---|---|---|---|---|
| **Corrección técnica** (¿funciona y se mide bien?) | Hay cuaderno, pero se rompe al ejecutarlo de arriba abajo, fallan las comprobaciones o se ha mirado la prueba para decidir | Se ejecuta entero con semillas fijas; una sola partición; referencia y MLP medidos con las mismas métricas; curva de aprendizaje con una frase de diagnóstico; la prueba se usa una sola vez | Además, el escalador se ajusta solo con el entrenamiento, hay 2–3 variantes elegidas con la validación (con su tabla) y la comparación usa 3 semillas o *bootstrap*, con los cuatro ejercicios en verde | Además, la variante de precio con el mismo rigor, o el modelo guardado y recargado dando el mismo resultado |
| **Reproducibilidad** (¿lo puede repetir otra persona?) | Solo funciona en el Colab de quien lo escribió (celdas desordenadas o rutas propias) | El cuaderno se ejecuta de arriba abajo y el README dice qué se entrega, quién hizo qué y cómo abrirlo | Otra persona abre el cuaderno en Colab, pulsa *Reiniciar y ejecutar todo* y obtiene **las cifras del informe** siguiendo solo el README; los ficheros están en `sprint-10/`, subidos desde cuentas distintas | Además, el README indica las versiones (Python, Keras, scikit-learn), las semillas usadas y la ruta exacta de los datos |
| **Análisis y comunicación al cliente** (¿lo entiende quien no programa?) | El informe solo da números, sin decir qué significan | Tiene la tabla de ambos enfoques y la recomendación en una frase («Recomendamos… porque…») | Responde a «¿vale la pena?» con media ± desviación, dice si la diferencia es real o ruido, añade el coste (tiempo, complejidad, explicabilidad) y los límites, y comenta la curva, sin jerga | Además, dice **cuándo cambiaría la recomendación** (más datos, imágenes o texto) o qué pasaría con el umbral según lo que cueste un *overbooking* |
| **IA responsable** (¿se sabe qué hizo la IA y qué riesgos hay?) | No dice si se ha usado IA ni nombra ningún riesgo | Dice dónde se ha usado IA y nombra al menos un riesgo del caso | Dice **qué se pidió y qué se comprobó a mano**; nombra dos riesgos concretos (por ejemplo, datos sintéticos y *overbooking*) con una medida para cada uno; quien escribe sabe explicar cualquier celda | Además, aplica una medida y mide su efecto (por ejemplo, el error por país o canal, o un umbral distinto) o cuenta un fallo concreto de la IA que detectaron |

**Cómo se revisa** (unos 10 minutos, antes de subir; lo hace **una persona que no escribió esa parte**):

1. **Ejecutar** el cuaderno en una pestaña nueva de Colab: *Entorno de ejecución → Reiniciar y ejecutar todo*, siguiendo solo el README. Anotar si algo falla y si las cifras coinciden con las del informe.
2. **Leer el informe como si fuera el cliente**: ¿se entiende la respuesta a «¿vale la pena?» sin saber de redes neuronales? Subrayar lo que no se entienda.
3. **Mirar el cuaderno**: ¿hay una sola partición?, ¿se usa la prueba una sola vez?, ¿el escalador se ajusta solo con el entrenamiento? Que quien lo escribió explique una celda cualquiera.
4. **Poner un nivel (1 a 4) en cada criterio, con una frase de prueba** (por ejemplo: «3 · reinicia y ejecuta sin errores y el AUC coincide, pero falta explicar el coste»). Sin prueba escrita, el nivel no vale.
5. **Apuntar el resultado** en la sección «Revisión con la rúbrica» del final de `informe_comparativo.md` y corregir lo más fácil de arreglar. Lo demás se anota como mejora.

Cada persona, además, se puntúa a sí misma en su hoja de [autoevaluación y coevaluación](../4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md) con **esta misma rúbrica**.

---

### 4 · 🪜 Guía paso a paso

Son seis pasos, de **145 minutos en total**. Cada uno dice **qué hacéis** (la lista corta), **cómo se hace** con el detalle, **qué deberíais ver** y **cuándo está hecho**. Las ayudas (IA, errores, atascos) están al final. Si el tiempo aprieta, completad el nivel mínimo y dejad lo demás para casa. Trabajad siempre en **una copia** del cuaderno que sea vuestra, sin tocar el original del curso.

#### Paso 1 · Elegir el problema y reproducir la referencia (día 2, 15 minutos)
1. Elegir **un problema**: cancelaciones (`cancelada`) o precio (`precio_noche`).
2. Abrir `S10_04` en Colab y ejecutarlo bloque a bloque, entendiendo cada uno.
3. Reproducir el modelo de referencia y anotar su métrica y su tiempo.
4. Fijar la partición entrenamiento / validación / prueba y no cambiarla nunca más.

**Cómo se hace**
- **Elegir el problema.** El cuaderno trae montado el de cancelaciones, así que es el camino más corto. Si elegís precio, seguid la sección 7 del cuaderno (hay que **quitar `precio_noche` de las entradas**). El otro problema es opcional.
- **Abrir el cuaderno.** Pulsad el [enlace de Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/2_Practica/S10_04_reto_vale_la_pena.ipynb) y haced una copia (*Archivo → Guardar una copia en Drive*). **Ejecutad siempre primero la celda «Preparación»**, que descarga los datos.
- **Ir bloque a bloque.** Pulsad ▶ en cada celda y leed lo que pone antes. Los ejercicios 1 a 4 tienen un hueco (`...`) y dan error hasta que lo rellenéis: es lo normal. En este paso, haced el **ejercicio 1** (`evaluar`), la función que mide a todos los modelos por igual. Si no entendéis un bloque, preguntad antes de seguir.
- **La partición.** La sección 1 reparte 64 % entrenamiento, 16 % validación y 20 % prueba, con semilla fija. No toquéis ni la semilla ni los `random_state`. La validación sirve para **decidir**; la prueba, para el veredicto final y **una sola vez**.
- **La referencia.** La sección 3 entrena el boosting (`HistGradientBoostingClassifier`). Si vuestro equipo tiene un campeón del Sprint 8 (XGBoost, LightGBM, Random Forest…), usadlo en su lugar y compararéis con él. **No se cambia la referencia para que la red gane.**

**Qué deberíais ver.** Al ejecutar la partición, tres tamaños: `(3840, 35) (960, 35) (1200, 35)`. Al entrenar el boosting, una línea como `Boosting entrenado en 0.3 s · AUC validación = 0.73`. Un AUC de 0,5 sería lo mismo que tirar una moneda; uno cercano a 1,0 haría sospechar de una fuga de datos.

**Hecho cuando:** el cuaderno llega hasta el boosting sin errores, el ejercicio 1 pasa su comprobación y tenéis anotadas la métrica y el tiempo de la referencia.

#### Paso 2 · Primera red (día 2, 25 minutos)
1. Comprobar que los datos están escalados **ajustando el escalador solo con el entrenamiento**.
2. Entrenar un MLP pequeño en CPU, con un máximo de 40 épocas.
3. Dibujar la curva de aprendizaje: error en entrenamiento y en validación.
4. Hacer el ejercicio 2 (el AUC de cada semilla).

**Cómo se hace**
- **Escalar sin fugas.** Escalar es poner todas las columnas en una escala parecida para que la red aprenda bien. El cuaderno ya lo hace en la sección 1 con `pre.fit_transform(X_ent)` (solo entrenamiento) y `pre.transform(...)` para validación y prueba. Mirad por qué: si el escalador viera la prueba, la red «se enteraría» de ella (eso es una **fuga**).
- **El MLP.** La sección 4 define `construir_mlp`: dos capas ocultas (64 y 32 neuronas), L2, *dropout*, parada temprana y un máximo de 40 épocas. Si preferís algo todavía más pequeño (por ejemplo, 2 capas de 32 neuronas y unas 30 épocas), cambiad los argumentos `capas` y `epochs`. Se entrena con **3 semillas**, y en CPU tarda pocos minutos.
- **Las curvas.** La sección 5 dibuja, para cada semilla, el error en entrenamiento y en validación a lo largo de las épocas. Mirad también cuántas épocas hizo cada una antes de parar.
- **Ejercicio 2.** Calculad en `aucs_mlp_val` el AUC de cada modelo sobre la **validación** y en `auc_mlp_medio` su media.

**Qué deberíais ver.** Tres líneas, una por semilla, del estilo `semilla 1: 17 épocas, AUC validación = 0.7… (máx.)`, tres gráficas con dos curvas cada una y, tras el ejercicio 2, `AUC de validación por semilla: …` con la media. La comprobación del cuaderno espera una media entre 0,6 y 0,85.

**Hecho cuando:** hay un MLP entrenado con su curva de aprendizaje, el ejercicio 2 pasa su comprobación y sabéis decir en una frase qué hace una época.

#### Paso 3 · Variantes (día 2, 25 minutos)
1. Probar **2 o 3 variantes** del MLP cambiando un solo ajuste cada vez.
2. Compararlas mirando **solo la validación**: el test no se toca.
3. Anotar en una tabla pequeña qué ha mejorado y qué no.

**Cómo se hace**
- **Qué cambiar.** `construir_mlp` ya tiene los botones: `capas` (más o menos neuronas, por ejemplo `(32,)` o `(128, 64)`), `dropout` (por ejemplo `0.5`), `l2` (por ejemplo `0.01`) y `tasa` (la tasa de aprendizaje, por ejemplo `3e-4`). También podéis probar otra paciencia en la parada temprana. **Cambiad una sola cosa por variante**, para saber qué ha causado el efecto.
- **Cómo comparar.** Entrenad cada variante y fijaos en la pérdida (el error) y el AUC **de validación**. Una tabla basta:

| Variante | Qué cambia | Error en entrenamiento | Error en validación | AUC en validación |
|---|---|---|---|---|
| Base | `capas=(64, 32)`, `dropout=0.3`, `l2=0.003` | (vuestra cifra) | (vuestra cifra) | (vuestra cifra) |
| Variante 1 | (lo que cambiáis) | (vuestra cifra) | (vuestra cifra) | (vuestra cifra) |
| Variante 2 | (lo que cambiáis) | (vuestra cifra) | (vuestra cifra) | (vuestra cifra) |

- **Cómo elegir.** Quedaos con la variante que mejor salga **en validación**. Si dos quedan casi iguales, escoged la más sencilla. Si miráis la prueba para decidir, ya no es una prueba.

**Qué deberíais ver.** Una tabla con la base y las 2–3 variantes, y una frase por variante: «mejoró», «empeoró» o «igual», con el número al lado. Que una variante no mejore es un resultado válido: lo importante es apuntarlo.

**Hecho cuando:** tenéis la tabla rellena, habéis elegido una variante mirando solo la validación y sabéis explicar por qué.

#### Paso 4 · Diagnosticar el sobreajuste (día 2, 20 minutos)
1. Mirar las curvas de vuestra mejor red.
2. Hacer el ejercicio 3 (`diagnostico`).
3. Escribir una frase de diagnóstico.

**Cómo se hace**
- **Leer las curvas.** Hay tres formas típicas:
  - **Entrenamiento baja y validación sube:** la red memoriza (sobreajuste). Se arregla con más regularización, menos neuronas o parando antes.
  - **Las dos curvas están altas y juntas:** la red es demasiado simple (subajuste).
  - **Las dos bajan y se estabilizan juntas:** buen ajuste.
- **Ejercicio 3.** Escribid `diagnostico(historial, margen=0.03)`: devuelve `"sobreajuste"` si la pérdida de validación **final** supera a su **mínimo** en más de `margen`, o si la de entrenamiento final es menor que la de validación final en más de `0.15`; si no, `"sin sobreajuste claro"`. Los `assert` del cuaderno os dicen si va bien. Aplicadlo a las tres semillas.
- **La frase.** Una frase para vuestra mejor red, con una cifra o una época: «Con la variante X, la validación deja de mejorar en la época 11 y el entrenamiento sigue bajando: hay un poco de sobreajuste, que la parada temprana corta a tiempo».

**Qué deberíais ver.** Tres líneas `MLP semilla 1: …` con `sobreajuste` o `sin sobreajuste claro`, y vuestra frase escrita junto a la gráfica.

**Hecho cuando:** el ejercicio 3 pasa su comprobación y la frase de diagnóstico está escrita (en el cuaderno y, resumida, en el informe).

#### Paso 5 · Comparación justa (día 2, 25 minutos)
1. Repetir el entrenamiento con varias semillas y calcular media ± desviación.
2. Medir el veredicto en la prueba **una sola vez**, con el MLP elegido y con la referencia.
3. Hacer el ejercicio 4 (¿la diferencia es real o es ruido?).
4. Añadir el coste: tiempo, complejidad y explicabilidad.

**Cómo se hace**
- **Varias semillas.** El bucle de la sección 4 ya entrena con tres semillas (1, 2 y 3). Si el MLP elegido es una variante, **cambiad en ese bucle los argumentos de `construir_mlp`** y volved a ejecutar antes de seguir. Calculad la media y la desviación del AUC; si el modelo clásico da siempre exactamente la misma cifra, el intervalo *bootstrap* del cuaderno es vuestra medida de incertidumbre.
- **El veredicto.** La sección 6 usa la prueba **una sola vez**: media de las 3 semillas para el MLP y el boosting, con la función `evaluar` del ejercicio 1. Apuntad los resultados y no la volváis a mirar para cambiar nada.
- **¿Real o ruido?** El *bootstrap* remuestrea la prueba 300 veces y da un intervalo para la diferencia de AUC. **Si el intervalo incluye el 0, no podéis decir que uno sea mejor.** Eso es el **ejercicio 4**: `hay_diferencia` (verdadero si el intervalo no contiene el 0) y `mejor_modelo` (`"MLP"`, `"Boosting"` o `"Empate"`).
- **El coste.** La tabla del cuaderno ya trae el tiempo de entrenamiento y el número de parámetros. Añadid la **explicabilidad** (explicar por qué un boosting dice «cancelará» es más fácil que explicar una red). Una red puede mejorar un 1 % y tardar 20 veces más.

**Qué deberíais ver.** Una tabla con dos filas (`Boosting de árboles` y `MLP (media de 3 semillas)`) y las columnas AUC, AP, F1, precisión, tiempo y parámetros; una línea `Diferencia de AUC (MLP − boosting): … · intervalo 95 %: […]`, un histograma con una línea roja en el 0 y `Veredicto estadístico: …`. Con estos datos lo esperable es que los dos queden muy cerca, y un «Empate» es un resultado perfectamente válido.

**Hecho cuando:** el ejercicio 4 pasa su comprobación, tenéis media ± desviación (o intervalo) de ambos enfoques y los números del coste apuntados.

#### Paso 6 · Informe, revisión y entrega (día 2, 35 minutos)
1. Escribir el informe de 1 página, con la recomendación al principio.
2. Rellenar el README de `sprint-10/`.
3. Pedir a alguien que no escribió esa parte que revise con la rúbrica y anote el resultado al final del informe.
4. Subir los tres ficheros del equipo a `sprint-10/`, y cada persona su autoevaluación.

**Cómo se hace**
- **El informe** (`informe_comparativo.md`). Seis partes, en este orden:

| Parte | Qué escribís | De dónde sale |
|---|---|---|
| 1. Pregunta y respuesta | Una frase: «Recomendamos mantener / cambiar a… porque…» | Vuestra decisión del paso 5 |
| 2. Tabla de resultados | Media ± desviación de ambos enfoques (AUC, AP, F1) | Secciones 4 y 6 del cuaderno |
| 3. Curva comentada | Qué se ve y vuestra frase de diagnóstico | Paso 4 |
| 4. Coste | Tiempo, complejidad y explicabilidad | Paso 5 |
| 5. Riesgos de IA responsable | Al menos dos, específicos, con su medida (datos sintéticos; umbral y coste de los errores por *overbooking*; sesgos por país o canal) | Vuestra reflexión |
| 6. Límites | Qué no sabemos y qué haríamos después | Vuestra reflexión |

  Si queréis ver la curva en el informe, guardad la imagen del cuaderno como `curvas_aprendizaje.png` y subidla a `sprint-10/`. Añadid también una línea de **uso de la IA**: qué pedisteis y qué comprobasteis a mano.
- **El README.** Abrid `sprint-10/README.md` → lápiz ✏️ y completadlo: *Reto* («¿Vale la pena la red?»), *Qué se entrega* (el cuaderno y el informe), *Quién hizo qué* y *Cómo reproducirlo* («abrir en Colab y ejecutar de arriba abajo»).
- **La revisión con la rúbrica (5 minutos).** Quien revisa sigue los cinco pasos de «Cómo se revisa» (apartado 3) y añade al final del informe esta sección, con un nivel de 1 a 4 por criterio y **una frase de prueba**:

```
## Revisión con la rúbrica

Revisado por: (nombre) · Fecha: (dd/mm/aaaa)

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
|---|---|---|
| Corrección técnica | | |
| Reproducibilidad | | |
| Análisis y comunicación al cliente | | |
| IA responsable | | |

Lo primero que mejoraríamos: (una cosa concreta)
```

  Si hay tiempo, arreglad lo más fácil; lo demás queda como «lo primero que mejoraríamos». Si sobran minutos, empezad un extra (la variante de precio, o guardar el modelo y recargarlo).
- **Subir los ficheros (la vía del curso, desde el navegador).** Seguid [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md). Para el cuaderno: en Colab, *Entorno de ejecución → Reiniciar y ejecutar todo* y después *Archivo → Descargar → Descargar .ipynb* (renombradlo a `reto_vale_la_pena.ipynb`). En el repositorio del equipo: (1) **entrad primero en la carpeta `sprint-10`**; (2) *Add file → Upload files*; (3) arrastrad el fichero; (4) escribid un mensaje corto y pulsad **Commit changes**. El informe también se puede crear directamente con *Add file → Create new file*. Cada subida es un *commit* con el nombre de quien la hace, así que repartid: una persona sube el cuaderno, otra escribe el informe y otra rellena el README. El CSV va a `data/` solo si aún no está.

**Qué deberíais ver.** En la carpeta `sprint-10` del repositorio, el cuaderno con sus resultados visibles, el informe, el README relleno y una hoja de autoevaluación por persona (**3 + N**); y en el historial (el icono del reloj), *commits* de personas distintas.

**Hecho cuando:** otra persona podría repetir el cuaderno siguiendo solo el README, el informe termina con «Recomendamos… porque…» y trae la sección «Revisión con la rúbrica» rellena, y los ficheros están en `sprint-10/`.

**Después, en la entrega y la review:** cada persona rellena y sube su autoevaluación y coevaluación a `sprint-10/`, y el equipo enseña, en unos 5 minutos, la tabla comparativa, una curva de aprendizaje comentada y la recomendación en una frase, con el coste y los riesgos.

#### Ayuda 1 · Cómo usar la IA en este reto

La IA puede ahorrar tiempo, pero **explica con mucha seguridad cosas que pueden estar mal**. Reglas:
- **Solo se compara con las mismas métricas y la misma partición.** No vale cambiar la referencia para que la red gane.
- **Las variantes se eligen con la validación**, nunca con el test.
- **Todo lo que dé, lo ejecutáis y lo entendéis.** Si el docente pregunta por una celda, tenéis que saber explicarla.
- **Declaradlo** en el informe: dónde habéis usado IA y qué habéis comprobado. **Nada de datos personales ni claves** en una IA.

| Para qué | Ejemplo de petición | Qué comprobáis |
|---|---|---|
| Entender conceptos | «Explícame qué es el sobreajuste en una red neuronal con una analogía de estudiar para un examen memorizando» | Que lo explicáis con vuestras palabras |
| Interpretar una curva | «Mi pérdida de entrenamiento baja pero la de validación sube a partir de la época 12. ¿Qué significa y qué puedo probar?» | Que probáis lo que sugiere y comprobáis el efecto |
| Entender un error de Keras | «Me da este error: *[mensaje]* con este código: *[código]*» | Que entendéis la causa |
| Revisar el informe | «Léelo como un directivo y dime qué no se entiende» | Que no cambie cifras |

#### Ayuda 2 · Errores frecuentes (y cómo evitarlos)

| Error | Por qué ocurre | Cómo evitarlo |
|---|---|---|
| Escalar con todos los datos | Se olvida la fuga | `fit` del escalador solo con el entrenamiento |
| Mirar el test para elegir la variante | «Para saber cuál va mejor» | Solo validación; el test, una sola vez |
| Comparar con una sola semilla | «Ya ha salido mejor» | Varias semillas y media ± desviación |
| Entrenar 500 épocas | «Cuanto más, mejor» | Máximo 40 épocas y parada temprana |
| Concluir «la red es mejor» por 0,3 puntos | Se mira solo el número | Comparad los intervalos y añadid el coste |
| Informe sin recomendación | Se queda en los números | Terminad con «Recomendamos… porque…» |
| Una celda da error con `...` | Falta rellenar el hueco de un ejercicio | Completad los ejercicios en orden, del 1 al 4 |
| Subir el cuaderno sin resultados | Se descarga sin haberlo ejecutado | *Reiniciar y ejecutar todo* y después descargar el `.ipynb` |

#### Ayuda 3 · Si os atascáis

1. **La red no aprende (la pérdida no baja):** revisad que los datos estén escalados y probad una tasa de aprendizaje menor.
2. **Las curvas son ruidosas:** es normal en datos pequeños; usad varias semillas y promediad.
3. **No entendemos las curvas:** repasad [`S10_03_regularizacion`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/2_Practica/S10_03_regularizacion.ipynb), que tiene un ejemplo comentado, y el [código explicado de `S10_04`](../../2_Practica/codigo_explicado/S10_04_reto_vale_la_pena.md).
4. Preguntad al equipo y, después, al docente. Más ayuda: [Cómo se trabaja un reto](../../../../material/4.%20Como_se_trabaja_un_reto.md).
