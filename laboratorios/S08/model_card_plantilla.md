# Model card · Predicción de cancelaciones de reservas · TurisData Canarias

**Equipo:** … · **Fecha:** … · **Versión del modelo:** 1.0 · **Contacto:** …

> Documento de 1–2 páginas para el cliente y para quien mantenga el modelo. Sé concreto y honesto con los límites.

## 1. Resumen
En 3–4 líneas: qué predice el modelo, para qué decisión se usará y quién lo usa.

## 2. Modelo campeón
- **Familia y algoritmo:** (p. ej. regresión logística / LightGBM / SVM RBF…)
- **Hiperparámetros finales:** …
- **Preprocesado:** imputación, escalado, codificación (pipeline).
- **Librerías y versiones:** …

## 3. Por qué este campeón (y no otro)
| Criterio | Peso acordado | Resultado del campeón | Mejor rival y diferencia |
|---|---|---|---|
| Rendimiento (AUC en validación cruzada) | … % | … ± … | … |
| Explicabilidad (1–5) | … % | … | … |
| Coste (ajuste, predicción, tamaño) | … % | … | … |

**Análisis de sensibilidad:** ¿cambia el campeón si cambian los pesos? ¿Con qué pesos? (adjunta la tabla).

## 4. Datos de entrenamiento
- Fuente, periodo, número de reservas, tasa de cancelación.
- Variables usadas y **variables excluidas** (fuga, sensibles, no disponibles al reservar).
- Limitaciones de los datos (sintéticos/limitados, periodos cortos, canales poco representados…).

## 5. Rendimiento
- **Validación cruzada (train):** AUC … · AP … · recall/precisión con el umbral elegido …
- **Test (una sola evaluación):** AUC …
- **Umbral de decisión** y su justificación (coste de una cancelación no prevista frente a una falsa alarma; ver el informe del Sprint 7).
- Rendimiento por subgrupos relevantes (canal, país, tipo de tarifa) y diferencias observadas.

## 6. Uso previsto y usos NO previstos
- **Uso previsto:** …
- **NO usar para:** (p. ej. denegar reservas, cobrar más a un país concreto, decisiones automáticas sin revisión humana…)

## 7. Explicabilidad
Cómo se puede explicar una predicción concreta a un gerente (variables más influyentes, reglas, odds ratio, importancia por permutación…).

## 8. Riesgos e IA responsable
- Sesgos posibles (país de origen, canal…) y cómo se han medido.
- Impacto de los errores en las personas (falsas alarmas: clientes reubicados).
- Medidas aplicadas y evaluadas; medidas pendientes.

## 9. Mantenimiento
- Qué vigilar en producción (deriva de datos, tasa de cancelación real vs. prevista).
- Cada cuánto se reentrena y con qué criterio.
- Coste estimado de mantenimiento y responsable.

## 10. Cómo reproducirlo
Semilla, versiones, orden de ejecución, ficheros (`leaderboard_S08.csv`, notebook).
