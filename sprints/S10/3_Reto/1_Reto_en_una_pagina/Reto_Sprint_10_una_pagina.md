# Sprint 10 · Reto «¿Vale la pena la red?» · en una página

> Versión corta para **trabajar con ella abierta**. La ficha completa (recursos, rúbrica, guía paso a paso, uso de la IA y errores frecuentes) sigue en [Reto_Sprint_10.md](../2_Ficha_completa/Reto_Sprint_10.md). Se hace con el cuaderno [`S10_04`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/2_Practica/S10_04_reto_vale_la_pena.ipynb) y los datos [`reservas_turisdata.csv`](../../../../datos/reservas_turisdata.csv).

**El cliente.** La dirección de TurisData oye hablar de redes neuronales y pregunta si debe **sustituir su modelo de cancelaciones por una red**. Quiere evidencias con el coste incluido. **«No compensa» es una respuesta tan válida como «sí».**
**Qué entregáis (no cambia):** el cuaderno ejecutado, un informe comparativo de 1–2 páginas *ML clásico frente a MLP* y el README del sprint. **Al final del sprint se suben a `sprint-10/` del repositorio del equipo: 3 ficheros del equipo (esos tres) + 1 autoevaluación y coevaluación por persona** (`autoevaluacion_nombre.md`).
**Tiempo en clase:** planning 10 min (día 1) · reto unos 90 min (día 2; los seis pasos suman 145) y 15 para poneros al día · entrega, review y retro 40 min. Los 40 min que faltan, en la consolidación y la 6.ª hora (subida hasta las 14:30); lo demás, a casa.

## Tres niveles: el equipo decide hasta dónde llega

| Nivel | Qué hay que tener | Nota* |
|---|---|---|
| 🟢 **Mínimo** (todos los equipos) | Cuaderno que se ejecuta de arriba abajo con semillas fijas · una partición única entrenamiento/validación/prueba · referencia (boosting) y **un MLP** con las mismas métricas · curva de aprendizaje y una frase de diagnóstico · prueba usada **una sola vez** · recomendación en una frase · README | 2 |
| 🟡 **Estándar** | **2–3 variantes** del MLP elegidas **mirando solo la validación** · **varias semillas** con media ± desviación (¿diferencia real o ruido?) · informe con recomendación, coste y límites · dos riesgos de IA responsable | 3 |
| 🔴 **Extra** | Variante de regresión (precio por noche) · comparar el coste de entrenar y mantener cada modelo · guardar el modelo y probarlo recargado | 4 |

\*Orientativo; puntúa el docente con la rúbrica del curso (0–4 en cada criterio). El mínimo es una entrega válida y evaluable; la rúbrica de la ficha completa describe el nivel **estándar**.

## Reparto sugerido de los 145 minutos

| Min | Qué | Se sabe que está hecho cuando… |
|---|---|---|
| 15 | Elegir el problema, ejecutar `S10_04` y reproducir la referencia | Hay AUC y tiempo del boosting, y el ejercicio 1 pasa |
| 25 | Primera red: escalar sin fugas, entrenar el MLP, dibujar la curva | Hay curva y el ejercicio 2 pasa |
| 25 | 2–3 variantes, comparadas **solo con la validación** | Hay tabla de variantes y una elegida |
| 20 | Leer las curvas y diagnosticar el sobreajuste | El ejercicio 3 pasa y hay una frase de diagnóstico |
| 25 | Comparación justa: semillas, prueba una vez y coste | El ejercicio 4 pasa y hay media ± desviación |
| 35 | Informe, README, revisión con la rúbrica y subida | Otra persona podría repetirlo con el README |

## Frases para el informe (completad los huecos)

- «Con el mismo conjunto de datos, el boosting obtiene un AUC de … ± … y la red … ± …. La diferencia (es / no es) mayor que el ruido entre semillas.»
- «La red (mejora / no mejora) al modelo clásico, y cuesta … (tiempo de entrenamiento, ajuste, explicabilidad).»
- «Recomendamos … porque … Solo cambiaría si …» · «Riesgos: … Medidas: …»

## Antes de entregar
- **Archivos subidos en `sprint-10/`:** `reto_vale_la_pena.ipynb` · `informe_comparativo.md` · `README.md` · `autoevaluacion_nombre.md` (**uno por persona**) = 3 + N ficheros
- [ ] Cuaderno ejecutado de arriba abajo, con semillas fijas · [ ] La prueba se ha usado una sola vez · [ ] Informe con recomendación, coste, límites y dos riesgos
- [ ] Sección «Revisión con la rúbrica» al final del informe · [ ] [Autoevaluación y coevaluación](../4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md): **una por persona**, subida a `sprint-10/`
