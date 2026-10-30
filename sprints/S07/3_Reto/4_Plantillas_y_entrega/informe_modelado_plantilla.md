# Informe de modelado · TurisData Canarias · «Precio y cancelación»

**Equipo:** … · **Fecha:** …

## 1. Resumen para el gerente (máx. 6 líneas)
Qué hemos hecho, qué funciona, qué cuesta cada tipo de error y qué recomendamos.

## 2. Datos y variables
Filas, variables usadas, variables **excluidas** y por qué (fuga, no disponibles al reservar). Partición train/test.

## 3. Regresión: precio por noche
| Modelo | MAE (€) | RMSE (€) | R² |
|---|---|---|---|
| Baseline (media) | | | |
| Lineal | | | |
| … | | | |

Lectura para el cliente: coeficientes clave en euros (p. ej. «una suite cuesta X € más que una estándar»). Dónde falla el modelo (residuos).

## 4. Clasificación: cancelación
| Modelo | AUC | AP | Recall (umbral) | Precisión (umbral) |
|---|---|---|---|---|
| Baseline | | | | |
| Logística | | | | |
| … | | | | |

Matriz de confusión en test con el umbral elegido. Factores que más aumentan y reducen el riesgo (*odds ratios*).

## 5. De las métricas a los euros
- **Hipótesis de coste** de una cancelación no prevista (FN): … € por reserva (justificación).
- **Hipótesis de coste** de una falsa alarma (FP): … € por reserva (justificación).
- Umbral elegido con validación cruzada: …
- Coste en test: sin modelo … € · umbral 0,5 … € · umbral elegido … €.
- **Análisis de sensibilidad:** qué pasa si el coste de FN o FP cambia (tabla o gráfico).

## 6. Recomendación de negocio
Acción concreta (qué hacer con las reservas de riesgo), beneficio esperado y **límites** (datos sintéticos/limitados, cambios de comportamiento, etc.).

## 7. IA responsable
Riesgos específicos (sesgo por país o canal, efecto sobre clientes reubicados, uso del modelo para discriminar precios/depósitos) y medidas aplicadas.

## 8. Cómo reproducirlo
Versiones, semilla, orden de ejecución.

## Revisión con la rúbrica
<Rúbrica completa en la ficha del reto, apartado 3. Rellena quien revisa y **no escribió esa parte**: ejecutar el cuaderno de arriba abajo con solo el README, leer el informe como si fueras el gerente, mirar el cuaderno (variables, umbral, test) y poner nivel con prueba.>

**Revisado por:** <nombre> · **Fecha:** <dd/mm/aaaa>

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
|---|---|---|
| Corrección técnica | <1–4> | <p. ej. «hay baselines y matriz, pero el umbral se eligió mirando el test»> |
| Reproducibilidad | <1–4> | <¿obtienes las mismas cifras ejecutando el cuaderno entero con solo el README?> |
| Análisis y comunicación al cliente | <1–4> | <¿se entiende la recomendación sin saber qué es el AUC? ¿tiene euros y límites?> |
| IA responsable | <1–4> | <¿dice qué se pidió, qué se revisó y qué se cambió, y nombra riesgos específicos?> |

**Lo primero que mejoraríamos:** <una cosa concreta>
