# Paso 3 · Escribir titular, viñetas y pie (día 1, 8 minutos)

<!--nav-->
> Sprint 13 · Reto «Informe visual para dirección» · paso 3 de 4 · [Ficha del reto](Reto_Sprint_13.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_13_una_pagina.md) · [Paso 4 →](Reto_Sprint_13_paso_4.md)
<!--/nav-->

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

<!--nav-->
---

[← Paso 2](Reto_Sprint_13_paso_2.md) · [Ficha del reto](Reto_Sprint_13.md) · [Paso 4 →](Reto_Sprint_13_paso_4.md)
<!--/nav-->
