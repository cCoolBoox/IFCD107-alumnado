# Sprint 7 · Reto «Precio y cancelación»

> **Ficha completa del reto, para consultar.** Para trabajar, [el reto en una página](../1_Trabajar/Reto_Sprint_07_una_pagina.md). Qué se sube y cómo se evalúa: [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md).
>
> - Volver al [README del sprint](../../README.md).
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
| **La plantilla del informe** [`informe_modelado_plantilla.md`](../1_Trabajar/plantillas/informe_modelado_plantilla.md) | Los apartados del informe, con huecos | En GitHub: copiad el texto con el botón *Raw* |
| **Matriz de confusión en sencillo** | Repasar FN, FP y por qué los errores no cuestan igual | [Explicación sencilla](../../1_Teoria/actividades/S07_matriz_de_confusion_en_sencillo.html) y [lámina de la matriz](../../4_Referencia/infografias/S07_04_matriz_de_confusion.png) |
| **Cómo entregar en GitHub** | Subir la carpeta `sprint-07/` desde el navegador | [Guía de entrega](../../../../material/5.%20Como_entregar_en_GitHub.md) (apartado 6: subir un cuaderno de Colab) |
| **Autoevaluación y coevaluación** | Cada persona rellena su hoja | [Hoja del sprint](../2_Entregar/autoevaluacion_y_coevaluacion.md) |
| **Un asistente de IA** (opcional) | Entender errores y métricas | Con las reglas de la «Ayuda 1» del paso a paso |

---

### 3 · 🪜 Guía paso a paso

Son cinco pasos, de **65 minutos en total** (25 el día 1 y 40 el día 2), más 15 minutos de entrega. Cada uno dice **qué hacéis** (la lista corta), **cómo se hace** con el detalle, **qué deberíais ver** y **cuándo está hecho**. Las ayudas (IA, errores, atascos) están al final. Si el tiempo aprieta, completad el nivel mínimo y dejad lo demás para casa. Antes del paso 1 ya habéis hecho el *planning* de 10 minutos (roles del sprint y tareas en el tablero).

**Cada paso tiene su propia página.** Abrid la que toque y volved aquí cuando acabéis:

- [Paso 1 · Acordar las hipótesis de coste y abrir el cuaderno (día 1, 5 minutos)](Reto_Sprint_07_paso_1.md)
- [Paso 2 · Regresión del precio (día 1, 20 minutos)](Reto_Sprint_07_paso_2.md)
- [Paso 3 · Clasificación de la cancelación y elección del umbral (día 2, 25 minutos)](Reto_Sprint_07_paso_3.md)
- [Paso 4 · Análisis de sensibilidad (día 2, 5 minutos)](Reto_Sprint_07_paso_4.md)
- [Paso 5 · Informe y README (día 2, 10 minutos)](Reto_Sprint_07_paso_5.md)

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
