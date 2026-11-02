# README Sprint S02 · Las matemáticas y la estadística detrás

**Pregunta guía:** ¿en qué se apoyan los modelos y cuándo no debemos fiarnos de un dato?  
**Fechas:** jue 22/10 – vie 23/10 · **Horas:** 12 h (5 h teoría · 4 h práctica · 3 h PBL)

📄 **Para imprimir:** todos los documentos del sprint en PDF, a color y ecofriendly, están juntos en la carpeta [`pdf/`](pdf/) (descárgalos para que funcionen los enlaces).

> **Sigue el orden de arriba abajo y abre solo lo que pone en cada fila.** Los demás documentos del sprint son para consultar si te atascas (apartado «Si te atascas»). Si el tiempo aprieta, haz solo lo que pone en las filas de cada día: lo demás es para casa.

## Qué aprenderás

1. Operar con **vectores y matrices** y entender qué hace un modelo cuando "multiplica" datos por pesos.
2. Interpretar una **derivada**, un **gradiente** y el **descenso del gradiente** como la forma en que un modelo mejora poco a poco.
3. Resumir datos con **media, mediana, desviación típica y cuartiles**, y calcular **probabilidades**, incluida la **probabilidad condicionada** y el teorema de **Bayes**.
4. Detectar **muestras sesgadas**, la **confusión entre correlación y causalidad** y la **paradoja de Simpson**.
5. Conocer el **ecosistema de software** de IA (Python, Colab, librerías, GPU) y tener tus cuentas listas.

## Antes de empezar
Sprint 1 terminado. Matemáticas de secundaria (fracciones, potencias, porcentajes). Una calculadora o el móvil.

## Día 1 · Jueves 22/10

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 🔔 Ceremonia · Planning del reto: leed el informe y repartid las afirmaciones 3 a 6 (paso 1) | — | 10 |
| ☐ | 💻 Práctica · Alta en Colab y primer cuaderno abierto | [alta cuentas](2_Practica/alta_cuentas.md) | 25 |
| ☐ | 📖 Teoría · Herramientas y matemáticas para IA: Python, Colab y GPU; álgebra lineal, derivadas y gradiente | [Presentación S02_01](1_Teoria/S02_01_presentacion_Herramientas_y_matematicas_para_IA.pdf) | 50 |
| ☐ | 💻 Práctica · Ejercicios de matemáticas (hoja 1) con Desmos o GeoGebra | [ejercicios algebra calculo](2_Practica/ejercicios_algebra_calculo.md) | 55 |
| ☐ | 🎯 Reto · Cartas de error, afirmaciones 1 y 2 guiadas y la vuestra (pasos 2 a 4) | [Reto en una página](3_Reto/1_Trabajar/Reto_Sprint_02_una_pagina.md) | 60 |

**En clase: 3 h 20 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Sé abrir un cuaderno en Colab y ejecutar una celda.
- [ ] Sé qué indica la derivada y para qué sirve el gradiente.
- [ ] Mi equipo ha repartido las afirmaciones 3 a 6 del informe.

## Día 2 · Viernes 23/10

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 📖 Teoría · Estadística y probabilidad: descriptiva, Bayes, correlación y paradoja de Simpson | [Presentación S02_02](1_Teoria/S02_02_presentacion_Estadistica_y_probabilidad.pdf) | 35 |
| ☐ | 💻 Práctica · Estadísticas engañosas (4 de los 9 casos en clase). **Para casa:** el resto y la hoja 2 de ejercicios de estadística | [Estadísticas engañosas](2_Practica/estadisticas_enganosas.md) | 45 |
| ☐ | 📝 Test · **Test corto de M1a** (matemáticas y estadística), solo se abre hoy | [Abrir](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S02/tests/test_M1a.html) | 25 |
| ☐ | 🎯 Reto · Dictamen, frase de IA responsable y revisión cruzada (paso 5) | [Reto en una página](3_Reto/1_Trabajar/Reto_Sprint_02_una_pagina.md) | 55 |
| ☐ | 🔔 Ceremonia · Entrega en `sprint-02/`, autoevaluación y coevaluación, review y retrospectiva | — | 40 |

**En clase: 3 h 20 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Sé auditar un informe con números: reconocer el fallo de cada frase y emitir un dictamen razonado.
- [ ] Sé calcular e interpretar una media, una tasa y una probabilidad condicionada.
- [ ] Mi equipo ha entregado en `sprint-02/` y he hecho la autoevaluación y la coevaluación.

## El reto en pocas palabras

**Qué os pide el cliente.** La dirección de TurisData ha escrito un borrador de informe con **seis afirmaciones** sobre cancelaciones y lo va a presentar al consejo. Os pide que lo reviséis como una persona auditora (revisar el trabajo de otra persona y dar vuestra opinión razonada en un **dictamen**): *«Decidme si nos podemos fiar de cada frase; y si no, cómo debería decirse»*. La afirmación 2 decide a qué canal de venta dar prioridad.

**Qué vais a entregar:** un dictamen de auditoría (`dictamen.md`) con al menos cuatro afirmaciones (la 1, la 2 y dos más), la recomendación sobre el canal y una frase de IA responsable; las respuestas del mínimo básico de las dos hojas de ejercicios (`ejercicios.md`); y la autoevaluación y coevaluación de cada persona. La lista con las comprobaciones está más abajo, en «Antes de cerrar el sprint».

**Núcleo y extra.** Núcleo: las afirmaciones 1 y 2 (guiadas) y dos más de la 3 a la 6, con la recomendación y el dictamen. Extra: las otras dos afirmaciones, la hoja de cálculo adjunta y los ejercicios que sobren.

Para trabajar: [reto en una página](3_Reto/1_Trabajar/Reto_Sprint_02_una_pagina.md). Para entregar: [qué se sube y rúbrica](3_Reto/2_Entregar/entrega_y_rubrica.md). Para consultar: [ficha del reto](3_Reto/3_Consultar/Reto_Sprint_02.md) (qué pide el cliente, ayudas y errores frecuentes) y [cada paso explicado](3_Reto/3_Consultar/).

## ✅ Antes de cerrar el sprint (Definition of Done)

**Archivos subidos en el repositorio del equipo, carpeta `sprint-02/`** (marca cada uno cuando lo veas en GitHub):
- [ ] `dictamen.md` · lo creáis a partir de una plantilla
- [ ] `ejercicios.md` · lo creáis
- [ ] `autoevaluacion_nombre.md` · **uno por persona** (la coevaluación va dentro del mismo fichero): [plantilla](3_Reto/2_Entregar/autoevaluacion_y_coevaluacion.md)

**Total en `sprint-02/`: 2 ficheros del equipo + 1 hoja por persona** (un equipo de 3 sube 5). Aparte: hoja_calculo.xlsx; los extras solo si los hacéis. La *review* y la *retro* no se suben.

**Comprobaciones antes de dar el sprint por cerrado:**
- [ ] Test de conocimientos hecho el vie 23/10
- [ ] Dictamen con al menos 4 afirmaciones (la 1, la 2 y dos más), cada una con su carta y su veredicto
- [ ] Cálculos rehechos (1 y 2) y recomendación de tres líneas sobre el canal
- [ ] Hoja de ejercicios con el mínimo básico (M1, M2, M7, E1, E2, E6, E8, E10)
- [ ] Alta en Colab y GitHub hecha (jueves 22/10)
- [ ] Alguien que **no escribió esa parte** ha revisado el entregable con la [rúbrica](3_Reto/2_Entregar/entrega_y_rubrica.md) y lo ha anotado en el propio entregable

## En casa (cuando puedas)

- Los ejercicios de cada cuaderno que **no** se hacen en clase. Se autocorrigen, y debajo llevan una «Solución de referencia» plegada por si te quedas atascado.
- Si quieres repasar la teoría con calma: [apuntes del sprint](1_Teoria/apuntes/apuntes_matematicas_y_estadistica.md).

## Si te atascas

1. Lee primero la parte «Si os atascáis» de la [ficha completa del reto](3_Reto/3_Consultar/Reto_Sprint_02.md).
2. Pregunta a tu equipo y, después, al docente. Si usas IA, cuenta en el README qué te dijo y qué comprobaste.

## Todo el material, por carpetas

Las carpetas están **numeradas en el orden en que las usas**. Cada documento está en `.md`.

| Carpeta | Qué hay |
|---|---|
| [`1_Teoria/`](1_Teoria/) | Las presentaciones del sprint y los apuntes para repasar |
| [`2_Practica/`](2_Practica/) | Las actividades del sprint: dinámicas, hojas de ejercicios, guías y scripts |
| [`3_Reto/`](3_Reto/) | `1_Trabajar` (reto en una página, plantillas y datos) · `2_Entregar` (qué se sube, rúbrica y autoevaluación) · `3_Consultar` (ficha del reto y cada paso explicado) |
| [`4_Referencia/`](4_Referencia/) | Infografías del sprint |

Cómo se trabaja un reto, en todos los sprints: [método de trabajo](../../material/4.%20Como_se_trabaja_un_reto.md).

## Temario oficial de este sprint

| Unidad | Conceptos que entran |
|---|---|
| UD 1a.4 · Fundamentos matemáticos | Álgebra lineal: vectores, matrices, producto escalar y matricial, transpuesta, inversa; idea de autovalores · Cálculo: función, derivada, derivada parcial, gradiente, regla de la cadena · Optimización: función de coste y descenso del gradiente (intuición geométrica) |
| UD 1a.5 · Fundamentos estadísticos | Estadística descriptiva: media, mediana, varianza, desviación típica, cuartiles · Probabilidad, probabilidad condicionada y teorema de Bayes · Distribuciones (normal, binomial, uniforme), muestreo y sesgo de muestreo · Correlación frente a causalidad; nociones de inferencia (intervalos, contraste de hipótesis) |
| UD 1a.6 · Ecosistema de software para IA | Python, Jupyter, Colab; librerías (NumPy, pandas, scikit-learn), frameworks (TensorFlow/Keras, PyTorch), Hugging Face · Hardware: CPU, GPU, TPU; local vs nube; costes |

**Y ahora:** Sprint 3 · Del dato al modelo en la nube (lunes 26/10).

*12 h (5 h teoría · 4 h práctica · 3 h PBL).*
