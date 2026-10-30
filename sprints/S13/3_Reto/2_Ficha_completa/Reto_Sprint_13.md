# Sprint 13 · Reto «Informe visual para dirección»

> **Ficha completa del reto, para consultar.** Para trabajar con ella abierta, usad **el reto en una página** (carpeta `1_Reto_en_una_pagina` de este reto).
>
> - Volver al [README del sprint](../../README.md) · [README del sprint en PDF](../../4_Referencia/README_Sprint_13.pdf) · [ecofriendly](../../4_Referencia/README_Sprint_13_ecofriendly.pdf)
> - **Esta ficha en PDF:** [a color](pdf/Reto_Sprint_13.pdf) · [ecofriendly, para imprimir](pdf/Reto_Sprint_13_ecofriendly.pdf)
> - Si es vuestro primer reto: [Cómo se trabaja un reto](../../../../material/4.%20Como_se_trabaja_un_reto.md).

## Ficha del reto

### 1 · 🎯 Qué os pide el cliente

**Qué os pide el cliente.** Marcos, el director general de TurisData Canarias, tiene **10 minutos** antes de la reunión de ingresos. **No sabe qué es un AUC y no quiere saberlo.** Os pide: *«Una página. ¿Puedo fiarme del modelo, qué mueve las cancelaciones y qué hago el lunes?»* Este reto **no trata de entrenar un modelo mejor**, sino de **comunicar**: muchos proyectos de IA fracasan no porque el modelo sea malo, sino porque nadie con capacidad de decidir entiende lo que dice. Vais a convertir **vuestro mejor modelo del curso** en **una página que se entiende en 30 segundos**: un titular que dice qué hacer, cuatro gráficos honestos, tres viñetas sin jerga y un pie con los límites. Será la **semilla de la memoria técnica** del proyecto final.

**Cómo se trabaja.** No hace falta experiencia previa: os damos un **cuaderno plantilla que ya funciona** (al ejecutarlo de arriba abajo dibuja el panel de cuatro gráficos con un modelo de ejemplo) y un **texto de informe con huecos**. Vuestro trabajo es cambiar lo marcado con `# >>> EDITA`, poner títulos que **digan una conclusión** y escribir el texto. En clase tenéis **25 minutos de reto** el 25/11, dentro del último día del Sprint 12 (por eso es corto: **llegad con el modelo elegido**), y después la franja de entrega y review. El equipo decide hasta dónde llega: 🟢 mínimo, 🟡 estándar o 🔴 extra.

---

### 2 · 🧰 Recursos del reto

| Recurso | Para qué lo usaréis | Dónde está |
|---|---|---|
| **Un navegador y Google Colab** (Python y las librerías ya vienen instaladas) | Ejecutar el cuaderno plantilla y generar el panel | Se abre con el botón de la fila siguiente; no hay que instalar nada |
| **Cuaderno plantilla** [`S13_02_plantilla_informe_visual`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/2_Practica/S13_02_plantilla_informe_visual.ipynb) | Adaptarlo a vuestro modelo: dibuja el panel 2 × 2 y lo guarda como `informe_visual_panel.png` | Colab; su [código explicado](../../2_Practica/codigo_explicado/S13_02_plantilla_informe_visual.md) |
| **Plantilla del informe** [`plantilla_informe_visual.md`](../4_Plantillas_y_entrega/plantilla_informe_visual.md) | El texto de la página (titular, gráficos, viñetas, IA responsable, pie), la lista de comprobación y la sección «Revisión con la rúbrica» | En GitHub: *Raw* para copiar el texto. Trabajad en una copia |
| **Vuestro mejor modelo del curso** | Es el que se cuenta en la página (el campeón del Sprint 8, por ejemplo) | Vuestros cuadernos de los Sprints 8, 10 o 12. Si no cargara a tiempo, la plantilla trae un modelo de ejemplo que sí funciona |
| **El CSV** [`reservas_turisdata.csv`](../../../../datos/reservas_turisdata.csv) | Las reservas **sintéticas** con las que se entrenó y se prueba el modelo | El cuaderno lo descarga solo |
| **Cuaderno del sprint** [`S13_01_visualizacion_resultados`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/2_Practica/S13_01_visualizacion_resultados.ipynb) y la [presentación S13.1](../../1_Teoria/S13.1_Visualizar_y_comunicar_resultados.pdf) | Las pistas para los gráficos (matriz de confusión, ROC, importancia, umbral y coste) y las reglas de comunicación | Colab y PDF; lo hicisteis justo antes del reto |
| **Cómo entregar en GitHub** | Subir los ficheros a `sprint-13/` | [Guía de entrega](../../../../material/5.%20Como_entregar_en_GitHub.md) |
| **Autoevaluación y coevaluación** | Cada persona rellena su hoja | [Hoja del sprint](../4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md) |
| **Un asistente de IA** (opcional) | Quitar jerga, probar titulares y simular al director | Con las reglas de la «Ayuda 1» del paso a paso |

---

### 3 · 📦 Qué entregar

Este apartado responde a **dos preguntas distintas**, una tabla para cada una:

**Tabla A · Los ficheros:** qué ficheros hay, de dónde sale cada uno (ya hecho, lo modificáis, lo creáis o lo genera el programa) y **cuáles se suben y adónde**.

**Tabla B · Los requisitos:** qué tiene que cumplir lo que entregáis y hasta dónde llegar (🟢 mínimo, 🟡 estándar, 🔴 extra). **Es lo que se evalúa.**

**En total, al final del sprint se suben a `sprint-13/`:** **3 ficheros del equipo** (`informe_visual.md`, `informe_visual_panel.png`, `informe_visual.ipynb`) **+ 1 autoevaluación y coevaluación por persona**, es decir, **3 + tantos ficheros como personas haya en el equipo** (un equipo de 3 sube 6). «El reto» no es un fichero aparte: es la página (`informe_visual.md` con su PNG) y el cuaderno que la genera. El CSV no se sube a `sprint-13/`: va a `data/` solo si el repositorio aún no lo tiene. El PDF de una página y los extras solo si los hacéis. La *review* y la *retro* se hacen de palabra: no se suben.

#### Tabla A · Los ficheros: de dónde sale cada uno y cuáles se suben

Todo lo que se sube va al repositorio privado del equipo (`ifcd107-equipo-…`), en la carpeta **`sprint-13/`**, salvo el CSV.

| Fichero | Origen | Qué hacéis vosotros | ¿Se sube? |
|---|---|---|---|
| `informe_visual.md` | **Lo creáis a partir de una plantilla.** Os damos `plantilla_informe_visual.md` con huecos | Copiarla como `informe_visual.md`, rellenarla y añadir la imagen del panel | **Sí** · `sprint-13/` |
| `informe_visual_panel.png` | **Lo genera el cuaderno** al ejecutar la celda del panel | Ejecutar el cuaderno, descargar la imagen del panel de archivos de Colab y no editarla a mano | **Sí** · `sprint-13/` |
| `informe_visual.ipynb` | **Lo modificáis.** Parte de `S13_02_plantilla_informe_visual.ipynb`, que ya funciona | Cambiar solo lo marcado con `# >>> EDITA` (modelo, costes, umbral, títulos), guardarlo con *Archivo → Descargar → Descargar .ipynb* y ponerle ese nombre | **Sí** · `sprint-13/` |
| `reservas_turisdata.csv` | **Ya hecho.** Los datos reales (sintéticos) | Nada: el cuaderno lo descarga solo | **Sí**, sin cambios · `data/` (si aún no está) |
| Autoevaluación y coevaluación (`autoevaluacion_nombre.md`) | **Ya hecha, en blanco** | Cada persona copia la plantilla con su nombre y la rellena; la coevaluación va **dentro del mismo fichero** | **Sí**, **una por persona** (no una por equipo) · `sprint-13/` |
| `informe_visual.pdf` (extra) | **Lo generáis vosotros** a partir del informe | Solo si queréis proyectar o imprimir la página en PDF; va **además** del `.md`, no en su lugar | Solo si lo hacéis · `sprint-13/` |

#### Tabla B · Los requisitos: qué tiene que cumplir y hasta dónde llegar

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

#### Rúbrica del reto · cómo se puntúa y cómo se revisa

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

Cada persona, además, se puntúa a sí misma en su hoja de [autoevaluación y coevaluación](../4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md) con **esta misma rúbrica**.

---

### 4 · 🪜 Guía paso a paso

Son cuatro pasos, de **25 minutos en total** (el 25/11, dentro del último día del Sprint 12). Cada uno dice **qué hacéis** (la lista corta), **cómo se hace** con el detalle, **qué deberíais ver** y **cuándo está hecho**. Las ayudas (IA, errores, atascos) están al final. Si el tiempo aprieta, completad el nivel mínimo (tres gráficos, titular y tres viñetas) y dejad lo demás para la franja de entrega o para casa.

#### Paso 1 · Elegir el modelo, cargarlo y fijar los costes (día 1, 4 minutos)
1. Elegir el mejor modelo del curso y abrir el cuaderno plantilla en Colab.
2. Comprobar que el modelo se carga y que el cuaderno llega hasta el final sin errores.
3. Escribir el coste de cada error y el umbral.
4. Repartir el trabajo del paso 2.

**Cómo se hace**
- **Abrir la plantilla.** Pulsad el botón de Colab del apartado 2 y guardad una copia (*Archivo → Guardar una copia en Drive*), para no perder los cambios.
- **Cambiar el modelo.** Buscad la línea marcada `# >>> EDITA` en la celda «1. Datos y modelo» y poned vuestro modelo. Tiene que ser un objeto que sepa dar probabilidades (`predict_proba`) y que reciba `X_test`. Mantened las **semillas** y la separación entre entrenamiento y prueba, y usad **el mismo preprocesado con el que se entrenó**. Si el modelo no carga a tiempo, dejad el de ejemplo (regresión logística), que sí funciona, y decidlo en el pie del informe.
- **Fijar los costes.** En la celda «Parámetros del informe» cambiad `COSTE_FN` (lo que perdéis por cada cancelación que el modelo no detecta, es decir, una habitación vacía) y `COSTE_FP` (lo que cuesta avisar a quien sí iba a venir). Los valores de la plantilla (50 y 30) son de ejemplo. Preguntadle al docente, que hace de cliente; si no lo sabe, **proponed una hipótesis y escribidla**.
- **Elegir el umbral.** `UMBRAL` es la probabilidad a partir de la cual avisáis. Elegidlo con el gráfico de costes del cuaderno [`S13_01`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/2_Practica/S13_01_visualizacion_resultados.ipynb), no por costumbre.

| Persona | Parte | Minutos |
|---|---|---|
| A | Modelo, costes y cuaderno (paso 1) | 4 |
| B | Los gráficos y sus títulos (paso 2) | 8 |
| C | Titular, viñetas y pie (paso 3) | 8 |
| D (si hay 4) | Prueba de los 30 segundos y revisión (paso 4) | 5 |

**Qué deberíais ver.** Una línea como `AUC en prueba: … · reservas de prueba: …` al final de la celda de datos y modelo, y ningún mensaje de error rojo.

**Hecho cuando:** el modelo se carga, `COSTE_FN`, `COSTE_FP` y `UMBRAL` están escritos, y cada persona sabe qué parte le toca.

#### Paso 2 · Ajustar los gráficos con título-conclusión (día 1, 8 minutos)
1. Ejecutar las celdas de cálculos y del panel.
2. Cambiar el título de cada gráfico para que **diga una conclusión** con su cifra.
3. Comprobar que cada gráfico tiene ejes con nombre, barras desde 0 y pocos colores.
4. Volver a ejecutar para guardar el PNG con los cambios.

**Cómo se hace.** El panel tiene cuatro gráficos y cada uno contesta a una pregunta de Marcos. Los títulos que lleva la plantilla son un punto de partida: los marcados con `# >>> EDITA` tenéis que reescribirlos.

| Gráfico | Contesta a | Qué cambiáis | Ejemplo de título-conclusión |
|---|---|---|---|
| 1. Matriz de confusión (en %) | ¿Puedo fiarme? | Nada si los números cambian solos; revisad que el título diga lo que se ve | «Detectamos 7 de cada 10 cancelaciones, con 2 falsas alarmas de cada 10» |
| 2. Curva ROC (la que se añade en el nivel 🟡) | ¿Puedo fiarme? | El título (hoy es genérico) | «Acierta bastante mejor que el azar, pero no es perfecto» |
| 3. Importancia de variables | ¿Qué mueve las cancelaciones? | El título: nombrad la variable líder | «La tarifa flexible es lo que más pesa en una cancelación» |
| 4. Coste con y sin modelo | ¿Qué hago el lunes? | El título, con el ahorro en € | «Con el modelo perdemos 1 230 € menos en 3 000 reservas» |

Los ejemplos llevan cifras inventadas: las vuestras son las que salen en vuestro gráfico. Para cada gráfico comprobad esta lista corta:
- El título enuncia una conclusión y se **ve realmente** en el gráfico.
- Los ejes tienen nombre y las barras empiezan en 0 (el gráfico 4 ya lleva `set_ylim(0, …)`). Nada de 3D y 3–4 colores con sentido.
- Está calculado sobre el **test**, no sobre el entrenamiento.

**Qué deberíais ver.** Un panel de 2 × 2 con vuestros cuatro títulos y, en el panel de archivos de Colab (icono de la carpeta), el fichero `informe_visual_panel.png`.

**Hecho cuando:** cada gráfico tiene un título-conclusión y ejes con nombre, y el PNG se ha generado **después** del último cambio.

#### Paso 3 · Escribir titular, viñetas y pie (día 1, 8 minutos)
1. Copiar `plantilla_informe_visual.md` como `informe_visual.md`.
2. Escribir el titular-decisión y las tres viñetas, sin jerga.
3. Rellenar la sección de IA responsable y el pie.
4. Comprobar que las cifras del texto son las mismas que las del gráfico.

**Cómo se hace**
- **Copiar la plantilla.** En GitHub abrid el archivo y pulsad *Raw*; copiad el texto y pegadlo en un archivo nuevo llamado `informe_visual.md`. Sustituid todo lo que está entre corchetes.
- **El titular** es una decisión de una línea: qué hacer, a quién y con qué efecto. Ejemplo (cifras inventadas): «Llamar cada lunes a las 25 reservas de mayor riesgo evitaría unas 8 habitaciones vacías al mes». Debajo de «Los cuatro gráficos» poned vuestros cuatro títulos con una frase cada uno y añadid la línea `![Panel del informe](informe_visual_panel.png )` (el espacio antes del último paréntesis es opcional).
- **Las tres viñetas** son «Qué hemos hecho» (cuántos datos, qué se predice), «Qué recomendamos» (acción, umbral y ahorro esperado) y «Qué límites tiene» (datos sintéticos, dónde falla más, qué no debe usarse para decidir). Entre el titular, los gráficos y las viñetas tienen que quedar contestadas las tres preguntas de Marcos.
- **IA responsable, en dos líneas.** Un riesgo concreto y una medida. Ejemplo: «El modelo no debe usarse para negar reservas a nadie; solo para priorizar avisos».
- **El pie** lleva los datos (con cuántas reservas y qué periodo), el modelo, el umbral, la semilla, el cuaderno y quién es responsable. Si habéis usado IA, decidlo aquí.
- **Traducir la jerga.** Si una sigla aparece, va con una frase:

| Palabra | Cómo decirlo |
|---|---|
| AUC | «nota de 0,5 a 1 de lo bien que el modelo separa a quien cancela de quien no» |
| F1 | «número que combina cuántos avisos acierta y cuántas cancelaciones detecta» |
| SHAP | «forma de ver qué datos empujan más la decisión del modelo» |
| Falso negativo / falso positivo | «cancelación que no detectamos» / «falsa alarma» |

**Qué deberíais ver.** Un `informe_visual.md` que se lee en un minuto, con el panel a la vista, un titular que es una decisión y todas las cifras del texto iguales que las del gráfico.

**Hecho cuando:** no queda ningún corchete de la plantilla, no hay jerga sin explicar y alguien ha comparado una por una las cifras del texto con las del gráfico.

#### Paso 4 · Probar con otro equipo, revisar con la rúbrica y dejarlo listo (día 1, 5 minutos)
1. Pasar la página a otro equipo y preguntar: **«¿Entiendes la decisión en 30 segundos?»**
2. Si no la entienden o entienden otra cosa, reescribir el titular.
3. Pedir a alguien que no escribió esa parte que la revise con la rúbrica y anote el resultado en `informe_visual.md`.

**Cómo se hace**
- **La prueba de los 30 segundos.** Quien lee mira la página 30 segundos y dice **con sus palabras** qué decisión entiende. Si no coincide con la vuestra, **el mensaje no está claro**: reescribid el titular, no el lector.
- **La revisión con la rúbrica.** Quien revisa sigue los cinco pasos de «Cómo se revisa» (apartado 3) y rellena la sección «Revisión con la rúbrica» del final de `informe_visual.md`: un nivel de 1 a 4 por criterio y **una frase de prueba**. Esa sección va debajo de la página del informe y no se proyecta. Si no da tiempo, se acaba al empezar la franja de entrega.
- **Antes de subir.** Repasad la lista de comprobación del final de la plantilla (la «Definition of Done» del reto) y descargad el cuaderno con *Archivo → Descargar → Descargar .ipynb*, con el nombre `informe_visual.ipynb`.
- **Subir los ficheros (la vía del curso, desde el navegador), en la franja de entrega.** Seguid [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md): (1) abrid el repositorio del equipo y **entrad primero en la carpeta `sprint-13`**; (2) *Add file → Upload files*; (3) arrastrad `informe_visual.md`, `informe_visual_panel.png` e `informe_visual.ipynb`; (4) escribid un mensaje corto y pulsad **Commit changes**. Cada subida es un *commit* con el nombre de quien la hace, así que repartidlas entre personas. Los nombres de archivo, **en minúsculas y sin espacios**.

**Qué deberíais ver.** Una página que otro equipo entiende, la sección «Revisión con la rúbrica» rellena con un nivel y una frase de prueba por criterio, y, tras la subida, en la carpeta `sprint-13` del repositorio, los tres ficheros del equipo y una hoja de autoevaluación por persona (**3 + N**).

**Hecho cuando:** otro equipo ha dicho la misma decisión que vosotros, la revisión con la rúbrica está anotada y los ficheros están listos para subir a `sprint-13/`.

**Después, en la franja de entrega y review:** cada persona rellena y sube su autoevaluación y coevaluación a `sprint-13/`, y cada equipo proyecta su página 30 segundos. **El resto de la clase dice la decisión que entiende**; si no coincide con la del equipo, el mensaje no está claro. Se comparan los titulares y se elige el más claro.

#### Ayuda 1 · Cómo usar la IA en este reto

La IA puede ahorrar tiempo, pero **es muy mala copiando cifras**. Reglas:
- **Todo lo que dé, lo comprobáis.** Si cambia una cifra, no vale.
- **Las cifras mandan:** las del texto tienen que ser las mismas que las del gráfico.
- **Declaradlo** en el pie del informe o en la sección de IA responsable: qué pedisteis y qué revisasteis.
- **Nada de datos personales ni claves** en una IA.

| Para qué | Ejemplo de petición | Qué comprobáis |
|---|---|---|
| Quitar jerga | «Reescribe estas tres viñetas para un director que no sabe estadística. No cambies ninguna cifra: *[viñetas]*» | Que **las cifras son idénticas** |
| Probar titulares | «Dame 5 versiones de este titular, cada una de menos de 15 palabras, que enuncien una decisión: *[titular]*» | Que la elegida siga siendo verdad |
| Mejorar un gráfico | «Este título describe el gráfico pero no concluye: *[título]*. Propón títulos-conclusión» | Que la conclusión **se vea realmente** en el gráfico |
| Simular al director | «Hazte pasar por un director de hotel sin formación técnica. Lee esta página y dime qué no entiendes» | Que tomáis nota y corregís |

#### Ayuda 2 · Errores frecuentes (y cómo evitarlos)

| Error | Por qué ocurre | Cómo evitarlo |
|---|---|---|
| Un informe lleno de gráficos y sin decisión | Se muestra todo lo que se hizo | Cuatro gráficos, un titular |
| Títulos descriptivos («AUC por modelo») | Es lo que sale por defecto | «El modelo detecta 7 de cada 10 cancelaciones» |
| Barras que no empiezan en 0 | La herramienta lo hace sola | Fijar el eje a 0 |
| Métricas sobre el entrenamiento | Se reutiliza el cuaderno sin mirar | Comprobar que usan `X_test` |
| Jerga sin explicar | Se escribe para el docente | La prueba de los 30 segundos con otro equipo |
| Texto con cifras distintas del gráfico | Se edita una y no la otra | Revisión cruzada, cifra por cifra |
| El PNG no coincide con el texto | Se cambió algo en el cuaderno y no se volvió a ejecutar | Reiniciar y ejecutar todo antes de descargar el PNG |

#### Ayuda 3 · Si os atascáis

1. **El tiempo se acaba:** reducid a tres gráficos y escribid primero el titular y las viñetas; los gráficos se ajustan después.
2. **No sabéis qué decisión recomendar:** pensad en una acción con persona y fecha («recepción llama los lunes»).
3. **El modelo no carga en la plantilla:** comprobad que usáis el mismo preprocesado con el que se entrenó; si no, dejad el modelo de ejemplo y decidlo en el pie. Después, preguntad al equipo y al docente.
