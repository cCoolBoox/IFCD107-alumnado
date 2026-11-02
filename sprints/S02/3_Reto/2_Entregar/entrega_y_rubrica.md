# Sprint 2 · Reto «¿Nos fiamos de este informe?» · Entrega y rúbrica

> **Qué se sube y cómo se evalúa.** Se lee **una vez**, antes de entregar, y se vuelve a la rúbrica cuando el equipo revisa su trabajo. Mientras trabajáis no hace falta: para eso está [el reto en una página](../1_Trabajar/Reto_Sprint_02_una_pagina.md).
>
> - Volver al [README del sprint](../../README.md) · [ficha del reto](../3_Consultar/Reto_Sprint_02.md), para consultar.
> - Vuestra hoja personal: [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md).
> - Cómo subir a GitHub paso a paso, con capturas: [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md).

Esta hoja responde a **dos preguntas distintas**, una tabla para cada una:

**Tabla A · Los ficheros:** qué ficheros hay, de dónde sale cada uno (ya hecho, lo modificáis, lo creáis o lo genera el programa) y **cuáles se suben y adónde**.

**Tabla B · Los requisitos:** qué tiene que cumplir lo que entregáis y hasta dónde llegar (🟢 mínimo, 🟡 estándar, 🔴 extra). **Es lo que se evalúa.**

**En total, al final del sprint se suben a `sprint-02/`:** **2 ficheros del equipo** (`dictamen.md`, `ejercicios.md`) **+ 1 autoevaluación y coevaluación por persona**, es decir, **2 + tantos ficheros como personas haya en el equipo** (un equipo de 3 sube 5). «El reto» no es un fichero aparte: es **el dictamen**, con la recomendación sobre el canal, la frase de IA responsable y el apartado «Uso de IA» escritos dentro. La hoja de cálculo es un extra opcional. El tablero se enseña en la review, y la *review* y la *retro* se hacen de palabra: no se suben.

## 1 · 📦 Tabla A · Los ficheros: de dónde sale cada uno y cuáles se suben

Todo lo que se sube va al repositorio privado del equipo (`ifcd107-equipo-…`), en la carpeta **`sprint-02/`**.

| Fichero | Origen | Qué hacéis vosotros | ¿Se sube? |
|---|---|---|---|
| `dictamen.md` | **Lo creáis a partir de una plantilla.** Os damos [`plantilla_dictamen.md`](../1_Trabajar/plantillas/plantilla_dictamen.md), con la afirmación 1 ya resuelta como modelo | Copiarla como `dictamen.md`, completar la afirmación 2 (con su tabla y la recomendación de tres líneas), al menos dos afirmaciones más de la 3 a la 6, la frase de IA responsable y «Uso de IA»; rellenar todos los huecos | **Sí** · `sprint-02/` |
| `ejercicios.md` | **Lo creáis.** No hay plantilla: los enunciados están en las hojas de práctica | Escribir las respuestas del mínimo básico, con cómo las habéis hecho: M1, M2 y M7 de la [hoja 1](../../2_Practica/ejercicios_algebra_calculo.md) y E1, E2, E6, E8 y E10 de la [hoja 2](../../2_Practica/ejercicios_estadistica.md) | **Sí** · `sprint-02/` |
| Autoevaluación y coevaluación (`autoevaluacion_nombre.md`) | **Ya hecha, en blanco** | Cada persona copia la plantilla con su nombre y la rellena; la coevaluación va **dentro del mismo fichero** | **Sí**, **una por persona** (no una por equipo) · `sprint-02/` |
| `hoja_calculo.xlsx` | **Lo creáis** si hacéis el extra: la hoja de cálculo del paso 3, descargada | En Google Sheets: *Archivo → Descargar → Microsoft Excel (.xlsx)* | Solo si hacéis el extra · `sprint-02/` |
| `informe_cliente.md` e `informe_cliente.csv` | **Ya hecho.** El informe y los datos del cliente | Nada: se leen y se copian a la hoja de cálculo sin cambiar nada | **No**: ya están en el material del reto |
| Borradores, reparto y cuentas en papel | **Lo creáis** en papel, pizarra o pantalla | Servirse de ellos para preparar el dictamen; no hay formato | **No se suben** |

---

## 2 · ✅ Tabla B · Los requisitos: qué tiene que cumplir y hasta dónde llegar

| Requisito | Qué se pide exactamente | Nivel | Dónde se comprueba |
|---|---|---|---|
| **Colab operativo** | Cada persona ha abierto un cuaderno en Colab y ha ejecutado una celda (el Sprint 3 lo usa) | 🟢 Mínimo | Día 1, en clase, con `alta_cuentas.md` |
| **Cuatro afirmaciones auditadas** | La 1, la 2 y dos más de la 3 a la 6, cada una con su **carta**, su **veredicto** y una **frase corregida** | 🟢 Mínimo | `dictamen.md` |
| **Cuentas rehechas** | Las tasas de las afirmaciones 1 y 2 están bien (cancelaciones ÷ reservas **del mismo grupo**) y cada cifra lleva su operación | 🟢 Mínimo | `dictamen.md` (afirmaciones 1 y 2) |
| **Sin inventar números** | Si no hay datos, el veredicto es «no se puede saber» y se dice qué datos faltan; ninguna cifra que no se pueda rehacer con los datos del informe | 🟢 Mínimo | `dictamen.md` (campo «Qué datos faltan») |
| **Ejercicios del mínimo básico** | M1, M2 y M7 de la hoja 1 y E1, E2, E6, E8 y E10 de la hoja 2, con cómo se han hecho | 🟢 Mínimo | `ejercicios.md` |
| **Uso de IA** | Una línea que diga si se ha usado IA (sí / no) y, si sí, para qué | 🟢 Mínimo | `dictamen.md` (apartado «Uso de IA») |
| **Subida a GitHub** | Los ficheros están en `sprint-02/` (no en la raíz del repositorio) y cada persona sube su autoevaluación con su cuenta | 🟢 Mínimo | Carpeta `sprint-02/` y su historial |
| **Paradoja de Simpson detectada** | En la afirmación 2, la carta 2 y la explicación de que la intermediaria cancela **más dentro de cada tarifa**, aunque en el total parezca menos | 🟡 Estándar | `dictamen.md` (afirmación 2) |
| **Tabla de la afirmación 2** | Una fila por tarifa y canal, con reservas, cancelaciones y tasa | 🟡 Estándar | `dictamen.md` (afirmación 2) |
| **Cada error con su carta** | La carta correcta en cada afirmación (solo valen las cartas 1 a 6), con la frase de la carta completada y un veredicto razonado | 🟡 Estándar | `dictamen.md` |
| **Lenguaje claro y recomendación** | Cada frase corregida se entiende sin jerga y cambia algo de la original (añade el límite); la recomendación sobre el canal ocupa tres líneas y trae una cautela | 🟡 Estándar | `dictamen.md` (frases corregidas y «Recomendación sobre el canal») |
| **IA responsable y uso de IA completo** | Una frase «Si entrenáramos un modelo con …, aprendería …, porque …»; el apartado «Uso de IA» dice **para qué** se usó la IA y **qué se comprobó a mano** (afirmaciones 2 y 6) | 🟡 Estándar | `dictamen.md` (apartados «IA responsable» y «Uso de IA») |
| **Revisión y autoevaluación** | Una persona que **no escribió ese dictamen** lo revisa con la rúbrica (justo debajo de estas tablas) y anota ✔, ✘ o — por afirmación, un nivel por criterio y una prueba en la **parte 2** de su propio `autoevaluacion_nombre.md`; cada persona rellena la **parte 1**; el equipo hace la review y la retro y actualiza el tablero | 🟡 Estándar | `autoevaluacion_nombre.md` en `sprint-02/` y el tablero |
| **Las seis afirmaciones** | Además de las cuatro, las otras dos de la 3 a la 6, o una razón de cuándo una diferencia sería real (por ejemplo, con una muestra pequeña) | 🔴 Extra | `dictamen.md` |
| **Hoja de cálculo adjunta** | `hoja_calculo.xlsx` con los datos, las tasas por fila y los dos totales por canal | 🔴 Extra | `sprint-02/` |
| **Recomendación con cautelas y datos a pedir** | La recomendación sobre el canal nombra las cautelas y los datos que habría que pedir antes de decidir; la frase de IA responsable propone una comprobación concreta antes de usar esos datos | 🔴 Extra | `dictamen.md` |

---

## 3 · 🧭 Rúbrica del reto · cómo se puntúa y cómo se revisa

La usan **dos veces**: el equipo, para revisar su propio trabajo antes de entregar (es lo que dice la *Definition of Done*), y el docente, para puntuar el sprint. Se mira **cada criterio por separado** y se pone el nivel de la columna cuyo texto **se cumple entero**: si lo de un nivel se cumple a medias, es el nivel de abajo. **0** significa que no se ha entregado nada de ese criterio.

Orientación: lo que pide el nivel 🟢 mínimo sale en un **2**, el 🟡 estándar en un **3** y los 🔴 extras en un **4**.

| Criterio | 1 · Empezado | 2 · Mínimo | 3 · Estándar | 4 · Extra |
|---|---|---|---|---|
| **Corrección técnica** (¿está bien hecho?) | Las cuentas de las afirmaciones 1 y 2 son erróneas, o no se ha detectado el problema de la 2 | Las tasas de las afirmaciones 1 y 2 están bien y hay un veredicto razonable en cuatro afirmaciones | Además se ve que la intermediaria cancela más **dentro de cada tarifa** (paradoja de Simpson) y cada error lleva su carta correcta | Además se resuelven las seis, o se razona cuándo una diferencia sería real (por ejemplo, por una muestra pequeña) |
| **Reproducibilidad** (¿lo puede repetir otra persona?) | No se ve de dónde salen las cifras | Las cifras llevan su operación (cancelaciones ÷ reservas) | Hay una tabla por tarifa y canal con reservas, cancelaciones y tasa | Además se adjunta la hoja de cálculo |
| **Análisis y comunicación al cliente** (¿lo entiende quien no programa?) | Solo dice «está mal» | Explica el error con la frase de la carta | Explica con lenguaje claro y propone una frase corregida en cada afirmación | Además la recomendación sobre el canal tiene cautelas y datos a pedir |
| **IA responsable** (¿se sabe qué hizo la IA y qué riesgos hay?) | No dice si se ha usado IA ni se considera el sesgo | Dice si se ha usado IA y menciona «cuidado con los sesgos» | Dice **para qué** se usó la IA y **qué se comprobó a mano**, y una frase explica qué aprendería un modelo entrenado con datos así | Además propone una comprobación concreta antes de usar esos datos |

**Cómo se revisa** (unos 15 minutos, en la revisión cruzada del paso 5; lo hace **una persona que no escribió ese dictamen**):

1. **Leer cada bloque** y marcar ✔, ✘ o — en la parte 2 de la hoja: ¿tiene carta, veredicto, frase corregida y cuenta (si la hay)?
2. **Rehacer una cuenta** con los datos (por ejemplo, la tasa del canal directo) y comprobar que la tabla de la afirmación 2 sale igual.
3. **Leer como si fuerais el cliente:** ¿se entiende cada frase corregida sin jerga? ¿La recomendación dice qué hacer y qué cautela tiene?
4. **Poner un nivel (1 a 4) en cada criterio, con una frase de prueba** (por ejemplo: «2 · la tabla de la afirmación 2 no tiene la tasa»; «3 · todas las frases corregidas se entienden, pero la 5 no dice qué datos faltan»). Sin prueba escrita, el nivel no vale.
5. **Apuntar el resultado** en la parte 2 de vuestro propio `autoevaluacion_nombre.md` y comentarlo de palabra con el equipo revisado. Lo que se pueda arreglar en el momento, que lo arregle su equipo; lo demás se anota como mejora.

Cada persona, además, se puntúa a sí misma en la parte 1 de su hoja de [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md) con **esta misma rúbrica**.
