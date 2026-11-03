# Paso 5 · *Model card*, README y entrega (día 2, 30 minutos)

<!--nav-->
> Sprint 8 · Reto «Duelo de modelos» · paso 5 de 5 · [Ficha del reto](Reto_Sprint_08.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_08_una_pagina.md)
<!--/nav-->

1. Copiar `model_card_plantilla.md` como `model_card.md` y rellenarla con vuestros datos.
2. Escribir el `README.md`.
3. Pedir a alguien que no escribió esa parte que revise con la rúbrica y anote el resultado en el README.
4. Subir los cuatro ficheros a `sprint-08/`.

**En sencillo.** El trabajo técnico ya está hecho; ahora hay que **dejarlo listo para que lo use otra persona**. Pensad en un electrodoméstico: dentro de la caja va la **ficha técnica** (la *model card*: qué hace, cómo rinde, para qué no sirve) y el **manual de instrucciones** (el README: qué hay en la caja, quién lo montó y cómo ponerlo en marcha). Después, alguien del equipo que no lo escribió lo revisa con una lista de comprobación (la rúbrica), con ojos frescos. Casi no hay código: se escribe **texto** con **vuestros números**, copiados del cuaderno. No hace falta saber Markdown: la plantilla ya trae los títulos (`#`) y las tablas (`|`); solo hay que rellenar lo que falta sin borrar esas marcas. Lo único nuevo en el cuaderno son tres líneas para apuntar las versiones de las librerías.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| ***Model card*** | La ficha del modelo campeón, de 1–2 páginas, para el cliente y para quien lo mantenga. |
| **README** | El «léeme» de la carpeta: qué se entrega, quién hizo qué y cómo repetirlo. Es lo primero que lee el docente. |
| **Markdown (`.md`)** | Texto normal con marcas sencillas: `#` para un título, `-` para una lista y barras verticales para separar las columnas de una tabla. |
| **Versión** | El número de edición de una librería (por ejemplo, `1.9.1`). Con otra versión, un resultado puede cambiar un poco. |
| **Reproducir** | Que otra persona repita el trabajo con el README y obtenga lo mismo: el mismo leaderboard y el mismo campeón. |
| **Deriva** | Cuando, con el tiempo, las reservas nuevas dejan de parecerse a las de entrenamiento y el modelo acierta menos. |
| **Falsa alarma** | Avisar de que una reserva se cancelará cuando no iba a hacerlo. |
| **Rúbrica** | La tabla con que se evalúa el reto: cuatro criterios, cada uno de 1 a 4. |
| ***Commit*** | Guardar en GitHub un cambio con un mensaje corto y vuestro nombre. Sin pulsar **Commit changes** no se guarda nada. |

**Cómo se hace**

1. **Dejar el cuaderno definitivo y descargar dos ficheros.** Hacedlo primero: así los números que copiéis a la *model card* son los finales. Debajo de la última celda pulsad **+ Código** y escribid:

    ```python
    import sklearn, xgboost, lightgbm
    print("scikit-learn", sklearn.__version__)
    print("xgboost", xgboost.__version__)
    print("lightgbm", lightgbm.__version__)
    ```

    Qué hace cada línea:

    - `import sklearn, xgboost, lightgbm`: carga las tres librerías (el cuaderno ya las usaba; volver a cargarlas no hace daño).
    - `print("scikit-learn", sklearn.__version__)`: escribe el nombre y su versión. `__version__` lleva **dos** guiones bajos a cada lado. Las otras dos líneas hacen lo mismo con `xgboost` y `lightgbm`.

    Después, *Entorno de ejecución → Reiniciar y ejecutar todo* (y confirmad). Mirad hasta el final: ninguna celda debe dar error en rojo y la última debe escribir tres líneas del estilo `scikit-learn 1.9.1` (vuestros números dependen de Colab: apuntadlos). Por último, *Archivo → Descargar → Descargar .ipynb* y, en el panel de archivos de la izquierda (icono de carpeta), clic derecho sobre `leaderboard_S08.csv` → *Descargar*. Hacedlo **antes de cerrar Colab**: al cerrar, el CSV se pierde.

2. **Rellenar la *model card*.** Abrid la [plantilla](../1_Trabajar/plantillas/model_card_plantilla.md) y cread `model_card.md` con vuestros datos: o bien en GitHub (en la plantilla, **Raw**, `Ctrl + A`, `Ctrl + C`; después, dentro de `sprint-08`, **Add file → Create new file**, nombre `model_card.md`, pegad y completad), o bien en un editor de texto. Cada apartado lleva **vuestros** datos: no dejéis los ejemplos ni los `…`. Para el **nivel mínimo** bastan estos apartados, en pocas líneas (la última columna es un ejemplo con los números de una ejecución real; los vuestros serán otros):

    | Apartado | Qué escribís | Ejemplo |
    |---|---|---|
    | 1. Resumen | Qué predice el modelo, para qué decisión y quién lo usa | «Calcula la probabilidad de que una reserva se cancele, para avisar al gerente de TurisData.» |
    | 2. Modelo campeón | Familia, hiperparámetros finales y versiones | «Regresión logística (familia lineal), `max_iter=1000`, variables escaladas. scikit-learn 1.9.1.» |
    | 3. Por qué este campeón | Vuestros pesos, el resultado del campeón, el mejor rival y las líneas del paso 4 | «Pesos 50 / 30 / 20. `logistica`: AUC 0,755 ± 0,014, explicabilidad 4. Mejor rival, `arbol_podado`: pierde 0,035 de AUC, pero se explica mejor (5).» |
    | 5. Rendimiento | AUC en validación cruzada (± desviación) y **AUC de test (una sola evaluación)** | «Validación cruzada 0,755 ± 0,014; test 0,762.» |
    | 6. Uso previsto y NO previsto | Para qué sirve y para qué **no** debe usarse | «No usar para denegar reservas ni para decidir sin revisión humana.» |

    Para el **nivel estándar**, completad también estos cinco (el apartado 3 lleva además vuestra tabla de sensibilidad del paso 4):

    | Apartado | Qué escribís | Ejemplo |
    |---|---|---|
    | 4. Datos | Fuente, número de reservas, tasa de cancelación, variables usadas y excluidas, límites | «6000 reservas sintéticas hechas en 2024–2025, 45,9 % canceladas; 15 variables; `id_reserva` y las fechas no se usan (solo la temporada de llegada). Son datos sintéticos.» |
    | 7. Explicabilidad | Cómo se explica una predicción a un gerente | «Pesan sobre todo el depósito, la antelación, el canal y la tarifa.» (Con la logística, mirad sus coeficientes como en `S07_03`; con un árbol, sus reglas; con *boosting* o SVM, decid que es caja negra.) |
    | 8. Riesgos | El **país de origen** como variable sensible y qué pasa con una falsa alarma | «La tasa de cancelación por país va del 44 % al 47,5 %: diferencia pequeña, pero el país no debe usarse para tratar distinto a nadie.» |
    | 9. Mantenimiento | Qué mediríais en producción para ver la **deriva**, cada cuánto se reentrena y quién se encarga | «Comparar cada mes la tasa de cancelación real con la prevista; reentrenar si…; responsable: …» |
    | 10. Cómo reproducirlo | Semilla, versiones, orden de ejecución y ficheros | «`SEMILLA = 42`; versiones del paso 1; orden del cuaderno de arriba abajo.» |

3. **Escribir el README.** Ya existe `sprint-08/README.md` en el repositorio del equipo, con la plantilla de cuatro campos: abridlo (icono del lápiz) y sustituid su contenido por este guion, cambiando los `…`. Tres cosas no pueden faltar: **qué se entrega y quién hizo qué**, **cómo se reproduce** (con versiones, `SEMILLA = 42` y orden de ejecución) y **uso de IA** (qué pedisteis y qué revisasteis):

    ```text
    # Sprint 8 · Duelo de modelos · Equipo …

    ## Qué se entrega
    - `reto_S08.ipynb`: el cuaderno, ejecutado de arriba abajo.
    - `leaderboard_S08.csv`: la tabla de modelos.
    - `model_card.md`: la ficha del modelo campeón.
    - `README.md`: este fichero.

    ## Quién hizo qué
    - … (nombre): …

    ## Cómo se reproduce
    1. Abrir `reto_S08.ipynb` en Google Colab.
    2. Entorno de ejecución → Reiniciar y ejecutar todo (tarda … minutos).
    3. Debe salir el mismo leaderboard y el mismo campeón: ….
    Versiones: scikit-learn …, xgboost …, lightgbm …. Semilla: SEMILLA = 42.

    ## Uso de IA
    Le pedimos …; lo revisamos …; cambiamos …. Los datos son sintéticos: no hay datos personales.
    ```

4. **La revisión con la rúbrica (5–10 minutos).** La hace **una persona que no escribió esa parte**. Sigue los cinco pasos de «Cómo se revisa» de [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md): ejecutar el cuaderno solo con el README, contar modelos, familias y filas con `auc_test` en el CSV, leer la *model card* como si fuera el gerente, poner un nivel de 1 a 4 en cada criterio **con una frase de prueba** (por ejemplo, «3 · 7 modelos, 5 familias y `auc_test` en una sola fila») y apuntar el resultado. Sin frase de prueba, el nivel no vale. Pegad esto al final del README y rellenadlo:

    ```text
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

    Si hay tiempo, arreglad lo más fácil; lo demás queda como «lo primero que mejoraríamos».

5. **Subir los cuatro ficheros (la vía del curso, desde el navegador).** Seguid [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md): (1) abrid el repositorio del equipo y **entrad primero en la carpeta `sprint-08`**; (2) *Add file → Upload files*; (3) arrastrad los ficheros; (4) escribid un mensaje corto («Subo la model card del duelo de modelos»; no valen «cambios» ni «asdf») y pulsad **Commit changes**. Cada subida es un *commit* con el nombre de quien la hace: un reparto posible es que A suba `reto_S08.ipynb` y `leaderboard_S08.csv`, B suba `model_card.md` y C suba `README.md`. Respetad los nombres tal cual, con la S mayúscula y sin espacios. Nada de claves ni datos personales.

**Qué deberíais ver.** En la carpeta `sprint-08` del repositorio, los cuatro ficheros del equipo y una hoja de autoevaluación por persona (**4 + N**); y en el historial (el icono del reloj), *commits* con nombres distintos.

**Hecho cuando:** otra persona podría ejecutar el cuaderno siguiendo solo el README y obtendría el mismo campeón, la sección «Revisión con la rúbrica» está rellena y los cuatro ficheros están en `sprint-08/`.

**Después, 35 minutos de entrega, review y retro:**
- **La autoevaluación.** Cada persona rellena la suya ([autoevaluación y coevaluación](../2_Entregar/autoevaluacion_y_coevaluacion.md)) y la sube a `sprint-08/`; la coevaluación va dentro del mismo fichero y se completa en la *review*, que es conjunta con la del Sprint 7.
- **La review (5 minutos por equipo).** Enseñad el leaderboard (la tabla o un gráfico), el campeón y **por qué no ganó otro**, y una frase sobre qué cambiaría la elección si el cliente valorara otra cosa.
- **La retrospectiva.** ¿Nos sorprendió que un modelo sencillo compitiera con uno complejo? ¿Qué criterio pesó más en nuestra decisión? ¿Qué mediríamos en producción para saber que el modelo se degrada?

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| Tras *Reiniciar y ejecutar todo*, `campeon` sale distinto o las puntuaciones cambian unas centésimas | Los tiempos (ajuste y predicción) varían de una ejecución a otra y entran en la nota de coste. Si los dos primeros están a menos de 0,03, es un empate técnico. | No cambiéis de campeón tras ver el test: escribid `campeon = "…"` (vuestro modelo) en la celda del examen final, antes de `final = …`, y contad el empate en la *model card*. |
| `AssertionError: Solo el campeón debe tener AUC de test` | `auc_test` tiene valor en más de una fila. | Ejecutad desde la celda de herramientas, que borra el CSV, y repetid el examen final con un solo campeón. |
| `FileNotFoundError: [Errno 2] No such file or directory: 'leaderboard_S08.csv'`, o el CSV no sale en el panel de archivos | La sesión de Colab se reinició o se cerró y el CSV se perdió. | Ejecutad el cuaderno entero otra vez (*Reiniciar y ejecutar todo*) y descargadlo antes de cerrar Colab. |
| `AttributeError: module 'lightgbm' has no attribute '_version__'` (o `'version'`) | `__version__` lleva dos guiones bajos a cada lado y habéis escrito menos. | Escribid `lightgbm.__version__`, igual con las otras dos. |
| Subisteis un fichero a la raíz del repositorio y no a `sprint-08` | No entrasteis primero en la carpeta. | Abrid el fichero → icono del lápiz → delante del nombre escribid `sprint-08/` → **Commit changes**. |
| Os falta algún fichero o el nombre es otro | La rúbrica busca `leaderboard_S08.csv` y `reto_S08.ipynb` con ese nombre exacto. | Renombrad en vuestro ordenador y subidlos de nuevo con el mismo nombre. |
| No sabéis qué nivel poner en un criterio | Los niveles están descritos en [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md). | Leed la fila del criterio y poned el nivel cuyo texto **se cumple entero**; si algo se cumple a medias, es el nivel de abajo. Escribid la prueba. |

<!--nav-->
---

[← Paso 4](Reto_Sprint_08_paso_4.md) · [Ficha del reto: ayudas, errores frecuentes y qué hacer si os atascáis](Reto_Sprint_08.md)
<!--/nav-->
