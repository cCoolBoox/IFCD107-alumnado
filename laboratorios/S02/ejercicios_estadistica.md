# Hoja de ejercicios 2 · Estadística, probabilidad, Bayes, muestreo y sesgo (UD 1a.5)

**Tiempo:** unos 100 minutos completa; se reparte entre los ratos de la teoría y el trabajo en equipo · **Cómo:** en papel y con calculadora. Los datos son **inventados** para practicar (no son estadísticas reales del turismo). Las soluciones las tiene el docente.
Graduación: ★ básico · ★★ medio · ★★★ reto.

> **Consejo:** en probabilidad, pasad todo a **frecuencias naturales** ("de cada 1.000 reservas…"). Se entiende mucho mejor que con fórmulas.

## Bloque A · Estadística descriptiva

### E1 ★ · Media, mediana y cuartiles
Estos son los **ingresos (€)** de 8 reservas de un apartamento:
**90, 95, 100, 100, 105, 110, 120, 480**
a) Calculad la **media** y la **mediana**. ¿Cuál describe mejor "una reserva normal"? ¿Por qué?
b) Calculad Q1 (mediana de la mitad inferior) y Q3 (mediana de la mitad superior) y el **rango intercuartílico** IQR = Q3 − Q1.
c) Una regla habitual dice que un dato es atípico (*outlier*) si supera **Q3 + 1,5·IQR**. ¿Lo es 480?
d) Calculad la media **sin** el 480. ¿Cuánto cambia?

### E2 ★ · Varianza y desviación típica
Las **noches** de 8 reservas: **2, 4, 4, 4, 5, 5, 7, 9**.
a) Calculad la media.
b) Calculad la **varianza** (media de las diferencias al cuadrado respecto de la media, dividiendo entre 8) y la **desviación típica**.
c) Si estos 8 datos fueran una **muestra** de todas las reservas, la varianza muestral divide entre n − 1 = 7. Calculadla y comparadla.
d) ¿Qué significa en llano una desviación típica de 2 noches?

## Bloque B · Probabilidad y distribuciones

### E3 ★★ · Probabilidad condicionada
De **200 reservas** de un mes: 120 son **directas** (30 canceladas) y 80 son de la **intermediaria** (24 canceladas).
a) Construid una tabla de contingencia (canal × cancelada sí/no).
b) P(cancelada), P(cancelada | directa) y P(cancelada | intermediaria).
c) Si sabemos que una reserva **se ha cancelado**, ¿cuál es la probabilidad de que fuera de la intermediaria?
d) ¿Son "canal" y "cancelación" independientes? Razonad con los números.

### E4 ★★ · Distribución binomial
Suponed que cada reserva flexible se cancela con probabilidad **0,2**, independientemente de las demás. Un alojamiento tiene **10** reservas flexibles para un fin de semana.
a) ¿Cuántas cancelaciones esperáis de media?
b) Probabilidad de **exactamente 2** cancelaciones. (Fórmula: C(10,2)·0,2²·0,8⁸, con C(10,2) = 45.)
c) Probabilidad de **ninguna** cancelación (0,8¹⁰).
d) Probabilidad de **al menos una**.

### E5 ★★ · Distribución normal
La ocupación diaria de un alojamiento tiene media **70 %** y desviación típica **10 puntos**; suponed que sigue una curva normal.
a) Usando la regla 68-95-99,7: ¿entre qué valores está **el 95 %** de los días?
b) ¿Cuántos puntos por encima de la media (en desviaciones típicas) está un día con **95 %** de ocupación? (es su *z* = (95 − 70)/10).
c) Un día con z = 2,5 ocurre con probabilidad de solo un **0,6 %** (una cola). Aproximadamente, ¿cuántos días al año?
d) Cuidado: la ocupación no puede pasar de 100 %. ¿Qué limitación tiene aquí el modelo normal?

### E6 ★ · Distribución uniforme
Los huéspedes llegan entre las **16:00 y las 20:00**, sin preferencias (uniforme).
a) Probabilidad de que lleguen **antes de las 17:30**.
b) Probabilidad de llegar entre las **18:00 y las 19:00**.
c) ¿Cuál es la hora media de llegada?

## Bloque C · Teorema de Bayes

### E7 ★★★ · El detector de reservas fraudulentas
TurisData prueba un detector de fraude. Datos: **1 %** de las reservas son fraudulentas. Si una reserva **es** fraudulenta, el detector salta el **90 %** de las veces. Si **no** lo es, salta el **5 %** de las veces (falsa alarma).
a) Imaginad **10.000 reservas**. ¿Cuántas son fraudulentas? ¿Cuántas de ellas salta la alarma? ¿Cuántas honestas saltan?
b) De todas las que saltan, ¿qué **proporción** es realmente fraudulenta?
c) Un directivo dice: "Es un 90 % fiable, así que si salta, el 90 % es fraude". ¿Qué tiene mal?
d) ¿Qué pasaría si el fraude fuera del **10 %** de las reservas (mismos porcentajes)?
e) Escribid el resultado con la fórmula de Bayes: P(F|A) = P(A|F)·P(F) / P(A).

## Bloque D · Muestreo y sesgo

### E8 ★★ · ¿Qué sesgo tiene esta muestra?
Para cada situación, decid **a quién falta**, **qué sesgo** hay y **cómo mejorarlo**.
a) Encuesta de satisfacción entregada a la salida, **solo a quienes pasan por el desayuno**.
b) La media de las reseñas online de un alojamiento, que solo escriben quienes se animan.
c) "Los alojamientos con más de 10 años abiertos tienen todos buena valoración, luego la buena valoración garantiza durar": el estudio solo mira los que siguen abiertos.
d) Un correo a "quienes dejaron su email en la web" preguntando "¿estás satisfecho?".

### E9 ★★ · Tamaño de muestra y margen de error
Se pregunta a **400** huéspedes elegidos al azar y el **62 %** dice que volvería.
a) Calculad el **error típico** √(p(1−p)/n) con p = 0,62.
b) Calculad un intervalo de confianza aproximado del 95 %: p ± 1,96·(error típico).
c) ¿Qué tamaño de muestra haría falta para un margen de **± 2 puntos** en el peor caso (p = 0,5)? Usad n = (1,96·0,5 / margen)².
d) Si **cuadruplicamos** la muestra, ¿cuánto baja el margen?

## Bloque E · Correlación, causalidad y contraste

### E10 ★★ · ¿Correlación o causalidad?
En cada frase, proponed **una tercera variable** (variable de confusión) o una **causalidad inversa** que explique la relación, y cómo comprobaríais la causa real:
a) "Los meses con más helados vendidos en la piscina tienen más reservas."
b) "Los hoteles con más personal reciben más quejas."
c) "Cuanto más gastamos en publicidad, más reservas tenemos."

### E11 ★★★ · Prueba A/B en la web
La web muestra la versión **A** a 200 visitantes (20 reservan) y la **B** a otros 200 (30 reservan).
a) Calculad las tasas de conversión y su diferencia.
b) El error típico de la diferencia es √(pA(1−pA)/200 + pB(1−pB)/200). Calculadlo.
c) Calculad el intervalo de confianza del 95 % de la diferencia: (pB − pA) ± 1,96·(error típico). ¿Incluye el 0?
d) ¿Podemos afirmar que B es mejor? ¿Qué haríais? (Pensad en el tamaño de muestra y en el riesgo de decidir por casualidad.)

### E12 ★★ · Coeficiente de correlación
Cinco alojamientos: nº de fotos en el anuncio (x, en decenas) y reservas al mes (y, en decenas):
x = 1, 2, 3, 4, 5 · y = 2, 4, 5, 4, 5
a) Calculad las medias de x e y.
b) Calculad r = Σ(x−x̄)(y−ȳ) / √(Σ(x−x̄)²·Σ(y−ȳ)²).
c) Calculad r² e interpretadlo ("proporción de variación de y explicada linealmente por x").
d) ¿Qué precauciones hay que tomar con solo 5 datos y con la causalidad?

## Bloque F · Evaluación y paradojas

### E13 ★★ · Cuando el acierto engaña
El 21 % de las reservas de TurisData se cancela. De **1.000** reservas, un modelo marca **200** como "se cancelará"; de ellas **120** se cancelan de verdad.
a) Construid la **matriz de confusión** (verdaderos positivos, falsos positivos, falsos negativos, verdaderos negativos).
b) Calculad la **exactitud**, la **precisión** (VP/(VP+FP)) y la **exhaustividad o recall** (VP/(VP+FN)).
c) ¿Qué exactitud tiene un "modelo" que siempre dice "no se cancela"? ¿Qué os dice sobre la exactitud?
d) ¿Cuál de las tres métricas os importa más si la recepción llama a cada reserva marcada? Razonad.

### E14 ★★★ · Una pequeña paradoja
Dos agencias, A y B, gestionan consultas de reserva. Miden qué porcentaje termina en reserva confirmada, separando por tipo de cliente:

| | Clientes habituales | Clientes nuevos |
|---|---|---|
| Agencia A | 18 de 20 | 480 de 800 |
| Agencia B | 640 de 800 | 8 de 20 |

a) Calculad el porcentaje de éxito de A y de B **dentro de cada tipo de cliente**. ¿Quién es mejor en cada uno?
b) Calculad el porcentaje **total** de A y de B. ¿Quién parece mejor ahora?
c) ¿Cómo puede ser? ¿Qué cambia entre las agencias en el **tipo de clientes que atienden**?
d) ¿Qué comparación es la justa? ¿Cómo lo explicaríais en una frase al director?
e) *Esto es la **paradoja de Simpson**. La volveréis a ver en el reto del sprint con los datos reales de TurisData.*

---

## Autoevaluación
- [ ] Distingo media, mediana y sus efectos con valores atípicos
- [ ] Sé calcular probabilidades condicionadas con una tabla
- [ ] Sé aplicar Bayes con frecuencias naturales
- [ ] Reconozco al menos tres tipos de sesgo de muestreo
- [ ] Entiendo qué es un intervalo de confianza y qué no
- [ ] Sé explicar por qué correlación no implica causalidad
- [ ] Sé explicar la paradoja de Simpson con un ejemplo

## Vocabulario
**Media · mediana · cuartil · desviación típica · probabilidad condicionada · independencia · binomial · normal · uniforme · Bayes · muestra · sesgo de selección · sesgo de supervivencia · intervalo de confianza · contraste · correlación · variable de confusión · matriz de confusión · paradoja de Simpson**
