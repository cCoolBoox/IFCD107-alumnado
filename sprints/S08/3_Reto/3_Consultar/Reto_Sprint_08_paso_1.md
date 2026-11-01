# Paso 1 · Planning y pesos de los criterios (día 1, 20 minutos)

<!--nav-->
> Sprint 8 · Reto «Duelo de modelos» · paso 1 de 5 · [Ficha del reto](Reto_Sprint_08.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_08_una_pagina.md) · [Paso 2 →](Reto_Sprint_08_paso_2.md)
<!--/nav-->

1. Repartir roles y tareas, y apuntarlas en el tablero.
2. Leer esta ficha y decidir hasta qué nivel queréis llegar (🟢, 🟡 o 🔴).
3. Acordar los **pesos** de los tres criterios con la «voz del cliente» (el docente) y justificarlos.
4. Escribir los pesos y su justificación en un sitio común: los usaréis en los pasos 4 y 5.

**Cómo se hace**
- **Los tres criterios.** Cada modelo se puntúa en tres cosas, y vosotros decidís cuánto vale cada una (los pesos suman 100 %):

| Criterio | Qué mide | Peso (ejemplo) |
|---|---|---|
| **Rendimiento** | El AUC en validación cruzada, con su desviación (media ± desviación) | 50 % |
| **Explicabilidad** | ¿Puede el gerente entender **por qué** el modelo avisa? Se puntúa de 1 (caja negra) a 5 (se lee directamente) | 30 % |
| **Coste** | Tiempo de entrenamiento y de predicción, tamaño del modelo y esfuerzo de mantenimiento | 20 % |

- **Justificarlos.** Los pesos son vuestros; lo importante es que tengan una razón. Preguntad al docente (que hace de cliente): «¿Necesita el gerente explicar a un cliente por qué se le avisa?», «¿hay poco presupuesto para mantener el modelo?». Ejemplo de frase: «Damos 30 % a la explicabilidad porque el gerente necesita entender por qué se avisa».
- **Repartir el trabajo.** Un reparto posible (con 3 personas, la persona D no existe y su tarea se reparte):

| Persona | Tarea | Paso |
|---|---|---|
| A | Modelos de referencia, lineal, árbol y bosque en el cuaderno | 2 |
| B | *Boosting*, SVM y primera búsqueda de hiperparámetros | 3 |
| C | Segunda búsqueda de hiperparámetros y análisis de sensibilidad | 3 y 4 |
| D (si hay 4) | *Model card* y README | 5 |

Todos revisan el trabajo de otra persona. Para el cuaderno, usad **una sola copia compartida** (Compartir → editor) o una pantalla compartida, y no editéis la misma celda a la vez.

**Palabras que vais a usar.**

| Palabra | Qué significa, en sencillo |
|---|---|
| ***Leaderboard*** | La tabla de clasificación de los modelos, con sus resultados |
| **Familia de modelos** | Un tipo de modelo: árbol, bosque, *boosting*, SVM, lineal… |
| **Hiperparámetro** | Un ajuste que hacéis vosotros **antes** de entrenar (la profundidad del árbol, el número de árboles…) |
| **Validación cruzada** | Evaluar varias veces con particiones distintas del *train* para tener una medida fiable |
| **AUC** | Nota de 0,5 (como el azar) a 1 (perfecto): cómo de bien separa las reservas que se cancelan de las que no |
| **Explicabilidad** | Poder decir **por qué** el modelo toma una decisión |
| ***Model card*** | La «ficha técnica» del modelo: usos, datos, métricas, límites y riesgos |
| **Deriva** | Cuando los clientes cambian su comportamiento con el tiempo y el modelo deja de funcionar bien |

**Qué deberíais ver.** Los pesos escritos (por ejemplo, 50 / 30 / 20) con una frase de por qué, las tareas en el tablero y el nivel objetivo acordado.

**Hecho cuando:** los pesos suman 100 %, están justificados y cada persona sabe qué le toca.

<!--nav-->
---

[Ficha del reto](Reto_Sprint_08.md) · [Paso 2 →](Reto_Sprint_08_paso_2.md)
<!--/nav-->
