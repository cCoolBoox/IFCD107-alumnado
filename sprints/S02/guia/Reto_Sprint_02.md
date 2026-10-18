# Sprint 2 · Reto «¿Nos fiamos de este informe?»

> **Esta es la ficha completa del reto, explicada paso a paso** para quien nunca ha trabajado con esta metodología ni con IA. Léela entera **antes de empezar** y vuelve a ella cuando tengas dudas.
>
> - Si es tu primer reto, lee antes [Cómo se trabaja un reto](../../../material/4.%20Como_se_trabaja_un_reto.md).
> - Volver al [README del sprint](../README.md) · [Guía del sprint en PDF](Guia_Sprint_02.pdf) · [versión ecofriendly para imprimir](Guia_Sprint_02_ecofriendly.pdf).

## Ficha del reto

### En pocas palabras (léelo primero)

**Qué os pide el cliente.** La dirección de TurisData ha escrito un borrador de informe con **seis afirmaciones** sobre cancelaciones y lo va a presentar al consejo. Antes, os pide que lo reviséis como lo haría una persona auditora: *«Decidme si nos podemos fiar de cada frase; y si no, cómo debería decirse»*. Una de las afirmaciones (la 2) influye en una decisión importante: a qué canal de venta dar prioridad.

**Qué vais a hacer, en cuatro pasos:**
1. **Leer** el informe y comprobar si las **cuentas** de cada frase salen de los datos.
2. **Detectar el error** de cada una (cada frase tiene un problema distinto) y ponerle nombre.
3. **Rehacer los cálculos** bien, con una calculadora u hoja de cálculo.
4. **Escribir un dictamen** (2–3 páginas) con el veredicto de cada afirmación y una recomendación para la dirección.

**No se programa.** Basta una calculadora o una hoja de cálculo (Excel, Calc, Google Sheets).

**Qué vais a entregar:** el dictamen de auditoría, la recomendación sobre el canal y la hoja de ejercicios del sprint (con el mínimo exigido).

**Qué vais a aprender haciéndolo:** a **no creerse una estadística solo porque salga en un informe**. Es la habilidad más útil antes de entrenar cualquier modelo, porque **un modelo entrenado con datos mal interpretados aprende mal**.

**Cuánto tiempo:** 2 horas de reto, entre el miércoles 21/10 y el viernes 23/10. Además, recordad dar de alta vuestra cuenta de Colab y GitHub **antes del 22/10**.

### Palabras que van a aparecer en este reto

| Palabra | Qué significa, en sencillo |
|---|---|
| **Auditar** | Revisar el trabajo de otra persona para comprobar si es correcto |
| **Dictamen** | El documento donde dais vuestra opinión razonada («veredicto») |
| **Tasa** | Una proporción: cuántas cancelaciones hay por cada 100 reservas |
| **Muestra** | Un trozo pequeño de los datos con el que se pretende hablar de todo |
| **Muestra sesgada** | Una muestra que no representa a todos (por ejemplo, solo clientes que dejaron su correo) |
| **Correlación** | Dos cosas que suben o bajan a la vez. **No significa que una cause la otra** |
| **Causalidad** | Una cosa produce la otra |
| **Paradoja de Simpson** | Un resultado que parece cierto al mirar el total, pero se invierte al separar por grupos |
| **Base de comparación** | Aquello con lo que se compara. Si la base es distinta, la comparación no es justa |
| **Reproducible** | Que otra persona, con los mismos datos y pasos, obtenga la misma cifra |

### Escena del cliente
La dirección de *TurisData Canarias* ha preparado un **borrador de informe** sobre cancelaciones para presentarlo al consejo. Antes de hacerlo, la directora os lo pasa: *"Un cliente del consejo me dijo que hay que revisar estos números con ojo crítico. Decidme **si nos podemos fiar de cada afirmación**, y si no, qué debemos decir en su lugar. Y cuidado: la decisión de a qué canal dar prioridad depende de esto."*

### Qué tenéis que entregar
1. **Dictamen de auditoría** (2-3 páginas en `.md` o PDF): para cada una de las **seis afirmaciones** del informe, indicad:
   - **Veredicto:** *fiable · parcialmente fiable · no fiable · no se puede saber*.
   - **Problema detectado** (tipo de error estadístico) y **por qué**.
   - **Cálculo rehecho** cuando haya datos (tabla con vuestros números).
   - **Cómo debería decirse** (redacción corregida) y **qué datos faltan**.
2. **Recomendación** para la dirección sobre el canal (afirmación 2): qué decidir y qué cautelas.
3. **La hoja de ejercicios** del sprint, con el mínimo exigido en el README del sprint (8 de 12 de la hoja 1 y 10 de 14 de la hoja 2).

### Datos y recursos
- **`informe_cliente.md`** (carpeta `datos/` del repositorio): el borrador del informe con las seis afirmaciones.
- **`informe_cliente.csv`** (carpeta `datos/` del repositorio): datos de **2.400 reservas**, agrupadas por `tarifa` y `canal`, con columnas `reservas` y `cancelaciones`. El archivo tiene 4 filas (una por combinación de tarifa y canal).
- Vuestras hojas de ejercicios, la lista de control de [`estadisticas_enganosas.md`](../actividades/estadisticas_enganosas.md) y una calculadora u hoja de cálculo. **No hace falta Python.**

### Restricciones
- **Tiempo:** 2 h de reto en clase (dentro de las 10 h del sprint).
- **Extensión:** 2-3 páginas.
- Cada cifra que aparezca en el dictamen debe poder **rehacerse** con los datos entregados (reproducibilidad).
- Cuando no haya datos para comprobar una afirmación, **no inventéis números**: decid qué datos harían falta.
- Si usáis un asistente de IA para redactar o calcular, **declarad dónde** y **comprobad** los cálculos a mano al menos en las afirmaciones 2 y 6.

### Criterios de evaluación
Cada entregable se evalúa de 0 a 4 en los cuatro criterios de la rúbrica de retos.

| Criterio | 1 · Insuficiente | 2 · Suficiente | 3 · Bueno | 4 · Excelente |
|---|---|---|---|---|
| **Corrección técnica** | Cálculos erróneos o errores no detectados | Detecta la mayoría de los errores, con fallos de cálculo o de nombre | Detecta los seis problemas y rehace los cálculos correctamente | Además cuantifica la incertidumbre (p. ej. intervalos) o razona cuándo la diferencia es real |
| **Reproducibilidad** | No se ve cómo se han obtenido las cifras | Cifras sin todos los pasos | Cada cifra se puede rehacer con los datos y los pasos indicados | Además hay tabla de cálculo o hoja adjunta y las fuentes están citadas |
| **Análisis y comunicación al cliente** | Solo dice "está mal" | Explica cada error de forma correcta pero técnica | Explica con lenguaje claro y propone redacciones corregidas | Recomendación accionable sobre el canal, con límites y datos a pedir |
| **IA responsable** | No se considera | Menciona "cuidado con los sesgos" | Relaciona los errores con riesgos de entrenar o decidir con datos así (muestra sesgada, confusión) | Propone comprobaciones concretas antes de usar estos datos para un modelo |

### Pasos sugeridos (2 h de reto)

| Momento | Qué hacer |
|---|---|
| **Mié 21/10 · planning (30 min)** | Leed el informe, repartid las 6 afirmaciones entre las personas del equipo (con revisión cruzada) y preparad el tablero |
| **Jue 22/10 (30 min)** | Primera lectura de cada afirmación con la lista de control; anotad vuestras **hipótesis** de error |
| **Vie 23/10 (30 min)** | Rehaced los cálculos, redactad el dictamen y la recomendación, revisión cruzada y DoD |
| **Vie 23/10 · última media hora** | Review (5 min por equipo) y retro |

### Pistas (sin destriparlo)
- Empezad por comprobar **las cuentas**: ¿las cifras que da el informe salen de los datos?
- En la afirmación 2, **mirad la tabla completa** y comparad canal por canal **dentro de cada tarifa**. Calculad también **cuántas reservas** de cada canal son de cada tarifa.
- En la 5 y la 6, pensad en qué **debería compararse** en lugar de lo que se compara.
- En la 1 y la 3, ¿"la media del sector" y "el depósito reduce" están respaldados por los datos entregados?
- ¡Ojo!: puede haber afirmaciones con cuentas correctas pero conclusión incorrecta.

### Guía paso a paso para principiantes

#### Paso 1 · Planning (miércoles 21/10, 30 minutos)
1. Leed el informe ([`informe_cliente.md`](../../../datos/informe_cliente.md)) **en voz alta**, afirmación por afirmación.
2. Repartid las seis afirmaciones entre las personas del equipo (por ejemplo, de dos en dos). Cada afirmación tendrá **una persona responsable** y **una persona que la revisa**.
3. Abrid la hoja de datos ([`informe_cliente.csv`](../../../datos/informe_cliente.csv)) en una hoja de cálculo y mirad qué columnas tiene: `tarifa`, `canal`, `reservas` y `cancelaciones`. Son solo **4 filas**.

#### Paso 2 · Primera lectura con la lista de control (jueves 22/10, 30 minutos)
Usad la lista de [`estadisticas_enganosas.md`](../actividades/estadisticas_enganosas.md). Para **cada** afirmación, respondeos tres preguntas:
1. **¿Qué afirma exactamente?** (con vuestras palabras).
2. **¿Qué falla o qué falta?** Pensad en el tipo de error: ¿muestra pequeña o sesgada?, ¿correlación tomada por causa?, ¿comparación con otra base?, ¿cuentas mal hechas?, ¿resultado que cambia al separar por grupos?
3. **¿Qué datos necesitaría para comprobarlo?**

Escribid vuestra **hipótesis** de error. Todavía no la deis por buena: en el paso 3 la comprobaréis.

#### Paso 3 · Rehacer los cálculos (viernes 23/10, primera media hora)
**Cómo se calcula una tasa de cancelación:** `cancelaciones ÷ reservas × 100`.

Ejemplo inventado (no son los datos del reto): si en una tarifa hay 500 reservas y 50 cancelaciones, la tasa es 50 ÷ 500 × 100 = **10 %**.

Aplicad la misma idea a vuestros datos:
1. **Afirmación 1:** calculad la tasa global (todas las cancelaciones ÷ todas las reservas) y comprobad si coincide con la cifra del informe. Luego pensad: ¿de dónde sale «la media del sector»? ¿Hay algún dato que lo respalde?
2. **Afirmación 2:** calculad la tasa **por canal** (primero con todas las reservas) y después **por canal dentro de cada tarifa**. Calculad también **cuántas reservas de cada canal pertenecen a cada tarifa**. Comparad: ¿lo que veis en el total se mantiene al separar?
3. **Afirmaciones 3 a 6:** mirad qué se compara en cada una, con qué tamaño de muestra y quién respondió o quedó fuera.

**Una tabla de ayuda** para la afirmación 2 (rellenadla con vuestros números):

| Tarifa | Canal | Reservas | Cancelaciones | Tasa (%) |
|---|---|---|---|---|
| … | … | … | … | … |

#### Paso 4 · Dictamen y recomendación (viernes 23/10, última parte)
Para **cada una de las seis afirmaciones**, escribid un bloque con esta estructura:

| Campo | Qué poner |
|---|---|
| **Veredicto** | *fiable · parcialmente fiable · no fiable · no se puede saber* |
| **Problema** | El nombre del error y **por qué** lo es, en lenguaje que entienda la dirección |
| **Cálculo rehecho** | Una tabla pequeña con vuestras cifras (si hay datos) |
| **Cómo debería decirse** | Una frase corregida |
| **Qué datos faltan** | Lo que pediríais al cliente para cerrar la duda |

**«No se puede saber» es una respuesta válida y honrada.** Si no hay datos para comprobar algo, **no inventéis números**.

Cerrad con la **recomendación sobre el canal** (afirmación 2): qué decidiría la dirección con los datos correctos y qué cautelas debe tener.

### Cómo usar la IA en este reto

Aquí la IA es un **ayudante de explicación**, pero **no una calculadora fiable**. Muchas IA de texto se equivocan al hacer porcentajes y tablas, y lo hacen con mucha seguridad.

| Para qué | Ejemplo de petición | Qué tenéis que comprobar |
|---|---|---|
| Entender un error | «Explícame qué es la paradoja de Simpson con un ejemplo de un hotel, sin fórmulas» | Que vosotros podáis explicarlo con vuestras palabras |
| Redactar con claridad | «Reescribe esta frase para que la entienda una directora no técnica: *[tu frase]*. No cambies las cifras» | Que **las cifras sigan siendo las mismas** |
| Detectar fallos | «Aquí tienes mi dictamen de la afirmación 4. ¿Qué argumento me falta?» | Que no añada datos inventados |

**Regla obligatoria del reto:** si la IA os hace un cálculo, **comprobadlo a mano**, al menos en las afirmaciones 2 y 6. Y escribid en el dictamen **dónde habéis usado IA** y **qué habéis verificado**.

**Nunca peguéis datos personales reales**: aquí no los hay, pero es una buena costumbre.

### Errores frecuentes (y cómo evitarlos)

| Error | Por qué ocurre | Cómo evitarlo |
|---|---|---|
| Decir solo «está mal» | Se detecta el fallo, pero no se explica | Cada veredicto debe tener **qué falla, por qué y cómo se diría bien** |
| Dar por buena una cuenta sin rehacerla | «Si lo dice el informe…» | Rehaced **todas** las cifras con los datos |
| Mirar solo el total | El total esconde diferencias entre grupos | Separad por tarifa y canal; comparad dentro de cada grupo |
| Confundir correlación con causa | Dos cosas suben a la vez y parece obvio | Preguntaos: ¿puede haber una **tercera cosa** que explique ambas? |
| Inventar la «media del sector» | Queda bien | Si no hay fuente en los datos, decid «no se puede saber» y qué dato falta |
| Redondear antes de tiempo | Se pierde exactitud | Calculad con todos los decimales y redondead solo al presentar |

### Un buen resultado se parece a…

Ejemplo **inventado** (no corresponde a ninguna afirmación real del reto) de cómo debe quedar un bloque:

> **Afirmación X:** «Las reseñas de 5 estrellas han subido un 30 %».
> **Veredicto:** parcialmente fiable.
> **Problema:** el informe compara un mes con 50 reseñas y otro con 200. Los porcentajes dependen de cuántas reseñas hay.
> **Cálculo rehecho:** mes A, 25 de 50 = 50 %; mes B, 120 de 200 = 60 %. La subida real es de 10 puntos porcentuales, no del 30 %.
> **Cómo debería decirse:** «El porcentaje de reseñas de 5 estrellas pasó del 50 % al 60 %».
> **Datos que faltan:** el número de reseñas por canal.

Fijaos en que cada parte responde a **una pregunta concreta** y se entiende sin saber estadística.

### Antes de entregar: autoevaluación rápida

| Pregunta | Sí / No |
|---|---|
| ¿Hay un veredicto para **las seis** afirmaciones? | |
| ¿Cada error tiene su **nombre** y su explicación en lenguaje sencillo? | |
| ¿Se pueden **rehacer** todas las cifras con los datos del CSV? | |
| ¿La afirmación 2 tiene tabla por tarifa y canal y una recomendación con cautelas? | |
| ¿Hay una lista de datos que faltan? | |
| ¿Hemos relacionado al menos un error con IA responsable (qué pasaría si entrenáramos un modelo con estos datos)? | |
| ¿Hemos comprobado a mano los cálculos que hizo la IA (si la usamos)? | |
| ¿Están hechas las altas en Colab y GitHub? | |

### Si os atascáis

- **No sabemos si una afirmación es buena o mala:** probad a **formularla de otra manera** (con números absolutos, con otra base de comparación) y mirad si la conclusión cambia.
- **Los números no nos cuadran:** revisad si estáis dividiendo por el total correcto (reservas del grupo, no reservas totales).
- **No sabemos cómo se llama el error:** la lista de control de `estadisticas_enganosas.md` tiene todos los nombres.
- Más ayuda: [Cómo se trabaja un reto](../../../material/4.%20Como_se_trabaja_un_reto.md).

### Qué se enseña en la review (5 min por equipo)
- **Una afirmación** de las seis y vuestro dictamen (veredicto + por qué).
- **La tabla de cálculo** de la afirmación 2 y vuestra recomendación sobre el canal.
- **El error que más os ha costado** ver.
- Los datos que pediríais a TurisData para cerrar las dudas.

## Definition of Done (lista de comprobación)

Si queda una casilla sin marcar, **el reto no está terminado**.

- [ ] Dictamen de 2-3 páginas con **las seis afirmaciones** y su veredicto
- [ ] Cálculos rehechos con los datos (afirmaciones 1, 2 y 6), con los pasos visibles
- [ ] La afirmación 2 tiene tabla por tarifa y canal, y una recomendación con cautelas
- [ ] Cada error tiene su **nombre** (muestreo, correlación/causalidad, Simpson, base...)
- [ ] Redacción corregida de cada afirmación
- [ ] Lista de datos que faltan
- [ ] Al menos una relación con **IA responsable** (qué pasaría si entrenáramos un modelo con estos datos)
- [ ] Hoja de ejercicios con el mínimo exigido
- [ ] Revisión cruzada, subido a Git, tablero actualizado
- [ ] Autoevaluación y coevaluación rellenadas
- [ ] Alta en Colab y GitHub hecha ( **antes del 22/10**)
