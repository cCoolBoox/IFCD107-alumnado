# Sprint 7 · Reto «Precio y cancelación»

> **Ficha completa del reto, para consultar.** Para trabajar con ella abierta, usad [el reto en una página](../1_Reto_en_una_pagina/Reto_Sprint_07_una_pagina.md).
>
> - Volver al [README del sprint](../../README.md) · [README del sprint en PDF](../../pdf/README_Sprint_07.pdf) · [ecofriendly](../../pdf/README_Sprint_07_ecofriendly.pdf)
> - **Esta ficha en PDF:** [a color](pdf/Reto_Sprint_07.pdf) · [ecofriendly, para imprimir](pdf/Reto_Sprint_07_ecofriendly.pdf)
> - Si es vuestro primer reto: [Cómo se trabaja un reto](../../../../material/4.%20Como_se_trabaja_un_reto.md).

## Ficha del reto

### 1 · 🎯 Qué os pide el cliente

**Qué os pide el cliente.** El gerente de TurisData quiere **dos herramientas**. La primera es una **tarifa de referencia**: cuánto debería costar una noche según el tipo de habitación y la época (predecir un **número**: `precio_noche`). La segunda es un **aviso de riesgo de cancelación**, para decidir cuándo vender por encima de su capacidad (*overbooking*: aceptar más reservas que habitaciones, apostando a que algunas se cancelarán), que predice una **categoría**: `cancelada`, sí o no. Hay un detalle importante: **el gerente no quiere oír hablar de «AUC»**. Quiere saber **cuánto dinero se juega** si el modelo se equivoca en un sentido o en otro. Vuestro trabajo es **traducir las métricas a euros**: escribir cuánto cuesta cada tipo de error, elegir el umbral que menos cuesta, comprobar qué pasa si esos costes cambian y recomendar una acción con cifras.

**Cómo se trabaja.** No hace falta experiencia previa: los cuadernos del sprint (`S07_01` a `S07_04`) tienen casi todo el código que necesitáis, y vuestro trabajo es **reutilizarlo en un cuaderno nuevo** y **decidir** con él. Las hipótesis de coste son vuestras: la IA no las elige por vosotros. En clase tenéis 10 minutos de planning y **25 minutos de reto el día 1** (hipótesis de coste y precio), **30 el día 2** (cancelación, sensibilidad e informe) y **15 de entrega**; lo que no quepa va a casa o a la 6.ª hora. El equipo decide hasta dónde llega: 🟢 mínimo, 🟡 estándar o 🔴 extra.

---

### 2 · 🧰 Recursos del reto

| Recurso | Para qué lo usaréis | Dónde está |
|---|---|---|
| **Google Colab** (Python con `pandas`, `numpy`, `scikit-learn` y `matplotlib`, las librerías del curso) | Crear y ejecutar `reto_S07.ipynb` | [colab.research.google.com](https://colab.research.google.com) → *Nuevo cuaderno* |
| **El CSV** [`reservas_turisdata.csv`](../../../../datos/reservas_turisdata.csv) | 6000 reservas **sintéticas**; objetivos `precio_noche` y `cancelada` | Los cuadernos lo descargan solos con la función `dato()`; también en el botón *Download raw file* |
| **Cuadernos del sprint**: [`S07_01`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/S07_01_regresion_lineal_polinomica.ipynb) (regresión lineal) y [`S07_02`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/S07_02_ridge_lasso.ipynb) (Ridge y Lasso) | Las celdas para el modelo de **precio** | Colab; su [código explicado](../../2_Practica/codigo_explicado/README.md) |
| **Cuadernos del sprint**: [`S07_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/S07_03_regresion_logistica.ipynb) (logística, umbral y coste) y [`S07_04`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/S07_04_roc_pr_desbalance.ipynb) (ROC, PR y desbalance) | Las celdas para la **cancelación**; `S07_03` trae `coste_total`, el punto de partida para el coste | Colab |
| **Cuaderno** [`S07_05`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/S07_05_knn_naive_bayes.ipynb) (k-NN y Naive Bayes) | Solo para el segundo modelo del nivel extra | Colab |
| **La plantilla del informe** [`informe_modelado_plantilla.md`](../4_Plantillas_y_entrega/informe_modelado_plantilla.md) | Los apartados del informe, con huecos | En GitHub: copiad el texto con el botón *Raw* |
| **Matriz de confusión en sencillo** | Repasar FN, FP y por qué los errores no cuestan igual | [Explicación sencilla](../../1_Teoria/actividades/S07_matriz_de_confusion_en_sencillo.html) y [lámina de la matriz](../../4_Referencia/infografias/S07_04_matriz_de_confusion.png) |
| **Cómo entregar en GitHub** | Subir la carpeta `sprint-07/` desde el navegador | [Guía de entrega](../../../../material/5.%20Como_entregar_en_GitHub.md) (apartado 6: subir un cuaderno de Colab) |
| **Autoevaluación y coevaluación** | Cada persona rellena su hoja | [Hoja del sprint](../4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md) |
| **Un asistente de IA** (opcional) | Entender errores y métricas | Con las reglas de la «Ayuda 1» del paso a paso |

---

### 3 · 📦 Qué entregar

Este apartado responde a **dos preguntas distintas**, una tabla para cada una:

**Tabla A · Los ficheros:** qué ficheros hay, de dónde sale cada uno (ya hecho, lo modificáis, lo creáis o lo genera el programa) y **cuáles se suben y adónde**.

**Tabla B · Los requisitos:** qué tiene que cumplir lo que entregáis y hasta dónde llegar (🟢 mínimo, 🟡 estándar, 🔴 extra). **Es lo que se evalúa.**

**En total, al final del sprint se suben a `sprint-07/`:** **3 ficheros del equipo** (`informe_modelado.md`, `reto_S07.ipynb`, `README.md`) **+ 1 autoevaluación y coevaluación por persona**, es decir, **3 + tantos ficheros como personas haya en el equipo** (un equipo de 3 sube 6). «El reto» no es un fichero aparte: son esos tres ficheros. Además, el CSV va a `data/` si aún no está. La *review* y la *retro* se hacen de palabra, el jueves 12/11 junto con las del Sprint 8: no se suben.

#### Tabla A · Los ficheros: de dónde sale cada uno y cuáles se suben

Todo lo que se sube va al repositorio privado del equipo (`ifcd107-equipo-…`), en la carpeta **`sprint-07/`**, salvo el CSV.

| Fichero | Origen | Qué hacéis vosotros | ¿Se sube? |
|---|---|---|---|
| `reto_S07.ipynb` | **Lo creáis.** No hay plantilla: es un cuaderno nuevo de Colab | Reutilizáis las celdas de `S07_01` a `S07_04`: un modelo de **precio** y otro de **cancelación**, cada uno con su *baseline*, validación y métricas | **Sí** · `sprint-07/` |
| `informe_modelado.md` (o `.pdf`) | **Lo creáis a partir de una plantilla.** Os damos `informe_modelado_plantilla.md` con huecos | Copiarla como `informe_modelado.md` y rellenarla (2–3 páginas, con euros) | **Sí** · `sprint-07/` |
| `README.md` | **Lo modificáis.** La carpeta `sprint-07/` ya trae un `README.md` (si no, lo creáis) | Abrirlo con el lápiz ✏️ y escribir semilla, versiones, cómo ejecutar, quién hizo qué y el uso de la IA | **Sí** · `sprint-07/` |
| `reservas_turisdata.csv` | **Ya hecho.** Los datos reales (sintéticos) | Nada: se usa sin cambiarlo | **Sí**, sin cambios · `data/` (si aún no está) |
| Autoevaluación y coevaluación (`autoevaluacion_nombre.md`) | **Ya hecha, en blanco** | Cada persona copia la plantilla con su nombre y la rellena; la coevaluación va **dentro del mismo fichero** | **Sí**, **una por persona** (no una por equipo) · `sprint-07/` |
| Segundo modelo de clasificación (extra) | **Lo creáis vosotros**, dentro de `reto_S07.ipynb` | Solo si el equipo llega al nivel extra | Solo si lo hacéis · dentro de `reto_S07.ipynb` |
| Cuadernos de práctica `S07_01`–`S07_05` | **Ya hecho.** Son vuestras copias de trabajo del sprint | Usarlos como pista y copiar las celdas que os sirvan | **No se suben** |

#### Tabla B · Los requisitos: qué tiene que cumplir y hasta dónde llegar

| Requisito | Qué se pide exactamente | Nivel | Dónde se comprueba |
|---|---|---|---|
| **Sin fuga de datos** | Solo variables **conocidas en el momento de reservar**. `cancelada` no se usa para predecir el precio. Lista escrita de variables usadas y excluidas | 🟢 Mínimo | `reto_S07.ipynb` · `informe_modelado.md` (apartado 2) |
| **Precio: referencia y regresión lineal** | *Baseline* (predecir siempre el precio medio de entrenamiento) y regresión lineal, con MAE y RMSE **en euros** sobre datos de test | 🟢 Mínimo | `reto_S07.ipynb` · informe (apartado 3) |
| **Cancelación: referencia y logística** | Partición train/test, *baseline* (siempre «no cancela») y regresión logística, con matriz de confusión | 🟢 Mínimo | `reto_S07.ipynb` · informe (apartado 4) |
| **Hipótesis de coste** | `COSTE_FN` y `COSTE_FP` como variables del cuaderno, cada una con **una frase de razón**. «La IA dijo 200 €» no vale | 🟢 Mínimo | `reto_S07.ipynb` · informe (apartado 5) |
| **Umbral elegido** | Un umbral elegido y justificado en una frase. En el mínimo, puede salir de una tabla corta de umbrales | 🟢 Mínimo | `reto_S07.ipynb` · informe (apartado 5) |
| **Informe** | `informe_modelado.md` con resumen para el gerente (con euros), tabla de métricas de los dos modelos y las hipótesis de coste. En el mínimo, versión corta | 🟢 Mínimo | `informe_modelado.md` |
| **README y reproducibilidad** | `SEMILLA = 42`, versiones de Python y `scikit-learn`, cómo ejecutar el cuaderno de arriba abajo. Cómo se usó la IA: qué pedisteis y qué revisasteis | 🟢 Mínimo | `README.md` |
| **Git** | Todo subido a `sprint-07/` con mensajes de commit claros, de personas distintas, sin claves ni datos personales | 🟢 Mínimo | Historial del repositorio del equipo |
| **Mejora del precio** | Una mejora (interacciones, polinomio, Ridge o Lasso) con MAE, RMSE y **R²**, y una frase sobre si compensa la complejidad. Máximo 3 modelos por problema | 🟡 Estándar | `reto_S07.ipynb` · informe (apartado 3) |
| **Curvas y métricas de la cancelación** | Curvas ROC y PR con AUC y AP, explicados sin jerga en el informe | 🟡 Estándar | `reto_S07.ipynb` · informe (apartado 4) |
| **Umbral que minimiza el coste** | Probar muchos umbrales con **validación cruzada sobre train**, calcular `FN × COSTE_FN + FP × COSTE_FP` y elegir el menor. El test se usa **una sola vez**: coste sin modelo, con umbral 0,5 y con el umbral elegido | 🟡 Estándar | `reto_S07.ipynb` · informe (apartado 5) |
| **Análisis de sensibilidad** | Tabla o gráfico con el umbral óptimo y el coste total cuando cambian `COSTE_FN` y `COSTE_FP` (por ejemplo, FN el doble o FP la mitad) | 🟡 Estándar | `reto_S07.ipynb` · informe (apartado 5) |
| **Recomendación de negocio** | Acción concreta con cifras (umbral, ahorro frente a «no hacer nada») y **límites** (datos sintéticos de un solo hotel…) | 🟡 Estándar | `informe_modelado.md` (apartado 6) |
| **IA responsable** | Riesgos específicos en el informe: quién sufre los falsos positivos, si se penaliza a algún país o canal, qué pasa si se piden depósitos solo a ciertos clientes | 🟡 Estándar | `informe_modelado.md` (apartado 7) |
| **Revisión y autoevaluación** | Alguien que **no escribió esa parte** revisa cuaderno, informe y README con la rúbrica (justo debajo de estas tablas) y anota nivel y prueba en el informe (si va en PDF, en el README); cada persona sube su hoja de autoevaluación y coevaluación | 🟡 Estándar | `informe_modelado.md` (sección «Revisión con la rúbrica») y `sprint-07/` |
| **Extras** | Un segundo modelo de clasificación (por ejemplo, k-NN) comparado · remuestreo solo en train · recomendación de *overbooking* con el ahorro estimado en euros por temporada | 🔴 Extra | `reto_S07.ipynb` · `informe_modelado.md` |

#### Rúbrica del reto · cómo se puntúa y cómo se revisa

La usan **dos veces**: el equipo, para revisar su propio trabajo antes de entregar (es lo que dice la *Definition of Done*), y el docente, para puntuar. Se mira **cada criterio por separado** y se pone el nivel de la columna cuyo texto **se cumple entero**: si lo de un nivel se cumple a medias, es el nivel de abajo. **0** significa que no se ha entregado nada de ese criterio.

Orientación: lo que pide el nivel 🟢 mínimo sale en un **2**, el 🟡 estándar en un **3** y los 🔴 extras en un **4**.

| Criterio | 1 · Empezado | 2 · Mínimo | 3 · Estándar | 4 · Extra |
|---|---|---|---|---|
| **Corrección técnica** (¿funciona?) | Hay cuaderno, pero faltan los *baselines*, se usa `cancelada` para predecir el precio o no se ejecuta de arriba abajo | Precio y cancelación tienen *baseline* y modelo; MAE y RMSE en euros; matriz de confusión; sin fuga; `COSTE_FN` y `COSTE_FP` definidos y un umbral elegido | Mejora del precio con R²; ROC/PR con AUC y AP; umbral elegido con validación cruzada sobre train minimizando el coste; test usado **una sola vez**; máximo 3 modelos por problema | Además, un segundo modelo de clasificación comparado o remuestreo hecho solo en train, sin fuga, y las cifras del informe coinciden con las del cuaderno |
| **Reproducibilidad** (¿lo puede repetir otra persona?) | Solo funciona en la sesión de quien lo hizo (faltan celdas, rutas propias) | El README dice cómo ejecutar, pero falta la semilla o las versiones | Otra persona ejecuta el cuaderno de arriba abajo y obtiene **las mismas cifras** siguiendo solo el README (`SEMILLA = 42`, versiones, orden); todo en `sprint-07/`, el CSV en `data/` y commits de personas distintas, sin claves | Además, el README indica el orden exacto de ejecución y qué cifras del informe sale de qué celda |
| **Análisis y comunicación al cliente** (¿lo entiende quien no programa?) | El informe solo da métricas técnicas (AUC, RMSE) sin pasarlas a euros | El resumen para el gerente da el error del precio en euros y una hipótesis de coste con razón para cada error, pero sin sensibilidad ni límites | Recomendación con **cifras** (umbral, coste frente a «no hacer nada»), sensibilidad y límites, sin jerga: el gerente entiende qué hacer y cuánto se juega | Además, dice con qué costes la recomendación cambiaría y qué dato del hotel haría falta para afinarla |
| **IA responsable** (¿se sabe qué hizo la IA y qué comprobasteis?) | No dice si se ha usado IA ni habla de riesgos | Dice que se ha usado IA, o nombra riesgos genéricos, sin detalle | El README dice **qué se pidió, qué se revisó y qué se cambió**; los costes y el umbral salen de vuestro cálculo; el informe nombra riesgos **específicos** (falsos positivos, país o canal, depósitos) | Además, comprueba un riesgo con los datos (por ejemplo, la tasa de falsos positivos por canal o país), propone una medida y recuerda que los datos son sintéticos |

**Cómo se revisa** (unos 10 minutos, antes de subir; lo hace **una persona que no escribió esa parte**):

1. **Ejecutar** el cuaderno en una sesión nueva de Colab con *Entorno de ejecución → Reiniciar y ejecutar todo*, copiando solo lo que dice el README. Anotar si algo falla o si alguna cifra cambia respecto al informe.
2. **Leer el informe como si fuera el gerente:** ¿se entiende el resumen sin saber qué es el AUC? ¿La recomendación tiene euros y límites? Subrayar lo que no se entienda.
3. **Mirar el cuaderno:** ¿alguna variable no se conoce al reservar? ¿Se usa `X_test` antes de elegir el umbral? ¿Los costes están en `COSTE_FN` y `COSTE_FP`, con su razón? Que quien lo escribió explique cualquier celda que no entendáis.
4. **Poner un nivel (1 a 4) en cada criterio, con una frase de prueba.** Ejemplos: «Corrección técnica · 2: hay baselines y matriz, pero el umbral se eligió mirando el test en la celda 18»; «Reproducibilidad · 3: mismas cifras siguiendo el README, versiones indicadas»; «Análisis · 2: el resumen da el MAE en euros, pero falta decir qué pasa si el coste de FP se duplica»; «IA responsable · 3: dicen qué pidieron y qué revisaron, y hablan de depósitos por país». Sin prueba escrita, el nivel no vale.
5. **Apuntar el resultado** en la sección «Revisión con la rúbrica» del final de `informe_modelado.md` y corregir lo más fácil de arreglar. Lo demás se anota como mejora.

Cada persona, además, se puntúa a sí misma en su hoja de [autoevaluación y coevaluación](../4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md) con **esta misma rúbrica**.

---

### 4 · 🪜 Guía paso a paso

Son cinco pasos, de **55 minutos en total** (25 el día 1 y 30 el día 2), más 15 minutos de entrega. Cada uno dice **qué hacéis** (la lista corta), **cómo se hace** con el detalle, **qué deberíais ver** y **cuándo está hecho**. Las ayudas (IA, errores, atascos) están al final. Si el tiempo aprieta, completad el nivel mínimo y dejad lo demás para casa. Antes del paso 1 ya habéis hecho el *planning* de 10 minutos (roles del sprint y tareas en el tablero).

#### Paso 1 · Acordar las hipótesis de coste y abrir el cuaderno (día 1, 5 minutos)
1. Abrir un cuaderno nuevo en Colab con el nombre `reto_S07`.
2. Responder la pregunta central: ¿qué cuesta más, una cancelación no prevista o una falsa alarma?
3. Escribir una hipótesis de coste para cada error, con una frase de razón.

**Cómo se hace**
- **Abrir el cuaderno.** En [Colab](https://colab.research.google.com), *Nuevo cuaderno*, y ponedle `reto_S07`. En la primera celda copiad la celda «Preparación» de `S07_01` (la función `dato()` que descarga el CSV) y escribid `SEMILLA = 42`.
- **La pregunta central del informe.** Una **cancelación no prevista** es un falso negativo (FN): el modelo dice «no se cancelará», sí se cancela y la habitación queda vacía. Una **falsa alarma** es un falso positivo (FP): el modelo dice «se cancelará», no se cancela y el cliente llega y no hay sitio.
- **Hipótesis de coste.** Proponed una cifra en euros para cada error y **una frase de razón**. Ejemplos del enunciado: una cancelación no prevista cuesta **la mitad de una noche**, porque solo se revende la mitad de esas noches; una falsa alarma cuesta **una noche de compensación** (alojamiento en otro hotel y una disculpa). Para pasar «una noche» a euros, mirad el precio medio de `precio_noche` en los datos.
- **Escribidlas como variables**, con su razón en un comentario, para poder cambiarlas luego: `COSTE_FN = …  # razón` y `COSTE_FP = …  # razón`.

**Qué deberíais ver.** Una celda con `SEMILLA`, `COSTE_FN` y `COSTE_FP`, cada coste con su razón al lado, y el CSV cargado en un `DataFrame`.

**Hecho cuando:** el cuaderno abre y carga los datos, y las dos hipótesis de coste están escritas con su razón.

#### Paso 2 · Regresión del precio (día 1, 20 minutos)
1. Elegir las variables que **se conocen al reservar**; `cancelada` queda fuera.
2. Separar train y test, y medir el modelo de referencia (precio medio).
3. Ajustar la regresión lineal y comparar.
4. Probar una mejora y decidir si compensa. Contar el resultado en euros.

**Cómo se hace**
- **Variables sin fuga.** Haced una lista de las columnas del CSV y marcad cuáles se conocen **en el momento de reservar** (por ejemplo, tipo de habitación, mes de llegada, antelación, canal). **`cancelada` no se puede usar para predecir el precio**: es fuga, porque no se sabe hasta después. Apuntad la lista de usadas y excluidas: va en el informe.
- **Separar y medir la referencia.** Como en `S07_01`: `train_test_split` con 20 % de test y `random_state=SEMILLA`. El modelo de referencia (*baseline*) predice siempre la media del precio de entrenamiento (`DummyRegressor`). Medid MAE y RMSE sobre test.
- **Regresión lineal.** La de `S07_01` (`LinearRegression`), con las variables elegidas. Medid MAE, RMSE y R². ¿Mejora a la referencia?
- **Una mejora.** Interacciones o polinomio (`S07_01`) o regularización Ridge o Lasso (`S07_02`). Si apenas mejora, quedaos con el modelo sencillo y decidlo en el informe.
- **En euros.** Escribid una frase del tipo «nos equivocamos de media en X € por noche».

**Qué deberíais ver.** Una tabla con una fila por modelo (referencia, lineal y mejora) y las columnas MAE, RMSE y R². La lineal mejora a la referencia. Como orientación: en `S07_01`, con tipo de habitación y temporada, el cuaderno espera un R² por encima de 0,85 y un MAE de entre 5 y 15 €. Si el vuestro está muy lejos, mirad la «Ayuda 2».

**Hecho cuando:** la tabla de precio está en el cuaderno, sin `cancelada` entre las variables, y tenéis la frase del error medio en euros.

#### Paso 3 · Clasificación de la cancelación y elección del umbral (día 2, 15 minutos)
1. Separar train y test, y **no tocar el test** hasta el final.
2. Medir la referencia (siempre «no cancela») y la regresión logística; dibujar la matriz de confusión y las curvas ROC y PR.
3. Elegir el umbral que minimiza el coste con validación cruzada sobre train.
4. Usar el test **una sola vez**, al final, para dar el coste esperado.

**Cómo se hace**
- **Partir y modelos.** Como en `S07_03`: partición train/test y regresión logística. La referencia es un `DummyClassifier` que siempre dice «no cancela». Máximo 3 modelos por problema, referencia incluida.
- **Matriz y curvas.** Matriz de confusión en test (`S07_03`), y curvas ROC y PR con AUC y AP (`S07_04`: `roc_auc_score`, `average_precision_score`). Para el nivel mínimo basta la matriz.
- **El umbral.** El umbral es la probabilidad a partir de la cual decimos «se cancelará». Con `cross_val_predict` sobre train (como en `S07_03`) obtenéis las probabilidades; probad muchos umbrales (`np.arange(0.05, 0.96, 0.05)`) y calculad el coste de cada uno: `coste = FN × COSTE_FN + FP × COSTE_FP`. **Cuidado:** `coste_total` de `S07_03` trae por defecto FN = 3 y FP = 1; pasadle **vuestros** costes. El mejor umbral es el que **minimiza el coste**; no se lo dejéis elegir a la IA.
- **El test, una vez.** Con el umbral ya elegido, calculad el coste en test de tres formas: **sin modelo** (la referencia, que nunca avisa), con el umbral 0,5 y con el umbral elegido.

**Qué deberíais ver.** La matriz de confusión, una tabla o curva de coste por umbral con un mínimo claro y tres cifras de coste en test (sin modelo, umbral 0,5 y umbral elegido). El umbral elegido cuesta menos que el 0,5.

**Hecho cuando:** hay umbral elegido con vuestros costes, el coste en test está calculado una sola vez y nadie ha mirado el test para elegir el umbral.

#### Paso 4 · Análisis de sensibilidad (día 2, 5 minutos)
1. Cambiar los costes: ¿y si una noche vacía costara el doble? ¿y si la compensación costara la mitad?
2. Calcular el umbral óptimo y el coste total de cada combinación.
3. Resumir en una tabla y una frase.

**Cómo se hace**
- **Repetid la búsqueda del paso 3** dentro de un bucle: para cada pareja de costes, buscad el umbral de menor coste y guardad el resultado. Usad al menos tres combinaciones: la vuestra, FN el doble y FP la mitad.
- **Tabla.** Con las columnas `COSTE_FN`, `COSTE_FP`, umbral óptimo y coste total; un gráfico del umbral óptimo también vale.
- **La conclusión** es del tipo: «con estos costes recomendamos un umbral de X; si el coste de una falsa alarma sube al doble, el umbral sube a Y». Las cifras serán las de vuestro cuaderno.

**Qué deberíais ver.** Una tabla con al menos tres filas y cómo se mueve el umbral óptimo. Si FN se encarece, el umbral baja (se avisa más); si se encarece FP, sube.

**Hecho cuando:** la tabla (o el gráfico) está en el cuaderno y tenéis la frase de conclusión escrita.

#### Paso 5 · Informe y README (día 2, 10 minutos)
1. Copiar la plantilla como `informe_modelado.md` y rellenarla con las cifras del cuaderno.
2. Escribir el README: semilla, versiones, cómo ejecutar y uso de la IA.
3. Preparar la entrega: revisión con la rúbrica, subida y autoevaluación (los 15 minutos siguientes).

**Cómo se hace**
- **El informe.** Abrid [`informe_modelado_plantilla.md`](../4_Plantillas_y_entrega/informe_modelado_plantilla.md), pulsad *Raw*, copiad el texto y pegadlo en un archivo nuevo `informe_modelado.md`. Para el **nivel mínimo** bastan estas, en pocas líneas:

| Apartado de la plantilla | Qué escribís |
|---|---|
| 1 · Resumen para el gerente | Cinco líneas con euros: qué recomendáis, qué cuesta cada error y cuánto ahorráis frente a no hacer nada |
| 3 · Regresión | La tabla de MAE, RMSE y R² y la frase del error medio en euros |
| 4 · Clasificación | La tabla de métricas y la matriz de confusión con el umbral elegido |
| 5 · De las métricas a los euros | `COSTE_FN` y `COSTE_FP` con su razón, el umbral y el coste en test |

  Para el **nivel estándar**, completad también el 2 (variables usadas y excluidas), la sensibilidad del 5, el 6 (recomendación con cifras y límites) y el 7 (riesgos de IA responsable).
- **El README.** Cuatro cosas: `SEMILLA = 42`; las versiones (`!python --version` y `import sklearn; print(sklearn.__version__)` en una celda); cómo ejecutar (*abrir en Colab y ejecutar de arriba abajo*); y el uso de la IA (qué pedisteis y qué revisasteis). Añadid quién hizo qué.
- **La revisión con la rúbrica (5 minutos, al empezar la entrega).** Quien revisa sigue los cinco pasos de «Cómo se revisa» (apartado 3) y rellena la sección «Revisión con la rúbrica» del final de `informe_modelado.md`: un nivel de 1 a 4 por criterio y **una frase de prueba**.
- **Subir los ficheros (la vía del curso, desde el navegador).** Seguid [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md): (1) en Colab, *Entorno de ejecución → Reiniciar y ejecutar todo* y después *Archivo → Descargar → Descargar .ipynb*; (2) abrid el repositorio del equipo y **entrad primero en la carpeta `sprint-07`**; (3) *Add file → Upload files* y arrastrad los ficheros; (4) escribid un mensaje corto y pulsad **Commit changes**. Cada subida es un *commit* con el nombre de quien la hace. Un reparto posible: la persona A sube `reto_S07.ipynb` («Añado cuaderno del reto»), la B sube `informe_modelado.md` («Añado informe»), la C edita `README.md` («Completo README»). Los nombres de archivo, **en minúsculas y sin espacios**. El CSV va a `data/` del repositorio solo si aún no está.

**Qué deberíais ver.** En la carpeta `sprint-07` del repositorio, los tres ficheros del equipo y una hoja de autoevaluación por persona (**3 + N**); y en el historial (el icono del reloj), commits de personas distintas.

**Hecho cuando:** otra persona podría ejecutar el cuaderno siguiendo solo el README, la sección «Revisión con la rúbrica» del informe está rellena y todo está subido a `sprint-07/`.

**Después, 15 minutos de entrega:** cada persona rellena y sube su autoevaluación y coevaluación a `sprint-07/` (la parte de coevaluación se completa en la *review* del jueves 12/11, en el mismo fichero). En la *review* (5 minutos por equipo) enseñaréis la tabla comparativa de métricas, el umbral elegido y su coste en euros frente a «no hacer nada», y una frase de recomendación para el gerente. En la retrospectiva, pensad: ¿qué hipótesis de coste discutimos más? ¿Cómo cambia la decisión si cambia el coste? ¿Qué habríamos necesitado saber del hotel para afinar?

#### Ayuda 1 · Cómo usar la IA en este reto

La IA puede ahorrar tiempo, pero **da código que parece funcionar y no se entiende**, y también **cifras que parecen razonables y no lo son**. Reglas:
- **Las hipótesis de coste son vuestras.** Si la IA os da cifras, preguntaos de dónde salen y justificadlas. No sirve «la IA dijo 200 €».
- **No dejéis que la IA elija el umbral por vosotros:** debe salir del cálculo con vuestros costes.
- **Todo lo que dé, lo ejecutáis y lo entendéis.** Si el docente pregunta por una línea, tenéis que saber explicarla.
- **Declaradlo** en el README: qué pedisteis y qué revisasteis.
- **Nada de datos personales ni claves** en una IA.

| Para qué | Ejemplo de petición | Qué comprobáis |
|---|---|---|
| Entender una métrica | «Explícame la diferencia entre MAE y RMSE con un ejemplo de precios de hotel» | Que podéis explicar cuándo conviene cada una |
| Entender falsos positivos y negativos | «Dame un ejemplo en un hotel de falso positivo y falso negativo de un modelo de cancelaciones» | Que los asociáis a **vuestros** costes |
| Depurar código | «Este código de scikit-learn da este error: *[error]*. ¿Qué lo causa?» | Que lo entendéis y lo arregláis vosotros |
| Revisar la recomendación | «Lee esta recomendación al gerente y dime si hay algo ambiguo o demasiado técnico» | Que no cambie las cifras |

**Pista de IA responsable:** ¿quién sufre los falsos positivos (un cliente reubicado)? ¿Se penaliza a algún país o canal? ¿Qué pasa si el modelo se usa para pedir depósitos solo a ciertos clientes? Respondedlo en el informe.

#### Ayuda 2 · Errores frecuentes (y cómo evitarlos)

| Error | Por qué ocurre | Cómo evitarlo |
|---|---|---|
| Usar `cancelada` o información posterior para predecir el precio | No se piensa en el momento de la reserva | Hacer una lista de variables y marcar cuáles se conocen **al reservar** |
| Elegir el umbral mirando el test | «Queda mejor» | El umbral sale de validación cruzada sobre train; el test, **una sola vez** |
| Costes sin justificar, o los de la IA | Parece un detalle | Cada coste lleva una frase de razón y es del equipo |
| Dejar los costes por defecto de `coste_total` (3 y 1) | Se copia la celda de `S07_03` sin cambiarla | Pasar `COSTE_FN` y `COSTE_FP` a la función |
| Informe solo con AUC | Es lo que muestra el cuaderno | Traducir a euros: «el modelo ahorra X € frente a no hacer nada» |
| Probar 10 modelos | «Más es mejor» | Máximo **3 modelos por problema**, referencia incluida |
| Olvidar el análisis de sensibilidad | Parece opcional | Es lo que da robustez a la recomendación |
| El cuaderno da errores de dimensiones | La variable objetivo sigue dentro de `X`, o `X` e `y` no coinciden | Comprobar `X.shape` y `y.shape` y que `precio_noche` o `cancelada` no están en `X` |

#### Ayuda 3 · Si os atascáis

1. **No sabemos qué costes poner:** pensad en una noche de un alojamiento de TurisData, razonad con una frase y luego **variad** los costes en la sensibilidad.
2. **No entendemos el umbral:** pensad en un semáforo. Con el umbral muy bajo avisamos casi siempre (muchas falsas alarmas); muy alto, casi nunca (muchas cancelaciones sin detectar).
3. Repasad el cuaderno de esa parte (`S07_01` a `S07_04`) y su [código explicado](../../2_Practica/codigo_explicado/README.md). Después preguntad al equipo y, por último, al docente.
