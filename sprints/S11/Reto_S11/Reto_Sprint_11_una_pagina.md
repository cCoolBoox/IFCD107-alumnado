# Sprint 11 · Reto «Visión artificial para el cliente» · en una página

> Versión corta para **trabajar con ella abierta**. La ficha completa sigue en [Reto_Sprint_11.md](Reto_Sprint_11.md). Se hace con el esqueleto del cuaderno [`S11_04`](../notebooks/S11_04_reto_vision_cliente.ipynb).

**El cliente.** TurisData recibe cientos de fotos a la semana y una persona las clasifica a mano. Quiere saber si un modelo puede **pre-clasificarlas** y, sobre todo, **en qué se equivoca**, para decidir qué fotos debe revisar una persona. **Lo importante no es el acierto, sino saber cuándo no fiarse.**
**Qué entregáis (no cambia):** el modelo (`.keras` o el cuaderno que lo reproduce), el **demostrador** y el **análisis de errores** de 1–2 páginas.
**Tiempo en clase:** planning 10 min · reto 105 min (25 el 19/11 y 80 el 20/11) · entrega, review y retro 30 min.

## Tres niveles: el equipo decide hasta dónde llega

| Nivel | Qué hay que tener | Nota* |
|---|---|---|
| 🟢 **Mínimo** (todos los equipos) | Conjunto de fotos con **una carpeta por clase** (el sintético del cuaderno vale) · modelo con *transfer learning* · métricas por clase y matriz de confusión · **3 fotos mal clasificadas** con una hipótesis cada una | 2 |
| 🟡 **Estándar** | Referencia «desde cero» para ver cuánto aporta el *transfer learning* · **6 fotos mal clasificadas** con hipótesis y mejora · demostrador: clase, confianza y «revisar a mano» si la confianza es baja · origen y licencia de los datos y dos riesgos de IA responsable | 3 |
| 🔴 **Extra** | Rama de Colab con MobileNetV2 y fotos reales con licencia · elegir el umbral de confianza con los datos (cuántas fotos se revisan a mano frente a cuántos fallos se evitan) · propuesta de mejora probada | 4 |

\*Orientativo; puntúa el docente con la rúbrica del curso (0–4 en cada criterio). El mínimo es una entrega válida y evaluable; la «Definition of Done» de la ficha completa describe el nivel **estándar**.

## Frases para el análisis de errores

- «El modelo acierta un … % en prueba, pero en la clase … solo un … %. Lo confunde con … porque …»
- «Foto …: la clasificó como … en vez de …. Creemos que es por … Podríamos mejorarlo con …»
- «Con un umbral de confianza de …, una persona revisa el … % de las fotos y evitamos … de cada … errores.»
- «Los datos vienen de … con licencia …. Riesgos: …»

## Antes de entregar
- [ ] Cuaderno de arriba abajo, semillas fijas · [ ] Prueba usada una sola vez · [ ] Matriz de confusión interpretada
- [ ] Errores analizados con hipótesis · [ ] Demostrador con «revisar a mano» · [ ] [Autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md) rellenadas
