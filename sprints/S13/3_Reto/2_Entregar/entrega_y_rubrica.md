# Sprint 13 · Reto «Informe visual para dirección» · Entrega y rúbrica

> **Qué se sube y cómo se evalúa.** Se lee **una vez**, antes de entregar, y se vuelve a la rúbrica cuando el equipo revisa su trabajo. Mientras trabajáis no hace falta: para eso está [el reto en una página](../1_Trabajar/Reto_Sprint_13_una_pagina.md).
>
> - Volver al [README del sprint](../../README.md) · [ficha del reto](../3_Consultar/Reto_Sprint_13.md), para consultar.
> - Vuestra hoja personal: [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md).
> - Cómo subir a GitHub paso a paso, con capturas: [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md).

Esta hoja responde a **dos preguntas distintas**, una tabla para cada una:

**Tabla A · Los ficheros:** qué ficheros hay, de dónde sale cada uno (ya hecho, lo modificáis, lo creáis o lo genera el programa) y **cuáles se suben y adónde**.

**Tabla B · Los requisitos:** qué tiene que cumplir lo que entregáis y hasta dónde llegar (🟢 mínimo, 🟡 estándar, 🔴 extra). **Es lo que se evalúa.**

**En total, al final del sprint se suben a `sprint-13/`:** **3 ficheros del equipo** (`informe_visual.md`, `informe_visual_panel.png`, `informe_visual.ipynb`) **+ 1 autoevaluación y coevaluación por persona**, es decir, **3 + tantos ficheros como personas haya en el equipo** (un equipo de 3 sube 6). «El reto» no es un fichero aparte: es la página (`informe_visual.md` con su PNG) y el cuaderno que la genera. El CSV no se sube a `sprint-13/`: va a `data/` solo si el repositorio aún no lo tiene. El PDF de una página y los extras solo si los hacéis. La *review* y la *retro* se hacen de palabra: no se suben.

## 1 · 📦 Tabla A · Los ficheros: de dónde sale cada uno y cuáles se suben

Todo lo que se sube va al repositorio privado del equipo (`ifcd107-equipo-…`), en la carpeta **`sprint-13/`**, salvo el CSV.

| Fichero | Origen | Qué hacéis vosotros | ¿Se sube? |
|---|---|---|---|
| `informe_visual.md` | **Lo creáis a partir de una plantilla.** Os damos `plantilla_informe_visual.md` con huecos | Copiarla como `informe_visual.md`, rellenarla y añadir la imagen del panel | **Sí** · `sprint-13/` |
| `informe_visual_panel.png` | **Lo genera el cuaderno** al ejecutar la celda del panel | Ejecutar el cuaderno, descargar la imagen del panel de archivos de Colab y no editarla a mano | **Sí** · `sprint-13/` |
| `informe_visual.ipynb` | **Lo modificáis.** Parte de `S13_02_plantilla_informe_visual.ipynb`, que ya funciona | Cambiar solo lo marcado con `# >>> EDITA` (modelo, costes, umbral, títulos), guardarlo con *Archivo → Descargar → Descargar .ipynb* y ponerle ese nombre | **Sí** · `sprint-13/` |
| `reservas_turisdata.csv` | **Ya hecho.** Los datos reales (sintéticos) | Nada: el cuaderno lo descarga solo | **Sí**, sin cambios · `data/` (si aún no está) |
| Autoevaluación y coevaluación (`autoevaluacion_nombre.md`) | **Ya hecha, en blanco** | Cada persona copia la plantilla con su nombre y la rellena; la coevaluación va **dentro del mismo fichero** | **Sí**, **una por persona** (no una por equipo) · `sprint-13/` |
| `informe_visual.pdf` (extra) | **Lo generáis vosotros** a partir del informe | Solo si queréis proyectar o imprimir la página en PDF; va **además** del `.md`, no en su lugar | Solo si lo hacéis · `sprint-13/` |

---

## 2 · ✅ Tabla B · Los requisitos: qué tiene que cumplir y hasta dónde llegar

| Requisito | Qué se pide exactamente | Nivel | Dónde se comprueba |
|---|---|---|---|
| **Modelo elegido** | Vuestro mejor modelo del curso se carga en la plantilla (un objeto con `predict_proba` que recibe `X_test`) y el cuaderno imprime su resultado en el test | 🟢 Mínimo | `informe_visual.ipynb` |
| **Costes de los errores** | `COSTE_FN` (cancelación no detectada) y `COSTE_FP` (falsa alarma) escritos, con el valor acordado con el docente o una hipótesis anotada | 🟢 Mínimo | `informe_visual.ipynb` y pie de `informe_visual.md` |
| **Tres gráficos con título-conclusión** | Uno por pregunta del director: fiabilidad (matriz de confusión), qué mueve las cancelaciones (importancia de variables) y qué ahorro hay (coste con y sin modelo); cada título dice **algo que se puede discutir** | 🟢 Mínimo | `informe_visual_panel.png` |
| **Calculado sobre el test** | Matriz, ROC, importancia y ahorro salen de los datos que el modelo no vio | 🟢 Mínimo | `informe_visual.ipynb` |
| **Titular-decisión** | Una línea que dice **qué hacer**, a quién y con qué efecto, no solo qué pasa | 🟢 Mínimo | `informe_visual.md` |
| **Tres viñetas** | «Qué hemos hecho», «Qué recomendamos» y «Qué límites tiene», en frases cortas con cifras | 🟢 Mínimo | `informe_visual.md` |
| **Guardado en el repositorio** | Los tres ficheros en `sprint-13/`, como semilla de la memoria técnica | 🟢 Mínimo | Repositorio del equipo |
| **Cuarto gráfico y gráficos honestos** | Se añade la curva ROC; en los cuatro: ejes con nombre, barras desde 0, sin 3D, 3–4 colores con sentido | 🟡 Estándar | `informe_visual_panel.png` |
| **Sin jerga y cifras coherentes** | Si aparece «AUC», «F1» o «SHAP» va con una frase que lo explica; las cifras del texto son **las mismas** que las del gráfico | 🟡 Estándar | `informe_visual.md` |
| **Pie del informe** | Con cuántos datos, qué modelo, qué umbral, qué semilla, qué límites y quién es responsable | 🟡 Estándar | `informe_visual.md` |
| **IA responsable** | Un riesgo específico (por ejemplo, el uso indebido o un grupo peor atendido) con una medida, y qué se pidió a la IA y qué se revisó | 🟡 Estándar | `informe_visual.md` (sección «IA responsable») |
| **Cuaderno reproducible** | Se ejecuta de arriba abajo (*Reiniciar y ejecutar todo*) con semillas fijas y sale el mismo PNG | 🟡 Estándar | `informe_visual.ipynb` |
| **Prueba de los 30 segundos** | Otro equipo lee la página y dice qué decisión entiende; si no coincide con la vuestra, se reescribe el titular | 🟡 Estándar | En clase, con otro equipo |
| **Revisión y autoevaluación** | Alguien que **no escribió esa parte** revisa la página y el cuaderno con la rúbrica (justo debajo de estas tablas) y anota nivel y prueba en `informe_visual.md`; cada persona sube su hoja de autoevaluación y coevaluación | 🟡 Estándar | `informe_visual.md` (sección «Revisión con la rúbrica») y `sprint-13/` |
| **Extras** | Comparar dos umbrales o dos modelos y justificar la elección · rendimiento por subgrupos (país, canal) con una medida · ahorro en euros con una recomendación accionable y sus límites · versiones de las librerías | 🔴 Extra | `informe_visual.ipynb` · `informe_visual.md` |

---

## 3 · 🧭 Rúbrica del reto · cómo se puntúa y cómo se revisa

La usan **dos veces**: el equipo, para revisar su propio trabajo antes de entregar (es lo que dice la *Definition of Done*), y el docente, para puntuar. Se mira **cada criterio por separado** y se pone el nivel de la columna cuyo texto **se cumple entero**: si lo de un nivel se cumple a medias, es el nivel de abajo. **0** significa que no se ha entregado nada de ese criterio.

Orientación: lo que pide el nivel 🟢 mínimo sale en un **2**, el 🟡 estándar en un **3** y los 🔴 extras en un **4**.

| Criterio | 1 · Empezado | 2 · Mínimo | 3 · Estándar | 4 · Extra |
|---|---|---|---|---|
| **Corrección técnica** (¿los gráficos dicen la verdad?) | Hay gráficos, pero calculados sobre el entrenamiento, o el modelo elegido no carga en el cuaderno | Tres gráficos calculados sobre el test con el modelo elegido y los costes escritos; algún fallo menor (un eje sin nombre, el umbral sin explicar) | Cuatro gráficos sobre el test, con barras desde 0, sin 3D y 3–4 colores con sentido; el umbral y los costes están explicados y el ahorro del gráfico coincide con el del cuaderno | Además compara dos umbrales o dos modelos y justifica la elección con los costes |
| **Reproducibilidad** (¿lo puede repetir otra persona?) | El cuaderno no se puede volver a ejecutar o falta el PNG | El cuaderno se ejecuta con ayuda (hay que arreglar una ruta o repetir celdas) | Otra persona hace *Reiniciar y ejecutar todo*, con semillas fijas, y obtiene el **mismo PNG y las mismas cifras**; el pie indica datos, modelo, umbral y semilla | Además indica las versiones de las librerías y guarda el PNG generado junto al informe |
| **Análisis y comunicación al cliente** (¿lo entiende quien no programa?) | Los títulos solo describen («AUC por modelo») y no hay decisión | Hay titular y viñetas, y algún título-conclusión, pero queda alguna sigla sin explicar | Titular-decisión, **todos** los títulos con una conclusión y tres viñetas sin jerga; cifras del texto = cifras del gráfico y otro equipo entiende la decisión en 30 segundos | Además cuantifica el valor en euros y da una recomendación accionable (quién, cuándo, con qué umbral) con sus límites |
| **IA responsable** (¿se sabe qué hizo la IA y qué riesgos hay?) | No se menciona la IA ni ningún riesgo | Una mención genérica («puede haber sesgos») o dice que se usó IA sin detalle | Un riesgo específico con su medida (por ejemplo, «no se usa para negar reservas») y qué se pidió a la IA y qué se revisó; se dice que los datos son sintéticos | Además comprueba el rendimiento por subgrupos (país, canal) y propone medidas con la cifra encontrada |

**Cómo se revisa** (unos 5 minutos en clase; si no da tiempo, se acaba al empezar la entrega; lo hace **una persona que no escribió esa parte**):

1. **Ejecutar** el cuaderno en una pestaña nueva de Colab con *Entorno de ejecución → Reiniciar y ejecutar todo*, y comparar el PNG y las cifras con las del informe. Anotar si algo no sale igual.
2. **Leer la página como si fuerais Marcos**, con 30 segundos en el reloj: ¿qué decisión entendéis? Subrayar toda la jerga y toda cifra que no sepáis de dónde sale.
3. **Mirar los gráficos uno a uno**: ¿el título es una conclusión?, ¿los ejes tienen nombre?, ¿las barras empiezan en 0?, ¿se calcula sobre el test?
4. **Poner un nivel (1 a 4) en cada criterio, con una frase de prueba** (por ejemplo: «3 · reinicio y ejecuto todo y sale el mismo PNG, pero el gráfico 2 tiene un título descriptivo»). Sin prueba escrita, el nivel no vale.
5. **Apuntar el resultado** en la sección «Revisión con la rúbrica» del final de `informe_visual.md` y corregir lo más fácil de arreglar. Lo demás se anota como mejora.

Cada persona, además, se puntúa a sí misma en su hoja de [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md) con **esta misma rúbrica**.
