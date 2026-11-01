# Sprint 9 · Reto «Conocer al huésped» · Entrega y rúbrica

> **Qué se sube y cómo se evalúa.** Se lee **una vez**, antes de entregar, y se vuelve a la rúbrica cuando el equipo revisa su trabajo. Mientras trabajáis no hace falta: para eso está [el reto en una página](../1_Trabajar/Reto_Sprint_09_una_pagina.md).
>
> - Volver al [README del sprint](../../README.md) · [ficha del reto](../3_Consultar/Reto_Sprint_09.md), para consultar.
> - Vuestra hoja personal: [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md).
> - Cómo subir a GitHub paso a paso, con capturas: [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md).

Esta hoja responde a **dos preguntas distintas**, una tabla para cada una:

**Tabla A · Los ficheros:** qué ficheros hay, de dónde sale cada uno (ya hecho, lo modificáis, lo creáis o lo genera el cuaderno) y **cuáles se suben y adónde**.

**Tabla B · Los requisitos:** qué tiene que cumplir lo que entregáis y hasta dónde llegar (🟢 mínimo, 🟡 estándar, 🔴 extra). **Es lo que se evalúa.**

**En total, al final del sprint se suben a `sprint-09/`:** **2 ficheros del equipo** (`reto_S09_conocer_al_huesped.ipynb`, `ficha_segmentos.md`) **+ 1 autoevaluación y coevaluación por persona**, es decir, **2 + tantos ficheros como personas haya en el equipo** (un equipo de 3 sube 5). «El reto» no es un fichero aparte: son esos dos ficheros. La **nota de IA responsable** (5 líneas) y la **revisión con la rúbrica** van **dentro de la ficha**, no en ficheros distintos. Los datos no se suben: ya están en el repositorio del curso y el cuaderno los descarga solo. La imagen del mapa solo se sube si la ponéis en la ficha. La *review* y la *retro* se hacen de palabra: no se suben.

## 1 · 📦 Tabla A · Los ficheros: de dónde sale cada uno y cuáles se suben

Todo lo que se sube va al repositorio privado del equipo (`ifcd107-equipo-…`), en la carpeta **`sprint-09/`**.

| Fichero | Origen | Qué hacéis vosotros | ¿Se sube? |
|---|---|---|---|
| `reto_S09_conocer_al_huesped.ipynb` | **Lo creáis.** Cuaderno nuevo en Colab; podéis reutilizar el código de `S09_01`, `S09_02` y `S09_03` | Segmentación, mapa PCA y recomendador, con semillas fijas y el uso de IA declarado | **Sí** · `sprint-09/` |
| `ficha_segmentos.md` | **Lo creáis a partir de una plantilla.** Os damos `plantilla_ficha_segmentos.md` con huecos | Copiarla como `ficha_segmentos.md` y rellenarla: segmentos, recomendador, nota de IA responsable y revisión con la rúbrica | **Sí** · `sprint-09/` |
| `mapa_pca.png` | **Lo genera el cuaderno** al guardar la figura del mapa (por ejemplo con `plt.savefig("mapa_pca.png")`) | Descargarla del panel de archivos de Colab y enlazarla desde la ficha | Solo si ponéis el mapa en la ficha · `sprint-09/` |
| Autoevaluación y coevaluación (`autoevaluacion_nombre.md`) | **Ya hecha, en blanco** | Cada persona copia la plantilla con su nombre y la rellena; la coevaluación va **dentro del mismo fichero** | **Sí**, **una por persona** (no una por equipo) · `sprint-09/` |
| `huespedes.csv` | **Ya hecho.** Los datos de 1.200 huéspedes (sintéticos) | Nada: el cuaderno los descarga con la celda «Preparación» | **No**: ya están en `datos/` del repositorio del curso |
| `valoraciones_experiencias.csv` y `experiencias.csv` | **Ya hechos.** Valoraciones y catálogo de 25 experiencias | Nada: los descarga la misma celda | **No**: ya están en `datos/` del repositorio del curso |

---

## 2 · ✅ Tabla B · Los requisitos: qué tiene que cumplir y hasta dónde llegar

| Requisito | Qué se pide exactamente | Nivel | Dónde se comprueba |
|---|---|---|---|
| **Escalar antes de agrupar** | Las 7 variables numéricas de `huespedes.csv` (sin `id_huesped`) se escalan antes de aplicar el clustering | 🟢 Mínimo | Cuaderno |
| **Elegir k** | k-means con varios `k` (de 2 a 8), curva de la silueta y **una frase con las dos razones** del `k` elegido: la técnica (silueta) y la de negocio (¿puede Lucía actuar con ese número de grupos?) | 🟢 Mínimo | Cuaderno y cabecera de la ficha |
| **Mapa 2D con PCA** | Los huéspedes en 2 componentes, coloreados por segmento, con el **% de varianza** en cada eje y un título que enuncia una conclusión | 🟢 Mínimo | Cuaderno y ficha |
| **Ficha de segmentos** | Por segmento: nombre comercial, tamaño (n y %), perfil en una frase **con cifras** y **una acción comercial**. Los tamaños suman 1.200 | 🟢 Mínimo | `ficha_segmentos.md` |
| **Nota de IA responsable** | 5 líneas dentro de la ficha sobre los riesgos de segmentar y recomendar | 🟢 Mínimo | `ficha_segmentos.md` |
| **Declarar el uso de la IA** | En el cuaderno, dónde la habéis usado y qué habéis comprobado a mano | 🟢 Mínimo | Cuaderno |
| **Recomendador comparado** | Al menos **dos métodos** (la popularidad y otro), evaluados con valoraciones **escondidas** (división de prueba) con **RMSE** y **precision@3**, y una frase que explica cuál elegís | 🟡 Estándar | Cuaderno y apartado «Recomendador» de la ficha |
| **Función `recomendar(id_usuario, n)`** | Devuelve las `n` mejores experiencias que el usuario **aún no ha valorado**; probada con 3 usuarios distintos | 🟡 Estándar | Cuaderno |
| **Experiencia estrella** | Por segmento, la experiencia que recomienda vuestro prototipo | 🟡 Estándar | `ficha_segmentos.md` |
| **IA responsable con riesgos concretos** | Al menos **2 riesgos específicos** de este caso (por ejemplo, sesgo de popularidad, discriminación por edad o niños, privacidad), cada uno con su medida | 🟡 Estándar | `ficha_segmentos.md` |
| **Cuaderno reproducible** | «Reiniciar y ejecutar todo» funciona sin errores y con semillas fijas | 🟡 Estándar | Cuaderno |
| **Git** | Cada persona del equipo sube su parte, con un mensaje claro, sin claves ni datos personales | 🟡 Estándar | Historial del repositorio del equipo |
| **Revisión y autoevaluación** | Alguien que **no escribió esa parte** revisa cuaderno y ficha con la rúbrica (justo debajo de estas tablas) y anota nivel y prueba en la ficha; cada persona sube su hoja de autoevaluación y coevaluación | 🟡 Estándar | `ficha_segmentos.md` (sección «Revisión con la rúbrica») y `sprint-09/` |
| **Extras** | Comparar k-means con clustering jerárquico o DBSCAN y explicar la diferencia · interpretar los ejes del PCA con las cargas · recomendar a un huésped nuevo sin historial | 🔴 Extra | Cuaderno y ficha |

---

## 3 · 🧭 Rúbrica del reto · cómo se puntúa y cómo se revisa

La usan **dos veces**: el equipo, para revisar su propio trabajo antes de entregar (es lo que dice la *Definition of Done*), y el docente, para puntuar. Se mira **cada criterio por separado** y se pone el nivel de la columna cuyo texto **se cumple entero**: si lo de un nivel se cumple a medias, es el nivel de abajo. **0** significa que no se ha entregado nada de ese criterio.

Orientación: lo que pide el nivel 🟢 mínimo sale en un **2**, el 🟡 estándar en un **3** y los 🔴 extras en un **4**.

| Criterio | 1 · Empezado | 2 · Mínimo | 3 · Estándar | 4 · Extra |
|---|---|---|---|---|
| **Corrección técnica** (¿funciona?) | Hay código, pero se agrupa sin escalar, el `k` se elige sin mirar la silueta o el cuaderno da errores | Las variables están escaladas, hay curva de silueta para varios `k` y un mapa PCA con los segmentos coloreados | Además, el recomendador se evalúa con valoraciones escondidas (RMSE y precision@3) frente a la popularidad, y `recomendar` no propone nada ya valorado en 3 usuarios de prueba | Además, compara k-means con jerárquico o DBSCAN con resultados razonados, o recomienda a un huésped nuevo sin historial |
| **Reproducibilidad** (¿lo puede repetir otra persona?) | Solo funciona en la sesión de Colab de quien lo escribió, con celdas ejecutadas en desorden | Se ejecuta de arriba abajo, pero con ayuda del equipo o sin semillas fijas | Otra persona hace *Reiniciar y ejecutar todo* y obtiene **el mismo `k`, los mismos tamaños y la misma tabla de RMSE y precision@3**; cada persona ha subido su parte, sin claves ni datos personales | Además, el cuaderno empieza con una celda de texto que explica cómo ejecutarlo y con las versiones de Python y de las bibliotecas |
| **Análisis y comunicación al cliente** (¿lo entiende quien no programa?) | Solo hay cifras o gráficos, sin interpretar y sin nombres de segmento | La ficha tiene nombre, tamaño, perfil y **una acción comercial** por segmento | Además, cada nombre se apoya en **dos cifras** del perfil, los tamaños suman 1.200, hay una experiencia estrella por segmento y la frase del `k` da la razón técnica y la de negocio | Además, prioriza los segmentos por valor, explica los límites (datos sintéticos, lo que el 2D no recoge) y dice qué haría con un huésped nuevo |
| **IA responsable** (¿se sabe qué hizo la IA y qué comprobasteis?) | No hay nota, o no dice si se ha usado IA | Hay nota de 5 líneas con riesgos genéricos y se dice que se ha usado IA | Al menos **2 riesgos específicos** de este caso, cada uno con su medida, y se dice **qué se pidió a la IA y qué se comprobó** | Además, comprueba una medida con los datos (por ejemplo, que el recomendador no repite siempre las mismas experiencias) y explica el arranque en frío |

**Cómo se revisa** (unos 10 minutos, antes de subir; lo hace **una persona que no escribió esa parte**):

1. **Ejecutar** el cuaderno en Colab con *Entorno de ejecución → Reiniciar y ejecutar todo*. Anotar si algo falla y si salen los mismos `k`, tamaños y tabla de RMSE y precision@3 que cuenta la ficha.
2. **Leer la ficha como si fuera Lucía**: ¿se entiende qué es cada segmento y qué hacer con él? ¿Los tamaños suman 1.200? Subrayar lo que no se entienda.
3. **Mirar el cuaderno**: ¿se escala antes de agrupar? ¿Se evalúa el recomendador con valoraciones escondidas? ¿`recomendar` no devuelve nada ya valorado? ¿Está dicho dónde se ha usado la IA? Que quien lo escribió explique cualquier celda.
4. **Poner un nivel (1 a 4) en cada criterio, con una frase de prueba** (por ejemplo: «3 · el cuaderno se ejecuta entero y salen k = 4 y los mismos tamaños, pero falta probar `recomendar` con un tercer usuario»). Sin prueba escrita, el nivel no vale.
5. **Apuntar el resultado** en la sección «Revisión con la rúbrica» del final de `ficha_segmentos.md` y corregir lo más fácil de arreglar. Lo demás se anota como mejora.

Cada persona, además, se puntúa a sí misma en su hoja de [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md) con **esta misma rúbrica**.
