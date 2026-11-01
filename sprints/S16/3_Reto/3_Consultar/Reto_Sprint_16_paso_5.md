# Paso 5 · Cerrar la model card y completar la memoria (día 2, 80 minutos)

<!--nav-->
> Sprint 16 · Reto «Entrega final: evaluar, demostrar y documentar» · paso 5 de 8 · [Ficha del reto](Reto_Sprint_16.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_16_una_pagina.md) · [Paso 6 →](Reto_Sprint_16_paso_6.md)
<!--/nav-->

1. Clasificar el sistema según el RGPD y el AI Act y cerrar el registro de riesgos.
2. Terminar la model card con las cifras finales (los apartados 6 a 9).
3. Completar el borrador de la memoria con todos los apartados.

**En sencillo.** Hasta hoy habéis construido el modelo; ahora hay que **contárselo a otra persona con pruebas**. Es como entregar un coche: no basta con que ande, hay que dar la ficha técnica (la model card), la lista de lo que puede fallar y qué se ha hecho para evitarlo (el registro de riesgos) y el manual completo (la memoria). La regla de oro es que **cada afirmación se pueda comprobar**: «hemos cuidado la privacidad» no vale; «no hay datos personales, ver `plan_datos_licencias.md`, apartado 6» sí. No hace falta saber de leyes ni de Python: casi todo es rellenar los documentos que ya tenéis con las cifras de vuestros cuadernos. Una pequeña parte de código os saca esas cifras ya escritas, para que no las copiéis a mano y no se cuele un error.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Model card** | La ficha de máximo 2 páginas del modelo. Hoy se rellenan los apartados 6 a 9 (subgrupos, riesgos, limitaciones, mantenimiento). |
| **Subgrupo** | Una parte de los datos que tiene sentido separar (un canal de venta, un país). El apartado 6 dice cómo rinde el modelo en cada uno. |
| **RGPD** | La ley europea de protección de datos personales. Pregunta: ¿hay datos de personas? |
| **AI Act** | El reglamento europeo de IA. Clasifica los sistemas por riesgo: inaceptable, alto, limitado o mínimo. |
| **Evidencia** | Algo que se puede comprobar en el repositorio: una ruta de archivo y el apartado donde se ve. |
| **Riesgo residual** | El riesgo que queda después de mitigar y que decidís aceptar y contar al cliente. |
| **Supervisión humana** | Que una persona revisa y decide; el modelo solo orienta. |
| **Pie de figura** | La frase bajo un gráfico: «Figura 3. Lo que demuestra. Fuente». Es lo que lee quien hojea la memoria. |

**Cómo se hace**

1. **Repartir y abrir los archivos (3 minutos).** Quien rellena cada cosa:

    | Persona | Hoy |
    |---|---|
    | C | Clasificación y registro de riesgos (puntos 2 y 3), apartados 6 y 7 de la model card, sección 5 y 6 de la memoria |
    | D | Apartados 8 y 9 de la model card (el 8 tiene que decir lo mismo que `limitaciones` del demostrador, paso 4), secciones 7 y 8 de la memoria |
    | B | Apartado 5 de la model card con las cifras finales, secciones 3 y 4 de la memoria |
    | A | Revisar los apartados 1 a 4 de la model card, secciones 1 y 2 de la memoria |

    Abrid `sprint-16/docs/model_card.md` (el del paso 2) y el documento de la memoria. El registro de riesgos lo copiáis ahora: abrid `sprint-14/riesgos_eticos.md`, pulsad **Raw**, `Ctrl + A` y `Ctrl + C`; luego **Add file → Create new file**, nombre `sprint-16/docs/riesgos_eticos.md`, `Ctrl + V` y **Commit changes**. Para editar un archivo, el lápiz ✏️; **cada fila de una tabla va en una sola línea**.

2. **Clasificar el sistema (8 minutos).** En `riesgos_eticos.md`, **Parte B**. Una respuesta por fila, con su justificación y, si procede, la ruta de la evidencia. La plantilla orienta así: un sistema que solo predice demanda agregada suele ser de riesgo **mínimo**; un chatbot que informa a personas tiene obligaciones de **transparencia** (riesgo **limitado**); uno que evalúe o decida sobre el acceso de personas a educación, empleo o servicios esenciales es de riesgo **alto**. **Llevad vuestra respuesta escrita al docente antes de darla por buena**, como pide la plantilla. Ejemplo con TurisData:

    | Cuestión | Respuesta de ejemplo |
    |---|---|
    | ¿Datos personales? | No. Datos sintéticos de una empresa ficticia; ninguna columna lleva nombres (`plan_datos_licencias.md`, apartado 6). |
    | Base legal / finalidad | No aplica por no haber datos personales. Finalidad: orientar la gestión de disponibilidad. |
    | ¿Evaluación de impacto (EIPD)? | No: no hay datos personales ni decisiones sobre personas. |
    | Nivel de riesgo AI Act | **Mínimo**: apoya la gestión de disponibilidad y no decide sobre el acceso de personas a educación, empleo ni servicios esenciales. |
    | Obligaciones que se derivan | Avisar de que es una estimación y de sus límites (demostrador), que una persona decida si se pide depósito y documentarlo (model card). |
    | ¿Decide sobre personas? | No. La model card prohíbe usarlo para decidir sobre personas concretas. |

3. **Cerrar el registro de riesgos (12 minutos).** Tres cosas, en este orden:

    - **Parte A, columna S16.** Para cada pregunta, un símbolo (**✔** cumplido con evidencia, **◐** parcial, **✘** no cumplido, **n/a** no aplica, y por qué) y, en «Evidencia», la ruta y el apartado. Un ✔ sin evidencia es un ◐. Ejemplo: «¿Se ha medido el rendimiento por subgrupos?» → ✔ · `sprint-16/notebooks/04_evaluacion.ipynb` y model card, apartado 6.
    - **Parte C, riesgos altos.** Nivel = P × I (cada uno de 1 a 3): 1-2 bajo, 3-4 medio, **6-9 alto**. Cada riesgo alto necesita estado y evidencia. Así se rellena una fila (R-01 de TurisData):

        | Campo | Qué se escribe | Ejemplo |
        |---|---|---|
        | Riesgo | Qué puede ir mal y a quién afecta, con cifra si la hay | En el canal `directo` se detecta el 61,6 % de las cancelaciones frente al 82,8 % global: el alojamiento pierde ingresos en ese canal |
        | Tipo · P · I · Nivel | Datos, modelo, uso, legal o técnico; probabilidad; impacto; producto | modelo · 3 · 2 · 6 (alto) |
        | Medida de mitigación | Qué se hizo | Umbral propio de 0,25 para el canal `directo` |
        | Responsable | Una persona | Ana |
        | Estado | `abierto`, `mitigado` o `aceptado` (el sprint a veces dice «pendiente»: es `abierto`) | mitigado |
        | Cómo se evaluó | Prueba, métrica y resultado, con la ruta | Test: recall de `directo` 61,6 % → 79,2 %; +52 falsas alarmas (`04_evaluacion.ipynb`, sección de mitigación) |

    - **Parte D, cierre.** Cuatro respuestas: riesgos altos mitigados y su evidencia, **riesgos residuales** que aceptáis y comunicáis, limitaciones y usos no permitidos (pasan a la model card), fecha y firmas. Si un riesgo alto sigue `abierto`, o lo mitigáis hoy o lo aceptáis y lo contáis aquí.

4. **Apartado 6 de la model card: subgrupos (6 minutos).** Las cifras no se escriben a mano. En el cuaderno `04_evaluacion.ipynb`, después de la mitigación del paso 3, ejecutad:

    ```python
    for estado, tabla_estado, prediccion in [("antes", antes, pred), ("después", despues, pred_nueva)]:
        global_ = recall_score(real, prediccion)
        for _, f in tabla_estado.iterrows():
            dif = (f["recall"] - global_) * 100
            print(f"| canal = {f['subgrupo']} ({estado}) | {f['reservas']} | recall {f['recall']:.1%} (± {f['±'] * 100:.1f}) | {dif:+.1f} puntos | |")
    ```

    Qué hace cada línea:

    - `antes` y `despues` son las tablas del paso 3; `pred` y `pred_nueva`, los avisos sin y con la medida. Si dan `NameError`, volved a ejecutar el cuaderno desde la primera celda.
    - `recall_score(real, prediccion)` es el recall global de cada estado y `dif` lo que se aleja de él cada subgrupo, en puntos.
    - El `print(f"| … |")` escribe cada subgrupo como **una fila ya en formato de tabla**. Copiad las filas que os interesan debajo de la cabecera del apartado 6. La última columna, «¿Es aceptable?», la escribís vosotros.

    Con TurisData salen filas como `| canal = directo (antes) | 388 | recall 61.6% (± 8.5) | -21.2 puntos | |`. Dejadlo así en el apartado 6 (cambiad el punto por la coma si queréis):

    | Subgrupo | n | Métrica | Diferencia con el global | ¿Es aceptable? |
    |---|---|---|---|---|
    | canal = directo (antes) | 388 | recall 61,6 % (± 8,5) | −21,2 puntos | No: se escapan 4 de cada 10 cancelaciones |
    | canal = directo (después) | 388 | recall 79,2 % (± 7,1) | −6,8 puntos | Sí, con coste: 52 falsas alarmas más |
    | canal = empresa | 79 | recall 73,7 % (± 14,0) | −12,3 puntos | Cifra poco fiable: solo 38 cancelaciones |
    | canal = web_intermediaria | 738 | recall 90,9 % (± 2,8) | +4,9 puntos | Sí |

    El «antes» y el «después» se comparan **cada uno con el global de su estado** (82,8 % y 86,0 %). Añadid una fila por cada subgrupo con diferencia grande y casos suficientes; los que tienen pocos casos, marcadlos como «poco fiable».

5. **Apartados 5, 7, 8 y 9 de la model card (6 minutos).**

    | Apartado | Qué se escribe | Ejemplo con TurisData |
    |---|---|---|
    | 5 · Métricas | Las cifras finales del paso 1, con intervalo | «AUC: baseline 0,50 → modelo 0,744 (95 %: 0,719–0,767). Recall 0,828 (0,799–0,854), precisión 0,589, umbral 0,35. Coste en 1500 reservas de prueba: 34.400 € sin modelo → 17.810 € con él» |
    | 7 · Ética y riesgos | La clasificación de la Parte B, los 2 o 3 riesgos principales con cómo se evaluó la mitigación, supervisión humana y transparencia | «Riesgo mínimo; sin datos personales. R-01, sesgo por canal: umbral propio para `directo`, recall 61,6 % → 79,2 %. Supervisión: una persona decide si pide depósito. Transparencia: cada resultado lleva el aviso con el AUC y las limitaciones» |
    | 8 · Limitaciones | Cuándo **no** fiarse (casos de vuestros análisis), recomendaciones y qué falta antes de un despliegue real. **Mismo texto que `limitaciones` del demostrador** | «No fiarse con el canal `directo`, con reservas sin país (15 cancelaciones en el test: cifra poco fiable) ni con otro alojamiento distinto del ficticio. Antes de un despliegue real: datos reales y vigilar el recall por canal» |
    | 9 · Contacto | Una persona responsable y cada cuánto se reevalúa | «Ana · se reevalúa cuando haya reservas nuevas y siempre que cambie la política de cancelaciones» |

    Si adoptáis la medida del paso 3, decid en el apartado 7 que el sistema final **usa** el umbral propio. Comprobad que no queda ningún `______` ni `[Nombre del modelo]` (buscadlos con `Ctrl + F`) y que el archivo cabe en 2 páginas: tablas y frases cortas.

6. **Memoria: todas las secciones en borrador (40 minutos).** «Borrador» significa que **cada sección tiene texto**, aunque sea áspero. Cada persona escribe **sus** secciones (las del paso 2) en el documento compartido, con **cifras copiadas de los cuadernos** (no de memoria) y con lo que dice el esqueleto en cada una. Lo que falte, escribidlo como `[PENDIENTE: qué falta]`, para encontrarlo luego con `Ctrl + F`.

    | Sección (páginas) | Qué se cuenta | De dónde sale |
    |---|---|---|
    | 1 Problema (1) | Contexto, **decisión** que apoya y quién la toma, métrica de negocio y técnica con umbral de éxito, valor esperado con supuestos | `ficha_proyecto.md` |
    | 2 Datos (2) | Tabla de fuentes con licencia, defectos de calidad y su tratamiento, sesgos de muestreo, 2-3 figuras del EDA | `plan_datos_licencias.md`, `01_eda.ipynb` |
    | 3 Metodología (1) | Partición anti-fuga, baseline, métricas, validación cruzada, semillas, enlace a `registro.csv` | `plan_datos_licencias.md`, `03_modelos.ipynb` |
    | 4 Modelado (2) | Baseline y al menos 3 modelos, tabla con media ± desviación y tiempo, por qué se eligió el candidato | `registro.csv`, `justificacion_candidato.md` |
    | 5 Evaluación (2) | Métricas en test con intervalo, gráficos, análisis de errores con ejemplos, generalización | `04_evaluacion.ipynb` (paso 1) |
    | 6 IA responsable (2) | Resumen del checklist, tabla de riesgos altos, subgrupos y mitigación medida, clasificación, limitaciones | `riesgos_eticos.md`, model card, paso 3 |
    | 7 Demostrador (1) | Qué hace, captura, errores del usuario, cómo reproducirlo, plan B | `demostrador/`, paso 4 |
    | 8 Gestión (0,5) | Roles y rotación, backlog y sprints, mejoras entre retros (acción → efecto), reparto de trabajo | tablero, `backlog_y_sprints.md` |
    | 9 Conclusiones (1) | Qué se recomienda al cliente, qué **no** hacer, límites y trabajo futuro | todo lo anterior |

    La sección 0 (resumen) se escribe el día 3. Ejemplo de párrafo de la sección 6 con las cifras del paso 3:

    ```text
    Medimos el recall (cancelaciones detectadas) por canal en las 1500 reservas de prueba.
    El global es del 82,8 %, pero en el canal directo es del 61,6 % (± 8,5 puntos; 77 de 125
    cancelaciones). Aplicamos un umbral propio para ese canal (0,25 en lugar de 0,35), elegido
    con validación cruzada sobre el entrenamiento. Tras la medida el recall de directo sube al
    79,2 % y el global al 86,0 %; los otros canales no cambian. El precio son 52 falsas alarmas
    más (449 frente a 397) y 460 € de coste más en esas 1500 reservas (de 17.810 € a 18.270 €).
    ```

    Cada **figura** lleva título que dice lo que se ve, ejes con nombre, número, pie y una mención en el texto. Para guardar el gráfico de subgrupos del paso 1, añadid esta línea justo antes de `plt.show()`:

    ```python
    fig.savefig("fig_subgrupos.png", dpi=150, bbox_inches="tight")
    ```

    `fig.savefig` guarda la imagen con el nombre indicado, `dpi=150` le da calidad para imprimir y `bbox_inches="tight"` recorta los márgenes. Después descargadla desde el panel de archivos de Colab (icono de carpeta). Pie de ejemplo: «Figura 4. En el canal directo detectamos solo el 62 % de las cancelaciones (test de 1500 reservas; las barras de error son el margen del 95 %). Fuente: `04_evaluacion.ipynb`.»

7. **Comprobar la coherencia y declarar la IA (5 minutos).** Una persona que no escribió esas partes comprueba que lo mismo dice lo mismo en todos los sitios:

    | Dato | Dónde aparece | Tiene que ser igual en |
    |---|---|---|
    | AUC y recall del modelo | Cuaderno del paso 1 | Model card (5), memoria (5), `auc_test` del demostrador y README |
    | Cifras por subgrupo, antes y después | Cuaderno del paso 3 | Model card (6), memoria (6) y `registro.csv` |
    | Limitaciones y usos no permitidos | Model card (8) | `limitaciones` del demostrador, memoria (6 y 9) y `riesgos_eticos.md` (Parte D) |
    | Nivel AI Act y datos personales | `riesgos_eticos.md` (Parte B) | Model card (7), README (apartado 7) y memoria (6) |

    Si habéis usado una IA para redactar o programar, **declaradlo**: qué pedisteis, qué revisasteis y qué cambiasteis. Cada persona lo escribe en su hoja de autoevaluación (la frase «He usado IA para ……, y lo que he comprobado a mano es ……») y el equipo lo resume en «Referencias y licencias» de la memoria, que no tiene un apartado fijo para ello. Ejemplo: pedimos «Corrige la ortografía y la claridad de este párrafo sin cambiar el contenido» (sección 6); revisamos que 61,6 %, 79,2 % y +52 falsas alarmas seguían iguales; cambiamos dos frases demasiado largas.

**Qué deberíais ver.**
- **En el cuaderno:** las ocho líneas con `| canal = … |`; por ejemplo `| canal = directo (antes) | 388 | recall 61.6% (± 8.5) | -21.2 puntos | |` y `| canal = directo (después) | 388 | recall 79.2% (± 7.1) | -6.8 puntos | |`. Y el archivo `fig_subgrupos.png` en el panel de archivos.
- **En el repositorio:** `docs/model_card.md` sin ningún `______`, con las tablas bien dibujadas en GitHub; `docs/riesgos_eticos.md` con la columna S16 del checklist, la Parte B justificada, al menos 5 riesgos y cada riesgo alto con estado y evidencia, y la Parte D rellena.
- **En el documento de la memoria:** las secciones 1 a 9 con texto (la 0 se escribe el día 3), figuras con pie y los `[PENDIENTE: …]` que queden localizados.

**Hecho cuando:** la model card está completa, la clasificación RGPD / AI Act está justificada con evidencia, cada riesgo alto tiene estado y evidencia, y la memoria tiene todos los apartados escritos aunque sea en borrador.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'antes' is not defined` (o `despues`, `pred_nueva`) | Colab se reinició o no se ejecutaron las celdas del paso 3. | Pulsad ▶ por orden desde la primera celda del cuaderno. |
| `KeyError: '±'` | La función `medir_subgrupos` no es la del paso 1 (le falta la columna `±`). | Volved a copiar la celda del paso 1 y ejecutad de nuevo las tablas. |
| Una tabla se ve en GitHub como texto suelto, sin dibujar | Falta la fila de guiones bajo la cabecera, o una fila está partida en dos líneas, o hay una barra vertical dentro de una celda. | Editad con ✏️: cada fila en una sola línea y la fila de guiones justo debajo de la cabecera. |
| La model card ocupa más de 2 páginas | Frases largas o demasiadas filas. | Dejad solo los subgrupos con diferencia grande y casos suficientes; una frase por celda. |
| Un riesgo alto sin evidencia, o con «hemos cuidado…» | La evidencia tiene que poder comprobarse. | Escribid la ruta y el apartado (`sprint-16/docs/model_card.md`, apartado 8). Si no existe, es un ◐ o sigue `abierto`. |
| La misma cifra sale distinta en la model card y en la memoria | Se copió de versiones distintas del cuaderno. | Volved a sacarla del cuaderno ejecutado y usad la tabla del punto 7. |
| No aparece `fig_subgrupos.png` en el panel de archivos | La línea `fig.savefig` va después de `plt.show()`, o el panel no se ha refrescado. | Ponedla justo antes de `plt.show()`, ejecutad la celda y pulsad el icono de refrescar. |

<!--nav-->
---

[← Paso 4](Reto_Sprint_16_paso_4.md) · [Ficha del reto](Reto_Sprint_16.md) · [Paso 6 →](Reto_Sprint_16_paso_6.md)
<!--/nav-->
