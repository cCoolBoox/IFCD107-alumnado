# Sprint 14 · Reto «Proyecto final: ficha y datos» · Equipo de ejemplo

Entrega de referencia del docente: sirve de modelo de lo que hay que subir al repositorio del equipo. Es una forma correcta de hacerlo, no la única. Para ver qué se pide, [entrega y rúbrica](../../3_Reto/2_Entregar/entrega_y_rubrica.md).

Proyecto del equipo de ejemplo: **BiciPrevisión** (brief libre inspirado en el 4): prever las bicis alquiladas en cada hora de mañana. Los datos son reales ([UCI Bike Sharing](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset), CC BY 4.0). Esta carpeta es el punto de partida de los sprints 15–17.

## Qué se entrega
La carpeta repite la forma del repositorio del equipo:
- [`raiz/README.md`](raiz/README.md) y [`raiz/requirements.txt`](raiz/requirements.txt): van en la **raíz** del repositorio (el README sigue la plantilla del curso, con los apartados de este sprint rellenos).
- [`sprint-14/ficha_proyecto.md`](sprint-14/ficha_proyecto.md): la ficha de 1 página, en su versión 2 (tras el *go / no-go*).
- [`sprint-14/plan_datos_licencias.md`](sprint-14/plan_datos_licencias.md): fuente, licencia, calidad, linaje y partición.
- [`sprint-14/descargar_datos.py`](sprint-14/descargar_datos.py): baja los datos y comprueba filas y huella (por eso el CSV no se sube).
- [`sprint-14/01_eda.ipynb`](sprint-14/01_eda.ipynb) y [`sprint-14/02_baseline.ipynb`](sprint-14/02_baseline.ipynb): EDA y *baseline*, ejecutados de arriba abajo.
- [`sprint-14/backlog_y_sprints.md`](sprint-14/backlog_y_sprints.md): 13 historias, objetivo de cada sprint y retro del Sprint 14.
- [`sprint-14/riesgos_eticos.md`](sprint-14/riesgos_eticos.md): checklist, clasificación AI Act y 7 riesgos.
- [`sprint-14/autoevaluacion_marta.md`](sprint-14/autoevaluacion_marta.md): la hoja de **una** persona (cada persona sube la suya).

El tablero Scrum (capturas en `sprint-14/scrum/`) no se incluye: es una captura de pantalla del equipo.

## Quién hizo qué (reparto de ejemplo)
- Marta: ficha, backlog y tablero (Scrum Master).
- Persona B: EDA y *baseline* (responsable técnico).
- Persona C: plan de datos y `descargar_datos.py` (responsable de datos).
- Persona D: riesgos, README y revisión con la rúbrica (IA responsable).

## Cómo se repite
1. Copiar `raiz/*` a la raíz de un repositorio nuevo y `sprint-14/` a `sprint-14/`.
2. `pip install -r requirements.txt` y `python sprint-14/descargar_datos.py` (crea `data/bicis_horas.csv`).
3. Abrir los dos cuadernos en orden y *Ejecutar todo*. El *baseline* debe dar **MAE 69,5** en validación.

Versiones: Python 3.13.18, numpy 2.5.3, pandas 2.3.3, scikit-learn 1.9.1. Semilla: `SEMILLA = 42`.

## Uso de IA
- **Qué se pidió:** una primera lista de variables, explicar WAPE y un borrador de la tabla de riesgos.
- **Qué se revisó:** la licencia en la página de la UCI (la IA dijo «MIT»; es CC BY 4.0) y el número de filas con `len` (la IA dijo 17.544; hay 17.379); las cifras de la ficha son las de los cuadernos.
- **Qué se cambió:** se rehízo la tabla de riesgos con los hallazgos del EDA (la IA proponía riesgos genéricos).
- (Ejemplo de referencia: cada equipo cuenta lo que hizo de verdad, incluidos los fallos concretos de la IA que detecte.)

## Revisión con la rúbrica
Está en [`raiz/README.md`](raiz/README.md) (apartado final), hecha por Persona D el 30/11/2026: 4 / 4 / 4 / 4.
