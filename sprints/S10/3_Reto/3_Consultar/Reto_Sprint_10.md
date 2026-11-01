# Sprint 10 · Reto «¿Vale la pena la red?»

> **Ficha completa del reto, para consultar.** Para trabajar, [el reto en una página](../1_Trabajar/Reto_Sprint_10_una_pagina.md). Qué se sube y cómo se evalúa: [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md).
>
> - Volver al [README del sprint](../../README.md).
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
| **Autoevaluación y coevaluación** | Cada persona rellena su hoja | [Hoja del sprint](../2_Entregar/autoevaluacion_y_coevaluacion.md) |
| **Un asistente de IA** (opcional) | Entender conceptos, curvas y errores de Keras | Con las reglas de la «Ayuda 1» del paso a paso |

---

### 3 · 🪜 Guía paso a paso

Son seis pasos, de **145 minutos en total**. Cada uno dice **qué hacéis** (la lista corta), **cómo se hace** con el detalle, **qué deberíais ver** y **cuándo está hecho**. Las ayudas (IA, errores, atascos) están al final. En el horario del día 2 caben unos 105 minutos (90 de reto y 15 para poneros al día); los 40 que faltan se hacen en la **consolidación** (13:00–13:30) y en la **6.ª hora** (hasta las 14:30), y la subida puede hacerse hasta esa hora. Si el tiempo aprieta, completad el nivel mínimo y dejad lo demás para casa. Trabajad siempre en **una copia** del cuaderno que sea vuestra, sin tocar el original del curso.

**Cada paso tiene su propia página.** Abrid la que toque y volved aquí cuando acabéis:

- [Paso 1 · Elegir el problema y reproducir la referencia (día 2, 15 minutos)](Reto_Sprint_10_paso_1.md)
- [Paso 2 · Primera red (día 2, 25 minutos)](Reto_Sprint_10_paso_2.md)
- [Paso 3 · Variantes (día 2, 25 minutos)](Reto_Sprint_10_paso_3.md)
- [Paso 4 · Diagnosticar el sobreajuste (día 2, 20 minutos)](Reto_Sprint_10_paso_4.md)
- [Paso 5 · Comparación justa (día 2, 25 minutos)](Reto_Sprint_10_paso_5.md)
- [Paso 6 · Informe, revisión y entrega (día 2, 35 minutos)](Reto_Sprint_10_paso_6.md)

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
