# Sprint 1 · Qué es la IA, cómo aprende y cómo usarla bien

**Pregunta guía:** ¿dónde puede ayudar la IA al cliente y qué riesgos tiene?

| | |
|---|---|
| **Fechas** | lun 19/10 – mié 21/10 (el relevo con el Sprint 2 se hace a mitad de jornada del miércoles) |
| **Horas** | 15 h en total: **8 h de teoría (T) · 4 h de práctica (P) · 3 h de reto (PBL)** |
| **Módulos** | M1a (UD 1a.1, 1a.2 y 1a.3) + M8 Responsible AI |
| **Bloque** | A · Sin Python: **no hay notebooks** en este sprint |

## Qué aprenderás
1. Explicar qué es la IA y distinguir IA, machine learning, deep learning e IA generativa, con sus **modalidades** (visión, lenguaje, voz, recomendación, generativa) y casos de uso reales.
2. Describir las **familias de algoritmos**, el ciclo de vida de un proyecto (CRISP-DM) y elegir una familia razonable ante un problema.
3. Distinguir aprendizaje **supervisado, no supervisado, por refuerzo** y preentrenado, y entender el **sobreajuste** y por qué se separan los datos de entrenamiento, validación y test.
4. Identificar riesgos de **sesgo, privacidad, transparencia, desinformación y decisiones automatizadas**, y conocer lo esencial de RGPD y del AI Act.
5. Aplicar un **checklist ético** a un caso y priorizar oportunidades de IA para un cliente.

## Requisitos previos
Haber cursado el Sprint 0 (equipo, tablero y entrevista al cliente TurisData). No hace falta Python ni matemáticas.

## Materiales del sprint

| Material | Tema | Tiempo | Cuándo |
|---|---|---|---|
| [`tarjetas_casos_uso.md`](tarjetas_casos_uso.md) · Dinámica A | Mapa de casos de uso: modalidad, aprendizaje y datos | 1 h | Práctica 1 |
| [`tarjetas_casos_uso.md`](tarjetas_casos_uso.md) · Dinámica B | Clasificación "a mano" y sobreajuste | 1 h | Práctica 2 |
| [`tarjetas_casos_uso.md`](tarjetas_casos_uso.md) · Dinámica C | ¿Qué familia de algoritmos? (6 problemas) | 1 h | Práctica 3 |
| [`casos_debate_ia_responsable.md`](casos_debate_ia_responsable.md) | Debate de 5 casos éticos con roles | 1 h | Práctica 4 (M8, UD 8.4) |
| [`checklist_etico_v1.md`](checklist_etico_v1.md) | Checklist de IA responsable (versión 1) | en el reto | Reto |
| [`ejemplo_clasificacion_caso.md`](ejemplo_clasificacion_caso.md) | Ejemplo resuelto de ficha de caso de uso | consulta | Reto |

*(Como no hay notebooks en este bloque, no hay enlaces a Colab. Los materiales son `.md` imprimibles.)*

---

# Ficha del reto · "Auditoría de oportunidades de IA"

## Escena del cliente
Tras la entrevista del Sprint 0, la directora de *TurisData Canarias* os pide un **informe de oportunidades**: "No sé por dónde empezar con la IA. Decidme **qué cinco cosas** podría hacer, cuáles tienen sentido primero, qué datos necesito y **qué riesgos** corro. No quiero líos con los datos de mis clientes ni que una máquina decida sin que yo lo sepa". Dispone de un presupuesto limitado para un piloto y de datos de reservas, ocupación y reseñas.

## Qué tenéis que entregar
1. **Informe de oportunidades** (2-3 páginas, en `.md` o PDF) con la estructura de abajo.
2. **Checklist ético (versión 1)** rellenado para **cada uno de los 5 casos** (o completo para los 2 casos priorizados y resumido para los otros 3).

### Estructura del informe (2-3 páginas)
1. **Resumen ejecutivo** (5-6 líneas): las 5 oportunidades y cuál recomendáis empezar.
2. **Lo que hemos entendido** del cliente (3-4 líneas, con vuestra HMW priorizada del Sprint 0).
3. **Tabla de 5 casos de uso**: nombre, problema de negocio, modalidad, tipo de aprendizaje, familia de algoritmos, **datos necesarios** (y si existen), métrica de éxito.
4. **Priorización:** matriz impacto × facilidad, con criterio explicado.
5. **Riesgos y checklist ético:** el semáforo de cada caso y las medidas para los riesgos principales.
6. **Recomendación y siguientes pasos:** qué piloto, con qué datos y qué necesitamos del cliente.
7. **Límites de este informe:** qué no hemos podido comprobar.

## Datos y recursos
- Notas de la entrevista y mapa de empatía del Sprint 0.
- Las **22 tarjetas** de la dinámica A (podéis elegir de ahí, adaptar o inventar casos nuevos, **al menos 2 propios**).
- [`ejemplo_clasificacion_caso.md`](ejemplo_clasificacion_caso.md) y [`checklist_etico_v1.md`](checklist_etico_v1.md).
- No hay datos que analizar todavía: esta auditoría es de **ideas y riesgos**, no de resultados.

## Restricciones
- **Tiempo:** 3 h de reto en clase (dentro de las 15 h del sprint).
- **Extensión:** 2-3 páginas de informe (sin contar el checklist).
- **Presupuesto orientativo del cliente:** hasta 15.000 € para un piloto; nada de proyectos eternos.
- **Los 5 casos** deben cubrir **al menos 3 modalidades** distintas y **al menos 1** no debe requerir IA (o debe resolverse mejor con reglas) para mostrar criterio.
- Uso de asistentes de IA generativa permitido, con **declaración** de dónde se ha usado y qué habéis verificado.

## Criterios de evaluación
Cada entregable se evalúa de 0 a 4 en los cuatro criterios de la rúbrica de retos.

| Criterio | 1 · Insuficiente | 2 · Suficiente | 3 · Bueno | 4 · Excelente |
|---|---|---|---|---|
| **Corrección técnica** | Confunde modalidad, tipo de aprendizaje o datos en varios casos | Clasificaciones correctas con fallos menores | Clasificaciones correctas y justificadas; datos concretos | Además compara alternativas (p. ej. reglas frente a modelo) y detecta riesgos técnicos (fuga de datos, desbalance) |
| **Reproducibilidad** | No se entiende cómo se llegó a las conclusiones | Se entiende con ayuda | El informe deja claro el criterio de priorización y las fuentes | Además el checklist y el informe están versionados en el repositorio del equipo |
| **Análisis y comunicación al cliente** | Jerga sin explicar o lista de ideas sin priorizar | Ideas con interpretación básica | Recomendación clara y comprensible para la dirección | Recomendación accionable con próximos pasos, datos necesarios y límites explicados |
| **IA responsable** | No se considera | Menciones genéricas ("hay que cumplir el RGPD") | Riesgos específicos por caso | Medidas concretas por caso y criterio para decidir el semáforo |

## Pasos sugeridos (3 h de reto, repartidas por días)

| Momento | Qué hacer |
|---|---|
| **Lunes 19/10 · planning (30 min)** | Leed la ficha, repartid el trabajo en el tablero, definid la estructura del informe |
| **Martes 20/10 (30 min)** | Lluvia de ideas con las tarjetas y elección de 8 candidatos; descartad hasta quedaros con 5 casos (al menos 2 propios) |
| **Miércoles 21/10 (1 h)** | Fichas de los 5 casos (usad el ejemplo resuelto), checklist ético v1 (completo en los 2 casos priorizados y resumido en el resto), matriz de priorización y redacción del informe; revisión cruzada y DoD. **Lo que no cabra, lo terminaréis dentro de vuestro tiempo de trabajo del equipo, antes del Sprint 2** |
| **Miércoles 21/10 · última hora** | Review de 5 min por equipo y retro |

Entre medias, aprovechad los ratos de las prácticas (mapa de casos, debate) para adelantar el informe: las tarjetas y el checklist son la materia prima.

## Qué se enseña en la review (5 min por equipo)
- La **recomendación** en una frase y por qué la primera prioridad.
- **Un caso que descartasteis** y por qué (por riesgo, por datos o por falta de valor).
- El **semáforo ético** de vuestro caso principal y la medida más importante.
- Una duda que queda abierta para el cliente.

## Checklist Definition of Done
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

## Preguntas de la retrospectiva
1. ¿Qué descartamos por falta de datos y qué haríamos para conseguirlos?
2. ¿Qué riesgo ético nos ha sorprendido más?
3. ¿Cómo nos organizamos con el tablero? ¿Qué cambiamos para el Sprint 2?

## Recursos
1. Guía y taxonomía de riesgos del **Reglamento europeo de IA** (Reglamento UE 2024/1689) en el sitio oficial de la UE: comprobad siempre la **fecha de aplicación de cada obligación** **[verificar calendario vigente antes de impartir]**.
2. **AEPD** (Agencia Española de Protección de Datos): guías sobre IA y protección de datos.
3. **CRISP-DM**: descripciones abiertas del ciclo de vida de un proyecto de minería de datos.
4. Apuntes y presentaciones del sprint (S1.1 a S1.4).
5. [`ejemplo_clasificacion_caso.md`](ejemplo_clasificacion_caso.md): ejemplo resuelto.
