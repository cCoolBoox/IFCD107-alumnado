# Paso 2 · Ajustar los gráficos con título-conclusión (día 1, 8 minutos)

<!--nav-->
> Sprint 13 · Reto «Informe visual para dirección» · paso 2 de 4 · [Ficha del reto](Reto_Sprint_13.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_13_una_pagina.md) · [Paso 3 →](Reto_Sprint_13_paso_3.md)
<!--/nav-->

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

<!--nav-->
---

[← Paso 1](Reto_Sprint_13_paso_1.md) · [Ficha del reto](Reto_Sprint_13.md) · [Paso 3 →](Reto_Sprint_13_paso_3.md)
<!--/nav-->
