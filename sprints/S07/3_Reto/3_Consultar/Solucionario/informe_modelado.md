# Informe de modelado · TurisData Canarias · «Precio y cancelación»

**Equipo:** de ejemplo (Solucionario) · **Fecha:** 11/11/2026

> Entrega de referencia: sirve de modelo de lo que hay que subir a `sprint-07/`. Cada cifra sale de `reto_S07.ipynb` (misma carpeta).

## 1. Resumen para el gerente
- Con 6000 reservas hemos construido dos modelos: uno estima el **precio por noche** y otro la **probabilidad de que una reserva se cancele**.
- El precio se estima con un error medio de **unos 7 €** (frente a 26 € si dijéramos siempre el precio medio).
- Una cancelación no prevista nos cuesta **unos 284 €** y una falsa alarma **unos 103 €** (hipótesis nuestras, con su razón en el apartado 5).
- Con el umbral elegido (0,25), en 1200 reservas de prueba el coste baja de **156 484 € a 58 331 €**: un ahorro de **98 153 € (63 %)**.
- Avisaremos de muchas reservas que al final no se cancelan: de cada 100 avisos, solo 53 son cancelaciones reales.
- Recomendamos usarlo para **priorizar a quién llamar**, no para decidir solo.

## 2. Datos y variables
- **Filas:** 6000 reservas de un hotel de Canarias (datos sintéticos), 20 columnas.
- **Usadas para el precio:** tipo de habitación y temporada alta.
- **Usadas para la cancelación (15):** antelación, noches, adultos, niños, precio por noche, peticiones especiales, cliente repetidor, cancelaciones previas, temporada alta, tipo de habitación, régimen, canal, país de origen, tarifa y depósito. Todas se conocen **al reservar**.
- **Excluidas:** `cancelada` (no se usa para predecir el precio: es posterior a la reserva), `id_reserva` y las fechas sueltas (solo se usa la temporada derivada de la llegada).
- **Partición:** 80 % entrenamiento (4800) y 20 % test (1200); la de cancelación, estratificada (45,9 % de canceladas en las dos). Semilla 42.

## 3. Regresión: precio por noche

| Modelo | MAE (€) | RMSE (€) | R² |
|---|---|---|---|
| Referencia (precio medio de entrenamiento) | 25,56 | 33,33 | −0,002 |
| Regresión lineal | 7,24 | 9,70 | 0,915 |
| Lineal con interacciones | 6,76 | 8,94 | 0,928 |

**Lectura para el cliente:** el precio base de una habitación estándar en temporada baja es **67 € por noche**; una suite cuesta **unos 101 € más**, una familiar 45 € más, una superior 28 € más y la temporada alta suma **unos 22 €**.

**Mejora probada:** con interacciones el error baja unos 0,5 €. **No compensa la complejidad:** perdemos la lectura sencilla de «tarifa más suplementos» por medio euro.

**Dónde falla:** en las suites (error medio de 14,6 € frente a 5,4 € en las estándar), porque su precio varía más de una reserva a otra (desviación de 24,5 € frente a 10,9 € en las estándar) y el modelo solo conoce el tipo de habitación y la temporada.

## 4. Clasificación: cancelación

| Modelo | AUC | AP | Recall (umbral 0,25) | Precisión (umbral 0,25) |
|---|---|---|---|---|
| Referencia (siempre «no cancela») | 0,500 | 0,459 | 0 % | — |
| Regresión logística | 0,746 | 0,729 | 92 % | 53 % |
| k-NN (extra, k = 201; validación cruzada) | 0,730 ± 0,017 | — | — | — |

**Cómo se lee, sin jerga:** el AUC dice qué tal ordena el modelo las reservas de menos a más arriesgadas: 0,5 es el azar y 1 es perfecto. La logística saca 0,75; sirve para priorizar, no para acertar siempre. La logística en validación cruzada saca 0,758 ± 0,012, así que k-NN no la mejora.

**Matriz de confusión en test (umbral 0,25):**

| | Dice «se mantiene» | Dice «cancela» |
|---|---|---|
| Se mantuvo | 204 (VN) | 445 (FP) |
| Canceló | 44 (FN) | 507 (VP) |

**Factores que más cambian el riesgo** (*odds ratio*; las numéricas, por cada desviación típica más):
- **Lo reducen:** tarifa no reembolsable (×0,44), depósito total (×0,46), canal directo (×0,55).
- **Lo aumentan:** más antelación (×2,12), sin depósito (×2,00), canal web intermediaria (×1,70).

## 5. De las métricas a los euros
- **Coste de una cancelación no prevista (FN): 284 €** por reserva. Reserva media de 5,5 noches a unos 103 €; solo se revende la mitad de las noches (0,5 × 5,52 × 102,87 ≈ 284 €).
- **Coste de una falsa alarma (FP): 103 €** por reserva. Una noche de compensación (otro alojamiento y una disculpa), más o menos el precio medio de una noche.
- **Umbral elegido con validación cruzada sobre train: 0,25**, el que menos cuesta. El test no se usó para elegirlo.
- **Coste en test:** sin modelo **156 484 €** · umbral 0,5 **78 439 €** · umbral elegido (0,25) **58 331 €**.
- **Análisis de sensibilidad** (coste mínimo en validación cruzada sobre las 4800 reservas de train):

| Hipótesis | COSTE_FN | COSTE_FP | Umbral óptimo | Coste con modelo | Sin modelo |
|---|---|---|---|---|---|
| La nuestra | 284 | 103 | 0,25 | 223 121 € | 625 652 € |
| FN el doble | 568 | 103 | 0,15 | 249 011 € | 1 251 304 € |
| FP la mitad | 284 | 51,5 | 0,15 | 124 506 € | 625 652 € |
| FP el doble | 284 | 206 | 0,40 | 354 720 € | 625 652 € |

Si el FN cuesta más, el umbral baja (se avisa más); si el FP cuesta más, sube (se avisa menos). **Siempre sale a cuenta usar el modelo**, pero el umbral va de 0,15 a 0,40: hay que confirmar con el cliente lo que cuesta una falsa alarma.

## 6. Recomendación de negocio
- **Acción:** llamar o enviar un recordatorio a las reservas con probabilidad de cancelación ≥ 0,25, empezando por las más altas.
- **Beneficio esperado:** unos **98 000 € menos de coste** en las 1200 reservas de prueba (63 % frente a no hacer nada).
- **Límites:** datos sintéticos de un solo hotel; los costes son hipótesis (ver sensibilidad); el comportamiento de los clientes puede cambiar cuando empecemos a llamar; el modelo avisa mucho (precisión 53 %).

## 7. IA responsable
- **Quién sufre los falsos positivos:** los clientes que sí iban a venir y reciben una llamada, o un traslado si se sobrevende. De las 1200 reservas de prueba, **445** fueron falsas alarmas.
- **Canal:** con el umbral 0,25 se avisa al **90 %** de las reservas de web intermediaria y al **60 %** de las directas (cancelan de verdad el 54 % y el 32 %). En parte es real, pero muchas avisadas de la web no iban a cancelar.
- **Medidas:** no usar el aviso para denegar reservas ni para cobrar depósitos distintos según canal o país; revisar cada temporada la tasa de aviso por canal; el aviso lo decide siempre una persona.

## 8. Cómo reproducirlo
Python 3.13, scikit-learn 1.9.1, pandas 2.3.3. `SEMILLA = 42`. Abrir `reto_S07.ipynb` en Colab y *Entorno de ejecución → Reiniciar y ejecutar todo*. Detalle en el [README](README.md).

## Revisión con la rúbrica

**Revisado por:** Persona D (no escribió el informe) · **Fecha:** 11/11/2026

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
|---|---|---|
| Corrección técnica | 3 | Hay baselines, matriz, curvas ROC y PR, umbral elegido con validación cruzada sobre train y sensibilidad; el test se usa una sola vez y sin fuga |
| Reproducibilidad | 3 | Ejecutado en una sesión nueva con solo el README: mismas cifras (MAE 7,24 €, coste 58 331 €); versiones y semilla indicadas |
| Análisis y comunicación al cliente | 3 | El resumen está en euros y se entiende sin saber qué es el AUC; la recomendación tiene cifras y límites; falta probar el *overbooking* |
| IA responsable | 3 | El README dice qué se pidió, qué se revisó y qué se cambió; el informe mide la tasa de aviso por canal y nombra medidas |

**Lo primero que mejoraríamos:** estimar el ahorro de una política de *overbooking* en euros por temporada (extra 🔴).
