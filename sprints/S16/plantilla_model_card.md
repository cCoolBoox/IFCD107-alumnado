# Model card · [Nombre del modelo]

> Una *model card* es la «etiqueta nutricional» de un modelo: para qué sirve, con qué datos se entrenó, cuánto vale y **cuándo no usarlo**. Máximo 2 páginas. Debe coincidir con la memoria y con el aviso del demostrador. Guárdala como `docs/model_card.md`.

## 1. Detalles del modelo
| Campo | Contenido |
|---|---|
| Nombre y versión | |
| Equipo / responsables | |
| Fecha de entrenamiento y etiqueta del repositorio | |
| Tipo de modelo y librería (con versión) | *(p. ej. GRU en Keras 3.x; regresión logística en scikit-learn 1.x; RAG con modelo X)* |
| Hiperparámetros principales | |
| Semilla y cómo reproducirlo | |
| Licencia del modelo y del código | |

## 2. Uso previsto
- **Uso principal:** ______ · **Usuarios previstos:** ______
- **Decisión que apoya (y cuál sigue siendo humana):** ______
- **Usos fuera de alcance / no permitidos:** ______ *(p. ej. decidir sobre personas concretas, restringir accesos, diagnósticos definitivos)*

## 3. Datos
| | Entrenamiento | Validación | Test |
|---|---|---|---|
| Fuente y licencia | | | |
| Periodo / tamaño | | | |
| Cómo se partió | | | |

- Sesgos de muestreo conocidos y qué falta en los datos: ______
- Datos personales: sí / no (detalle): ______

## 4. Factores relevantes
Grupos o condiciones que pueden cambiar el rendimiento: *(isla, mercado, franja horaria, cultivo, iluminación del foto, tipo de pregunta, periodo del año…)*: ______

## 5. Métricas
| Métrica | Baseline | Modelo | Comentario (¿mejora relevante para el negocio?) |
|---|---|---|---|
| (técnica principal) | | | |
| (de negocio) | | | |

**Incertidumbre:** intervalo o variación (validación cruzada, remuestreo…): ______

## 6. Rendimiento por subgrupos
| Subgrupo | n | Métrica | Diferencia con el global | ¿Es aceptable? |
|---|---|---|---|---|
| | | | | |

## 7. Análisis ético y de riesgos
- **Clasificación AI Act / RGPD:** ______
- **Riesgos principales y mitigaciones aplicadas** (con su evaluación): ______
- **Supervisión humana:** ______ · **Transparencia hacia el usuario:** ______

## 8. Limitaciones y recomendaciones
- Cuándo **no** fiarse del modelo (casos fuera de distribución, sucesos atípicos, datos sintéticos, etc.): ______
- Recomendaciones para quien lo use: ______
- Qué habría que hacer antes de un despliegue real (más datos, monitorización, auditoría…): ______

## 9. Contacto y mantenimiento
Responsable: ______ · ¿Cada cuánto se reevalúa?: ______
