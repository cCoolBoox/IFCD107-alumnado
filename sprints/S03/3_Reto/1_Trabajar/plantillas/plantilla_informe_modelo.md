# Informe del mejor modelo · TurisData Canarias

> **Máximo 4 páginas** (la tabla «Revisión con la rúbrica» del final no cuenta). Copiad este archivo a `sprint-03/informe_modelo.md` del repositorio del equipo y sustituid los `______` (cómo hacerlo: [subir a GitHub sin instalar nada](../../../../../material/5.%20Como_entregar_en_GitHub.md)). Borrad las notas en cursiva al terminar.
> Cada apartado dice de qué paso del [reto](../../3_Consultar/Reto_Sprint_03.md) sale. **Todo número sale de vuestro cuaderno**, no de esta plantilla ni de la guía. Las tres partes que pide el cliente son: el modelo (apartados 1 a 3, 6 y 7), la llamada a la API (4) y los recursos y costes (5). Cómo se evalúa: [entrega y rúbrica](../../2_Entregar/entrega_y_rubrica.md).

**Equipo:** ______ · **Fecha:** ______ · **Personas:** ______

## 1 · El problema, los datos y la métrica (pasos 1 y 2)

- **Qué predecimos y para qué:** queremos predecir ______ para que el equipo de reservas pueda ______.
- **Los datos:** `reservas_turisdata.csv`, ______ reservas y ______ columnas, sintéticas. Se cancelan el ______ %.
- **Columnas excluidas y por qué:** ______. *(Revisamos las 18 columnas, una a una, con la pregunta «¿la tendríamos el día de la reserva?». Decid cuáles quedan fuera y por qué; y por qué las demás se conocen al reservar.)*
- **Métrica elegida y por qué:** ______ *(con vuestras palabras: qué mide y por qué sirve más que «el porcentaje de aciertos»)*.

## 2 · Modelos comparados y umbral de decisión (pasos 2 y 3)

- **Partición:** entrenamos con las reservas más antiguas (______ filas, del ______ al ______) y evaluamos con las más recientes (______ filas, del ______ al ______), no con las mismas con las que entrenó.
- **Modelos comparados** *(los tres primeros del leaderboard son suficientes)*:

| Modelo | `score_test` | `score_val` | `fit_time` |
|---|---|---|---|
| ______ | ______ | ______ | ______ |
| ______ | ______ | ______ | ______ |
| ______ | ______ | ______ | ______ |

- **Modelo elegido y por qué:** ______ *(no solo «tiene el número más alto»: ¿cuánto gana al segundo?, ¿cuánto tarda?)*.
- **Nuestros importes:** una cancelación no prevista cuesta ______ € porque ______; una alerta falsa cuesta ______ € porque ______. *Son supuestos nuestros, a validar con TurisData.*
- **Umbral elegido:** ______ . **Coste** con ese umbral: ______ € · avisar a todos: ______ € · no avisar nunca: ______ €.
- **En una frase para un directivo:** «Recomendamos avisar cuando el riesgo supere el ______ %: así detectamos ______ de cada 10 cancelaciones, aunque ______ de cada 10 alertas serán falsas.»

## 3 · Qué pesa más y cómo repetirlo (pasos 2 y 4)

- **Variables que más pesan:** ______, ______ y ______. ¿Tienen sentido para el negocio? ______ ¿Alguna parece una fuga de datos? ______
- **Cómo repetirlo:** datos `reservas_turisdata.csv` · AutoGluon versión ______ · preset `medium_quality` · límite de tiempo ______ s · semilla 42 · partición 80 % más antiguo / 20 % más reciente por `fecha_reserva` · para publicar el servicio: celdas 8 a 10 del cuaderno con `UMBRAL` = ______.

## 4 · Evidencia de la llamada a la API (paso 4)

Petición y respuesta reales, **sin claves**. *(Pegad el texto de la salida de la celda 10 del cuaderno, tal cual sale, dentro del bloque.)*

```text
______
```

Qué significa la respuesta: ______ *(probabilidad, alerta y umbral, en una frase)*.

## 5 · Recursos y costes, con la prueba de cierre (paso 5)

| Recurso | Cuándo se creó | Tiempo usado | Coste | ¿Cerrado? | Prueba |
|---|---|---|---|---|---|
| Sesión de Colab | ______ | ______ | 0 € | ______ | `captura_cierre.png` |
| Modelo guardado (`modelo_cancelaciones`) | ______ | ______ | 0 € | ______ | |
| Datos descargados (`reservas_turisdata.csv`) | ______ | ______ | 0 € | ______ | |
| Servicio (API de prueba) | ______ | ______ | 0 € | ______ | |

**Captura del cierre:** el fichero `captura_cierre.png`, en esta misma carpeta `sprint-03/`. *(Si el informe es un PDF, pegad la captura aquí dentro y borrad esta frase.)*

En una plataforma de pago ______ *(una frase: qué se cobraría y por qué cerrar importa; sin inventar precios)*.

## 6 · Riesgos de IA responsable (paso 6)

| Riesgo | Qué vemos | Medida |
|---|---|---|
| ______ | ______ | ______ |
| ______ | ______ | ______ |

## 7 · Recomendación al cliente (paso 6)

Cuando llegue una alerta, ______. El modelo sirve para ______ y no sirve para ______. Antes de fiarse de los euros, TurisData debería ______.

## Revisión con la rúbrica

*Rúbrica completa en [entrega y rúbrica](../../2_Entregar/entrega_y_rubrica.md). La rellena una persona que **no escribió esa parte**: ejecutar los pasos del apartado 3 con solo este informe, leerlo como si fuera el director de TurisData, mirar las capturas, poner un nivel con su prueba.*

**Revisado por:** ______ · **Fecha:** ______

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
|---|---|---|
| Corrección técnica | | |
| Reproducibilidad | | |
| Análisis y comunicación al cliente | | |
| IA responsable | | |

**Lo primero que mejoraríamos:** ______
