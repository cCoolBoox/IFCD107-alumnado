# README Sprint S05 · Matemáticas y estadística en código

**Pregunta guía:** ¿podemos demostrar con código lo que vimos en teoría?
**Fechas:** 30/10 y 3/11 · **Horas:** 12 h (3 h teoría · 6 h práctica, incluye 1 h de CRUD · 3 h PBL)

📄 **Este README en PDF:** [a color](README_Sprint_05.pdf) · [ecofriendly, para imprimir](README_Sprint_05_ecofriendly.pdf) (descárgalo para que funcionen los enlaces; la vista previa de GitHub no los abre).

## Qué aprenderás
1. A manejar **datos numéricos con NumPy**: arrays, vectorización, *broadcasting* y álgebra lineal.
2. A **entrenar un modelo desde cero**: entender el gradiente y programar la regresión lineal con descenso del gradiente.
3. A hacer **estadística con Python**: describir datos, usar distribuciones, simular (Monte Carlo) y construir intervalos de confianza.
4. A **contrastar hipótesis** e interpretar p-valores, tamaños de efecto y la diferencia entre **correlación y causalidad**.
5. A hacer **CRUD desde Python** sobre SQLite y MongoDB y a dejar una base de datos poblada.

## Requisitos previos
- Haber hecho el Sprint 4 (Python básico, funciones, ficheros).
- Colab o Jupyter con Python 3.11. Los cuadernos usan `numpy`, `pandas`, `matplotlib`, `scipy`, `statsmodels`, `scikit-learn`, `sqlite3` y `mongomock`.
- Los datos (`ocupacion_diaria.csv`, `reservas_turisdata.csv`, `turisdata.db`) se descargan solos. Son **sintéticos**: sirven para practicar, no son estadísticas reales del turismo canario.

## 📎 Materiales del sprint

**Documentos del curso** (PDF y .md; las actividades van en la tabla siguiente)

| Material | Tema | Tiempo | Cuándo |
|---|---|---|---|
| [Guía del sprint (PDF)](guia/Guia_Sprint_05.pdf) · [ecofriendly](guia/Guia_Sprint_05_ecofriendly.pdf) | Resumen del sprint: qué aprenderás, temario, material, reto y conclusión | 2 páginas | Antes de empezar |
| [Reto completo, paso a paso (.md)](guia/Reto_Sprint_05.md) · [PDF](guia/Reto_Sprint_05.pdf) · [ecofriendly](guia/Reto_Sprint_05_ecofriendly.pdf) | Qué pide el cliente, pasos, rúbrica, ayudas y errores frecuentes | — | Antes del planning y durante el reto |
| [Resumen del sprint en una página](infografias/S05_00_resumen_del_sprint.png) | Lámina con la pregunta guía, qué aprenderás, cómo se reparte el sprint (teoría, práctica y reto) y dónde estás en el curso | — | Antes del planning |
| [Esquema del contenido y su relación con el reto](infografias/S05_07_esquema_contenido_y_reto.png) | Qué presentación prepara cada pieza del entregable, con el material que se reutiliza después | — | Antes del planning y como guía durante el reto |
| [Infografías del reto](infografias/) | 3 láminas ilustradas del reto | — | Reto |
| [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md) | El método de trabajo de todos los retos | — | Antes del primer reto |
| [`S05.1_NumPy_y_algebra_lineal.pdf`](presentaciones/S05.1_NumPy_y_algebra_lineal.pdf) | NumPy y álgebra lineal: vectorización y *broadcasting* | 15 min | Teoría · día 1 del S05 |
| [`S05.2_Descenso_del_gradiente_y_regresion_desde_cero.pdf`](presentaciones/S05.2_Descenso_del_gradiente_y_regresion_desde_cero.pdf) | Descenso del gradiente y regresión desde cero | 20 min | Teoría · día 1 del S05 |
| [`S05.3_Estadistica_con_Python_y_CRUD.pdf`](presentaciones/S05.3_Estadistica_con_Python_y_CRUD.pdf) | Estadística con Python y CRUD | 15 min | Teoría · día 2 del S05 |

**Material de las actividades**

Cuadernos en orden (5 h). Cada ejercicio se autocorrige con un `assert`: si falla, lee el mensaje y corrige.

| Cuaderno | Tema | Colab |
|---|---|---|
| `S05_01_numpy` | Arrays, vectorización, *broadcasting* | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_01_numpy.ipynb) |
| `S05_02_algebra_lineal` | Matrices, sistemas, ecuación normal | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_02_algebra_lineal.ipynb) |
| `S05_03_gradiente_regresion` | Descenso del gradiente y regresión desde cero | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_03_gradiente_regresion.ipynb) |
| `S05_04_estadistica_descriptiva_ic` | Descriptiva, Monte Carlo, intervalos de confianza | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_04_estadistica_descriptiva_ic.ipynb) |
| `S05_05_contrastes_causalidad` | Contrastes, causalidad, `statsmodels`, Bayes | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_05_contrastes_causalidad.ipynb) |
| `S05_06_crud_python` | CRUD con `sqlite3` y `mongomock` | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_06_crud_python.ipynb) |

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

**Día 1 del S05**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 1 | 🔔 Ceremonia | Planning del reto «¿La ocupación depende de esto?» | 10 min |
| 2 | 📖 Teoría | [NumPy y álgebra lineal: vectorización y *broadcasting*](presentaciones/S05.1_NumPy_y_algebra_lineal.pdf) | 15 min |
| 3 | 💻 Práctica | [Arrays, vectorización y *broadcasting*](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_01_numpy.ipynb) | 35 min |
| 4 | 💻 Práctica | [Matrices, sistemas y ecuación normal](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_02_algebra_lineal.ipynb) | 35 min |
| 5 | 📖 Teoría | [Descenso del gradiente y regresión desde cero](presentaciones/S05.2_Descenso_del_gradiente_y_regresion_desde_cero.pdf) | 20 min |
| 6 | 💻 Práctica | [Descenso del gradiente y regresión desde cero](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_03_gradiente_regresion.ipynb) | 1 h 10 min |
| 7 | 💻 Práctica | Terminad los cuadernos pendientes, incluido el apartado «en casa», y poneos al día | 15 min |

**Día 2 del S05**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 8 | 📖 Teoría | [Estadística con Python y CRUD](presentaciones/S05.3_Estadistica_con_Python_y_CRUD.pdf) | 15 min |
| 9 | 💻 Práctica | [Descriptiva, Monte Carlo e intervalos de confianza](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_04_estadistica_descriptiva_ic.ipynb) | 35 min |
| 10 | 💻 Práctica | [Contrastes, causalidad, `statsmodels` y Bayes](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_05_contrastes_causalidad.ipynb) | 35 min |
| 11 | 💻 Práctica | [CRUD con `sqlite3` y `mongomock` (es también el paso 1 del reto: cargar los datos en una base)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_06_crud_python.ipynb) | 30 min |
| 12 | 🎯 Reto | Cuaderno [`S05_07`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_07_reto_ocupacion.ipynb): mirar los datos → regresión desde cero → comparar con una librería → medir la seguridad del resultado → responder en 150 palabras (pasos 2–6) | 45 min |
| 13 | 🔔 Ceremonia | Entrega en `sprint-05/`, autoevaluación y coevaluación, review y retrospectiva | 40 min |

<!--orden:fin-->

## Reto · «¿La ocupación depende de esto?»

📄 [Reto en PDF](guia/Reto_Sprint_05.pdf) · [ecofriendly](guia/Reto_Sprint_05_ecofriendly.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

👉 **[Ver el reto completo, explicado paso a paso](guia/Reto_Sprint_05.md)** (qué se pide, cómo hacerlo, cómo usar la IA, errores frecuentes y autoevaluación).


**Contexto:** TurisData Canarias quiere saber cuánto cambia la ocupación con la temperatura y los festivos, y con cuánta seguridad. Tenéis su serie diaria de tres años (`ocupacion_diaria.csv`).

**Entregáis** (en la carpeta `sprint-05/` del repositorio del equipo):
- El cuaderno `S05_07_reto_ocupacion` (plantilla: [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_07_reto_ocupacion.ipynb)), ejecutado de arriba abajo.
- La base `turisdata_reto.db` con la serie cargada y leída con SQL.
- Regresión desde cero (simple y con estacionalidad), comparada con `statsmodels`.
- Contraste, intervalos de confianza y p-valores, y una respuesta al cliente de máx. 150 palabras.

**Reglas:**
- Unas 2 h 30 min de reto; el descenso del gradiente lo escribís vosotros (la librería solo para contrastar).
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
