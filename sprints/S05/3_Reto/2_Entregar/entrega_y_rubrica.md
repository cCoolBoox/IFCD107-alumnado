# Sprint 5 · Reto «¿La ocupación depende de esto?» · Entrega y rúbrica

> **Qué se sube y cómo se evalúa.** Se lee **una vez**, antes de entregar, y se vuelve a la rúbrica cuando el equipo revisa su trabajo. Mientras trabajáis no hace falta: para eso está [el reto en una página](../1_Trabajar/Reto_Sprint_05_una_pagina.md).
>
> - Volver al [README del sprint](../../README.md) · [ficha del reto](../3_Consultar/Reto_Sprint_05.md), para consultar.
> - Vuestra hoja personal: [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md).
> - Cómo subir a GitHub paso a paso, con capturas: [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md).

Esta hoja responde a **dos preguntas distintas**, una tabla para cada una:

**Tabla A · Los ficheros:** qué ficheros hay, de dónde sale cada uno (ya hecho, lo modificáis, lo creáis o lo genera el programa) y **cuáles se suben y adónde**.

**Tabla B · Los requisitos:** qué tiene que cumplir lo que entregáis y hasta dónde llegar (🟢 mínimo, 🟡 estándar, 🔴 extra). **Es lo que se evalúa.**

**En total, al final del sprint se suben a `sprint-05/`:** **2 ficheros del equipo** (`S05_07_reto_ocupacion.ipynb`, `turisdata_reto.db`) **+ 1 autoevaluación y coevaluación por persona**, es decir, **2 + tantos ficheros como personas haya en el equipo** (un equipo de 3 sube 5). «El reto» no es un fichero aparte: es **el cuaderno completo** (con los gráficos, las cifras y la respuesta al cliente escrita dentro) **más la base de datos** que ese cuaderno crea. Además, el CSV va a `data/` si aún no está. La *review* y la *retro* se hacen de palabra: no se suben.

## 1 · 📦 Tabla A · Los ficheros: de dónde sale cada uno y cuáles se suben

Todo lo que se sube va al repositorio privado del equipo (`ifcd107-equipo-…`), en la carpeta **`sprint-05/`**, salvo el CSV.

| Fichero | Origen | Qué hacéis vosotros | ¿Se sube? |
|---|---|---|---|
| `S05_07_reto_ocupacion.ipynb` | **Lo modificáis.** Os damos la plantilla con las celdas por rellenar y los puntos de control | Rellenáis las celdas, escribís vuestras observaciones y la respuesta al cliente, y añadís al final las celdas «Uso de IA» y «Revisión con la rúbrica». Antes de bajarlo: *Entorno de ejecución → Reiniciar y ejecutar todo* | **Sí** · `sprint-05/` |
| `turisdata_reto.db` | **Lo genera el cuaderno** al ejecutar el paso 1 (la tabla `ocupacion_diaria` con 1096 filas y un índice) | Ejecutar la celda; no se escribe a mano. En Colab aparece en el panel de archivos de la izquierda: descargadlo con el botón derecho | **Sí** · `sprint-05/` |
| `ocupacion_diaria.csv` | **Ya hecho.** Los datos del curso (sintéticos) | Nada: el cuaderno lo descarga y no se cambia | **Sí**, sin cambios · `data/` (si aún no está) |
| Respuesta al cliente (150 palabras como máximo) | **Lo creáis** dentro del cuaderno, en su sección 6 | Escribirla en la celda de texto del cuaderno | **No**, va dentro del cuaderno |
| Autoevaluación y coevaluación (`autoevaluacion_nombre.md`) | **Ya hecha, en blanco** | Cada persona copia la plantilla con su nombre y la rellena; la coevaluación va **dentro del mismo fichero** | **Sí**, **una por persona** (no una por equipo) · `sprint-05/` |
| Copias de prueba del cuaderno o gráficos sueltos (`.png`) | **Las creáis** si queréis probar cosas | Usarlas y borrarlas: los gráficos ya están dentro del cuaderno | **No se suben** |

---

## 2 · ✅ Tabla B · Los requisitos: qué tiene que cumplir y hasta dónde llegar

| Requisito | Qué se pide exactamente | Nivel | Dónde se comprueba |
|---|---|---|---|
| **Base de datos** | `turisdata_reto.db` con la tabla `ocupacion_diaria` (1096 filas) y el índice `idx_ocupacion_fecha`; los datos se leen **con SQL** a un DataFrame `diaria` que incluye la columna `mes` (1 a 12) | 🟢 Mínimo | Cuaderno, sección 1 · punto de control 1 |
| **Primer vistazo a los datos** | `describe()`, la media por mes y **al menos dos gráficos** con título y ejes en español; 2–3 observaciones escritas con vuestras palabras | 🟢 Mínimo | Cuaderno, sección 2 |
| **Regresión simple desde cero** | Escribís `gradiente_mse` y `entrenar` (sin `scikit-learn`) y ajustáis `ocupacion ~ temperatura`; guardáis `pendiente_simple` en puntos por °C | 🟢 Mínimo | Cuaderno, sección 3 · punto de control 2 |
| **Curva de aprendizaje** | Gráfico del error (MSE) por época, con título y ejes en español, y una línea que diga si ha convergido | 🟢 Mínimo | Cuaderno, sección 3 |
| **Respuesta al cliente (versión mínima)** | Hasta 150 palabras, sin jerga, con **una cifra** (el efecto de la temperatura) **y su intervalo de confianza** | 🟢 Mínimo | Cuaderno, sección 6 |
| **Uso de IA** | Una celda de texto «Uso de IA» al final del cuaderno. En el mínimo, una línea que diga si la habéis usado y para qué | 🟢 Mínimo | Cuaderno (última celda) |
| **Subida a GitHub** | Los ficheros están en `sprint-05/` y los suben **personas distintas**, cada una con su cuenta | 🟢 Mínimo | Carpeta `sprint-05/` y su historial |
| **Modelo con control** | `ocupacion ~ temperatura + festivo + indicadores de mes` (11 columnas), todo estandarizado, unas 2000 épocas con tasa 0,1; guardáis `efecto_temp_control` y `efecto_festivo_control` en unidades originales | 🟡 Estándar | Cuaderno, sección 3 · punto de control 2 |
| **Comparación con `statsmodels`** | Los mismos dos modelos con `smf.ols` (`ols_simple`, `ols_control`) y una tabla `comparacion` de 3 filas × 2 columnas (`desde_cero`, `statsmodels`) que coincide (diferencia menor de 0,02) | 🟡 Estándar | Cuaderno, sección 4 · punto de control 3 |
| **Medir la seguridad** | `p_temp_control`, `ic_festivo` (intervalo del 95 %), `p_festivo_ttest` (t de Welch) y `r2_control`, **explicados con palabras** junto con el tamaño del efecto | 🟡 Estándar | Cuaderno, sección 5 · punto de control 4 |
| **Respuesta al cliente (completa)** | Hasta 150 palabras: responde a **las dos preguntas** (temperatura y festivos) con cifras e incertidumbre, da una **recomendación** concreta (personal o precios), dice **qué no se puede afirmar** y añade una frase de IA responsable | 🟡 Estándar | Cuaderno, sección 6 |
| **Cuaderno reproducible** | *Reiniciar y ejecutar todo* funciona sin errores, con la semilla `SEMILLA = 42` y los cuatro puntos de control en verde | 🟡 Estándar | Cuaderno, sección 7 |
| **Uso de IA (completo)** | La celda «Uso de IA» dice **qué pedisteis, qué comprobasteis a mano y qué cambiasteis** | 🟡 Estándar | Cuaderno (última celda) |
| **Revisión y autoevaluación** | Alguien que **no escribió esa parte** revisa el cuaderno con la rúbrica (justo debajo de estas tablas) y anota nivel y prueba en una celda de texto «Revisión con la rúbrica» al final del cuaderno; cada persona sube su hoja de autoevaluación y coevaluación | 🟡 Estándar | Cuaderno (última celda) y `sprint-05/` |
| **Extras** | Explicar con el control por mes **por qué correlación no es causalidad** · comparar varias tasas de aprendizaje con sus curvas · gráficos cuidados (leyenda, unidades °C y %, un comentario bajo cada gráfico) | 🔴 Extra | Cuaderno, secciones 2, 3 y 6 |

En el nivel mínimo, el punto de control 2 comprueba también el modelo con control: **fallará en esas líneas hasta que lo hagáis**, y es normal. Las cifras del modelo simple sí se pueden comprobar sueltas.

---

## 3 · 🧭 Rúbrica del reto · cómo se puntúa y cómo se revisa

La usan **dos veces**: el equipo, para revisar su propio trabajo antes de entregar (es lo que dice la *Definition of Done*), y el docente, para puntuar. Se mira **cada criterio por separado** y se pone el nivel de la columna cuyo texto **se cumple entero**: si lo de un nivel se cumple a medias, es el nivel de abajo. **0** significa que no se ha entregado nada de ese criterio.

Orientación: lo que pide el nivel 🟢 mínimo sale en un **2**, el 🟡 estándar en un **3** y los 🔴 extras en un **4**.

| Criterio | 1 · Empezado | 2 · Mínimo | 3 · Estándar | 4 · Extra |
|---|---|---|---|---|
| **Corrección técnica** (¿funciona?) | Hay celdas rellenas, pero el cuaderno da error antes de llegar a la regresión o fallan varios puntos de control | Pasa el punto de control 1 (1096 filas leídas con SQL); `pendiente_simple` sale ≈ −1,86 y la curva de aprendizaje baja y se estabiliza | Pasan los **cuatro puntos de control**: el modelo con control sale como `statsmodels`, y el p-valor, el intervalo y el R² están bien calculados | Además, comparan varias tasas de aprendizaje y dicen cuál converge y cuál se dispara |
| **Reproducibilidad** (¿lo puede repetir otra persona?) | Solo funciona ejecutando las celdas en un orden raro o con ficheros que están en un solo ordenador | El cuaderno se ejecuta de arriba abajo hasta el modelo simple y `turisdata_reto.db` está subida a `sprint-05/` | *Reiniciar y ejecutar todo* funciona sin errores, con semilla fija; otra persona obtiene **las mismas cifras** y el CSV está en `data/` | Además, anotan las versiones de las librerías (por ejemplo con `!pip freeze`) y lo prueban en una sesión nueva de Colab |
| **Análisis y comunicación al cliente** (¿lo entiende quien no programa?) | La respuesta no tiene cifras o pasa de 150 palabras | Cabe en 150 palabras y da **una cifra con su intervalo de confianza**, sin jerga | Responde a las dos preguntas con cifra e incertidumbre, da una **recomendación concreta**, dice **qué no se puede afirmar**, y el p-valor y el tamaño del efecto se explican con palabras | Además, explica con el control por mes por qué la pendiente simple (≈ −1,86) casi desaparece (≈ −0,09), y los gráficos están cuidados |
| **IA responsable** (¿se sabe qué hizo la IA y qué comprobasteis?) | No dice si se ha usado IA ni habla de límites | Dice si se ha usado IA y menciona que los datos son sintéticos | Dice **qué se pidió, qué se comprobó y qué se cambió**; el equipo escribió el gradiente y sabe explicarlo; la respuesta habla de «se asocia con», no de «causa», y avisa de una cautela (por ejemplo, no fijar precios sin revisión humana) | Además, cuenta un fallo o una cifra de la IA que detectaron al compararla con su cuaderno, y explica por qué el modelo (R² ≈ 0,58, un solo alojamiento) no se debe generalizar |

**Cómo se revisa** (unos 10 minutos, antes de subir; lo hace **una persona que no escribió esa parte**):

1. **Ejecutar**: abrir el cuaderno en Colab y pulsar *Entorno de ejecución → Reiniciar y ejecutar todo*. Anotar qué celda falla y qué puntos de control dicen «superado».
2. **Leer la respuesta al cliente como si fuerais el cliente**: ¿entendéis qué ocurre con la temperatura y con los festivos? ¿Hay cifra con intervalo, una recomendación y límites? Contar las palabras (`len(texto.split())`).
3. **Mirar el código y la curva**: ¿baja la curva de aprendizaje? ¿Escribieron ellos `gradiente_mse` y `entrenar`, sin `scikit-learn`? Que quien lo escribió explique una línea.
4. **Poner un nivel (1 a 4) en cada criterio, con una frase de prueba** (por ejemplo: «3 · los cuatro puntos de control pasan, pero el segundo gráfico no tiene título»). Sin prueba escrita, el nivel no vale.
5. **Apuntar el resultado** en la celda de texto «Revisión con la rúbrica» al final del cuaderno y corregir lo más fácil de arreglar. Lo demás se anota como mejora.

Cada persona, además, se puntúa a sí misma en su hoja de [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md) con **esta misma rúbrica**.
