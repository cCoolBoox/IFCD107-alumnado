# Paso 5 · Informe, README y revisión con la rúbrica (día 2, 20 minutos)

<!--nav-->
> Sprint 6 · Reto «Datos sucios, cliente impaciente» · paso 5 de 5 · [Ficha del reto](Reto_Sprint_06.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_06_una_pagina.md)
<!--/nav-->

1. Completar `informe_calidad.md` a partir de la plantilla.
2. Rellenar el `README.md` y comprobar *Reiniciar y ejecutar todo*.
3. Pedir a alguien que no escribió esa parte que revise con la rúbrica y anote el resultado.

**Cómo se hace**
- **El informe** (1–2 páginas). Copiad la plantilla en `informe_calidad.md` y completad: resumen para el gerente (máximo 5 líneas), tabla de defectos, antes y después, *pipeline* y modelo de referencia, al menos 3 preguntas al cliente, IA responsable y cómo reproducirlo. **Para el nivel mínimo** bastan el resumen, la tabla de defectos (6 o más) y el antes y después; para el estándar, completad también el resto.
- **IA responsable.** Respondedlo con ejemplos del dataset: ¿qué pasa si el país de origen se imputa mal? ¿Podría el modelo discriminar por nacionalidad? ¿Hay columnas que no deberían usarse?
- **El README.** Cuatro cosas, en pocas líneas: qué hace el cuaderno; cómo ejecutarlo y en qué orden (*abrir en Colab y ejecutar de arriba abajo*); las versiones, que sacáis con `import sys, pandas, sklearn` y `print(sys.version, pandas.__version__, sklearn.__version__)`; y quién hizo qué y **qué le pedisteis a la IA y qué revisasteis**.
- **Reiniciar y ejecutar todo.** En Colab, *Entorno de ejecución → Reiniciar y ejecutar todo*. Si falla, hay celdas que dependen de un orden: arreglad antes de seguir.
- **La revisión con la rúbrica (5 minutos).** Quien revisa sigue los cinco pasos de «Cómo se revisa» de [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md) y rellena la sección «Revisión con la rúbrica» del final del informe: un nivel de 1 a 4 por criterio y **una frase de prueba**. Si hay tiempo, arreglad lo más fácil; lo demás queda como «lo primero que mejoraríamos». Si sobran minutos, empezad el extra.

**Qué deberíais ver.** `informe_calidad.md` con todos los apartados rellenos y la sección «Revisión con la rúbrica» completa, un `README.md` con los comandos y las versiones, y el cuaderno ejecutándose de arriba abajo sin errores.

**Hecho cuando:** otra persona podría repetir el cuaderno siguiendo solo el README, y el informe tiene anotados el nivel y la prueba de cada criterio.

**Después, 35 minutos de entrega, review y retro** (también el día 2): subid los ficheros a `sprint-06/` siguiendo [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md), cada persona con su cuenta. Descargad el cuaderno con *Archivo → Descargar → Descargar .ipynb* (después de *Reiniciar y ejecutar todo*) y subidlo. Los nombres de archivo, **en minúsculas y sin espacios**; el CSV va a `data/` solo si aún no está. Un reparto posible: la persona A sube `informe_calidad.md` («Añado informe de calidad»), la B sube `reto_S06.ipynb` («Añado cuaderno»), la C actualiza `README.md` («Completo el README»). Después, cada persona rellena y sube su autoevaluación y coevaluación. En la *review* (5 minutos por equipo) enseñad: la tabla de defectos (los 3 más graves y por qué), el cuaderno corriendo desde cero y la métrica del *baseline* frente al modelo tonto. Para la retro, pensad: ¿qué defecto nos costó más encontrar? ¿Qué decisión de limpieza discutimos más? ¿Qué haríamos distinto con el siguiente fichero del cliente?

<!--nav-->
---

[← Paso 4](Reto_Sprint_06_paso_4.md) · [Ficha del reto: ayudas, errores frecuentes y qué hacer si os atascáis](Reto_Sprint_06.md)
<!--/nav-->
