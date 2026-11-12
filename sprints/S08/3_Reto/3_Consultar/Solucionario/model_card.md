# Model card · Predicción de cancelaciones de reservas · TurisData Canarias

**Equipo:** de ejemplo (Solucionario) · **Fecha:** 12/11/2026 · **Versión del modelo:** 1.0 · **Contacto:** el equipo, desde el repositorio `ifcd107-equipo-…`

> Entrega de referencia: sirve de modelo de lo que hay que subir a `sprint-08/`. Cada cifra sale del cuaderno `reto_S08.ipynb` y de `leaderboard_S08.csv` de esta misma carpeta.

## 1. Resumen
El modelo calcula la **probabilidad de que una reserva se cancele**. El gerente de TurisData lo usará para **decidir a quién llamar o escribir un recordatorio** antes de la llegada. Lo usa recepción, con una persona que decide.

## 2. Modelo campeón
- **Familia y algoritmo:** lineal · regresión logística.
- **Hiperparámetros finales:** `max_iter=1000`; el resto, por defecto.
- **Preprocesado (`Pipeline`):** números con mediana y escalado; categorías con la más frecuente y *one-hot*.
- **Librerías y versiones:** Python 3.13, scikit-learn 1.9.1, xgboost 3.3.0, lightgbm 4.7.0. Semilla: `SEMILLA = 42`.

## 3. Por qué este campeón (y no otro)

**Pesos acordados:** rendimiento **50 %** (el gerente quiere avisar bien) · explicabilidad **30 %** (tiene que contárselo a recepción) · coste **20 %** (el hotel no tiene servidor propio).

| Criterio | Peso | Resultado del campeón (`logistica`) | Mejor rival y diferencia |
|---|---|---|---|
| Rendimiento (AUC en validación cruzada, 5 folds) | 50 % | 0,755 ± 0,014 | `lightgbm_ajustado` 0,747 ± 0,015: **0,008 menos**, menos que la desviación |
| Explicabilidad (1–5) | 30 % | 4 | `arbol_podado` 5: se lee como reglas, pero su AUC es 0,719 |
| Coste (ajuste, predicción, tamaño) | 20 % | 4,1 KB; ajuste en centésimas de segundo | `arbol_podado` 10,9 KB; el bosque pesa 11 847 KB |

**Puntuación global:** `logistica` 0,920 · `arbol_podado` 0,904 · `lightgbm_ajustado` 0,684. La ventaja sobre el árbol es **corta**.

**Análisis de sensibilidad (¿cambia el campeón si cambian los pesos?):**

| Pesos (rendimiento / explicabilidad / coste) | Campeón |
|---|---|
| 0,5 / 0,3 / 0,2 (acordados) | `logistica` |
| 0,8 / 0,1 / 0,1 (solo rendimiento) | `logistica` |
| 0,4 / 0,4 / 0,2 (equilibrado) | `arbol_podado` |
| 0,2 / 0,6 / 0,2 (explicabilidad primero) | `arbol_podado` |

**Lectura:** el campeón **cambia con los pesos**. Con los acordados gana la logística; si el cliente valora sobre todo entender el modelo, gana el árbol a cambio de unas 0,035 de AUC. Los modelos ajustados con búsqueda mejoran en milésimas (el bosque pasa de 0,737 a 0,744 y LightGBM de 0,745 a 0,747): no podemos asegurar que sean mejoras reales.

## 4. Datos de entrenamiento
- **Fuente:** `reservas_turisdata.csv` (datos sintéticos de un hotel de Canarias): **6000 reservas**; 4800 para entrenar y validar y 1200 de test, con la misma tasa de cancelación (**45,9 %**).
- **Variables usadas (conocidas al reservar):** antelación, noches, adultos, niños, precio por noche, peticiones especiales, cliente repetidor, cancelaciones previas, temporada alta, tipo de habitación, régimen, canal, país de origen, tarifa y depósito.
- **Variables excluidas:** `id_reserva` y las fechas (solo se usa la temporada derivada de la llegada). `cancelada` es lo que se predice.
- **Limitaciones:** datos sintéticos de un solo hotel; no hay años distintos ni cambios de política.

## 5. Rendimiento
- **Validación cruzada (train):** AUC 0,755 ± 0,014 · AP 0,718 · con el umbral 0,25: recall 0,93 y precisión 0,54.
- **Test (una sola evaluación):** **AUC 0,762**, unas 0,007 más que en validación: no hay sobreajuste. En `leaderboard_S08.csv` solo la fila del campeón tiene `auc_test`.
- **Umbral de decisión:** **0,25**, el del informe del Sprint 7: una cancelación no prevista cuesta unos 284 € y una falsa alarma unos 103 €, así que conviene avisar de más antes que perder cancelaciones.
- **Por canal (test, umbral 0,25):**

| Canal | Reservas | Cancelan de verdad | Avisadas | AUC |
|---|---|---|---|---|
| web_intermediaria | 607 | 55,4 % | **90,8 %** | 0,741 |
| agencia | 226 | 45,6 % | 76,5 % | 0,725 |
| empresa | 67 | 44,8 % | 77,6 % | 0,718 |
| directo | 300 | 27,3 % | **56,3 %** | 0,758 |

- **Por país de origen:** el AUC va de 0,710 (Alemania) a 0,796 (otros); las más pequeñas (Francia, 45 reservas) no permiten sacar conclusiones. La tasa de aviso es parecida entre países (67–82 %).

## 6. Uso previsto y usos NO previstos
- **Uso previsto:** **priorizar** llamadas o recordatorios a las reservas con probabilidad ≥ 0,25, empezando por las más altas.
- **NO usar para:** denegar reservas, cobrar más (o pedir depósitos distintos) a un canal o país concreto, ni tomar decisiones sin revisión humana.

## 7. Explicabilidad
Se explica con los *odds ratio* de la logística (las variables numéricas están escaladas: es por cada desviación típica más):
- **Reducen el riesgo:** depósito total (×0,43), canal directo (×0,54), tarifa no reembolsable (×0,60).
- **Aumentan el riesgo:** más antelación (×2,14), sin depósito (×1,87), canal web intermediaria (×1,62).

Frase para el gerente: «Se cancela más lo que se reserva con mucha antelación, sin depósito y a través de una web intermediaria; menos lo que lleva depósito total o llega por el canal directo».

## 8. Riesgos e IA responsable
- **Sesgo por canal:** se avisa al 91 % de las reservas de web intermediaria y al 56 % de las directas. Es en parte real (cancelan más), pero **la mayoría de avisadas de la web no iban a cancelar**: la precisión del conjunto es 0,54.
- **Falsas alarmas:** cliente que sí iba a venir y recibe una llamada o, si se sobrevende, un traslado. Por eso el aviso es una **llamada de recordatorio**, no una sanción.
- **Medido:** tasa de aviso y AUC por canal y país (apartado 5). **Pendiente:** medir el efecto de llamar, porque cambia el comportamiento del cliente.

## 9. Mantenimiento
- **Vigilar:** la tasa de cancelación real frente a la prevista y la tasa de aviso por canal (**deriva**). Si la cancelación real se desvía de forma sostenida de 45,9 %, hay que revisar.
- **Reentrenar:** cada temporada, o antes si salta la alerta anterior, con los mismos pasos del cuaderno.
- **Coste y responsable:** reentrenar tarda segundos; responsable: la persona de revenue management del hotel.

## 10. Cómo reproducirlo
`SEMILLA = 42` y las versiones del apartado 2. Abrir `reto_S08.ipynb` en Google Colab → *Entorno de ejecución → Reiniciar y ejecutar todo*. Sale el mismo leaderboard (`leaderboard_S08.csv`) y el mismo campeón; los tiempos de ajuste y predicción cambian de un ordenador a otro y con ellos la puntuación global (unas centésimas).
