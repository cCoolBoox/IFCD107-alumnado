# Sprint 12 · Reto «Escuchar al cliente» · en una página

> Versión corta para **trabajar con ella abierta**. La ficha completa (qué pide el cliente, recursos, uso de la IA y errores frecuentes) sigue en [Reto_Sprint_12.md](../3_Consultar/Reto_Sprint_12.md) y cada paso, explicado, en su propio archivo (enlaces tras el reparto de minutos); la plantilla del informe está en [`plantilla_informe_cliente.md`](plantillas/plantilla_informe_cliente.md). El informe visual del Sprint 13 es otro reto, con su propia ficha.

- **El cliente.**
    - TurisData recibe decenas de reseñas y de mensajes con las mismas preguntas.
    - Quiere tres cosas:
        - Saber **qué opinan y de qué se quejan**.
        - **Prever la ocupación de la semana siguiente**.
        - Probar un **asistente que responda con la política del alojamiento sin inventar nada** (RAG).
    - Los datos son sintéticos: decidlo en el informe.
- **Qué entregáis (no cambia):**
    - El informe de reseñas y el cuaderno de ocupación.
    - El cuaderno del asistente con su tabla de evaluación.
    - La nota de IA responsable y un `LEEME.md` de 5 líneas.
    - Al final se suben a `sprint-12/` del repositorio del equipo (lista completa en «Antes de entregar»).
- **Tiempo en clase:**
    - Planning: 10 min (día 1); reto: 130 min y entrega y review: 35 min (días 2 y 3).
    - **Se reparte:** cada persona lidera una parte, pero todas entienden todas.

## Tres niveles: el equipo decide hasta dónde llega

| Nivel | Qué hay que tener | Nota* |
|---|---|---|
| 🟢 **Mínimo** (todos los equipos) | **Ocupación:** serie partida por fecha y *baseline* de los próximos 7 días con su MAE · **Reseñas:** sentimiento con cifras, un gráfico y 3 citas reales · **Asistente:** cita la fuente y responde «No consta…» si no hay respuesta · nota de IA responsable · `LEEME.md` | 2 |
| 🟡 **Estándar** | Un modelo (SARIMAX o GRU) comparado con el *baseline*, con veredicto honesto · sentimiento evaluado en prueba · asistente evaluado con las 20 preguntas de referencia y 5 vuestras (aciertos, sin fuente, alucinaciones) · **3 intentos de ataque** probados y descritos · informe de 2 páginas con 3 recomendaciones · ninguna clave en el código | 3 |
| 🔴 **Extra** | Temas más criticados y más valorados con ejemplos reales · escalado y vectorización ajustados solo con entrenamiento, justificado · todo funciona de arriba abajo **sin internet** · alternativas comparadas y medidas de seguridad con cifras | 4 |

\*Orientativo; puntúa el docente con la rúbrica del curso (0–4 en cada criterio). El mínimo es una entrega válida y evaluable; la «Definition of Done» de la ficha completa describe el nivel **estándar**.

## Reparto sugerido de los 165 minutos (reto, entrega y review)

| Min | Qué | Se sabe que está hecho cuando… |
|---|---|---|
| 5 | Día 2: repasar el reparto, la rúbrica y la pregunta de negocio de cada parte (paso 1) | Cada tarjeta tiene responsable y día |
| 50 | Día 2: reseñas (A) y asistente (C), en paralelo | Hay sentimiento con gráfico y un asistente que cita |
| 30 | Día 3: ocupación (B) | Hay tabla de MAE con *baseline* y modelo |
| 40 | Día 3: evaluar las 25 preguntas, probar 3 ataques y medir una defensa | `evaluacion_asistente.csv` completo |
| 40 | Día 3: informe, nota y `LEEME.md`; todo desde cero; revisión con la rúbrica; subida y ensayo de la review | Otra persona podría repetirlo con el `LEEME.md` |

**Cada paso, explicado al detalle:** [Paso 1](../3_Consultar/Reto_Sprint_12_paso_1.md) · [Paso 2](../3_Consultar/Reto_Sprint_12_paso_2.md) · [Paso 3](../3_Consultar/Reto_Sprint_12_paso_3.md) · [Paso 4](../3_Consultar/Reto_Sprint_12_paso_4.md)

## Frases para el informe

- «El … % de las reseñas es positivo. Lo más criticado es …, por ejemplo: «…». Lo más valorado es …»
- «Para prever la ocupación, el *baseline* (…) se equivoca de media … puntos y nuestro modelo …; (sí / no) mejora porque …»
- «El asistente respondió bien … de 25 preguntas, no tenía fuente en … y se inventó … Ante «Ignora las instrucciones…», …»
- «Recomendamos 1) … 2) … 3) … Límites: …»

## Antes de entregar
- **Archivos subidos en `sprint-12/`:** `informe_resenas.md` · `grafico_resenas.png` · `resenas.ipynb` · `ocupacion.ipynb` · `asistente_rag.ipynb` · `evaluacion_asistente.csv` · `nota_ia_responsable.md` · `LEEME.md` · `autoevaluacion_nombre.md` (**uno por persona**) = 8 + N ficheros
- [ ] Serie partida por fecha y *baseline* en la tabla · [ ] Asistente con fuente y «No consta…» · [ ] 3 ataques probados · [ ] Ninguna clave en el repositorio
- [ ] Informe con 3 recomendaciones y límites · [ ] Cuadernos ejecutados de arriba abajo · [ ] `LEEME.md` con la «Revisión con la rúbrica»
- [ ] [Autoevaluación y coevaluación](../2_Entregar/autoevaluacion_y_coevaluacion.md): **una por persona**, subida a `sprint-12/`
