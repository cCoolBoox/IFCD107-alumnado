# README Sprint S01 · Qué es la IA, cómo aprende y cómo usarla bien

**Pregunta guía:** ¿dónde puede ayudar la IA al cliente y qué riesgos tiene?  
**Fechas:** mar 20/10 – mié 21/10 · **Horas:** 12 h (4 h teoría · 3 h práctica · 5 h PBL, con 1 h para cerrar el Sprint 0)

📄 **Para imprimir:** todos los documentos del sprint en PDF, a color y ecofriendly, están juntos en la carpeta [`pdf/`](pdf/) (descárgalos para que funcionen los enlaces).

> **Sigue el orden de arriba abajo y abre solo lo que pone en cada fila.** Los demás documentos del sprint son para consultar si te atascas (apartado «Si te atascas»). Si el tiempo aprieta, haz solo lo que pone en las filas de cada día: lo demás es para casa.

## Qué aprenderás

1. Explicar qué es la IA y distinguir IA, machine learning, deep learning e IA generativa, con sus **modalidades** (visión, lenguaje, voz, recomendación, generativa) y casos de uso reales.
2. Describir las **familias de algoritmos**, el ciclo de vida de un proyecto (CRISP-DM) y elegir una familia razonable ante un problema.
3. Distinguir aprendizaje **supervisado, no supervisado, por refuerzo** y preentrenado, y entender el **sobreajuste** y por qué se separan los datos de entrenamiento, validación y test.
4. Identificar riesgos de **sesgo, privacidad, transparencia, desinformación y decisiones automatizadas**, y conocer lo esencial de RGPD y del AI Act.
5. Aplicar un **checklist ético** a un caso y priorizar oportunidades de IA para un cliente.

## Antes de empezar
Haber cursado el Sprint 0 (equipo, tablero y entrevista al cliente TurisData). No hace falta Python ni matemáticas.

## Día 1 · Martes 20/10

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 🎯 Reto · **Cierre del Sprint 0** (lo que quedó pendiente del reto): acuerdo de trabajo y lista de «terminado», entrevista al cliente en grupo grande (antes, 10 min en equipo para preparar las preguntas con la plantilla del mapa a la vista), después el mapa de empatía de TurisData con lo oído y retro corta. **Si aún no tenéis tablero**, montadlo con la guía rápida de Trello (15 min, en casa o en este bloque) | [acuerdo de trabajo y lista de «terminado»](../S00/Reto_S00/plantillas_equipo.md) | 40 |
| ☐ | 🔔 Ceremonia · Planning del Sprint 1: leed la ficha del reto y repartid los 7 apartados del informe | — | 10 |
| ☐ | 📖 Teoría · Introducción a la IA: modalidades, casos de uso y mitos | [Presentación S01_01](1_Teoria/S01_01_presentacion_Introduccion_a_la_IA.pdf) | 25 |
| ☐ | 💻 Práctica · Dinámica A: tarjetas de casos de uso (11 tarjetas) | [tarjetas casos uso](2_Practica/tarjetas_casos_uso.md) | 25 |
| ☐ | 📖 Teoría · Panorama de algoritmos y CRISP-DM | [Presentación S01_02](1_Teoria/S01_02_presentacion_Algoritmos_y_CRISP-DM.pdf) | 25 |
| ☐ | 💻 Práctica · Dinámica C: elegir la familia de algoritmos en 3 de los 6 problemas (con el docente) | — | 15 |
| ☐ | 📖 Teoría · Tipos de aprendizaje, entrenamiento/validación/test y sobreajuste | [Presentación S01_03](1_Teoria/S01_03_presentacion_Tipos_de_aprendizaje_y_sobreajuste.pdf) | 25 |
| ☐ | 💻 Práctica · Dinámica B: clasificación «a mano» (demostración en la pizarra) | [ejemplo clasificacion caso](2_Practica/ejemplo_clasificacion_caso.md) | 10 |
| ☐ | 🎯 Reto · Lluvia de ideas y elección de casos (paso 2) | [Reto en una página](3_Reto/1_Trabajar/Reto_Sprint_01_una_pagina.md) | 25 |

**En clase: 3 h 20 min.**

**Al acabar el día, deberías poder decir:**

- [ ] El Sprint 0 está cerrado: acuerdo de trabajo, «terminado» y mapa de empatía en el repositorio del equipo.
- [ ] Sé distinguir aprendizaje supervisado, no supervisado y por refuerzo.
- [ ] Mi equipo tiene sus 5 casos de uso candidatos (al menos 2 propios y 1 que no necesita IA).

## Día 2 · Miércoles 21/10

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 📖 Teoría · IA responsable: ética, sesgo, gobernanza de datos, RGPD, AI Act y lista de comprobación ética | [Presentación S01_04](1_Teoria/S01_04_presentacion_IA_responsable.pdf) | 50 |
| ☐ | 💻 Práctica · Debate de casos éticos con roles (2 de los 5 casos) | [casos debate ia responsable](2_Practica/casos_debate_ia_responsable.md) | 25 |
| ☐ | 🎯 Reto · Fichas de 4 casos (el 5.º, en versión breve), lista de comprobación ética (completa en los 2 casos priorizados), matriz de priorización y redacción (pasos 3–5) | [Reto en una página](3_Reto/1_Trabajar/Reto_Sprint_01_una_pagina.md) | 75 |
| ☐ | 🔔 Ceremonia · Entrega en `sprint-01/`, autoevaluación y coevaluación, review (5 min por equipo) y retrospectiva | — | 50 |

**En clase: 3 h 20 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Informe de oportunidades y checklist ético subidos a `sprint-01/` de mi repo.
- [ ] Autoevaluación y coevaluación rellenadas.

## El reto en pocas palabras

**Qué os pide el cliente.** La directora de TurisData no sabe por dónde empezar con la inteligencia artificial. Os pide **un informe corto** que le diga: *qué cinco cosas podría hacer con IA, cuál conviene hacer primero, qué datos necesita y qué riesgos corre.* No quiere códigos ni fórmulas: quiere **un consejo claro para decidir**, con hasta 15.000 € para un piloto.

**Qué vais a entregar:** el informe de oportunidades (siete apartados, 2 o 3 páginas) y el checklist ético, en `sprint-01/`; cada persona sube además su autoevaluación y coevaluación.

**Núcleo y extra.** Núcleo: las fichas de 4 casos (el quinto, en versión breve), la matriz de priorización y el checklist ético completo en los 2 casos priorizados. Extra: fichas y checklist completos en los 5 casos.

Para trabajar: [reto en una página](3_Reto/1_Trabajar/Reto_Sprint_01_una_pagina.md). Para entregar: [qué se sube y rúbrica](3_Reto/2_Entregar/entrega_y_rubrica.md). Para consultar: [ficha del reto](3_Reto/3_Consultar/Reto_Sprint_01.md) (qué pide el cliente, ayudas y errores frecuentes) y [cada paso explicado](3_Reto/3_Consultar/).

## ✅ Antes de cerrar el sprint (Definition of Done)

**Archivos subidos en el repositorio del equipo, carpeta `sprint-01/`** (marca cada uno cuando lo veas en GitHub):
- [ ] `informe_oportunidades.md` · lo creáis a partir de una plantilla
- [ ] `checklist_etico.md` · lo creáis a partir de una plantilla
- [ ] `autoevaluacion_nombre.md` · **uno por persona** (la coevaluación va dentro del mismo fichero): [plantilla](3_Reto/2_Entregar/autoevaluacion_y_coevaluacion.md)

**Total en `sprint-01/`: 2 ficheros del equipo + 1 hoja por persona** (un equipo de 3 sube 5). Los extras solo si los hacéis. La *review* y la *retro* no se suben.

**Comprobaciones antes de dar el sprint por cerrado:**
- [ ] Informe de 2-3 páginas con 5 casos y matriz de priorización
- [ ] Checklist ético v1 con al menos 1 riesgo específico por caso
- [ ] Revisado por otra persona y declaración de uso de IA hecha
- [ ] Tablero actualizado
- [ ] Alguien que **no escribió esa parte** ha revisado el entregable con la [rúbrica](3_Reto/2_Entregar/entrega_y_rubrica.md) y lo ha anotado en el propio entregable

## En casa (cuando puedas)

- Los ejercicios de cada cuaderno que **no** se hacen en clase. Se autocorrigen, y debajo llevan una «Solución de referencia» plegada por si te quedas atascado.
- Si quieres repasar la teoría con calma: [apuntes del sprint](1_Teoria/apuntes/apuntes_ia_conceptos_y_etica.md).

## Si te atascas

1. Lee primero la parte «Si os atascáis» de la [ficha completa del reto](3_Reto/3_Consultar/Reto_Sprint_01.md).
2. Pregunta a tu equipo y, después, al docente. Si usas IA, cuenta en el README qué te dijo y qué comprobaste.

## Todo el material, por carpetas

Las carpetas están **numeradas en el orden en que las usas**. Cada documento está en `.md`.

| Carpeta | Qué hay |
|---|---|
| [`1_Teoria/`](1_Teoria/) | Las presentaciones del sprint y los apuntes para repasar |
| [`2_Practica/`](2_Practica/) | Las actividades del sprint: dinámicas, hojas de ejercicios, guías y scripts |
| [`3_Reto/`](3_Reto/) | `1_Trabajar` (reto en una página, plantillas y datos) · `2_Entregar` (qué se sube, rúbrica y autoevaluación) · `3_Consultar` (ficha del reto y cada paso explicado) |
| [`4_Referencia/`](4_Referencia/) | Infografías del sprint |

Cómo se trabaja un reto, en todos los sprints: [método de trabajo](../../material/4.%20Como_se_trabaja_un_reto.md).

## Temario oficial de este sprint

| Unidad | Conceptos que entran |
|---|---|
| UD 1a.1 · Introducción a la IA | Historia y definiciones: IA simbólica, ML, DL, IA generativa. IA débil, general y superinteligencia · Modalidades: visión por computador, NLP, voz, sistemas de recomendación, robótica, IA generativa · Casos de uso reales por sector (educación, salud, turismo, industria, administración) · Mitos y límites: qué puede y qué no puede hacer la IA hoy |
| UD 1a.2 · Panorama de algoritmos y ciclo de un proyecto | Familias: reglas, regresión, clasificación, clustering, árboles, ensembles, redes neuronales · Ciclo de vida: CRISP-DM (negocio → datos → modelado → evaluación → despliegue) · Datos, características y etiquetas; qué hace falta para entrenar un modelo |
| UD 1a.3 · Tipos de aprendizaje | Supervisado, no supervisado, semisupervisado, autosupervisado y por refuerzo · Entrenamiento, validación y test; overfitting y underfitting; sesgo y varianza (intuición) · Introducción a métricas: exactitud, error, matriz de confusión |
| M8 · IA responsable (UD 8.1 a 8.5) | Ética, responsabilidad, gobernanza de datos, investigación e innovación responsables · Fuentes de sesgo en datos y modelos; equidad; transparencia y explicabilidad · RGPD y LOPDGDD; Reglamento Europeo de IA (AI Act): niveles de riesgo y obligaciones · Análisis de casos con dilemas éticos (selección de personal, reconocimiento facial, scoring, IA en educación) · Checklist de IA responsable aplicado a un caso propio |

**Y ahora:** Sprint 2 · Las matemáticas y la estadística detrás (jueves 22/10).

*12 h (4 h teoría · 3 h práctica · 5 h PBL, con 1 h de cierre del Sprint 0).*
