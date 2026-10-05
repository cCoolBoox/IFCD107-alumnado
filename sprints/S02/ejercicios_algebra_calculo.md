# Hoja de ejercicios 1 · Álgebra lineal, derivadas y gradiente (UD 1a.4)

**Tiempo:** unos 90 minutos completa; en clase tenéis **1 h** (empezad por los ★ y ★★ y terminad en equipo) · **Cómo:** en **papel** (bolígrafo y calculadora sencilla) y, donde se indica, con **Desmos** (desmos.com/calculator) o **GeoGebra** (geogebra.org/classic). Trabajad en parejas; las soluciones las tiene el docente y las revisaremos juntos.
**Entregable del sprint:** esta hoja + la de estadística, con vuestras respuestas y, si os atascáis, **una nota de dónde**.

> **No hace falta ser matemático.** Buscamos entender **qué significa** cada operación para un modelo de IA. Cada ejercicio está graduado: ★ básico, ★★ medio, ★★★ reto.

## Bloque A · Álgebra lineal: vectores y matrices

### M1 ★ · Vectores
Sean **v = (3, −1, 2)** y **w = (1, 4, −2)**. Calculad:
a) v + w  b) 2v − w  c) la longitud (norma) de v, |v| = √(3² + (−1)² + 2²).

### M2 ★ · Producto escalar y modelos de precio
a) Calculad el **producto escalar** v · w (suma de multiplicar componente a componente).
b) Un modelo muy simple de precio por reserva es **precio = pesos · características + base**. Las características son **x = (noches, huéspedes, temporada alta)** con temporada alta = 1 (sí) o 0 (no). Los pesos son **w = (60, 15, 40)** y la base **b = 20**. ¿Cuánto cuesta una reserva de 3 noches, 2 huéspedes en temporada alta?
c) ¿Y la misma reserva fuera de temporada alta?
d) ¿Qué significa el peso "40" en lenguaje llano?

### M3 ★★ · Producto de matrices
Sean **A = [[1, 2], [3, 4]]** y **B = [[0, 1], [1, 0]]**.
a) Calculad **AB** y **BA**.
b) ¿Son iguales? ¿Qué os dice sobre el orden en el producto de matrices?
c) ¿Qué hace B al multiplicarla por A por la derecha (AB)? ¿Y por la izquierda (BA)?

### M4 ★★ · Dimensiones, transpuesta y matriz por vector
Sea **A = [[2, 0, 1], [1, 3, −1]]** (2 filas × 3 columnas) y **x = (1, 2, 3)** como vector columna.
a) ¿Qué tamaño tiene A·x? Calculadlo.
b) Escribid la transpuesta **Aᵀ** e indicad su tamaño.
c) Calculad **A·Aᵀ** (¿qué tamaño tiene?).
d) ¿Se puede calcular x·A (poniendo x, columna de 3 filas, a la izquierda)? ¿Por qué?

### M5 ★★ · Inversa y sistema de ecuaciones
Sea **A = [[2, 1], [5, 3]]**.
a) Calculad su determinante (2·3 − 1·5).
b) Comprobad que **A⁻¹ = [[3, −1], [−5, 2]]** multiplicando A·A⁻¹.
c) Un bar de la piscina vende bonos: **2 menús infantiles + 1 menú adulto = 4 €** y **5 menús infantiles + 3 adultos = 11 €**. Escribid el sistema como **A·x = b** con x = (p, q) el precio de cada menú. Resolvedlo con la inversa.

### M6 ★★ · Autovectores (la idea)
Sea **A = [[2, 0], [0, 3]]**.
a) Calculad A·(1, 0), A·(0, 1) y A·(1, 1).
b) ¿Para qué vectores el resultado es **el mismo vector estirado**? ¿Cuánto se estira cada uno? (Son los **autovectores**; los factores, **autovalores**.)
c) Pensad: si tenemos una nube de datos alargada en una dirección, ¿qué dirección querríamos "conservar" para resumir los datos? (Es la idea del PCA, que veremos en el Sprint 9.)

## Bloque B · Cálculo: derivadas y gradiente

### M7 ★ · Derivada y mínimo
Sea **f(x) = 3x² − 12x + 5**.
a) Calculad f'(x).
b) ¿Cuánto vale la pendiente en x = 0? ¿La función sube o baja ahí?
c) ¿En qué punto la pendiente es 0? Calculad el valor mínimo de f.
d) **Desmos:** dibujad f y la recta tangente en x = 0. Comprobad que su pendiente coincide con vuestra respuesta.

### M8 ★★ · Regla de la cadena
a) Derivad **g(x) = (2x + 1)³**. Calculad g'(0).
b) Derivad **h(x) = e^(−x²)** (la campana de Gauss sin normalizar). Calculad h'(1) con dos decimales.
c) La regla de la cadena es lo que permite propagar el error por las capas de una red neuronal (*backpropagation*). Explicad con vuestras palabras: "si y = f(u) y u = g(x), ¿cómo cambia y si cambia x?".

### M9 ★★ · Derivadas parciales y gradiente
Sea **f(x, y) = x² + 3xy + y²**.
a) Calculad **∂f/∂x** y **∂f/∂y**.
b) Calculad el **gradiente** ∇f en el punto (1, 2).
c) El gradiente apunta hacia donde la función **crece más rápido**. ¿Hacia dónde tendríamos que movernos para **bajar** más rápido?
d) ¿Cuánto vale el gradiente en (0, 0)? ¿Qué significa?

### M10 ★★ · Descenso del gradiente con una variable
Queremos minimizar **f(x) = x²** (mínimo en x = 0) con la regla **x_nuevo = x − η · f'(x)**, donde η es el **paso** (*learning rate*). Empezamos en **x₀ = 4**.
a) Con **η = 0,25**, calculad x₁, x₂, x₃.
b) Con **η = 0,5**, ¿cuánto vale x₁?
c) Con **η = 1,1**, calculad x₁ y x₂. ¿Qué observáis?
d) Explicad con vuestras palabras qué pasa si el paso es **demasiado pequeño** y qué si es **demasiado grande**.
e) **Desmos/GeoGebra:** cread una lista con los puntos (x_k, x_k²) del apartado a) y dibujadlos sobre la parábola. ¿Cómo se acercan al mínimo?

### M11 ★★★ · Función de coste y un paso de descenso
Tenemos tres reservas (x = nº de noches, y = precio en cientos de euros): **(1, 2), (2, 4), (3, 6)**. Ajustamos el modelo **ŷ = w·x**.
a) Con **w = 1**, calculad los errores (ŷ − y) y el **error cuadrático medio**: J(w) = (1/3)·Σ(ŷ − y)².
b) La derivada es **dJ/dw = (2/3)·Σ (ŷ − y)·x**. Calculadla en w = 1.
c) Haced **un paso** de descenso con **η = 0,05**: w_nuevo = w − η·dJ/dw.
d) Calculad el nuevo error. ¿Ha bajado? ¿Cuál creéis que es el valor de w que hace J = 0?
e) **Desmos:** dibujad J(w) como función de w (parábola) y marcad w = 1 y el nuevo w. ¿Se acerca al mínimo?

### M12 ★★★ · Explorar una función con Desmos/GeoGebra
Sea **f(x) = x³ − 3x**.
a) Calculad f'(x) y los puntos donde f'(x) = 0.
b) Decid cuáles son máximo local y cuáles mínimo local (mirad el signo de f' antes y después, o el dibujo).
c) Calculad la tangente en x = 2 (necesitáis f(2) y f'(2)) y comprobadla en Desmos.
d) **Reflexión:** ¿puede el descenso del gradiente quedarse en un mínimo local? ¿A dónde llega el descenso del gradiente (paso pequeño) si empezamos en x = 2? ¿Y en x = −0,5? ¿Y en x = −2?

---

## Rúbrica de autoevaluación (marcad)
- [ ] Sé calcular un producto escalar y explicar qué mide
- [ ] Sé multiplicar matrices y comprobar sus dimensiones
- [ ] Sé derivar funciones sencillas y usar la regla de la cadena
- [ ] Sé calcular un gradiente y decir hacia dónde "baja" la función
- [ ] Sé aplicar el descenso del gradiente a mano y explicar el efecto del paso
- [ ] He usado Desmos o GeoGebra para comprobar al menos dos resultados

## Vocabulario del sprint
**Vector · matriz · producto escalar · producto matricial · transpuesta · inversa · autovector · función de coste · derivada · derivada parcial · gradiente · descenso del gradiente · paso (*learning rate*)**
