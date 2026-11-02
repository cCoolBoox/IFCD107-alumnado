# Sprint 1 · Reto «Auditoría de oportunidades de IA» · Entrega y rúbrica

> **Qué se sube y cómo se evalúa.** Se lee **una vez**, antes de entregar, y se vuelve a la rúbrica cuando el equipo revisa su trabajo. Mientras trabajáis no hace falta: para eso está [el reto en una página](../1_Trabajar/Reto_Sprint_01_una_pagina.md).
>
> - Volver al [README del sprint](../../README.md) · [ficha del reto](../3_Consultar/Reto_Sprint_01.md), para consultar.
> - Vuestra hoja personal: [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md).
> - Cómo subir a GitHub paso a paso, con capturas: [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md).

Esta hoja responde a **dos preguntas distintas**, una tabla para cada una:

**Tabla A · Los ficheros:** qué ficheros hay, de dónde sale cada uno (ya hecho, lo modificáis, lo creáis o lo genera el programa) y **cuáles se suben y adónde**.

**Tabla B · Los requisitos:** qué tiene que cumplir lo que entregáis y hasta dónde llegar (🟢 mínimo, 🟡 estándar, 🔴 extra). **Es lo que se evalúa.**

**En total, al final del sprint se suben a `sprint-01/`:** **2 ficheros del equipo** (`informe_oportunidades.md`, `checklist_etico.md`) **+ 1 autoevaluación y coevaluación por persona**, es decir, **2 + tantos ficheros como personas haya en el equipo** (un equipo de 3 sube 5). «El reto» no es un fichero aparte: es **el informe** (con la tabla de casos, la priorización, la recomendación, la declaración de uso de IA y la revisión con la rúbrica dentro) **más el checklist ético** de los casos. La *review* y la *retro* se hacen de palabra: no se suben.

## 1 · 📦 Tabla A · Los ficheros: de dónde sale cada uno y cuáles se suben

Todo lo que se sube va al repositorio privado del equipo (`ifcd107-equipo-…`), en la carpeta **`sprint-01/`**.

| Fichero | Origen | Qué hacéis vosotros | ¿Se sube? |
|---|---|---|---|
| `informe_oportunidades.md` | **Lo creáis a partir de una plantilla.** Os damos `plantilla_informe_oportunidades.md` con los siete apartados | Copiarla con ese nombre (botón *Raw*), rellenar los apartados en 2 o 3 páginas, borrar las notas en cursiva y anotar al final la «Revisión con la rúbrica». También vale un PDF (con la revisión en su última página) | **Sí** · `sprint-01/` |
| `checklist_etico.md` | **Lo creáis a partir de una plantilla.** Os damos `checklist_etico_v1.md` | Copiar su formulario una vez por caso, con el nombre del caso como título: **completo** en los 2 casos priorizados y **resumido** en los otros 3 | **Sí** · `sprint-01/` |
| Fichas de los casos (hoja de trabajo) | **Las creáis** siguiendo el modelo `ejemplo_clasificacion_caso.md` | Una ficha por caso (la del quinto, breve); su contenido pasa a la tabla del informe | **No se suben** |
| Lista de las 8 candidatas, descartes y matriz dibujada | **Lo creáis** en papel, pizarra o tablero | Servirse de ello para decidir y para la *review*; no hay formato | **No se suben** |
| Autoevaluación y coevaluación (`autoevaluacion_nombre.md`) | **Ya hecha, en blanco** | Cada persona copia la plantilla con su nombre y la rellena; la coevaluación va **dentro del mismo fichero** | **Sí**, **una por persona** (no una por equipo) · `sprint-01/` |

---

## 2 · ✅ Tabla B · Los requisitos: qué tiene que cumplir y hasta dónde llegar

| Requisito | Qué se pide exactamente | Nivel | Dónde se comprueba |
|---|---|---|---|
| **Informe de siete apartados** | Resumen ejecutivo (5–6 líneas), lo que hemos entendido, tabla de casos, priorización, riesgos y checklist, recomendación y límites; 2–3 páginas sin contar el checklist | 🟢 Mínimo | `informe_oportunidades.md` |
| **Cinco casos clasificados** | Tabla con nombre, problema, modalidad, tipo de aprendizaje, familia de algoritmos y datos necesarios (y si existen) en los cinco casos; la métrica de éxito, en cuatro (el quinto puede ir en versión breve, sin métrica) | 🟢 Mínimo | `informe_oportunidades.md` (apartado 3) |
| **Mezcla de casos** | Al menos 3 modalidades distintas, al menos 2 casos propios y al menos 1 caso que no necesita IA (o va mejor con reglas), con su motivo | 🟢 Mínimo | `informe_oportunidades.md` (apartado 3) |
| **Matriz de priorización** | Los cinco casos puntuados de 1 a 5 en impacto y facilidad, con el criterio escrito | 🟢 Mínimo | `informe_oportunidades.md` (apartado 4) |
| **Checklist ético** | Completo en los 2 casos priorizados; en los otros 3, ficha rápida, preguntas (★) y semáforo con una línea de justificación | 🟢 Mínimo | `checklist_etico.md` |
| **Recomendación** | Qué piloto recomendáis, con qué datos y qué necesitáis del cliente | 🟢 Mínimo | `informe_oportunidades.md` (apartados 1 y 6) |
| **Uso de IA** | Una línea al final del informe: si se ha usado IA, para qué y qué se comprobó a mano | 🟢 Mínimo | `informe_oportunidades.md` (apartado «Uso de IA») |
| **Subida a GitHub** | Los ficheros están en `sprint-01/` y los suben **personas distintas**, cada una con su cuenta | 🟢 Mínimo | Carpeta `sprint-01/` y su historial |
| **Métrica y datos concretos en los cinco casos** | Cada caso dice cómo se medirá el éxito, en palabras que entienda el cliente («habitaciones vacías evitadas»), y qué datos hacen falta, concretos y no «datos del cliente» | 🟡 Estándar | `informe_oportunidades.md` (apartado 3) |
| **Criterio de priorización explicado** | Una frase por caso que explique por qué está donde está, y el criterio general | 🟡 Estándar | `informe_oportunidades.md` (apartado 4) |
| **Riesgos específicos** | Al menos un riesgo específico de ese caso, con su medida, en cada uno de los cinco; la clasificación del AI Act, con la advertencia «verificar calendario vigente» | 🟡 Estándar | `checklist_etico.md` y `informe_oportunidades.md` (apartado 5) |
| **Uso de IA (completo)** | La declaración dice **qué se pidió, qué se comprobó a mano y qué se descartó** | 🟡 Estándar | `informe_oportunidades.md` |
| **Revisión y autoevaluación** | Alguien que **no escribió esa parte** revisa el informe con la rúbrica (justo debajo de estas tablas) y anota nivel y prueba en «Revisión con la rúbrica»; cada persona sube su hoja de autoevaluación y coevaluación; el equipo hace la review y la retro | 🟡 Estándar | `informe_oportunidades.md` (último apartado) y `sprint-01/` |
| **Fichas y checklist de los cinco casos** | Las cinco fichas y los cinco checklists **completos** (también el quinto y los tres no priorizados) | 🔴 Extra | `informe_oportunidades.md` y `checklist_etico.md` |
| **Alternativas y riesgos técnicos** | En algún caso, comparar una regla sencilla con un modelo y señalar un riesgo técnico (fuga de datos, datos desbalanceados) | 🔴 Extra | `informe_oportunidades.md` (apartado 3) y `checklist_etico.md` |
| **Recomendación accionable** | Siguientes pasos concretos (quién y qué), datos necesarios y límites explicados, dentro de los 15.000 € del piloto | 🔴 Extra | `informe_oportunidades.md` (apartados 6 y 7) |
| **Medidas concretas y criterio del semáforo** | Cada caso con medidas concretas y el criterio con el que se decidió su semáforo; el historial muestra al menos una corrección hecha tras la revisión cruzada | 🔴 Extra | `checklist_etico.md` y el historial del repositorio |

---

## 3 · 🧭 Rúbrica del reto · cómo se puntúa y cómo se revisa

La usan **dos veces**: el equipo, para revisar su propio trabajo antes de entregar (es lo que dice la *Definition of Done*), y el docente, para puntuar el sprint. Se mira **cada criterio por separado** y se pone el nivel de la columna cuyo texto **se cumple entero**: si lo de un nivel se cumple a medias, es el nivel de abajo. **0** significa que no se ha entregado nada de ese criterio.

Orientación: lo que pide el nivel 🟢 mínimo sale en un **2**, el 🟡 estándar en un **3** y los 🔴 extras en un **4**.

| Criterio | 1 · Empezado | 2 · Mínimo | 3 · Estándar | 4 · Extra |
|---|---|---|---|---|
| **Corrección técnica** (¿están bien clasificados los casos?) | En varios casos se confunde modalidad (tipo de dato) con tipo de aprendizaje, o faltan casos o datos necesarios | Los cinco casos están clasificados (modalidad, aprendizaje, familia y datos, con si existen) con fallos menores; hay 3 modalidades, 2 casos propios y 1 sin IA | Clasificaciones correctas y **justificadas** (una frase de por qué ese aprendizaje y esa familia); los datos son concretos (qué información hace falta, no «datos del cliente») y cada caso tiene métrica | Además compara una regla con un modelo y señala riesgos técnicos (fuga de datos, datos desbalanceados) |
| **Reproducibilidad** (¿se entiende cómo se llegó a la conclusión?) | No se entiende por qué se recomienda ese caso, o los ficheros no están en `sprint-01/` | El informe y el checklist están en `sprint-01/` y, con ayuda de quien los escribió, se entiende cómo se eligió el caso recomendado | El informe deja claro el **criterio de priorización** y de dónde sale cada idea o dato (tarjeta, entrevista del Sprint 0, apuntes); hay *commits* de varias personas | Además el historial muestra versiones del informe y del checklist, con al menos una corrección hecha tras la revisión cruzada |
| **Análisis y comunicación al cliente** (¿lo entiende la directora?) | Hay jerga sin explicar o una lista de ideas sin priorizar | Las ideas están priorizadas y el resumen dice qué se recomienda, aunque quede alguna palabra técnica sin explicar | La recomendación es **clara y comprensible para la dirección**: qué piloto, por qué ese primero, qué datos y qué riesgo, sin jerga | Además es accionable: siguientes pasos con responsable, datos necesarios y límites explicados, dentro del presupuesto del piloto |
| **IA responsable** (¿se sabe qué hizo la IA y qué riesgos hay?) | No se consideran los riesgos o no se dice si se ha usado IA | Hay checklist y declaración de uso de IA, pero los riesgos son genéricos («hay que cumplir el RGPD») | **Riesgos específicos en cada caso**, con su medida; AI Act con la advertencia «verificar calendario vigente»; la declaración dice qué se pidió y qué se comprobó a mano | Además cada caso tiene medidas concretas y el informe explica el criterio con el que se decidió cada semáforo |

**Cómo se revisa** (unos 10 minutos, antes de la *review*; lo hace **una persona que no escribió esa parte**):

1. **Leer el informe como si fuera la directora**: ¿se entiende la recomendación sin preguntar? Subrayar cada palabra técnica que no se explique.
2. **Comprobar las clasificaciones** de cada caso con las tarjetas y los apuntes: ¿la modalidad es un tipo de dato? ¿El tipo de aprendizaje responde a «¿hay ejemplos del pasado con la respuesta?»? ¿Hay 3 modalidades, 2 casos propios y 1 sin IA?
3. **Abrir el checklist y leer los riesgos**: ¿cada caso tiene uno que **solo vale para ese caso**? Si valdría para cualquier otro, es genérico. Mirad también que haya semáforo y justificación.
4. **Poner un nivel (1 a 4) en cada criterio, con una frase de prueba** (por ejemplo: «3 · la priorización está explicada, pero falta el riesgo específico del caso 4»; «2 · las ideas están priorizadas, pero el resumen usa “modalidad” sin explicarla»). Sin prueba escrita, el nivel no vale.
5. **Apuntar el resultado** en el último apartado del `informe_oportunidades.md` («Revisión con la rúbrica») y corregir lo más fácil de arreglar. Lo demás se anota como mejora.

Cada persona, además, se puntúa a sí misma en su hoja de [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md) con **esta misma rúbrica**.
