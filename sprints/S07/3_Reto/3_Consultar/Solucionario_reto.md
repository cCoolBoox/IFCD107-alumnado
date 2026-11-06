# Solucionario del reto · Sprint 7 · «Precio y cancelación»

> **Para contrastar y para entender**, no solo para copiar. El **código** de cada paso ya está en su [página del reto](Reto_Sprint_07_paso_2.md) (con «Qué hace cada línea»). Aquí están las cifras para comprobar y las respuestas de ejemplo de lo que se escribe con palabras propias. Volver a la [ficha del reto](Reto_Sprint_07.md).

## Índice

- [Cómo usarlo](#cómo-usarlo)
- [Las cifras que tienen que salir](#las-cifras-que-tienen-que-salir)
- [Paso 1 · Hipótesis de coste](#paso-1--hipótesis-de-coste)
- [Paso 2 · Regresión del precio](#paso-2--regresión-del-precio)
- [Paso 3 · Clasificación y umbral](#paso-3--clasificación-y-umbral)
- [Paso 4 · Sensibilidad](#paso-4--sensibilidad)
- [Paso 5 · Informe: respuestas de ejemplo](#paso-5--informe-respuestas-de-ejemplo)

## Cómo usarlo

- **Primero intentadlo.** Si algo falla: leed el error → «Si algo falla» de la página del paso → equipo → docente → **este solucionario**.
- **Después de mirarlo, cerradlo y volved a escribirlo con vuestras palabras.**
- Con **vuestros costes** saldrán otras cifras en euros. Lo que no cambia: la curva de coste tiene un mínimo claro y el umbral elegido cuesta menos que el 0,5.

## Las cifras que tienen que salir

| Dónde | Cifra | Qué es |
|---|---|---|
| Paso 1 | `(6000, 20)` | 6000 reservas y 20 columnas |
| Paso 1 | `102.87 €` por noche · `5.5` noches | Precio y estancia medios |
| Paso 1 | `COSTE_FN = 284` · `COSTE_FP = 103` | Ejemplo de hipótesis de coste |
| Paso 2 | `(4800, 4)` y `(1200, 4)` | *Train* y *test* de la regresión |
| Paso 2 | referencia MAE `25,564 €` · R² `−0,002` | El «modelo tonto» |
| Paso 2 | lineal MAE `7,239 €` · RMSE `9,704 €` · R² `0,915` | La tarifa con suplementos |
| Paso 2 | con interacciones MAE `6,758 €` · RMSE `8,936 €` · R² `0,928` | Mejora de unos 0,5 € |
| Paso 2 | precio base `67.3 €` · familiar `+45,0` · suite `+101,2` · superior `+28,4` · temporada alta `+22,4` | Coeficientes en euros |
| Paso 3 | `(4800, 15)` y `(1200, 15)` · `0.459` y `0.459` | Partición con la misma proporción de canceladas |
| Paso 3 | `Umbral elegido: 0.25` | El mínimo de la curva de coste |
| Paso 3 | coste en test: sin modelo `156,484 €` · umbral 0,5 `78,439 €` · elegido `58,331 €` | Ahorro de `98,153 €` (63 %) |
| Paso 3 | `VN 204 · FP 445 · FN 44 · VP 507` · precisión `53 %` · recall `92 %` | Matriz de confusión con el umbral 0,25 |
| Paso 3 | `AUC 0.746` · `AP 0.729` · referencia `0.500` y `0.459` | Calidad del clasificador |
| Paso 4 | umbral óptimo `0.25 → 0.15` (FN el doble) · `0.15` (FP la mitad) · `0.40` (FP el doble) | Cómo se mueve el umbral |

## Paso 1 · Hipótesis de coste

- **Falso negativo (cancelación no prevista), 284 €:** reserva media de 5,5 noches a unos 103 €; solo se revende la mitad (0,5 × 5,52 × 102,87 ≈ 284 €).
- **Falso positivo (falsa alarma), 103 €:** una noche de compensación (otro alojamiento y una disculpa), más o menos el precio medio de una noche.
- Lo importante no es la cifra exacta: es que **cada una tenga su razón escrita** y se pueda discutir con el cliente.

## Paso 2 · Regresión del precio

- Lectura para el cliente (en euros): «El precio base es 67 € por noche; una suite cuesta unos 101 € más que una estándar y la temporada alta suma unos 22 €.»
- «Con interacciones mejora solo unos 0,5 € de error medio: no compensa la complejidad.»
- Si vuestro R² está por debajo de 0,85 o el MAE fuera de 5–15 €, mirad la «Ayuda 2» de la ficha del reto.

## Paso 3 · Clasificación y umbral

- Lectura de la matriz con el umbral 0,25: «Avisamos mucho (precisión 53 %) para no perdernos casi ninguna cancelación (recall 92 %): un FN cuesta casi tres veces más que un FP.»
- **El umbral se elige con validación cruzada sobre *train***. Si se elige mirando el test, el coste en test deja de ser una prueba honesta.
- Comprobación: el coste con el umbral elegido tiene que ser **menor** que el del 0,5 y que el de «sin modelo».

## Paso 4 · Sensibilidad

```text
     hipótesis  COSTE_FN  COSTE_FP  umbral_optimo  coste_total  sin_modelo
0   la nuestra       284     103.0           0.25       223121      625652
1  FN el doble       568     103.0           0.15       249011     1251304
2  FP la mitad       284      51.5           0.15       124506      625652
3  FP el doble       284     206.0           0.40       354720      625652
```

- **Si el FN cuesta más, el umbral baja** (se avisa más); **si el FP cuesta más, el umbral sube** (se avisa menos).
- Frase de ejemplo: «La recomendación se mantiene en las cuatro hipótesis (siempre cuesta menos usar el modelo que no hacer nada), pero el umbral va de 0,15 a 0,40 según lo que cueste una falsa alarma: hay que confirmar ese coste con el cliente.»

## Paso 5 · Informe: respuestas de ejemplo

**1. Resumen para el gerente (6 líneas)**

- «Hemos construido dos modelos con 6000 reservas: uno estima el precio por noche y otro la probabilidad de cancelación.»
- «El precio se estima con un error medio de unos 7 €.»
- «Una cancelación no prevista nos cuesta unos 284 € y una falsa alarma unos 103 €.»
- «Con el umbral elegido (0,25) el coste baja de 156 000 € a 58 000 € en las 1200 reservas de prueba: un ahorro del 63 %.»
- «Avisaremos de muchas reservas que al final no se cancelan (precisión del 53 %).»
- «Recomendamos usarlo para **priorizar a quién llamar**, no para decidir solo.»

**6. Recomendación de negocio (ejemplo)**

- Acción: llamar o enviar un recordatorio a las reservas con probabilidad ≥ 0,25, empezando por las más altas.
- Beneficio esperado: unos 98 000 € menos de coste en el conjunto de prueba (63 %).
- **Límites:** datos sintéticos, un solo hotel, los costes son hipótesis (ver sensibilidad) y el comportamiento puede cambiar si empezamos a llamar.

**7. IA responsable (ejemplo)**

- Riesgo: el canal y el país pueden hacer que el modelo avise más a unos clientes que a otros.
- Medidas: no usar el aviso para denegar reservas ni para cobrar depósitos distintos; revisar la tasa de aviso por canal.
- Decir **qué se pidió a la IA, qué se revisó y qué se cambió**, con un caso concreto.
