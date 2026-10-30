# Solucionario · Reto S03 «Primer modelo en producción»

**Cliente:** TurisData Canarias · **Equipo:** solución de referencia del docente · **Fecha:** 30/10/2026

> **Para qué sirve este documento:** es **una** forma correcta de resolver el reto, para **compartirla y debatirla** en clase. No es la única ni es perfecta: al final hay preguntas para discutir. Los datos son **sintéticos** (inventados para el curso). **Los importes de coste de este informe son los de este equipo y se razonan con los datos (apartado 1.4); no son los 100 € y 40 € de ejemplo del cuaderno.** Cada equipo debe razonar los suyos. Todas las cifras se pueden repetir: el apartado «De dónde salen los datos» (después del informe) dice cómo, en Colab y en local.

---

# Parte 1 · Informe del mejor modelo

## 1.1 El problema y la métrica

**Qué queremos predecir:** si una reserva se cancelará (`cancelada` = 1) **con la información que se conoce en el momento de reservar**, para que el equipo de reservas actúe antes (llamar, ofrecer un cambio de fecha, reasignar la habitación).

**Los datos:** 6.000 reservas entre el 01/01/2024 y el 30/12/2025. **Se cancelan 2.754 (45,9 %).** En `pais_origen` faltan 138 valores (2,3 %); no se han borrado, el modelo los trata como «sin dato».

**Columnas excluidas y por qué**
- `cancelada`: es lo que queremos predecir.
- `id_reserva`: es solo un número de identificación. No describe la reserva y el modelo podría aprender «trucos» del orden de los números.
- **Revisadas una a una las otras 16:** todas se conocen al reservar. `fecha_llegada` es la fecha de reserva más la antelación, y `cancelaciones_previas` cuenta las cancelaciones **anteriores** del cliente. Ninguna se rellena después de que la reserva se cancele, así que **no hay fuga de datos**.

**Métrica elegida: ROC-AUC**, con los euros como criterio final.
- Con casi la mitad de reservas canceladas, la exactitud engaña poco, pero sigue sin decir nada sobre **a quién avisar**: «nadie cancela» ya acierta el **51,9 %** en el periodo de prueba.
- El AUC mide si el modelo **ordena** las reservas de más a menos riesgo (0,5 = azar, 1 = perfecto) y **no depende del umbral**. El umbral se decide después, con costes (apartado 1.4).

## 1.2 Cómo se evaluó: partición por fecha

Se entrena con el pasado y se prueba con el futuro, como pasará en la realidad:

| | Filas | Periodo (fecha de reserva) | % de cancelaciones |
|---|---|---|---|
| Entrenamiento | 4.800 | 01/01/2024 – 06/08/2025 | 45,4 % |
| **Prueba (datos no vistos)** | **1.200** | **06/08/2025 – 30/12/2025** | **48,1 %** |

Todos los resultados de este informe, salvo que se diga lo contrario, son **sobre la prueba**.

## 1.3 Modelos comparados y modelo elegido

AutoML (AutoGluon 1.6.3, preset `medium_quality`, límite de 120 s, semilla 42) entrenó **10 modelos candidatos**:

| Modelo | AUC en prueba | AUC en validación interna |
|---|---|---|
| **WeightedEnsemble_L2 (elegido)** | **0,721** | 0,779 |
| CatBoost | 0,719 | 0,777 |
| LightGBMXT | 0,717 | 0,774 |
| LightGBM | 0,715 | 0,763 |
| XGBoost | 0,713 | 0,757 |
| Los otros 5 (ExtraTrees y RandomForest ×2, LightGBMLarge) | 0,691 – 0,705 | 0,740 – 0,752 |

Cada modelo se ajustó en entre 0,4 y 7 segundos (cambia de una ejecución a otra).

- **Elegido: el ensamblado**, que combina varios modelos. Gana por poco: el segundo, CatBoost, queda a 0,002. **Con una diferencia tan pequeña, un modelo único y más simple (CatBoost) sería igual de defendible**, y es más fácil de explicar.
- **El AUC cae de 0,78 a 0,72 al pasar de validación a prueba.** La validación interna de AutoGluon mezcla reservas de todo el periodo de entrenamiento; la prueba es el futuro. Es justo el efecto que se quiere detectar al partir por fecha: **si hubiéramos barajado, habríamos presumido de un 0,78 que no se mantendría**.

**Resultado con el modelo elegido (prueba, 1.200 reservas, 577 cancelaciones):** AUC **0,72**. El modelo ordena mejor que el azar, pero **no es un adivino**.

## 1.4 Umbral de decisión: con euros, no con la métrica

Una alerta se da cuando la probabilidad ≥ umbral. Hay dos formas de equivocarse, y **sus importes se razonan con los datos del cliente**, no se copian del cuaderno:

| Dato de partida (SQL) | Valor |
|---|---|
| Ingreso medio por reserva (`noches × precio_noche`) | **568 €** |

| Error | Supuesto del equipo | Importe |
|---|---|---|
| **Cancelación no prevista** | Si nos avisan con tiempo, revendemos la habitación y recuperamos el 60 % del ingreso; una cancelación que no vimos venir pierde ese 40 % (0,40 × 568 €) | **225 €** |
| **Alerta falsa** | Ofrecemos un 10 % de descuento a una reserva que no iba a cancelarse (0,10 × 568 € ≈ 57 €) más unos 5 € de tiempo del equipo | **60 €** |

**Son supuestos razonados, no cifras del cliente: hay que validarlos con TurisData.** Si cambian, cambia el umbral (ver más abajo, «¿Y si los importes fueran otros?»).

Umbral teórico = 60 / (60 + 225) = **0,21**. Lo comprobamos con los datos de prueba:

| Umbral | Alertas | No previstas | Alertas falsas | Coste (€) |
|---|---|---|---|---|
| 0,10 | 1.154 | 4 | 581 | 35.760 |
| 0,15 | 1.100 | 12 | 535 | **34.800** |
| **0,20 (elegido)** | **1.042** | **25** | **490** | **35.025** |
| 0,25 | 965 | 48 | 436 | 36.960 |
| 0,30 | 898 | 69 | 390 | 38.925 |
| 0,50 | 543 | 227 | 193 | 62.655 |
| 0,70 | 240 | 391 | 54 | 91.215 |
| *Referencia: no avisar nunca* | 0 | 577 | 0 | *129.825* |
| *Referencia: avisar a todos* | 1.200 | 0 | 623 | *37.380* |

**Umbral elegido: 0,20.** El mínimo de las pruebas está en 0,15 (34.800 €), pero la curva es **muy plana**: elegir 0,20 cuesta solo 225 € más (0,6 %), da **58 alertas menos** (1.042 frente a 1.100) y coincide con el umbral teórico (0,21).

**Lo que dice el resultado, sin adornos:**
- Frente a **no hacer nada**, el modelo ahorra **94.800 €** (−73 %) en estos 5 meses.
- Frente a **avisar a todos**, el ahorro es de **2.355 € (−6,3 %)**. Es poco. **«Avisar a todos» es una referencia fuerte** porque una cancelación perdida cuesta casi cuatro veces más que una alerta falsa y casi la mitad de las reservas se cancelan.
- **Con este umbral se avisa al 87 % de las reservas** (1.042 de 1.200): recall del 96 % (solo se escapan 25 cancelaciones), pero precisión del 53 %. La alerta, tal cual, **apenas distingue**.

**¿Y si los importes fueran otros?** Mismas 1.200 reservas, tres supuestos:

| Supuesto | No prevista | Alerta falsa | Umbral teórico | Nunca | Todos | Mejor umbral probado | Ahorro frente a «todos» |
|---|---|---|---|---|---|---|---|
| **Este equipo** | 225 € | 60 € | 0,21 | 129.825 € | 37.380 € | 0,15 (34.800 €) | 2.580 € (6,9 %) |
| Ejemplo del cuaderno | 100 € | 40 € | 0,29 | 57.700 € | 24.920 € | 0,20 (22.100 €) | 2.820 € (11,3 %) |
| Alerta casi gratis (un correo) | 225 € | 5 € | 0,02 | 129.825 € | 3.115 € | 0,05 (3.285 €) | **−170 € (−5,5 %)** |

**Con una alerta casi gratis el modelo no compensa:** avisar a todos es mejor. La conclusión depende más de **cuánto cuesta actuar** que del modelo.

**Conclusión:** el modelo aporta cuando **actuar cuesta o hay poca gente para hacerlo**. Si el equipo solo puede contactar a una parte de las reservas, el modelo sirve para **elegir a cuáles**:

| Si contactamos al… | Reservas | Cancelan de verdad | Cancelaciones capturadas |
|---|---|---|---|
| 10 % de más riesgo | 120 | 84,2 % | 101 de 577 (18 %) |
| 20 % de más riesgo | 240 | 77,5 % | 186 de 577 (32 %) |
| 30 % de más riesgo | 360 | 68,6 % | 247 de 577 (43 %) |
| *(media de todas las reservas)* | 1.200 | 48,1 % | 577 |

## 1.5 Variables que más pesan

Importancia por permutación (cuánto baja el AUC si se desordena esa columna):

| Variable | Importancia |
|---|---|
| `antelacion_dias` | 0,070 |
| `deposito` | 0,058 |
| `canal` | 0,039 |
| `tarifa` | 0,021 |
| Las demás (noches, peticiones, cancelaciones previas, habitación…) | < 0,005 |

**¿Tiene sentido para el negocio? Sí.** Se cancela más lo que se reservó con mucha antelación, **sin depósito**, a través de intermediarias y con tarifa flexible. Los datos del SQL lo confirman (apartado «De dónde salen los datos»): el % de cancelación sube del **27,6 %** (menos de 30 días de antelación) al **76,9 %** (180 días o más), y baja del **54,0 %** (sin depósito) al **26,4 %** (depósito total). Esto también apunta a una **medida de negocio sin IA**: pedir un depósito a las reservas lejanas.

---

# Parte 2 · Evidencia de la llamada a la API

El modelo se publicó como servicio local (FastAPI + uvicorn, puerto 8077) con el umbral 0,20. **Sin claves ni credenciales** (es un servicio local sin autenticación; en un servicio real habría que protegerlo). En Colab la misma llamada se hace con `TestClient` (celda del paso 10 del cuaderno) y la respuesta tiene exactamente este formato.

**Reserva de alto riesgo** (web intermediaria, sin depósito, tarifa flexible, 222 días de antelación):

```
$ curl -s -X POST http://127.0.0.1:8077/predecir -H "Content-Type: application/json" -d @reserva_alto_riesgo.json
{"probabilidad_cancelacion":0.919,"alerta":true,"umbral":0.2}
```

**Reserva de bajo riesgo** (directo, depósito total, no reembolsable, 14 días de antelación):

```
$ curl -s -X POST http://127.0.0.1:8077/predecir -H "Content-Type: application/json" -d @reserva_bajo_riesgo.json
{"probabilidad_cancelacion":0.0372,"alerta":false,"umbral":0.2}
```

**Datos mal formados** (`{"noches":0}`): el servicio **rechaza la petición** con `HTTP 422` en vez de inventarse una probabilidad.

**Qué hacer con una alerta (recomendación al cliente):** que una persona del equipo de reservas llame o escriba al cliente para confirmar. **La alerta no cancela ni cambia nada sola.**

---

# Parte 3 · Informe de recursos y costes

| Recurso creado | Uso | Coste |
|---|---|---|
| Datos: `reservas_turisdata.csv` | 6.000 filas, 0,66 MB (sintéticos) | 0 € |
| Entrenamiento AutoML | 13–17 s según la ejecución (límite fijado: 120 s), 2 CPU, sin GPU | 0 € |
| Modelo guardado | 225,6 MB en disco (carpeta `modelo_cancelaciones`) | 0 € |
| Servicio de predicción (API) | encendido solo mientras se hicieron las 3 llamadas | 0 € |
| **Total** | | **0 €** |

**Cuánto habría costado en una plataforma de nube de pago:** con unos 15 segundos de entrenamiento, el entrenamiento sería casi irrelevante. **El riesgo está en el servicio encendido**, que se cobra por hora **aunque nadie lo use**. Por eso el cierre importa.

**Prueba de cierre** (servicio parado, modelo borrado):

```
$ curl -s -o /dev/null -w "%{http_code}\n" --max-time 3 http://127.0.0.1:8077/salud
000                  ← nadie responde: el servicio está parado
$ rm -rf modelo_cancelaciones __pycache__
$ ls modelo_cancelaciones
ls: cannot access 'modelo_cancelaciones': No such file or directory
```

En **Google Colab** se hace con *Entorno de ejecución → Desconectar y eliminar entorno* y una captura de la pantalla.

---

# Riesgos de IA responsable y medidas

| Riesgo | Qué hemos visto | Medida |
|---|---|---|
| **Datos sintéticos** | Las relaciones están inventadas: nada de lo aprendido vale para decidir en un hotel real | Repetir con datos reales de TurisData (anonimizados) antes de usarlo; no presentar estas cifras como estadísticas del turismo |
| **Alertas falsas que molestan a clientes** | Con umbral 0,20, **490 de 623 reservas que se mantuvieron (79 %)** recibieron alerta | Mensaje amable y opcional (no «sabemos que vas a cancelar»); que una persona decida; medir quejas |
| **Trato desigual por canal o país** | Ver abajo | Revisar estas tablas cada trimestre; no usar la alerta para negar o cambiar condiciones a un cliente |
| **El modelo envejece** | La prueba ya cae de 0,78 a 0,72 al pasar al futuro; la cancelación sube del 45,4 % al 48,1 % | Reevaluar con reservas nuevas cada cierto tiempo y reentrenar si empeora |
| **Importes inventados** | Los 225 € y 60 € son supuestos del equipo | Validarlos con TurisData y repetir el cálculo del umbral con los reales |

**Revisión de sesgos (umbral 0,20, datos de prueba):**

| Canal | Reservas | % con alerta | % cancelan de verdad | Falsas alarmas (% de las que no cancelan) | Cancelaciones no previstas (% de las que cancelan) |
|---|---|---|---|---|---|
| web_intermediaria | 591 | 96,4 | 55,5 | 93,2 | 0,9 |
| agencia | 263 | 89,7 | 47,5 | 84,1 | 4,0 |
| empresa | 56 | 78,6 | 48,2 | 72,4 | 14,8 |
| directo | 290 | 66,2 | 33,4 | 56,0 | 13,4 |

- **El modelo no trata igual a todos los canales:** a un cliente que reserva por una web intermediaria se le avisa casi siempre (96 %), frente al 66 % de un cliente directo, y se equivoca (alerta falsa) en el 93 % de los que no cancelan. **Es en parte lógico** (esos clientes cancelan más: 55,5 % frente a 33,4 %), **pero la carga de molestias cae sobre ellos**. A la vez, en el canal directo se escapan más cancelaciones (13,4 % frente a 0,9 %).
- **Por país**, el % de alertas va del 81 % (FR, NL) al 89 % (IT, UK). Hay pocas reservas por país (43–325), así que **no se pueden sacar conclusiones firmes**. Las reservas **sin país** (22) reciben alerta en el 91 % y solo cancelan el 32 %: **el modelo trata «sin dato» como señal de riesgo**.
- **Qué haríamos si saliera desigual:** que la alerta solo se use para *ayudar* al cliente (confirmar, ofrecer cambio de fecha), **nunca** para penalizarlo, y revisar con el cliente si compensa tratar distinto a cada canal.

---

# Recomendación al cliente (en cuatro líneas)

1. **Usad el modelo para decidir a quién llamar primero,** no como una sentencia. Con el umbral 0,20 se avisa al 87 % de las reservas: si no hay gente para tantas llamadas, empezad por el 20 % de más riesgo, donde **cancelan 3 de cada 4**.
2. **Si avisar es casi gratis** (un correo automático), **avisad a todos:** el modelo apenas mejora esa referencia.
3. **Antes de fiarse de los euros, validad los importes con TurisData:** los 225 € y 60 € de este informe son supuestos razonados con los datos, no cifras del cliente.
4. **Cómo medir si funciona:** durante un mes, actuad solo sobre la mitad de las reservas con alerta (elegidas al azar) y comparad cuántas se cancelan en cada mitad. Si no hay diferencia, la acción no sirve, aunque el modelo acierte.

---

# Revisión con la rúbrica

**Revisado por:** docente · **Fecha:** 30/10/2026

| Criterio | Nivel (1–4) | Prueba |
|---|---|---|
| Corrección técnica | 4 | Partición por fecha; 10 modelos comparados; umbral con euros razonados con los datos y comparado con «avisar a todos» y «no avisar nunca»; API que responde y rechaza datos mal formados (422); recursos cerrados con prueba |
| Reproducibilidad | 4 | Datos, versión (AutoGluon 1.6.3), preset, semilla (42), partición y pasos para Colab y local en «De dónde salen los datos»; tres ejecuciones dieron las mismas cifras |
| Análisis y comunicación al cliente | 4 | Recomendación accionable, con límites, beneficio en euros frente a no hacer nada y cómo medirlo |
| IA responsable | 4 | Cinco riesgos con medida; sesgos por canal y país comprobados con datos; una persona decide siempre |

**Lo primero que mejoraríamos:** validar los importes con el cliente y probar el modelo con datos **reales**, que es lo que más puede cambiar las conclusiones.

---
---

# De dónde salen los datos

Este apartado explica **cómo llegar, paso a paso, a cada cifra del informe**: qué se ejecuta, dónde aparece el número y qué resultado se debe obtener.

## A. Qué hace falta

| Pieza | Valor con el que se obtuvieron las cifras |
|---|---|
| Datos | `reservas_turisdata.csv` (6.000 filas, 18 columnas). El cuaderno de Colab lo descarga solo; en local, `python generar_reservas_turisdata.py` (6.000 filas, semilla 42) |
| Laboratorio | `S3.5_lab_autogluon.ipynb` (Colab) o `S3.5_lab_autogluon.py` (local), en la carpeta `laboratorio_automl/` de la ficha del reto |
| Cálculos extra | `calcular_cifras_informe.py` (esta carpeta): SQL, umbrales y sensibilidad, sesgos, capacidad limitada. Lo que **no** imprime el laboratorio sale de aquí. Sus importes por defecto son los de este informe (225 € y 60 €) |
| Entorno de las cifras | Ordenador local: Python 3.13 · AutoGluon 1.6.3 · pandas 2.3 · scikit-learn 1.9 · 2 CPU, sin GPU y sin PyTorch |
| Ajustes | preset `medium_quality`, `eval_metric = roc_auc`, límite de tiempo 120 s, semilla 42, partición 80/20 por `fecha_reserva` |

## B. Pasos para repetirlo (unos 10 minutos)

**Elige uno de los dos caminos. En el curso se trabaja en Google Colab (B1); el ordenador local (B2) es opcional.** Las cifras del informe se obtuvieron en local; en Colab saldrán iguales o casi (ver apartado E).

### B1. En Google Colab (no hay que instalar ni crear carpetas)

1. **Abre el cuaderno** [`S3.5_lab_autogluon.ipynb` en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S03/Reto_S03/laboratorio_automl/S3.5_lab_autogluon.ipynb). Con el Colab gratuito basta (CPU, sin GPU). **Todo se guarda en el disco temporal de la sesión de Colab**: no hay carpeta que crear, y desaparece al cerrar la sesión.
2. **Ejecuta las celdas de arriba abajo, una a una** (Mayús + Intro). La primera instala AutoGluon (2–3 min); si Colab pide reiniciar, acepta y sigue desde «0. Configuración». El cuaderno descarga solo el CSV y la API, y deja el límite de entrenamiento en 120 s.
3. **En la celda del paso 6b, cambia los dos importes** (`COSTE_NO_PREVISTA` y `COSTE_ALERTA_FALSA`) por los de tu equipo. En este informe son 225 y 60; el cuaderno trae 100 y 40 solo como ejemplo. Ejecútala.
4. **Cifras extra:** añade una celda al final y ejecútala (descarga el script y lo ejecuta sobre el modelo que acabas de entrenar; **hay que estar en la misma sesión**, porque el modelo vive en ella):

   ```python
   import urllib.request
   urllib.request.urlretrieve(
       "https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/sprints/S03/Reto_S03/Solucionario/calcular_cifras_informe.py",
       "calcular_cifras_informe.py")
   !python calcular_cifras_informe.py
   ```

   Con tus importes y tu umbral: `!COSTE_NO_PREVISTA=150 COSTE_ALERTA_FALSA=30 UMBRAL=0.2 python calcular_cifras_informe.py`.
5. **Llamada a la API:** antes de la celda del paso 10, ejecuta una celda con `import os; os.environ["UMBRAL"] = "0.2"`. Después de la celda del paso 10 (que usa `TestClient`), prueba las dos reservas del informe:

   ```python
   alto = {"fecha_reserva": "2026-01-10", "fecha_llegada": "2026-08-20", "antelacion_dias": 222, "noches": 7,
           "adultos": 2, "ninos": 0, "tipo_habitacion": "estandar", "regimen": "solo_alojamiento",
           "canal": "web_intermediaria", "pais_origen": "UK", "tarifa": "flexible", "deposito": "sin_deposito",
           "precio_noche": 95.0, "peticiones_especiales": 0, "cliente_repetidor": 0, "cancelaciones_previas": 0}
   bajo = {"fecha_reserva": "2026-01-10", "fecha_llegada": "2026-01-24", "antelacion_dias": 14, "noches": 4,
           "adultos": 2, "ninos": 1, "tipo_habitacion": "familiar", "regimen": "media_pension",
           "canal": "directo", "pais_origen": "ES", "tarifa": "no_reembolsable", "deposito": "total",
           "precio_noche": 120.0, "peticiones_especiales": 1, "cliente_repetidor": 1, "cancelaciones_previas": 0}
   print(cliente.post("/predecir", json=alto).json())
   print(cliente.post("/predecir", json=bajo).json())
   print(cliente.post("/predecir", json={"noches": 0}).status_code)   # 422: datos mal formados
   ```
6. **Cerrar:** *Entorno de ejecución → Desconectar y eliminar entorno*, y captura de la pantalla como prueba.

### B2. En tu ordenador (opcional)

1. **Crea una carpeta** y copia en ella `reservas_turisdata.csv`, `S3.5_lab_autogluon.py`, `api_cancelaciones.py`, `calcular_cifras_informe.py`, `reserva_alto_riesgo.json` y `reserva_bajo_riesgo.json` (están en `laboratorio_automl/` y en `Solucionario/evidencias/`). Abre una terminal **dentro de esa carpeta**.
2. **Instala** (Python 3.10–3.13): `pip install "autogluon.tabular[lightgbm,xgboost,catboost]" fastapi uvicorn httpx`.
3. **Entrena y evalúa:** `TIME_LIMIT=120 python S3.5_lab_autogluon.py`. Tarda unos 15 s y crea la carpeta `modelo_cancelaciones/`. (El importe del paso 6b del laboratorio es el de ejemplo; los de este informe los aplica el script del paso siguiente.)
4. **Cifras extra:** `python calcular_cifras_informe.py`. Con otros importes: `COSTE_NO_PREVISTA=150 COSTE_ALERTA_FALSA=30 UMBRAL=0.2 python calcular_cifras_informe.py`.
5. **Servicio y llamadas:** `UMBRAL=0.2 uvicorn api_cancelaciones:app --port 8077`; en **otra** terminal, `curl` como en la Parte 2. Con `http://127.0.0.1:8077/docs` se puede probar desde el navegador.
6. **Cerrar:** parar el servicio (`Ctrl + C`) y borrar `modelo_cancelaciones/`. Capturar la prueba.

## C. De dónde sale cada cifra

| Cifra del informe | De dónde sale | Cómo se obtiene |
|---|---|---|
| 6.000 reservas, 45,9 % canceladas (2.754), 138 sin país (2,3 %) | Laboratorio, paso **2** (exploración) y consultas SQL 1 y 7 | `print(datos.shape)` y `datos["cancelada"].mean()`; en SQL: `SELECT COUNT(*), SUM(cancelada) FROM reservas` |
| % de cancelación por antelación, depósito, tarifa y canal | `calcular_cifras_informe.py`, apartado **A** (SQL) | `SELECT canal, ROUND(100.0*AVG(cancelada),1) FROM reservas GROUP BY canal` (igual para depósito y tarifa; la antelación usa `CASE WHEN`) |
| **Ingreso medio por reserva: 568 €** | `calcular_cifras_informe.py`, apartado **A** (SQL), consulta «Ingreso medio» | `SELECT ROUND(AVG(noches*precio_noche),1) FROM reservas` |
| **Importes 225 € y 60 €** | **Supuestos del equipo** a partir de los 568 € (apartado 1.4) | `0,40 × 568 = 227 ≈ 225`; `0,10 × 568 + 5 = 62 ≈ 60` |
| Partición: 4.800 / 1.200 filas y fechas | Laboratorio, paso **3** | Se ordena por `fecha_reserva` y se corta al 80 %: `corte = int(len(datos) * 0.8)` |
| «Nadie cancela» acierta el 51,9 % | `calcular_cifras_informe.py`, apartado **B** | `1 − media de cancelada en la prueba` (1 − 0,481) |
| 10 modelos, AUC de prueba y validación | Laboratorio, paso **5** (leaderboard) | `predictor.leaderboard(prueba)`: columnas `score_test`, `score_val` y `fit_time` |
| AUC 0,721; alertas, precisión y recall por umbral | Laboratorio, paso **6** (y apartado **C** del script) | `roc_auc_score(y_real, prob)` con `prob = predictor.predict_proba(...)[1]` |
| Tabla de costes por umbral y umbral teórico 0,21 | `calcular_cifras_informe.py`, apartado **D** (el laboratorio, paso **6b**, hace lo mismo con los importes de ejemplo) | `coste = 225 × no_previstas + 60 × alertas_falsas`; teórico = 60 / (60 + 225) |
| «Nadie» 129.825 € y «todos» 37.380 € | Apartado **D** del script, última línea | `225 × 577` y `60 × 623` (577 canceladas y 623 no canceladas en la prueba) |
| Ahorro 94.800 € (−73 %) y 2.355 € (−6,3 %) | Cálculo a partir de la tabla anterior | `129.825 − 35.025` y `37.380 − 35.025`; el porcentaje es esa resta entre la referencia |
| Tabla «¿Y si los importes fueran otros?» | `calcular_cifras_informe.py`, apartado **D2** | Misma tabla con otros importes: el del cuaderno (100 y 40) y alerta casi gratis (225 y 5) |
| 10 / 20 / 30 % de más riesgo | `calcular_cifras_informe.py`, apartado **G** | Se ordena la prueba por probabilidad y se mira cuántas del grupo cancelan de verdad |
| Importancia de variables | Laboratorio, paso **7** | `predictor.feature_importance(prueba, num_shuffle_sets=3, subsample_size=1000)` |
| Sesgos por canal y país | `calcular_cifras_informe.py`, apartado **F** | Se agrupa la prueba por `canal` y `pais_origen` y se calcula: % con alerta, % que cancelan, falsas alarmas y no previstas |
| Probabilidades de la API (0,919 y 0,0372) | Parte 2, llamadas `curl` (local) o `TestClient` (Colab) | Servicio de `api_cancelaciones.py` con `UMBRAL=0.2`; las dos reservas están en `reserva_alto_riesgo.json` y `reserva_bajo_riesgo.json` |
| 13–17 s de entrenamiento, 225,6 MB | Laboratorio, paso **11** (informe de recursos) | `Tiempo de entrenamiento` y `Tamaño del modelo en disco` |
| Prueba de cierre | Terminal (local) o menú de Colab | `curl` a `/salud` (devuelve `000`) y `ls modelo_cancelaciones` (no existe); en Colab, captura de «Desconectar y eliminar entorno» |

## D. Consultas SQL que alimentan el informe

Se ejecutan en `sqlite` (en memoria, desde Python) sobre la tabla `reservas`, que es el CSV cargado tal cual:

```sql
-- % de cancelación por canal
SELECT canal, COUNT(*) AS reservas, ROUND(100.0*AVG(cancelada),1) AS pct
FROM reservas GROUP BY canal ORDER BY pct DESC;
```

| canal | reservas | pct |
|---|---|---|
| web_intermediaria | 3.020 | 53,9 |
| agencia | 1.190 | 44,0 |
| empresa | 328 | 43,3 |
| directo | 1.462 | 31,5 |

```sql
-- % de cancelación por antelación
SELECT CASE WHEN antelacion_dias<30 THEN '1) menos de 30 días'
            WHEN antelacion_dias<90 THEN '2) 30 a 89 días'
            WHEN antelacion_dias<180 THEN '3) 90 a 179 días'
            ELSE '4) 180 días o más' END AS antelacion,
       COUNT(*) AS reservas, ROUND(100.0*AVG(cancelada),1) AS pct
FROM reservas GROUP BY 1 ORDER BY 1;
```

| antelación | reservas | pct |
|---|---|---|
| menos de 30 días | 823 | 27,6 |
| 30 a 89 días | 2.740 | 39,1 |
| 90 a 179 días | 1.879 | 54,7 |
| 180 días o más | 558 | 76,9 |

```sql
-- Ingreso medio por reserva: base de los importes de coste
SELECT ROUND(AVG(noches*precio_noche),1) AS ingreso_medio_reserva FROM reservas;   -- 568,2
```

Depósito: sin depósito 54,0 % (3.292 reservas), parcial 40,9 % (1.799), total 26,4 % (909). Tarifa: flexible 51,9 % (3.619), no reembolsable 36,7 % (2.381).

## E. ¿Saldrá exactamente lo mismo?

- **En el mismo entorno, sí:** repetimos el laboratorio tres veces y salieron **las mismas cifras** (solo cambian los tiempos de entrenamiento).
- **En Colab, casi:** Colab tiene PyTorch y AutoGluon puede añadir modelos de redes neuronales, que aquí no se entrenaron. Además, las versiones cambian. **Esperad el mismo orden de magnitud** (AUC cerca de 0,72; ±0,02) y **comprobad las conclusiones**, no el último decimal: el ensamblado o un modelo de árboles arriba, y el mejor umbral entre 0,15 y 0,25 con los importes de este informe.
- Si **vuestros resultados son muy distintos**, revisad primero: ¿partición por fecha?, ¿importes de coste?, ¿límite de tiempo?, ¿se ha dejado `id_reserva`?
- Los importes (225 € y 60 €) **no son datos del cliente**: son supuestos razonados con el ingreso medio por reserva. Cambiarlos cambia el umbral y el ahorro, y es **lo que hay que debatir**.

---

# Para debatir en clase

1. **Elegimos el ensamblado por 0,002 de AUC sobre CatBoost.** ¿Merece la pena un modelo más difícil de explicar por tan poca mejora?
2. **El AUC baja de 0,78 a 0,72 al evaluar con el futuro.** ¿Qué habría pasado si hubiéramos barajado las reservas? ¿Cuál de los dos números se lo diríais al cliente?
3. **«Avisar a todos» queda a solo un 6,3 % del modelo.** ¿En qué casos compensa el modelo y en cuáles no? ¿Cuánto debería costar una alerta falsa para que no compense?
4. **Con el umbral 0,20 se avisa a 87 de cada 100 reservas.** ¿Es una «alerta» útil o es ruido? ¿Preferís el 20 % de más riesgo?
5. **El mínimo de coste está en 0,15 y elegimos 0,20.** ¿Es razonable perder 225 € por 58 alertas menos? ¿Qué criterio usaríais vosotros?
6. **Los 225 € y 60 € salen de suponer que se recupera el 60 % del ingreso y de un 10 % de descuento.** ¿Qué supuestos cambiaríais? ¿Cómo los validaríais con el cliente?
7. **El modelo avisa mucho más a las reservas de intermediarias que a las directas (96 % frente a 66 %).** ¿Es un sesgo injusto o un reflejo de los datos? ¿Qué se debería prohibir hacer con la alerta?
8. **Reservas sin país: 32 % cancelan, 91 % reciben alerta.** ¿Qué haríais con los datos que faltan?
9. **El depósito baja la cancelación del 54 % al 26 %.** ¿Es una medida mejor que cualquier modelo? ¿Qué haríais primero?
10. **¿Pondríais un 4 en todos los criterios de este informe?** ¿Qué le falta todavía? (Pista: los importes reales, los datos reales y la prueba de que la acción funciona).
