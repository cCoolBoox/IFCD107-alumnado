# Paso 5 · Ficha, IA responsable, revisión y entrega (día 2, 30 minutos)

<!--nav-->
> Sprint 9 · Reto «Conocer al huésped» · paso 5 de 5 · [Ficha del reto](Reto_Sprint_09.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_09_una_pagina.md)
<!--/nav-->

1. Rellenar la ficha de segmentos y la nota de IA responsable.
2. Pedir a alguien que no escribió esa parte que revise con la rúbrica y anote el resultado en la ficha.
3. Dejar el cuaderno ejecutable y subir los ficheros a `sprint-09/`.
4. Ensayar 3 minutos de review.

**Cómo se hace**
- **La ficha.** Copiad el texto de `plantilla_ficha_segmentos.md` en un archivo nuevo `ficha_segmentos.md` y rellenad cada sección:

| Sección de la plantilla | Qué escribís |
|---|---|
| Cabecera | Equipo, método, `k`, silueta y la frase de las dos razones del paso 2 |
| Mapa de segmentos | La imagen del mapa (`mapa_pca.png`, subida junto a la ficha) o dónde está en el cuaderno |
| Segmentos | Una fila por segmento: nombre, tamaño, perfil con cifras, acción y **experiencia estrella** (la que recomienda vuestro prototipo a ese grupo; **ojo:** los datos son sintéticos y las 300 personas de las valoraciones **no son** las de `huespedes.csv`, así que no hay un cruce real entre ambos ficheros: elegid la experiencia razonando con el perfil del segmento y apoyadla en lo que recomienda vuestro prototipo, y anotad esa decisión como supuesto) |
| Recomendador | Los dos métodos con su RMSE y precision@3, el elegido y un ejemplo con un usuario; qué haría el sistema con un huésped nuevo sin valoraciones |
| IA responsable | Cinco líneas con **al menos 2 riesgos específicos** de este caso, cada uno con su medida (ejemplos justo debajo de la tabla) |
| Limitaciones | Datos sintéticos, comportamiento de un año, pocas valoraciones por persona, y las vuestras |

- **Nota de IA responsable.** Ejemplos, para que elijáis los que valen para **vuestro** caso: *discriminar* (si se usan la edad o «viaja con niños» para fijar precios; medida: usar la segmentación para comunicar, no para variar precios); *sesgo de popularidad* (las experiencias poco conocidas casi no se recomiendan; medida: reservar un hueco a opciones menos populares); *privacidad* (se combinan datos de reserva y valoraciones; medida: usar identificadores y no mostrar datos personales).
- **Declarar la IA.** En el cuaderno, una celda de texto que diga dónde la habéis usado y qué habéis comprobado a mano.
- **La revisión con la rúbrica (10 minutos).** Quien revisa sigue los cinco pasos de «Cómo se revisa» de [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md) y rellena la sección «Revisión con la rúbrica» del final de `ficha_segmentos.md`: un nivel de 1 a 4 por criterio y **una frase de prueba**. Si hay tiempo, arreglad lo más fácil; lo demás queda como «lo primero que mejoraríamos». Si sobran minutos, empezad algún extra.
- **Subir los ficheros (la vía del curso, desde el navegador).** Seguid [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md). (1) En Colab, *Entorno de ejecución → Reiniciar y ejecutar todo* y después *Archivo → Descargar → Descargar .ipynb*. (2) Abrid el repositorio del equipo y **entrad primero en la carpeta `sprint-09`**. (3) *Add file → Upload files*, arrastrad los ficheros, escribid un mensaje corto y pulsad **Commit changes**. Cada subida es un *commit* con el nombre de quien la hace. Un reparto posible: la persona A sube el cuaderno («Añado segmentación y recomendador»), la B sube la ficha y el mapa («Añado ficha de segmentos»), y cada persona sube su autoevaluación. Nombres de archivo **sin espacios ni tildes**.

**Qué deberíais ver.** En la carpeta `sprint-09` del repositorio, el cuaderno y la ficha del equipo (y el mapa, si lo habéis puesto) y una hoja de autoevaluación por persona (**2 + N**); y en el historial (el icono del reloj), *commits* de todas las personas del equipo.

**Hecho cuando:** otra persona podría repetir el cuaderno de arriba abajo, la sección «Revisión con la rúbrica» está rellena y cada persona ha subido algo con su cuenta.

**Después, 40 minutos de entrega, review y retrospectiva:** cada persona rellena y sube su autoevaluación y coevaluación a `sprint-09/`, y el equipo presenta en 3 minutos **sus segmentos (nombre y acción)** y **una recomendación concreta para un usuario**. Se comparan los `k` elegidos y se discute: *¿es el mismo cliente aunque le pongamos otro nombre?*

<!--nav-->
---

[← Paso 4](Reto_Sprint_09_paso_4.md) · [Ficha del reto: ayudas, errores frecuentes y qué hacer si os atascáis](Reto_Sprint_09.md)
<!--/nav-->
