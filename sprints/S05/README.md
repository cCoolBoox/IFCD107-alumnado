# Sprint 5 · Matemáticas y estadística en código
**Pregunta guía:** ¿podemos demostrar con código lo que vimos en teoría?
**Fechas:** 29/10–3/11 · **Horas:** 13 h (4 h teoría · 6 h práctica, incluye 1 h de CRUD · 3 h proyecto)

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_05.pdf`](Guia_Sprint_05.pdf)
- 🖥️ **S05.1 · NumPy y algebra lineal:** [`S05.1_NumPy_y_algebra_lineal.pdf`](presentaciones/S05.1_NumPy_y_algebra_lineal.pdf)
- 🖥️ **S05.2 · Descenso del gradiente y regresion desde cero:** [`S05.2_Descenso_del_gradiente_y_regresion_desde_cero.pdf`](presentaciones/S05.2_Descenso_del_gradiente_y_regresion_desde_cero.pdf)
- 🖥️ **S05.3 · Estadistica con Python y CRUD:** [`S05.3_Estadistica_con_Python_y_CRUD.pdf`](presentaciones/S05.3_Estadistica_con_Python_y_CRUD.pdf)

## Qué aprenderás
- Datos numéricos con NumPy y álgebra lineal.
- Entrenar una regresión lineal desde cero con descenso del gradiente.
- Estadística con Python: intervalos de confianza, contrastes, p-valores y correlación frente a causalidad.
- CRUD desde Python sobre SQLite y MongoDB. Requisito: Sprint 4; los datos (sintéticos) se descargan solos.

## Prácticas
Cuadernos en orden (6 h). Cada ejercicio se autocorrige con un `assert`: si falla, lee el mensaje y corrige.

| Cuaderno | Tema | Colab |
|---|---|---|
| `S05_01_numpy` | Arrays, vectorización, *broadcasting* | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/S05_01_numpy.ipynb) |
| `S05_02_algebra_lineal` | Matrices, sistemas, ecuación normal | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/S05_02_algebra_lineal.ipynb) |
| `S05_03_gradiente_regresion` | Descenso del gradiente y regresión desde cero | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/S05_03_gradiente_regresion.ipynb) |
| `S05_04_estadistica_descriptiva_ic` | Descriptiva, Monte Carlo, intervalos de confianza | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/S05_04_estadistica_descriptiva_ic.ipynb) |
| `S05_05_contrastes_causalidad` | Contrastes, causalidad, `statsmodels`, Bayes | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/S05_05_contrastes_causalidad.ipynb) |
| `S05_06_crud_python` | CRUD con `sqlite3` y `mongomock` | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/S05_06_crud_python.ipynb) |

## Reto · «¿La ocupación depende de esto?»
**Contexto:** TurisData Canarias quiere saber cuánto cambia la ocupación con la temperatura y los festivos, y con cuánta seguridad. Tenéis su serie diaria de tres años (`ocupacion_diaria.csv`).
**Entregáis** (en la carpeta `sprint-05/` del repositorio del equipo):
- El cuaderno `S05_07_reto_ocupacion` (plantilla: [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/S05_07_reto_ocupacion.ipynb)), ejecutado de arriba abajo.
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
