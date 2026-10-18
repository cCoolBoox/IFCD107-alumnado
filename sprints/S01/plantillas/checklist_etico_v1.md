# Checklist de IA responsable · versión 1

**Se rellena por cada caso de uso** del informe de oportunidades (M8, UD 8.5). Es la **versión 1**: **se reutiliza y se actualiza en el proyecto final** (Sprints 14-16, requisito R6). Guardadla en el repositorio del equipo con un control de versiones (`checklist_etico_v1.md`, luego `v2`…).

**Caso de uso evaluado:** ______________________ · **Equipo:** __________ · **Fecha:** ____ · **Revisado por (otra persona):** __________

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
