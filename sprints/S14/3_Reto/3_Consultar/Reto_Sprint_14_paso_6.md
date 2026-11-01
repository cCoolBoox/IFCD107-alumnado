# Paso 6 · Backlog, plan ético y repositorio (día 3, 140 minutos)

<!--nav-->
> Sprint 14 · Reto «Proyecto final: definir, tener datos y un punto de partida» · paso 6 de 7 · [Ficha del reto](Reto_Sprint_14.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_14_una_pagina.md) · [Paso 7 →](Reto_Sprint_14_paso_7.md)
<!--/nav-->

1. Hacer el backlog de 10 a 15 historias y fijar el objetivo de cada sprint.
2. Rellenar el plan ético con al menos 5 riesgos específicos.
3. Montar el repositorio: README, `requirements.txt` y *commits* de todas las personas.

**En sencillo.** Hoy se escribe, no se programa (salvo cuatro líneas para sacar las versiones). Son tres documentos de organización. El **backlog** es la lista de tareas del proyecto, ordenada, como la lista de la compra antes de ir al súper. El **plan ético** es una revisión honesta de qué puede salir mal y a quién perjudica. El **repositorio** es la carpeta de GitHub que otra persona debería poder abrir y, con el README, repetir vuestro trabajo. Repartid el día: **cada parte la lidera una persona distinta y otra la revisa**.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Backlog** | La lista ordenada de todo lo que hay que hacer en el proyecto. |
| **Historia de usuario** | Una tarea escrita como «**Como** [rol] **quiero** [qué] **para** [beneficio]». |
| **Criterio de aceptación** | Cómo se comprueba que una historia está terminada. |
| **Tamaño (S, M o L)** | Una estimación: pequeña, mediana o grande. |
| **Tablero** | El panel (Trello o similar) con una tarjeta por historia y columnas del tipo *Por hacer / En curso / Hecho*. |
| **Riesgo ético específico** | Algo que puede salir mal **en vuestros datos y vuestro caso**. Si valdría para cualquier proyecto («cuidado con los sesgos»), es genérico. |
| **RGPD y AI Act** | La ley de protección de datos y el reglamento europeo de IA. |
| **README** | La portada del repositorio: explica el proyecto y cómo repetirlo. |
| **`requirements.txt`** | La lista de librerías con su versión, una por línea, como `pandas==2.3.3`. |

**Cómo se hace**

1. **Backlog: copiar la plantilla (5 minutos).** Copiad [`plantilla_backlog_y_sprints.md`](../1_Trabajar/plantillas/plantilla_backlog_y_sprints.md) como `backlog_y_sprints.md` en `sprint-14` (**Raw** → copiar → *Create new file*, como en el paso 4). Escribid el nombre del proyecto y quién es el Scrum Master de este sprint.

2. **Backlog: adaptar las historias (25 minutos).** La tabla del apartado 2 trae doce historias de ejemplo (H1 a H12). **Adaptadlas** a vuestro proyecto y añadid las vuestras (H13…) hasta tener **entre 10 y 15**. Cada fila lleva: historia, criterios de aceptación, tamaño (S, M o L), sprint (14 a 17), responsable y estado. Si no sabéis cómo comprobar una historia, no está bien definida. Una historia = una tarea que cabe en unas horas. Ejemplo para el brief 4:

    ```text
    | H13 | Como cliente quiero ver el error por franja horaria para saber cuándo no fiarme de la previsión | Gráfico del error por hora en el demostrador | M | 16 | (responsable) | por hacer |
    ```

3. **Backlog: objetivos de sprint y tablero (15 minutos).** En el apartado 3 escribid, para los sprints 14, 15, 16 y 17, **una frase medible** en la columna «Objetivo» (no toquéis las columnas de fechas ni de hitos, que ya vienen). Ejemplos: sprint 15, «tres modelos comparados con un registro y un candidato elegido»; sprint 16, «demostrador, evaluación, análisis de sesgos y memoria». Después cargad las historias en el **tablero**: una tarjeta por historia. Si no existe tablero, es lo primero que se crea. El **Scrum Master** lo mantiene al día. El apartado 5 (retrospectivas) se rellena en el paso 7.

4. **Plan ético: copiar y rellenar (45 minutos).** Copiad [`plantilla_registro_riesgos_eticos.md`](../1_Trabajar/plantillas/plantilla_registro_riesgos_eticos.md) como `riesgos_eticos.md`; en la línea «Versión vigente» dejad solo S14. Este documento **actualiza el checklist del Sprint 1** (`checklist_etico_v1.md`): si lo tenéis, pasad vuestras respuestas a la columna S1. Tiene cuatro partes:

    - **Parte A (checklist, seis bloques A1 a A6).** Rellenad la columna **S14** de cada pregunta con **✔** (cumplido con evidencia), **◐** (parcial), **✘** (no cumplido) o **n/a** (no aplica, con motivo) y, en «Evidencia», dónde se comprueba (por ejemplo, «Plan de datos» o «EDA»). Las columnas S15 y S16 se dejan para esos sprints.
    - **Parte B (clasificación normativa).** Contestad las seis preguntas: datos personales y de qué tipo; base legal; si haría falta una evaluación de impacto (EIPD); **nivel de riesgo del AI Act** (inaceptable, alto, limitado o mínimo); obligaciones que se derivan; y si el sistema apoya decisiones sobre personas. La nota de orientación al final de la parte B os ayuda.
    - **Parte C (registro de riesgos).** Escribid **al menos 5 riesgos específicos de vuestros datos**. Para cada uno: qué puede ir mal y a quién afecta, tipo (datos, modelo, uso, legal o técnico), **probabilidad (P)** e **impacto (I)** de 1 a 3, nivel = P × I (1-2 bajo, 3-4 medio, 6-9 alto), medida, responsable y estado. Mirad los ejemplos por brief al final de la parte C, pero **no los copiéis**: ajustadlos con vuestras cifras.
    - **Parte D (cierre).** No se toca: se rellena en el sprint 16.

    Ejemplo de una fila de la parte C (para un proyecto de series, adaptado de los ejemplos de la plantilla):

    ```text
    | R-01 | La previsión falla cuando hay un suceso atípico (una crisis) y el cliente planifica mal el personal | datos | 2 | 3 | 6 | Avisar en el demostrador de que no cubre sucesos extraordinarios y medir el error en los periodos atípicos | (responsable) | abierto | |
    ```

    Dejad vacía la última columna («cómo se evaluó la mitigación»): se rellena en el sprint 16.

5. **Repositorio: README (30 minutos).** Copiad [`plantilla_README_repositorio.md`](../1_Trabajar/plantillas/plantilla_README_repositorio.md) como `README.md` **en la raíz** del repositorio (no dentro de `sprint-14`). Sustituid lo que va entre corchetes en: el título y el brief; el apartado 1 (el problema en tres líneas); el 3 (el árbol ya muestra las carpetas `sprint-14/` a `sprint-17/`; hoy solo existe la de este sprint y las demás se crean en su momento); el 4 (**cómo reproducirlo**: descargar los datos y ejecutar los cuadernos en orden; en «Requisitos» escribid la versión de Python que usáis); el 6 (datos y licencias); el 7 (resumen de IA responsable); el 8 (equipo) y el 9 (tablero). La tabla de resultados (apartado 2) y el demostrador (apartado 5) se rellenan en los sprints 15 y 16: dejad los corchetes.

6. **Repositorio: `requirements.txt` (10 minutos).** En un cuaderno de Colab, ejecutad:

    ```python
    import pandas, numpy, sklearn, matplotlib

    for modulo, nombre in [(pandas, "pandas"), (numpy, "numpy"), (sklearn, "scikit-learn"), (matplotlib, "matplotlib")]:
        print(f"{nombre}=={modulo.__version__}")
    ```

    Qué hace cada línea:

    - `import` carga las cuatro librerías; añadid las que importen vuestros cuadernos (por ejemplo `scipy` o `seaborn`).
    - El bucle recorre cada pareja (librería, nombre) y escribe `nombre==versión`. Sale una línea por librería, como `pandas==2.3.3` (la versión que tenga vuestro Colab). `scikit-learn` es el nombre de instalación de `sklearn`.

    Copiad las líneas en un archivo `requirements.txt` en la raíz del repositorio (*Add file → Create new file*). También se puede hacer con `pip show nombre` o, en Colab, con `!pip freeze` y buscando el nombre.

7. **Repositorio: commits y uso de IA (10 minutos).** Comprobad en el historial (icono del reloj) que **todas las personas** tienen al menos un *commit*. Usad mensajes con la forma `tipo: descripción`: `docs: añado backlog`, `data: añado plan de datos`. Ningún dato personal ni claves. En el apartado 7 del README **añadid una línea de «Uso de IA»**: qué pedisteis a la IA y qué comprobasteis a mano.

**Qué deberíais ver.** `backlog_y_sprints.md` con entre 10 y 15 historias y cuatro objetivos de sprint; `riesgos_eticos.md` con la columna S14 rellena, la parte B contestada y cinco filas en la parte C; un `README.md` y un `requirements.txt` en la raíz; un tablero con las historias; y *commits* de todas las personas.

**Hecho cuando:** los cuatro documentos están escritos, el tablero tiene las historias y otra persona podría descargar los datos y ejecutar los cuadernos solo con el README.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| La tabla del backlog se ve como texto con barras | Falta una barra vertical o una línea en blanco antes de la tabla. | Pulsad **Preview** antes de guardar y comprobad cada fila. |
| Tenéis 8 historias o 20 | La rúbrica pide entre 10 y 15. | Juntad las que sean muy pequeñas o dejad las demás como ideas fuera del backlog. |
| Los riesgos son «cuidado con los sesgos» o «hay que proteger los datos» | Son genéricos. | Si valen para cualquier proyecto, no valen: poned qué dato concreto, qué cifra y a quién perjudica. |
| No sabéis qué poner en probabilidad e impacto | Las dos escalas van de 1 (bajo) a 3 (alto). | Puntuad entre todos; el nivel es P × I. Los de nivel 6 a 9 necesitan una medida que se pueda comprobar. |
| `ModuleNotFoundError: No module named 'shap'` (con otro nombre) | Esa librería no está instalada en la sesión. | Quitadla del `import` si no la usáis; si la usáis, añadid antes una celda con `!pip install shap`. |
| El historial solo tiene *commits* de una persona | Una sola persona hizo todas las subidas. | Repartid las subidas: cada persona sube o edita al menos un archivo con su cuenta. |
| El README dice «Python 3.11» pero Colab usa otra versión | El ejemplo de la plantilla puede no coincidir con vuestro entorno. | Escribid la versión que os salga con `import sys; print(sys.version)`. |

<!--nav-->
---

[← Paso 5](Reto_Sprint_14_paso_5.md) · [Ficha del reto](Reto_Sprint_14.md) · [Paso 7 →](Reto_Sprint_14_paso_7.md)
<!--/nav-->
