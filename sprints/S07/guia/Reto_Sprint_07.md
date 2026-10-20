# Sprint 7 · Reto «Precio y cancelación»

> **Esta es la ficha completa del reto, explicada paso a paso** para quien nunca ha trabajado con esta metodología ni con IA. Léela entera **antes de empezar** y vuelve a ella cuando tengas dudas.
>
> - Si es tu primer reto, lee antes [Cómo se trabaja un reto](../../../material/4.%20Como_se_trabaja_un_reto.md).
> - Volver al [README del sprint](../README.md) · [Guía del sprint en PDF](Guia_Sprint_07.pdf) · [versión ecofriendly para imprimir](Guia_Sprint_07_ecofriendly.pdf).
> - **Este reto en PDF:** [a color](Reto_Sprint_07.pdf) · [ecofriendly, para imprimir](Reto_Sprint_07_ecofriendly.pdf).

## Ficha del reto

### En pocas palabras (léelo primero)

**Qué os pide el cliente.** El gerente de TurisData quiere **dos herramientas**:
1. Una **tarifa de referencia**: cuánto debería costar una noche según el tipo de habitación y la época (predecir un **número**: `precio_noche`).
2. Un **aviso de riesgo de cancelación**, para decidir cuándo vender por encima de su capacidad (*overbooking*: aceptar más reservas que habitaciones, apostando a que algunas se cancelarán) (predecir una **categoría**: `cancelada`, sí o no).

Y hay un detalle importante: **el gerente no quiere oír hablar de «AUC»**. Quiere saber **cuánto dinero se juega** si el modelo se equivoca en un sentido o en otro. Vuestro trabajo es **traducir métricas técnicas a euros**.

**Qué vais a hacer, en seis pasos:**
1. **Predecir el precio** (regresión): un modelo de referencia, una regresión lineal y una mejora.
2. **Predecir la cancelación** (clasificación): un modelo de referencia y una regresión logística (y, si queréis, un segundo modelo).
3. **Decidir cuánto cuesta cada tipo de error** (con hipótesis razonadas).
4. **Elegir el umbral** que minimiza el coste total.
5. **Probar qué pasa si esos costes cambian** (análisis de sensibilidad).
6. **Escribir un informe** de 2–3 páginas con una recomendación de negocio, con euros.

**Qué vais a entregar:** `informe_modelado.md` (o PDF), el cuaderno `reto_S07.ipynb` y un `README.md`.

**Qué vais a aprender haciéndolo:** a elegir métricas según el problema, a **evitar la fuga de datos**, a **traducir un modelo a dinero** y a defender una decisión con hipótesis claras.

**Cuánto tiempo:** unas 1 hora y 40 minutos en equipo entre el planning, el reto y la entrega (6 y 9/11). El reto se hace sobre todo el lunes 9/11, con lo aprendido el viernes.

**Núcleo y extra.** Núcleo: regresión del precio y clasificación de la cancelación con las hipótesis de coste. Extra: análisis de sensibilidad completo.

### Palabras que van a aparecer en este reto

| Palabra | Qué significa, en sencillo |
|---|---|
| **Regresión** | Predecir un número (el precio) |
| **Clasificación** | Predecir una categoría (cancela / no cancela) |
| **Baseline** | Modelo sencillo de referencia (por ejemplo, predecir siempre el precio medio) |
| **MAE** | Error medio en euros: «de media nos equivocamos en X €» |
| **RMSE** | Parecido al MAE, pero castiga más los errores grandes |
| **R²** | Cuánta parte de la variación del precio explica el modelo (de 0 a 1) |
| **Falso negativo (FN)** | El modelo dice «no se cancelará» y **sí se cancela** → habitación vacía |
| **Falso positivo (FP)** | El modelo dice «se cancelará» y **no se cancela** → cliente que llega y no hay sitio |
| **Umbral** | Probabilidad a partir de la cual decimos «se cancelará» |
| **Curva ROC / PR** | Gráficos que muestran cómo cambian los aciertos y errores al mover el umbral |
| **AUC / AP** | Un solo número que resume una curva ROC / PR. Mejor cuanto más alto |
| **Análisis de sensibilidad** | Comprobar si la decisión cambia cuando cambian los costes que habíamos supuesto |
| **Fuga de datos** | Usar información que no se conocería al decidir (por ejemplo, `cancelada` para predecir el precio) |
| **Overbooking** | Vender más habitaciones de las que hay, esperando cancelaciones |

**Contexto del cliente.** TurisData Canarias quiere dos cosas: (1) una **tarifa de referencia** que le diga cuánto debería costar una noche según el tipo de habitación y la época, y (2) un **aviso de riesgo de cancelación** para decidir cuándo vender por encima de su capacidad (*overbooking*). El gerente no quiere oír hablar de "AUC": quiere saber **cuánto dinero se juega** si el modelo se equivoca en un sentido o en otro.

**Qué se entrega.**
1. `informe_modelado.md` (o PDF), 2–3 páginas. Plantilla: [`plantillas/informe_modelado_plantilla.md`](../plantillas/informe_modelado_plantilla.md). Debe incluir la comparativa de métricas de los dos modelos y una **recomendación de negocio** (con euros).
2. `reto_S07.ipynb`: un modelo de **regresión** para `precio_noche` y otro de **clasificación** para `cancelada`, cada uno con su *baseline*, validación y métricas.
3. `README.md` para reproducirlo (semilla, versiones).

**La pregunta clave del informe.** *¿Qué cuesta más: una cancelación no prevista (habitación vacía) o una falsa alarma (cliente que llega y no hay sitio)?* Debéis **proponer una hipótesis de coste razonada** para cada error (por ejemplo, «solo se revende la mitad de las noches» o «una noche de compensación»), elegir el **umbral** que minimiza el coste y mostrar **qué pasa si esos costes cambian** (análisis de sensibilidad).

**Restricciones.**
- Solo variables **conocidas en el momento de reservar** (¡sin fuga!). `cancelada` no puede usarse para predecir el precio.
- El umbral se elige con validación cruzada sobre train; el test se usa una sola vez.
- Solo librerías del curso; semilla fija (`SEMILLA = 42`).
- Máximo 3 modelos por problema (baseline incluido).

**Criterios de evaluación** (0–4 cada uno; misma rúbrica de todos los retos):

| Criterio | 1 · Insuficiente | 2 · Suficiente | 3 · Bueno | 4 · Excelente |
|---|---|---|---|---|
| Corrección técnica | Errores que invalidan el resultado | Correcto con fallos menores | Correcto y bien justificado | Correcto, justificado y con alternativas comparadas |
| Reproducibilidad | No se puede volver a ejecutar | Se ejecuta con ayuda | Se ejecuta desde el README | Además incluye datos o script y versiones fijas |
| Análisis y comunicación al cliente | Solo código o cifras sin interpretar | Interpretación básica | Conclusiones claras para el cliente | Recomendación accionable con límites explicados |
| IA responsable | No se considera | Menciones genéricas | Riesgos específicos identificados | Medidas aplicadas y evaluadas |

*Pista de IA responsable:* ¿quién sufre los falsos positivos (un cliente reubicado)? ¿Se penaliza a algún país o canal? ¿Qué pasa si el modelo se usa para pedir depósitos solo a ciertos clientes?

**Pasos sugeridos.**
- **Viernes 6/11:** *planning* (20 min); las prácticas de regresión y de regresión logística preparan los modelos del reto.
- **Lunes 9/11 (2 h 15 min):** acordar las hipótesis de coste (15 min); regresión: baseline, lineal y una mejora, con métricas en euros (30 min); clasificación: baseline y logística, curva ROC/PR, elección del umbral con validación cruzada y coste total en test (45 min).
- **Cierre del lunes:** análisis de sensibilidad (15 min), informe con la recomendación y README (30 min), autoevaluación y coevaluación; **review + retrospectiva** (última hora).

### Guía paso a paso para principiantes

#### Paso 1 · Acordar las hipótesis de coste (lunes 9/11, 10 minutos; el planning fue el viernes)
1. Roles del sprint y tareas en el tablero.
2. **La pregunta central del informe:** *¿qué cuesta más, una cancelación no prevista (habitación vacía) o una falsa alarma (un cliente llega y no hay sitio)?*
3. **Proponed una hipótesis de coste para cada error**, razonada con una frase. Ejemplos:
   - Una cancelación no prevista cuesta **la mitad de una noche**, porque solo se revende la mitad de esas noches.
   - Una falsa alarma cuesta **una noche de compensación** (alojamiento en otro hotel + disculpa).
4. Escribidlas en el cuaderno como variables (`COSTE_FN`, `COSTE_FP`) para poder cambiarlas luego.

#### Paso 2 · Regresión del precio (lunes 9/11, 25 minutos)
1. Elegid las variables que **se conocen al reservar** (tipo de habitación, mes, antelación, canal…). **`cancelada` no puede usarse para predecir el precio** (es fuga).
2. Modelo de referencia: predecir siempre el precio medio de entrenamiento. Medid MAE y RMSE.
3. Regresión lineal. Medid MAE, RMSE y R². ¿Mejora al modelo de referencia?
4. Una mejora (añadir interacciones o regularización tipo Lasso). ¿Compensa la complejidad?
5. Expresad el resultado **en euros**: «nos equivocamos de media en X € por noche».

#### Paso 3 · Clasificación de la cancelación (lunes 9/11, 35 minutos)
1. Partid los datos (train/test) y **no toquéis el test hasta el final**.
2. Modelo de referencia (por ejemplo, el que siempre dice «no cancela»). Regresión logística. Opcional: un segundo modelo.
3. Dibujad la **matriz de confusión** y las curvas ROC y PR. Calculad AUC y AP.
4. **Elegid el umbral con validación cruzada sobre train**: probad muchos umbrales y calculad el coste total de cada uno con vuestras hipótesis: `coste = FN × COSTE_FN + FP × COSTE_FP`. El mejor umbral es el que **minimiza el coste**.
5. **Usad el test una sola vez**, al final, para dar el coste esperado.

#### Paso 4 · Análisis de sensibilidad (lunes 9/11, 10 minutos)
Preguntaos: *¿y si una noche vacía costara el doble? ¿y si la compensación costara la mitad?* Variad los costes y mirad **cómo cambia el umbral óptimo** y el coste total. Mostradlo en una tabla o gráfico. La conclusión es del tipo: *«con estos costes recomendamos un umbral de 0,35; si el coste de una falsa alarma sube al doble, el umbral sube a 0,45»*.

#### Paso 5 · Informe y README (lunes 9/11, 25 minutos)
Seguid la plantilla [`informe_modelado_plantilla.md`](../plantillas/informe_modelado_plantilla.md):
1. **Resumen para el gerente** (5 líneas, con euros).
2. Tabla comparativa de métricas de los dos modelos.
3. Umbral elegido y su coste frente a «no hacer nada».
4. Análisis de sensibilidad.
5. **Recomendación de negocio con cifras y límites.**
6. Riesgos de IA responsable.

README: semilla (`SEMILLA = 42`), versiones y cómo ejecutar.

### Cómo usar la IA en este reto

| Para qué | Ejemplo de petición | Qué tenéis que comprobar |
|---|---|---|
| Entender una métrica | «Explícame la diferencia entre MAE y RMSE con un ejemplo de precios de hotel» | Que podáis explicar cuándo conviene cada una |
| Entender falsos positivos y negativos | «Dame un ejemplo en un hotel de falso positivo y falso negativo de un modelo de cancelaciones» | Que los asociáis a **vuestros** costes |
| Depurar código | «Este código de scikit-learn da este error: *[error]*. ¿Qué lo causa?» | Que lo entendéis y lo arregláis |
| Revisar la recomendación | «Lee esta recomendación al gerente y dime si hay algo ambiguo o demasiado técnico» | Que no cambie las cifras |

**Reglas del reto:**
- **Las hipótesis de coste son vuestras:** si la IA os da cifras, preguntaos de dónde salen y justificadlas. No sirve «la IA dijo 200 €».
- **No dejéis que la IA elija el umbral por vosotros:** debe salir del cálculo con vuestros costes.
- Declarad el uso de IA en el README.

**Pista de IA responsable:** ¿quién sufre los falsos positivos (un cliente reubicado)? ¿Se penaliza a algún país o canal? ¿Qué pasa si el modelo se usa para pedir depósitos solo a ciertos clientes? Respondedlo en el informe.

### Errores frecuentes (y cómo evitarlos)

| Error | Por qué ocurre | Cómo evitarlo |
|---|---|---|
| Usar `cancelada` o información posterior para predecir el precio | No se piensa en el momento de la reserva | Haced una lista de variables y marcad cuáles se conocen **al reservar** |
| Elegir el umbral mirando el test | «Queda mejor» | El umbral sale de validación sobre train; el test, **una sola vez** |
| Costes sin justificar | Parece un detalle | Cada coste lleva una frase de razón |
| Informe solo con AUC | Es lo que muestra el cuaderno | Traducid a euros: «el modelo ahorra X € frente a no hacer nada» |
| Probar 10 modelos | «Más es mejor» | Máximo **3 modelos por problema**, baseline incluido |
| Olvidar el análisis de sensibilidad | Parece opcional | Es lo que da robustez a la recomendación |

### Un buen resultado se parece a…

> *«Recomendamos activar el aviso de cancelación con un umbral de 0,35. Con nuestras hipótesis (noche vacía = 50 €, compensación = 100 €), el coste esperado pasa de 4.200 € a 2.900 € por temporada, es decir, ahorra unos 1.300 €. Si la compensación costara 200 €, el umbral óptimo subiría a 0,45 y el ahorro bajaría a 800 €: la recomendación se mantiene, pero conviene medir el coste real. Límites: datos sintéticos de un solo hotel.»* (Cifras de ejemplo.)

### Antes de entregar: autoevaluación rápida

| Pregunta | Sí / No |
|---|---|
| ¿La regresión tiene baseline y métricas en euros (MAE, RMSE) y R²? | |
| ¿La clasificación tiene baseline, matriz de confusión, AUC/AP y umbral justificado? | |
| ¿Los costes de FN y FP son hipótesis explícitas con análisis de sensibilidad? | |
| ¿La recomendación tiene cifras y límites? | |
| ¿No hay fuga de datos y el test se usó una sola vez? | |
| ¿El cuaderno se ejecuta entero y el README tiene versiones y semilla? | |
| ¿Está subido a Git, con autoevaluación y coevaluación? | |

### Si os atascáis

- **No sabemos qué costes poner:** pensad en una noche de un alojamiento de TurisData y razonad con una frase; luego **variad** los costes en la sensibilidad.
- **No entendemos el umbral:** pensad en un semáforo: si ponemos el umbral muy bajo, avisamos casi siempre (muchas falsas alarmas); muy alto, casi nunca (muchas cancelaciones sin detectar).
- **El cuaderno da errores de dimensiones:** comprobad `X.shape` y `y.shape` y que habéis eliminado la variable objetivo de `X`.
- Más ayuda: [Cómo se trabaja un reto](../../../material/4.%20Como_se_trabaja_un_reto.md).

**Qué se enseña en la review** (5 min por equipo): la tabla comparativa de métricas, el umbral elegido y su coste en euros frente a «no hacer nada», y una frase de recomendación para el gerente.

**Preguntas de la retrospectiva:** ¿qué hipótesis de coste discutimos más? ¿Cómo cambia la decisión si cambia el coste? ¿Qué habríamos necesitado saber del hotel para afinar?

## Definition of Done (lista de comprobación)

Si queda una casilla sin marcar, **el reto no está terminado**.

- [ ] Modelo de regresión con baseline y métricas en euros (MAE, RMSE) y R².
- [ ] Modelo de clasificación con baseline, matriz de confusión, AUC/AP y umbral justificado.
- [ ] Costes de FN y FP explicitados como hipótesis y análisis de sensibilidad.
- [ ] Recomendación de negocio con cifras y límites.
- [ ] Sin fuga de datos; test usado una sola vez.
- [ ] Notebook ejecutable de principio a fin y README con versiones.
- [ ] Subido a Git; autoevaluación y coevaluación rellenadas.
