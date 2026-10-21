# README Sprint S01 · Qué es la IA, cómo aprende y cómo usarla bien

**Pregunta guía:** ¿dónde puede ayudar la IA al cliente y qué riesgos tiene?
**Fechas:** mar 20/10 – mié 21/10 · **Horas:** 12 h (4 h teoría · 3 h práctica · 5 h PBL, con 1 h para cerrar el Sprint 0)
**Módulos:** M1a (UD 1a.1 a 1a.3) + M8 IA responsable · Bloque A: sin Python ni notebooks

📄 **Este README en PDF:** [a color](README_Sprint_01.pdf) · [ecofriendly, para imprimir](README_Sprint_01_ecofriendly.pdf) (descárgalo para que funcionen los enlaces; la vista previa de GitHub no los abre).

## Qué aprenderás
1. Explicar qué es la IA y distinguir IA, machine learning, deep learning e IA generativa, con sus **modalidades** (visión, lenguaje, voz, recomendación, generativa) y casos de uso reales.
2. Describir las **familias de algoritmos**, el ciclo de vida de un proyecto (CRISP-DM) y elegir una familia razonable ante un problema.
3. Distinguir aprendizaje **supervisado, no supervisado, por refuerzo** y preentrenado, y entender el **sobreajuste** y por qué se separan los datos de entrenamiento, validación y test.
4. Identificar riesgos de **sesgo, privacidad, transparencia, desinformación y decisiones automatizadas**, y conocer lo esencial de RGPD y del AI Act.
5. Aplicar un **checklist ético** a un caso y priorizar oportunidades de IA para un cliente.

## Requisitos previos
Haber cursado el Sprint 0 (equipo, tablero y entrevista al cliente TurisData). No hace falta Python ni matemáticas.

## 📎 Materiales del sprint

**Documentos del curso** (PDF y .md; las actividades van en la tabla siguiente)

| Material | Tema | Tiempo | Cuándo |
|---|---|---|---|
| [Guía del sprint (PDF)](guia/Guia_Sprint_01.pdf) · [ecofriendly](guia/Guia_Sprint_01_ecofriendly.pdf) | Resumen del sprint: qué aprenderás, temario, material, reto y conclusión | 2 páginas | Antes de empezar |
| [Reto completo, paso a paso (.md)](guia/Reto_Sprint_01.md) · [PDF](guia/Reto_Sprint_01.pdf) · [ecofriendly](guia/Reto_Sprint_01_ecofriendly.pdf) | Qué pide el cliente, pasos, rúbrica, ayudas y errores frecuentes | — | Antes del planning y durante el reto |
| [Infografías del reto](infografias/) | 3 láminas ilustradas del reto | — | Reto |
| [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md) | El método de trabajo de todos los retos | — | Antes del primer reto |
| [`S01.1_Introduccion_a_la_IA.pdf`](presentaciones/S01.1_Introduccion_a_la_IA.pdf) | Introducción a la IA: modalidades, casos de uso y mitos | 25 min | Teoría · martes 20/10 |
| [`S01.2_Panorama_de_algoritmos_y_CRISP_DM.pdf`](presentaciones/S01.2_Panorama_de_algoritmos_y_CRISP_DM.pdf) | Panorama de algoritmos y CRISP-DM | 25 min | Teoría · martes 20/10 |
| [`S01.3_Tipos_de_aprendizaje.pdf`](presentaciones/S01.3_Tipos_de_aprendizaje.pdf) | Tipos de aprendizaje, entrenamiento/validación/test y sobreajuste | 25 min | Teoría · martes 20/10 |
| [`S01.4_IA_responsable_etica_sesgo_y_normativa.pdf`](presentaciones/S01.4_IA_responsable_etica_sesgo_y_normativa.pdf) | IA responsable: ética, sesgo, gobernanza de datos, RGPD, AI Act y lista de comprobación ética | 50 min | Teoría · miércoles 21/10 |

**Material de las actividades**

| Material | Tema | Tiempo | Cuándo |
|---|---|---|---|
| [`tarjetas_casos_uso.md`](actividades/tarjetas_casos_uso.md) · Dinámica A | Mapa de casos de uso: modalidad, aprendizaje y datos | 25 min (11 tarjetas) | Práctica 1 |
| [`tarjetas_casos_uso.md`](actividades/tarjetas_casos_uso.md) · Dinámica B | Clasificación "a mano" y sobreajuste | 10 min (demostración) | Práctica 2 |
| [`tarjetas_casos_uso.md`](actividades/tarjetas_casos_uso.md) · Dinámica C | ¿Qué familia de algoritmos? (6 problemas) | 15 min (3 de los 6 problemas, en gran grupo) | Práctica 3 |
| [`casos_debate_ia_responsable.md`](actividades/casos_debate_ia_responsable.md) | Debate de casos éticos con roles (2 de los 5) | 25 min | Práctica 4 (M8, UD 8.4) |
| [`checklist_etico_v1.md`](plantillas/checklist_etico_v1.md) | Checklist de IA responsable (versión 1) | en el reto | Reto |
| [`ejemplo_clasificacion_caso.md`](actividades/ejemplo_clasificacion_caso.md) | Ejemplo resuelto de ficha de caso de uso | consulta | Reto |

*(Como no hay notebooks en este bloque, no hay enlaces a Colab. Los materiales son `.md` imprimibles.)*

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

**Martes 20/10**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 1 | 🎯 Reto | **Cierre del Sprint 0** (lo que quedó pendiente del reto): [acuerdo de trabajo y lista de «terminado»](../S00/plantillas/plantillas_equipo.md), [entrevista al cliente](../S00/actividades/entrevista_descubrimiento.md) en grupo grande (antes, 10 min en equipo para preparar las preguntas con la plantilla del mapa a la vista), después el [mapa de empatía de TurisData](../S00/plantillas/empatia_hmw_plantillas.md) con lo oído y retro corta | 40 min |
| 2 | 🔔 Ceremonia | Planning del Sprint 1: leed la ficha del reto y repartid los 7 apartados del informe | 10 min |
| 3 | 📖 Teoría | [Introducción a la IA: modalidades, casos de uso y mitos](presentaciones/S01.1_Introduccion_a_la_IA.pdf) | 25 min |
| 4 | 💻 Práctica | [Dinámica A: tarjetas de casos de uso (11 tarjetas)](actividades/tarjetas_casos_uso.md) | 25 min |
| 5 | 📖 Teoría | [Panorama de algoritmos y CRISP-DM](presentaciones/S01.2_Panorama_de_algoritmos_y_CRISP_DM.pdf) | 25 min |
| 6 | 💻 Práctica | Dinámica C: elegir la familia de algoritmos en 3 de los 6 problemas (con el docente) | 15 min |
| 7 | 📖 Teoría | [Tipos de aprendizaje, entrenamiento/validación/test y sobreajuste](presentaciones/S01.3_Tipos_de_aprendizaje.pdf) | 25 min |
| 8 | 💻 Práctica | [Dinámica B: clasificación «a mano» (demostración en la pizarra)](actividades/ejemplo_clasificacion_caso.md) | 10 min |
| 9 | 🎯 Reto | [Lluvia de ideas y elección de casos (paso 2)](guia/Reto_Sprint_01.md) | 25 min |

**Miércoles 21/10**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 10 | 📖 Teoría | [IA responsable: ética, sesgo, gobernanza de datos, RGPD, AI Act y lista de comprobación ética](presentaciones/S01.4_IA_responsable_etica_sesgo_y_normativa.pdf) | 50 min |
| 11 | 💻 Práctica | [Debate de casos éticos con roles (2 de los 5 casos)](actividades/casos_debate_ia_responsable.md) | 25 min |
| 12 | 🎯 Reto | [Fichas de 4 casos (el 5.º, en versión breve), lista de comprobación ética (completa en los 2 casos priorizados), matriz de priorización y redacción (pasos 3–5)](plantillas/checklist_etico_v1.md) | 1 h 15 min |
| 13 | 🔔 Ceremonia | Entrega en `sprint-01/`, autoevaluación y coevaluación, review (5 min por equipo) y retrospectiva | 50 min |

<!--orden:fin-->

## Reto · «Auditoría de oportunidades de IA»

📄 [Reto en PDF](guia/Reto_Sprint_01.pdf) · [ecofriendly](guia/Reto_Sprint_01_ecofriendly.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

👉 **[Ver el reto completo, explicado paso a paso](guia/Reto_Sprint_01.md)** (qué se pide, cómo hacerlo, cómo usar la IA, errores frecuentes y autoevaluación).




**Contexto:** la directora de TurisData Canarias quiere saber qué 5 cosas podría hacer con IA, cuáles primero, qué datos necesita y qué riesgos corre. Tiene un piloto limitado (hasta 15.000 €).



**Entregáis** (en la carpeta `sprint-01/` del repositorio del equipo):
- Informe de oportunidades de 2-3 páginas (`.md` o PDF): resumen, tabla de 5 casos, priorización, riesgos y recomendación.
- Checklist ético v1 de cada caso (completo en los 2 priorizados).
- Declaración de dónde habéis usado IA generativa y qué habéis verificado.



**Reglas:**
- Unas 1 h 40 min de reto, más el planning y la review; los 5 casos cubren 3 modalidades o más y al menos 2 son propios.
- Al menos 1 caso no necesita IA (o va mejor con reglas).
- Nunca claves ni datos personales; no hay datos que analizar, solo ideas y riesgos.



**Se valora:** corrección técnica, reproducibilidad (criterio de priorización claro), comunicación al cliente e IA responsable (riesgos por caso, AI Act con calendario verificado).

## ✅ Antes de cerrar el sprint
- [ ] Informe de 2-3 páginas con 5 casos y matriz de priorización
- [ ] Checklist ético v1 con al menos 1 riesgo específico por caso
- [ ] Revisado por otra persona y declaración de uso de IA hecha
- [ ] Entregable subido a la carpeta `sprint-01/` del repositorio del equipo
- [ ] Tablero actualizado
- [ ] Autoevaluación y coevaluación rellenadas
