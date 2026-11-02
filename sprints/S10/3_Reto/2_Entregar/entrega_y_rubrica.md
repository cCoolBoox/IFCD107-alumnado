# Sprint 10 · Reto «¿Vale la pena la red?» · Entrega y rúbrica

> **Qué se sube y cómo se evalúa.** Se lee **una vez**, antes de entregar, y se vuelve a la rúbrica cuando el equipo revisa su trabajo. Mientras trabajáis no hace falta: para eso está [el reto en una página](../1_Trabajar/Reto_Sprint_10_una_pagina.md).
>
> - Volver al [README del sprint](../../README.md) · [ficha del reto](../3_Consultar/Reto_Sprint_10.md), para consultar.
> - Vuestra hoja personal: [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md).
> - Cómo subir a GitHub paso a paso, con capturas: [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md).

Esta hoja responde a **dos preguntas distintas**, una tabla para cada una:

**Tabla A · Los ficheros:** qué ficheros hay, de dónde sale cada uno (ya hecho, lo modificáis, lo creáis o lo genera el programa) y **cuáles se suben y adónde**.

**Tabla B · Los requisitos:** qué tiene que cumplir lo que entregáis y hasta dónde llegar (🟢 mínimo, 🟡 estándar, 🔴 extra). **Es lo que se evalúa.**

**En total, al final del sprint se suben a `sprint-10/`:** **3 ficheros del equipo** (`reto_vale_la_pena.ipynb`, `informe_comparativo.md`, `README.md`) **+ 1 autoevaluación y coevaluación por persona**, es decir, **3 + tantos ficheros como personas haya en el equipo** (un equipo de 4 sube 7). «El reto» no es un fichero aparte: son esos tres ficheros (el cuaderno ejecutado, el informe y el README que dice cómo repetirlo). Los datos no van a `sprint-10/`: el CSV va a `data/` si aún no está, y los extras solo si los hacéis. La *review* y la *retro* se hacen de palabra: no se suben.

## 1 · 📦 Tabla A · Los ficheros: de dónde sale cada uno y cuáles se suben

Todo lo que se sube va al repositorio privado del equipo (`ifcd107-equipo-…`), en la carpeta **`sprint-10/`**, salvo el CSV.

| Fichero | Origen | Qué hacéis vosotros | ¿Se sube? |
|---|---|---|---|
| `reto_vale_la_pena.ipynb` | **Lo modificáis.** Parte del cuaderno `S10_04`, que trae el esqueleto y cuatro ejercicios con hueco | Completáis los ejercicios, añadís vuestras variantes y vuestro diagnóstico, y lo descargáis con **todas las celdas ejecutadas** (nombre en minúsculas y sin espacios) | **Sí** · `sprint-10/` |
| `informe_comparativo.md` | **Lo creáis a partir de una plantilla.** Os damos `plantilla_informe_comparativo.md` con las seis partes | Copiarla como `informe_comparativo.md` y rellenarla (1–2 páginas, *ML clásico frente a MLP*) y, al final, la sección «Revisión con la rúbrica» | **Sí** · `sprint-10/` |
| `README.md` | **Lo modificáis.** Ya está creado en `sprint-10/` con la plantilla del repositorio del equipo | Lo rellenáis: qué se entrega, quién hizo qué y cómo repetirlo (abrir en Colab y ejecutar de arriba abajo) | **Sí** · `sprint-10/` |
| `reservas_turisdata.csv` | **Ya hecho.** Los datos del curso (sintéticos) | Nada: el cuaderno los descarga solo; no se modifican | **Sí**, sin cambios · `data/` (si aún no está) |
| Autoevaluación y coevaluación (`autoevaluacion_nombre.md`) | **Ya hecha, en blanco** | Cada persona copia la plantilla con su nombre y la rellena; la coevaluación va **dentro del mismo fichero** | **Sí**, **una por persona** (no una por equipo) · `sprint-10/` |
| `curvas_aprendizaje.png` (opcional) | **Lo generáis** guardando desde el cuaderno el dibujo de las curvas | Solo si queréis ver la imagen dentro del informe | Solo si lo hacéis · `sprint-10/` |
| `mlp_final.keras` (extra) | **Lo genera** el cuaderno al guardar el MLP elegido | Solo si el equipo llega al nivel extra (guardar el modelo y probarlo recargado) | Solo si lo hacéis · `sprint-10/` |

---

## 2 · ✅ Tabla B · Los requisitos: qué tiene que cumplir y hasta dónde llegar

| Requisito | Qué se pide exactamente | Nivel | Dónde se comprueba |
|---|---|---|---|
| **Cuaderno que se ejecuta** | De arriba abajo y sin errores, con semillas fijas, y con los cuatro ejercicios (`evaluar`, `aucs_mlp_val`, `diagnostico`, `hay_diferencia` y `mejor_modelo`) pasando sus comprobaciones | 🟢 Mínimo | `reto_vale_la_pena.ipynb` |
| **Partición única** | Una sola división entrenamiento / validación / prueba, igual para todos los modelos, que no se cambia; el escalador se ajusta **solo con el entrenamiento** | 🟢 Mínimo | `reto_vale_la_pena.ipynb` (sección 1) |
| **Referencia y MLP, con las mismas métricas** | Un modelo de referencia (el boosting del cuaderno o el campeón del Sprint 8) y un MLP de un solo problema (cancelaciones **o** precio), medidos con las mismas métricas y la misma partición; máximo 40 épocas | 🟢 Mínimo | `reto_vale_la_pena.ipynb` y la tabla del informe |
| **Curvas y diagnóstico** | Curva de aprendizaje del MLP (error en entrenamiento y en validación) y **una frase** que diga si hay sobreajuste, subajuste o buen ajuste | 🟢 Mínimo | `reto_vale_la_pena.ipynb` (sección 5) e informe |
| **La prueba, una sola vez** | El conjunto de prueba se mira una única vez, al final, con el modelo elegido y con la referencia | 🟢 Mínimo | `reto_vale_la_pena.ipynb` (sección 6) |
| **Recomendación en una frase** | «Recomendamos… porque…», al principio del informe | 🟢 Mínimo | `informe_comparativo.md` |
| **README del sprint** | Qué se entrega, quién hizo qué y cómo repetirlo | 🟢 Mínimo | `README.md` |
| **2–3 variantes del MLP** | Probar 2 o 3 variantes (tamaño, *dropout*, L2, tasa de aprendizaje o parada temprana), **elegidas mirando solo la validación**, con una tabla pequeña de resultados | 🟡 Estándar | `reto_vale_la_pena.ipynb` (sección 4) e informe |
| **Comparación con incertidumbre** | Varias semillas (por ejemplo, 3) con media ± desviación, o intervalo *bootstrap*; si los intervalos se solapan, no se dice que uno sea mejor | 🟡 Estándar | `reto_vale_la_pena.ipynb` (sección 6) e informe |
| **Coste** | Tiempo de entrenamiento, complejidad y explicabilidad de cada enfoque | 🟡 Estándar | `informe_comparativo.md` |
| **Informe completo** | Las seis partes del paso 6 (pregunta y respuesta, tabla con media ± desviación, curva comentada, coste, riesgos y límites) en 1–2 páginas, sin jerga que no se explique | 🟡 Estándar | `informe_comparativo.md` |
| **IA responsable** | Al menos **dos riesgos específicos de este caso** (datos sintéticos, umbral y coste de los errores por *overbooking*, posibles sesgos por país o canal) con una medida para cada uno; qué se pidió a la IA y qué se comprobó | 🟡 Estándar | `informe_comparativo.md` |
| **Revisión y autoevaluación** | Alguien que **no escribió esa parte** revisa cuaderno e informe con la rúbrica (justo debajo de estas tablas) y anota nivel y prueba en el informe; cada persona sube su hoja de autoevaluación y coevaluación | 🟡 Estándar | `informe_comparativo.md` (sección «Revisión con la rúbrica») y `sprint-10/` |
| **Extras** | Variante de regresión (precio por noche) con el mismo rigor · comparar el coste de entrenar y mantener cada modelo · guardar el modelo y probarlo recargado | 🔴 Extra | `reto_vale_la_pena.ipynb` (sección 7) · `informe_comparativo.md` · `mlp_final.keras` |

---

## 3 · 🧭 Rúbrica del reto · cómo se puntúa y cómo se revisa

La usan **dos veces**: el equipo, para revisar su propio trabajo antes de entregar, y el docente, para puntuar. Se mira **cada criterio por separado** y se pone el nivel de la columna cuyo texto **se cumple entero**: si lo de un nivel se cumple a medias, es el nivel de abajo. **0** significa que no se ha entregado nada de ese criterio.

Orientación: lo que pide el nivel 🟢 mínimo sale en un **2**, el 🟡 estándar en un **3** y los 🔴 extras en un **4**.

| Criterio | 1 · Empezado | 2 · Mínimo | 3 · Estándar | 4 · Extra |
|---|---|---|---|---|
| **Corrección técnica** (¿funciona y se mide bien?) | Hay cuaderno, pero se rompe al ejecutarlo de arriba abajo, fallan las comprobaciones o se ha mirado la prueba para decidir | Se ejecuta entero con semillas fijas; una sola partición; referencia y MLP medidos con las mismas métricas; curva de aprendizaje con una frase de diagnóstico; la prueba se usa una sola vez | Además, el escalador se ajusta solo con el entrenamiento, hay 2–3 variantes elegidas con la validación (con su tabla) y la comparación usa 3 semillas o *bootstrap*, con los cuatro ejercicios en verde | Además, la variante de precio con el mismo rigor, o el modelo guardado y recargado dando el mismo resultado |
| **Reproducibilidad** (¿lo puede repetir otra persona?) | Solo funciona en el Colab de quien lo escribió (celdas desordenadas o rutas propias) | El cuaderno se ejecuta de arriba abajo y el README dice qué se entrega, quién hizo qué y cómo abrirlo | Otra persona abre el cuaderno en Colab, pulsa *Reiniciar y ejecutar todo* y obtiene **las cifras del informe** siguiendo solo el README; los ficheros están en `sprint-10/`, subidos desde cuentas distintas | Además, el README indica las versiones (Python, Keras, scikit-learn), las semillas usadas y la ruta exacta de los datos |
| **Análisis y comunicación al cliente** (¿lo entiende quien no programa?) | El informe solo da números, sin decir qué significan | Tiene la tabla de ambos enfoques y la recomendación en una frase («Recomendamos… porque…») | Responde a «¿vale la pena?» con media ± desviación, dice si la diferencia es real o ruido, añade el coste (tiempo, complejidad, explicabilidad) y los límites, y comenta la curva, sin jerga | Además, dice **cuándo cambiaría la recomendación** (más datos, imágenes o texto) o qué pasaría con el umbral según lo que cueste un *overbooking* |
| **IA responsable** (¿se sabe qué hizo la IA y qué riesgos hay?) | No dice si se ha usado IA ni nombra ningún riesgo | Dice dónde se ha usado IA y nombra al menos un riesgo del caso | Dice **qué se pidió y qué se comprobó a mano**; nombra dos riesgos concretos (por ejemplo, datos sintéticos y *overbooking*) con una medida para cada uno; quien escribe sabe explicar cualquier celda | Además, aplica una medida y mide su efecto (por ejemplo, el error por país o canal, o un umbral distinto) o cuenta un fallo concreto de la IA que detectaron |

**Cómo se revisa** (unos 10 minutos, antes de subir; lo hace **una persona que no escribió esa parte**):

1. **Ejecutar** el cuaderno en una pestaña nueva de Colab: *Entorno de ejecución → Reiniciar y ejecutar todo*, siguiendo solo el README. Anotar si algo falla y si las cifras coinciden con las del informe.
2. **Leer el informe como si fuera el cliente**: ¿se entiende la respuesta a «¿vale la pena?» sin saber de redes neuronales? Subrayar lo que no se entienda.
3. **Mirar el cuaderno**: ¿hay una sola partición?, ¿se usa la prueba una sola vez?, ¿el escalador se ajusta solo con el entrenamiento? Que quien lo escribió explique una celda cualquiera.
4. **Poner un nivel (1 a 4) en cada criterio, con una frase de prueba** (por ejemplo: «3 · reinicia y ejecuta sin errores y el AUC coincide, pero falta explicar el coste»). Sin prueba escrita, el nivel no vale.
5. **Apuntar el resultado** en la sección «Revisión con la rúbrica» del final de `informe_comparativo.md` y corregir lo más fácil de arreglar. Lo demás se anota como mejora.

Cada persona, además, se puntúa a sí misma en su hoja de [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md) con **esta misma rúbrica**.
