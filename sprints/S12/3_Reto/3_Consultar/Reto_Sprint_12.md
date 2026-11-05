# Sprint 12 · Reto «Escuchar al cliente»

> **Ficha completa del reto, para consultar.** Para trabajar, [el reto en una página](../1_Trabajar/Reto_Sprint_12_una_pagina.md). Qué se sube y cómo se evalúa: [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md).
>
> - Volver al [README del sprint](../../README.md).
> - Si es vuestro primer reto: [Cómo se trabaja un reto](../../../../material/4.%20Como_se_trabaja_un_reto.md).

## Ficha del reto

### 1 · 🎯 Qué os pide el cliente

**Qué os pide el cliente.** TurisData Canarias recibe cada semana **decenas de reseñas** y **decenas de mensajes** de huéspedes con las mismas preguntas («¿hasta cuándo puedo cancelar?», «¿admiten perros?»). La dirección no puede leerlo todo ni contestar a mano. Os pide **tres cosas**: (1) **saber qué opinan y de qué se quejan** sus clientes (reseñas), (2) **prever la ocupación de la semana que viene** para organizar personal y compras (una *serie temporal*) y (3) **probar un asistente** que conteste con la política del alojamiento **sin inventar nada** (un asistente con *RAG*: primero busca en un documento y después responde citando lo que ha encontrado; si no lo encuentra, dice «No consta…»). Tenéis que demostrar que se puede hacer con datos, con sentido común y con cuidado. Los datos son **sintéticos** (inventados para el curso): decidlo en el informe.

**Cómo se trabaja.** Es un reto largo, de **175 minutos repartidos en los tres días del sprint** (10 de planning, 130 de reto y 35 de entrega y review), y por eso se trabaja **repartido**: cada persona lidera una parte, pero todas entienden todas. No hace falta experiencia previa: en los cuadernos de práctica del sprint ya hicisteis, con ejercicios guiados, casi todas las piezas (serie temporal, sentimiento, buscador con umbral y ataques); aquí las juntáis para el cliente. Todo debe poder ejecutarse **sin internet** y sin claves. El equipo decide hasta dónde llega: 🟢 mínimo, 🟡 estándar o 🔴 extra. El informe visual del Sprint 13 va dentro de la última jornada pero es **otro reto, con su propia ficha**: aquí no se cuenta.

---

### 2 · 🧰 Recursos del reto

| Recurso | Para qué lo usaréis | Dónde está |
|---|---|---|
| **Python y las librerías del curso** (`pandas`, `scikit-learn`, `statsmodels`, `keras`) | Hacer los tres cuadernos del reto | Colab, ya instalado. No hace falta instalar nada |
| **Datos de las reseñas** [`resenas.csv`](../../../../datos/resenas.csv) | 1.500 reseñas **sintéticas** con texto, nota, sentimiento y temas | Botón *Download raw file*, o subidlo al panel izquierdo de Colab |
| **Datos de la ocupación** [`ocupacion_diaria.csv`](../../../../datos/ocupacion_diaria.csv) | Serie diaria 2023–2025 de un alojamiento: ocupación, temperatura, festivo y precio medio | Igual que el anterior |
| **Política y preguntas del asistente**: [`politica_alojamiento.md`](../../../../datos/politica_alojamiento.md) y [`preguntas_referencia.csv`](../../../../datos/preguntas_referencia.csv) | El documento donde busca el asistente y las 20 preguntas de referencia con su respuesta esperada | Igual que el anterior |
| **Cuadernos de práctica del sprint**: [`S12_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/para_casa/S12_03_nlp_clasico.ipynb) (reseñas), [`S12_01`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/para_casa/S12_01_series_temporales.ipynb) y [`S12_02`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/para_casa/S12_02_redes_recurrentes.ipynb) (ocupación), [`S12_06`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/para_casa/S12_06_mini_rag.ipynb) (asistente) | Son el punto de partida: ya traen el método, el código y las pistas | Colab. Su [código explicado](../../2_Practica/codigo_explicado/README.md) está escrito paso a paso |
| **Presentaciones del sprint** | Repasar la idea de cada parte: [S12_01](../../1_Teoria/S12_01_presentacion_Series_temporales.pdf) y [S12_02](../../1_Teoria/S12_02_presentacion_RNN_LSTM_y_GRU.pdf) (series), [S12_03](../../1_Teoria/S12_03_presentacion_NLP_clasico.pdf) (texto) y [S12_05](../../1_Teoria/S12_05_presentacion_Transformers_y_atencion.pdf) y [S12_06](../../1_Teoria/S12_06_presentacion_Mini_RAG.pdf) (Transformers y RAG) | En la carpeta `1_Teoria` del sprint |
| **Plantilla del informe** [`plantilla_informe_cliente.md`](../1_Trabajar/plantillas/plantilla_informe_cliente.md) | Dar forma al informe de reseñas para la dirección | Copiad el texto con el botón *Raw* |
| **Cómo entregar en GitHub** | Subir los ficheros a `sprint-12/` | [Guía de entrega](../../../../material/5.%20Como_entregar_en_GitHub.md) |
| **Autoevaluación y coevaluación** | Cada persona rellena su hoja | [Hoja del sprint](../2_Entregar/autoevaluacion_y_coevaluacion.md) |
| **Un asistente de IA** (opcional) | Entender errores y pedir pistas | Con las reglas de la «Ayuda 1» del paso a paso |
| **Un modelo de lenguaje real** (Ollama o una API, **opcional**) | Probar el asistente con un modelo de verdad | [Acceso a modelos de lenguaje](../../../../material/Acceso_modelos_de_lenguaje.md). Si lo usáis, decid que el docente no ha podido verificarlo y **no escribáis ninguna clave** |

---

### 3 · 🪜 Guía paso a paso

Son cuatro pasos, de **175 minutos en total** entre planning (10), reto (130) y entrega y review (35); el paso 4 incluye la subida a GitHub y el ensayo de la review. Cada uno dice **qué hacéis** (la lista corta), **cómo se hace** con el detalle, **qué deberíais ver** y **cuándo está hecho**. Las ayudas (IA, errores, atascos) están al final. Si el tiempo aprieta, completad el nivel mínimo de las tres partes y dejad lo demás para casa: es mejor entregar las cuatro piezas en versión sencilla que tres perfectas y una vacía.

**Cada paso tiene su propia página.** Abrid la que toque y volved aquí cuando acabéis:

- [Paso 1 · Reparto y plan (día 1, 10 minutos, y día 2, 5 minutos)](Reto_Sprint_12_paso_1.md)
- [Paso 2 · Datos y modelos (día 2, 50 minutos, y día 3, 30 minutos)](Reto_Sprint_12_paso_2.md)
- [Paso 3 · Evaluación y seguridad del asistente (día 3, 40 minutos)](Reto_Sprint_12_paso_3.md)
- [Paso 4 · Cierre, entrega y review (día 3, 40 minutos)](Reto_Sprint_12_paso_4.md)

#### Ayuda 1 · Cómo usar la IA en este reto

Este reto trata **de** asistentes de IA, así que conviene tener muy claras las reglas:
- **Todo lo que dé, lo ejecutáis y lo entendéis.** Si el docente pregunta por una línea o por una cifra, tenéis que saber explicarla.
- **Las cifras del informe salen del código**, no de la IA: una IA puede inventarlas.
- **Ninguna clave en el código ni en el repositorio.** Si usáis un modelo real, la clave se lee de una variable de entorno. Y el modelo real es opcional: si lo usáis, decid que el docente no ha podido verificarlo.
- **Nada de datos personales** en una IA. Los datos del reto son sintéticos, pero practicad el hábito.
- **Contadlo** en la nota de IA responsable: qué pedisteis y qué comprobasteis.

| Para qué | Ejemplo de petición | Qué comprobáis |
|---|---|---|
| Entender conceptos | «Explícame qué es RAG con la analogía de un bibliotecario que primero busca el libro y luego responde» | Que podéis explicarlo al cliente |
| Depurar código | «Este código da un error al trocear el texto: *[código y error]*» | Que entendéis el arreglo |
| Ideas de ataques | «Dame ejemplos de intentos de prompt injection contra un asistente de hotel, solo para probar mi defensa» | Que probáis **vuestros** ataques y medís el resultado |
| Redactar recomendaciones | «Convierte este hallazgo en una recomendación que el director pueda ejecutar el lunes» | Que no inventa cifras |

#### Ayuda 2 · Errores frecuentes (y cómo evitarlos)

| Error | Por qué ocurre | Cómo evitarlo |
|---|---|---|
| Barajar la serie temporal antes de partirla | Es el hábito de otros sprints | Partid **por fecha**: lo antiguo para entrenar, lo último para evaluar |
| Escalar o vectorizar con todos los datos antes de partir | Se hace «para ir más rápido» | Ajustad el escalador y el vectorizador **solo con el entrenamiento**; con la prueba, solo aplicadlos |
| El modelo no mejora al *baseline* y no se dice | Parece un fracaso | Es un resultado válido: explicadlo y proponed quedaros con el método simple |
| El asistente inventa respuestas | No hay umbral | Fijad un umbral y responded «No consta» |
| Respuestas sin fuente | Se olvida citar | La salida debe incluir el número del fragmento |
| Probar solo ataques fáciles | Prisa | Probad al menos 3 tipos distintos y decid qué esquivaría vuestro filtro |
| Informe lleno de gráficos sin recomendaciones | Faltan acciones | 3 recomendaciones que se puedan ejecutar el lunes |
| Subir un cuaderno sin resultados o con una clave | Se descarga sin ejecutar o se pega la clave «para probar» | Ejecutad con *Reiniciar sesión y ejecutar todo* antes de descargar y buscad claves antes de subir |
| Cuatro partes sin integrar | Cada uno va a lo suyo | Una persona coordina y revisa el `LEEME.md` |

#### Ayuda 3 · Si os atascáis

1. **El tiempo se acaba:** priorizad. Entregad las cuatro piezas en versión sencilla y anotad en el `LEEME.md` lo que falta.
2. **El modelo de ocupación no converge:** quedaos con el *baseline* y un modelo estadístico sencillo; explicad el resultado.
3. **No sabéis cómo medir una defensa:** contad, con un conjunto fijo de ataques y de preguntas legítimas, cuántos se bloquean y cuántas pasan.
4. Repasad la sección de ese cuaderno en el paso 2, preguntad al equipo y, después, al docente. Más ayuda: [Cómo se trabaja un reto](../../../../material/4.%20Como_se_trabaja_un_reto.md).
