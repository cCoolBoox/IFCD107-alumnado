# Sprint 5 · Matemáticas y estadística en código
**Pregunta guía:** ¿podemos demostrar con código lo que vimos en teoría?
**Fechas:** 29/10–3/11 · **Horas:** 13 h (4 h teoría · 6 h práctica, incluye 1 h de CRUD · 3 h proyecto)

> 🎯 **Reto de este sprint: «¿La ocupación depende de esto?».** 👉 [**Ver el reto completo, explicado paso a paso**](guia/Reto_Sprint_05.md) · [Reto en PDF](guia/Reto_Sprint_05.pdf) ([ecofriendly](guia/Reto_Sprint_05_ecofriendly.pdf)) · [PDF de la guía](guia/Guia_Sprint_05.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

📄 **Este README en PDF:** [a color](README_Sprint_05.pdf) · [ecofriendly, para imprimir](README_Sprint_05_ecofriendly.pdf) (descárgalo para que funcionen los enlaces; la vista previa de GitHub no los abre).

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_05.pdf`](guia/Guia_Sprint_05.pdf) · [versión ecofriendly para imprimir](guia/Guia_Sprint_05_ecofriendly.pdf)
- 🎯 **Reto completo, paso a paso:** [`Reto_Sprint_05.md`](guia/Reto_Sprint_05.md)
- 🖥️ **S05.1 · NumPy y algebra lineal:** [`S05.1_NumPy_y_algebra_lineal.pdf`](presentaciones/S05.1_NumPy_y_algebra_lineal.pdf)
- 🖥️ **S05.2 · Descenso del gradiente y regresion desde cero:** [`S05.2_Descenso_del_gradiente_y_regresion_desde_cero.pdf`](presentaciones/S05.2_Descenso_del_gradiente_y_regresion_desde_cero.pdf)
- 🖥️ **S05.3 · Estadistica con Python y CRUD:** [`S05.3_Estadistica_con_Python_y_CRUD.pdf`](presentaciones/S05.3_Estadistica_con_Python_y_CRUD.pdf)

**📁 En esta carpeta:** [`guia/`](guia/) PDF de la guía (normal y para imprimir) y el reto explicado paso a paso · [`presentaciones/`](presentaciones/) diapositivas de cada sesión · [`notebooks/`](notebooks/) prácticas para abrir en Colab

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

📖 teoría (diapositivas) · 💻 práctica (cuaderno de Colab o actividad) · 🎯 reto en equipo · 🔔 ceremonia de Scrum

**Sesión 1**

1. 📖 **Teoría**: [NumPy y álgebra lineal: vectorización y *broadcasting*](presentaciones/S05.1_NumPy_y_algebra_lineal.pdf) · _1 h 30 min_
2. 💻 **Práctica**: [Arrays, vectorización y *broadcasting*](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_01_numpy.ipynb) · _45 min_
3. 💻 **Práctica**: [Matrices, sistemas y ecuación normal](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_02_algebra_lineal.ipynb) · _45 min_

**Sesión 2**

4. 📖 **Teoría**: [Descenso del gradiente y regresión desde cero](presentaciones/S05.2_Descenso_del_gradiente_y_regresion_desde_cero.pdf) · _1 h 30 min_
5. 💻 **Práctica**: [Descenso del gradiente y regresión desde cero](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_03_gradiente_regresion.ipynb) · _1 h 30 min_

**Sesión 3**

6. 📖 **Teoría**: [Estadística con Python y CRUD](presentaciones/S05.3_Estadistica_con_Python_y_CRUD.pdf) · _1 h_
7. 💻 **Práctica**: [Descriptiva, Monte Carlo e intervalos de confianza](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_04_estadistica_descriptiva_ic.ipynb) · _1 h_
8. 💻 **Práctica**: [Contrastes, causalidad, `statsmodels` y Bayes](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_05_contrastes_causalidad.ipynb) · _1 h_
9. 💻 **Práctica**: [CRUD con `sqlite3` y `mongomock`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_06_crud_python.ipynb) · _1 h_

**Reto «¿La ocupación depende de esto?»**

10. 🎯 **Reto**: [Cuaderno del reto (plantilla de trabajo)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_07_reto_ocupacion.ipynb) · _dentro de las 3 h_
11. 🎯 **Reto**: [Cargar datos en una base → mirar los datos → regresión desde cero → comparar con una librería → medir la seguridad del resultado → responder en 150 palabras (pasos 1–6)](guia/Reto_Sprint_05.md) · _3 h_

<!--orden:fin-->

## Qué aprenderás
- Datos numéricos con NumPy y álgebra lineal.
- Entrenar una regresión lineal desde cero con descenso del gradiente.
- Estadística con Python: intervalos de confianza, contrastes, p-valores y correlación frente a causalidad.
- CRUD desde Python sobre SQLite y MongoDB. Requisito: Sprint 4; los datos (sintéticos) se descargan solos.

## Prácticas
Cuadernos en orden (6 h). Cada ejercicio se autocorrige con un `assert`: si falla, lee el mensaje y corrige.

| Cuaderno | Tema | Colab |
|---|---|---|
| `S05_01_numpy` | Arrays, vectorización, *broadcasting* | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_01_numpy.ipynb) |
| `S05_02_algebra_lineal` | Matrices, sistemas, ecuación normal | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_02_algebra_lineal.ipynb) |
| `S05_03_gradiente_regresion` | Descenso del gradiente y regresión desde cero | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_03_gradiente_regresion.ipynb) |
| `S05_04_estadistica_descriptiva_ic` | Descriptiva, Monte Carlo, intervalos de confianza | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_04_estadistica_descriptiva_ic.ipynb) |
| `S05_05_contrastes_causalidad` | Contrastes, causalidad, `statsmodels`, Bayes | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_05_contrastes_causalidad.ipynb) |
| `S05_06_crud_python` | CRUD con `sqlite3` y `mongomock` | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_06_crud_python.ipynb) |

## Reto · «¿La ocupación depende de esto?»

👉 **[Ver el reto completo, explicado paso a paso](guia/Reto_Sprint_05.md)** (qué se pide, cómo hacerlo, cómo usar la IA, errores frecuentes y autoevaluación).

**Contexto:** TurisData Canarias quiere saber cuánto cambia la ocupación con la temperatura y los festivos, y con cuánta seguridad. Tenéis su serie diaria de tres años (`ocupacion_diaria.csv`).
**Entregáis** (en la carpeta `sprint-05/` del repositorio del equipo):
- El cuaderno `S05_07_reto_ocupacion` (plantilla: [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_07_reto_ocupacion.ipynb)), ejecutado de arriba abajo.
- La base `turisdata_reto.db` con la serie cargada y leída con SQL.
- Regresión desde cero (simple y con estacionalidad), comparada con `statsmodels`.
- Contraste, intervalos de confianza y p-valores, y una respuesta al cliente de máx. 150 palabras.
**Reglas:**
- 3 h de reto; el descenso del gradiente lo escribís vosotros (la librería solo para contrastar).
- Semillas fijas; datos sintéticos, sin generalizar al turismo real.
- Nunca claves ni datos personales.
**Se valora:** corrección técnica, reproducibilidad, comunicación al cliente e IA responsable, más cifras con su incertidumbre y distinguir correlación de causalidad.

## ✅ Antes de cerrar el sprint
- [ ] Todos los `assert` del cuaderno pasan y reiniciar y ejecutar todo funciona
- [ ] `turisdata_reto.db` con la tabla `ocupacion_diaria` (1096 filas)
- [ ] Regresión coincide con `statsmodels`; hay p-valor, intervalo y tamaño del efecto interpretados
- [ ] Respuesta al cliente (≤ 150 palabras) con recomendación y límites
- [ ] Entregable subido a la carpeta `sprint-05/` del repositorio del equipo
- [ ] Autoevaluación y coevaluación rellenadas
