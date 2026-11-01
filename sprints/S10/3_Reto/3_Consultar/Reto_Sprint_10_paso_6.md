# Paso 6 · Informe, revisión y entrega (día 2, 35 minutos)

<!--nav-->
> Sprint 10 · Reto «¿Vale la pena la red?» · paso 6 de 6 · [Ficha del reto](Reto_Sprint_10.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_10_una_pagina.md)
<!--/nav-->

1. Escribir el informe de 1 página, con la recomendación al principio.
2. Rellenar el README de `sprint-10/`.
3. Pedir a alguien que no escribió esa parte que revise con la rúbrica y anote el resultado al final del informe.
4. Subir los tres ficheros del equipo a `sprint-10/`, y cada persona su autoevaluación.

**Cómo se hace**
- **El informe** (`informe_comparativo.md`). Seis partes, en este orden:

| Parte | Qué escribís | De dónde sale |
|---|---|---|
| 1. Pregunta y respuesta | Una frase: «Recomendamos mantener / cambiar a… porque…» | Vuestra decisión del paso 5 |
| 2. Tabla de resultados | Media ± desviación de ambos enfoques (AUC, AP, F1) | Secciones 4 y 6 del cuaderno |
| 3. Curva comentada | Qué se ve y vuestra frase de diagnóstico | Paso 4 |
| 4. Coste | Tiempo, complejidad y explicabilidad | Paso 5 |
| 5. Riesgos de IA responsable | Al menos dos, específicos, con su medida (datos sintéticos; umbral y coste de los errores por *overbooking*; sesgos por país o canal) | Vuestra reflexión |
| 6. Límites | Qué no sabemos y qué haríamos después | Vuestra reflexión |

  Si queréis ver la curva en el informe, guardad la imagen del cuaderno como `curvas_aprendizaje.png` y subidla a `sprint-10/`. Añadid también una línea de **uso de la IA**: qué pedisteis y qué comprobasteis a mano.
- **El README.** Abrid `sprint-10/README.md` → lápiz ✏️ y completadlo: *Reto* («¿Vale la pena la red?»), *Qué se entrega* (el cuaderno y el informe), *Quién hizo qué* y *Cómo reproducirlo* («abrir en Colab y ejecutar de arriba abajo»).
- **La revisión con la rúbrica (5 minutos).** Quien revisa sigue los cinco pasos de «Cómo se revisa» de [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md) y añade al final del informe esta sección, con un nivel de 1 a 4 por criterio y **una frase de prueba**:

```
## Revisión con la rúbrica

Revisado por: (nombre) · Fecha: (dd/mm/aaaa)

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
|---|---|---|
| Corrección técnica | | |
| Reproducibilidad | | |
| Análisis y comunicación al cliente | | |
| IA responsable | | |

Lo primero que mejoraríamos: (una cosa concreta)
```

  Si hay tiempo, arreglad lo más fácil; lo demás queda como «lo primero que mejoraríamos». Si sobran minutos, empezad un extra (la variante de precio, o guardar el modelo y recargarlo).
- **Subir los ficheros (la vía del curso, desde el navegador).** Seguid [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md). Para el cuaderno: en Colab, *Entorno de ejecución → Reiniciar y ejecutar todo* y después *Archivo → Descargar → Descargar .ipynb* (renombradlo a `reto_vale_la_pena.ipynb`). En el repositorio del equipo: (1) **entrad primero en la carpeta `sprint-10`**; (2) *Add file → Upload files*; (3) arrastrad el fichero; (4) escribid un mensaje corto y pulsad **Commit changes**. El informe también se puede crear directamente con *Add file → Create new file*. Cada subida es un *commit* con el nombre de quien la hace, así que repartid: una persona sube el cuaderno, otra escribe el informe y otra rellena el README. El CSV va a `data/` solo si aún no está.

**Qué deberíais ver.** En la carpeta `sprint-10` del repositorio, el cuaderno con sus resultados visibles, el informe, el README relleno y una hoja de autoevaluación por persona (**3 + N**); y en el historial (el icono del reloj), *commits* de personas distintas.

**Hecho cuando:** otra persona podría repetir el cuaderno siguiendo solo el README, el informe termina con «Recomendamos… porque…» y trae la sección «Revisión con la rúbrica» rellena, y los ficheros están en `sprint-10/`.

**Después, en la entrega y la review:** cada persona rellena y sube su autoevaluación y coevaluación a `sprint-10/`, y el equipo enseña, en unos 5 minutos, la tabla comparativa, una curva de aprendizaje comentada y la recomendación en una frase, con el coste y los riesgos.

<!--nav-->
---

[← Paso 5](Reto_Sprint_10_paso_5.md) · [Ficha del reto: ayudas, errores frecuentes y qué hacer si os atascáis](Reto_Sprint_10.md)
<!--/nav-->
