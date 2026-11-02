# Sprint 9 · Reto «Conocer al huésped»

> **Ficha completa del reto, para consultar.** Para trabajar, [el reto en una página](../1_Trabajar/Reto_Sprint_09_una_pagina.md). Qué se sube y cómo se evalúa: [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md).
>
> - Volver al [README del sprint](../../README.md).
> - Si es vuestro primer reto: [Cómo se trabaja un reto](../../../../material/4.%20Como_se_trabaja_un_reto.md).

## Ficha del reto

### 1 · 🎯 Qué os pide el cliente

**Qué os pide el cliente.** Lucía, la directora comercial de TurisData Canarias, envía **la misma newsletter a sus 1.200 huéspedes** y vende sus **25 experiencias** con los mismos banners. Sospecha que hay «tipos» de cliente muy distintos y que cada uno querría cosas diferentes. Os pide: *«Decidme quiénes son mis clientes, cómo los llamo y qué le enseño a cada uno.»* Ninguna columna dice a qué tipo pertenece cada huésped: vosotros tenéis que **descubrir los grupos** con *clustering* (agrupar datos parecidos sin respuestas previas), **dibujarlos** en un mapa 2D, **ponerles nombre** y proponer **una acción comercial por grupo**. Además, construiréis un **recomendador** sencillo: dado un huésped, sugerirle experiencias que probablemente le gusten.

**Cómo se trabaja.** No hace falta experiencia previa: los cuadernos del sprint (`S09_01`, `S09_02` y `S09_03`) ya os hacen practicar cada pieza, y el reto consiste en **reutilizarlas con vuestras propias decisiones** y, sobre todo, en **explicar** qué habéis encontrado. No hay pruebas automáticas ni solución del docente: los grupos se validan con **sentido de negocio** y con **métricas internas** (silueta, RMSE). En clase tenéis 10 minutos de planning y 45 de reto el día 1, y 50 de reto más 40 de entrega, review y retrospectiva el día 2; lo que no quepa va a casa. El equipo decide hasta dónde llega: 🟢 mínimo, 🟡 estándar o 🔴 extra.

---

### 2 · 🧰 Recursos del reto

| Recurso | Para qué lo usaréis | Dónde está |
|---|---|---|
| **Python con `numpy`, `pandas`, `matplotlib`/`seaborn` y `scikit-learn`** (solo esas bibliotecas: nada de librerías de recomendación especializadas) | Escribir el cuaderno del reto | Ya instaladas en Google Colab |
| **Google Colab** | Crear y ejecutar `reto_S09_conocer_al_huesped.ipynb` | En colab.research.google.com: *Archivo → Cuaderno nuevo* |
| **Los datos de huéspedes** [`huespedes.csv`](../../../../datos/huespedes.csv) | 1.200 huéspedes con 7 variables (`edad`, `gasto_medio_dia`, `noches_medias`, `reservas_anio`, `antelacion_media`, `pct_gasto_actividades`, `viaja_con_ninos`). Son **sintéticos** | No hace falta descargarlos: la celda «Preparación» de los cuadernos `S09_01`–`S09_03` los baja sola |
| **Las valoraciones** [`valoraciones_experiencias.csv`](../../../../datos/valoraciones_experiencias.csv) y [`experiencias.csv`](../../../../datos/experiencias.csv) | 2.232 valoraciones (de 1 a 5 estrellas) de 300 usuarios sobre 25 experiencias, y el catálogo con nombre, categoría e isla | Igual: los baja la celda «Preparación» |
| **Cuadernos del sprint**: [`S09_01`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/2_Practica/S09_01_clustering.ipynb), [`S09_02`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/2_Practica/S09_02_pca.ipynb) y [`S09_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/2_Practica/S09_03_recomendadores.ipynb) | El código de cada paso: escalar, k-means y silueta, PCA, recomendadores, RMSE y precision@3 | Colab; su [código explicado](../../2_Practica/codigo_explicado/README.md) |
| **Presentaciones y apuntes** | Repasar los conceptos: [clustering](../../1_Teoria/S09_01_presentacion_Clustering.pdf), [PCA](../../1_Teoria/S09_02_presentacion_PCA.pdf), [sistemas de recomendación](../../1_Teoria/S09_03_presentacion_Sistemas_de_recomendacion.pdf), [aprendizaje por refuerzo](../../1_Teoria/S09_04_presentacion_Aprendizaje_por_refuerzo.pdf) y los [apuntes](../../1_Teoria/apuntes/apuntes_clustering_recomendadores_y_refuerzo.md) | Carpeta `1_Teoria` |
| **La plantilla de la ficha** [`plantilla_ficha_segmentos.md`](../1_Trabajar/plantillas/plantilla_ficha_segmentos.md) | Ficha de segmentos con huecos, nota de IA responsable y sección «Revisión con la rúbrica» | En GitHub: abrid el archivo y copiad el texto con el botón *Raw* |
| **Cómo entregar en GitHub** | Subir el cuaderno y la ficha a `sprint-09/` | [Guía de entrega](../../../../material/5.%20Como_entregar_en_GitHub.md) |
| **Autoevaluación y coevaluación** | Cada persona rellena su hoja | [Hoja del sprint](../2_Entregar/autoevaluacion_y_coevaluacion.md) |
| **Un asistente de IA** (opcional) | Entender conceptos, pedir nombres y pensar riesgos | Con las reglas de la «Ayuda 1» del paso a paso |

---

### 3 · 🪜 Guía paso a paso

Son cinco pasos, de **105 minutos en total** (unos 45 el día 1 y unos 60 el día 2; el aula da 45 y 50, así que lo que no quepa va a casa). Cada uno dice **qué hacéis** (la lista corta), **cómo se hace** con el detalle, **qué deberíais ver** y **cuándo está hecho**. Las ayudas (IA, errores, atascos) están al final. Si el tiempo aprieta, completad el nivel mínimo y dejad lo demás para casa.

**Cada paso tiene su propia página.** Abrid la que toque y volved aquí cuando acabéis:

- [Paso 1 · Preparar el cuaderno y los datos (día 1, 10 minutos)](Reto_Sprint_09_paso_1.md)
- [Paso 2 · Segmentar y elegir k (día 1, 20 minutos)](Reto_Sprint_09_paso_2.md)
- [Paso 3 · Mapa PCA e interpretación de los segmentos (día 1, 15 minutos)](Reto_Sprint_09_paso_3.md)
- [Paso 4 · Recomendador de experiencias (día 2, 30 minutos)](Reto_Sprint_09_paso_4.md)
- [Paso 5 · Ficha, IA responsable, revisión y entrega (día 2, 30 minutos)](Reto_Sprint_09_paso_5.md)

#### Ayuda 1 · Cómo usar la IA en este reto

La IA puede ahorrar tiempo, pero **inventa con mucha seguridad**: un nombre de segmento que suena bien pero no refleja las cifras es un error. Reglas:
- **Todo lo que dé, lo comprobáis y lo entendéis.** Si el docente pregunta por una celda, tenéis que saber explicarla; en la review puede preguntar a cualquiera.
- **Los datos mandan:** si un nombre o una conclusión de la IA no cuadra con vuestras cifras, no vale.
- **Declaradlo** en el cuaderno: dónde la habéis usado y qué habéis comprobado.
- **Nada de datos personales ni claves** en una IA.

| Para qué | Ejemplo de petición | Qué comprobáis |
|---|---|---|
| Entender un concepto | «Explícame k-means y la silueta con una analogía de personas en una fiesta» | Que podéis explicarlo con vuestras palabras |
| Entender PCA | «¿Qué significa que PCA conserve el 60 % de la varianza? Dame un ejemplo sin fórmulas» | Que vuestro gráfico dice lo mismo |
| Poner nombres a los segmentos | «Dado este perfil medio: *[tabla]*, dame 5 nombres comerciales cortos y evocadores» | Que el nombre refleja las **cifras** del segmento, no una invención |
| Pensar en riesgos | «¿Qué riesgos tiene recomendar experiencias según la edad?» | Elegid los que aplican a **vuestro** caso y dad una medida real |

#### Ayuda 2 · Errores frecuentes (y cómo evitarlos)

| Error | Por qué ocurre | Cómo evitarlo |
|---|---|---|
| Agrupar sin escalar | Se olvida | Escalad **antes** del clustering |
| Elegir `k` solo con la silueta | «Es lo que dice el número» | Añadid el criterio de negocio |
| Poner nombres sin mirar los datos | Suena bien | Cada nombre debe justificarse con **dos cifras** del perfil |
| Recomendar lo que el usuario ya ha valorado | No se filtra | La función debe excluirlas |
| Evaluar el recomendador con los mismos datos que usó | «Es lo más fácil» | Probad con valoraciones **escondidas** |
| Nota de IA responsable genérica | Prisa | Dos riesgos **concretos** de este caso, con medida |
| El cuaderno falla al ejecutarlo de nuevo | Celdas ejecutadas en desorden o semillas sin fijar | *Reiniciar y ejecutar todo* antes de subirlo y usar siempre la misma `SEMILLA` |

#### Ayuda 3 · Si os atascáis

1. **Todos los segmentos se parecen:** revisad que habéis escalado y probad otras columnas; quizá algunas no aportan.
2. **El mapa PCA sale con todo mezclado:** es posible; decidlo en la ficha. Los grupos pueden estar separados en dimensiones que el 2D no recoge.
3. **El recomendador recomienda siempre lo mismo:** probablemente es un sesgo de popularidad; comentadlo como riesgo.
4. Repasad el cuaderno de ese paso y su código explicado; preguntad al equipo y, después, al docente. Más ayuda: [Cómo se trabaja un reto](../../../../material/4.%20Como_se_trabaja_un_reto.md).
