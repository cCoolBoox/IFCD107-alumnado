# Sprint 2 · Reto «¿Nos fiamos de este informe?»

> **Esta es la ficha completa del reto, explicada paso a paso** para quien nunca ha trabajado con esta metodología ni con IA. Léela entera **antes de empezar** y vuelve a ella cuando tengas dudas.
>
> - Si es tu primer reto, lee antes [Cómo se trabaja un reto](../../../material/4.%20Como_se_trabaja_un_reto.md).
> - Volver al [README del sprint](../README.md) · [Guía del sprint en PDF](Guia_Sprint_02.pdf) · [versión ecofriendly para imprimir](Guia_Sprint_02_ecofriendly.pdf).
> - **Este reto en PDF:** [a color](Reto_Sprint_02.pdf) · [ecofriendly, para imprimir](Reto_Sprint_02_ecofriendly.pdf).

## Ficha del reto

### En pocas palabras (léelo primero)

**Qué os pide el cliente.** La dirección de TurisData ha escrito un borrador de informe con **seis afirmaciones** sobre cancelaciones y lo va a presentar al consejo. Antes, os pide que lo reviséis como lo haría una persona auditora: *«Decidme si nos podemos fiar de cada frase; y si no, cómo debería decirse»*. Una de las afirmaciones (la 2) influye en una decisión importante: a qué canal de venta dar prioridad.

**Esta versión del reto va guiada.** No partís de una hoja en blanco: tenéis **6 «cartas de error»** (los errores posibles, con una pregunta para reconocerlos), **una afirmación resuelta** como modelo, **una plantilla** del dictamen con frases para completar y **fórmulas** para la hoja de cálculo. Vuestro trabajo es **reconocer qué carta encaja con cada afirmación, comprobar las cuentas y explicarlo con claridad**.

**Qué vais a hacer, en cuatro pasos:**
1. **Entender** las cartas de error y ver juntos una afirmación resuelta (la 1).
2. **Comprobar las cuentas** de la afirmación 2 con una hoja de cálculo, siguiendo los pasos.
3. **Elegir y resolver** al menos dos afirmaciones más (de la 3 a la 6), una por persona.
4. **Completar el dictamen** con la plantilla y dar una recomendación de tres líneas sobre el canal.

**No se programa.** Basta una calculadora o una hoja de cálculo (Excel, Calc, Google Sheets).

**Qué vais a entregar:** un **dictamen de 1–2 páginas** (con la [plantilla](../plantillas/plantilla_dictamen.md)), la recomendación sobre el canal y la hoja de ejercicios con el **mínimo básico**: ★ de cada hoja más E8 y E10 (lo dice el README del sprint).

**Qué vais a aprender haciéndolo:** a **no creerse una estadística solo porque salga en un informe**. Es la habilidad más útil antes de entrenar cualquier modelo, porque **un modelo entrenado con datos mal interpretados aprende mal**.

**Cuánto tiempo:** unas 2 horas repartidas entre el planning, la primera sesión (jueves) y la segunda (viernes), con margen: **el núcleo cabe en 1 h 30 min**. La cuenta de Colab y GitHub se da de alta **en la primera sesión, a primera hora, en clase** (guía en [`alta_cuentas.md`](../actividades/alta_cuentas.md)).

**Núcleo y extra.** Núcleo: las afirmaciones **1 y 2** (guiadas) y **dos más** de la 3 a la 6 (4 de 6 en total), la recomendación y el dictamen. Extra: las otras dos afirmaciones, la lista de datos que faltan y los ejercicios que sobren.

### Palabras que van a aparecer en este reto

| Palabra | Qué significa, en sencillo |
|---|---|
| **Auditar** | Revisar el trabajo de otra persona para comprobar si es correcto |
| **Dictamen** | El documento donde dais vuestra opinión razonada («veredicto») |
| **Tasa** | Cuántas cancelaciones hay por cada 100 reservas |
| **Muestra** | Un trozo pequeño de los datos con el que se pretende hablar de todo |
| **Correlación** | Dos cosas que suben o bajan a la vez. **No significa que una cause la otra** |
| **Paradoja de Simpson** | Un resultado que parece cierto al mirar el total, pero se invierte al separar por grupos |
| **Base de comparación** | Aquello con lo que se compara. Si la base es distinta, la comparación no es justa |

### Escena del cliente
La dirección de *TurisData Canarias* ha preparado un **borrador de informe** sobre cancelaciones para presentarlo al consejo. Antes de hacerlo, la directora os lo pasa: *"Un cliente del consejo me dijo que hay que revisar estos números con ojo crítico. Decidme **si nos podemos fiar de cada afirmación**, y si no, qué debemos decir en su lugar. Y cuidado: la decisión de a qué canal dar prioridad depende de esto."*

### Qué tenéis que entregar
1. **Dictamen de auditoría** (1-2 páginas en `.md` o PDF, con la [plantilla](../plantillas/plantilla_dictamen.md)): para **al menos cuatro de las seis afirmaciones** (la 1, la 2 y dos más de la 3 a la 6), indicad:
   - **La carta** (el nombre del error) y el **veredicto**: *fiable · parcialmente fiable · no fiable · no se puede saber*.
   - **El cálculo rehecho**, cuando haya datos.
   - **Cómo debería decirse** (una frase corregida) y **qué datos faltan**.
2. **Recomendación de tres líneas** para la dirección sobre el canal (afirmación 2), con una cautela.
3. **Una frase de IA responsable**: qué pasaría si entrenáramos un modelo con datos así.
4. **La hoja de ejercicios**, con el **mínimo básico**: M1, M2 y M7 (hoja 1) y E1, E2, E6, E8 y E10 (hoja 2).

### Datos y recursos
- **[`informe_cliente.md`](../../../datos/informe_cliente.md)** (carpeta [`datos/`](../../../datos/) del repositorio): el borrador del informe con las seis afirmaciones.
- **[`informe_cliente.csv`](../../../datos/informe_cliente.csv)** (carpeta [`datos/`](../../../datos/) del repositorio): datos de **2.400 reservas**, agrupadas por `tarifa` y `canal`, con columnas `reservas` y `cancelaciones`. El archivo tiene 4 filas (una por combinación de tarifa y canal).
- La [plantilla del dictamen](../plantillas/plantilla_dictamen.md), las cartas de error de este reto y una calculadora u hoja de cálculo. **No hace falta Python.** Si queréis profundizar, la lista de control de [`estadisticas_enganosas.md`](../actividades/estadisticas_enganosas.md).

### Restricciones
- **Tiempo:** unas 2 h de reto repartidas en dos sesiones (el núcleo cabe en 1 h 30 min), más la review.
- **Extensión:** 1-2 páginas.
- Cada cifra que aparezca en el dictamen debe poder **rehacerse** con los datos entregados (reproducibilidad).
- Cuando no haya datos para comprobar una afirmación, **no inventéis números**: decid qué datos harían falta.
- Si usáis un asistente de IA, **declarad dónde** y **comprobad** a mano los cálculos de las afirmaciones 2 y 6.

### Criterios de evaluación
Cada entregable se evalúa de 0 a 4 en los cuatro criterios de la rúbrica de retos.

| Criterio | 1 · Insuficiente | 2 · Suficiente | 3 · Bueno | 4 · Excelente |
|---|---|---|---|---|
| **Corrección técnica** | Las cuentas de las afirmaciones 1 y 2 son erróneas o no se ha detectado el problema de la 2 | Las tasas de las afirmaciones 1 y 2 están bien y hay veredicto razonable en 4 afirmaciones | Además se ve que la intermediaria cancela más **dentro de cada tarifa** (Simpson) y cada error lleva su carta correcta | Además se resuelven las seis o se razona cuándo una diferencia sería real (p. ej. por una muestra pequeña) |
| **Reproducibilidad** | No se ve de dónde salen las cifras | Las cifras llevan su operación (cancelaciones ÷ reservas) | Hay una tabla por tarifa y canal con reservas, cancelaciones y tasa | Además se adjunta la hoja de cálculo |
| **Análisis y comunicación al cliente** | Solo dice "está mal" | Explica el error con la frase de la carta | Explica con lenguaje claro y propone una frase corregida en cada afirmación | Además la recomendación sobre el canal tiene cautelas y datos a pedir |
| **IA responsable** | No se considera | Menciona "cuidado con los sesgos" | Una frase que dice qué aprendería un modelo entrenado con datos así | Además propone una comprobación concreta antes de usar esos datos |

### Pasos sugeridos (unas 2 h de reto)

| Momento | Qué hacer |
|---|---|
| **Planning (10 min)** | Leed el informe, repartid las afirmaciones 3 a 6 y copiad la plantilla |
| **Primera sesión (60 min)** | Cartas de error y afirmación 1 resuelta (15 min) · afirmación 2 paso a paso con la hoja de cálculo (25 min) · vuestra afirmación (20 min) |
| **Segunda sesión (55 min)** | Completar el dictamen y la recomendación (20 min) · frase de IA responsable (5 min) · revisión cruzada (15 min) · entrega y DoD (15 min) |
| **Cierre** | Review (2 min por persona) y retro |

### Pistas (sin destriparlo)
- Empezad siempre por **la cuenta**: ¿las cifras del informe salen de los datos?
- Una cuenta puede salir bien y la **conclusión** estar mal.
- En la afirmación 2, comparad **dentro de cada tarifa**, no solo el total.
- Si no encontráis la carta, contestad su pregunta con vuestra afirmación.

### Guía paso a paso para principiantes

#### Paso 1 · Planning (10 minutos, antes de empezar)
1. Leed el informe ([`informe_cliente.md`](../../../datos/informe_cliente.md)) **en voz alta**, afirmación por afirmación.
2. Repartíos las afirmaciones: **la 1 y la 2 las hacéis todos juntos** (con el docente). De la **3 a la 6**, cada persona elige **una** (si sois cuatro, una cada una; si sois menos, algunas hacen dos).
3. Abrid [`informe_cliente.csv`](../../../datos/informe_cliente.csv) en una hoja de cálculo. Son solo **4 filas**, con cuatro columnas: `tarifa`, `canal`, `reservas` y `cancelaciones`.
4. Copiad la [plantilla del dictamen](../plantillas/plantilla_dictamen.md) a `sprint-02/` de vuestro repositorio.

#### Paso 2 · Las cartas de error y un ejemplo resuelto (primera sesión, 15 minutos)

Cada afirmación del informe tiene **un problema distinto**. Estas son las **cartas** entre las que elegir. **Ojo: hay 8 cartas y solo 6 se usan**; las dos últimas son «trampas» que no encajan con ninguna afirmación.

| Carta | Cómo se reconoce (la pregunta) | Frase para el dictamen |
|---|---|---|
| **1. Comparación sin fuente** | ¿Con qué se compara? ¿Hay algún dato que lo respalde? | «Se compara con ……, pero no hay ningún dato que lo respalde.» |
| **2. Paradoja de Simpson** | Si separo por grupos, ¿cambia el resultado? | «En el total gana ……, pero dentro de cada grupo ocurre lo contrario, porque …….» |
| **3. Muestra pequeña** | ¿Cuántos datos hay? ¿De qué momento? | «Solo hay …… datos, de ……; es poco para sacar una conclusión.» |
| **4. Muestra sesgada** | ¿Quién ha respondido y quién falta? | «Solo ha respondido ……; faltan ……, así que no representa a todos.» |
| **5. Correlación no es causa** | ¿Hay una tercera cosa que explique las dos? | «Que …… y …… suban a la vez no prueba que una cause la otra; puede influir …….» |
| **6. Base de comparación distinta** | ¿Se comparan cosas iguales (mismos días, misma situación)? | «Se comparan …… y ……, que no son equivalentes porque …….» |
| 7. Eje truncado *(trampa)* | ¿Hay un gráfico con el eje cortado? | — |
| 8. Sesgo de supervivencia *(trampa)* | ¿Solo se mira a quien «llegó hasta el final»? | — |

**Veredictos posibles** (elegid uno por afirmación):
- **Fiable:** la cuenta y la conclusión están bien.
- **Parcialmente fiable:** la cuenta sale, pero la conclusión no se sigue de ella.
- **No fiable:** la cuenta o la conclusión fallan.
- **No se puede saber:** faltan datos para comprobarlo. **Es una respuesta válida y honrada**: no inventéis números.

**Ejemplo resuelto, con el docente: la afirmación 1.** Así debe quedar **cada** bloque del dictamen:

> **Afirmación 1:** «La tasa de cancelación global es del 21 %, así que estamos en la media del sector».
>
> - **Carta:** 1 · Comparación sin fuente.
> - **Veredicto:** parcialmente fiable.
> - **Por qué:** la cuenta sale, pero «la media del sector» no aparece en ningún dato. Se compara con algo que no podemos comprobar.
> - **Cálculo:** cancelaciones 300 + 70 + 20 + 120 = 510. Reservas 1000 + 200 + 200 + 1000 = 2400. Tasa = 510 ÷ 2400 × 100 = **21,25 %**.
> - **Cómo debería decirse:** «Nuestra tasa global de cancelación es del 21,25 % (510 de 2.400 reservas). No tenemos datos del sector para compararla».
> - **Qué datos faltan:** la tasa media del sector, con su fuente y su periodo.

#### Paso 3 · La afirmación 2, paso a paso (primera sesión, 25 minutos)

Es la afirmación importante: el informe dice que la web intermediaria cancela **menos** (15,8 %) que el canal directo (26,7 %) y que por eso conviene priorizarla. **Vamos a comprobarlo con la hoja de cálculo.**

**3.1 Preparad la hoja.** Poned los datos en las columnas A–D (de la fila 2 a la 5), en este orden: `flexible/directo`, `flexible/intermediaria`, `no_reembolsable/directo`, `no_reembolsable/intermediaria`. En la columna E, la **tasa de cada fila**: `=D2/C2` (y arrastrad hasta la fila 5). Dadle formato de porcentaje.

**3.2 Comprobad las cifras del informe** (si vuestro Excel o Sheets usa `;` o `,` en las fórmulas, usad el que os pida):

| Qué calculáis | Fórmula |
|---|---|
| Tasa del canal **directo** (total) | `=(D2+D4)/(C2+C4)` |
| Tasa del canal **intermediaria** (total) | `=(D3+D5)/(C3+C5)` |

¿Coinciden con 26,7 % y 15,8 %? **Sí: la cuenta del informe está bien.** Entonces, ¿dónde está el problema? Probad con las pistas, **de una en una**:

- **Pista 1.** El informe solo mira el **total**. ¿Qué pasa si comparáis los canales **dentro de cada tarifa**? Mirad la columna E: comparad filas 2 y 3 (flexible) y filas 4 y 5 (no reembolsable).
- **Pista 2.** Calculad qué parte de las reservas de cada canal es de tarifa flexible: directo `=C2/(C2+C4)`, intermediaria `=C3/(C3+C5)`.
- **Pista 3.** La tarifa flexible se cancela mucho más que la no reembolsable. ¿Qué tarifa vende sobre todo cada canal?

**Comprobad vuestras cifras** (leedlo **después** de calcular):

| Tarifa | Directo | Intermediaria |
|---|---|---|
| Flexible | 30 % | 35 % |
| No reembolsable | 10 % | 12 % |

**3.3 Completad la explicación** con las palabras que encajen (*flexible · no reembolsable · mucho · poco · peor · mejor*):

> Dentro de cada tarifa, la intermediaria cancela …… que el directo. En el total parece …… porque vende sobre todo tarifa ……, que se cancela …….

**3.4 Poned nombre al error.** ¿Qué carta es? (Pista: la que dice «si separo por grupos, cambia el resultado».)

**3.5 La recomendación de tres líneas.** Completad: «*Recomendamos …… (priorizar la intermediaria / no priorizarla / seguir mirando), porque ……. Antes de decidir habría que mirar ……*» (por ejemplo, el coste de cada canal o el margen de cada reserva).

#### Paso 4 · Vuestra afirmación (primera sesión, 20 minutos)

Cada persona resuelve **la afirmación que eligió (de la 3 a la 6)** usando la plantilla. Seguid esta receta, de arriba abajo:

1. **Copiad la frase** del informe.
2. **Elegid la carta** que encaje (las preguntas de la tabla del paso 2 os ayudan).
3. **Elegid el veredicto**.
4. **Completad la frase** de la carta en la plantilla.
5. **Escribid cómo debería decirse** en una frase, con vuestras palabras.
6. **Escribid qué datos faltan** (una línea).

Para la afirmación 6 hay una cuenta que hacer: ¿sale la bajada del 25 %? `(30 − 40) ÷ 40`. Y luego preguntaos: ¿se pueden comparar un mes de 28 días de baja ocupación con otro de 31 días de alta ocupación? Las demás no necesitan cuentas, solo mirar **qué se compara y quién falta**.

#### Paso 5 · Dictamen y revisión (segunda sesión, 55 minutos)

1. **Completar (20 min).** Terminad los bloques que falten: la afirmación 2 con su tabla (por tarifa y canal) y la recomendación; vuestras afirmaciones de la 3 a la 6.
2. **Una frase de IA responsable (5 min).** Al final del dictamen, completad: «*Si entrenáramos un modelo con ……, aprendería ……, porque ……*». Ejemplo inventado: «Si entrenáramos un modelo con las reseñas de quien se anima a escribir, aprendería solo la opinión de los extremos, porque las personas medianamente satisfechas casi no escriben».
3. **Revisión cruzada (15 min).** Intercambiad el dictamen con otra persona y comprobad con la autoevaluación de más abajo que cada bloque tiene carta, veredicto, frase corregida y cuenta, si la hay.
4. **Entrega (15 min).** Subid a `sprint-02/`, actualizad el tablero, rellenad la autoevaluación y repasad la Definition of Done.

### Cómo usar la IA en este reto

La IA es un **ayudante de explicación**, no una calculadora fiable: muchas IA de texto se equivocan en porcentajes y tablas, y lo hacen con mucha seguridad.

| Para qué | Ejemplo de petición | Qué tenéis que comprobar |
|---|---|---|
| Entender una carta | «Explícame la paradoja de Simpson con un ejemplo de un hotel, sin fórmulas» | Que podáis explicarlo con vuestras palabras |
| Redactar con claridad | «Reescribe esta frase para que la entienda una directora: *[tu frase]*. No cambies las cifras» | Que **las cifras sigan siendo las mismas** |

**Una sola regla:** si la IA os hace un cálculo, **comprobadlo a mano** (afirmaciones 2 y 6) y escribid en el dictamen **dónde habéis usado IA**. Nunca peguéis datos personales reales.

### Errores frecuentes (y cómo evitarlos)

| Error | Cómo evitarlo |
|---|---|
| Decir solo «está mal» | Cada bloque lleva **carta, veredicto y frase corregida** |
| Dar por buena una cuenta sin rehacerla | Rehaced las cifras con los datos, también las que parecen obvias |
| Mirar solo el total | Separad por tarifa y canal; comparad dentro de cada grupo |
| Dividir por el total equivocado | La tasa es cancelaciones ÷ reservas **del mismo grupo** |
| Inventar números cuando no hay datos | Decid «no se puede saber» y qué datos faltan |

### Antes de entregar: autoevaluación rápida

| Pregunta | Sí / No |
|---|---|
| ¿Hay veredicto para al menos **4 afirmaciones** (la 1, la 2 y dos más)? | |
| ¿Cada una tiene su **carta** (el nombre del error) y una frase corregida? | |
| ¿Las cuentas de las afirmaciones 1, 2 (y 6, si la hicisteis) se pueden rehacer con el CSV? | |
| ¿La afirmación 2 tiene la tabla por tarifa y canal y la recomendación de tres líneas? | |
| ¿Hay una frase de IA responsable? | |
| ¿Hemos comprobado a mano lo que calculó la IA (si la usamos)? | |
| ¿Están hechas las altas en Colab y GitHub? | |

### Si os atascáis

- **No sabemos qué carta es:** leed las preguntas de la tabla y contestadlas con vuestra afirmación; probad a **formularla de otra manera** (con números absolutos, con otra base) y mirad si la conclusión cambia.
- **Los números no nos cuadran:** revisad que dividís por las reservas **del grupo** (no por el total).
- **No sabemos cómo escribirlo:** usad la frase de la carta y rellenad los huecos.
- **No sabemos usar la hoja de cálculo:** preguntad al docente; son solo cuatro filas y dos fórmulas.
- Más ayuda: [Cómo se trabaja un reto](../../../material/4.%20Como_se_trabaja_un_reto.md).

### Qué se enseña en la review (2 min por persona)
- **Cada persona** presenta **una afirmación**: su carta, su veredicto y por qué, y la frase corregida.
- **El equipo** enseña la tabla de la afirmación 2 y la recomendación de tres líneas.
- Una cosa que os costó ver.

## Definition of Done (lista de comprobación)

Si queda una casilla sin marcar, **el reto no está terminado**.

- [ ] Dictamen de 1-2 páginas con **al menos 4 afirmaciones** (la 1, la 2 y dos más) y su veredicto
- [ ] Cada afirmación tiene su **carta** (nombre del error) y una frase corregida
- [ ] Cálculos rehechos y visibles (afirmaciones 1 y 2, y la 6 si la hacéis)
- [ ] Tabla de la afirmación 2 por tarifa y canal, y recomendación de tres líneas con una cautela
- [ ] Una frase de **IA responsable**
- [ ] Hoja de ejercicios con el mínimo básico (M1, M2, M7, E1, E2, E6, E8, E10)
- [ ] Revisión cruzada, subido a Git, tablero actualizado
- [ ] Autoevaluación y coevaluación rellenadas
- [ ] Alta en Colab y GitHub hecha (primera sesión, en clase)
