# Sprint 5 · Reto «¿La ocupación depende de esto?» · en una página

> Versión corta para **trabajar con ella abierta**. La ficha completa (recursos, rúbrica, guía paso a paso, uso de la IA y errores frecuentes) sigue en [Reto_Sprint_05.md](../2_Ficha_completa/Reto_Sprint_05.md). Todo se hace dentro del cuaderno [`S05_07_reto_ocupacion`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_07_reto_ocupacion.ipynb), que lleva puntos de control (`assert`); los datos: [`ocupacion_diaria.csv`](../../../../datos/ocupacion_diaria.csv).

**El cliente.** Al dueño de TurisData le han dicho que «con calor se llena menos» y que «los festivos llenan». Quiere saber **cuánto** cambia la ocupación diaria y **con qué seguridad** se puede afirmar. Tres años de datos diarios.
**Qué entregáis (no cambia):** el cuaderno completo, la base de datos `turisdata_reto.db` y, dentro del cuaderno, una **respuesta al cliente de 150 palabras como máximo**. **Al final del sprint se suben a `sprint-05/` del repositorio del equipo: 2 ficheros del equipo (cuaderno y base de datos) + 1 autoevaluación y coevaluación por persona** (`autoevaluacion_nombre.md`).
**Tiempo en clase:** planning 10 min (día 1) · día 2: CRUD (paso 1) y reto 45 min · entrega, review y retro 40 min. Los 35 min que faltan, en la consolidación y la 6.ª hora (subida hasta las 14:30); lo demás, a casa.

## Tres niveles: el equipo decide hasta dónde llega

| Nivel | Qué hay que tener | Nota* |
|---|---|---|
| 🟢 **Mínimo** (todos los equipos) | `turisdata_reto.db` con la tabla `ocupacion_diaria` (1096 filas) leída con SQL · un vistazo a los datos con dos gráficos · regresión **simple** desde cero con descenso del gradiente y su curva de aprendizaje · respuesta con **una cifra y su intervalo de confianza** · celda «Uso de IA» | 2 |
| 🟡 **Estándar** | Modelo **con control** (festivo y mes) · comparación con `statsmodels` (coinciden) · p-valor, intervalo y tamaño del efecto **explicados con palabras** · respuesta con recomendación y límites · «Reiniciar y ejecutar todo» sin errores · revisión con la rúbrica | 3 |
| 🔴 **Extra** | Explicar con el control por mes por qué **correlación no es causalidad** · comparar varias tasas de aprendizaje · gráficos cuidados | 4 |

\*Orientativo; puntúa el docente con la rúbrica del curso (0–4 en cada criterio). El mínimo es una entrega válida y evaluable; la «Definition of Done» de la ficha completa describe el nivel **estándar**.

## Reparto sugerido de los 105 minutos

| Min | Qué | Se sabe que está hecho cuando… |
|---|---|---|
| 30 | Paso 1: base de datos `turisdata_reto.db` y lectura con SQL (es la práctica de CRUD) | Punto de control 1 superado |
| 10 | Paso 2: mirar los datos con dos gráficos y 2–3 observaciones | Los gráficos tienen título y ejes en español |
| 35 | Paso 3: `gradiente_mse` y `entrenar`, modelo simple, curva y modelo con control | Punto de control 2 superado |
| 10 | Paso 4: comparar con `statsmodels` | Punto de control 3 superado |
| 10 | Paso 5: p-valor, intervalo y tamaño del efecto, con palabras | Punto de control 4 superado |
| 10 | Paso 6: respuesta al cliente, reiniciar y ejecutar todo, revisión con la rúbrica | Todo corre sin errores y la revisión está anotada |

## Frases para la respuesta al cliente (150 palabras)

> «Con los datos de tres años, por cada grado más de temperatura la ocupación … (intervalo de confianza: … a …), una vez descontados …. Los festivos … Recomendamos … No podemos afirmar que … porque … Los datos son sintéticos y de …: no deben generalizarse. El modelo no debería usarse para … sin ….»

Una buena respuesta tiene siempre: **cifra con incertidumbre · recomendación concreta · límites explícitos · una cautela de IA responsable**. Todas las cifras salen de vuestro cuaderno.

## Antes de entregar
- **Archivos subidos en `sprint-05/`:** `S05_07_reto_ocupacion.ipynb` · `turisdata_reto.db` · `autoevaluacion_nombre.md` (**uno por persona**) = 2 + N ficheros
- [ ] Los cuatro puntos de control pasan y *Reiniciar y ejecutar todo* funciona sin errores · [ ] La respuesta tiene cifra, recomendación y límites (≤ 150 palabras)
- [ ] Celdas finales «Uso de IA» y «Revisión con la rúbrica» rellenas · [ ] Subido por personas distintas (varios *commits*)
- [ ] [Autoevaluación y coevaluación](../4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md): **una por persona**, subida a `sprint-05/`
