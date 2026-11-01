# Paso 5 · Test una sola vez, explicación, revisión y entrega (día 3, 70 minutos)

<!--nav-->
> Sprint 15 · Reto «El mejor modelo, demostrado» · paso 5 de 5 · [Ficha del reto](Reto_Sprint_15.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_15_una_pagina.md)
<!--/nav-->

1. Evaluar el candidato en el test, una sola vez.
2. Guardar el modelo con `metadatos.json` y hacer la primera explicación.
3. Revisar con la rúbrica y anotar el resultado.
4. Subir los ficheros a `sprint-15/`.

**Cómo se hace**
- **Test, una vez (10 minutos).** Ejecutad **una sola vez** la evaluación del candidato en el test y copiad el resultado a la justificación. Si no os gusta, **no volváis a elegir con él**: anotadlo y explicadlo.
- **Guardar el modelo (10 minutos).** Guardad el candidato con `joblib.dump(modelo, "modelo_candidato.joblib")` (o el formato de la red) y escribid `metadatos.json` con versión de las bibliotecas, fecha, métrica en validación y en test, y nombres de las variables. En el brief 3, guardad el asistente tal como lo ejecutáis y apuntad en `metadatos.json` el modelo de lenguaje, los parámetros y el modo de recuperar los textos.
- **Primera explicación (20 minutos).** Importancia de variables, SHAP (si los datos son tabulares) o Grad-CAM (si son imágenes). Guardad el gráfico como `explicacion_modelo.png` y escribid 2–3 frases de lectura en la justificación («la variable más importante es …, lo que tiene sentido porque …»). Se profundiza en el Sprint 16.
- **La revisión con la rúbrica (10 minutos).** Quien revisa sigue los cinco pasos de «Cómo se revisa» de [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md) y añade al final de `justificacion_candidato.md` una sección como esta:

```
## Revisión con la rúbrica
**Revisado por:** <nombre> · **Fecha:** <dd/mm/aaaa>

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
|---|---|---|
| Corrección técnica | | |
| Reproducibilidad | | |
| Análisis y comunicación al cliente | | |
| IA responsable | | |

**Lo primero que mejoraríamos:** <una cosa concreta>
```

- **Subir los ficheros (la vía del curso, desde el navegador).** Seguid [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md): (1) abrid el repositorio del equipo y **entrad primero en la carpeta `sprint-15`**; (2) *Add file → Upload files*; (3) arrastrad los ficheros; (4) escribid un mensaje corto y pulsad **Commit changes**. Cada subida es un *commit* con el nombre de quien la hace. Un reparto posible: la persona A sube `03_modelos.ipynb` («Añado cuaderno de modelos»), la B sube `registro.csv` y `explicacion_modelo.png`, la C sube `justificacion_candidato.md`, `modelo_candidato.joblib` y `metadatos.json`. Los cuadernos de Colab se descargan con *Archivo → Descargar → .ipynb*. Los nombres de archivo, **en minúsculas y sin espacios**.

**Qué deberíais ver.** En la carpeta `sprint-15` del repositorio, los seis ficheros del equipo y una hoja de autoevaluación por persona (**6 + N**); y en el historial (el icono del reloj), al menos tres *commits* con nombres distintos.

**Hecho cuando:** el test se ha evaluado una vez, el modelo y su explicación están guardados, la sección «Revisión con la rúbrica» está rellena y todo está en `sprint-15/`.

**Después, 60 minutos de review y retro.** Cada persona sube su autoevaluación y coevaluación a `sprint-15/` (en el tiempo de entrega). En la *review*, cada equipo enseña en 5 minutos: (1) la tabla de modelos con media ± desviación, (2) el candidato elegido y **por qué** (no solo la métrica), (3) una fuga que evitó o detectó, (4) una hipótesis sobre por qué gana ese modelo y (5) su registro de experimentos. El resto de equipos pregunta: *«¿cómo sabéis que la diferencia no es ruido?»*

<!--nav-->
---

[← Paso 4](Reto_Sprint_15_paso_4.md) · [Ficha del reto: ayudas, errores frecuentes y qué hacer si os atascáis](Reto_Sprint_15.md)
<!--/nav-->
