# Sprint 7 · Reto «Precio y cancelación» · en una página

> Versión corta para **trabajar con ella abierta**. La ficha completa sigue en [Reto_Sprint_07.md](Reto_Sprint_07.md).

**El cliente.** El gerente quiere dos herramientas: una **tarifa de referencia** (predecir `precio_noche`, un número) y un **aviso de riesgo de cancelación** (predecir `cancelada`, sí o no). Y no quiere oír hablar de «AUC»: quiere **euros**.
**Qué entregáis (no cambia):** `informe_modelado.md` (o PDF) de 2–3 páginas, el cuaderno `reto_S07.ipynb` y `README.md`.
**Tiempo en clase:** planning 10 min · reto 55 min (25 el 10/11 y 30 el 11/11) · entrega 15 min.

## Tres niveles: el equipo decide hasta dónde llega

| Nivel | Qué hay que tener | Nota* |
|---|---|---|
| 🟢 **Mínimo** (todos los equipos) | **Precio:** baseline y regresión lineal con MAE y RMSE **en euros** · **Cancelación:** baseline y regresión logística con matriz de confusión · los costes de cada error escritos como **hipótesis** · un umbral elegido y justificado en una frase | 2 |
| 🟡 **Estándar** | Mejora del modelo de precio (por ejemplo, polinómico o Ridge) · AUC y precisión–recall · umbral que **minimiza el coste total** · análisis de sensibilidad (¿y si los costes cambian?) · test usado **una sola vez**, sin fuga | 3 |
| 🔴 **Extra** | Un segundo modelo de clasificación (por ejemplo, k-NN) comparado · remuestreo solo en train · recomendación de *overbooking* con ahorro estimado en euros por temporada | 4 |

\*Orientativo; puntúa el docente con la rúbrica del curso (0–4 en cada criterio). El mínimo es una entrega válida y evaluable; la «Definition of Done» de la ficha completa describe el nivel **estándar**.

## Frases para el informe

- «Recomendamos activar el aviso con un umbral de …. Con nuestras hipótesis (noche vacía = … €, compensación = … €), el coste esperado pasa de … € a … €: ahorra unos … €.»
- «Si la compensación costara … €, el umbral óptimo sería … y el ahorro … €: la recomendación (se mantiene / cambia) porque …»
- «El modelo de precio se equivoca de media … € (MAE). Es (aceptable / poco) porque …»
- «Límites: datos sintéticos de un solo hotel; …»

## Antes de entregar
- [ ] Baselines presentes · [ ] Costes de FN y FP como hipótesis · [ ] Recomendación con cifras y límites
- [ ] Cuaderno ejecutable de principio a fin · [ ] Subido a Git, [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md) rellenadas
