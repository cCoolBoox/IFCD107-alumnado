# Sprint 5 · Reto «¿La ocupación depende de esto?» · en una página

> Versión corta para **trabajar con ella abierta**. La ficha completa sigue en [Reto_Sprint_05.md](Reto_Sprint_05.md). Todo se hace dentro del cuaderno [`S05_07_reto_ocupacion`](../notebooks/S05_07_reto_ocupacion.ipynb), que lleva comprobaciones automáticas (`assert`).

**El cliente.** Al dueño le han dicho que «con calor se llena menos» y que «los festivos llenan». Quiere saber **cuánto** cambia la ocupación diaria y **con qué seguridad** se puede afirmar. Tres años de datos diarios.
**Qué entregáis (no cambia):** el cuaderno completo, la base de datos `turisdata_reto.db` y una **respuesta al cliente de 150 palabras como máximo**.
**Tiempo en clase:** planning 10 min · reto 45 min · entrega, review y retro 40 min. El resto del cuaderno, en casa.

## Tres niveles: el equipo decide hasta dónde llega

| Nivel | Qué hay que tener | Nota* |
|---|---|---|
| 🟢 **Mínimo** (todos los equipos) | `turisdata_reto.db` con la tabla `ocupacion_diaria` (1096 filas) leída con SQL · un vistazo a los datos con un gráfico · regresión **simple** desde cero con descenso del gradiente y su curva de aprendizaje · respuesta al cliente con **una cifra y su intervalo de confianza** | 2 |
| 🟡 **Estándar** | Modelo **con control** (festivo y mes) · comparación con `statsmodels` (coinciden) · p-valor, intervalo y tamaño del efecto **interpretados con palabras** · la respuesta incluye recomendación y límites | 3 |
| 🔴 **Extra** | Explicar con el control por mes por qué **correlación no es causalidad** · comparar varias tasas de aprendizaje · gráficos cuidados con título y ejes en español | 4 |

\*Orientativo; puntúa el docente con la rúbrica del curso (0–4 en cada criterio). El mínimo es una entrega válida y evaluable; la «Definition of Done» de la ficha completa describe el nivel **estándar**.

## Frases para la respuesta al cliente (150 palabras)

> «Con los datos de tres años, por cada grado más de temperatura la ocupación … (intervalo de confianza: … a …), una vez descontados …. Los festivos … Recomendamos … No podemos afirmar que … porque … Los datos son sintéticos y de …: no deben generalizarse.»

Una buena respuesta tiene siempre: **cifra con incertidumbre · recomendación concreta · límites explícitos**.

## Si vais justos de tiempo
Cargar la base de datos es la práctica de CRUD (`S05_06`): si ya la hicisteis, copiad el código. Lo que no entre en clase es el nivel estándar y el extra, en casa.

## Antes de entregar
- [ ] Todos los `assert` del cuaderno pasan · [ ] Reiniciar y ejecutar todo funciona sin errores
- [ ] La respuesta tiene cifra, recomendación y límites (≤ 150 palabras) · [ ] [Autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md) rellenadas
