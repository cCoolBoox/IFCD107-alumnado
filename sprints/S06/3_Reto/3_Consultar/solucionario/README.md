# Sprint 6 · Reto «Datos sucios, cliente impaciente»

Entrega de referencia del docente: sirve de modelo de lo que hay que subir a `sprint-06/`.

## Qué hay
- `informe_calidad.md`: qué está mal en `reservas_sucio.csv`, cuántas filas afecta y qué se hizo con cada defecto (10 defectos, resumen para el gerente, preguntas al cliente, IA responsable y revisión con la rúbrica).
- `reto_S06.ipynb`: inventario de defectos, función `limpiar_reservas`, partición, *pipeline*, *baseline*, validación cruzada y extras.
- `README.md`: este documento.

## Cómo ejecutarlo
1. Abrir `reto_S06.ipynb` en Google Colab (*Archivo → Subir cuaderno*).
2. *Entorno de ejecución → Reiniciar y ejecutar todo*. Orden: preparación, inventario, limpieza, partición, *pipeline*, IA responsable, extras, versiones.
3. La primera celda descarga `reservas_sucio.csv` desde el repositorio del curso si no está en `data/` o `datos/`.
4. Cifras de control: 1545 → 1500 filas; AUC en validación cruzada 0,758 ± 0,025 (modelo tonto 0,500).

## Versiones
- Python 3.13, pandas 2.3.3, scikit-learn 1.9.1 (en Colab saldrán otras; las cifras pueden variar en el último decimal).
- Semilla fija: 42. Solo librerías del curso.

## Quién hizo qué
- Persona A: inventario de defectos y tabla del informe.
- Persona B: `limpiar_reservas`, partición, *pipeline* y validación cruzada.
- Persona C: README, revisión con la rúbrica y subida a GitHub.
- (Reparto de ejemplo; cada equipo pone sus nombres.)

## Uso de la IA
- **Qué se pidió:** explicar `fillna`, `drop_duplicates` y `to_datetime` con ejemplos pequeños; depurar un `KeyError`; revisar si el *pipeline* tiene fuga de datos; reescribir la tabla del informe sin cambiar cifras.
- **Qué se revisó:** cada línea se ejecutó y se entiende; las cifras del informe salen del cuaderno, no de la IA; no se instaló ningún paquete extra; no se subieron datos personales ni claves.
- **Qué se cambió:** cualquier sugerencia de rellenar nulos antes de partir *train* y *test* se descartó, porque sería fuga de datos; la imputación va dentro del `Pipeline`.
- (Ejemplo de referencia: cada equipo cuenta lo que hizo de verdad, incluidos los fallos concretos de la IA que detecte.)
