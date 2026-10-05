# Sprint 4 · Python para IA
**Pregunta guía:** ¿cómo automatizamos lo que hemos hecho a mano?
**Fechas:** 27–29/10 · **Horas:** 10 h (3 h teoría · 5 h práctica · 2 h proyecto)

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_04.pdf`](Guia_Sprint_04.pdf)
- 🖥️ **S04.1 · Python entorno y lenguaje:** [`S04.1_Python_entorno_y_lenguaje.pdf`](presentaciones/S04.1_Python_entorno_y_lenguaje.pdf)
- 🖥️ **S04.2 · Python estructuras funciones y POO:** [`S04.2_Python_estructuras_funciones_y_POO.pdf`](presentaciones/S04.2_Python_estructuras_funciones_y_POO.pdf)

## Qué aprenderás
- Python básico en Colab: variables, decisiones y bucles. No hace falta saber programar (necesitas cuenta de Google).
- Funciones, módulos y estructuras de datos (listas, diccionarios, conjuntos).
- Leer y escribir CSV y JSON y controlar errores con excepciones.
- Entregar una herramienta con pruebas y un README claro.

## Prácticas
Cuadernos en orden (4 h obligatorias + 1 h opcional). Cada ejercicio se autocorrige: si falla la celda de comprobación, lee el mensaje y corrige. Los datos son sintéticos.

| Cuaderno | Tema | Colab |
|---|---|---|
| `S04_01_entorno_sintaxis` | Entorno, variables, tipos, `if`, `for`, `while` | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/S04_01_entorno_sintaxis.ipynb) |
| `S04_02_funciones_modulos` | Funciones, `*args`, `lambda`, módulos | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/S04_02_funciones_modulos.ipynb) |
| `S04_03_estructuras_datos` | Listas, tuplas, diccionarios, conjuntos | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/S04_03_estructuras_datos.ipynb) |
| `S04_04_ficheros_excepciones` | CSV y JSON, `try`/`except` | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/S04_04_ficheros_excepciones.ipynb) |
| `S04_05_poo_buenas_practicas` | **(OPCIONAL)** Clases, buenas prácticas, Git básico | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/S04_05_poo_buenas_practicas.ipynb) |

## Reto · «Herramientas internas»
**Contexto:** el equipo de reservas de TurisData Canarias calcula sus cifras a mano cada semana. Os pide un script que lea el CSV de reservas, calcule tres KPIs, avise si el fichero está mal y deje un JSON.
**Entregáis** (en la carpeta `sprint-04/` del repositorio del equipo; base en [`reto_herramientas/`](reto_herramientas/)):
- `kpis.py` (funciones + `main`) y `test_kpis.py` (pruebas con `assert`).
- `README.md` con cómo ejecutar, cómo probar y definición de cada KPI (plantilla: [`README_PLANTILLA.md`](reto_herramientas/README_PLANTILLA.md)).
- `salida.json` generado con el CSV real; opcional: `kpis_pandas.py`.
**Reglas:**
- 2 h de reto; solo biblioteca estándar (pandas solo en la parte opcional).
- El script no se rompe con fichero inexistente, columnas que faltan o filas defectuosas: informa.
- Nunca claves ni datos personales en el repositorio.
**Se valora:** corrección técnica (pruebas en verde), reproducibilidad, comunicación al cliente (KPIs definidos, ocupación solo como proxy) e IA responsable (qué hizo la IA y qué revisasteis).

## ✅ Antes de cerrar el sprint
- [ ] `python test_kpis.py` pasa todas las pruebas
- [ ] `python kpis.py reservas_turisdata.csv salida.json` genera el JSON con los 3 KPIs y `calidad`
- [ ] Funciones con docstring y README con las definiciones de los KPIs
- [ ] Entregable subido a la carpeta `sprint-04/` del repositorio del equipo (al menos 3 *commits*)
- [ ] Alguien del grupo ha revisado el código con la rúbrica
- [ ] Autoevaluación y coevaluación rellenadas
