# Sprint 6 · Reto «Datos sucios, cliente impaciente»

> **Ficha completa del reto, para consultar.** Para trabajar, [el reto en una página](../1_Trabajar/Reto_Sprint_06_una_pagina.md). Qué se sube y cómo se evalúa: [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md).
>
> - Volver al [README del sprint](../../README.md).
> - Si es vuestro primer reto: [Cómo se trabaja un reto](../../../../material/4.%20Como_se_trabaja_un_reto.md).

## Ficha del reto

### 1 · 🎯 Qué os pide el cliente

**Qué os pide el cliente.** TurisData Canarias os manda por correo un fichero de reservas, [`reservas_sucio.csv`](../../../../datos/reservas_sucio.csv), **exportado a mano desde varios sistemas**. El gerente quiere un primer modelo que prediga qué reservas se cancelan «para ayer», pero **no se fía de los datos** (con razón). Os pide dos cosas: un **informe corto** que diga **qué está mal en los datos y por qué**, y un **proceso automático** (una función y un *pipeline*, es decir, una cadena de pasos que se ejecuta siempre igual) que deje los datos listos cada vez que le llegue un fichero así, con un primer modelo sencillo de referencia (un *baseline*) para saber si merece la pena seguir.

**Cómo se trabaja.** Los datos reales siempre vienen sucios (fechas escritas de varias maneras, países con distintos nombres, números imposibles, filas repetidas, huecos…) y limpiarlos es entre el 60 y el 80 % del trabajo en un proyecto de IA. No hace falta experiencia previa: ya habéis practicado cada técnica en los cuadernos del sprint, y aquí las juntáis en un caso real. Regla de oro: **toda corrección va escrita en código**, nunca editando el CSV a mano, para que se pueda repetir. En clase tenéis 10 minutos de planning (día 1), **80 minutos de reto** (30 el día 1 y 50 el día 2) y **35 de entrega, review y retrospectiva** (día 2); lo que no quepa va a casa o a la 6.ª hora. El equipo decide hasta dónde llega: 🟢 mínimo, 🟡 estándar o 🔴 extra.

---

### 2 · 🧰 Recursos del reto

| Recurso | Para qué lo usaréis | Dónde está |
|---|---|---|
| **Google Colab** (Python con `pandas`, `matplotlib`, `seaborn` y `scikit-learn`, ya instalados) | Escribir y ejecutar `reto_S06.ipynb` | Colab, con vuestra cuenta de Google. Solo librerías del curso |
| **El CSV sucio** [`reservas_sucio.csv`](../../../../datos/reservas_sucio.csv) | Los datos del cliente (sintéticos, sin datos personales). **No se edita a mano** | Los cuadernos del sprint lo descargan solos con la función `dato(...)` de su primera celda; cópiala en vuestro cuaderno |
| **La plantilla del informe** [`informe_calidad_plantilla.md`](../1_Trabajar/plantillas/informe_calidad_plantilla.md) | Tabla de defectos, antes y después, preguntas al cliente, IA responsable y revisión con la rúbrica | En GitHub: abrid el archivo y copiad el texto con el botón *Raw* |
| **Cuadernos del sprint**: [`S06_01`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/2_Practica/S06_01_pandas_eda.ipynb) (EDA y `resumen_calidad`) y [`S06_02`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/2_Practica/S06_02_limpieza.ipynb) (limpieza y mini-reto `limpiar_reservas`) | Las técnicas y el código de partida para el inventario y la limpieza | Colab; su [código explicado](../../2_Practica/codigo_explicado/README.md) |
| **Cuadernos del sprint**: [`S06_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/2_Practica/S06_03_preprocesado_pipeline.ipynb) (*pipeline*) y [`S06_04`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/2_Practica/S06_04_metricas_validacion.ipynb) (*baseline*, métricas y validación cruzada) | El código de partida para el *pipeline* y la comparación con el modelo «tonto» | Colab; su código explicado: [`S06_03`](../../2_Practica/codigo_explicado/S06_03_preprocesado_pipeline.md) y [`S06_04`](../../2_Practica/codigo_explicado/S06_04_metricas_validacion.md) |
| **Cómo entregar en GitHub** | Subir la carpeta `sprint-06/` (incluido el cuaderno de Colab, apartado 6 de la guía) | [Guía de entrega](../../../../material/5.%20Como_entregar_en_GitHub.md) |
| **Autoevaluación y coevaluación** | Cada persona rellena su hoja | [Hoja del sprint](../2_Entregar/autoevaluacion_y_coevaluacion.md) |
| **Un asistente de IA** (opcional) | Entender errores y pedir pistas | Con las reglas de la «Ayuda 1» del paso a paso |

---

### 3 · 🪜 Guía paso a paso

Son cinco pasos, de **90 minutos en total** (10 de planning y 80 de reto). Cada uno dice **qué hacéis** (la lista corta), **cómo se hace** con el detalle, **qué deberíais ver** y **cuándo está hecho**. Las ayudas (IA, errores, atascos) están al final. Si el tiempo aprieta, completad el nivel mínimo y dejad lo demás para casa.

#### Palabras que van a aparecer en este reto

| Palabra | Qué significa, en sencillo |
|---|---|
| **Defecto de calidad** | Un problema del dato: huecos (nulos), duplicados, valores imposibles, formatos mezclados… |
| **Imputar** | Rellenar un hueco con un valor razonable (la mediana, la categoría más frecuente…) |
| **Outlier** (valor atípico) | Un valor muy raro. A veces es un error y a veces es real: hay que decidir |
| **Train / test** | Los datos con los que entrena el modelo (*train*) y los que se guardan para evaluarlo (*test*) |
| **Pipeline** | Una cadena de pasos de preparación y modelo que se ejecuta siempre igual |
| **Fuga de datos** | Cuando información del *test* «se cuela» en el entrenamiento y los resultados parecen mejores de lo que son |
| **Baseline y `DummyClassifier`** | El modelo de referencia, y un «modelo tonto» (por ejemplo, responde siempre la clase más frecuente) que es el suelo con el que comparar |
| **Validación cruzada** | Entrenar y evaluar varias veces con particiones distintas para tener una medida más fiable (media ± desviación) |

**Cada paso tiene su propia página.** Abrid la que toque y volved aquí cuando acabéis:

- [Paso 1 · Planning y reparto de roles (día 1, 10 minutos)](Reto_Sprint_06_paso_1.md)
- [Paso 2 · Inventario de defectos (día 1, 30 minutos)](Reto_Sprint_06_paso_2.md)
- [Paso 3 · Función de limpieza y partición train/test (día 2, 15 minutos)](Reto_Sprint_06_paso_3.md)
- [Paso 4 · Pipeline y baseline (día 2, 15 minutos)](Reto_Sprint_06_paso_4.md)
- [Paso 5 · Informe, README y revisión con la rúbrica (día 2, 20 minutos)](Reto_Sprint_06_paso_5.md)

#### Ayuda 1 · Cómo usar la IA en este reto

La limpieza de datos es un terreno donde la IA ayuda mucho, pero **donde también introduce errores sutiles**. Reglas:
- **Todo lo que dé, lo ejecutáis y lo entendéis.** Si el docente pregunta por una línea, tenéis que saber explicarla.
- **Solo librerías del curso.** No instaléis paquetes extra que os «arreglen» los datos automáticamente.
- **Toda corrección va en el código**, no en el CSV ni en un clic de Excel.
- **Declaradlo** en el README: qué pedisteis y qué revisasteis.
- **Nada de datos personales ni claves** en una IA (los datos de este reto son sintéticos, pero se coge el hábito).

| Para qué | Ejemplo de petición | Qué comprobáis |
|---|---|---|
| Entender una función de pandas | «Explícame `fillna`, `drop_duplicates` y `to_datetime` con un ejemplo muy pequeño» | Que probáis cada ejemplo y lo entendéis |
| Depurar un error | «Este código da `KeyError: 'precio'`. El DataFrame tiene estas columnas: *[lista]*. ¿Qué puede pasar?» | Que arregláis la causa, no solo el síntoma |
| Revisar la fuga | «Aquí está mi pipeline: *[código]*. ¿Hay alguna operación que use el test para aprender?» | Que entendéis **por qué** hay o no fuga |
| Redactar el informe | «Reescribe esta tabla de defectos de forma más clara» | Que **no cambie cifras ni defectos** |

#### Ayuda 2 · Errores frecuentes (y cómo evitarlos)

| Error | Por qué ocurre | Cómo evitarlo |
|---|---|---|
| Calcular la mediana con **todos** los datos antes de partir | «Total, es solo la mediana» | Partid primero; imputación y escalado se ajustan **solo con *train***, dentro del `Pipeline` |
| Borrar filas «raras» sin avisar | Se quieren datos limpios | Cada fila eliminada se **cuenta y se justifica** en el informe |
| Informe que dice «hay nulos» sin más | Falta el análisis | Para cada defecto: dónde, cuántas filas, causa, tratamiento y razón |
| Un modelo que «acierta mucho» y se celebra | La exactitud engaña si una clase pesa mucho más | Comparadlo con `DummyClassifier` y mirad F1 o ROC-AUC |
| El cuaderno solo funciona con las celdas en cierto orden | Se editaron celdas sueltas | *Reiniciar y ejecutar todo* antes de entregar |
| Convertir las fechas y que salgan nulas o con día y mes cambiados | Hay dos formatos mezclados y se aplica solo uno | Probar cada formato por separado con `errors="coerce"` y comprobar el año mínimo y máximo |
| Usar columnas que delatan la respuesta o que no se conocen al reservar | Parece que ayudan | Preguntad por cada columna: ¿se conoce **al reservar**? |
| Que la limpieza cambie el CSV original o la tabla `crudo` | Se modifica la tabla en lugar de una copia | Empezar la función con `.copy()` y no escribir nunca en `crudo` |

#### Ayuda 3 · Si os atascáis

1. **No encontramos más defectos:** probad `df.describe()`, `df.isna().sum()`, `df.duplicated().sum()` y `df[columna].value_counts()` en cada columna, y revisad las ocho categorías de la tabla del paso 2.
2. **No sabemos si algo es un error o un dato real:** apuntadlo como **pregunta para el cliente** y explicad qué hacéis mientras tanto.
3. **Una función de pandas no hace lo que queremos:** probadla con un ejemplo de 3 filas inventadas, y repasad el cuaderno correspondiente y su [código explicado](../../2_Practica/codigo_explicado/README.md). Después, preguntad al equipo y al docente.
