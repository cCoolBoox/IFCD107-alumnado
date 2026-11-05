# README Sprint S05 · Matemáticas y estadística en código

**Pregunta guía:** ¿podemos demostrar con código lo que vimos en teoría?  
**Fechas:** 4–5 de noviembre · **Horas:** 9 h (2 h teoría · 4 h práctica, incluye 1 h de CRUD · 3 h PBL)

📄 **Para imprimir:** todos los documentos del sprint en PDF, a color y ecofriendly, están juntos en la carpeta [`pdf/`](pdf/) (descárgalos para que funcionen los enlaces).

> **Sigue el orden de arriba abajo y abre solo lo que pone en cada fila.** Los demás documentos del sprint son para consultar si te atascas (apartado «Si te atascas»). Los cuadernos **«en clase»** (carpeta `2_Practica/en_clase/`) son la versión corta que se hace en el aula; los completos son para casa.

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
| ☐ | 📖 Teoría · NumPy: arrays, máscaras, vectorización y *broadcasting* | [Presentación S05_01](1_Teoria/S05_01_presentacion_NumPy_calcular_sin_bucles.pdf) | 25 |
| ☐ | 💻 Práctica · Arrays y vectorización (cuaderno «en clase»: ejercicios 1 y 3; lo que falte, en la tutoría) | [Cuaderno S05_01](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/en_clase/S05_01_numpy_en_clase.ipynb) | 15 |
| ☐ | 🏠 **En casa** · Álgebra lineal con NumPy: vectores, matrices y sistemas de ecuaciones (cuaderno completo) | [Cuaderno S05_02](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_02_algebra_lineal.ipynb) · [Presentación S05_02](1_Teoria/S05_02_presentacion_Algebra_lineal_con_NumPy.pdf) | 40 (casa) |

**En clase: 50 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Sé hacer cálculos con arrays sin escribir bucles.

## Día 2 · Jueves 5/11

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 💻 Práctica · Descenso del gradiente y regresión desde cero (cuaderno «en clase»: ejercicios 4 y 5) | [Cuaderno S05_03](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/en_clase/S05_03_gradiente_regresion_en_clase.ipynb) · [Presentación S05_03](1_Teoria/S05_03_presentacion_Descenso_del_gradiente_y_regresion.pdf) | 40 |
| ☐ | 📖 Teoría · Estadística descriptiva, Monte Carlo e intervalos de confianza | [Presentación S05_04](1_Teoria/S05_04_presentacion_Estadistica_descriptiva_Monte_Carlo_e_IC.pdf) | 20 |
| ☐ | 💻 Práctica · Descriptiva e intervalos de confianza (cuaderno «en clase»: ejercicios 1 y 5) | [Cuaderno S05_04](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/en_clase/S05_04_estadistica_descriptiva_ic_en_clase.ipynb) | 30 |
| ☐ | 💻 Práctica · CRUD con `sqlite3` (cuaderno «en clase»: ejercicios 1 y 3; el 3 es también el paso 1 del reto: cargar los datos en una base) | [Cuaderno S05_06](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/en_clase/S05_06_crud_python_en_clase.ipynb) · [Presentación S05_06](1_Teoria/S05_06_presentacion_CRUD_desde_Python.pdf) | 25 |
| ☐ | 🎯 Reto · Cuaderno `S05_07`: mirar los datos → regresión desde cero → comparar con una librería → medir la seguridad del resultado → responder en 150 palabras (pasos 2–6; lo que falte, en la consolidación y la 6.ª hora) | [Reto en una página](3_Reto/1_Trabajar/Reto_Sprint_05_una_pagina.md) | 45 |
| ☐ | 🔔 Ceremonia · Entrega en `sprint-05/`, autoevaluación y coevaluación, y review y retrospectiva de los Sprints 4 y 5 | — | 40 |
| ☐ | 🏠 **En casa** · Contrastes de hipótesis, correlación y causalidad (cuaderno completo) | [Cuaderno S05_05](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_05_contrastes_causalidad.ipynb) · [Presentación S05_05](1_Teoria/S05_05_presentacion_Contrastes_correlacion_y_causalidad.pdf) | 40 (casa) |

**En clase: 3 h 20 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Sé ajustar una regresión con el descenso del gradiente y comprobar que da lo mismo que una librería.
- [ ] Sé medir lo seguro que es un resultado con un intervalo de confianza.
- [ ] Sé cargar datos en una base con `sqlite3` y responder al cliente con una conclusión y sus límites.

## El reto en pocas palabras

**Qué os pide el cliente.** Al dueño de TurisData le han dicho dos cosas: *«cuando hace calor se llena menos»* y *«los festivos llenan»*. Antes de cambiar personal y precios, quiere saber **cuánto** cambia realmente la ocupación diaria con la temperatura y con los festivos, y **con qué seguridad** se puede afirmar. Os da tres años de datos diarios.

**Qué vais a entregar:** un cuaderno, una base de datos y la respuesta al cliente.

**Niveles del reto.** 🟢 Mínimo: la regresión simple desde cero y la respuesta al cliente con una cifra y su intervalo. 🟡 Estándar: el modelo con control (festivo y mes), la comparación con `statsmodels` y el p-valor, el intervalo y el tamaño del efecto explicados con palabras. 🔴 Extra: explicar con el control por mes por qué correlación no es causalidad, comparar varias tasas de aprendizaje y cuidar los gráficos.

Antes de empezar, probad la [demo interactiva](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S05/3_Reto/1_Trabajar/S05_demo_reto.html) (muestra lo que tendréis al final). Para trabajar: [reto en una página](3_Reto/1_Trabajar/Reto_Sprint_05_una_pagina.md). Para entregar: [qué se sube y rúbrica](3_Reto/2_Entregar/entrega_y_rubrica.md). Para consultar: [ficha del reto](3_Reto/3_Consultar/Reto_Sprint_05.md) (qué pide el cliente, ayudas y errores frecuentes) y [cada paso explicado](3_Reto/3_Consultar/).

## ✅ Antes de cerrar el sprint (Definition of Done)

**Archivos subidos en el repositorio del equipo, carpeta `sprint-05/`** (marca cada uno cuando lo veas en GitHub):
- [ ] `S05_07_reto_ocupacion.ipynb` · lo modificáis
- [ ] `turisdata_reto.db` · lo genera el cuaderno
- [ ] `autoevaluacion_nombre.md` · **uno por persona** (la coevaluación va dentro del mismo fichero): [plantilla](3_Reto/2_Entregar/autoevaluacion_y_coevaluacion.md)

**Total en `sprint-05/`: 2 ficheros del equipo + 1 hoja por persona** (un equipo de 3 sube 5). Aparte: ocupacion_diaria.csv en `data/` si aún no está; los extras solo si los hacéis. La *review* y la *retro* no se suben.

**Comprobaciones antes de dar el sprint por cerrado:**
- [ ] Todos los `assert` del cuaderno pasan y reiniciar y ejecutar todo funciona
- [ ] `turisdata_reto.db` con la tabla `ocupacion_diaria` (1096 filas)
- [ ] Regresión coincide con `statsmodels`; hay p-valor, intervalo y tamaño del efecto interpretados
- [ ] Respuesta al cliente (≤ 150 palabras) con recomendación y límites
- [ ] Alguien que **no escribió esa parte** ha revisado el entregable con la [rúbrica](3_Reto/2_Entregar/entrega_y_rubrica.md) y lo ha anotado en el propio entregable

## En casa (cuando puedas)

- Los **cuadernos completos** (🏠 para casa) de los que hiciste en clase la versión corta («en clase»). Traen **todos** los ejercicios, se autocorrigen y llevan una «Solución de referencia» plegada por si te quedas atascado: [`S05_01`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_01_numpy.ipynb) · [`S05_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_03_gradiente_regresion.ipynb) · [`S05_04`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_04_estadistica_descriptiva_ic.ipynb) · [`S05_06`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_06_crud_python.ipynb).
- Si quieres repasar la teoría con calma: [apuntes del sprint](1_Teoria/apuntes/apuntes_numpy_gradiente_y_estadistica.md).

## Si te atascas

1. Lee primero la parte «Si os atascáis» de la [ficha completa del reto](3_Reto/3_Consultar/Reto_Sprint_05.md).
2. Mira el [código explicado](2_Practica/codigo_explicado/README.md) del cuaderno en el que estás.
3. Pregunta a tu equipo y, después, al docente. Si usas IA, cuenta en el README qué te dijo y qué comprobaste.

## Todo el material, por carpetas

Las carpetas están **numeradas en el orden en que las usas**. Cada documento está en `.md`.

| Carpeta | Qué hay |
|---|---|
| [`1_Teoria/`](1_Teoria/) | Las presentaciones del sprint y los apuntes para repasar |
| [`2_Practica/`](2_Practica/) | Los cuadernos (Colab) y su explicación línea a línea en `codigo_explicado/` |
| [`3_Reto/`](3_Reto/) | `1_Trabajar` (reto en una página, plantillas y datos) · `2_Entregar` (qué se sube, rúbrica y autoevaluación) · `3_Consultar` (ficha del reto y cada paso explicado) |
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
