# Paso 3 · Mapa PCA e interpretación de los segmentos (día 1, 15 minutos)

<!--nav-->
> Sprint 9 · Reto «Conocer al huésped» · paso 3 de 5 · [Ficha del reto](Reto_Sprint_09.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_09_una_pagina.md) · [Paso 4 →](Reto_Sprint_09_paso_4.md)
<!--/nav-->

1. Dibujar el mapa 2D con PCA, con los segmentos coloreados.
2. Calcular el perfil medio de cada segmento y su tamaño.
3. Ponerle nombre a cada segmento, con cifras.
4. Proponer una acción comercial por segmento.

**Cómo se hace**
- **El mapa.** Entrenad `k-means` con el `k` elegido y guardad el grupo de cada huésped. Aplicad `PCA(n_components=2)` sobre `X` y dibujad un diagrama de dispersión coloreado por grupo (es el ejercicio 2 de `S09_02`). Los ejes llevan el **% de varianza** de cada componente (`explained_variance_ratio_`) y el título dice una **conclusión** («Cuatro tipos de huésped bastante separados»). Con 2 componentes se conserva solo una parte de la información (en `S09_02` salía cerca del 69 %): si el mapa sale mezclado, decidlo en la ficha.
- **El perfil.** Con `groupby` calculad la media de cada variable por grupo y el número de huéspedes. Comparad cada media con la media general; el mapa de calor de `S09_01` ayuda.
- **El nombre.** Cada nombre se apoya en **dos cifras** del perfil. Ejemplo de la plantilla: «Familias de larga estancia · 410 (34 %) · 9 de cada 10 viajan con niños, reservan con 110 días de antelación y gastan poco en actividades». Los tamaños de todos los segmentos suman 1.200.
- **La acción comercial.** Una por segmento: qué enseñar, cuándo y por qué canal. La IA puede sugerir nombres, pero el nombre tiene que reflejar vuestras cifras.

**Qué deberíais ver.** Un mapa con un color por segmento y el % de varianza en los ejes, y una tabla con el perfil medio de cada segmento: nombre, tamaño, dos o tres cifras y una acción.

**Hecho cuando:** el mapa está dibujado y cada segmento tiene nombre, tamaño, perfil con cifras y una acción.

<!--nav-->
---

[← Paso 2](Reto_Sprint_09_paso_2.md) · [Ficha del reto](Reto_Sprint_09.md) · [Paso 4 →](Reto_Sprint_09_paso_4.md)
<!--/nav-->
