# Plan ético y registro de riesgos

**Proyecto:** ______ · **Responsable de IA responsable:** ______ · **Versión vigente:** S14 / S15 / S16 (tacha)

> Este documento **actualiza el checklist de IA responsable del Sprint 1** (M8, UD 8.5) para el proyecto final (requisito **R6**).
> Se rellena en el Sprint 14 (plan inicial), se revisa el 3/12 y se **cierra el 10/12** con evidencias. No es un trámite: cada respuesta debe apoyarse en algo que se pueda comprobar en el repositorio.
> **Cómo se actualiza:** conserva vuestras respuestas del Sprint 1 (columna «S1» si las tenéis), y en cada sprint anota en la columna correspondiente qué ha cambiado y la evidencia.

## Parte A · Checklist ético (versión proyecto final)
Estado: **✔** cumplido con evidencia · **◐** parcial · **✘** no cumplido · **n/a** no aplica (justificar).

### A1. Propósito y proporcionalidad
| Pregunta | S1 | S14 | S15 | S16 | Evidencia |
|---|---|---|---|---|---|
| ¿Qué problema resolvemos y para quién? ¿Es necesario usar IA o basta una regla simple? | | | | | Ficha |
| ¿Qué pasa si el modelo falla? ¿Quién sale perjudicado? | | | | | |
| ¿Hay usos indebidos previsibles (dual use)? ¿Qué **no** debe hacerse con el resultado? | | | | | Model card |

### A2. Datos y privacidad (RGPD / LOPDGDD)
| Pregunta | S1 | S14 | S15 | S16 | Evidencia |
|---|---|---|---|---|---|
| ¿Hay **datos personales**? ¿Cuáles? ¿Podemos evitarlos (minimización)? | | | | | Plan de datos |
| ¿Base legal y finalidad claras? ¿Se informa a las personas? | | | | | |
| ¿Datos sensibles (salud, biometría, menores, origen…)? Si sí, ¿justificado y autorizado? | | | | | |
| ¿Se pueden reidentificar personas a partir de los datos o de las salidas del modelo? | | | | | |
| ¿Licencia de los datos compatible con el uso? ¿Se ha citado la fuente? | | | | | Plan de datos |
| ¿Se guardan datos de usuarios en el demostrador? ¿Dónde y cuánto tiempo? | | | | | |

### A3. Sesgo y equidad
| Pregunta | S1 | S14 | S15 | S16 | Evidencia |
|---|---|---|---|---|---|
| ¿Quién falta o está infrarrepresentado en los datos (sesgo de muestreo)? | | | | | EDA |
| ¿Hay variables proxy de atributos protegidos (edad, sexo, origen, discapacidad, ubicación)? | | | | | |
| ¿Se ha medido el rendimiento **por subgrupos** (país, isla, cultivo, ciclo, franja horaria…)? | | | | | Notebook de evaluación |
| ¿Se han aplicado y evaluado medidas de mitigación (reponderar, umbrales, revisión humana)? | | | | | |

### A4. Transparencia y explicabilidad
| Pregunta | S1 | S14 | S15 | S16 | Evidencia |
|---|---|---|---|---|---|
| ¿El usuario sabe que interactúa con un sistema de IA? (obligatorio en chatbots) | | | | | Demostrador |
| ¿Se explica qué variables pesan (permutación / SHAP / Grad-CAM) y con qué límites? | | | | | |
| ¿Se muestra la **incertidumbre** (probabilidad, intervalo, «no sé»)? | | | | | |
| ¿Existe *model card* con usos previstos, límites y métricas? | | | | | `model_card.md` |

### A5. Supervisión humana y robustez
| Pregunta | S1 | S14 | S15 | S16 | Evidencia |
|---|---|---|---|---|---|
| ¿Hay una persona que revisa las decisiones importantes y puede corregir? | | | | | |
| ¿Qué ocurre con entradas fuera de distribución, errores del usuario o eventos atípicos? | | | | | Pruebas |
| ¿Se ha probado con datos reales distintos a los de entrenamiento (generalización)? | | | | | |
| ¿Hay riesgo de sobreconfianza del usuario en la salida del modelo? ¿Cómo se avisa? | | | | | |

### A6. Impacto y sostenibilidad
| Pregunta | S1 | S14 | S15 | S16 | Evidencia |
|---|---|---|---|---|---|
| ¿Impacto social, laboral o ambiental (coste de cómputo, energía)? | | | | | |
| ¿Se ha elegido el modelo más simple que cumple el objetivo? | | | | | Registro de experimentos |

## Parte B · Clasificación normativa preliminar
| Cuestión | Respuesta y justificación |
|---|---|
| ¿Trata datos personales? ¿De qué tipo? | |
| Base legal / finalidad (si aplica) | |
| ¿Necesitaría una evaluación de impacto (EIPD)? | *(indicar por qué sí / por qué no)* |
| **Nivel de riesgo AI Act:** inaceptable · alto · limitado (obligaciones de transparencia) · mínimo | |
| Obligaciones que se derivan (transparencia, supervisión humana, documentación…) | |
| ¿El sistema toma o apoya **decisiones sobre personas**? (educación, empleo, servicios esenciales…) | |

*Orientación general (verifica el calendario y el texto vigente con el docente antes de fijar la clasificación): un sistema que solo predice demanda agregada suele ser de riesgo **mínimo**; un chatbot que informa a personas tiene obligaciones de **transparencia** (riesgo limitado); un sistema que evalúe o decida sobre el acceso de personas a la educación, al empleo o a servicios esenciales entra en el ámbito de **alto riesgo**.*

## Parte C · Registro de riesgos
**Probabilidad (P)** y **impacto (I)** de 1 (bajo) a 3 (alto). **Nivel = P × I:** 1-2 bajo · 3-4 medio · 6-9 alto (los altos requieren mitigación evaluada).

| ID | Riesgo (qué puede ir mal y a quién afecta) | Tipo (datos / modelo / uso / legal / técnico) | P | I | Nivel | Medida de mitigación | Responsable | Estado (abierto / mitigado / aceptado) | **Cómo se evaluó la mitigación** (prueba, métrica, resultado) |
|---|---|---|---|---|---|---|---|---|---|
| R-01 | | | | | | | | | |
| R-02 | | | | | | | | | |
| R-03 | | | | | | | | | |
| R-04 | | | | | | | | | |
| R-05 | | | | | | | | | |

**Ejemplos de riesgos según el brief (no los copies: adáptalos con vuestras cifras):**
- *Brief 1 / 4 (series):* rotura de la serie por un suceso atípico; uso de la previsión para restringir el acceso o discriminar mercados; errores de sobrepredicción con coste en infraestructura.
- *Brief 2 (cultivos):* fotos de laboratorio con fondo uniforme que no generalizan; sobreconfianza en un diagnóstico que es solo orientativo; sesgo por cultivos o enfermedades infrarrepresentadas.
- *Brief 3 (asistente FP):* alucinaciones y desinformación al alumnado; falta de transparencia sobre el asistente; que se use para tomar decisiones sobre personas; datos personales en las preguntas de los usuarios.
- *Libre:* ______

## Parte D · Cierre (10/12)
- ¿Qué riesgos altos quedaron mitigados y con qué evidencia? ______
- ¿Qué riesgos **residuales** aceptamos y se comunican al cliente? ______
- Limitaciones y usos no permitidos (pasan a la *model card* y a la memoria): ______
- Fecha y firmas del responsable de IA responsable y del equipo: ______
