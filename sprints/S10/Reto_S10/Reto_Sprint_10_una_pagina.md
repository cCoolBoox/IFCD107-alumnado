# Sprint 10 · Reto «¿Vale la pena la red?» · en una página

> Versión corta para **trabajar con ella abierta**. La ficha completa sigue en [Reto_Sprint_10.md](Reto_Sprint_10.md). Se hace con el esqueleto del cuaderno [`S10_04`](../notebooks/S10_04_reto_vale_la_pena.ipynb).

**El cliente.** La dirección oye hablar de redes neuronales en todas partes y pregunta si debe **sustituir su modelo de cancelaciones por una red**. Quiere evidencias con el coste incluido. **«No compensa» es una respuesta tan válida como «sí».**
**Qué entregáis (no cambia):** el cuaderno ejecutable y un **informe comparativo de 1–2 páginas** *ML clásico frente a MLP*.
**Tiempo en clase:** planning 10 min · reto 90 min (el 18/11) · entrega, review y retro 40 min.

## Tres niveles: el equipo decide hasta dónde llega

| Nivel | Qué hay que tener | Nota* |
|---|---|---|
| 🟢 **Mínimo** (todos los equipos) | Partición única entrenamiento/validación/prueba · modelo de referencia (boosting) y **un MLP** con las mismas métricas · curvas de aprendizaje y una frase de diagnóstico de sobreajuste · prueba usada **una sola vez** · recomendación en una frase | 2 |
| 🟡 **Estándar** | **2–3 variantes** del MLP (tamaño, *dropout*, L2, tasa de aprendizaje) elegidas **mirando solo la validación** · comparación con **varias semillas** y su incertidumbre (¿la diferencia es real o ruido?) · informe con recomendación, coste y límites · dos riesgos de IA responsable | 3 |
| 🔴 **Extra** | Variante de regresión (precio por noche) · comparar el coste de entrenar y mantener cada modelo · guardar el modelo y probarlo recargado | 4 |

\*Orientativo; puntúa el docente con la rúbrica del curso (0–4 en cada criterio). El mínimo es una entrega válida y evaluable; la «Definition of Done» de la ficha completa describe el nivel **estándar**.

## Frases para el informe

- «Con el mismo conjunto de datos, el boosting obtiene un AUC de … ± … y la red … ± …. La diferencia (es / no es) mayor que el ruido entre semillas.»
- «La red (mejora / no mejora) al modelo clásico, y cuesta … (tiempo de entrenamiento, ajuste, explicabilidad).»
- «Recomendamos … porque … Si el cliente …, entonces …»
- «Riesgos: … Medidas: …»

## Antes de entregar
- [ ] Cuaderno de arriba abajo con semillas fijas · [ ] La prueba se ha usado una sola vez
- [ ] Informe con recomendación concreta, coste y límites · [ ] [Autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md) rellenadas
