# Sprint 13 · Reto «Informe visual para dirección» · en una página

> Versión corta para **trabajar con ella abierta**. La ficha completa (rúbrica, ayudas, errores frecuentes, guía paso a paso) sigue en [Reto_Sprint_13.md](../2_Ficha_completa/Reto_Sprint_13.md); el texto del informe está en [`plantilla_informe_visual.md`](../4_Plantillas_y_entrega/plantilla_informe_visual.md) y el cuaderno en [`S13_02`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/2_Practica/S13_02_plantilla_informe_visual.ipynb).

**El cliente.** Marcos, director de TurisData Canarias, tiene 10 minutos y no sabe qué es un AUC. Pide: *«Una página. ¿Puedo fiarme del modelo, qué mueve las cancelaciones y qué hago el lunes?»*
**Qué entregáis (no cambia):** el informe de una página (`informe_visual.md` con el PNG del panel) y el cuaderno que lo genera. **Al final del sprint se suben a `sprint-13/` del repositorio del equipo: 3 ficheros del equipo + 1 autoevaluación y coevaluación por persona** (`autoevaluacion_nombre.md`).
**Tiempo en clase:** 25 min de reto el 25/11, dentro del último día del Sprint 12; luego, entrega y review. **Llegad con el modelo elegido.**

## Tres niveles: el equipo decide hasta dónde llega

| Nivel | Qué hay que tener | Nota* |
|---|---|---|
| 🟢 **Mínimo** (todos los equipos) | Vuestro mejor modelo cargado en la plantilla · costes de los errores escritos · **tres gráficos** (matriz, importancia y ahorro) con título-conclusión, calculados sobre el test · titular-decisión · tres viñetas | 2 |
| 🟡 **Estándar** | Los **cuatro gráficos** honestos (ejes con nombre, barras desde 0, sin 3D) · sin jerga y cifras del texto = cifras del gráfico · pie con datos, modelo, umbral y límites · un riesgo de IA con su medida · cuaderno que se ejecuta de arriba abajo · prueba de los 30 segundos | 3 |
| 🔴 **Extra** | Comparar dos umbrales o modelos · rendimiento por subgrupos (país, canal) · ahorro en euros con una recomendación accionable y sus límites | 4 |

\*Orientativo; puntúa el docente con la rúbrica del curso (0–4 en cada criterio). El mínimo es una entrega válida y evaluable; la «Definition of Done» de la ficha completa describe el nivel **estándar**.

## Reparto sugerido de los 25 minutos

| Min | Qué | Se sabe que está hecho cuando… |
|---|---|---|
| 4 | Elegir el modelo, cargarlo y fijar `COSTE_FN`, `COSTE_FP` y `UMBRAL` | El cuaderno llega al final sin errores |
| 8 | Ajustar los gráficos: un título-conclusión en cada uno | Se genera `informe_visual_panel.png` |
| 8 | Titular, tres viñetas, IA responsable y pie en `informe_visual.md` | Las cifras del texto son las del gráfico |
| 5 | Prueba de los 30 segundos con otro equipo y revisión con la rúbrica | Otro equipo dice vuestra misma decisión |

## Frases para el informe (completad los huecos)

- Titular: «… cada … a las … reservas de mayor riesgo evitaría unas … habitaciones vacías (≈ … €)».
- «Detectamos … de cada 10 cancelaciones; … de cada 10 avisos son falsas alarmas.»
- «Lo que más pesa en una cancelación es …» · «El modelo no debe usarse para …»
- Pie: «Modelo: …; datos: … reservas sintéticas; umbral …; límite: …; responsables: …»

## Antes de entregar
- **Archivos subidos en `sprint-13/`:** `informe_visual.md` · `informe_visual_panel.png` · `informe_visual.ipynb` · `autoevaluacion_nombre.md` (**uno por persona**) = 3 + N ficheros
- [ ] Una página con titular, gráficos con título-conclusión, 3 viñetas y pie · [ ] Cuaderno ejecutado de arriba abajo · [ ] Revisión con la rúbrica anotada
- [ ] Un equipo ajeno entendió la decisión en 30 segundos · [ ] [Autoevaluación y coevaluación](../4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md): **una por persona**, subida a `sprint-13/`
