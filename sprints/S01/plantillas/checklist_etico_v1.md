# Checklist de IA responsable · versión 1

## Cuándo y para qué se rellena

En el reto del Sprint 1 (**Auditoría de oportunidades de IA**) vuestro equipo propone **5 casos de uso**: ideas concretas de cómo podría ayudar la IA a TurisData Canarias. Las recogéis en el **informe de oportunidades**, y este checklist es la parte que **revisa los riesgos éticos y legales de esos casos antes de construir nada** (en el temario del curso: módulo 8 «IA responsable», unidad 8.5 «Evaluación ética de un proyecto»).

- **Para los 2 casos que priorizáis** (los de arriba a la derecha en la matriz impacto × facilidad): rellenad el checklist **completo**, con una copia de esta plantilla por caso.
- **Para los otros 3 casos**: una versión **resumida**. Como mínimo, la ficha rápida (apartado 0), las preguntas marcadas con **(★)** y el semáforo con una línea de justificación.

**Dónde se guarda.** Todo va en un solo fichero del repositorio del equipo, `sprint-01/checklist_etico.md` (como indica la guía «Cómo entregar en GitHub»): un bloque por caso, cada uno con el nombre del caso como título.

**Es la versión 1:** se reutiliza y se actualiza en el proyecto final (Sprints 14-16, requisito R6). Al actualizarla, el historial de Git conserva esta versión; si queréis, guardad la nueva con otro nombre (`checklist_etico_v2.md`).

**Caso de uso evaluado:** ______________________ · **Equipo:** __________ · **Fecha:** ____ · **Revisado por (otra persona):** __________

## De dónde sale este checklist

**Es una herramienta propia de este curso, no un formulario oficial.** No hay un «checklist ético de la IA» que la ley exija rellenar. Este se ha construido para el curso a partir de lo que se trabaja en el **módulo M8 · IA responsable** (UD 8.1 a 8.5) y, en concreto, en la presentación **S01.4 · IA responsable: ética, sesgo y normativa**. Convierte en preguntas comprobables lo que allí se explica, para que se pueda aplicar a un caso concreto antes de construir nada.

**La idea de partida.** Los casos que salieron mal (COMPAS, la selección de CV de Amazon, el reconocimiento facial) comparten las mismas causas: datos históricos sesgados, nadie midió la equidad antes de desplegar y no había revisión humana. Un checklist sirve para **hacerse esas preguntas a tiempo**, caso por caso, en vez de descubrir los problemas cuando el sistema ya está en marcha.

**Cada apartado sale de una parte del módulo:**

| Apartado del checklist | De dónde sale (S01.4 y módulo M8) |
|---|---|
| 0. Ficha rápida · 1. Propósito y proporcionalidad | Los **cuatro pilares éticos**: beneficencia (beneficio real y medible) y no maleficencia (minimizar daños) |
| 2. Datos y privacidad | **Gobernanza de datos** y principios del **RGPD y la LOPDGDD**: limitación de finalidad, minimización, derechos de las personas |
| 3. Sesgo y equidad | **Fuentes de sesgo** en datos y modelos, y **equidad** (hay varias definiciones; se elige según el contexto) |
| 4. Transparencia y explicabilidad | **Transparencia y explicabilidad (XAI)**; obligaciones de transparencia del **AI Act** |
| 5. Supervisión humana | **Autonomía** (sin manipulación) y **art. 22 del RGPD** (no decidir solo con automatización efectos relevantes) |
| 6. Robustez, seguridad y calidad | Evaluar con **datos que el modelo no ha visto** (train y test, métricas: S01.3) y vigilar el sistema tras ponerlo en marcha |
| 7. Impacto social y ambiental | **Justicia** (beneficios y riesgos repartidos con equidad) |
| 8. Normativa | **RGPD/LOPDGDD** (evaluación de impacto) y los **cuatro niveles de riesgo del AI Act** |
| 9. Gobernanza y responsabilidad | «**¿Quién responde cuando falla?**»: la cadena de actores es larga y la responsabilidad no puede acabar siendo de nadie |
| 10. Resultado | Tabla de riesgos y semáforo, para **decidir** y dejar constancia; un caso puede salir «no recomendable», y eso también es un buen resultado |

**Qué no es.** No sustituye el asesoramiento legal ni la opinión de un delegado de protección de datos: el apartado 8 es solo una **orientación**, y los plazos del AI Act son escalonados (**consultad siempre el calendario vigente**). Tampoco es un trámite: su valor está en las **evidencias y acciones** que escribís, no en marcar casillas.

**Dónde se usa en el curso:** Sprint 1 (esta versión 1, en el reto de auditoría de oportunidades) → **Sprint 14** (plan ético del proyecto final: se actualiza este checklist) → entrega final (**requisito R6**: «checklist ético del Sprint 1 actualizado», con análisis de sesgos, limitaciones y clasificación de riesgo).

## Cómo se usa
1. Respondéis a cada punto con **Sí / No / No aplica / No lo sé**.
2. Escribid una **evidencia o una acción** (algo comprobable): "no lo sé" no es una respuesta válida en la versión final: hay que averiguarlo o marcarlo como riesgo abierto.
3. Al final, asignad un **semáforo**: verde (se puede avanzar), ámbar (con medidas), rojo (no avanzar sin cambios).
4. Cada "No" o "No lo sé" en puntos marcados con **(★)** se lleva a la tabla de riesgos.

## 0. Ficha rápida del caso
| Pregunta | Respuesta |
|---|---|
| ¿Qué problema de negocio resuelve? | |
| ¿Quién usa el resultado y quién se ve afectado por él? | |
| ¿La IA **decide** o **apoya** a una persona que decide? | |
| ¿Qué pasa si se equivoca? ¿quién sufre el error y cómo de grave es? | |

## 1. Propósito y proporcionalidad
| # | Pregunta | S/N/NA/? | Evidencia o acción |
|---|---|---|---|
| 1.1 (★) | ¿El problema es **real y está explicado** con datos o testimonios del cliente? | | |
| 1.2 | ¿Es necesaria la IA o basta con una regla sencilla? | | |
| 1.3 (★) | ¿El beneficio esperado **justifica el riesgo** para las personas? | | |
| 1.4 | ¿Hay una alternativa menos invasiva que consiga casi lo mismo? | | |

## 2. Datos y privacidad
| # | Pregunta | S/N/NA/? | Evidencia o acción |
|---|---|---|---|
| 2.1 (★) | ¿Sabemos **qué datos** usa, de dónde vienen y con qué **licencia o base legal**? | | |
| 2.2 (★) | ¿Hay **datos personales**? ¿Se usan solo los necesarios? (minimización) | | |
| 2.3 | ¿Hay datos de **menores** o categorías especiales (salud, biometría, creencias)? | | |
| 2.4 (★) | ¿Se informa a las personas y se respeta la **finalidad** original del dato? | | |
| 2.5 | ¿Están **anonimizados o seudonimizados**? ¿Se definió el plazo de conservación? | | |
| 2.6 | ¿Se usan servicios de terceros o de IA en la nube? ¿Hay contrato y control de dónde van los datos? | | |
| 2.7 | ¿Puede una persona ejercer sus derechos (acceso, rectificación, supresión, oposición)? | | |

## 3. Sesgo y equidad
| # | Pregunta | S/N/NA/? | Evidencia o acción |
|---|---|---|---|
| 3.1 (★) | ¿Los datos de entrenamiento **representan** a las personas a las que se aplicará? ¿quién falta? | | |
| 3.2 (★) | ¿Hay variables sensibles o **proxies** (código postal, país, apellido, edad, sexo)? | | |
| 3.3 | ¿Se evaluará el rendimiento **por grupos** (no solo la media)? ¿con qué métrica? | | |
| 3.4 | ¿Las etiquetas reflejan una **realidad** o decisiones humanas anteriores potencialmente sesgadas? | | |
| 3.5 | ¿Hay un plan si aparece un sesgo (corregir, limitar el uso, retirar)? | | |

## 4. Transparencia y explicabilidad
| # | Pregunta | S/N/NA/? | Evidencia o acción |
|---|---|---|---|
| 4.1 (★) | ¿Las personas saben que **interactúan con IA** o que una IA interviene en una decisión? | | |
| 4.2 | ¿Se puede **explicar** el resultado en lenguaje sencillo (qué factores pesan)? | | |
| 4.3 | ¿Se documenta **qué hace el sistema y qué no** (límites, casos donde falla)? | | |
| 4.4 | ¿Los contenidos generados por IA están **etiquetados**? | | |

## 5. Supervisión humana y decisiones automatizadas
| # | Pregunta | S/N/NA/? | Evidencia o acción |
|---|---|---|---|
| 5.1 (★) | ¿Hay una **persona con capacidad real** de revisar y cambiar el resultado? | | |
| 5.2 (★) | ¿La decisión tiene efectos **significativos** (dinero, acceso, empleo)? Si es así, ¿existe vía de reclamación? | | |
| 5.3 | ¿Se puede **desactivar** el sistema con rapidez si algo va mal? | | |
| 5.4 | ¿Se forma al personal para que **no confíe ciegamente** en el sistema? | | |

## 6. Robustez, seguridad y calidad
| # | Pregunta | S/N/NA/? | Evidencia o acción |
|---|---|---|---|
| 6.1 | ¿Se ha **medido** el error con datos que el modelo no ha visto? | | |
| 6.2 | ¿Se sabe qué pasa con datos raros, incompletos o de otro año? | | |
| 6.3 | ¿Hay medidas ante **ataques o abusos** (inyección de instrucciones, fuga de datos)? | | |
| 6.4 | ¿Está previsto **monitorizar** el sistema tras ponerlo en marcha (deriva de datos, errores)? | | |

## 7. Impacto social y ambiental
| # | Pregunta | S/N/NA/? | Evidencia o acción |
|---|---|---|---|
| 7.1 | ¿Cómo afecta a las **personas empleadas** (tareas, formación, puestos)? | | |
| 7.2 | ¿Puede tener un efecto negativo en el **territorio o la comunidad** (precios de vivienda, presión turística)? | | |
| 7.3 | ¿Es proporcionado el **coste de computación** y energía? | | |

## 8. Normativa (orientación; no sustituye el asesoramiento legal)
| # | Pregunta | S/N/NA/? | Evidencia o acción |
|---|---|---|---|
| 8.1 (★) | ¿Aplica el **RGPD/LOPDGDD**? ¿Hace falta una evaluación de impacto? | | |
| 8.2 (★) | Nivel de riesgo aproximado según el **AI Act**: inaceptable / alto / transparencia (limitado) / mínimo | | |
| 8.3 | ¿Qué obligaciones de esa clase se aplican y **desde cuándo**? **[verificar calendario vigente antes de impartir]** | | |
| 8.4 | ¿Hay otras normas (consumo, propiedad intelectual, sectoriales)? | | |

## 9. Gobernanza y responsabilidad
| # | Pregunta | S/N/NA/? | Evidencia o acción |
|---|---|---|---|
| 9.1 (★) | ¿Hay una **persona responsable** del sistema y de sus efectos? | | |
| 9.2 | ¿Se registra quién decidió qué y cuándo (trazabilidad, versiones del modelo y de los datos)? | | |
| 9.3 | ¿Hay un canal para **quejas y errores**? | | |
| 9.4 | ¿Se ha pedido opinión a las **personas afectadas**? | | |

## 10. Resultado

**Tabla de riesgos** (una fila por cada ★ con "No" o "No lo sé", más los que detectéis):

| Riesgo | Probabilidad (B/M/A) | Impacto (B/M/A) | Medida propuesta | Responsable |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

**Semáforo:** [ ] Verde (avanzar) · [ ] Ámbar (avanzar con medidas) · [ ] Rojo (no avanzar sin cambios)

**Justificación en 3 líneas:** ______________________________________________

**Qué actualizaremos en el proyecto final:** ______________________________________________

## Consejos
- Un **checklist no es un trámite**: si todo es "Sí" sin evidencia, no se ha hecho.
- Rellenad el checklist **con otra persona** que no haya diseñado el caso.
- Priorizad las preguntas (★): con poco tiempo, empezad por ellas.
- Guardad esta versión: en el proyecto final se pide **actualizarla** y demostrar qué medidas se aplicaron y cómo se evaluaron.
