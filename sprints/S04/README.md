# README Sprint S04 · Python para IA

**Pregunta guía:** ¿cómo automatizamos lo que hemos hecho a mano?
**Fechas:** 3–4 de noviembre · **Horas:** 9 h (2 h teoría · 4 h práctica · 3 h PBL)

📄 **Este README en PDF:** [a color](README_Sprint_04.pdf) · [ecofriendly, para imprimir](README_Sprint_04_ecofriendly.pdf) (descárgalo para que funcionen los enlaces; la vista previa de GitHub no los abre).

## 🚀 Empieza aquí

👉 **[Tu sprint, día a día](Tu_sprint_dia_a_dia.md)** · [PDF](Tu_sprint_dia_a_dia.pdf) · [ecofriendly](Tu_sprint_dia_a_dia_ecofriendly.pdf)

Una hoja con los días del sprint, en orden, y lo que abres en cada momento. Con ella puedes trabajar todo el sprint; el resto de este README es para consultar.

## Qué aprenderás
1. Escribir **Python** básico en Colab (variables, decisiones, bucles) y crear **funciones y módulos** con pruebas.
2. Representar datos con **listas, diccionarios y conjuntos**, y leer y escribir **CSV y JSON** controlando los errores.
3. Entregar una herramienta con **pruebas y Git**: es lo que haréis en el reto «Herramientas internas».

## Requisitos previos
- Cuenta de Google para usar Colab (o Python 3.11 y Jupyter/VS Code en tu equipo).
- **No hace falta saber programar.** Si vienes de Java, en los cuadernos hay comparativas con Python.
- Los datos (`reservas_turisdata.csv`) los descargan los cuadernos solos; para el reto los tendrás también en el repositorio.
- Recuerda: los datos son **sintéticos** (no son estadísticas reales del turismo canario).

## 📎 Materiales del sprint

### 1 · Hoy en clase

| Material | Para qué | Cuándo |
|---|---|---|
| [**Tu sprint, día a día**](Tu_sprint_dia_a_dia.md) | El orden de trabajo y lo que abres en cada paso | Siempre |
| [S04.1](presentaciones/S04.1_Python_entorno_y_lenguaje.pdf) · [S04.2](presentaciones/S04.2_Python_estructuras_funciones_y_POO.pdf) | Teoría: las diapositivas de cada día | Teoría de cada día |
| [**Reto en una página** (.md)](Reto_S04/Reto_Sprint_04_una_pagina.md) · [PDF](Reto_S04/Reto_Sprint_04_una_pagina.pdf) · [ecofriendly](Reto_S04/Reto_Sprint_04_una_pagina_ecofriendly.pdf) | Lo esencial del reto: tres niveles, reparto del tiempo y frases para el informe | Durante el reto |
| [El reto paso a paso](Reto_S04/S04_03_reto_paso_a_paso.png) · [PDF con enlaces](Reto_S04/S04_03_reto_paso_a_paso.pdf) | Los pasos del reto en una lámina, con día y minutos | Durante el reto |

**Cuadernos, en orden** (en clase, los ejercicios marcados «en clase»; el resto, en casa):

| Cuaderno | Tema | Colab |
|---|---|---|
| `S04_01_entorno_sintaxis` | Entorno, variables, tipos, `if`, `for`, `while` | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/notebooks/S04_01_entorno_sintaxis.ipynb) |
| `S04_02_funciones_modulos` | Funciones, `*args`, `lambda`, módulos | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/notebooks/S04_02_funciones_modulos.ipynb) |
| `S04_03_estructuras_datos` | Listas, tuplas, diccionarios, conjuntos | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/notebooks/S04_03_estructuras_datos.ipynb) |
| `S04_04_ficheros_excepciones` | CSV y JSON, `try`/`except` | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/notebooks/S04_04_ficheros_excepciones.ipynb) |
| `S04_05_poo_buenas_practicas` | **(OPCIONAL)** Clases, buenas prácticas, Git básico | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/notebooks/S04_05_poo_buenas_practicas.ipynb) |

### 2 · Cuando te atasques

| Material | Para qué |
|---|---|
| [Reto completo, paso a paso (.md)](Reto_S04/Reto_Sprint_04.md) · [PDF](Reto_S04/Reto_Sprint_04.pdf) · [ecofriendly](Reto_S04/Reto_Sprint_04_ecofriendly.pdf) | La ficha completa del reto: qué pide el cliente, pasos, rúbrica, ayudas y errores frecuentes |
| [**Código explicado de los cuadernos**](codigo_explicado/) | Cada cuaderno explicado por escrito, con glosario y recorrido celda a celda |
| [**Carpeta del reto: `Reto_S04/`**](Reto_S04/) | Plantillas y material de apoyo del reto |
| [`apuntes_python_para_datos.md`](actividades/apuntes_python_para_datos.md) · [PDF](actividades/apuntes_python_para_datos.pdf) · [ecofriendly](actividades/apuntes_python_para_datos_ecofriendly.pdf) | Apuntes que complementan las diapositivas, para repasar en casa |

### 3 · Referencia (no hace falta abrirla el primer día)

- [Guía del sprint (PDF)](guia/Guia_Sprint_04.pdf) · [ecofriendly](guia/Guia_Sprint_04_ecofriendly.pdf): resumen del sprint en 2 páginas.
- [Resumen del sprint en una página](infografias/S04_00_resumen_del_sprint.png): lámina con la pregunta guía y cómo se reparte el sprint.
- [Esquema del contenido y su relación con el reto](infografias/S04_07_esquema_contenido_y_reto.png): qué presentación prepara cada pieza del entregable.
- [Infografías del sprint](infografias/): láminas ilustradas del sprint.
- [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md): el método de trabajo de todos los retos.

<!--orden:ini-->
<!--orden:fin-->

## Reto · «Herramientas internas»

👉 [**Reto en una página** (.md)](Reto_S04/Reto_Sprint_04_una_pagina.md) para trabajar · [Reto completo, paso a paso (.md)](Reto_S04/Reto_Sprint_04.md) para consultar.

**Contexto:** el equipo de reservas de TurisData Canarias calcula sus cifras a mano cada semana. Os pide un script que lea el CSV de reservas, calcule tres KPIs, avise si el fichero está mal y deje un JSON.

**Entregáis** (en la carpeta `sprint-04/` del repositorio del equipo; base en [`reto_herramientas/`](Reto_S04/reto_herramientas/)):
- `kpis.py` (funciones + `main`) y `test_kpis.py` (pruebas con `assert`).
- `README.md` con cómo ejecutar, cómo probar y definición de cada KPI (plantilla: [`README_PLANTILLA.md`](Reto_S04/reto_herramientas/README_PLANTILLA.md)).
- `salida.json` generado con el CSV real; opcional: `kpis_pandas.py`.

## ✅ Antes de cerrar el sprint
- [ ] `python test_kpis.py` pasa todas las pruebas
- [ ] `python kpis.py reservas_turisdata.csv salida.json` genera el JSON con los 3 KPIs y `calidad`
- [ ] Funciones con docstring y README con las definiciones de los KPIs
- [ ] Entregable subido a la carpeta `sprint-04/` del repositorio del equipo (al menos 3 *commits*)
- [ ] Alguien del grupo ha revisado el código con la rúbrica
- [ ] [Autoevaluación y coevaluación](Reto_S04/autoevaluacion_y_coevaluacion.md) rellenadas
