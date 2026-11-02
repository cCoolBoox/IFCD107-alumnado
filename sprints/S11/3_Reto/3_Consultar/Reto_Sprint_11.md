# Sprint 11 · Reto «Visión artificial para el cliente»

> **Ficha completa del reto, para consultar.** Para trabajar, [el reto en una página](../1_Trabajar/Reto_Sprint_11_una_pagina.md). Qué se sube y cómo se evalúa: [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md).
>
> - Volver al [README del sprint](../../README.md).
> - Si es vuestro primer reto: [Cómo se trabaja un reto](../../../../material/4.%20Como_se_trabaja_un_reto.md).

## Ficha del reto

### 1 · 🎯 Qué os pide el cliente

**Qué os pide el cliente.** TurisData recibe **cientos de fotos** de alojamientos cada semana y una persona las clasifica a mano (hotel, apartamentos, casa rural, camping, piscina). Quiere saber si un **modelo de visión artificial** (una IA que trabaja con imágenes) puede **pre-clasificarlas** y, sobre todo, **en qué se equivoca**, para decidir cuánto puede fiarse de él y **qué fotos debe revisar una persona**. Lo importante no es el acierto, sino **saber cuándo no fiarse**: un modelo que acierta el 90 % pero no sabe cuándo falla es peligroso; uno que acierta el 85 % y dice «esto no lo tengo claro, que lo revise una persona» es útil. Os pide tres cosas: un **modelo** entrenado con *transfer learning* (reutilizar una red ya entrenada y adaptarla a vuestras clases), un **demostrador** (una función que recibe una foto y responde clase, confianza o «revisar a mano») y un **análisis de errores** de 1–2 páginas.

**Cómo se trabaja.** No hace falta experiencia previa: el cuaderno [`S11_04`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/2_Practica/S11_04_reto_vision_cliente.ipynb) (que practicáis el día 2) trae casi todo el código y cinco ejercicios cortos; vuestro trabajo es completarlo, entender los resultados y **mirar las fotos que el modelo falla**. Por defecto se usa un conjunto de **dibujos sintéticos** (no son fotos reales) y, si queréis, uno propio con licencia. En clase tenéis 10 minutos de planning y **25 minutos de reto el día 1**, **80 minutos el día 2** y 30 de entrega, *review* y retro; lo que no quepa va a casa o a la 6.ª hora. El equipo decide hasta dónde llega: 🟢 mínimo, 🟡 estándar o 🔴 extra.

---

### 2 · 🧰 Recursos del reto

| Recurso | Para qué lo usaréis | Dónde está |
|---|---|---|
| **Google Colab** (Python con TensorFlow/Keras y scikit-learn ya instalados) | Ejecutar el cuaderno sin instalar nada | En el navegador, con una cuenta de Google. Colab puede desconectarse: ejecutad otra vez desde arriba |
| **El cuaderno del reto** [`S11_04_reto_vision_cliente`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/2_Practica/S11_04_reto_vision_cliente.ipynb) | Es el esqueleto: genera el conjunto de fotos, parte los datos, entrena, evalúa y trae el demostrador | Colab. Haced una copia (*Archivo → Guardar una copia en Drive*); su [código explicado](../../2_Practica/codigo_explicado/S11_04_reto_vision_cliente.md) |
| **Cuadernos de las prácticas**: [`S11_01`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/2_Practica/S11_01_cnn.ipynb) (CNN) y [`S11_02`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/2_Practica/S11_02_transfer_learning.ipynb) (*transfer learning*) | Las pistas para congelar la red, entrenar la «cabeza» y hacer el ajuste fino | Colab |
| **Presentación y apuntes** [`S11.2`](../../1_Teoria/S11.2_Transfer_learning_y_fine_tuning.pdf) · [apuntes de visión por computador](../../1_Teoria/apuntes/apuntes_vision_por_computador.md) | Repasar qué es una CNN y qué es el *transfer learning* | En la carpeta del sprint |
| **Las fotos sintéticas** | 5 clases (hotel, apartamentos, casa rural, camping, piscina), 60 dibujos por clase; algunos con la etiqueta dudosa a propósito | Las **genera el propio cuaderno** la primera vez (o el script [`generar_dataset_sintetico.py`](../1_Trabajar/plantillas/generar_dataset_sintetico.py)) |
| **Fotos propias** (opcional) | Probar con fotos reales: hechas por vosotros o con licencia abierta, **sin personas reconocibles** | Una carpeta por clase; apuntad autor y licencia de cada una |
| **La plantilla del informe** [`plantilla_analisis_errores.md`](../1_Trabajar/plantillas/plantilla_analisis_errores.md) | Los seis apartados del informe, con huecos | En GitHub: copiad el texto con el botón *Raw* |
| **Cómo entregar en GitHub** | Subir los ficheros a `sprint-11/` y subir el cuaderno de Colab | [Guía de entrega](../../../../material/5.%20Como_entregar_en_GitHub.md) |
| **Autoevaluación y coevaluación** | Cada persona rellena su hoja | [Hoja del sprint](../2_Entregar/autoevaluacion_y_coevaluacion.md) |
| **Un asistente de IA** (opcional) | Entender errores y pedir ideas | Con las reglas de la «Ayuda 1» del paso a paso |

---

### 3 · 🪜 Guía paso a paso

Son cinco pasos, de **105 minutos en total**: el primero el día 1 (25 minutos) y los otros cuatro el día 2 (80 minutos). Cada uno dice **qué hacéis** (la lista corta), **cómo se hace** con el detalle, **qué deberíais ver** y **cuándo está hecho**. Las ayudas (IA, errores, atascos) están al final. Si el tiempo aprieta, completad el nivel mínimo y dejad lo demás para casa. Una idea para todo el reto: **primero se mira, después se mide**. Mirad siempre las fotos, no solo los números.

**Cada paso tiene su propia página.** Abrid la que toque y volved aquí cuando acabéis:

- [Paso 1 · Preparar los datos (día 1, 25 minutos)](Reto_Sprint_11_paso_1.md)
- [Paso 2 · Entrenar con *transfer learning* y una referencia (día 2, 25 minutos)](Reto_Sprint_11_paso_2.md)
- [Paso 3 · Evaluación y análisis de errores (día 2, 20 minutos)](Reto_Sprint_11_paso_3.md)
- [Paso 4 · Demostrador y umbral de confianza (día 2, 15 minutos)](Reto_Sprint_11_paso_4.md)
- [Paso 5 · Informe, README y entrega (día 2, 20 minutos)](Reto_Sprint_11_paso_5.md)

#### Ayuda 1 · Cómo usar la IA en este reto

La IA puede ahorrar tiempo, pero **suena muy segura aunque se equivoque** y no ha visto vuestras fotos. Reglas:
- **Todo lo que dé, lo ejecutáis y lo entendéis.** Si el docente pregunta por una línea o por un error del informe, tenéis que saber explicarlo.
- **Las hipótesis se comprueban mirando la foto.** La IA propone causas típicas; vosotros dejáis solo las que **se ven en vuestras fotos**.
- **Declaradlo** en el README: qué pedisteis, qué revisasteis y qué cambiasteis.
- **Nada de datos personales ni claves** en una IA, y **no subáis fotos con personas** a ningún servicio.

| Para qué | Ejemplo de petición | Qué comprobáis |
|---|---|---|
| Entender el *transfer learning* | «Explícame transfer learning con la analogía de un cocinero experto que aprende un plato nuevo» | Que podéis contarlo con vuestras palabras |
| Interpretar una matriz | «Mi modelo confunde mucho camping con casa rural. ¿Qué causas habituales puede haber?» | Que las contrastáis mirando las **fotos reales** |
| Entender un error de Keras | «Me sale este error al cargar las imágenes: *[mensaje completo]*. Explícame qué significa, sin darme todavía la solución» | Que entendéis la causa y lo arregláis vosotros |
| Revisar el informe | «Léelo como si fueras el cliente y dime qué no se entiende» | Que no cambia ninguna cifra |

#### Ayuda 2 · Errores frecuentes (y cómo evitarlos)

| Error | Por qué ocurre | Cómo evitarlo |
|---|---|---|
| `AssertionError` al ejecutar un ejercicio | La función no devuelve lo que pide el enunciado | Leer el mensaje del `assert`: dice qué esperaba. Probar con un ejemplo pequeño |
| La base original queda congelada | Se pone `trainable = False` sobre la base y no sobre la copia | Trabajar con la copia (`clone_model`); el ejercicio 2 lo comprueba |
| Fotos casi idénticas en entrenamiento y prueba | Se parte sin cuidado o se generan variantes antes de partir | No tocar la partición del cuaderno; si hacéis aumento de datos, solo con las fotos de entrenamiento |
| Pocas fotos en alguna clase | Es difícil conseguirlas | Mínimo 30 por clase; si no llegáis, avisad del límite en el informe |
| Fiarse solo de la exactitud global | Es un solo número y esconde las clases que fallan | Mirar las **métricas por clase** y la matriz de confusión |
| Analizar errores sin mirar las fotos | Es más cómodo | Abrir las fotos mal clasificadas una a una |
| Usar la prueba para decidir | Se prueba «a ver qué sale» varias veces | Decidir con validación; la prueba se mira **una vez** |
| Umbral de confianza «a ojo» | Se pone 0,5 sin más | Medir cobertura y acierto de varios umbrales |
| Usar fotos de internet sin licencia | «Total, es un curso» | Solo fotos propias o con licencia abierta; guardar autor y licencia |

#### Ayuda 3 · Si os atascáis

1. **Colab dice que no hay memoria o se desconecta:** reducid el tamaño de las imágenes o el número de fotos, y usad *Entorno de ejecución → Reiniciar y ejecutar todo*.
2. **El modelo acierta siempre la misma clase:** hay desequilibrio; comprobad con `contar_por_clase` cuántas fotos hay en cada clase.
3. **No sabemos explicar un error:** mirad la foto como si fuerais el modelo: ¿qué rasgo la haría parecerse a la otra clase?
4. **Hay menos de 6 errores en la prueba:** analizadlos todos y completad hasta 6 con errores de validación, diciéndolo en la tabla. Preguntad al docente si dudáis.
5. Repasad el apartado del paso en el que estáis y el [código explicado](../../2_Practica/codigo_explicado/S11_04_reto_vision_cliente.md) del cuaderno; después, preguntad al equipo y, por último, al docente.
