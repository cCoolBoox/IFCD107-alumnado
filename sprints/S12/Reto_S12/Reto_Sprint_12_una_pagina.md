# Sprint 12 · Reto «Escuchar al cliente» · en una página

> Versión corta para **trabajar con ella abierta**. La ficha completa sigue en [Reto_Sprint_12.md](Reto_Sprint_12.md); la plantilla del informe está en [`plantilla_informe_cliente.md`](plantilla_informe_cliente.md). El informe visual del Sprint 13 va dentro del último día.

**El cliente.** TurisData recibe decenas de reseñas y de mensajes con las mismas preguntas. Quiere (1) saber **qué opinan y de qué se quejan**, (2) **prever la ocupación de la semana siguiente** y (3) probar un **asistente que responda con la política del alojamiento sin inventar nada** (RAG).
**Qué entregáis (no cambia):** una carpeta o zip por equipo con (1) el informe de reseñas, (2) el cuaderno de ocupación, (3) el cuaderno del asistente con su tabla de evaluación y (4) la nota de IA responsable, más un `LEEME.md` de 5 líneas.
**Tiempo en clase:** planning 10 min · reto 155 min (65 el 24/11 y 90 el 25/11, con el reto del S13) · entrega y review 35 min. **Se reparte:** cada persona lidera una parte, pero todas entienden todas.

## Tres niveles: el equipo decide hasta dónde llega

| Nivel | Qué hay que tener | Nota* |
|---|---|---|
| 🟢 **Mínimo** (todos los equipos) | **Reseñas:** sentimiento con cifras, un gráfico y 3 citas reales · **Ocupación:** partición por fecha y *baseline* de los próximos 7 días · **Asistente:** cita la fuente y responde «No consta…» si no hay respuesta · nota de IA responsable · `LEEME.md` | 2 |
| 🟡 **Estándar** | Un modelo mejor que el baseline y una comprobación honesta de si de verdad lo mejora · asistente evaluado con las 20 preguntas de referencia y 5 vuestras (aciertos, sin fuente, alucinaciones) · **3 intentos de ataque** probados y descritos · informe de 2 páginas con 3 recomendaciones · ninguna clave en el código | 3 |
| 🔴 **Extra** | Temas más criticados y más valorados con ejemplos reales · escalado y vectorización ajustados solo con entrenamiento, justificado · todo funciona de arriba abajo **sin internet** | 4 |

\*Orientativo; puntúa el docente con la rúbrica del curso (0–4 en cada criterio). El mínimo es una entrega válida y evaluable; la «Definition of Done» de la ficha completa describe el nivel **estándar**.

## Frases para el informe

- «El … % de las reseñas es positivo. Lo más criticado es …, por ejemplo: «…». Lo más valorado es …»
- «Para prever la ocupación, el baseline (…) se equivoca de media … puntos y nuestro modelo …; (sí / no) mejora porque …»
- «El asistente respondió bien … de 25 preguntas, no tenía fuente en … y se inventó … Ante «Ignora las instrucciones…», …»
- «Recomendamos 1) … 2) … 3) … Límites: …»

## Antes de entregar
- [ ] Serie partida por fecha y baseline en la tabla · [ ] Asistente con fuente y «No consta…» · [ ] 3 ataques probados
- [ ] Ninguna clave en el repositorio · [ ] `LEEME.md` · [ ] [Autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md) rellenadas
