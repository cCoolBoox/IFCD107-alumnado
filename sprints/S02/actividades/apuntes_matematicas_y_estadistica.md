# Apuntes del Sprint 2 · Las matemáticas y la estadística detrás de la IA

Las diapositivas (S02.1 y S02.2) son un esquema. Estos apuntes cuentan lo mismo **explicado con calma, con ejemplos pequeños y las cuentas hechas paso a paso**. Léelos **antes** de los ejercicios o cuando una diapositiva te suene a chino. No hay que memorizar nada: hay que **entender qué significa cada cosa**.

No hace falta ser bueno en matemáticas. Con fracciones, porcentajes, potencias y una calculadora (o el móvil) llegas a todo. Cuando veas un símbolo raro, mira su «traducción a lengua normal».

---

## 0. De qué va el sprint (en 1 minuto)

Un modelo de IA, por dentro, hace tres cosas:

1. **Convierte los datos en números** (una reserva, una foto o un texto se vuelven listas de números).
2. **Mide cuánto se equivoca** y **se corrige poco a poco** hasta equivocarse lo menos posible.
3. Da una predicción… **que nunca es segura**: siempre hay un margen de duda.

Y de ahí salen los dos días del sprint:

| Día | Tema | La idea | Herramientas |
|---|---|---|---|
| **Día 1** | Matemáticas para IA | Cómo "piensa" y "aprende" un modelo | Vectores, matrices, derivadas, gradiente |
| **Día 2** | Estadística y probabilidad | Cómo **no dejarse engañar** por los datos | Media, probabilidad, Bayes, sesgos, correlación, Simpson |

**El reto** junta todo: sois **auditores**. La dirección de TurisData os da un informe con seis frases sobre cancelaciones y os pide: *"¿nos podemos fiar de cada frase? Y si no, ¿cómo debería decirse?"*. No programáis: usáis las ideas del día 2 (y una hoja de cálculo).

---

# DÍA 1 · Matemáticas para IA

## 1. Vectores: una lista de números

Un **vector** es una lista ordenada de números. Por ejemplo, una reserva:

`reserva = (noches, huéspedes, temporada alta)` → `(3, 2, 1)`

(temporada alta: 1 = sí, 0 = no). Con ella puedes hacer tres cosas:

- **Sumar** vectores: se suma posición a posición. `(3, 2, 1) + (1, 0, 0) = (4, 2, 1)`.
- **Multiplicar por un número**: se multiplica cada posición. `2·(3, 2, 1) = (6, 4, 2)`.
- **Longitud (norma)**: es la hipotenusa, con Pitágoras. `|(3, 4)| = √(3² + 4²) = √25 = 5`.

### El producto escalar (lo más importante del día)

Es **multiplicar posición a posición y sumar**. Da **un solo número**.

Imagina un modelo de precio muy simple. Cada característica tiene un **peso** (cuánto "pesa" en el precio):

`precio = 50·noches + 20·huéspedes + 30·temporada_alta`

Los pesos son el vector `w = (50, 20, 30)`. Para la reserva `x = (3, 2, 1)`:

```
w · x = 50·3 + 20·2 + 30·1 = 150 + 40 + 30 = 220 €
```

**En lengua normal:** el producto escalar es una **suma ponderada**: "cuenta cada cosa tantas veces como importa". Si el peso de "huéspedes" es 20, cada huésped extra suma 20 €.

> **Conexión con la IA:** una neurona artificial hace exactamente esto: `z = w · x + b` (productos, suma y un número base `b`). Una red neuronal enorme son muchísimas de estas cuentas juntas. **Entrenar = encontrar buenos pesos `w`.**

## 2. Matrices: una tabla de números

Una **matriz** es una tabla. En IA, **cada fila es una muestra** (una reserva) y **cada columna una variable** (noches, huéspedes…). Si hay 3 reservas y 3 variables, es una matriz de **3 × 3** (filas × columnas):

```
        noches  huésp.  temp.
A = [     3       2       1   ]   ← reserva 1
    [     1       1       0   ]   ← reserva 2
    [     5       4       1   ]   ← reserva 3
```

### Matriz por vector: calcular muchas cosas a la vez

Multiplicar `A · w` es hacer el producto escalar **de cada fila con w**. Así sacas el precio de las tres reservas de una vez (con `w = (50, 20, 30)`):

```
reserva 1:  3·50 + 2·20 + 1·30 = 150 + 40 + 30 = 220
reserva 2:  1·50 + 1·20 + 0·30 =  50 + 20 +  0 =  70
reserva 3:  5·50 + 4·20 + 1·30 = 250 + 80 + 30 = 360
```

Resultado: el vector `(220, 70, 360)`. **Una capa de una red neuronal es esto:** `y = A·x + b`.

### Producto de matrices: la regla de las dimensiones

Para multiplicar `A · B`, **las columnas de A tienen que ser tantas como las filas de B**. El resultado tiene las filas de A y las columnas de B:

`(m × n) · (n × p) = (m × p)`

Cada casilla del resultado es el producto escalar de **una fila de A por una columna de B**.

**Cuidado: el orden importa.** Con `A = [[1, 2], [0, 1]]` y `B = [[1, 0], [3, 1]]`:

```
A·B = [[1·1 + 2·3,  1·0 + 2·1],     = [[7, 2],
       [0·1 + 1·3,  0·0 + 1·1]]        [3, 1]]

B·A = [[1·1 + 0·0,  1·2 + 0·1],     = [[1, 2],
       [3·1 + 1·0,  3·2 + 1·1]]        [3, 7]]
```

`A·B` y `B·A` **no son iguales**. (En números normales 2·3 = 3·2; en matrices, no.)

### Tres palabras más (solo la idea)

- **Transpuesta (Aᵀ):** girar la tabla, las filas pasan a ser columnas. Una matriz 2×3 se vuelve 3×2.
- **Inversa (A⁻¹):** la matriz que "deshace" a A, como dividir deshace multiplicar. `A · A⁻¹` da la matriz que no cambia nada (la **identidad**). No todas tienen inversa (si el **determinante** vale 0, no hay).
- **Autovector:** una flecha que, al aplicarle la matriz, **sigue apuntando en la misma dirección** (solo se estira o encoge). Con `A = [[2, 0], [0, 1]]`, el vector `(1, 0)` pasa a `(2, 0)`: misma dirección, el doble de largo. Sirve para resumir datos (PCA, Sprint 9).

## 3. La derivada: "cuánto cambia si lo muevo un poquito"

Piensa en un **coche**. La posición cambia con el tiempo; **la derivada de la posición es la velocidad** (cuánto cambia la posición por cada segundo). La derivada es **el velocímetro de una función**.

En un dibujo, la derivada en un punto es la **pendiente** de la recta que toca la curva en ese punto (la **tangente**):

| Derivada | Qué hace la función ahí |
|---|---|
| **Positiva** | **Sube** |
| **Negativa** | **Baja** |
| **Cero** | Está plana: **posible fondo (mínimo) o cima (máximo)** |

### Comprobación con un ejemplo

`f(x) = x²`. Su derivada es `f'(x) = 2x`. En `x = 3` vale 6. ¿Es verdad? Muévete un poquito: `f(3) = 9` y `f(3,01) = 9,0601`. Subió 0,0601 al avanzar 0,01 → `0,0601 / 0,01 = 6,01 ≈ 6`. ✔

### Las reglas que necesitas (no hay más)

| Función | Derivada | Ejemplo |
|---|---|---|
| un número solo (constante) | 0 | `(7)' = 0` |
| `x` | 1 | `(5x)' = 5` |
| `xⁿ` | `n·xⁿ⁻¹` ("baja el exponente y réstale 1") | `(x³)' = 3x²` |
| suma | se deriva cada trozo | `(x² − 6x + 10)' = 2x − 6` |
| `eˣ` | `eˣ` | |
| `ln(x)` | `1/x` | |

### Cómo se usa para encontrar el mínimo

`f(x) = x² − 6x + 10` → `f'(x) = 2x − 6`. Pendiente cero cuando `2x − 6 = 0` → `x = 3`. Y `f(3) = 9 − 18 + 10 = 1`. **El punto más bajo está en x = 3 y vale 1.** (Antes de 3 la derivada es negativa → baja; después, positiva → sube. Es un fondo.)

### La regla de la cadena: funciones dentro de funciones

Imagina **engranajes**: si el engranaje 1 da 3 vueltas por cada vuelta tuya y el 2 da 2 vueltas por cada una del 1, el 2 da 3·2 = 6. Las velocidades **se multiplican**.

`y = u²` con `u = 3x` (o sea `y = (3x)²`). Derivada = (derivada de fuera) · (derivada de dentro):

```
dy/dx = 2u · 3 = 2·(3x)·3 = 18x        (compruébalo: y = 9x²  →  y' = 18x ✔)
```

> **Conexión con la IA:** una red neuronal son funciones dentro de funciones (capa tras capa). La regla de la cadena permite saber **cuánto ha contribuido cada peso al error**, de atrás hacia delante: es la **retropropagación**.

## 4. Derivadas parciales y gradiente: lo mismo, con varias "perillas"

Un modelo tiene **muchos** pesos, no uno. Una función con dos variables, por ejemplo `f(x, y) = x² + y²`, es una **superficie** (como un cuenco).

- **Derivada parcial:** derivas respecto a **una** variable y **tratas las demás como si fueran números**. "Muevo solo esta perilla y miro qué pasa."
  - `∂f/∂x = 2x` (la `y²` no depende de x, se va) · `∂f/∂y = 2y`.
- **Gradiente (∇f):** **todas las derivadas parciales juntas** en un vector: `∇f = (2x, 2y)`.

**Cómo leer el gradiente:** apunta hacia donde la función **sube más deprisa**. En el punto `(3, 1)`: `∇f = (6, 2)`. Si quieres **bajar** lo más rápido, vas en el **sentido contrario**: `(−6, −2)`.

**Imagen para recordarlo:** estás en una montaña, con niebla, y solo notas la pendiente bajo tus pies. El gradiente te dice por dónde **se sube** más; si quieres bajar al valle, das un paso **justo al revés**.

## 5. El descenso del gradiente: así aprende un modelo

Es la idea central del día. **Aprender = bajar un error hasta el fondo.**

La **regla** (se repite una y otra vez):

```
nuevo valor = valor actual − α · pendiente
```

- `α` (alfa, o "η" en las hojas) es el **paso** o **tasa de aprendizaje**: lo grande que es cada paso.
- La **pendiente** es la derivada (o el gradiente si hay varias variables).
- Se **resta** porque queremos **bajar**, no subir.

### Ejemplo completo, a mano

Queremos minimizar `f(x) = (x − 3)²` (el mínimo está en x = 3, pero "no lo sabemos"). Su derivada es `f'(x) = 2(x − 3)`. Empezamos en `x = 0` con **α = 0,1**:

| Paso | x | pendiente `2(x − 3)` | nuevo x = x − 0,1·pendiente |
|---|---|---|---|
| 0 | 0 | −6 | 0 − 0,1·(−6) = **0,6** |
| 1 | 0,6 | −4,8 | 0,6 + 0,48 = **1,08** |
| 2 | 1,08 | −3,84 | 1,08 + 0,384 = **1,464** |
| 3 | 1,464 | −3,07 | 1,464 + 0,307 = **1,771** |
| … | … | … | cada vez más cerca de 3 |

Fíjate: la pendiente es negativa (la función baja hacia la derecha), así que "menos pendiente" **suma** y nos movemos a la derecha, hacia el fondo. Y los pasos **se hacen más pequeños** al acercarnos (la pendiente se aplana).

### ¿Y si el paso α no es el adecuado?

Con el mismo ejemplo (empezamos en x = 0):

| α | Qué pasa | Cuentas |
|---|---|---|
| **Muy pequeño** (0,001) | Llega, pero **lentísimo** | x₁ = 0,006… |
| **Adecuado** (0,1) | Se acerca poco a poco | ver tabla anterior |
| **α = 1** | **Rebota** sin acercarse | 0 → 6 → 0 → 6 … |
| **α = 1,1** | **Se aleja** (diverge) | 0 → 6,6 → −1,32 → … cada vez más lejos |

Por eso α es el **ajuste más importante** del entrenamiento: ni muy tímido, ni muy bestia.

### Cómo encaja todo (la tabla de la diapositiva final)

| Qué hace el modelo | Qué matemáticas usa |
|---|---|
| **Entrada → predicción** | vectores y matrices: `y = A·x + b` |
| **Predicción → error** | una **función de coste** (cuánto se aleja de lo real) |
| **Error → cómo corregir** | el **gradiente** (regla de la cadena = retropropagación) |
| **Corregir** | el **descenso del gradiente** con paso α |

Y se repite miles de veces. **Todo lo que viene en el curso, hasta los transformers, es esto mismo a mayor escala.** En el Sprint 5 lo programarás tú.

**Ejercicios que practican este día** (hoja 1, `ejercicios_algebra_calculo.md`): M1–M2 (sección 1), M3–M6 (sección 2), M7–M8 (sección 3), M9 (sección 4), M10–M12 (sección 5). Mínimo: **M1, M2 y M7**.

---

# DÍA 2 · Estadística y probabilidad: no dejarse engañar

> **Truco que lo cambia todo:** en probabilidad, **pasa los porcentajes a "personas de cada 1.000"** (frecuencias naturales). "El 3 %" es difícil de imaginar; "30 de cada 1.000" se ve y se cuenta.

## 6. Describir datos: centro y dispersión

Datos de 5 sueldos (€/mes): `1.200 · 1.250 · 1.300 · 1.350 · 6.000`

| Medida | Qué es | Resultado aquí |
|---|---|---|
| **Media** | suma ÷ cuántos | `(1.200 + 1.250 + 1.300 + 1.350 + 6.000) ÷ 5 = 2.220` |
| **Mediana** | el valor **de en medio** (ordenados) | **1.300** |
| **Moda** | el valor que **más se repite** | (aquí ninguno; sirve sobre todo para categorías) |

Mira: la media (2.220) **no representa a nadie** porque el 6.000 la arrastra hacia arriba. La mediana (1.300) sí describe un sueldo "típico". **Regla:** cuando hay valores extremos o los datos son "asimétricos" (sueldos, precios), manda la **mediana**.

### Dispersión: ¿cuánto se separan los datos?

- **Desviación típica (σ):** "cuánto se alejan, de media, los datos de la media". Con `2, 4, 4, 4, 5, 5, 7, 9`:
  1. Media = 5.
  2. Diferencias con la media: `−3, −1, −1, −1, 0, 0, 2, 4`.
  3. Elévalas al cuadrado: `9, 1, 1, 1, 0, 0, 4, 16` → suma 32.
  4. Divide entre 8 (**varianza** = 4) y haz la raíz: **σ = 2**.
  
  Sale en las **mismas unidades** que el dato (si son euros, σ son euros).
- **Cuartiles:** ordena los datos y pártelos en 4 trozos iguales. **Q1** deja el 25 % por debajo, la mediana es Q2 y **Q3** deja el 75 %. El **IQR = Q3 − Q1** es el rango donde está el **50 % central**. Es la "caja" del diagrama de caja.

## 7. Probabilidad: contar posibilidades

`P(A) = casos favorables ÷ casos posibles`, y va siempre de **0** (imposible) a **1** (seguro) (o de 0 % a 100 %).

- **Complementario:** `P(no A) = 1 − P(A)`. Si la probabilidad de cancelar es 0,2, la de **no** cancelar es 0,8.
- **Sucesos independientes** (uno no influye en el otro): se **multiplican**. Probabilidad de que dos reservas distintas se cancelen, con 0,2 cada una: `0,2 · 0,2 = 0,04`.
- **Una u otra** (que ocurra A **o** B): se suman y se resta lo que se ha contado dos veces: `P(A o B) = P(A) + P(B) − P(A y B)`.

### Probabilidad condicionada: "sabiendo que…"

`P(A | B)` se lee **"probabilidad de A sabiendo que ha ocurrido B"**. Con frecuencias naturales (1.000 huéspedes):

- 400 viajan con niños; **100 de ellos** contratan guardería.
- `P(guardería | viajan con niños) = 100 ÷ 400 = 0,25` (**25 %**).
- `P(guardería)` en total = `100 ÷ 1.000 = 10 %`.

**Ojo, no es simétrico:** `P(guardería | niños) = 25 %`, pero `P(niños | guardería) = 100 %` (todos los que contratan guardería traen niños). **Confundir las dos es un error clásico.**

### La binomial: contar "éxitos" repetidos

Si haces **n** intentos y cada uno sale "bien" con probabilidad **p**, la **binomial** te da la probabilidad de **k** éxitos. Ejemplo: 5 reservas, cada una se cancela con p = 0,2. ¿Probabilidad de que se cancele **exactamente 1**?

```
5 formas de elegir cuál se cancela · 0,2 (esa se cancela) · 0,8⁴ (las otras 4 no)
= 5 · 0,2 · 0,4096 = 0,4096  → un 41 %
```

(Y que no se cancele ninguna: `0,8⁵ = 0,328` → un 33 %). No hace falta memorizar la fórmula: **piensa en cuántas formas hay y multiplica.**

### La normal: la campana

Muchas medidas (alturas, tiempos, errores) se reparten en forma de **campana** alrededor de la media. La regla **68-95-99,7**: a 1, 2 y 3 desviaciones típicas de la media caen el 68 %, 95 % y 99,7 % de los datos. Si las noches medias de estancia son 4 con σ = 1, lo normal es entre 3 y 5 noches (68 %), y casi todo entre 2 y 6 (95 %). Una estancia de 9 noches ya es **muy rara**.

## 8. El teorema de Bayes: por qué un test "fiable" puede fallar tanto

La pregunta: **"si ha dado positivo, ¿cuánta probabilidad hay de que sea de verdad?"** Casi nadie acierta a ojo. Se resuelve **contando personas**.

**Ejemplo:** alarma de humo de un hotel. Un día de cada 100 hay un incendio real. La alarma detecta el **90 %** de los incendios reales, pero **suena en falso el 10 %** de los días sin incendio. Se ha activado. ¿Probabilidad de incendio real?

Imagina **10.000 días**:

```
Incendios reales: 1 de cada 100          → 100 días
   de ellos, la alarma suena (90 %)      →  90 días  ✔ (alarma buena)
Días sin incendio: 9.900
   de ellos, suena en falso (10 %)       → 990 días  ✘ (falsas alarmas)

Total de días en que suena la alarma = 90 + 990 = 1.080
De esos, incendios reales = 90
Probabilidad = 90 ÷ 1.080 = 0,083  → solo un 8,3 %
```

**Aunque la alarma "acierta el 90 %", casi 9 de cada 10 veces que suena es falsa**, porque lo que se busca (el incendio) es **raro** y las falsas alarmas se acumulan sobre los muchos días normales. Es exactamente lo que le pasa a un detector de reservas fraudulentas si el fraude es poco frecuente.

La fórmula de Bayes, `P(A|B) = P(B|A) · P(A) ÷ P(B)`, es **esta misma cuenta**: *(los verdaderos positivos) ÷ (todos los positivos)*. Si en un examen te falla la fórmula, vuelve a contar personas.

## 9. Muestreo y sesgos

Casi nunca miramos a **todos** (la población); miramos una **muestra**. Si la muestra está mal elegida, las conclusiones fallan aunque las cuentas estén perfectas.

| Tipo de muestreo | Idea |
|---|---|
| **Aleatorio simple** | todos con la misma probabilidad (el menos sesgado) |
| **Estratificado** | se coge cada grupo en su proporción (ej.: 30 % de reservas web → 30 % de la muestra) |
| **Por conglomerados** | se eligen grupos enteros (ej.: tres hoteles completos); más barato, más variación |

**Los sesgos más típicos** (siempre con la pregunta *"¿quién falta?"*):

- **De selección:** la muestra no representa a la población. *Encuesta de satisfacción enviada solo a quien dejó su correo → ¿y el que no lo dejó?*
- **De respuesta:** quien contesta es distinto de quien no contesta (o no es sincero). Responden sobre todo los muy contentos y los muy enfadados.
- **De supervivencia:** solo vemos lo que "sobrevivió". *"Los negocios antiguos tienen buenas valoraciones"* → los malos cerraron y no los vemos.

**Tamaño de muestra:** con pocos datos, todo es inestable. "El 100 % lo recomienda" suena genial… si preguntaste a **2 personas**, no vale nada. Siempre pregunta: **¿sobre cuántos?**

## 10. Correlación no es causalidad

El **coeficiente de correlación r** va de **−1 a +1**: cerca de +1, las dos cosas **suben juntas**; cerca de −1, una **sube y la otra baja**; cerca de 0, **no hay relación en línea recta**.

Pero que **vayan juntas no significa que una cause la otra**. Puede haber:

- **Una causa común escondida:** *"cuando se venden más helados, hay más quemaduras de sol"*. Los helados no queman: ambos suben en **verano**.
- **Casualidad** (con pocos datos) o **al revés** (el efecto era la causa).

Para decir que algo **causa** otra cosa hace falta un **experimento** (por ejemplo, una prueba A/B con grupos comparables), no solo una correlación.

## 11. La paradoja de Simpson: mira los grupos antes de concluir

A veces una tendencia **se da la vuelta** al juntar los grupos. Ejemplo (datos inventados): dos guías, A y B, y qué porcentaje de grupos acaban satisfechos, según la dificultad del tour:

| | Tour sencillo | Tour difícil | **TOTAL** |
|---|---|---|---|
| **Guía A** | 81 de 87 → **93 %** | 192 de 263 → **73 %** | 273 de 350 → **78 %** |
| **Guía B** | 234 de 270 → **87 %** | 55 de 80 → **69 %** | 289 de 350 → **83 %** |

- **Dentro de cada tipo de tour, A gana a B** (93 > 87 y 73 > 69).
- **En el total, B parece mejor** (83 % > 78 %).

¿Por qué? A hace muchos más tours **difíciles** (263 frente a 80), que siempre puntúan peor. La comparación **total** mezcla peras con manzanas.

**Regla para siempre:** **desagrega** (separa por grupos) **antes de concluir**, sobre todo cuando los grupos no son del mismo tamaño o dificultad.

## 12. Inferencia, en dos ideas

- **Intervalo de confianza al 95 %:** en vez de decir "la tasa es 35 %", dices "está **entre 32 % y 38 %**". Cuanta **más muestra**, más **estrecho** (más preciso) el intervalo.
- **Contraste de hipótesis y p-valor:** partes de que "no pasa nada" (H₀) y calculas **lo raro que sería ver estos datos si de verdad no pasara nada**. Si esa probabilidad (el **p-valor**) es muy pequeña (menos de 0,05), sospechas que **sí pasa algo**.
  - **El p-valor NO es** la probabilidad de que H₀ sea cierta. Es: *"si no pasara nada, ¿qué probabilidad hay de ver algo tan extremo?"*.

## 13. Lista de trampas para auditar una frase (la usarás en el reto)

| Trampa | Ejemplo | La pregunta que la destapa |
|---|---|---|
| **Sin comparación o sin fuente** | "Estamos en la media del sector" | ¿Con qué se compara? ¿Hay un dato? |
| **Muestra pequeña** | "El 100 % lo recomienda" (n = 2) | ¿Cuántos datos hay? |
| **Muestra sesgada** | Encuesta solo a quien dejó su correo | ¿Quién ha respondido y quién falta? |
| **Correlación = causa** | "Helados ↔ quemaduras" | ¿Hay una tercera cosa que explique las dos? |
| **Simpson / no separar grupos** | El total contradice a los grupos | Si separo por grupos, ¿cambia? |
| **Base de comparación distinta** | "+50 % y −10 % se compensan" (no: depende de cuánto había) · "julio→agosto" no es "agosto→julio" | ¿Se comparan cosas iguales (mismos días, misma situación)? |
| **Eje truncado** | Gráfico que empieza en 90 en vez de 0 | ¿Dónde empieza el eje? |
| **Significativo ≠ importante** | Un efecto minúsculo puede tener p < 0,05 | ¿Es lo bastante grande como para importar? |

### El método en 3 preguntas (para cada frase del informe)

1. **¿Qué afirma, exactamente?** (copia la frase)
2. **¿Qué falla o qué falta?** (elige la trampa de la tabla)
3. **¿Cómo debería decirse?** (la frase honesta, con números y sin pasarse)

*Ejemplo:* **"Con el nuevo menú, el 100 % de los clientes que lo probaron lo recomienda."**
1. Afirma que el menú gusta a todo el mundo.
2. Falla: **muestra pequeña** (¿sobre cuántos?). Supongamos que fueron 2.
3. Mejor: *"Dos de dos clientes lo recomiendan, pero es una muestra demasiado pequeña para sacar conclusiones."*

Veredictos posibles en el reto: **fiable · parcialmente fiable · no fiable · no se puede saber** (cuando faltan datos; **es una respuesta válida**: no inventes números).

---

## 14. Chuleta de vocabulario

| Palabra | En lengua normal |
|---|---|
| **Vector** | lista de números |
| **Matriz** | tabla de números (filas × columnas) |
| **Producto escalar** | multiplicar posición a posición y sumar: una "suma ponderada" |
| **Peso** | cuánto importa cada variable en el modelo |
| **Derivada** | pendiente: cuánto cambia algo si lo muevo un poco |
| **Gradiente** | todas las derivadas parciales juntas; apunta hacia donde la función más sube |
| **Función de coste** | número que mide cuánto se equivoca el modelo |
| **Descenso del gradiente** | ir bajando el coste dando pasos contrarios al gradiente |
| **Tasa de aprendizaje (α, η)** | lo grande que es cada paso |
| **Media / mediana** | el promedio / el valor de en medio |
| **Desviación típica (σ)** | cuánto se alejan los datos de la media |
| **Probabilidad condicionada** | probabilidad de A sabiendo que ocurrió B |
| **Bayes** | recalcular una probabilidad al conocer una evidencia (contando personas) |
| **Sesgo** | la muestra o la medida favorece sistemáticamente una respuesta |
| **Correlación** | dos cosas que suben o bajan juntas (no implica causa) |
| **Paradoja de Simpson** | la tendencia se invierte al juntar los grupos |
| **p-valor** | lo raro que sería ver estos datos si no pasara nada |

## 15. Cómo estudiar con esto

1. **Primero la idea, luego la cuenta.** Antes de calcular, dilo en voz alta: *"¿Qué me están preguntando?"*.
2. **Dibuja.** Una pendiente, un cuenco, una tabla de 1.000 personas… Casi todo se entiende mejor con un dibujo.
3. **Comprueba con la calculadora o con Desmos/GeoGebra.** Si dibujas la función y la tangente, ves la derivada.
4. **Si te atascas, apunta dónde.** En los ejercicios vale tanto una respuesta como una nota *"me bloqueo en este paso"*.
5. **Los ejercicios** tienen la graduación ★ (básico), ★★ (medio), ★★★ (reto). Empieza por las ★ y no te agobies con las ★★★.

**Relación con el material del sprint:**

| Si no entiendes… | Mira primero… | Y practica en… |
|---|---|---|
| vectores, matrices, producto escalar | secciones 1–2 | hoja 1: M1–M6 |
| derivadas, gradiente, descenso | secciones 3–5 | hoja 1: M7–M12 |
| media, mediana, σ | sección 6 | hoja 2: E1–E2 |
| probabilidad, Bayes | secciones 7–8 | hoja 2: E3–E7 |
| muestreo, sesgos, correlación | secciones 9–10 | hoja 2: E8–E12 |
| paradojas, trampas, el reto | secciones 11–13 | `estadisticas_enganosas.md` y la ficha del reto |
