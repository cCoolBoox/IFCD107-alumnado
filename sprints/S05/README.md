# README Sprint S05 · Matemáticas y estadística en código

**Pregunta guía:** ¿podemos demostrar con código lo que vimos en teoría?  
**Fechas:** 4–5 de noviembre · **Horas:** 9 h (2 h teoría · 4 h práctica, incluye 1 h de CRUD · 3 h PBL)

📄 **Este README en PDF** (para imprimir; descárgalo para que funcionen los enlaces): [a color](pdf/README_Sprint_05.pdf) · [ecofriendly](pdf/README_Sprint_05_ecofriendly.pdf)

> **Sigue el orden de arriba abajo y abre solo lo que pone en cada fila.** Los demás documentos del sprint son para consultar si te atascas (apartado «Si te atascas»). Si el tiempo aprieta, haz solo los ejercicios marcados «en clase»: el resto es para casa.

## Qué aprenderás

1. A manejar **datos numéricos con NumPy**: arrays, vectorización, *broadcasting* y álgebra lineal.
2. A **entrenar un modelo desde cero**: entender el gradiente y programar la regresión lineal con descenso del gradiente.
3. A hacer **estadística con Python**: describir datos, usar distribuciones, simular (Monte Carlo) y construir intervalos de confianza.
4. A **contrastar hipótesis** e interpretar p-valores, tamaños de efecto y la diferencia entre **correlación y causalidad**.
5. A hacer **CRUD desde Python** sobre SQLite y MongoDB y a dejar una base de datos poblada.

## Día 1 · Miércoles 4/11

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 🔔 Ceremonia · Planning del reto «¿La ocupación depende de esto?» | — | 10 |
| ☐ | 📖 Teoría · NumPy y álgebra lineal: vectorización y *broadcasting* | [Presentación S05.1](1_Teoria/S05.1_NumPy_y_algebra_lineal.pdf) | 25 |
| ☐ | 💻 Práctica · Arrays, vectorización y *broadcasting* (los ejercicios marcados «en clase») | [Cuaderno S05_01](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_01_numpy.ipynb) | 30 |
| ☐ | 📖 Teoría · Descenso del gradiente y regresión desde cero | [Presentación S05.2](1_Teoria/S05.2_Descenso_del_gradiente_y_regresion_desde_cero.pdf) | 20 |

**En clase: 1 h 25 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Sé hacer cálculos con arrays sin escribir bucles.
- [ ] Sé qué es el descenso del gradiente.

## Día 2 · Jueves 5/11

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 💻 Práctica · Descenso del gradiente y regresión desde cero (los ejercicios marcados «en clase») | [Cuaderno S05_03](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_03_gradiente_regresion.ipynb) | 40 |
| ☐ | 📖 Teoría · Estadística con Python y CRUD | [Presentación S05.3](1_Teoria/S05.3_Estadistica_con_Python_y_CRUD.pdf) | 20 |
| ☐ | 💻 Práctica · Descriptiva, Monte Carlo e intervalos de confianza (los ejercicios marcados «en clase») | [Cuaderno S05_04](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_04_estadistica_descriptiva_ic.ipynb) | 30 |
| ☐ | 💻 Práctica · CRUD con `sqlite3` y `mongomock` (es también el paso 1 del reto: cargar los datos en una base) | [Cuaderno S05_06](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_06_crud_python.ipynb) | 25 |
| ☐ | 🎯 Reto · Cuaderno `S05_07`: mirar los datos → regresión desde cero → comparar con una librería → medir la seguridad del resultado → responder en 150 palabras (pasos 2–6; lo que falte, en la consolidación y la 6.ª hora) | [Reto en una página](3_Reto/1_Reto_en_una_pagina/Reto_Sprint_05_una_pagina.md) | 45 |
| ☐ | 🔔 Ceremonia · Entrega en `sprint-05/`, autoevaluación y coevaluación, y review y retrospectiva de los Sprints 4 y 5 | — | 40 |

**En clase: 3 h 20 min.**

## El reto en pocas palabras

**Qué os pide el cliente.** Al dueño de TurisData le han dicho dos cosas: *«cuando hace calor se llena menos»* y *«los festivos llenan»*. Antes de cambiar personal y precios, quiere saber **cuánto** cambia realmente la ocupación diaria con la temperatura y con los festivos, y **con qué seguridad** se puede afirmar. Os da tres años de datos diarios.

**Qué vais a entregar:** un cuaderno, una base de datos y la respuesta al cliente.

**Núcleo y extra.** Núcleo: la regresión desde cero y la respuesta al cliente con su medida de confianza. Extra: la comparación con una librería y el CRUD ampliado.

Para trabajar: [reto en una página](3_Reto/1_Reto_en_una_pagina/Reto_Sprint_05_una_pagina.md). Para consultar: [ficha completa del reto](3_Reto/2_Ficha_completa/Reto_Sprint_05.md) (pasos, rúbrica, ayudas y errores frecuentes). Plantillas, datos y autoevaluación: [`3_Reto/4_Plantillas_y_entrega/`](3_Reto/4_Plantillas_y_entrega/).

## ✅ Antes de cerrar el sprint (Definition of Done)

**Archivos subidos en el repositorio del equipo, carpeta `sprint-05/`** (marca cada uno cuando lo veas en GitHub):
- [ ] `S05_07_reto_ocupacion.ipynb` · lo modificáis
- [ ] `turisdata_reto.db` · lo genera el cuaderno
- [ ] `autoevaluacion_nombre.md` · **uno por persona** (la coevaluación va dentro del mismo fichero): [plantilla](3_Reto/4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md)

**Total en `sprint-05/`: 2 ficheros del equipo + 1 hoja por persona** (un equipo de 3 sube 5). Aparte: ocupacion_diaria.csv en `data/` si aún no está; los extras solo si los hacéis. La *review* y la *retro* no se suben.

**Comprobaciones antes de dar el sprint por cerrado:**
- [ ] Todos los `assert` del cuaderno pasan y reiniciar y ejecutar todo funciona
- [ ] `turisdata_reto.db` con la tabla `ocupacion_diaria` (1096 filas)
- [ ] Regresión coincide con `statsmodels`; hay p-valor, intervalo y tamaño del efecto interpretados
- [ ] Respuesta al cliente (≤ 150 palabras) con recomendación y límites
- [ ] Alguien que **no escribió esa parte** ha revisado el entregable con la [rúbrica](3_Reto/2_Ficha_completa/Reto_Sprint_05.md#rúbrica-del-reto--cómo-se-puntúa-y-cómo-se-revisa) y lo ha anotado en el propio entregable

## En casa (cuando puedas)

- Los ejercicios de cada cuaderno que **no** se hacen en clase. Se autocorrigen, y debajo llevan una «Solución de referencia» plegada por si te quedas atascado.
- Cuaderno completo en casa: [`S05_02_algebra_lineal`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_02_algebra_lineal.ipynb)
- Cuaderno completo en casa: [`S05_05_contrastes_causalidad`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_05_contrastes_causalidad.ipynb)
- Si quieres repasar la teoría con calma: [apuntes del sprint](1_Teoria/apuntes/apuntes_numpy_gradiente_y_estadistica.md).

## Si te atascas

1. Lee primero la parte «Si os atascáis» de la [ficha completa del reto](3_Reto/2_Ficha_completa/Reto_Sprint_05.md).
2. Mira el [código explicado](2_Practica/codigo_explicado/README.md) del cuaderno en el que estás.
3. Pregunta a tu equipo y, después, al docente. Si usas IA, cuenta en el README qué te dijo y qué comprobaste.

## Todo el material, por carpetas

Las carpetas están **numeradas en el orden en que las usas**. Cada documento está en `.md`; sus PDF (color y ecofriendly) están en la subcarpeta `pdf/`.

| Carpeta | Qué hay |
|---|---|
| [`1_Teoria/`](1_Teoria/) | Las presentaciones del sprint y los apuntes para repasar |
| [`2_Practica/`](2_Practica/) | Los cuadernos (Colab) y su explicación línea a línea en `codigo_explicado/` |
| [`3_Reto/`](3_Reto/) | `1_Reto_en_una_pagina` · `2_Ficha_completa` · `3_Laminas` · `4_Plantillas_y_entrega` |
| [`4_Referencia/`](4_Referencia/) | Infografías del sprint |

Cómo se trabaja un reto, en todos los sprints: [método de trabajo](../../material/4.%20Como_se_trabaja_un_reto.md).

## Temario oficial de este sprint

| Unidad | Conceptos que entran |
|---|---|
| UD 1b.5 · NumPy | Arrays, indexación, vectorización, broadcasting; álgebra lineal (dot, matmul, inversa, autovalores) |
| UD 1b.6 · Implementación de conceptos matemáticos | Derivadas numéricas, función de coste, descenso del gradiente y regresión lineal desde cero |
| UD 1b.7 · Estadística con Python | Estadística descriptiva con pandas; distribuciones con SciPy; simulación Monte Carlo · Bayes en código, correlación, contraste de hipótesis (t-test), intervalos de confianza |
| M6b · CRUD desde Python | sqlite3/SQLAlchemy y pandas.to_sql para cargar un dataset y consultarlo; pymongo (demostración) |

**Y ahora:** Sprint 6 · Datos listos para modelar (viernes 6/11).

*9 h (2 h teoría · 4 h práctica · 3 h PBL).*
