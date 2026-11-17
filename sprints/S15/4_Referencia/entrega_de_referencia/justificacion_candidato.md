# Justificación del candidato · BiciPrevisión · Las Palmeras IA

**Responsable:** Marta · **Fecha:** 03/12/2026 · **Partición:** por fechas (entrenamiento hasta 31/8/2012, validación sep–oct, test nov–dic reservado) · **Métrica:** MAE, el error medio en **bicis por hora** (menos es mejor) · **Datos:** huella `95d6bcad`

## 1. Tabla comparativa (validación en 5 bloques de 2 meses, sin usar el test)
Cada modelo se prueba 5 veces, siempre entrenando con lo anterior y probando en los 2 meses siguientes. La última prueba es la validación de sep–oct 2012, la del umbral de éxito.

| Modelo | MAE medio ± desv. (5 bloques) | MAE en sep–oct | Tiempo | Explicabilidad | Comentario |
|---|---|---|---|---|---|
| Baseline: igual que la semana pasada | 59,2 ± 9,2 | 69,5 | < 1 s | Total: una regla | Punto de partida (fila 1 del registro) |
| Baseline: media de 4 semanas | 49,7 ± 8,2 | 57,6 | < 1 s | Total | Mejor que el primero, sin aprender nada |
| Regresión lineal (Ridge) | 49,7 ± 6,4 | 53,9 | < 1 s | Alta: un peso por variable | No llega al umbral (≤ 52,1) |
| Bosque aleatorio | 43,0 ± 7,6 | 48,3 | 25,2 s | Media | Cerca del boosting, pero 8 veces más lento |
| Red neuronal (MLP, 3 semillas) | 66,9–70,4 (± hasta 20,4) | 57,3–74,3 | ≈ 39 s | Baja | **Peor que el baseline** y muy sensible a la semilla |
| Boosting sin clima | 67,2 ± 19,8 | 63,9 | 3,6 s | Media | No llega al umbral: el clima es clave |
| Boosting con clima, sin límite de profundidad | 40,8 ± 6,7 | 42,7 | 3,4 s | Media | Empata con el candidato |
| **Boosting con clima, profundidad 6 (candidato)** | **40,6 ± 6,8** | **42,2** | 3,1 s | Media (importancia por permutación) | **Candidato** |

Ajustes probados solo con validación (todos en `registro.csv`): profundidad 3 (43,3 ± 6,4) y 6; 150 y 600 árboles (41,2 ± 6,7 y 40,9 ± 7,0); bosque con hojas de 5 y de 20 muestras.

## 2. Por qué este modelo, y si la diferencia puede ser ruido
- **Elegimos el boosting de profundidad 6 (40,6 ± 6,8) frente al boosting sin límite de profundidad (40,8 ± 6,7): es un empate, la diferencia está dentro del ruido.** Desempatamos por simplicidad: árboles más pequeños, menos riesgo de memorizar y algo más rápido.
- **Frente al resto no es ruido.** Como la demanda cambia mucho entre bloques (invierno frente a verano), la desviación es grande para todos y comparar solo medias no basta. Comparando bloque a bloque, el candidato **gana al bosque en 4 de 5 bloques** (diferencia media de 2,5 bicis por hora), **a la regresión lineal en 5 de 5** (9,1) y **al baseline en 5 de 5** (18,7).
- **La red neuronal no compensa:** con las mismas variables queda por detrás del baseline y su resultado cambia mucho con la semilla (de 57,3 a 74,3 en la validación). Con unas 15.000 filas de tabla, los árboles aprovechan mejor la información y no hemos afinado más la red porque cada prueba cuesta unos 39 segundos.

## 3. Coste y beneficio
- **Beneficio:** en la validación de sep–oct el error baja de **69,5 a 42,2 bicis por hora (39 % menos)**, más del 25 % pactado (umbral: ≤ 52,1). En hora punta baja de 132,7 a 82,2 (38 %). En un día son unas **655 bicis menos mal planificadas**.
- **Coste:** entrena en 3,1 s, el modelo guardado pesa 1023 KB y no necesita equipo especial. Es menos explicable que una regresión (no hay un peso por variable), pero la importancia por permutación (apartado 5) permite contar qué pesa.
- **Dependencia del clima (riesgo R-01):** sin las variables de clima el error en validación es 63,9, una mejora de solo 8 %: **no cumple el umbral**. En el histórico el clima es el real; en producción será una previsión. Con un 10 % de error en el clima el modelo da 46,0 en la validación, que **sigue cumpliendo el umbral**. Recomendación: usarlo solo con una previsión del clima fiable y vigilar su error.

## 4. Resultado en test (nov–dic 2012), mirado **una sola vez** después de elegir
| | MAE | WAPE | MAE en hora punta |
|---|---|---|---|
| Candidato (HGB_prof6) | **44,0** | 23,3 % | 85,5 |
| Baseline (semana pasada) | 75,4 | 39,9 % | 140,6 |

El candidato falla 44,0 bicis por hora en el test, 1,8 más que en la validación: es lo esperable, porque la desviación entre bloques es de 6,8. Mejora al baseline un **42 %**. No hemos vuelto a elegir con este resultado, y no sabemos todavía cómo se porta en el huracán Sandy (29/10/2012, está en la validación y no lo hemos mirado aparte) ni por tipo de día: eso se mide en el Sprint 16.

## 5. Primera explicación (`explicacion_modelo.png`)
Importancia por permutación calculada en la validación con un modelo entrenado solo con el entrenamiento (el test no se usa). **La variable con más peso es la media de esa hora en las 4 semanas anteriores** (su desorden sube el error unas 174 bicis por hora), muy por encima de las demás: la mejor pista para mañana es qué pasó a esa hora en las últimas semanas. Después van la hora del día, la humedad y la misma hora de la semana pasada; entre humedad, tipo de tiempo y temperatura suman unas 22 bicis. El gráfico dice qué pistas usa el modelo, **no** que sean la causa: la humedad puede estar sustituyendo a «llueve» o a «hace frío», y como varias variables se parecen entre sí, sus pesos se reparten.

## 6. Hipótesis de por qué gana, contrastada (extra)
**Hipótesis:** gana porque la demanda depende a la vez de la hora y del tipo de día, y una regresión lineal no ve esos cruces. **Contraste** (validación, modelo entrenado solo con el entrenamiento):

| Franja | Horas | MAE regresión lineal | MAE candidato |
|---|---|---|---|
| Laborable, hora punta | 246 | 90,4 | 82,2 |
| Laborable, resto del día | 738 | 34,3 | 28,9 |
| Fin de semana y festivos | 480 | 65,3 | 42,2 |

**Se confirma a medias.** La mayor ganancia está en fines de semana y festivos (23,1 bicis por hora menos), donde la forma del día cambia mucho. En la hora punta de los laborables gana poco (8,2) y sigue siendo el punto débil: 82,2 bicis de error justo cuando más cuesta equivocarse. **Hay que mirarlo en el Sprint 16.**

## 7. Lo que no sabemos
- Cómo se porta con una previsión del clima real (solo hemos simulado un 10 % de error).
- Si sirve en otra ciudad o en otro año: tenemos 2 años y un solo operador, y la demanda crece un 64 % de 2011 a 2012.
- Si la diferencia con el bosque se mantendría con más datos.

## 8. Uso de la IA
- **Qué se pidió:** el código de la red neuronal, la validación cruzada y la importancia por permutación (marcado en `notas` del registro: «código generado con IA, revisado a mano»).
- **Qué se revisó:** cada línea de la red y de la validación; que el objetivo se escale para la red; que `early_stopping=False` (si no, el boosting reserva un trozo **barajado** del entrenamiento).
- **Qué se cambió y la fuga que vimos:** el código de validación de la IA **barajaba las horas** (`KFold` con `shuffle=True`). Dio un MAE de **26,7 ± 0,9** frente a 40,8 del mismo modelo validado por fechas: demasiado bueno, porque con horas barajadas el modelo ve el futuro de la misma semana. Lo sustituimos por bloques temporales y dejamos la prueba en el registro marcada «NO CANDIDATO». Además provocamos a propósito una fuga con `registered` (MAE 17,0) para reconocer una.
- **Un límite de la explicación:** la importancia por permutación mide cuánto usa una variable el modelo, no si la causa; con variables parecidas (temperatura y sensación térmica) reparte el peso y puede infravalorarlas.

---
## Revisión con la rúbrica

**Revisado por:** Persona D (no escribió la justificación) · **Fecha:** 03/12/2026

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
|---|---|---|
| Corrección técnica | 4 | Ejecuté el cuaderno entero: 14 modelos legítimos (con los 2 baselines) validados con los mismos bloques, red neuronal, ajustes solo con validación, 5 respuestas de fugas, test una vez y análisis por franjas que enseña dónde falla (hora punta) |
| Reproducibilidad | 4 | Con SEMILLA = 42 salieron las mismas cifras (repetí la prueba de Marta: 40,8 ± 6,7 otra vez); las 18 filas del registro llevan `datos_hash`, semilla y tiempo, y hay filas de las cuatro personas |
| Análisis y comunicación al cliente | 3 | La justificación dice si la diferencia es ruido y explica el test sin jerga; falta traducir las bicis de error a euros o a personas de redistribución con el coste real del cliente |
| IA responsable | 4 | Dice qué se pidió, qué se revisó y qué se cambió; cuenta una fuga concreta de la IA (validación barajada, 26,7 frente a 40,8) y un límite de la explicación del modelo |

**Lo primero que mejoraríamos:** pedir al cliente cuánto cuesta una bici mal colocada para expresar la mejora en euros, y mirar la hora punta, que sigue fallando mucho.
