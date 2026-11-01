# Paso 5 · *Model card*, README y entrega (día 2, 30 minutos)

<!--nav-->
> Sprint 8 · Reto «Duelo de modelos» · paso 5 de 5 · [Ficha del reto](Reto_Sprint_08.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_08_una_pagina.md)
<!--/nav-->

1. Copiar `model_card_plantilla.md` como `model_card.md` y rellenarla con vuestros datos.
2. Escribir el `README.md`.
3. Pedir a alguien que no escribió esa parte que revise con la rúbrica y anote el resultado en el README.
4. Subir los cuatro ficheros a `sprint-08/`.

**Cómo se hace**
- **La *model card*.** Descargad la [plantilla](../1_Trabajar/plantillas/model_card_plantilla.md) (en GitHub: *Raw*, copiar, y crear `model_card.md` con *Add file → Create new file*), o editadla en cualquier editor de texto. Debe caber en 1–2 páginas y cada apartado lleva **vuestros** datos (nada de dejar los ejemplos). Para el **nivel mínimo** bastan estos apartados, en pocas líneas:

| Apartado de la plantilla | Qué escribís |
|---|---|
| 1. Resumen | Qué predice el modelo, para qué decisión y quién lo usa |
| 2. Modelo campeón | Familia, hiperparámetros finales y versiones de las librerías |
| 3. Por qué este campeón | Vuestros pesos, el resultado del campeón, el mejor rival y las líneas del paso 4 |
| 5. Rendimiento | AUC en validación cruzada (± desviación) y **AUC de test (una sola evaluación)** |
| 6. Uso previsto y NO previsto | Para qué sirve y para qué **no** debe usarse (por ejemplo, no denegar reservas ni decidir sin revisión humana) |

  Para el **nivel estándar**, completad también 4 (datos y límites: son sintéticos), 7 (cómo se explica una predicción a un gerente), 8 (riesgos: el **país de origen** es una variable sensible; qué pasa con una falsa alarma), 9 (mantenimiento: qué mediríais en producción para detectar la **deriva**, cada cuánto se reentrena y quién se encarga) y 10 (cómo reproducirlo).
- **El README.** Tres cosas que no pueden faltar: **qué se entrega y quién hizo qué**; **cómo se reproduce** (abrir `reto_S08.ipynb` en Colab y *Reiniciar y ejecutar todo*; versiones de `scikit-learn`, `xgboost` y `lightgbm`; `SEMILLA = 42`; orden de ejecución); y **uso de IA** (qué pedisteis y qué revisasteis; los datos son sintéticos, sin datos personales). Para saber las versiones, en una celda del cuaderno: `import sklearn, xgboost, lightgbm` y mostrad `sklearn.__version__`, `xgboost.__version__` y `lightgbm.__version__`.
- **La revisión con la rúbrica (5 minutos).** Quien revisa sigue los cinco pasos de «Cómo se revisa» de [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md) y añade al final del README esta sección, con un nivel de 1 a 4 por criterio y **una frase de prueba**. Si hay tiempo, arreglad lo más fácil; lo demás queda como «lo primero que mejoraríamos».

```
## Revisión con la rúbrica
**Revisado por:** (nombre) · **Fecha:** (dd/mm/aaaa)

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
|---|---|---|
| Corrección técnica | | |
| Reproducibilidad | | |
| Análisis y comunicación al cliente | | |
| IA responsable | | |

**Lo primero que mejoraríamos:** (una cosa concreta)
```

- **Preparar los ficheros.** En Colab: *Entorno de ejecución → Reiniciar y ejecutar todo* (así queda con los resultados visibles y sabéis que funciona de arriba abajo), después *Archivo → Descargar → Descargar .ipynb*. Descargad `leaderboard_S08.csv` desde el panel de archivos (clic derecho → *Descargar*) **antes de cerrar Colab**: al cerrar la sesión se pierde. Ojo: al reiniciar y ejecutar todo, el cuaderno vuelve a crear el CSV desde cero, así que descargadlo después.
- **Subir los ficheros (la vía del curso, desde el navegador).** Seguid [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md): (1) abrid el repositorio del equipo y **entrad primero en la carpeta `sprint-08`**; (2) *Add file → Upload files*; (3) arrastrad los ficheros; (4) escribid un mensaje corto y pulsad **Commit changes**. Cada subida es un *commit* con el nombre de quien la hace. Un reparto posible: la persona A sube `reto_S08.ipynb` y `leaderboard_S08.csv`, la B sube `model_card.md` y la C sube `README.md`. Respetad los nombres tal como están en la tabla A (el reto fija `leaderboard_S08.csv` y `reto_S08.ipynb`, con la S mayúscula), sin espacios.

**Qué deberíais ver.** En la carpeta `sprint-08` del repositorio, los cuatro ficheros del equipo y una hoja de autoevaluación por persona (**4 + N**); y en el historial (el icono del reloj), *commits* con nombres distintos.

**Hecho cuando:** otra persona podría ejecutar el cuaderno siguiendo solo el README y obtendría el mismo campeón, la sección «Revisión con la rúbrica» está rellena y los cuatro ficheros están en `sprint-08/`.

**Después, 35 minutos de entrega, review y retro:** cada persona rellena y sube su autoevaluación y coevaluación a `sprint-08/`. En la *review* (5 minutos por equipo) enseñáis el leaderboard (la tabla o un gráfico), el campeón y **por qué no ganó otro**, y una frase sobre qué cambiaría la elección si el cliente valorara otra cosa. Preguntas de la retrospectiva: ¿nos sorprendió que un modelo sencillo compitiera con uno complejo? ¿Qué criterio pesó más en nuestra decisión? ¿Qué mediríamos en producción para saber que el modelo se degrada?

<!--nav-->
---

[← Paso 4](Reto_Sprint_08_paso_4.md) · [Ficha del reto: ayudas, errores frecuentes y qué hacer si os atascáis](Reto_Sprint_08.md)
<!--/nav-->
