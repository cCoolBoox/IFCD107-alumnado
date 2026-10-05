# Sprint 5 · Matemáticas y estadística en código

**Pregunta guía:** ¿podemos demostrar con código lo que vimos en teoría?
**Fechas:** 29/10–3/11 · **Horas:** 4 h de teoría (T) · 6 h de práctica (P, incluye 1 h de CRUD desde Python) · 3 h de proyecto (PBL) = 13 h

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_05.pdf`](Guia_Sprint_05.pdf)
- 🖥️ **S05.1 · NumPy y algebra lineal:** [`S05.1_NumPy_y_algebra_lineal.pdf`](presentaciones/S05.1_NumPy_y_algebra_lineal.pdf)
- 🖥️ **S05.2 · Descenso del gradiente y regresion desde cero:** [`S05.2_Descenso_del_gradiente_y_regresion_desde_cero.pdf`](presentaciones/S05.2_Descenso_del_gradiente_y_regresion_desde_cero.pdf)
- 🖥️ **S05.3 · Estadistica con Python y CRUD:** [`S05.3_Estadistica_con_Python_y_CRUD.pdf`](presentaciones/S05.3_Estadistica_con_Python_y_CRUD.pdf)

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

## Prácticas (6 h)
Cada ejercicio se autocorrige con un `assert`: si falla, lee el mensaje, corrige y ejecuta de nuevo. Sigue el orden.

| Cuaderno | Tema | Tiempo | Colab |
|---|---|---|---|
| `S05_01_numpy` | NumPy: arrays, máscaras, vectorización, broadcasting, semillas | 45 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/S05_01_numpy.ipynb) |
| `S05_02_algebra_lineal` | Vectores, matrices, producto matricial, sistemas de ecuaciones, ecuación normal | 45 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/S05_02_algebra_lineal.ipynb) |
| `S05_03_gradiente_regresion` | Derivada, MSE, descenso del gradiente y regresión lineal desde cero | 90 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/S05_03_gradiente_regresion.ipynb) |
| `S05_04_estadistica_descriptiva_ic` | Estadística descriptiva, distribuciones, Monte Carlo e intervalos de confianza | 60 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/S05_04_estadistica_descriptiva_ic.ipynb) |
| `S05_05_contrastes_causalidad` | Contrastes de hipótesis, correlación frente a causalidad, `statsmodels`, Bayes | 60 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/S05_05_contrastes_causalidad.ipynb) |
| `S05_06_crud_python` | CRUD desde Python: `sqlite3`, `pymongo`/`mongomock` (M6b) | 60 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/S05_06_crud_python.ipynb) |

---

## Reto PBL · «¿La ocupación depende de esto?»  (3 h)

### Contexto del cliente
*TurisData Canarias* quiere planificar personal y precios de su alojamiento de referencia. Le han dicho que «cuando hace calor se llena menos» y que «los festivos llenan». Antes de tomar decisiones quiere saber **cuánto** cambia la ocupación diaria con la temperatura y con los festivos, y **con cuánta seguridad** podemos decirlo. Tenéis su serie diaria de tres años (`ocupacion_diaria.csv`).

### Qué tenéis que entregar
Un **cuaderno** (`S05_07_reto_ocupacion`, con la plantilla) y una **base de datos** con:
1. La serie diaria **cargada en una base SQLite** (`turisdata_reto.db`) y leída desde Python con SQL.
2. La **regresión lineal implementada desde cero** con descenso del gradiente (modelo simple y modelo con control de la estacionalidad).
3. La **comparación con una librería** (`statsmodels`).
4. El **análisis estadístico**: contraste, intervalos de confianza y p-valores.
5. Una **respuesta al cliente de máximo 150 palabras**: qué encontráis, qué recomendáis y qué no podéis afirmar.

### Restricciones
- **Tiempo:** 3 h dentro del sprint.
- El descenso del gradiente lo escribís vosotros (sin `LinearRegression` en la implementación; la librería solo sirve para contrastar).
- Datos sintéticos: no generalicéis a otros alojamientos ni al turismo real.
- Semillas fijas y el cuaderno debe ejecutarse de arriba abajo sin errores.

### Criterios de evaluación (rúbrica del curso, 0–4 en cada criterio)
| Criterio | Qué se mirará en este reto |
|---|---|
| **Corrección técnica** | El gradiente converge y coincide con `statsmodels`; los contrastes e intervalos están bien calculados; se controla la estacionalidad. |
| **Reproducibilidad** | Reiniciar y ejecutar todo funciona; se crea o entrega la base; se indican versiones y semilla. |
| **Análisis y comunicación al cliente** | La respuesta se entiende sin ser técnico, incluye cifras con su incertidumbre y una recomendación accionable con límites explicados. |
| **IA responsable** | Se distingue correlación y causalidad, se explican los límites (datos sintéticos, un solo alojamiento) y se propone una cautela concreta sobre el uso del modelo. |

### Pasos sugeridos
- **Día 1:** cargad los datos en la base, leedlos con SQL y explorad (gráficos, medias por mes). Implementad el gradiente y el modelo simple.
- **Día 2:** implementad el modelo con control (festivo y mes), contrastad con `statsmodels` y calculad p-valores e intervalos de confianza.
- **Día 3:** redactad la respuesta al cliente, revisad con la rúbrica, reiniciad y ejecutad todo, y preparad la demostración.

### Qué se enseña en la review
Una demostración de 5 minutos: (1) la pregunta y la base de datos, (2) cómo converge vuestro descenso del gradiente y su comparación con la librería, (3) el resultado clave con su intervalo, (4) cómo habéis distinguido lo que los datos muestran de lo que no pueden demostrar (correlación frente a causalidad), (5) la recomendación al cliente.

### Definition of Done
- [ ] Todos los puntos de control (`assert`) del cuaderno pasan.
- [ ] `turisdata_reto.db` existe y contiene la tabla `ocupacion_diaria` con 1096 filas.
- [ ] La regresión desde cero coincide con `statsmodels` (tolerancia razonable) y hay una curva de aprendizaje.
- [ ] Hay al menos un p-valor, un intervalo de confianza y una medida del tamaño del efecto interpretados con palabras.
- [ ] La respuesta al cliente (≤ 150 palabras) incluye recomendación y límites.
- [ ] Gráficos con título y ejes en español.
- [ ] Reiniciar y ejecutar todo funciona sin errores; alguien del grupo ha revisado el trabajo con la rúbrica.

**Plantilla del cuaderno del reto:** [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/S05_07_reto_ocupacion.ipynb)

## Recursos
- Documentación de NumPy (guía para principiantes): <https://numpy.org/doc/stable/user/absolute_beginners.html>
- Documentación de SciPy Stats: <https://docs.scipy.org/doc/scipy/reference/stats.html>
- Documentación de `statsmodels`: <https://www.statsmodels.org/stable/index.html>
- Módulo `sqlite3` de Python: <https://docs.python.org/es/3/library/sqlite3.html>
- Vídeos «Essence of linear algebra» (3Blue1Brown, con subtítulos): <https://www.3blue1brown.com/topics/linear-algebra>
