# Sprint 2 · Reto «¿Nos fiamos de este informe?»

> **Esta es la ficha completa del reto, explicada paso a paso** para quien nunca ha trabajado con esta metodología ni con IA. Léela entera **antes de empezar** y vuelve a ella cuando tengas dudas.
>
> - Si es tu primer reto, lee antes [Cómo se trabaja un reto](../../../material/4.%20Como_se_trabaja_un_reto.md).
> - Volver al [README del sprint](../README.md) · [Guía del sprint en PDF](Guia_Sprint_02.pdf) · [versión ecofriendly para imprimir](Guia_Sprint_02_ecofriendly.pdf).
> - **Este reto en PDF:** [a color](Reto_Sprint_02.pdf) · [ecofriendly, para imprimir](Reto_Sprint_02_ecofriendly.pdf).

## Ficha del reto

### En pocas palabras (léelo primero)

**Qué os pide el cliente.** La dirección de TurisData ha escrito un borrador de informe con **seis afirmaciones** sobre cancelaciones y lo va a presentar al consejo. Os pide que lo reviséis como una persona auditora (revisar el trabajo de otra persona y dar vuestra opinión razonada en un **dictamen**): *«Decidme si nos podemos fiar de cada frase; y si no, cómo debería decirse»*. La afirmación 2 decide a qué canal de venta dar prioridad.

**Va guiado.** No partís de una hoja en blanco: tenéis **8 cartas de error** (con una pregunta para reconocer cada una), **una afirmación resuelta** como modelo, **una plantilla** del dictamen con frases para completar y **fórmulas** para la hoja de cálculo. Vuestro trabajo es reconocer qué carta encaja con cada afirmación, comprobar las cuentas y explicarlo con claridad.

**Qué vais a hacer, en cuatro pasos:**
1. **Entender** las cartas de error y ver juntos la afirmación 1 resuelta.
2. **Comprobar las cuentas** de la afirmación 2 con una hoja de cálculo, siguiendo los pasos.
3. **Resolver** una afirmación más, de la 3 a la 6, cada persona la suya.
4. **Completar el dictamen** con la plantilla y dar una recomendación de tres líneas sobre el canal.

**No se programa:** basta una calculadora o una hoja de cálculo. **Qué aprendéis:** a no creeros una estadística solo porque salga en un informe, porque un modelo entrenado con datos mal interpretados aprende mal.

**Tiempo y reparto.** Unas 2 horas entre el planning, el día 1 y el día 2; el núcleo cabe en 1 h 30 min. **Núcleo:** afirmaciones 1 y 2 (guiadas) y dos más de la 3 a la 6, con la recomendación y el dictamen. **Extra:** las otras dos afirmaciones y los ejercicios que sobren. El alta en Colab y GitHub se hace el día 1, a primera hora (guía en [`alta_cuentas.md`](../actividades/alta_cuentas.md)).

### Qué tenéis que entregar
1. **Dictamen de auditoría** (1-2 páginas en `.md` o PDF, con la [plantilla](../plantillas/plantilla_dictamen.md)) con **al menos cuatro de las seis afirmaciones** (la 1, la 2 y dos más): la **carta** (nombre del error), el **veredicto** (*fiable · parcialmente fiable · no fiable · no se puede saber*), el **cálculo rehecho** si hay datos, **cómo debería decirse** y **qué datos faltan**.
2. **Recomendación de tres líneas** sobre el canal (afirmación 2), con una cautela, y **una frase de IA responsable**.
3. **La hoja de ejercicios**, con el **mínimo básico**: M1, M2 y M7 (hoja 1) y E1, E2, E6, E8 y E10 (hoja 2).

**Datos:** [`informe_cliente.md`](../../../datos/informe_cliente.md) (las seis afirmaciones) e [`informe_cliente.csv`](../../../datos/informe_cliente.csv) (2.400 reservas por `tarifa` y `canal`, 4 filas), en la carpeta [`datos/`](../../../datos/) del repositorio. No hace falta Python.

**Reglas:** cada cifra debe poder rehacerse con los datos; si no hay datos, no inventéis números y decid qué faltaría; si usáis IA, declarad dónde y comprobad a mano las afirmaciones 2 y 6.

### Criterios de evaluación
Cada entregable se evalúa de 0 a 4 en los cuatro criterios de la rúbrica de retos.

| Criterio | 1 · Insuficiente | 2 · Suficiente | 3 · Bueno | 4 · Excelente |
|---|---|---|---|---|
| **Corrección técnica** | Las cuentas de las afirmaciones 1 y 2 son erróneas o no se ha detectado el problema de la 2 | Las tasas de las afirmaciones 1 y 2 están bien y hay veredicto razonable en 4 afirmaciones | Además se ve que la intermediaria cancela más **dentro de cada tarifa** (Simpson) y cada error lleva su carta correcta | Además se resuelven las seis o se razona cuándo una diferencia sería real (p. ej. por una muestra pequeña) |
| **Reproducibilidad** | No se ve de dónde salen las cifras | Las cifras llevan su operación (cancelaciones ÷ reservas) | Hay una tabla por tarifa y canal con reservas, cancelaciones y tasa | Además se adjunta la hoja de cálculo |
| **Análisis y comunicación al cliente** | Solo dice "está mal" | Explica el error con la frase de la carta | Explica con lenguaje claro y propone una frase corregida en cada afirmación | Además la recomendación sobre el canal tiene cautelas y datos a pedir |
| **IA responsable** | No se considera | Menciona "cuidado con los sesgos" | Una frase que dice qué aprendería un modelo entrenado con datos así | Además propone una comprobación concreta antes de usar esos datos |

### Guía paso a paso para principiantes

#### Paso 1 · Planning (10 minutos)
1. Leed el informe ([`informe_cliente.md`](../../../datos/informe_cliente.md)) **en voz alta**.
2. **La 1 y la 2 las hacéis todos juntos**, con el docente. De la **3 a la 6**, cada persona elige una (si sois menos, algunas hacen dos).
3. Abrid [`informe_cliente.csv`](../../../datos/informe_cliente.csv) en una hoja de cálculo: solo 4 filas (`tarifa`, `canal`, `reservas`, `cancelaciones`).
4. Copiad la [plantilla del dictamen](../plantillas/plantilla_dictamen.md) a `sprint-02/` de vuestro repositorio.

#### Paso 2 · Las cartas de error y un ejemplo resuelto (día 1, 15 minutos)

Cada afirmación tiene **un problema distinto**. Estas son las cartas entre las que elegir. **Ojo: solo se usan 6**; las dos últimas son trampas que no encajan con ninguna afirmación.

| Carta | Cómo se reconoce (la pregunta) | Frase para el dictamen |
|---|---|---|
| **1. Comparación sin fuente** | ¿Con qué se compara? ¿Hay algún dato que lo respalde? | «Se compara con ……, pero no hay ningún dato que lo respalde.» |
| **2. Paradoja de Simpson** | Si separo por grupos, ¿cambia el resultado? | «En el total gana ……, pero dentro de cada grupo ocurre lo contrario, porque ……» |
| **3. Muestra pequeña** | ¿Cuántos datos hay? ¿De qué momento? | «Solo hay …… datos, de ……; es poco para sacar una conclusión.» |
| **4. Muestra sesgada** | ¿Quién ha respondido y quién falta? | «Solo ha respondido ……; faltan ……, así que no representa a todos.» |
| **5. Correlación no es causa** | ¿Hay una tercera cosa que explique las dos? | «Que …… y …… suban a la vez no prueba que una cause la otra; puede influir ……» |
| **6. Base de comparación distinta** | ¿Se comparan cosas iguales (mismos días, misma situación)? | «Se comparan …… y ……, que no son equivalentes porque ……» |
| 7. Eje truncado *(trampa)* | ¿Hay un gráfico con el eje cortado? | — |
| 8. Sesgo de supervivencia *(trampa)* | ¿Solo se mira a quien «llegó hasta el final»? | — |

**Veredictos:** *fiable* (cuenta y conclusión bien) · *parcialmente fiable* (la cuenta sale, la conclusión no se sigue) · *no fiable* · *no se puede saber* (faltan datos; es una respuesta válida y honrada, no inventéis números).

**Ejemplo resuelto, con el docente: la afirmación 1.** Así debe quedar cada bloque del dictamen:

> **Afirmación 1:** «La tasa de cancelación global es del 21 %, así que estamos en la media del sector».
>
> - **Carta:** 1 · Comparación sin fuente.
> - **Veredicto:** parcialmente fiable.
> - **Por qué:** la cuenta sale, pero «la media del sector» no aparece en ningún dato.
> - **Cálculo:** cancelaciones 300 + 70 + 20 + 120 = 510; reservas 1000 + 200 + 200 + 1000 = 2400; tasa = 510 ÷ 2400 × 100 = **21,25 %**.
> - **Cómo debería decirse:** «Nuestra tasa global de cancelación es del 21,25 % (510 de 2.400 reservas). No tenemos datos del sector para compararla».
> - **Qué datos faltan:** la tasa media del sector, con su fuente y su periodo.

#### Paso 3 · La afirmación 2, paso a paso (día 1, 25 minutos)

El informe dice que la web intermediaria cancela **menos** (15,8 %) que el canal directo (26,7 %) y que por eso conviene priorizarla. Lo comprobamos con la hoja de cálculo.

**La tasa** de cancelación es cuántas cancelaciones hay por cada 100 reservas: cancelaciones ÷ reservas × 100.

**3.1 Preparad la hoja.** Datos en las columnas A–D, filas 2 a 5, en este orden: `flexible/directo`, `flexible/intermediaria`, `no_reembolsable/directo`, `no_reembolsable/intermediaria`. En la columna E, la tasa de cada fila: `=D2/C2` (arrastrad hasta la fila 5) en formato porcentaje.

**3.2 Comprobad las cifras del informe** (si vuestro programa usa `;` o `,` en las fórmulas, usad el que os pida):

| Qué calculáis | Fórmula |
|---|---|
| Tasa del canal **directo** (total) | `=(D2+D4)/(C2+C4)` |
| Tasa del canal **intermediaria** (total) | `=(D3+D5)/(C3+C5)` |

¿Coinciden con 26,7 % y 15,8 %? **Sí: la cuenta está bien.** Entonces, ¿dónde está el problema? Probad las pistas **de una en una**:

- **Pista 1.** El informe solo mira el total. Comparad los canales **dentro de cada tarifa** (columna E: filas 2 y 3, y filas 4 y 5).
- **Pista 2.** ¿Qué parte de las reservas de cada canal es tarifa flexible? Directo `=C2/(C2+C4)`, intermediaria `=C3/(C3+C5)`.
- **Pista 3.** La tarifa flexible se cancela mucho más que la no reembolsable. ¿Cuál vende sobre todo cada canal?

**Comprobad vuestras cifras** (después de calcular): flexible, directo 30 % e intermediaria 35 %; no reembolsable, directo 10 % e intermediaria 12 %.

**3.3 Completad la explicación** con *flexible · no reembolsable · mucho · poco · peor · mejor*:

> Dentro de cada tarifa, la intermediaria cancela …… que el directo. En el total parece …… porque vende sobre todo tarifa ……, que se cancela ……

**3.4 Elegid la carta** (la que dice «si separo por grupos, cambia el resultado») y **escribid la recomendación de tres líneas**: «*Recomendamos …… (priorizar la intermediaria / no priorizarla / seguir mirando), porque …… Antes de decidir habría que mirar ……*» (por ejemplo, el coste o el margen de cada canal).

#### Paso 4 · Vuestra afirmación (día 1, 20 minutos)

Cada persona resuelve la que eligió (de la 3 a la 6) con esta receta, de arriba abajo: **copiad la frase** del informe → **elegid la carta** (las preguntas de la tabla os ayudan) → **elegid el veredicto** → **completad la frase** de la carta → **escribid cómo debería decirse** en una frase → **escribid qué datos faltan**.

Para la **afirmación 6** hay una cuenta: ¿sale la bajada del 25 %? `(30 − 40) ÷ 40`. Y después: ¿se pueden comparar un mes de 28 días de baja ocupación con otro de 31 días de alta ocupación? Las demás no necesitan cuentas: mirad **qué se compara y quién falta**.

#### Paso 5 · Dictamen y entrega (día 2, 55 minutos)

1. **Completar (20 min):** la afirmación 2 con su tabla (por tarifa y canal) y la recomendación; vuestras afirmaciones.
2. **Una frase de IA responsable (5 min)**, al final del dictamen: «*Si entrenáramos un modelo con ……, aprendería ……, porque ……*». Ejemplo inventado: «Si entrenáramos un modelo con las reseñas de quien se anima a escribir, aprendería solo la opinión de los extremos, porque las personas medianamente satisfechas casi no escriben».
3. **Revisión cruzada (15 min):** intercambiad el dictamen con otra persona y comprobad que cada bloque tiene carta, veredicto, frase corregida y cuenta (si la hay).
4. **Entrega (15 min):** subid a `sprint-02/`, actualizad el tablero, rellenad la autoevaluación y repasad la Definition of Done.

**Si os atascáis:** contestad con vuestra afirmación la pregunta de la carta, o formulad la frase de otra manera (con números absolutos, con otra base) y mirad si la conclusión cambia. Si los números no cuadran, revisad que dividís por las reservas **del grupo**, no por el total. Más ayuda: [Cómo se trabaja un reto](../../../material/4.%20Como_se_trabaja_un_reto.md).

### Cómo usar la IA en este reto

La IA sirve para **entender y redactar**, no para calcular: muchas se equivocan en porcentajes y lo hacen con mucha seguridad. Podéis pedirle, por ejemplo, «explícame la paradoja de Simpson con un ejemplo de un hotel, sin fórmulas» o «reescribe esta frase para que la entienda una directora; no cambies las cifras» (y comprobad que **las cifras siguen siendo las mismas**).

**Una sola regla:** si la IA os hace un cálculo, **comprobadlo a mano** (afirmaciones 2 y 6) y escribid en el dictamen **dónde la habéis usado**. Nunca peguéis datos personales reales.

### Errores frecuentes (y cómo evitarlos)

| Error | Cómo evitarlo |
|---|---|
| Decir solo «está mal» | Cada bloque lleva **carta, veredicto y frase corregida** |
| Dar por buena una cuenta sin rehacerla | Rehaced las cifras con los datos, también las que parecen obvias |
| Mirar solo el total | Separad por tarifa y canal; comparad dentro de cada grupo |
| Dividir por el total equivocado | La tasa es cancelaciones ÷ reservas **del mismo grupo** |
| Inventar números cuando no hay datos | Decid «no se puede saber» y qué datos faltan |

### Qué se enseña en la review (2 min por persona)
- **Cada persona** presenta **una afirmación**: su carta, su veredicto y por qué, y la frase corregida.
- **El equipo** enseña la tabla de la afirmación 2 y la recomendación de tres líneas.
- Una cosa que os costó ver.

## Definition of Done (lista de comprobación)

Si queda una casilla sin marcar, **el reto no está terminado**.

- [ ] Dictamen con **al menos 4 afirmaciones** (la 1, la 2 y dos más), cada una con su **carta**, su veredicto y una frase corregida
- [ ] Cálculos rehechos y visibles (afirmaciones 1 y 2, y la 6 si la hacéis) y tabla de la 2 por tarifa y canal
- [ ] Recomendación de tres líneas con una cautela y una frase de **IA responsable**
- [ ] Hoja de ejercicios con el mínimo básico (M1, M2, M7, E1, E2, E6, E8, E10)
- [ ] Revisión cruzada, subido a Git, tablero actualizado, autoevaluación y coevaluación
- [ ] Alta en Colab y GitHub hecha (día 1, en clase)
