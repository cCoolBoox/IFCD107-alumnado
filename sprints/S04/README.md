# README Sprint S04 · Python para IA

**Pregunta guía:** ¿cómo automatizamos lo que hemos hecho a mano?
**Fechas:** 28–29/10 · **Horas:** 12 h (3 h teoría · 5 h práctica · 4 h PBL)

📄 **Este README en PDF:** [a color](README_Sprint_04.pdf) · [ecofriendly, para imprimir](README_Sprint_04_ecofriendly.pdf) (descárgalo para que funcionen los enlaces; la vista previa de GitHub no los abre).

## Qué aprenderás
1. A trabajar en Colab o Jupyter y a escribir Python básico: variables, tipos, decisiones y bucles.
2. A crear **funciones** y **módulos** reutilizables, con documentación y pruebas.
3. A manejar **listas, diccionarios, conjuntos** y comprensiones para representar datos reales.
4. A leer y escribir **CSV y JSON** con la biblioteca estándar y a controlar errores con excepciones.
5. A organizar tu código con clases, buenas prácticas y **Git básico**, y a entregar una herramienta con pruebas.

## Requisitos previos
- Cuenta de Google para usar Colab (o Python 3.11 y Jupyter/VS Code en tu equipo).
- **No hace falta saber programar.** Si vienes de Java, en los cuadernos hay comparativas con Python.
- Los datos (`reservas_turisdata.csv`) los descargan los cuadernos solos; para el reto los tendrás también en el repositorio.
- Recuerda: los datos son **sintéticos** (no son estadísticas reales del turismo canario).

## 📎 Materiales del sprint

**Documentos del curso** (PDF y .md; las actividades van en la tabla siguiente)

| Material | Tema | Tiempo | Cuándo |
|---|---|---|---|
| [Guía del sprint (PDF)](guia/Guia_Sprint_04.pdf) · [ecofriendly](guia/Guia_Sprint_04_ecofriendly.pdf) | Resumen del sprint: qué aprenderás, temario, material, reto y conclusión | 2 páginas | Antes de empezar |
| [Reto completo, paso a paso (.md)](guia/Reto_Sprint_04.md) · [PDF](guia/Reto_Sprint_04.pdf) · [ecofriendly](guia/Reto_Sprint_04_ecofriendly.pdf) | Qué pide el cliente, pasos, rúbrica, ayudas y errores frecuentes | — | Antes del planning y durante el reto |
| [Resumen del sprint en una página](infografias/S04_00_resumen_del_sprint.png) | Lámina con la pregunta del cliente, los pasos, lo que se entrega y lo que se aprende | — | Antes del planning |
| [Esquema del contenido y su relación con el reto](infografias/S04_07_esquema_contenido_y_reto.png) | Qué presentación prepara cada pieza del entregable, con el material que se reutiliza después | — | Antes del planning y como guía durante el reto |
| [Infografías del reto](infografias/) | 4 láminas ilustradas del reto | — | Reto |
| [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md) | El método de trabajo de todos los retos | — | Antes del primer reto |
| [`S04.1_Python_entorno_y_lenguaje.pdf`](presentaciones/S04.1_Python_entorno_y_lenguaje.pdf) | Python: entorno (venv, pip, Jupyter, Git) y lenguaje | 20 min | Teoría · miércoles 28/10 |
| [`S04.2_Python_estructuras_funciones_y_POO.pdf`](presentaciones/S04.2_Python_estructuras_funciones_y_POO.pdf) | Estructuras de datos, funciones, ficheros, excepciones y POO | 20 min | Teoría · jueves 29/10 |

**Material de las actividades**

Cuadernos en orden (3 h 35 min obligatorias + 45 min opcionales). Cada ejercicio se autocorrige: si falla la celda de comprobación, lee el mensaje y corrige. Los datos son sintéticos.

| Cuaderno | Tema | Colab |
|---|---|---|
| `S04_01_entorno_sintaxis` | Entorno, variables, tipos, `if`, `for`, `while` | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/notebooks/S04_01_entorno_sintaxis.ipynb) |
| `S04_02_funciones_modulos` | Funciones, `*args`, `lambda`, módulos | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/notebooks/S04_02_funciones_modulos.ipynb) |
| `S04_03_estructuras_datos` | Listas, tuplas, diccionarios, conjuntos | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/notebooks/S04_03_estructuras_datos.ipynb) |
| `S04_04_ficheros_excepciones` | CSV y JSON, `try`/`except` | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/notebooks/S04_04_ficheros_excepciones.ipynb) |
| `S04_05_poo_buenas_practicas` | **(OPCIONAL)** Clases, buenas prácticas, Git básico | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/notebooks/S04_05_poo_buenas_practicas.ipynb) |

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

**Miércoles 28/10**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 1 | 🔔 Ceremonia | Planning del reto «Herramientas internas» | 10 min |
| 2 | 📖 Teoría | [Python: entorno (venv, pip, Jupyter, Git) y lenguaje](presentaciones/S04.1_Python_entorno_y_lenguaje.pdf) | 20 min |
| 3 | 💻 Práctica | [Entorno, variables, tipos, `if`, `for` y `while`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/notebooks/S04_01_entorno_sintaxis.ipynb) | 45 min |
| 4 | 💻 Práctica | [Funciones, `*args`, `lambda` y módulos](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/notebooks/S04_02_funciones_modulos.ipynb) | 45 min |
| 5 | 💻 Práctica | [Listas, tuplas, diccionarios y conjuntos](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/notebooks/S04_03_estructuras_datos.ipynb) | 45 min |
| 6 | 💻 Práctica | [CSV, JSON y `try`/`except` (prepara `leer_reservas`)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/notebooks/S04_04_ficheros_excepciones.ipynb) | 35 min |

**Jueves 29/10**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 7 | 📖 Teoría | [Estructuras de datos, funciones, ficheros, excepciones y POO](presentaciones/S04.2_Python_estructuras_funciones_y_POO.pdf) | 20 min |
| 8 | 💻 Práctica | Terminad los cuadernos pendientes, incluido el apartado «en casa», y poneos al día | 10 min |
| 9 | 🎯 Reto | [Preparar la carpeta y ver que las pruebas fallan → rellenar las funciones una a una → exportar y ejecutar el programa → probar que no se rompe → README y Git (pasos 1–5)](guia/Reto_Sprint_04.md) | 2 h 10 min |
| 10 | 🔔 Ceremonia | Entrega en `sprint-04/`, autoevaluación y coevaluación, review y retrospectiva | 40 min |

<!--orden:fin-->

## Reto · «Herramientas internas»

📄 [Reto en PDF](guia/Reto_Sprint_04.pdf) · [ecofriendly](guia/Reto_Sprint_04_ecofriendly.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

👉 **[Ver el reto completo, explicado paso a paso](guia/Reto_Sprint_04.md)** (qué se pide, cómo hacerlo, cómo usar la IA, errores frecuentes y autoevaluación).


**Contexto:** el equipo de reservas de TurisData Canarias calcula sus cifras a mano cada semana. Os pide un script que lea el CSV de reservas, calcule tres KPIs, avise si el fichero está mal y deje un JSON.

**Entregáis** (en la carpeta `sprint-04/` del repositorio del equipo; base en [`reto_herramientas/`](recursos/reto_herramientas/)):
- `kpis.py` (funciones + `main`) y `test_kpis.py` (pruebas con `assert`).
- `README.md` con cómo ejecutar, cómo probar y definición de cada KPI (plantilla: [`README_PLANTILLA.md`](recursos/reto_herramientas/README_PLANTILLA.md)).
- `salida.json` generado con el CSV real; opcional: `kpis_pandas.py`.

**Reglas:**
- Unas 3 h 35 min de reto; solo biblioteca estándar (pandas solo en la parte opcional).
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
