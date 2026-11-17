# Sprint 16 · Reto «Entrega final: evaluar, demostrar y documentar» · Equipo de ejemplo

Entrega de referencia del docente: sirve de modelo de lo que hay que subir a `sprint-16/`. Es una forma correcta de hacerlo, no la única. Para ver qué se pide, [entrega y rúbrica](../../3_Reto/2_Entregar/entrega_y_rubrica.md).

Proyecto del equipo de ejemplo: **BiciPrevisión**. Parte del modelo candidato del [Sprint 15](../../../S15/4_Referencia/entrega_de_referencia/README.md) (`sprint-16/` lo necesita para ejecutar el cuaderno).

## Qué se entrega
La carpeta `sprint-16/` repite la del repositorio del equipo:
- [`README.md`](sprint-16/README.md): la versión final (la raíz del repositorio lleva una copia al día), con la «Revisión con la rúbrica» y la prueba en limpio.
- [`notebooks/04_evaluacion.ipynb`](sprint-16/notebooks/04_evaluacion.ipynb): evaluación en test, gráficos, subgrupos, errores, mitigación y riesgos de datos; genera `figuras/` y `demostrador/modelo/`.
- [`demostrador/`](sprint-16/demostrador/): `app.py`, `logica.py`, `requirements.txt`, `tests/test_logica.py` y `modelo/` (modelo, metadatos e histórico de la demo).
- [`docs/riesgos_eticos.md`](sprint-16/docs/riesgos_eticos.md), [`docs/model_card.md`](sprint-16/docs/model_card.md) y [`docs/memoria_tecnica.pdf`](sprint-16/docs/memoria_tecnica.pdf).
- [`autoevaluacion_marta.md`](sprint-16/autoevaluacion_marta.md): la hoja de **una** persona (cada persona sube la suya).

Un equipo de cuatro personas sube **9 + 4 = 13** ficheros. **No incluidos en esta copia:** `docs/demo.mp4` (grabación de pantalla del equipo) y la coevaluación confidencial (se entrega al docente). La carpeta `docs/figuras/` trae también las capturas del demostrador que usa la memoria.

## Quién hizo qué (reparto de ejemplo)
- Marta: cuaderno de evaluación y gráficos. Persona B: cierre del registro de riesgos y README. Persona C: demostrador, pruebas y prueba en limpio. Persona D: mitigación, *model card* y memoria.

## Cómo se repite
1. Copiar la entrega del Sprint 15 en `sprint-15/` y esta en `sprint-16/`, con `pip install -r sprint-16/demostrador/requirements.txt`.
2. Ejecutar `04_evaluacion.ipynb` (con `bicis_horas.csv` en `datos/`): sale **MAE 44,0** en test y se rehacen figuras y `demostrador/modelo/`.
3. `cd sprint-16/demostrador && python -m pytest -q`, y `streamlit run sprint-16/demostrador/app.py` desde la raíz.

Versiones: Python 3.13.18, numpy 2.5.3, pandas 2.3.3, scikit-learn 1.9.1. Semilla: `SEMILLA = 42`.

## Uso de IA
- **Qué se pidió:** gráficos, validación cruzada de las mitigaciones y esqueleto del demostrador.
- **Qué se revisó:** que el MAE coincide con el del Sprint 15, que ninguna decisión usa el test y que las cifras de todos los documentos salen de la celda «Cifras para la memoria».
- **Qué se cambió:** los intervalos por franja (la propuesta inicial dejaba infracubierto el fin de semana) y un título de gráfico que prometía una mejora en todas las horas.
- (Ejemplo de referencia: cada equipo cuenta lo que hizo de verdad, incluidos los fallos concretos de la IA que detecte.)

## Revisión con la rúbrica
Está al final de [`sprint-16/README.md`](sprint-16/README.md), hecha por Persona C el 10/12/2026: 4 / 4 / 4 / 4.
