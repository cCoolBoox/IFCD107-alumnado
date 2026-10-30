# Sprint 7 · Reto «Precio y cancelación» · en una página

> Versión corta para **trabajar con ella abierta**. La ficha completa (recursos, tablas de requisitos, rúbrica, guía paso a paso, uso de la IA y errores frecuentes) sigue en [Reto_Sprint_07.md](../2_Ficha_completa/Reto_Sprint_07.md); la plantilla del informe está en [`informe_modelado_plantilla.md`](../4_Plantillas_y_entrega/informe_modelado_plantilla.md).

**El cliente.** El gerente de TurisData quiere una **tarifa de referencia** (predecir `precio_noche`, un número) y un **aviso de riesgo de cancelación** (predecir `cancelada`, sí o no). No quiere oír hablar de «AUC»: quiere saber **cuánto dinero se juega** si el modelo se equivoca. Vosotros traducís las métricas a **euros**.
**Qué entregáis (no cambia):** el informe `informe_modelado.md` (2–3 páginas), el cuaderno `reto_S07.ipynb` y el `README.md`. **Al final del sprint se suben a `sprint-07/` del repositorio del equipo: 3 ficheros del equipo (esos tres) + 1 autoevaluación y coevaluación por persona** (`autoevaluacion_nombre.md`).
**Tiempo en clase:** planning 10 min · reto 55 min (25 el día 1 y 30 el día 2) · entrega 15 min. Lo que no quepa, a casa o a la 6.ª hora.

## Tres niveles: el equipo decide hasta dónde llega

| Nivel | Qué hay que tener | Nota* |
|---|---|---|
| 🟢 **Mínimo** (todos los equipos) | **Precio:** referencia (la media) y regresión lineal con MAE y RMSE **en euros** · **Cancelación:** referencia y regresión logística con matriz de confusión · sin fuga (`cancelada` no predice el precio) · `COSTE_FN` y `COSTE_FP` escritos como **hipótesis con su razón** · un umbral elegido y justificado en una frase · informe corto y README con semilla y versiones | 2 |
| 🟡 **Estándar** | Mejora del modelo de precio (polinómico o Ridge) con R² · AUC y AP · umbral que **minimiza el coste total** con validación cruzada sobre train · test usado **una sola vez** · análisis de sensibilidad (¿y si los costes cambian?) · recomendación con cifras y límites · riesgos de IA responsable | 3 |
| 🔴 **Extra** | Un segundo modelo de clasificación (por ejemplo, k-NN) comparado · remuestreo solo en train · recomendación de *overbooking* con ahorro estimado en euros por temporada | 4 |

\*Orientativo; puntúa el docente con la rúbrica del curso (0–4 en cada criterio). El mínimo es una entrega válida y evaluable; la «Definition of Done» de la ficha completa describe el nivel **estándar**.

## Reparto sugerido de los 55 minutos

| Día | Min | Qué | Se sabe que está hecho cuando… |
|---|---|---|---|
| 1 | 5 | Abrir `reto_S07`, escribir `COSTE_FN` y `COSTE_FP` con su razón | Dos variables con una frase de razón cada una |
| 1 | 20 | Precio: variables sin fuga, referencia, lineal y una mejora | Tabla con MAE, RMSE y R² y una frase en euros |
| 2 | 15 | Cancelación: referencia, logística, matriz, ROC/PR y umbral | Umbral elegido con vuestros costes; test usado una vez |
| 2 | 5 | Sensibilidad: FN el doble, FP la mitad | Tabla con tres combinaciones o más |
| 2 | 10 | Informe (plantilla) y README | Otra persona podría ejecutarlo con el README |

## Frases para el informe (completad los huecos)

- «Recomendamos activar el aviso con un umbral de …. Con nuestras hipótesis (noche vacía = … €, compensación = … €), el coste esperado pasa de … € a … €: ahorra unos … €.»
- «Si la compensación costara … €, el umbral óptimo sería … y el ahorro … €: la recomendación (se mantiene / cambia) porque …»
- «El modelo de precio se equivoca de media … € (MAE). Es (aceptable / poco) porque …»
- «Límites: datos sintéticos de un solo hotel; …»

## Antes de entregar
- **Archivos subidos en `sprint-07/`:** `informe_modelado.md` · `reto_S07.ipynb` · `README.md` · `autoevaluacion_nombre.md` (**uno por persona**) = 3 + N ficheros
- [ ] Referencias presentes y sin fuga · [ ] Costes de FN y FP como hipótesis con razón · [ ] Umbral elegido sin mirar el test · [ ] Recomendación con cifras y límites
- [ ] Cuaderno ejecutable de arriba abajo · [ ] README con `SEMILLA = 42`, versiones y uso de la IA · [ ] Revisión con la rúbrica anotada en el informe
- [ ] [Autoevaluación y coevaluación](../4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md): **una por persona**, subida a `sprint-07/`
