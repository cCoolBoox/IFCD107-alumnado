# Paso 1 · Planning y pesos de los criterios (día 1, 20 minutos)

<!--nav-->
> Sprint 8 · Reto «Duelo de modelos» · paso 1 de 5 · [Ficha del reto](Reto_Sprint_08.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_08_una_pagina.md) · [Paso 2 →](Reto_Sprint_08_paso_2.md)
<!--/nav-->

1. Repartir roles y tareas, y apuntarlas en el tablero.
2. Leer el reto y decidir hasta qué nivel queréis llegar (🟢, 🟡 o 🔴).
3. Acordar los **pesos** de los tres criterios con la «voz del cliente» (el docente) y justificarlos.
4. Escribir los pesos y su justificación en un sitio común: los usaréis en los pasos 4 y 5.

**En sencillo.** Imaginad que vuestra empresa tiene que elegir una furgoneta. Una es la más potente, otra es la que cualquiera sabe conducir y arreglar, y otra es la más barata de mantener. No hay una «mejor» a secas: depende de lo que le importe más a quien paga. En este reto hacéis lo mismo con modelos de inteligencia artificial que avisan de qué reservas se van a cancelar: los enfrentáis en una tabla de clasificación (el *leaderboard*) y elegís un campeón con **tres criterios**. En este primer paso **no se programa nada**: decidís cuánto vale cada criterio (los **pesos**) junto con el cliente, que es el docente, y repartís el trabajo. No hace falta saber qué es un árbol, un bosque o una SVM: los iréis conociendo en los pasos siguientes.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Modelo** | Un programa que aprende de reservas pasadas a calcular la probabilidad de que una reserva nueva se cancele. |
| ***Leaderboard*** | La tabla de clasificación: una fila por modelo, con sus notas. Es un fichero, `leaderboard_S08.csv`. |
| **Peso** | Cuánto cuenta un criterio en la nota final. Los tres pesos suman 100 % (en el cuaderno, 1). |
| **AUC** | Una nota de 0,5 a 1 que dice cómo de bien separa un modelo las reservas que se cancelan de las que no. 0,5 es como tirar una moneda; 1 es perfecto. |
| **Validación cruzada** | Medir el modelo varias veces con trozos distintos de los datos de entrenamiento (aquí, 5) y quedarse con la media: la nota es más fiable que con una sola prueba. |
| **Explicabilidad** | Poder decir **por qué** el modelo avisa de una cancelación. |
| **Coste** | Lo que cuesta tener el modelo en marcha: tiempo de entrenarlo, tiempo de predecir y espacio que ocupa. |
| **Test** | Un trozo de las reservas (1200 de 6000) que se aparta y no se toca hasta el final: el examen final. Se usa **una sola vez**. |
| ***Model card*** | La «ficha técnica» del modelo elegido: para qué sirve, con qué datos, cómo rinde, riesgos y límites. Es un fichero de texto, `model_card.md`. |

**Cómo se hace**

1. **Leed el reto entre todos (5 minutos).** Abrid [el reto en una página](../1_Trabajar/Reto_Sprint_08_una_pagina.md) y subrayad tres cosas. Una: el cliente pregunta **qué modelo poner en producción**. Dos: se entregan **cuatro ficheros** (`leaderboard_S08.csv`, `model_card.md`, `reto_S08.ipynb` y `README.md`) más una autoevaluación por persona. Tres: la **regla de oro**, el test se usa **una sola vez y solo con el campeón**.
2. **Decidir el nivel.** El equipo elige hasta dónde llega:

    | Nivel | Qué hay que tener, en corto |
    |---|---|
    | 🟢 **Mínimo** (todos los equipos) | Pesos justificados, leaderboard con 6 modelos, campeón elegido, test una sola vez, *model card* y README cortos. |
    | 🟡 **Estándar** | Lo anterior, más búsqueda de hiperparámetros en dos familias de modelos, análisis de sensibilidad de los pesos, *model card* completa y README con versiones y uso de IA. |
    | 🔴 **Extra** | Lo anterior, más importancia de variables, varias semillas o plan de mantenimiento. |

    El mínimo ya es una entrega válida. Si dudáis, apuntad el estándar como objetivo y bajad al mínimo solo si el tiempo aprieta.

3. **Entender los tres criterios.** Son los que vais a ponderar. Fijaos en que dos de las tres notas las calcula el cuaderno solo y una la ponéis vosotros:

    | Criterio | Qué mide | De dónde sale su nota en el cuaderno |
    |---|---|---|
    | **Rendimiento** | Cuánto acierta: AUC en validación cruzada, con su desviación (media ± desviación). | El AUC, llevado a una escala de 0 a 1 (el peor modelo de la tabla, 0; el mejor, 1). |
    | **Explicabilidad** | Si el gerente puede entender **por qué** avisa el modelo. | Una nota de 1 (caja negra) a 5 (se lee directamente) que **ponéis vosotros**; el cuaderno la pasa a una escala de 0 a 1. |
    | **Coste** | Tiempo de entrenar, tiempo de predecir y tamaño del modelo. | Los tres juntos, llevados a una escala de 0 a 1 (1 = barato). El esfuerzo de mantenimiento no se calcula: se cuenta en la *model card*. |

4. **Preguntar al cliente y decidir los pesos (10 minutos).** El docente hace de cliente: preguntadle lo que haría una consultora, por ejemplo «¿necesita el gerente explicar a un cliente por qué se le avisa?», «¿hay poco presupuesto para mantener el modelo?» o «¿qué le duele más, una cancelación que no vimos venir o una falsa alarma?». Partid de un reparto como **50 % rendimiento, 30 % explicabilidad, 20 % coste** y moved los números según lo que conteste. Tres reglas:

    - Los tres pesos suman **100 %**.
    - Cada peso lleva una **razón que viene del cliente**. Vale: «damos 30 % a la explicabilidad porque el gerente necesita entender por qué se avisa». No vale: «porque sí», «porque es el ejemplo» ni «porque nos salía bien».
    - No dejéis el rendimiento casi a cero: un modelo que no acierta no sirve, y el cuaderno no admite como campeón al modelo de referencia (el que no sabe nada).

5. **Repartir el trabajo.** Un reparto posible (con 3 personas, la persona D no existe y su tarea se reparte entre las demás). **Todas las personas revisan el trabajo de otra:**

    | Persona | Tarea | Paso |
    |---|---|---|
    | A | Modelos de referencia, logística, árbol y bosque en el cuaderno | 2 |
    | B | *Boosting*, SVM y primera búsqueda de hiperparámetros | 3 |
    | C | Segunda búsqueda de hiperparámetros y análisis de sensibilidad | 3 y 4 |
    | D (si hay 4) | *Model card* y README | 5 |

    Acordad también quién es *Scrum Master* y quién responsable técnico en este sprint (los dos roles cambian en cada sprint). Para el cuaderno usaréis **una sola copia compartida** (*Compartir* → permiso de Editor) o una pantalla compartida, y **nunca dos personas en la misma celda a la vez**.

6. **Escribirlo todo en un sitio común.** Una tarjeta del tablero (Trello o similar, columnas *Por hacer → En curso → En revisión → Hecho*) con este texto, con vuestros datos:

    ```text
    Nivel objetivo: estándar
    Pesos (rendimiento / explicabilidad / coste): 50 % / 30 % / 20 %
    Por qué: damos 30 % a la explicabilidad porque el gerente necesita entender por qué se avisa.
    Reparto: A = …, B = …, C = …
    ```

    Y una tarjeta por tarea, cada una con su responsable. Si el planning se queda corto, la justificación se termina de escribir al empezar el día 2.

**Qué deberíais ver.** Una tarjeta (o un mensaje fijado) con el nivel objetivo, los tres pesos que suman 100 % y una frase de por qué para cada uno, y en el tablero una tarjeta por tarea con su responsable. Nada de código ni de resultados todavía.

**Hecho cuando:** los pesos suman 100 %, están justificados con una razón del cliente y cada persona sabe qué le toca.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| No os ponéis de acuerdo en los pesos | Es normal: cada persona valora cosas distintas. | Preguntad al docente (el cliente) qué le importa más. Si sigue el empate, votad y apuntad la razón. |
| Los pesos no suman 100 % | Alguna cifra está mal. | Sumadlos: 50 + 30 + 20 = 100. En el paso 4, el cuaderno dará `AssertionError: Los pesos deben sumar 1` si no suman. |
| Queréis dejar el rendimiento en 0 % | Con casi nada de peso al rendimiento, el modelo de referencia (que no sabe nada) puede acabar con la mejor puntuación, y el cuaderno no lo acepta como campeón. | Dad al rendimiento un peso claro, de 20 % o más. |
| Queréis poner el 100 % a un solo criterio | Es válido, pero entonces no hay compromiso que discutir: gana el mejor en ese criterio. | Justificadlo con una razón del cliente, o repartid el peso entre los tres. |
| No sabéis qué son el AUC, el árbol o el bosque | Es normal: todavía no los habéis usado. | Basta con la tabla de palabras. Hoy solo hay que decidir; los modelos se conocen en los pasos 2 y 3. |
| Sois 3 personas y la tarea D se queda sin dueño | El reparto de la tabla es para 4. | Repartid la *model card* y el README entre las otras tres, y apuntadlo en la tarjeta. |

<!--nav-->
---

[Ficha del reto](Reto_Sprint_08.md) · [Paso 2 →](Reto_Sprint_08_paso_2.md)
<!--/nav-->
