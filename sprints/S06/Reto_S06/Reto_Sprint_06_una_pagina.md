# Sprint 6 · Reto «Datos sucios, cliente impaciente» · en una página

> Versión corta para **trabajar con ella abierta**. La ficha completa sigue en [Reto_Sprint_06.md](Reto_Sprint_06.md); la plantilla del informe está en [`informe_calidad_plantilla.md`](informe_calidad_plantilla.md).

**El cliente.** TurisData os manda por correo [`reservas_sucio.csv`](../../../datos/reservas_sucio.csv), exportado a mano de varios sistemas. El gerente quiere un primer modelo de cancelaciones «para ayer», pero no se fía de los datos.
**Qué entregáis (no cambia):** `informe_calidad.md`, `reto_S06.ipynb` y `README.md`.
**Tiempo en clase:** planning 10 min · reto 80 min (30 el 6/11 y 50 el 9/11) · entrega y review 35 min.

## Tres niveles: el equipo decide hasta dónde llega

| Nivel | Qué hay que tener | Nota* |
|---|---|---|
| 🟢 **Mínimo** (todos los equipos) | Tabla de **al menos 6 defectos** con qué, dónde, cuántas filas, causa probable y tratamiento (los tres más graves destacados) · **una** función `limpiar_reservas` con docstring que devuelve la tabla limpia y un resumen de lo cambiado · el cuaderno se ejecuta de arriba abajo · README | 2 |
| 🟡 **Estándar** | Pipeline que imputa, escala y codifica **ajustando solo con train** · `DummyClassifier` y un modelo comparados con validación cruzada (frase con media ± desviación) · README con versiones de las librerías | 3 |
| 🔴 **Extra** | Tabla con los 8–10 defectos · partición temporal en lugar de aleatoria, justificada · explicar qué pasaría si se ajustara el escalado con todos los datos (fuga) | 4 |

\*Orientativo; puntúa el docente con la rúbrica del curso (0–4 en cada criterio). El mínimo es una entrega válida y evaluable; la «Definition of Done» de la ficha completa describe el nivel **estándar**.

## Frases para el informe y el README

- «Hemos encontrado … defectos. El más grave es …, que afecta a … filas. Creemos que viene de … y lo tratamos con … porque …»
- «`limpiar_reservas` no toca el CSV original: devuelve una tabla nueva y un resumen con …»
- «Nuestro modelo obtiene un F1 medio de … ± …, frente a … del modelo tonto. Eso significa que …»
- «Límites: …»

## Antes de entregar
- [ ] El cuaderno corre con *Restart & Run all* · [ ] El informe recoge cada defecto con causa y tratamiento
- [ ] Pipeline ajustado solo con train · [ ] Baseline y modelo comparados · [ ] Subido a Git, [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md) rellenadas
