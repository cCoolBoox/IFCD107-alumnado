# Sprint 1 · Reto «Auditoría de oportunidades de IA»

> **Esta es la ficha completa del reto, explicada paso a paso** para quien nunca ha trabajado con esta metodología ni con IA. Léela entera **antes de empezar** y vuelve a ella cuando tengas dudas.
>
> - Si es tu primer reto, lee antes [Cómo se trabaja un reto](../../../material/4.%20Como_se_trabaja_un_reto.md).
> - Volver al [README del sprint](../README.md) · [Guía del sprint en PDF](Guia_Sprint_01.pdf) · [versión ecofriendly para imprimir](Guia_Sprint_01_ecofriendly.pdf).

## Ficha del reto

### En pocas palabras (léelo primero)

**Qué os pide el cliente.** La directora de TurisData no sabe por dónde empezar con la inteligencia artificial. Os pide **un informe corto** que le diga: *qué cinco cosas podría hacer con IA, cuál conviene hacer primero, qué datos necesita y qué riesgos corre.* No quiere códigos ni fórmulas: quiere **un consejo claro para decidir**.

**Importante: en este reto no se programa ni se calcula nada.** Es un trabajo de **pensar, comparar y escribir**. Se parece a lo que hace una persona asesora cuando propone un plan antes de gastar dinero.

**Qué vais a hacer, en cinco pasos:**
1. **Buscar ideas** (unas 8) usando las [tarjetas de casos de uso](../actividades/tarjetas_casos_uso.md) de la práctica.
2. **Quedaros con 5**, de las que al menos 2 tienen que ser inventadas por vosotros.
3. **Describir cada una** en una ficha (hay un [ejemplo resuelto](../actividades/ejemplo_clasificacion_caso.md)): qué problema resuelve, con qué tipo de dato, qué tipo de aprendizaje y qué algoritmo podría servir.
4. **Ordenarlas** por «cuánto ayuda» y «lo fácil que es» (matriz de priorización) y **pasarles un [checklist ético](../plantillas/checklist_etico_v1.md)**.
5. **Escribir el informe** de 2–3 páginas con una recomendación.

**Qué vais a entregar:** el informe (7 apartados) y el [checklist ético](../plantillas/checklist_etico_v1.md) relleno.

**Qué vais a aprender haciéndolo:** a **distinguir** los tipos de IA y de aprendizaje con ejemplos reales, y a **detectar riesgos** (datos personales, sesgos, decisiones automáticas) *antes* de construir nada.

**Cuánto tiempo:** 3 horas de reto, entre el lunes 19/10 y el miércoles 21/10. La review es el último rato del miércoles.

### Palabras que van a aparecer en este reto

| Palabra | Qué significa, en sencillo |
|---|---|
| **Caso de uso** | Una situación concreta donde se podría usar IA: «avisar de qué reservas se cancelarán» |
| **Modalidad** | El tipo de dato con el que trabaja la IA: tablas (datos tabulares), imágenes (visión), texto (lenguaje), sonido (voz) |
| **Aprendizaje supervisado** | La IA aprende con ejemplos que **ya tienen la respuesta** (reservas pasadas con «se canceló: sí/no») |
| **Aprendizaje no supervisado** | La IA busca patrones **sin respuestas**, por ejemplo agrupar clientes parecidos |
| **Familia de algoritmos** | Un tipo de método: árboles, regresiones, redes neuronales, agrupamiento… No hay que saber cómo funcionan por dentro, solo para qué sirven |
| **Matriz de priorización** | Un cuadro de 2 ejes (impacto y facilidad) que ayuda a decidir qué hacer primero |
| **Sesgo** | Cuando la IA trata peor a un grupo de personas porque sus datos de aprendizaje estaban desequilibrados |
| **RGPD** | Ley europea de protección de datos personales |
| **AI Act** | Reglamento europeo de IA: clasifica los sistemas según su riesgo |
| **Semáforo ético** | Verde (se puede avanzar), ámbar (con medidas) o rojo (no avanzar sin cambios) |
| **Piloto** | Una prueba pequeña y barata antes de hacer algo grande |

### Escena del cliente
Tras la entrevista del Sprint 0, la directora de *TurisData Canarias* os pide un **informe de oportunidades**: "No sé por dónde empezar con la IA. Decidme **qué cinco cosas** podría hacer, cuáles tienen sentido primero, qué datos necesito y **qué riesgos** corro. No quiero líos con los datos de mis clientes ni que una máquina decida sin que yo lo sepa". Dispone de un presupuesto limitado para un piloto y de datos de reservas, ocupación y reseñas.

### Qué tenéis que entregar
1. **Informe de oportunidades** (2-3 páginas, en `.md` o PDF) con la estructura de abajo.
2. **Checklist ético (versión 1)** rellenado para **cada uno de los 5 casos** (o completo para los 2 casos priorizados y resumido para los otros 3).

#### Estructura del informe (2-3 páginas)
1. **Resumen ejecutivo** (5-6 líneas): las 5 oportunidades y cuál recomendáis empezar.
2. **Lo que hemos entendido** del cliente (3-4 líneas, con vuestra HMW priorizada del Sprint 0).
3. **Tabla de 5 casos de uso**: nombre, problema de negocio, modalidad, tipo de aprendizaje, familia de algoritmos, **datos necesarios** (y si existen), métrica de éxito.
4. **Priorización:** matriz impacto × facilidad, con criterio explicado.
5. **Riesgos y checklist ético:** el semáforo de cada caso y las medidas para los riesgos principales.
6. **Recomendación y siguientes pasos:** qué piloto, con qué datos y qué necesitamos del cliente.
7. **Límites de este informe:** qué no hemos podido comprobar.

### Datos y recursos
- Notas de la entrevista y mapa de empatía del Sprint 0.
- Las **22 tarjetas** de la dinámica A (podéis elegir de ahí, adaptar o inventar casos nuevos, **al menos 2 propios**).
- [`ejemplo_clasificacion_caso.md`](../actividades/ejemplo_clasificacion_caso.md) y [`checklist_etico_v1.md`](../plantillas/checklist_etico_v1.md).
- No hay datos que analizar todavía: esta auditoría es de **ideas y riesgos**, no de resultados.

### Restricciones
- **Tiempo:** 3 h de reto en clase (dentro de las 15 h del sprint).
- **Extensión:** 2-3 páginas de informe (sin contar el checklist).
- **Presupuesto orientativo del cliente:** hasta 15.000 € para un piloto; nada de proyectos eternos.
- **Los 5 casos** deben cubrir **al menos 3 modalidades** distintas y **al menos 1** no debe requerir IA (o debe resolverse mejor con reglas) para mostrar criterio.
- Uso de asistentes de IA generativa permitido, con **declaración** de dónde se ha usado y qué habéis verificado.

### Criterios de evaluación
Cada entregable se evalúa de 0 a 4 en los cuatro criterios de la rúbrica de retos.

| Criterio | 1 · Insuficiente | 2 · Suficiente | 3 · Bueno | 4 · Excelente |
|---|---|---|---|---|
| **Corrección técnica** | Confunde modalidad, tipo de aprendizaje o datos en varios casos | Clasificaciones correctas con fallos menores | Clasificaciones correctas y justificadas; datos concretos | Además compara alternativas (p. ej. reglas frente a modelo) y detecta riesgos técnicos (fuga de datos, desbalance) |
| **Reproducibilidad** | No se entiende cómo se llegó a las conclusiones | Se entiende con ayuda | El informe deja claro el criterio de priorización y las fuentes | Además el checklist y el informe están versionados en el repositorio del equipo |
| **Análisis y comunicación al cliente** | Jerga sin explicar o lista de ideas sin priorizar | Ideas con interpretación básica | Recomendación clara y comprensible para la dirección | Recomendación accionable con próximos pasos, datos necesarios y límites explicados |
| **IA responsable** | No se considera | Menciones genéricas ("hay que cumplir el RGPD") | Riesgos específicos por caso | Medidas concretas por caso y criterio para decidir el semáforo |

### Pasos sugeridos (3 h de reto, repartidas por días)

| Momento | Qué hacer |
|---|---|
| **Lunes 19/10 · planning (30 min)** | Leed la ficha, repartid el trabajo en el tablero, definid la estructura del informe |
| **Martes 20/10 (30 min)** | Lluvia de ideas con las tarjetas y elección de 8 candidatos; descartad hasta quedaros con 5 casos (al menos 2 propios) |
| **Miércoles 21/10 (1 h)** | Fichas de los 5 casos (usad el ejemplo resuelto), checklist ético v1 (completo en los 2 casos priorizados y resumido en el resto), matriz de priorización y redacción del informe; revisión cruzada y DoD. **Lo que no cabra, lo terminaréis dentro de vuestro tiempo de trabajo del equipo, antes del Sprint 2** |
| **Miércoles 21/10 · última hora** | Review de 5 min por equipo y retro |

Entre medias, aprovechad los ratos de las prácticas (mapa de casos, debate) para adelantar el informe: las tarjetas y el checklist son la materia prima.

### Guía paso a paso para principiantes

#### Paso 1 · Planning y reparto (lunes 19/10, 30 minutos)
1. Leed la ficha entera. Una persona lee, el resto subraya lo que no entiende.
2. **Repartid las partes del informe** (7 apartados). Una persona puede encargarse de 1 o 2 apartados, pero **todas leen todo al final**.
3. Pasad al tablero las tareas: «Elegir 8 tarjetas», «Fichas de casos», «Matriz», «Checklist ético», «Redacción», «Revisión cruzada».

#### Paso 2 · Lluvia de ideas (martes 20/10, 30 minutos)
1. Poned sobre la mesa las **22 tarjetas** de la dinámica A ([`tarjetas_casos_uso.md`](../actividades/tarjetas_casos_uso.md)).
2. Cada persona elige 2 o 3 que le parezcan **útiles para TurisData** (no para cualquier empresa). Pensad en los dolores que contó el cliente en el Sprint 0.
3. Quedaos con **8 candidatos** y luego **descartad hasta 5**. Apuntad **por qué** descartáis las otras tres: lo contaréis en la review.
4. **Inventad al menos 2 casos propios.** Un truco: recordad una frustración del cliente («las reseñas son miles y nadie las lee») y preguntad «¿se podría ayudar con IA?».
5. **Incluid un caso que no necesite IA**, o que se resuelva mejor con una regla sencilla (por ejemplo, «enviar un recordatorio 48 h antes de que caduque la cancelación gratuita»). Saber decir «aquí no hace falta IA» demuestra criterio.

#### Paso 3 · Fichas de los 5 casos (miércoles 21/10, primera parte)
Para cada caso rellenad una ficha como la del ejemplo resuelto ([`ejemplo_clasificacion_caso.md`](../actividades/ejemplo_clasificacion_caso.md)). Un **mini-ejemplo** de cómo se responde, caso «Resumen automático de reseñas»:

| Campo | Cómo se rellena (ejemplo) |
|---|---|
| Problema de negocio | La dirección recibe cientos de reseñas y no las lee. Se pierden quejas repetidas |
| Modalidad | **Texto** (lenguaje) |
| Tipo de aprendizaje | Podría ser **supervisado** (si hay reseñas ya etiquetadas con «positiva/negativa») o usar un modelo de lenguaje ya preentrenado |
| Familia de algoritmos | Clasificación de texto o modelos de lenguaje |
| Datos necesarios | Reseñas de huéspedes (texto + puntuación). **¿Existen?** Sí, el cliente tiene reseñas, pero conviene revisar si incluyen nombres |
| Métrica de éxito | % de quejas repetidas detectadas; tiempo que ahorra la dirección |

**Truco para no equivocarse con el tipo de aprendizaje:** preguntaos *«¿tengo ya ejemplos del pasado con la respuesta correcta?»*. Si **sí** → supervisado. Si **no** y quiero agrupar o detectar rarezas → no supervisado.

#### Paso 4 · Matriz de priorización y lista de comprobación ética (miércoles 21/10, segunda parte)
1. **Matriz impacto × facilidad:** poned cada caso en un cuadro con dos ejes de 1 a 5. Arriba a la derecha (mucho impacto y fácil) es lo que haríais primero. **Explicad vuestro criterio** («facilidad = tenemos los datos y el plazo es corto»).
2. **Checklist ético** ([`checklist_etico_v1.md`](../plantillas/checklist_etico_v1.md)): responded Sí / No / No aplica / No lo sé a cada pregunta y escribid una **evidencia o una acción**. Rellenadlo **completo para los 2 casos priorizados** y resumido para los otros 3.
3. Poned un **semáforo** a cada caso y justificadlo en una línea.

#### Paso 5 · Redacción, revisión y cierre
1. Escribid el **resumen ejecutivo** el último, cuando ya sepáis qué recomendáis (5–6 líneas: «Recomendamos empezar por X porque…»).
2. **Revisión cruzada:** otra persona del equipo lee el informe *como si fuera la directora* y subraya lo que no entiende.
3. Subid todo al repositorio, repasad la Definition of Done y rellenad autoevaluación y coevaluación.
4. Preparad la review de 5 minutos (ver más abajo).

### Cómo usar la IA en este reto

Aquí la IA puede ser un **buen compañero de lluvia de ideas** y un **revisor de estilo**, pero cuidado: **inventa con mucha seguridad**.

| Para qué | Ejemplo de petición | Qué tenéis que comprobar |
|---|---|---|
| Generar ideas | «Soy consultor de IA y mi cliente es una empresa de alojamientos turísticos en Canarias con datos de reservas, ocupación y reseñas. Dame 10 posibles usos de IA, cada uno con el problema que resuelve» | Que cada idea sea realista **con los datos que tiene el cliente**; descartad las que no |
| Entender un término | «Explícame la diferencia entre aprendizaje supervisado y no supervisado con un ejemplo de hoteles» | Que podáis explicarlo vosotros sin mirar |
| Revisar el texto | «Revisa este resumen ejecutivo: ¿hay jerga que una directora no entendería? Marca las frases y propón cambios, sin añadir información nueva» | Que no haya añadido cifras ni datos que no estaban |
| Buscar riesgos | «Para este caso de uso (…) dime 5 riesgos de datos personales y sesgos que debería considerar» | Contrastadlos con el checklist; **no los copiéis sin entender** |

**Qué NO hacer:** pedirle «hazme el informe entero». Perderéis el aprendizaje y, además, el informe será genérico, sin las notas de la entrevista.

**Declaración de uso (obligatoria):** una línea al final del informe, por ejemplo: *«Hemos usado [herramienta] para generar ideas de casos y revisar la redacción; hemos descartado X ideas por falta de datos y hemos comprobado a mano las clasificaciones»*.

**Sobre el AI Act:** si citáis artículos o fechas del reglamento, **comprobad la fecha en la fuente oficial**; las IA se equivocan mucho con ellas. Añadid la advertencia «verificar calendario vigente».

### Errores frecuentes (y cómo evitarlos)

| Error | Por qué ocurre | Cómo evitarlo |
|---|---|---|
| Cinco casos casi iguales | Todos piensan en «predecir cancelaciones» | Cubrid **al menos 3 modalidades** distintas (tablas, texto, imágenes…) |
| Confundir modalidad con tipo de aprendizaje | Suenan parecido | Modalidad = **tipo de dato**. Aprendizaje = **cómo aprende** |
| Ningún caso sin IA | Se piensa que «más IA = mejor» | Incluid uno que se resuelva con reglas y explicad por qué |
| Checklist ético con «cumplir el RGPD» | Frases genéricas | Un **riesgo específico por caso** («las reseñas pueden contener nombres de personas») |
| Jerga sin explicar | Se escribe para el docente | Releed como si fuerais la directora: ¿se entiende «modalidad»? |
| Priorizar «a ojo» | Falta criterio | Escribid una frase que explique **por qué** cada caso está donde está |

### Un buen resultado se parece a…

- **Resumen ejecutivo:** «Recomendamos empezar por un aviso de riesgo de cancelación porque ataca el problema más caro (habitaciones vacías de última hora), los datos ya existen y el riesgo ético es medio y controlable».
- **Tabla de casos:** cinco filas completas, con una columna de «datos necesarios» que dice si **ya existen** o no.
- **Riesgo específico bien escrito:** «El país de origen podría actuar como sustituto indirecto de la nacionalidad; se propone no usarlo para decidir depósitos».
- **Límites:** «No hemos podido comprobar si las reseñas contienen datos personales».

### Antes de entregar: autoevaluación rápida

| Pregunta | Sí / No |
|---|---|
| ¿Los 7 apartados del informe están, en 2–3 páginas? | |
| ¿Hay 5 casos con modalidad, aprendizaje, familia de algoritmos y datos? | |
| ¿Al menos 3 modalidades y 2 casos propios? | |
| ¿Hay un caso que no necesita IA, justificado? | |
| ¿Cada caso tiene al menos 1 riesgo específico en el checklist? | |
| ¿Otra persona ha leído el informe y entiende la recomendación? | |
| ¿Hay declaración de uso de IA? | |

### Si os atascáis

- **No se nos ocurren casos propios:** pensad en una frase de la entrevista del Sprint 0 y preguntaos «¿qué haría una persona para resolver esto hoy?». Ahí suele haber un caso.
- **No sabemos qué familia de algoritmos poner:** usad la dinámica C de las tarjetas (6 problemas con sus familias) como chuleta.
- **El informe sale largo:** el límite es 2–3 páginas **sin contar el checklist**. Pasad detalles a un anexo.
- Más ayuda: [Cómo se trabaja un reto](../../../material/4.%20Como_se_trabaja_un_reto.md).

### Qué se enseña en la review (5 min por equipo)
- La **recomendación** en una frase y por qué la primera prioridad.
- **Un caso que descartasteis** y por qué (por riesgo, por datos o por falta de valor).
- El **semáforo ético** de vuestro caso principal y la medida más importante.
- Una duda que queda abierta para el cliente.

## Definition of Done (lista de comprobación)

Si queda una casilla sin marcar, **el reto no está terminado**.

- [ ] Informe de 2-3 páginas con las 7 secciones
- [ ] 5 casos con modalidad, tipo de aprendizaje, familia y datos necesarios
- [ ] Al menos 3 modalidades distintas y 2 casos propios
- [ ] Al menos un caso que no requiere IA (o se resuelve mejor con reglas), justificado
- [ ] Matriz de priorización con criterio explicado
- [ ] Checklist ético v1 de cada caso, con al menos 1 riesgo específico por caso
- [ ] Referencias al AI Act con la advertencia de verificar el calendario vigente
- [ ] Revisado por otra persona; declaración de uso de IA generativa
- [ ] Subido a Git / repositorio del equipo; tablero actualizado
- [ ] Autoevaluación y coevaluación rellenadas
