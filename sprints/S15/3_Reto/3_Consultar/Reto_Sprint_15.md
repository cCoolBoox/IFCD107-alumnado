# Sprint 15 · Reto «El mejor modelo, demostrado»

> **Ficha completa del reto, para consultar.** Para trabajar, [el reto en una página](../1_Trabajar/Reto_Sprint_15_una_pagina.md). Qué se sube y cómo se evalúa: [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md).
>
> - Volver al [README del sprint](../../README.md).
> - Si es vuestro primer reto: [Cómo se trabaja un reto](../../../../material/4.%20Como_se_trabaja_un_reto.md).

## Ficha del reto

### 1 · 🎯 Qué os pide el cliente

**Qué os pide el cliente.** El cliente (el docente) quiere saber **qué modelo recomendáis para vuestro proyecto y por qué**. No le basta con «el que tiene el número más alto»: quiere saber si la mejora frente al *baseline* (el modelo más simple, que sirve de referencia) **compensa el coste y la complejidad**, si el modelo **funciona con datos que no ha visto** y si vuestros resultados **se pueden repetir** otro día y en otro ordenador. Este sprint es el corazón técnico del proyecto, pero lo que se valora **no es probar muchos modelos**: es **probar con orden, anotar cada prueba y elegir con honestidad**.

**Cómo se trabaja.** Partís de lo que ya tenéis del Sprint 14 (datos, análisis y *baseline*) y de las herramientas del cuaderno de práctica: una función que fija el azar, otra que anota cada prueba en un fichero y la validación cruzada (evaluar varias veces con trozos distintos de los datos). Vosotros decidís **antes** qué modelos probáis y por qué (como mínimo, tres modelos clásicos y uno neuronal —vale la red de scikit-learn—, o un asistente LLM/RAG si vuestro brief es el 3), los comparáis **con la misma partición**, **elegís el candidato sin mirar el test** y solo después lo evaluáis en el test **una única vez**. Son tres jornadas: **470 minutos de reto** (130 el día 1, 200 el día 2 y 140 el día 3) más 60 de review y retro. El equipo decide hasta dónde llega: 🟢 mínimo, 🟡 estándar o 🔴 extra.

---

### 2 · 🧰 Recursos del reto

| Recurso | Para qué lo usaréis | Dónde está |
|---|---|---|
| **Python 3.11 y las bibliotecas del proyecto** (`pandas`, `scikit-learn`, `matplotlib`; la de redes que usasteis en el Sprint 10) | Entrenar, comparar y guardar los modelos | Colab, o el entorno del equipo con las versiones de vuestro `requirements.txt` |
| **Cuaderno del sprint** [`S15_01_seguimiento_experimentos`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S15/2_Practica/para_casa/S15_01_seguimiento_experimentos.ipynb) | Copiar las funciones `fijar_semillas`, `registrar` y `experimento`, y ver cómo se mide con validación cruzada, cómo se detecta una fuga y cómo se evalúa el test una vez | Colab (50 minutos el día 1). MLflow es **opcional** |
| **Plantilla del registro** [`registro_experimentos_plantilla.csv`](../1_Trabajar/plantillas/registro_experimentos_plantilla.csv) | Solo trae la cabecera de las columnas; es la base de vuestro `registro.csv` | En GitHub: *Raw → Download* o copiar el texto |
| **Píldora y apuntes** [presentación S15_01](../../1_Teoria/S15_01_presentacion_Seguimiento_de_experimentos.pdf) · [apuntes](../../1_Teoria/apuntes/apuntes_experimentos_y_reproducibilidad.md) | El porqué de cada regla (semillas, fuga, media ± desviación, test una vez), con ejemplos numéricos | En el repositorio del curso |
| **Vuestro trabajo del Sprint 14** | Los datos, el *baseline* y el cuaderno de partida | El repositorio del equipo (`ifcd107-equipo-…`) |
| **Cómo entregar en GitHub** | Subir los ficheros a la carpeta `sprint-15/` | [Guía de entrega](../../../../material/5.%20Como_entregar_en_GitHub.md) |
| **Autoevaluación y coevaluación** | Cada persona rellena su hoja | [Hoja del sprint](../2_Entregar/autoevaluacion_y_coevaluacion.md) |
| **Un asistente de IA** (opcional) | Entender errores, pedir pistas y revisar si hay fugas | Con las reglas de la «Ayuda 1» del paso a paso |

---

### 3 · 🪜 Guía paso a paso

Son cinco pasos, de **470 minutos en total** (130 el día 1, 200 el día 2 y 140 el día 3, junto a la píldora, la práctica, la tutoría, la entrega y la review). Las jornadas de proyecto duran **6 horas completas (250 minutos de trabajo al día)**: los pasos de esta ficha ocupan unos 200 y los **50 minutos restantes de cada día son «subir de nivel»** (pasar del mínimo al estándar con la rúbrica en la mano). Cada uno dice **qué hacéis** (la lista corta), **cómo se hace** con el detalle, **qué deberíais ver** y **cuándo está hecho**. Las ayudas (IA, errores, atascos) están al final. Si el tiempo aprieta, completad el nivel mínimo y dejad lo demás para casa.

**Cada paso tiene su propia página.** Abrid la que toque y volved aquí cuando acabéis:

- [Paso 1 · Preparar el terreno y repetir el baseline (día 1, 130 minutos)](Reto_Sprint_15_paso_1.md)
- [Paso 2 · Probar los modelos clásicos y el neuronal (día 2, 140 minutos)](Reto_Sprint_15_paso_2.md)
- [Paso 3 · Comprobar que no hay fugas y tutoría (día 2, 60 minutos)](Reto_Sprint_15_paso_3.md)
- [Paso 4 · Elegir el candidato sin tocar el test (día 3, 70 minutos)](Reto_Sprint_15_paso_4.md)
- [Paso 5 · Test una sola vez, explicación, revisión y entrega (día 3, 70 minutos)](Reto_Sprint_15_paso_5.md)

#### Ayuda 1 · Cómo usar la IA en este reto

La IA puede ahorrar tiempo, pero **da código que parece funcionar y no se entiende**, y puede pasar por alto una fuga o ver una que no existe. Reglas:
- **Todo lo que dé, lo ejecutáis y lo entendéis.** Si el docente pregunta por una línea, tenéis que saber explicarla.
- **El test se usa una sola vez, con el modelo ya elegido.** Elegir por el test invalida el resultado.
- **Declaradlo** en `justificacion_candidato.md` y **marcad en el registro** las pruebas hechas con código generado por IA.
- **Nada de datos personales ni claves** en una IA ni en el repositorio.

| Para qué | Ejemplo de petición | Qué comprobáis |
|---|---|---|
| Entender un modelo | «Explícame cuándo conviene un modelo de boosting frente a una regresión logística, con un ejemplo sencillo» | Que la explicación encaja con **vuestros datos** |
| Depurar un error | «Este código de scikit-learn da este error: *[error]*. Datos: *[estructura]*» | Que entendéis la causa |
| Detectar fugas | «Aquí está mi pipeline: *[código]*. ¿Hay alguna operación que use el test o el futuro?» | Que **verificáis** la respuesta; la IA puede pasarlas por alto o ver fugas inexistentes |
| Interpretar la importancia de variables | «Tengo este gráfico de importancia por permutación (descripción). ¿Qué significa que la variable X pese tanto?» | Contrastadlo con el sentido del negocio |

#### Ayuda 2 · Errores frecuentes (y cómo evitarlos)

| Error | Por qué ocurre | Cómo evitarlo |
|---|---|---|
| Elegir el modelo mirando el test | «Para ver cuál es mejor» | Elegid solo con validación; el test, una vez |
| Resultados «increíbles» (99 %) | Fuga de datos | Revisad variables y partición con la lista del paso 3 |
| Registro con 3 filas de una sola persona | El responsable técnico lo hace todo | Cada persona prueba algo y lo anota con su nombre |
| Cada persona tiene su propio `registro.csv` | Se trabaja en copias distintas del cuaderno | Un único `03_modelos.ipynb` compartido (Compartir → editor), con una sección por persona: el `registro.csv` sale de «Reiniciar y ejecutar todo» |
| Comparar con particiones distintas | Cada uno prueba por su lado | Una partición común, guardada y compartida |
| Mejor número = mejor modelo | Se mira solo la métrica | Añadid tiempo, simplicidad y explicabilidad |
| Mezclar fotos del mismo objeto entre entrenamiento y test | En imágenes es fácil | Particionad por objeto o por parcela |
| Cambiar la semilla hasta que salga un resultado bonito | Prisa o ganas de ganar | Una semilla para todo el equipo; si cambia mucho, el modelo es inestable y hay que decirlo |

#### Ayuda 3 · Si os atascáis

1. **No sabemos qué modelos probar:** repasad el *leaderboard* del Sprint 8 y la red del Sprint 10, y usad las mismas familias.
2. **Dos modelos dan casi lo mismo:** perfecto; elegid el más simple y explicadlo.
3. **No tenemos GPU o va lenta:** usad un subconjunto de los datos y anotad el coste en el registro.
4. **El modelo guardado pesa más de 25 MB:** no lo subáis por el navegador; avisad al docente, subid `metadatos.json` y dejad escrito en él cómo volver a generar el modelo con vuestro cuaderno.
5. Preguntad al equipo y, después, al docente. Más ayuda: [Cómo se trabaja un reto](../../../../material/4.%20Como_se_trabaja_un_reto.md).
