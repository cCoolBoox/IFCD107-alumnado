# Soluciones paso a paso · Hoja 1 · Álgebra lineal, derivadas y gradiente

Aquí tenéis las soluciones de la hoja [`ejercicios_algebra_calculo.md`](ejercicios_algebra_calculo.md), **explicadas paso a paso** y sin dar nada por sabido (M1 a M12).

## Cómo usarlas

- **Primero intentad cada ejercicio vosotros**, en papel, sin mirar. Equivocarse también es aprender.
- **Después comparad** con la solución y **corregid con otro color**.
- Si vuestro resultado es distinto, **buscad en qué paso se separa**: ahí está lo que hay que repasar. Anotadlo como «mi nota de dónde me atasqué».
- No copiéis el resultado: lo que importa es **entender el camino** y poder **explicarlo con vuestras palabras**.

## Cómo está organizado cada ejercicio

- **La idea en una frase:** qué se está haciendo, sin símbolos.
- **Paso a paso:** cada operación en una línea, con las cuentas a la vista.
- **Resultado:** la respuesta final.
- **Qué significa:** la respuesta traducida al caso (reservas, precios, modelos de IA).
- **Ojo con:** el error que más se repite.

## Cuatro palabras antes de empezar

- **Vector:** una **lista de números** en orden. Por ejemplo, (3, −1, 2) son tres números. Cada número se llama **componente**.
- **Matriz:** una **tabla de números** con filas (en horizontal) y columnas (en vertical).
- **Derivada:** un número que dice **lo empinada que es una cuesta** en un punto. Si es positiva, la cuesta sube; si es negativa, baja; si es cero, es llano.
- **Gradiente:** lo mismo que la derivada, pero cuando hay **más de una variable**. Es una lista de pendientes, una por cada dirección.

## Regla práctica para todo el bloque

> **Despacio y escribiendo.** Una cuenta por línea. Si un número negativo da miedo, ponedlo **entre paréntesis**: (−1)·4, no −1·4.

---

## Bloque A · Álgebra lineal: vectores y matrices

### M1 · Vectores
Datos: **v = (3, −1, 2)** y **w = (1, 4, −2)**.

**La idea en una frase:** un vector es una lista de números, y se puede **sumar, restar, multiplicar por un número** y medir su longitud, **componente a componente**.

**a) v + w**

Paso a paso:
- Sumamos **los primeros** números de cada vector: 3 + 1 = 4.
- Sumamos **los segundos**: (−1) + 4 = 3.
- Sumamos **los terceros**: 2 + (−2) = 0.

**Resultado:** v + w = **(4, 3, 0)**.

**b) 2v − w**

Paso a paso:
- Primero **2v**: multiplicamos cada número de v por 2. 2·3 = 6; 2·(−1) = −2; 2·2 = 4. Sale (6, −2, 4).
- Ahora restamos w, **uno a uno**: 6 − 1 = 5; (−2) − 4 = −6; 4 − (−2) = 4 + 2 = 6.

**Resultado:** 2v − w = **(5, −6, 6)**.

**c) La longitud de v**

Paso a paso:
- Elevamos cada número **al cuadrado** (multiplicarlo por sí mismo): 3² = 9; (−1)² = **1** (un negativo por un negativo da positivo); 2² = 4.
- Sumamos: 9 + 1 + 4 = 14.
- Hacemos la **raíz cuadrada** (el número que multiplicado por sí mismo da 14): √14 ≈ 3,74.

**Resultado:** |v| ≈ **3,74**.

**Qué significa:** la longitud de un vector es **«cuánto mide la flecha»** desde el origen hasta el punto. Sumar vectores es **ir primero por uno y luego por el otro**.

**Ojo con:** el signo de (−1)². Da +1, no −1.

### M2 · Producto escalar y modelo de precio

**La idea en una frase:** el **producto escalar** es **multiplicar los números de dos listas por parejas y sumar**. Es la operación que hace un modelo para calcular un precio: cada característica se multiplica por **lo que pesa** y se suma todo.

**a) v · w**

Paso a paso:
- Multiplicamos por parejas: 3·1 = 3; (−1)·4 = −4; 2·(−2) = −4.
- Sumamos: 3 − 4 − 4 = −5.

**Resultado:** v · w = **−5**.

**b) Precio de la reserva de 3 noches, 2 huéspedes, temporada alta**

Datos: x = (3, 2, 1) (el 1 significa «sí es temporada alta»), pesos w = (60, 15, 40), base b = 20.

Paso a paso:
- **Noches:** 3 · 60 = 180 €.
- **Huéspedes:** 2 · 15 = 30 €.
- **Temporada alta:** 1 · 40 = 40 €.
- Sumamos las tres partes: 180 + 30 + 40 = 250.
- **Añadimos la base:** 250 + 20 = 270.

**Resultado:** **270 €**.

**c) La misma reserva fuera de temporada alta**

Ahora x = (3, 2, 0).
- 180 + 30 + 0 = 210; 210 + 20 = 230.

**Resultado:** **230 €**.

**d) ¿Qué significa el peso «40»?**

Comparamos b) y c): la **única diferencia** es la temporada alta, y el precio sube de 230 a 270 € (40 € más).

**Resultado:** el 40 es **lo que añade cada reserva por estar en temporada alta**, manteniendo lo demás igual.

**Qué significa:** cada peso dice **«cuánto pesa» esa característica** en el precio. Un modelo de IA **aprende** esos pesos mirando muchos datos.

**Ojo con:** olvidar la base (20). Si sale 250, falta sumarla.

### M3 · Producto de matrices
Datos: **A = [[1, 2], [3, 4]]** y **B = [[0, 1], [1, 0]]** (la primera fila entre corchetes es la fila de arriba).

**La idea en una frase:** para multiplicar dos matrices, cada casilla del resultado sale de **una fila de la primera por una columna de la segunda**, como un producto escalar.

**a) AB**

Cada casilla = (fila de A) · (columna de B).
- Casilla de arriba a la izquierda: fila (1, 2) con columna (0, 1): 1·0 + 2·1 = 2.
- Arriba a la derecha: fila (1, 2) con columna (1, 0): 1·1 + 2·0 = 1.
- Abajo a la izquierda: fila (3, 4) con columna (0, 1): 3·0 + 4·1 = 4.
- Abajo a la derecha: fila (3, 4) con columna (1, 0): 3·1 + 4·0 = 3.

**Resultado:** AB = **[[2, 1], [4, 3]]**.

**a) BA** (ahora **al revés**: filas de B por columnas de A)
- Arriba a la izquierda: fila (0, 1) con columna (1, 3): 0·1 + 1·3 = 3.
- Arriba a la derecha: fila (0, 1) con columna (2, 4): 0·2 + 1·4 = 4.
- Abajo a la izquierda: fila (1, 0) con columna (1, 3): 1·1 + 0·3 = 1.
- Abajo a la derecha: fila (1, 0) con columna (2, 4): 1·2 + 0·4 = 2.

**Resultado:** BA = **[[3, 4], [1, 2]]**.

**b) ¿Son iguales?**

Comparamos: [[2, 1], [4, 3]] y [[3, 4], [1, 2]]. **No son iguales.**

**Qué significa:** con matrices **el orden importa**. A·B no es B·A. (Con números normales, 2·3 y 3·2 sí dan igual; con matrices, no.)

**c) ¿Qué hace B?**

Miramos AB al lado de A:
- A = [[1, 2], [3, 4]] y AB = [[2, 1], [4, 3]]: en cada fila, el **2 y el 1 han cambiado de sitio**. Se han intercambiado las **columnas**.
- BA = [[3, 4], [1, 2]]: **la fila de arriba (3, 4) y la de abajo (1, 2) se han cambiado de sitio**. Se han intercambiado las **filas**.

**Qué significa:** una matriz es una **máquina que transforma** a otra. Esta máquina, B, es la que **intercambia**: por la derecha cambia columnas y por la izquierda cambia filas.

**Ojo con:** multiplicar casilla con casilla (1·0, 2·1…). Eso **no** es el producto de matrices.

### M4 · Dimensiones, transpuesta y matriz por vector
Datos: **A = [[2, 0, 1], [1, 3, −1]]** (2 filas y 3 columnas) y **x = (1, 2, 3)** escrito como columna.

**La idea en una frase:** antes de multiplicar, **se comprueba el tamaño**. «Filas × columnas» del primero **con** «filas × columnas» del segundo: **los números de en medio deben ser iguales**.

**a) Tamaño de A·x y cálculo**

Paso a paso:
- A es de **2×3** y x es de **3×1**. Los de en medio son 3 y 3: **coinciden**, se puede.
- El resultado tiene el tamaño de los de fuera: **2×1** (dos números en columna).
- Primera fila de A con x: 2·1 + 0·2 + 1·3 = 2 + 0 + 3 = 5.
- Segunda fila de A con x: 1·1 + 3·2 + (−1)·3 = 1 + 6 − 3 = 4.

**Resultado:** tamaño **2×1**; A·x = **(5, 4)**.

**b) La transpuesta Aᵀ**

**Transponer** es **cambiar filas por columnas**: la primera fila pasa a ser la primera columna, etc.
- Primera fila de A: (2, 0, 1) → primera columna de Aᵀ.
- Segunda fila de A: (1, 3, −1) → segunda columna de Aᵀ.

**Resultado:** Aᵀ = **[[2, 1], [0, 3], [1, −1]]**, de tamaño **3×2** (3 filas y 2 columnas).

**c) A·Aᵀ**

Paso a paso:
- Tamaños: A es 2×3 y Aᵀ es 3×2. Los de en medio son 3 y 3: se puede. Resultado: **2×2**.
- Arriba a la izquierda: fila 1 de A (2, 0, 1) con columna 1 de Aᵀ (2, 0, 1): 4 + 0 + 1 = 5.
- Arriba a la derecha: fila 1 de A (2, 0, 1) con columna 2 de Aᵀ (1, 3, −1): 2 + 0 − 1 = 1.
- Abajo a la izquierda: fila 2 de A (1, 3, −1) con columna 1 de Aᵀ (2, 0, 1): 2 + 0 − 1 = 1.
- Abajo a la derecha: fila 2 de A (1, 3, −1) con columna 2 de Aᵀ (1, 3, −1): 1 + 9 + 1 = 11.

**Resultado:** A·Aᵀ = **[[5, 1], [1, 11]]**.

**d) ¿Se puede x·A?**

- x es 3×1 y A es 2×3. Los de en medio: **1 y 2**. **No coinciden.**

**Resultado:** **no se puede**.

**Qué significa:** una multiplicación de matrices solo existe si **encajan** como piezas. Comprobar los tamaños antes evita errores y es lo primero que hace un programa (NumPy da un error de «dimensiones» si no encajan).

**Ojo con:** escribir la transpuesta con los números sin cambiar de fila a columna.

### M5 · Inversa y sistema de ecuaciones
Datos: **A = [[2, 1], [5, 3]]**.

**La idea en una frase:** la **inversa** de una matriz es la que **deshace** lo que hace la matriz, como restar deshace sumar. Sirve para **resolver ecuaciones** con varias incógnitas a la vez.

**a) El determinante**

Paso a paso (en una matriz 2×2, **diagonal principal menos la otra diagonal**):
- Diagonal principal: 2·3 = 6.
- Otra diagonal: 1·5 = 5.
- Restamos: 6 − 5 = 1.

**Resultado:** determinante = **1**. (Si fuera 0, no habría inversa.)

**b) Comprobar la inversa**

Multiplicamos A por la matriz propuesta A⁻¹ = [[3, −1], [−5, 2]], fila por columna:
- Arriba a la izquierda: 2·3 + 1·(−5) = 6 − 5 = 1.
- Arriba a la derecha: 2·(−1) + 1·2 = −2 + 2 = 0.
- Abajo a la izquierda: 5·3 + 3·(−5) = 15 − 15 = 0.
- Abajo a la derecha: 5·(−1) + 3·2 = −5 + 6 = 1.

**Resultado:** sale **[[1, 0], [0, 1]]**, la matriz **identidad** (el «1» de las matrices). Por eso A⁻¹ es de verdad la inversa.

**c) El problema del bar**

Paso a paso:
- Llamamos **p** al precio del menú infantil y **q** al del adulto.
- Primer bono: 2p + 1q = 4.
- Segundo bono: 5p + 3q = 11.
- En forma de matrices: **A · x = b**, con A = [[2, 1], [5, 3]], x = (p, q) y b = (4, 11).
- Para despejar x, **multiplicamos por la inversa**: x = A⁻¹ · b.
- Primera componente: 3·4 + (−1)·11 = 12 − 11 = 1.
- Segunda componente: (−5)·4 + 2·11 = −20 + 22 = 2.

**Resultado:** p = **1 €** (menú infantil) y q = **2 €** (menú adulto).

**Comprobamos** en las dos ecuaciones: 2·1 + 2 = 4 ✓ y 5·1 + 3·2 = 5 + 6 = 11 ✓.

**Qué significa:** la inversa permite **«despejar» varias incógnitas a la vez**. Es la versión con matrices de dividir entre un número.

**Ojo con:** dejar la respuesta como «(1, 2)» sin decir **qué es cada número**.

### M6 · Autovectores (la idea)
Datos: **A = [[2, 0], [0, 3]]**.

**La idea en una frase:** una matriz **transforma vectores** (los gira, los estira…). Un **autovector** es un vector que la matriz **solo estira, sin cambiarle la dirección**; el **autovalor** es **cuánto** lo estira.

**a) Las tres multiplicaciones**

Paso a paso (fila por vector):
- A·(1, 0): 2·1 + 0·0 = 2 y 0·1 + 3·0 = 0 → **(2, 0)**.
- A·(0, 1): 2·0 + 0·1 = 0 y 0·0 + 3·1 = 3 → **(0, 3)**.
- A·(1, 1): 2·1 + 0·1 = 2 y 0·1 + 3·1 = 3 → **(2, 3)**.

**b) ¿Cuáles solo se estiran?**

- (1, 0) → (2, 0): es **el mismo vector multiplicado por 2**. Se estira ×2.
- (0, 1) → (0, 3): es **el mismo vector multiplicado por 3**. Se estira ×3.
- (1, 1) → (2, 3): **ya no es un múltiplo** de (1, 1): ha **cambiado de dirección**.

**Resultado:** autovectores (1, 0) y (0, 1); autovalores **2** y **3**.

**c) La nube de datos**

Imaginad la nube de puntos como un **balón de rugby**. Para resumirla con una sola línea, queremos la dirección **en la que se extiende más**.

**Resultado:** conservar la **dirección en la que los datos varían más**. Esa es la idea del **PCA** (Sprint 9).

**Qué significa:** los autovectores son **las direcciones «naturales»** de una transformación. Se usan para **resumir datos** quedándonos con lo importante.

**Ojo con:** pensar que (1, 1) también se estira. Cambia de dirección, así que **no** es autovector.

---

## Bloque B · Cálculo: derivadas y gradiente

### M7 · Derivada y mínimo
Datos: **f(x) = 3x² − 12x + 5**.

**La idea en una frase:** la **derivada** nos dice **cómo de empinada es la cuesta** de la gráfica en cada punto. Donde la pendiente es **cero**, la gráfica se aplana: allí hay un **mínimo** (el fondo del valle) o un máximo.

**Regla que necesitamos:** la derivada de **xⁿ** es **n·xⁿ⁻¹** (se baja el exponente multiplicando y se resta 1). La de un número solo (5) es 0, y la de **12x** es 12.

**a) La derivada f'(x)**

Paso a paso:
- 3x² → 3·2·x¹ = 6x.
- −12x → −12.
- +5 → 0.

**Resultado:** f'(x) = **6x − 12**.

**b) La pendiente en x = 0**

- Sustituimos x = 0 en f'(x) = 6x − 12: 6·0 − 12 = −12.

**Resultado:** pendiente **−12**. Como es negativa, la función **baja** ahí.

**c) Dónde la pendiente es cero y valor mínimo**

Paso a paso:
- Igualamos a cero: 6x − 12 = 0.
- Pasamos el 12: 6x = 12.
- Dividimos entre 6: x = 2.
- Para saber **cuánto vale** la función ahí, sustituimos en **f** (no en f'): 3·2² − 12·2 + 5 = 12 − 24 + 5 = −7.

**Resultado:** el mínimo está en **x = 2** y vale **−7**. Es mínimo porque la parábola **abre hacia arriba** (el 3 de 3x² es positivo).

**d) En Desmos**

- Escribid `f(x)=3x^2-12x+5`.
- La recta tangente en x = 0 pasa por (0, 5) y tiene pendiente −12: `y=-12x+5`.
- Comprobad que **baja 12 de cada 1 que avanza**.

**Qué significa:** derivada negativa = bajando, positiva = subiendo, cero = llano. **Un modelo de IA busca el punto de error mínimo**, y para eso mira la derivada.

**Ojo con:** decir que el mínimo «vale 2». El 2 es **dónde** está (x), el −7 es **cuánto** vale.

### M8 · Regla de la cadena

**La idea en una frase:** cuando una función está **dentro de otra** (como una muñeca rusa), se deriva la de fuera y **se multiplica por la derivada de la de dentro**.

**a) g(x) = (2x + 1)³**

Paso a paso:
- Lo de **dentro** es 2x + 1. Lo de **fuera** es «elevar al cubo».
- Derivamos fuera: 3·(2x + 1)² (el 3 baja y el exponente queda en 2).
- **Multiplicamos por la derivada de dentro**: la de 2x + 1 es 2.
- Juntamos: 3·(2x + 1)²·2 = 6(2x + 1)².
- Evaluamos en x = 0: 6·(1)² = 6.

**Resultado:** g'(x) = **6(2x + 1)²** y g'(0) = **6**.

**b) h(x) = e^(−x²)** (campana de Gauss sin normalizar)

Paso a paso:
- Lo de **fuera** es «e elevado a algo»; su derivada es **la misma e elevada a lo mismo**.
- Lo de **dentro** es −x²; su derivada es −2x.
- Multiplicamos: h'(x) = e^(−x²)·(−2x) = **−2x·e^(−x²)**.
- En x = 1: −2·1·e^(−1) = −2/e. Como e ≈ 2,718: −2 ÷ 2,718 ≈ −0,74.

**Resultado:** h'(1) ≈ **−0,74**.

**c) Con vuestras palabras**

Pensad en una **cadena de engranajes**: si la rueda x da una vuelta y hace girar la rueda u, y u hace girar la rueda y, **el efecto total es el producto de los efectos**.

**Resultado:** dy/dx = (dy/du)·(du/dx): **los efectos se multiplican**.

**Qué significa:** una red neuronal es **una cadena de funciones**, una detrás de otra. Gracias a la regla de la cadena podemos saber **cuánto influye cada capa en el error**.

**Ojo con:** olvidar multiplicar por la derivada de lo de dentro (da 3(2x + 1)² = 3 en lugar de 6).

### M9 · Derivadas parciales y gradiente
Datos: **f(x, y) = x² + 3xy + y²**.

**La idea en una frase:** si la función tiene **dos variables** (como un terreno con norte-sur y este-oeste), derivamos **una cada vez**, haciendo como si la otra fuera un número fijo. Esa lista de pendientes es el **gradiente**.

**a) Derivadas parciales**

Paso a paso:
- **∂f/∂x** (derivamos en x; **y es un número fijo**): x² → 2x; 3xy → 3y (la x desaparece al derivar; la y se queda); y² → 0 (no tiene x).
  Resultado: **2x + 3y**.
- **∂f/∂y** (ahora **x es fijo**): x² → 0; 3xy → 3x; y² → 2y.
  Resultado: **3x + 2y**.

**b) El gradiente en (1, 2)**

Paso a paso:
- Primera componente: 2·1 + 3·2 = 2 + 6 = 8.
- Segunda componente: 3·1 + 2·2 = 3 + 4 = 7.

**Resultado:** ∇f(1, 2) = **(8, 7)**.

**c) Hacia dónde bajar**

- El gradiente apunta hacia donde **sube** más rápido.
- Para bajar, vamos **al lado contrario**: cambiamos el signo.

**Resultado:** −∇f = **(−8, −7)**.

**d) El gradiente en (0, 0)**

- Sustituimos x = 0 e y = 0: 2·0 + 3·0 = 0 y 3·0 + 2·0 = 0.

**Resultado:** **(0, 0)**. Significa que **allí el terreno es llano en todas las direcciones**: es un punto donde se «aplana» la función.

**Qué significa:** el gradiente es **la brújula** que dice por dónde sube el terreno; **por eso la IA «baja la cuesta» en sentido contrario** para reducir el error.

**Ojo con:** pensar que gradiente cero siempre es un mínimo. Puede ser un **punto de silla** (como en este ejemplo): llano en el centro, pero sube por un lado y baja por otro.

### M10 · Descenso del gradiente con una variable
Queremos bajar al fondo de **f(x) = x²** (el mínimo está en x = 0), empezando en **x₀ = 4**.

**La idea en una frase:** el **descenso del gradiente** es **bajar una cuesta a pasitos** mirando en cada paso hacia dónde baja el terreno. La regla es: **nuevo x = x − η · pendiente**, donde **η** (letra «eta») es **el tamaño del paso**.

**Antes de empezar:** la derivada de x² es 2x. Esa es la **pendiente** en cada punto: en x = 4 vale 8, en x = 2 vale 4, etc.

**a) Con η = 0,25**

Paso a paso:
- **x₁:** pendiente en 4 = 2·4 = 8. 4 − 0,25·8 = 4 − 2 = **2**.
- **x₂:** pendiente en 2 = 4. 2 − 0,25·4 = 2 − 1 = **1**.
- **x₃:** pendiente en 1 = 2. 1 − 0,25·2 = 1 − 0,5 = **0,5**.

**Resultado:** 2, 1, 0,5. **Cada paso divide por 2** y nos acercamos a 0.

**b) Con η = 0,5**

- Pendiente en 4 = 8. 4 − 0,5·8 = 4 − 4 = **0**.

**Resultado:** x₁ = **0**: llegamos al mínimo **en un solo paso** (es una casualidad de este caso).

**c) Con η = 1,1** (paso grande)

Paso a paso:
- **x₁:** pendiente en 4 = 8. 4 − 1,1·8 = 4 − 8,8 = **−4,8**.
- **x₂:** pendiente en −4,8 = 2·(−4,8) = −9,6. −4,8 − 1,1·(−9,6) = −4,8 + 10,56 = **5,76**.

**Resultado:** 4 → −4,8 → 5,76. **Salta de un lado a otro y cada vez se aleja más** (cada paso multiplica la distancia al 0 por 1,2). **Diverge.**

**d) Con vuestras palabras**

- **Paso demasiado pequeño:** vamos bien, pero **tardamos muchísimo** en llegar.
- **Paso demasiado grande:** nos pasamos del fondo, **vamos de un lado a otro** y hasta nos podemos **alejar**.

**Resultado:** hay que **elegir bien el paso**. A ese número que elegimos nosotros se le llama **hiperparámetro**.

**e) En Desmos**

- Dibujad `f(x)=x^2`.
- Poned los puntos (4, 16), (2, 4), (1, 1), (0,5; 0,25).
- Veréis que **bajan por la parábola hacia el fondo, con saltos cada vez más cortos** (porque la cuesta es cada vez más suave).

**Qué significa:** **así «aprende» un modelo de IA**: da pasos pequeños en la dirección en que el error baja.

**Ojo con:** usar siempre la pendiente del primer punto. **En cada paso hay que volver a calcular la pendiente en el punto donde estamos.**

### M11 · Función de coste y un paso de descenso
Datos: tres reservas **(1, 2), (2, 4), (3, 6)** (noches, precio en cientos de euros). Modelo: **ŷ = w·x** (el precio que predice el modelo es **w por las noches**).

**La idea en una frase:** el **coste** J mide **cuánto se equivoca el modelo** (más pequeño = mejor). Vamos a mejorar w con **un paso de descenso**.

**a) Con w = 1: errores y coste**

Paso a paso:
- Predicciones ŷ = 1·x: (1, 2, 3).
- Precios reales y: (2, 4, 6).
- **Error = predicción − real**: 1 − 2 = −1; 2 − 4 = −2; 3 − 6 = −3.
- Elevamos cada error al cuadrado (así no se compensan los positivos con los negativos): 1, 4, 9.
- Sumamos: 1 + 4 + 9 = 14.
- Dividimos entre 3 (hay tres reservas): 14/3 ≈ 4,67.

**Resultado:** errores **(−1, −2, −3)** y J = **4,67**.

**b) La derivada dJ/dw en w = 1**

Paso a paso:
- Multiplicamos **cada error por su x**: (−1)·1 = −1; (−2)·2 = −4; (−3)·3 = −9.
- Sumamos: −1 − 4 − 9 = −14.
- Multiplicamos por 2/3: (2/3)·(−14) = −28/3 ≈ **−9,33**.

**Resultado:** la pendiente es **−9,33**. Es **negativa**: si **subimos w**, el coste **baja**.

**c) Un paso con η = 0,05**

Paso a paso:
- Fórmula: w nuevo = w − η·pendiente.
- w nuevo = 1 − 0,05·(−9,33).
- 0,05·(−9,33) = −0,4667, y **restar un negativo es sumar**: 1 + 0,4667 = 1,467.

**Resultado:** w nuevo = **1,467**.

**d) El nuevo error**

Paso a paso:
- Predicciones con w = 1,467: (1,467; 2,933; 4,400).
- Errores: 1,467 − 2 = −0,533; 2,933 − 4 = −1,067; 4,400 − 6 = −1,600.
- Al cuadrado: 0,284; 1,138; 2,560.
- Suma: 3,982. Dividimos entre 3: **≈ 1,33**.

**Resultado:** J ha bajado de **4,67 a 1,33**. El valor de w que da **J = 0** es **w = 2**, porque los datos cumplen **y = 2x** (1→2, 2→4, 3→6).

**e) En Desmos**

- Dibujad `J(w)=(1/3)((w-2)^2+(2w-4)^2+(3w-6)^2)`. Sale una **parábola** con el fondo en w = 2.
- Marcad w = 1 y w = 1,467: **los dos están a la izquierda del fondo y el segundo está más cerca**.

**Qué significa:** **un paso de descenso es un paso de aprendizaje**: el modelo se equivoca menos que antes. Si repetimos muchas veces, w se acerca a 2.

**Ojo con:** el signo. Restar una pendiente **negativa** hace que w **suba**.

### M12 · Explorar f(x) = x³ − 3x

**La idea en una frase:** una función puede tener **varios valles y colinas**. El descenso del gradiente **cae al valle que tiene más cerca**, aunque no sea el más profundo.

**a) Dónde la pendiente es cero**

Paso a paso:
- Derivamos: x³ → 3x²; −3x → −3. **f'(x) = 3x² − 3**.
- Igualamos a cero: 3x² − 3 = 0.
- Pasamos el 3: 3x² = 3.
- Dividimos entre 3: x² = 1.
- ¿Qué números elevados al cuadrado dan 1? **1 y −1**.

**Resultado:** **x = −1** y **x = 1**.

**b) ¿Máximo o mínimo?**

Miramos el **signo de f'** a un lado y a otro:
- Alrededor de x = −1: antes (x = −2) f' = 3·4 − 3 = 9, **positiva (sube)**; después (x = 0) f' = −3, **negativa (baja)**. Sube y luego baja: una **colina**, **máximo local**. f(−1) = −1 + 3 = **2**.
- Alrededor de x = 1: antes (x = 0) f' = −3, **baja**; después (x = 2) f' = 9, **sube**. Baja y luego sube: un **valle**, **mínimo local**. f(1) = 1 − 3 = **−2**.

**c) La tangente en x = 2**

Paso a paso:
- f(2) = 8 − 6 = **2** (el punto de la gráfica).
- f'(2) = 3·4 − 3 = **9** (la pendiente).
- Recta: y − 2 = 9·(x − 2).
- Desarrollamos: y = 9x − 18 + 2 = **9x − 16**.

**d) Reflexión: ¿a dónde llega el descenso?**

Recordad: **el descenso se mueve en sentido contrario a la pendiente**.
- **Desde x = 2:** f'(2) = 9 (positiva, sube hacia la derecha), así que **se mueve hacia la izquierda** y cae en el valle de **x = 1**.
- **Desde x = −0,5:** f'(−0,5) = 3·0,25 − 3 = −2,25 (negativa, baja hacia la derecha), así que **se mueve hacia la derecha** y también cae en **x = 1**.
- **Desde x = −2:** f'(−2) = 9 (positiva), así que **se mueve hacia la izquierda**, **más lejos del valle**, y **la función sigue bajando sin parar**: **no hay mínimo** por ese lado.

**Resultado:** el resultado **depende de dónde empecemos** y, cuando hay mínimo, solo asegura un **mínimo local** (no el mejor posible).

**Qué significa:** en una red neuronal el «paisaje» del error tiene **muchos valles**. Por eso se prueban **varios puntos de partida**.

**Ojo con:** pensar que x = −1 también es un mínimo. Es un máximo local.

---

## Un último consejo

> Si una explicación no os entra, **dibujad**: una flecha, una cuesta, una tabla o una tarta. Y recordad que lo importante de cada ejercicio es **entender qué significa el resultado** para un modelo de IA o para las reservas de TurisData.
