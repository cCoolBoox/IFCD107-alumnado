# Soluciones paso a paso · Hoja 2 · Estadística, probabilidad, Bayes, muestreo y sesgo

Aquí tenéis las soluciones de la hoja [`ejercicios_estadistica.md`](ejercicios_estadistica.md), **explicadas paso a paso** y sin dar nada por sabido (E1 a E14).

## Cómo usarlas

- **Primero intentad cada ejercicio vosotros**, en papel, sin mirar. Equivocarse también es aprender.
- **Después comparad** con la solución y **corregid con otro color**.
- Si vuestro resultado es distinto, **buscad en qué paso se separa**: ahí está lo que hay que repasar. Anotadlo como «mi nota de dónde me atasqué».
- No copiéis el resultado: lo que importa es **entender el camino** y poder **explicarlo con vuestras palabras**.

## Cómo está organizado cada ejercicio

- **La idea en una frase:** qué se está haciendo, sin fórmulas.
- **Paso a paso:** cada operación en una línea, con las cuentas a la vista.
- **Resultado:** la respuesta final.
- **Qué significa:** la respuesta traducida al caso (reservas, hoteles, clientes).
- **Ojo con:** el error que más se repite.

## Palabras que vamos a usar

- **Dato:** un número que hemos medido (lo que ha pagado una reserva, las noches que se queda un huésped…).
- **Media:** lo que tocaría a cada uno si **repartiéramos todo a partes iguales**.
- **Mediana:** el dato **de en medio** cuando los ordenamos de menor a mayor.
- **Probabilidad:** un número entre 0 y 1 (o entre 0 % y 100 %) que dice **cuántas posibilidades hay** de que algo ocurra. 0,25 = 25 % = «1 de cada 4».
- **Muestra:** un **grupo pequeño** que miramos para saber cómo es un grupo grande.

## Regla práctica para todo el bloque

> **Pasad los porcentajes a «de cada…».** «El 1 % son fraude» = «de cada 100 reservas, 1 es fraude». Se entiende mucho mejor que con fórmulas.

---

## Bloque A · Estadística descriptiva

### E1 · Media, mediana y cuartiles
Datos: ingresos de 8 reservas: **90, 95, 100, 100, 105, 110, 120, 480** (ya están ordenados de menor a mayor).

**La idea en una frase:** queremos **un solo número que describa «una reserva normal»**. Hay dos formas de calcularlo y **no siempre dan lo mismo**.

**a) Media y mediana**

Paso a paso:
- **Media:** sumamos todo: 90 + 95 + 100 + 100 + 105 + 110 + 120 + 480 = 1.200.
- Dividimos entre cuántos datos hay (8): 1.200 ÷ 8 = **150**.
- **Mediana:** como son 8 datos (par), no hay uno solo en el centro. Cogemos **los dos del medio**, el 4.º y el 5.º: 100 y 105.
- Hacemos su media: (100 + 105) ÷ 2 = **102,5**.

**Resultado:** media = **150 €** y mediana = **102,5 €**.

**¿Cuál describe mejor «una reserva normal»?** La **mediana**. Casi todas las reservas están **alrededor de 100 €**, y la media (150) **no se parece a ninguna**: la ha subido la reserva de 480 €.

**b) Cuartiles Q1 y Q3 y el IQR**

Paso a paso:
- Partimos los datos **en dos mitades**: la de abajo (90, 95, 100, 100) y la de arriba (105, 110, 120, 480).
- **Q1** es la **mediana de la mitad de abajo**: los dos del medio son 95 y 100 → (95 + 100) ÷ 2 = **97,5**.
- **Q3** es la **mediana de la mitad de arriba**: 110 y 120 → (110 + 120) ÷ 2 = **115**.
- El **IQR** es la distancia entre ellos: 115 − 97,5 = **17,5**.

**Resultado:** Q1 = **97,5**, Q3 = **115**, IQR = **17,5**. El IQR dice **cuánto se reparte la mitad central** de los datos.

**c) ¿Es 480 un dato atípico?**

Paso a paso:
- La regla: es atípico si **supera Q3 + 1,5·IQR**.
- 1,5·17,5 = 26,25.
- 115 + 26,25 = **141,25**.
- Comparamos: 480 es **mucho mayor** que 141,25.

**Resultado:** **sí**, 480 es un dato atípico (*outlier*): se sale de lo normal.

**d) La media sin el 480**

Paso a paso:
- Quitamos el 480. Quedan 7 datos que suman 1.200 − 480 = 720.
- 720 ÷ 7 ≈ **102,9**.
- Antes era 150: **ha bajado unos 47 €**.

**Resultado:** media sin el 480 ≈ **102,9 €**.

**Qué significa:** **una sola reserva rara cambia mucho la media**, pero **casi nada la mediana**. La mediana es más fiable cuando hay valores extremos.

**Ojo con:** dividir la suma entre un número equivocado (7 en vez de 8 en el apartado a).

### E2 · Varianza y desviación típica
Datos: noches de 8 reservas: **2, 4, 4, 4, 5, 5, 7, 9**.

**La idea en una frase:** la media dice **dónde está el centro**; la desviación típica dice **cuánto se alejan los datos de ese centro** (si son parecidos o muy distintos).

**a) La media**

- Suma: 2 + 4 + 4 + 4 + 5 + 5 + 7 + 9 = 40.
- 40 ÷ 8 = **5**.

**b) Varianza y desviación típica**

Paso a paso:
- Restamos la media (5) a cada dato: −3, −1, −1, −1, 0, 0, 2, 4.
- Elevamos cada diferencia **al cuadrado** (así los negativos no se compensan con los positivos): 9, 1, 1, 1, 0, 0, 4, 16.
- Sumamos: 9 + 1 + 1 + 1 + 0 + 0 + 4 + 16 = 32.
- **Varianza** = media de esos cuadrados: 32 ÷ 8 = **4**.
- **Desviación típica** = raíz cuadrada de la varianza: √4 = **2**.

**Resultado:** varianza = **4** y desviación típica = **2 noches**.

**c) Si fueran una muestra**

- Cuando solo miramos **una parte** de todas las reservas, la varianza se calcula **dividiendo entre 7** (n − 1) en vez de 8.
- 32 ÷ 7 ≈ **4,57**. Raíz: √4,57 ≈ **2,14**.

**Resultado:** varianza muestral ≈ **4,57** y desviación ≈ **2,14**: **un poco mayor**, porque una muestra tiende a quedarse corta al medir cuánto varía todo el grupo, y esto lo corrige.

**d) En llano, ¿qué significa 2 noches?**

**Resultado:** **una reserva típica se aleja unas 2 noches de la media de 5**. Es decir, las estancias suelen estar entre unas 3 y 7 noches.

**Ojo con:** olvidar elevar al cuadrado, o olvidar la raíz al final.

---

## Bloque B · Probabilidad y distribuciones

### E3 · Probabilidad condicionada
Datos: 200 reservas. **120 directas** (30 canceladas) y **80 de la intermediaria** (24 canceladas).

**La idea en una frase:** una probabilidad **condicionada** es la probabilidad **cuando ya sabemos algo** («si la reserva es directa…»). Para entenderlo, **primero ordenamos los datos en una tabla**.

**a) La tabla**

Paso a paso:
- Directas: 30 canceladas, así que **no canceladas = 120 − 30 = 90**.
- Intermediaria: 24 canceladas, así que **no canceladas = 80 − 24 = 56**.
- Totales por columna: canceladas 30 + 24 = 54; no canceladas 90 + 56 = 146.
- Comprobamos: 54 + 146 = 200 ✓.

| | Cancelada | No cancelada | Total |
|---|---|---|---|
| Directa | 30 | 90 | 120 |
| Intermediaria | 24 | 56 | 80 |
| Total | 54 | 146 | 200 |

**b) Tres probabilidades**

Paso a paso (siempre «los que cumplen» entre «los que miramos»):
- **P(cancelada)** = canceladas entre todas: 54 ÷ 200 = **0,27** (27 %).
- **P(cancelada | directa)** = canceladas **entre las directas**: 30 ÷ 120 = **0,25** (25 %).
- **P(cancelada | intermediaria)** = 24 ÷ 80 = **0,30** (30 %).

**c) Se ha cancelado: ¿cuál es la probabilidad de que fuera de la intermediaria?**

Ahora **miramos solo las canceladas** (54):
- De ellas, 24 eran de la intermediaria.
- 24 ÷ 54 ≈ **0,444**.

**Resultado:** **44 %**: «de cada 100 canceladas, unas 44 vienen de la intermediaria».

**d) ¿Son independientes canal y cancelación?**

- Si **no tuvieran nada que ver**, daría igual el canal: las tres probabilidades serían iguales.
- Pero son **0,25**, **0,30** y **0,27**: **no son idénticas**.

**Resultado:** **no son independientes**, aunque la diferencia es pequeña. Con solo 200 datos **podría ser casualidad**: una diferencia no es lo mismo que una diferencia que importe de verdad.

**Qué significa:** la intermediaria cancela algo más, pero no podemos asegurar que sea por el canal.

**Ojo con:** en c) dividir entre 80 (que daría 0,30). La pregunta es distinta: ahora **partimos de las canceladas**.

### E4 · Distribución binomial
Datos: cada reserva flexible se cancela con probabilidad **0,2** (1 de cada 5), independientemente de las demás. Hay **10** reservas.

**La idea en una frase:** es como **tirar 10 veces una moneda trucada** que cae «cancelada» 1 de cada 5 veces. La binomial calcula las probabilidades de cada número de cancelaciones.

**a) Cancelaciones esperadas**

- 10 reservas × 0,2 = **2**.

**Resultado:** de media, **2 cancelaciones**.

**b) Exactamente 2 cancelaciones**

Paso a paso:
- Fórmula: C(10,2) · 0,2² · 0,8⁸.
- C(10,2) = 45 (formas de elegir **cuáles dos** de las 10 se cancelan).
- 0,2² = 0,04 (dos canceladas).
- 0,8⁸ ≈ 0,168 (las otras ocho **no** se cancelan: 0,8 por 0,8 por 0,8…).
- Multiplicamos: 45 · 0,04 = 1,8; 1,8 · 0,168 ≈ **0,302**.

**Resultado:** **30 %**: tres de cada diez fines de semana habrá justo 2 cancelaciones.

**c) Ninguna cancelación**

- Las 10 deben **no** cancelarse: 0,8 · 0,8 · … (diez veces) = 0,8¹⁰ ≈ **0,107**.

**Resultado:** **11 %** (poco más de 1 de cada 10 fines de semana).

**d) Al menos una**

- «Al menos una» es **todo lo contrario** de «ninguna».
- 1 − 0,107 = **0,893**.

**Resultado:** **89 %**: casi 9 de cada 10 fines de semana habrá alguna cancelación.

**Qué significa:** aunque de media sean 2, **no sabemos exactamente cuántas**; la binomial da **la probabilidad de cada caso**.

**Ojo con:** confundir 0,8⁸ con 0,8·8 (que daría 6,4: una probabilidad nunca pasa de 1).

### E5 · Distribución normal
Datos: la ocupación diaria tiene **media 70 %** y **desviación típica 10 puntos**.

**La idea en una frase:** la **campana normal** dice que la mayoría de los días están **cerca de la media** y los días raros (muy altos o muy bajos) son pocos.

**a) La regla 68-95-99,7**

- Dentro de **1** desviación de la media está el 68 % de los días; dentro de **2**, el **95 %**; dentro de 3, el 99,7 %.
- Para el 95 %: 70 − 2·10 = **50** y 70 + 2·10 = **90**.

**Resultado:** el 95 % de los días la ocupación está **entre el 50 % y el 90 %**.

**b) La z de un día con 95 %**

- *z* cuenta **cuántas desviaciones típicas** nos alejamos de la media.
- (95 − 70) ÷ 10 = 25 ÷ 10 = **2,5**.

**Resultado:** z = **2,5**: ese día está **2,5 desviaciones por encima** de la media. Es un día muy poco habitual.

**c) ¿Cuántos días al año?**

- Probabilidad: 0,6 % = 0,006.
- 0,006 · 365 ≈ 2,2.

**Resultado:** **unos 2 días al año**.

**d) Limitación del modelo**

- La ocupación **no puede pasar del 100 %**, pero la campana **sí deja valores más grandes**.
- Cerca del 100 %, la distribución real se **«aplasta»** contra el tope.

**Resultado:** el modelo normal es **una aproximación**: da probabilidad a cosas imposibles (más del 100 %).

**Qué significa:** los modelos **simplifican** la realidad; sirven, pero hay que saber **dónde fallan**.

**Ojo con:** olvidar que las **2 desviaciones** son **20 puntos** (2·10), no 2.

### E6 · Distribución uniforme
Datos: llegadas **entre las 16:00 y las 20:00**, sin preferencias.

**La idea en una frase:** «uniforme» significa que **todas las horas son igual de probables**. La probabilidad se calcula como **una parte entre el total** (como cortar una tarta).

**a) Llegar antes de las 17:30**

- Tiempo total posible: de 16:00 a 20:00 = **4 horas**.
- Tiempo favorable: de 16:00 a 17:30 = **1,5 horas** (1 hora y 30 minutos).
- 1,5 ÷ 4 = **0,375**.

**Resultado:** **37,5 %** (casi 4 de cada 10).

**b) Llegar entre las 18:00 y las 19:00**

- 1 hora favorable de 4: 1 ÷ 4 = **0,25**.

**Resultado:** **25 %** (1 de cada 4).

**c) Hora media de llegada**

- Si todo es parejo, **la media es el punto de en medio** entre las 16:00 y las 20:00.

**Resultado:** **las 18:00**.

**Ojo con:** escribir 1 hora 30 como 1,30 en vez de **1,5**.

---

## Bloque C · Teorema de Bayes

### E7 · El detector de reservas fraudulentas
Datos: **1 %** de las reservas son fraude. Si es fraude, el detector salta **90 %** de las veces. Si **no** es fraude, salta **5 %** de las veces (falsa alarma).

**La idea en una frase:** una alarma «90 % fiable» **no** significa que, cuando salta, haya un 90 % de fraude. Para verlo, **imaginamos 10.000 reservas** y las contamos.

**a) Contamos con 10.000 reservas**

Paso a paso:
- **Fraudulentas:** el 1 % de 10.000 = **100**.
- **Honestas:** 10.000 − 100 = **9.900**.
- De las 100 fraudulentas, la alarma salta en el 90 %: **90**.
- De las 9.900 honestas, la alarma salta en el 5 % (falsas alarmas): 9.900 · 0,05 = **495**.

**b) De todas las que saltan, ¿qué proporción es fraude?**

Paso a paso:
- **Alarmas en total:** 90 + 495 = **585**.
- De esas 585, **fraude de verdad:** 90.
- 90 ÷ 585 ≈ **0,154**.

**Resultado:** solo el **15 %**: de cada 100 alarmas, **unas 15** son fraude real.

**c) ¿Qué tiene mal lo del directivo?**

- «Si es fraude, salta el 90 %» **no es lo mismo** que «si salta, es fraude el 90 %».
- **Casi todas las reservas son honestas** (9.900 de 10.000), así que **aunque la falsa alarma sea pequeña (5 %), son muchas** (495) y **superan** a las alarmas verdaderas (90).

**Resultado:** el directivo **confunde los dos sentidos** y se olvida de que **el fraude es raro**.

**d) ¿Y si el fraude fuera el 10 %?**

Paso a paso (con 10.000 reservas):
- Fraudulentas: **1.000**; honestas: **9.000**.
- Alarmas verdaderas: 90 % de 1.000 = **900**.
- Falsas alarmas: 5 % de 9.000 = **450**.
- Alarmas en total: 900 + 450 = 1.350.
- Fraude real entre las alarmas: 900 ÷ 1.350 ≈ **0,667**.

**Resultado:** **67 %**. **Cuanto más frecuente es el fraude, más fiable es la alarma.**

**e) Con la fórmula de Bayes**

Paso a paso (con el 1 % de fraude):
- P(F|A) = P(A|F) · P(F) ÷ P(A).
- P(A|F) = 0,9 (si es fraude, salta). P(F) = 0,01.
- P(A) = 0,9·0,01 + 0,05·0,99 = 0,009 + 0,0495 = 0,0585 (saltar en fraudes + saltar en honestas).
- P(F|A) = 0,009 ÷ 0,0585 ≈ **0,154**.

**Resultado:** **15,4 %**: **el mismo resultado**, calculado con la fórmula en vez de contando.

**Qué significa:** una prueba «muy buena» **puede fallar mucho** si lo que busca es **raro**. Pasa igual con las pruebas médicas y con los detectores de fraude.

**Ojo con:** dividir 90 ÷ 100 en el apartado b): eso responde a otra pregunta («de los fraudes, ¿en cuántos salta?»).

---

## Bloque D · Muestreo y sesgo

### E8 · ¿Qué sesgo tiene esta muestra?

**La idea en una frase:** una **muestra** sirve si es **parecida al grupo grande**. Si **faltan** ciertos tipos de personas, el resultado engaña: eso es un **sesgo**.

Para cada caso nos hacemos tres preguntas: **¿a quién falta? ¿qué sesgo es? ¿cómo lo mejoro?**

**a) Encuesta a la salida, solo a quienes pasan por el desayuno**

- **¿A quién falta?** A quienes **se van temprano o no desayunan** (quizá con prisa o más molestos).
- **¿Qué sesgo?** **Sesgo de selección**: hemos elegido a la gente de forma que no representa a todos.
- **¿Cómo mejorarlo?** Preguntar a una **muestra aleatoria de todos los que salen**.

**b) Reseñas online**

- **¿A quién falta?** A quienes **no se animan a escribir** (la mayoría, que está «normal»).
- **¿Qué sesgo?** **Autoselección**: responden sobre todo los **muy contentos o los muy enfadados**.
- **¿Cómo mejorarlo?** Invitar a una **muestra aleatoria de todos los huéspedes**.

**c) «Los alojamientos con más de 10 años tienen buena valoración, luego la buena valoración garantiza durar»**

- **¿A quién falta?** A los alojamientos **que cerraron**.
- **¿Qué sesgo?** **Sesgo de supervivencia**: solo vemos a los que **sobrevivieron**.
- **¿Cómo mejorarlo?** **Incluir también los que cerraron** y ver cómo eran sus valoraciones.

**d) Correo a quienes dejaron su email, «¿estás satisfecho?»**

- **¿A quién falta?** A quienes **no dejaron el email** (suelen estar menos comprometidos).
- **¿Qué sesgo?** **Autoselección** y además una **pregunta que invita a decir que sí**.
- **¿Cómo mejorarlo?** Muestra **aleatoria**, pregunta **neutra** («¿cómo valoras tu estancia?») y una **escala** (de 1 a 5).

**Qué significa:** **antes de fiarse de un dato, preguntad quién falta**.

**Ojo con:** quedarse solo en el nombre del sesgo. Hay que decir **también a quién falta y cómo se arregla**.

### E9 · Tamaño de muestra y margen de error
Datos: preguntamos a **400** huéspedes al azar y el **62 %** dice que volvería.

**La idea en una frase:** como solo hemos preguntado a **400**, el 62 % **no es exacto**: el valor real estará en un **rango** alrededor. Ese rango es el **margen de error**.

**a) El error típico**

Paso a paso:
- Fórmula: √( p·(1 − p) ÷ n ), con p = 0,62 y n = 400.
- 1 − 0,62 = 0,38.
- 0,62 · 0,38 = 0,2356.
- 0,2356 ÷ 400 = 0,000589.
- Raíz cuadrada: **≈ 0,0243**.

**Resultado:** error típico ≈ **0,0243** (2,4 puntos).

**b) El intervalo de confianza del 95 %**

Paso a paso:
- Multiplicamos por 1,96: 1,96 · 0,0243 ≈ 0,0476 (unos **4,8 puntos**).
- **Restamos y sumamos** a 0,62: 0,62 − 0,0476 = 0,572 y 0,62 + 0,0476 = 0,668.

**Resultado:** **entre el 57,2 % y el 66,8 %**.

**En llano:** el porcentaje real de huéspedes que volverían está **razonablemente entre el 57 % y el 67 %**. No es exactamente 62.

**c) ¿Qué muestra para ±2 puntos?**

Paso a paso:
- Fórmula: n = (1,96 · 0,5 ÷ margen)², con margen = 0,02.
- 1,96 · 0,5 = 0,98.
- 0,98 ÷ 0,02 = 49.
- 49² = 49 · 49 = **2.401**.

**Resultado:** hacen falta **unas 2.400 personas**.

**d) Si cuadruplicamos la muestra**

- El margen depende de **1/√n**. Con 4 veces más gente, √4 = 2.

**Resultado:** el margen **se reduce a la mitad**.

**Qué significa:** **hacerlo más preciso cuesta mucho**: para bajar el margen a la mitad hay que preguntar **a cuatro veces más gente**.

**Ojo con:** decir «el 62 % exacto volverá». Con una muestra solo podemos dar **un rango**.

---

## Bloque E · Correlación, causalidad y contraste

### E10 · ¿Correlación o causalidad?

**La idea en una frase:** que **dos cosas suban juntas** no significa que **una cause la otra**. Puede haber **una tercera cosa** que provoque las dos, o **la causa puede ser al revés**.

Para cada frase buscamos **una explicación alternativa** y pensamos **cómo comprobar la causa real**.

**a) «Los meses con más helados vendidos tienen más reservas»**

- **Tercera variable:** la **temporada alta** (calor, más gente).
- **Por qué:** en temporada alta **se venden más helados y también hay más reservas**: las dos cosas vienen del mismo motivo.
- **Cómo comprobarlo:** comparar **semanas de la misma temporada** con y sin helados regalados.

**b) «Los hoteles con más personal reciben más quejas»**

- **Tercera variable:** el **tamaño del hotel** (un hotel grande tiene más personal y también más huéspedes, y por eso más quejas en total).
- **O causalidad inversa:** **contratan más personal donde hay más problemas**.
- **Cómo comprobarlo:** comparar **quejas por cada 100 huéspedes**, que hace justa la comparación.

**c) «Cuanto más gastamos en publicidad, más reservas tenemos»**

- **Tercera variable:** la **temporada o la demanda** (se gasta más cuando se espera más gente).
- **O causalidad inversa:** **se invierte más porque ya hay muchas reservas**.
- **Cómo comprobarlo:** un **experimento**: hacer la campaña solo en algunas islas o semanas **elegidas al azar** y comparar con las que no la tienen (**grupo de control**).

**Qué significa:** **la correlación es una pista, no una prueba**. Para probar una causa hace falta comparar de forma justa o hacer un experimento.

**Ojo con:** responder solo «no hay causalidad». Hay que **proponer qué lo explica** y cómo lo comprobaríamos.

### E11 · Prueba A/B en la web
Datos: versión **A** → 200 visitantes, **20** reservan. Versión **B** → 200 visitantes, **30** reservan.

**La idea en una frase:** B ha ido mejor, pero **¿es una mejora real o ha sido suerte?** Para saberlo calculamos **un rango razonable para la diferencia**: si ese rango incluye el **0** («no hay diferencia»), no podemos estar seguros.

**a) Tasas de conversión**

Paso a paso:
- A: 20 ÷ 200 = 0,10 → **10 %**.
- B: 30 ÷ 200 = 0,15 → **15 %**.
- Diferencia: 15 % − 10 % = **5 puntos**.

**b) El error típico de la diferencia**

Paso a paso:
- Parte de A: 0,10 · 0,90 ÷ 200 = 0,09 ÷ 200 = 0,00045.
- Parte de B: 0,15 · 0,85 ÷ 200 = 0,1275 ÷ 200 = 0,0006375.
- Las sumamos: 0,00045 + 0,0006375 = 0,0010875.
- Raíz cuadrada: **≈ 0,033**.

**c) El intervalo de la diferencia**

Paso a paso:
- 1,96 · 0,033 ≈ 0,065 (6,5 puntos).
- Límite de abajo: 0,05 − 0,065 = **−0,015** (−1,5 %).
- Límite de arriba: 0,05 + 0,065 = **+0,115** (+11,5 %).

**Resultado:** el intervalo va **de −1,5 % a +11,5 %** e **incluye el 0**.

**d) ¿Podemos decir que B es mejor?**

- Como el intervalo **incluye el 0**, B podría ser **igual** que A, o incluso **peor** (−1,5 %).

**Resultado:** **no podemos afirmar** que B sea mejor: la diferencia **podría ser casualidad**.

**¿Qué haríamos?** **No decidir todavía.** Seguir la prueba con **más visitantes** (unas 700 por versión para notar de forma fiable una mejora de 5 puntos) y volver a calcular.

**Qué significa:** un resultado «mejor» en una prueba corta **puede ser suerte**. Decidir demasiado pronto es un riesgo.

**Ojo con:** decir «B es mejor porque 15 > 10» sin mirar el intervalo.

### E12 · Coeficiente de correlación
Datos: 5 alojamientos. Fotos en el anuncio (x, en decenas): **1, 2, 3, 4, 5**. Reservas al mes (y, en decenas): **2, 4, 5, 4, 5**.

**La idea en una frase:** la **correlación r** es un número **entre −1 y 1** que dice **si dos cosas suben juntas** (cerca de 1), **al revés** (cerca de −1) o **no tienen relación** (cerca de 0).

**a) Las medias**

- Media de x: (1 + 2 + 3 + 4 + 5) ÷ 5 = 15 ÷ 5 = **3**.
- Media de y: (2 + 4 + 5 + 4 + 5) ÷ 5 = 20 ÷ 5 = **4**.

**b) Calcular r**

Paso a paso (conviene hacer una tabla):

| x | y | x − 3 | y − 4 | producto | (x − 3)² | (y − 4)² |
|---|---|---|---|---|---|---|
| 1 | 2 | −2 | −2 | 4 | 4 | 4 |
| 2 | 4 | −1 | 0 | 0 | 1 | 0 |
| 3 | 5 | 0 | 1 | 0 | 0 | 1 |
| 4 | 4 | 1 | 0 | 0 | 1 | 0 |
| 5 | 5 | 2 | 1 | 2 | 4 | 1 |
| **Suma** | | | | **6** | **10** | **6** |

- Numerador: **6**.
- Denominador: √(10 · 6) = √60 ≈ 7,746.
- r = 6 ÷ 7,746 ≈ **0,775**.

**Resultado:** r ≈ **0,775**: una relación **positiva y bastante fuerte** (más fotos, más reservas).

**c) r²**

- 0,775² ≈ **0,60**.

**Resultado:** **el 60 % de lo que varían las reservas** se explica de forma lineal por las fotos. El otro 40 %, por otras cosas.

**d) Precauciones**

- Con **solo 5 alojamientos**, un solo dato distinto puede **cambiar mucho** el resultado: es **poco fiable**.
- **Correlación no es causalidad:** puede que los alojamientos **mejor gestionados** pongan más fotos **y** tengan más reservas, sin que las fotos sean la causa.

**Qué significa:** r **mide si van juntas**, no **por qué**.

**Ojo con:** olvidar la raíz del denominador (daría 6 ÷ 60 = 0,1).

---

## Bloque F · Evaluación y paradojas

### E13 · Cuando el acierto engaña
Datos: de **1.000** reservas, **210** se cancelan (21 %). El modelo marca **200** como «se cancelará» y **120** de ellas se cancelan de verdad.

**La idea en una frase:** para saber si un modelo es bueno **no basta con el porcentaje de aciertos**. Hay que ver **en qué acierta y en qué falla**, con una tabla.

**a) La matriz de confusión**

Paso a paso:
- **Verdaderos positivos (VP):** avisó de cancelación y **sí** se canceló: **120**.
- **Falsos positivos (FP):** avisó de cancelación pero **no** se canceló: 200 − 120 = **80**.
- **Falsos negativos (FN):** **no** avisó pero **sí** se canceló: las canceladas son 210 y ya hemos pillado 120, así que 210 − 120 = **90**.
- **Verdaderos negativos (VN):** no avisó y **no** se canceló: las no canceladas son 790 y 80 de ellas dieron falsa alarma, así que 790 − 80 = **710**.
- Comprobamos: 120 + 80 + 90 + 710 = **1.000** ✓.

**b) Tres métricas**

Paso a paso:
- **Exactitud** (aciertos entre todas): (120 + 710) ÷ 1.000 = **0,83** → 83 %.
- **Precisión** (de las que avisa, cuántas aciertan): 120 ÷ 200 = **0,60** → 60 %.
- **Recall** (de las cancelaciones reales, cuántas pilla): 120 ÷ 210 ≈ **0,57** → 57 %.

**Resultado:** exactitud **83 %**, precisión **60 %**, recall **57 %**.

**c) Un «modelo» que siempre dice «no se cancela»**

- Acierta **todas las no canceladas**: 790 de 1.000 = **79 %**.
- Pero **no detecta ninguna cancelación**.

**Resultado:** **79 %** de exactitud sin hacer **nada útil**. El modelo real (83 %) apenas mejora esa cifra, pero **sí detecta el 57 % de las cancelaciones**. **La exactitud engaña cuando hay muchos más «no» que «sí».**

**d) ¿Qué métrica importa más si recepción llama a cada reserva marcada?**

Respuesta abierta; lo importante es **razonar con el coste**:
- Si **llamar es barato** y **perder una reserva es caro**: importa el **recall** (no dejar escapar ninguna).
- Si **cada llamada molesta o cuesta dinero**: importa la **precisión** (llamar solo cuando estemos bastante seguros).

**Qué significa:** **no existe «la mejor métrica»**: se elige según lo que cuesta cada error, y **eso se decide con el cliente**.

**Ojo con:** quedarse con la exactitud «porque es la más alta».

### E14 · Una pequeña paradoja
Datos: dos agencias, A y B, y cuántas consultas terminan en reserva:

| | Clientes habituales | Clientes nuevos |
|---|---|---|
| Agencia A | 18 de 20 | 480 de 800 |
| Agencia B | 640 de 800 | 8 de 20 |

**La idea en una frase:** a veces **A gana en cada tipo de cliente y, aun así, B gana en el total**. Para entender cómo, hay que mirar **qué tipo de clientes atiende cada agencia**.

**a) Porcentaje dentro de cada tipo**

Paso a paso:
- **Habituales:** A = 18 ÷ 20 = **90 %**; B = 640 ÷ 800 = **80 %**.
- **Nuevos:** A = 480 ÷ 800 = **60 %**; B = 8 ÷ 20 = **40 %**.

**Resultado:** **A es mejor en los dos tipos** (90 > 80 y 60 > 40).

**b) Porcentaje total**

Paso a paso (primero **sumamos**, después **dividimos**):
- A: éxitos 18 + 480 = 498; consultas 20 + 800 = 820. 498 ÷ 820 ≈ **60,7 %**.
- B: éxitos 640 + 8 = 648; consultas 800 + 20 = 820. 648 ÷ 820 ≈ **79,0 %**.

**Resultado:** **B parece mejor** (79 % > 60,7 %). Al revés que antes.

**c) ¿Cómo puede ser?**

- Los clientes **nuevos** son **más difíciles** de convertir: ambas agencias sacan menos con ellos.
- **A atiende casi solo a clientes nuevos** (800 de 820).
- **B atiende casi solo a clientes habituales** (800 de 820), que son **fáciles**.

**Resultado:** B parece mejor **porque le tocan los clientes fáciles**, no porque trabaje mejor.

**d) ¿Qué comparación es la justa?**

**Resultado:** comparar **dentro de cada tipo de cliente**. Frase para el director: *«A convierte mejor que B con clientes del mismo tipo; B parece mejor porque atiende sobre todo a clientes fáciles.»*

**e) Nombre**

Esto es la **paradoja de Simpson**: **una tendencia global que se invierte al separar los datos por un tipo oculto** (aquí, el tipo de cliente).

**Qué significa:** **un porcentaje total puede engañar**. Antes de comparar, preguntad: «¿se están comparando cosas del mismo tipo?».

**Ojo con:** calcular el total **promediando** 90 % y 60 %. Hay que **sumar los éxitos y los intentos** y dividir al final.

---

## Un último consejo

> Si una explicación no os entra, **dibujad**: una flecha, una cuesta, una tabla o una tarta. Y recordad que lo importante de cada ejercicio es **entender qué significa el resultado** para un modelo de IA o para las reservas de TurisData.
