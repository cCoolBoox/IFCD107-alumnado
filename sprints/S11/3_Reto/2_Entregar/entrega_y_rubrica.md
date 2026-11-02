# Sprint 11 · Reto «Visión artificial para el cliente» · Entrega y rúbrica

> **Qué se sube y cómo se evalúa.** Se lee **una vez**, antes de entregar, y se vuelve a la rúbrica cuando el equipo revisa su trabajo. Mientras trabajáis no hace falta: para eso está [el reto en una página](../1_Trabajar/Reto_Sprint_11_una_pagina.md).
>
> - Volver al [README del sprint](../../README.md) · [ficha del reto](../3_Consultar/Reto_Sprint_11.md), para consultar.
> - Vuestra hoja personal: [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md).
> - Cómo subir a GitHub paso a paso, con capturas: [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md).

Esta hoja responde a **dos preguntas distintas**, una tabla para cada una:

**Tabla A · Los ficheros:** qué ficheros hay, de dónde sale cada uno (ya hecho, lo modificáis, lo creáis o lo genera el cuaderno) y **cuáles se suben y adónde**.

**Tabla B · Los requisitos:** qué tiene que cumplir lo que entregáis y hasta dónde llegar (🟢 mínimo, 🟡 estándar, 🔴 extra). **Es lo que se evalúa.**

**En total, al final del sprint se suben a `sprint-11/`:** **3 ficheros del equipo** (`reto_vision_cliente.ipynb`, `analisis_errores.md`, `README.md`) **+ 1 autoevaluación y coevaluación por persona**, es decir, **3 + tantos ficheros como personas haya en el equipo** (un equipo de 3 sube 6). «El reto» no es un fichero aparte: son esos tres ficheros, y el **cuaderno contiene el modelo y el demostrador**. Las fotos (sintéticas o propias) **no se suben**: el cuaderno las vuelve a generar y, si usáis fotos propias, el README cuenta de dónde salen y con qué licencia. El modelo guardado (`.keras`) solo si lo guardáis. La *review* y la *retro* se hacen de palabra: no se suben.

## 1 · 📦 Tabla A · Los ficheros: de dónde sale cada uno y cuáles se suben

Todo lo que se sube va al repositorio privado del equipo (`ifcd107-equipo-…`), en la carpeta **`sprint-11/`**.

| Fichero | Origen | Qué hacéis vosotros | ¿Se sube? |
|---|---|---|---|
| `reto_vision_cliente.ipynb` | **Lo modificáis.** Parte del cuaderno `S11_04` (esqueleto con los ejercicios 1 a 5 y el demostrador) | Completar los ejercicios, entrenar y evaluar con vuestros datos, y ejecutarlo entero de arriba abajo. Al bajarlo de Colab, que conserve el nombre `reto_vision_cliente.ipynb` | **Sí** · `sprint-11/` |
| `analisis_errores.md` | **Lo creáis a partir de una plantilla.** Os damos `plantilla_analisis_errores.md` con los seis apartados | Escribir el informe de 1–2 páginas (métricas por clase, matriz de confusión, al menos 6 errores, recomendación). Si preferís PDF, se sube en lugar del `.md` | **Sí** · `sprint-11/` |
| `README.md` | **Lo modificáis.** Ya está creado en `sprint-11/` con la plantilla del repositorio del equipo; seguid las secciones del paso 5 | Cómo se ejecuta, de dónde salen las fotos, uso de la IA, quién hizo qué y la revisión con la rúbrica | **Sí** · `sprint-11/` |
| `clasificador_alojamientos.keras` | **Lo genera el cuaderno** con `modelo.save("clasificador_alojamientos.keras")` | Nada si no lo queréis: el cuaderno ya reproduce el modelo | Solo si lo guardáis · `sprint-11/` |
| Autoevaluación y coevaluación (`autoevaluacion_nombre.md`) | **Ya hecha, en blanco** | Cada persona copia la plantilla con su nombre y la rellena; la coevaluación va **dentro del mismo fichero** | **Sí**, **una por persona** (no una por equipo) · `sprint-11/` |
| Carpeta `datos_sinteticos/alojamientos/` (una subcarpeta por clase) | **Lo genera el cuaderno** (o `generar_dataset_sintetico.py`) la primera vez que lo ejecutáis | Nada: se crea sola y se puede borrar y volver a crear | **No se sube** |
| `generar_dataset_sintetico.py` | **Ya hecho.** Script del curso que crea las mismas fotos sintéticas | Nada: solo si queréis generarlas fuera de Colab | **No se sube** |
| Fotos propias (si las usáis) | **Las creáis vosotros** (fotos hechas por el equipo) o las bajáis con licencia abierta | Una carpeta por clase; apuntar autor y licencia; sin personas reconocibles | **No se suben**: autor y licencia van en el README |

---

## 2 · ✅ Tabla B · Los requisitos: qué tiene que cumplir y hasta dónde llegar

| Requisito | Qué se pide exactamente | Nivel | Dónde se comprueba |
|---|---|---|---|
| **Conjunto de fotos** | Una carpeta por clase, mínimo 30 fotos por clase (mejor 100 o más) y sin personas reconocibles. Se comprueba con `contar_por_clase` (ejercicio 1). El sintético del cuaderno vale | 🟢 Mínimo | `reto_vision_cliente.ipynb` · sección 1 |
| **Cuaderno ejecutable** | Se ejecuta de arriba abajo (*Entorno de ejecución → Reiniciar y ejecutar todo*) con la semilla fija (`SEMILLA = 42`) | 🟢 Mínimo | `reto_vision_cliente.ipynb` |
| **Modelo con *transfer learning*** | Red preentrenada **congelada** más una cabeza nueva con una neurona por clase (`modelo_transfer`, ejercicio 2) | 🟢 Mínimo | `reto_vision_cliente.ipynb` · sección 2 |
| **Métricas por clase y matriz de confusión** | Precisión y *recall* de cada clase (ejercicio 3), la matriz de confusión de la prueba y una frase que diga qué clases se confunden | 🟢 Mínimo | `reto_vision_cliente.ipynb` · sección 3 y `analisis_errores.md` |
| **Tres errores analizados** | Tres fotos mal clasificadas, cada una con una hipótesis de por qué | 🟢 Mínimo | `analisis_errores.md` |
| **Partición y prueba** | Entrenamiento, validación y prueba separados con la misma semilla; **la prueba se usa una sola vez** | 🟡 Estándar | `reto_vision_cliente.ipynb` |
| **Referencia «desde cero»** | La misma red sin preentrenar, entrenada con los mismos datos, para ver cuánto aporta el *transfer learning* | 🟡 Estándar | `reto_vision_cliente.ipynb` · `analisis_errores.md` |
| **Seis errores analizados** | Al menos 6 fotos mal clasificadas, cada una con la clase verdadera, la predicha, una hipótesis **que se vea en la foto** y una mejora | 🟡 Estándar | `analisis_errores.md` |
| **Demostrador** | `clasificar_foto(ruta)` devuelve clase, confianza y «revisar a mano» si la confianza es menor que el umbral | 🟡 Estándar | `reto_vision_cliente.ipynb` · sección 6 |
| **Datos y riesgos de IA responsable** | Origen y licencia de las fotos y al menos dos riesgos concretos (fotos poco representativas, clases poco frecuentes, etiquetas dudosas, privacidad, licencias) con una medida cada uno | 🟡 Estándar | `README.md` y `analisis_errores.md` |
| **Informe** | 1–2 páginas con los seis apartados del paso 5. En el mínimo, versión corta (matriz y tres errores) | 🟢 Mínimo | `analisis_errores.md` |
| **README** | Cómo se ejecuta, de dónde salen las fotos, uso de la IA (qué pedisteis y qué revisasteis) y quién hizo qué. En el mínimo, versión corta | 🟢 Mínimo | `README.md` |
| **Git** | Al menos 3 *commits* con mensaje claro, de personas distintas, sin claves ni datos personales | 🟢 Mínimo | Historial del repositorio del equipo |
| **Revisión y autoevaluación** | Alguien que **no escribió esa parte** revisa cuaderno, informe y README con la rúbrica (justo debajo de estas tablas) y anota nivel y prueba en el README; cada persona sube su hoja de autoevaluación y coevaluación | 🟡 Estándar | `README.md` (sección «Revisión con la rúbrica») y `sprint-11/` |
| **Umbral elegido con datos** | Probar varios umbrales y medir la **cobertura** (qué parte de las fotos decide el modelo solo) y el acierto de esas fotos; justificar el umbral elegido | 🔴 Extra | `analisis_errores.md` · `reto_vision_cliente.ipynb` |
| **Fotos reales con MobileNetV2** | La rama de Colab (sección 7 del cuaderno) con fotos reales con licencia, comparada con el modelo anterior | 🔴 Extra | `reto_vision_cliente.ipynb` · `README.md` |
| **Mejora probada** | Una mejora propuesta en el informe (más fotos de una clase, aumento de datos, revisar etiquetas…) que se prueba y se mide | 🔴 Extra | `analisis_errores.md` |

---

## 3 · 🧭 Rúbrica del reto · cómo se puntúa y cómo se revisa

La usan **dos veces**: el equipo, para revisar su propio trabajo antes de entregar (es lo que dice la *Definition of Done*), y el docente, para puntuar. Se mira **cada criterio por separado** y se pone el nivel de la columna cuyo texto **se cumple entero**: si lo de un nivel se cumple a medias, es el nivel de abajo. **0** significa que no se ha entregado nada de ese criterio.

Orientación: lo que pide el nivel 🟢 mínimo sale en un **2**, el 🟡 estándar en un **3** y los 🔴 extras en un **4**.

| Criterio | 1 · Empezado | 2 · Mínimo | 3 · Estándar | 4 · Extra |
|---|---|---|---|---|
| **Corrección técnica** (¿funciona?) | Hay cuaderno, pero no se ejecuta de arriba abajo o no hay un modelo con resultados | El cuaderno se ejecuta; las clases se han contado; hay un modelo con base congelada y cabeza nueva, y métricas por clase y matriz de confusión de la prueba | Además, partición fija con semilla y **prueba usada una sola vez**; la referencia «desde cero» se compara con los mismos datos; `clasificar_foto` devuelve clase, confianza y «revisar a mano» | Además, el umbral se elige midiendo cobertura y acierto en validación, o hay una segunda base (MobileNetV2) comparada con la primera |
| **Reproducibilidad** (¿lo puede repetir otra persona?) | Solo funciona en la sesión de Colab de quien lo hizo; no se sabe de dónde salen las fotos | El README dice cómo abrir el cuaderno, pero falta algo: el origen de las fotos, la semilla o el orden de ejecución | Otra persona, siguiendo solo el README y *Reiniciar y ejecutar todo*, obtiene las **mismas cifras**; hay 3 o más *commits* de personas distintas, sin claves ni datos personales | Además, el README indica las versiones (Python y TensorFlow), cómo conseguir las mismas carpetas de fotos y qué esperar al terminar |
| **Análisis y comunicación al cliente** (¿lo entiende quien no programa?) | Solo hay una cifra de acierto; no se dice en qué se equivoca | Las métricas por clase y la matriz dicen qué clases se confunden; hay 3 errores con una hipótesis cada uno | Al menos **6 errores** con foto, hipótesis que se ve en la imagen y mejora; la recomendación dice qué fotos se automatizan y cuáles se revisan a mano, con el umbral, sin jerga | Además, el umbral está justificado con números (cuántas fotos revisa una persona frente a cuántos fallos se evitan) y la mejora propuesta se ha probado |
| **IA responsable** (¿se sabe qué hizo la IA y qué riesgos hay?) | No dice si se ha usado IA ni de dónde vienen las fotos | Dice si se ha usado IA y de dónde vienen las fotos, sin riesgos concretos | Dice **qué se pidió a la IA, qué se revisó y qué se cambió**; da origen y licencia de las fotos y **dos riesgos concretos** con su medida | Además, cuenta un fallo concreto (por ejemplo, un error con confianza alta) y qué se hace con él, y avisa de que sintético no es lo mismo que fotos reales |

**Cómo se revisa** (unos 10 minutos, antes de subir; lo hace **una persona que no escribió esa parte**):

1. **Ejecutar** el cuaderno con *Entorno de ejecución → Reiniciar y ejecutar todo*, siguiendo solo lo que dice el README. Anotar si algo falla o si las cifras no coinciden con las del informe.
2. **Leer el informe y el README como si fuerais el cliente**: ¿se entiende en qué se equivoca el modelo y qué fotos debe revisar una persona? Subrayar lo que no se entienda.
3. **Mirar dos errores del informe** con la foto delante: ¿la hipótesis se ve de verdad en la imagen? Que quien la escribió la explique.
4. **Poner un nivel (1 a 4) en cada criterio, con una frase de prueba** (por ejemplo: «3 · el cuaderno se ejecuta y la referencia sale en la misma tabla, pero la prueba se usa dos veces»). Sin prueba escrita, el nivel no vale.
5. **Apuntar el resultado** en la sección «Revisión con la rúbrica» del `README.md` y corregir lo más fácil de arreglar. Lo demás se anota como mejora.

Cada persona, además, se puntúa a sí misma en su hoja de [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md) con **esta misma rúbrica**.
