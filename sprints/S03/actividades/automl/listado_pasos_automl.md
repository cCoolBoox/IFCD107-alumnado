# Listado de pasos y preguntas de AutoML · S03 (cuaderno S3.5_lab_autogluon)

> **Qué es:** el índice de todo lo que hay que hacer en el laboratorio de AutoML, para saber **qué toca** y **llevar la cuenta**. A diferencia de SQL y NoSQL, aquí **no hay celdas con `...` que rellenar**: el cuaderno ya trae el código y vuestro trabajo es **ejecutarlo, leer el resultado y responder**. Cómo abrirlo: apartado 1 de la [guía en parejas](guia_automl_en_parejas.md).

**Cómo usarlo:** marcad la casilla cuando la celda haya terminado **y** tengáis anotado vuestro dato en la hoja de registro. Después podéis contrastar con el [solucionario paso a paso](soluciones_automl_paso_a_paso.md).

**Orden:** de arriba abajo, **una celda cada vez**. Si reiniciáis el entorno de Colab, volved a ejecutar desde el paso 0. Las cifras de la guía son orientativas: en el informe van **las vuestras**.

**Archivo:** [`S3.5_lab_autogluon.ipynb`](../../Reto_S03/laboratorio_automl/S3.5_lab_autogluon.ipynb) · [Abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S03/Reto_S03/laboratorio_automl/S3.5_lab_autogluon.ipynb)

## Qué datos usa

Un CSV con **6.000 reservas y 18 columnas**, [`reservas_turisdata.csv`](../../Reto_S03/laboratorio_automl/reservas_turisdata.csv) (la celda 0 lo descarga sola). Son las columnas de la tabla `reservas` de `turisdata.db`, sin `id_cliente` ni `id_alojamiento`; las explica el [esquema de turisdata.db](../esquema_turisdata/esquema_turisdata.md).

| Grupo | Columnas |
|---|---|
| Identificador (no se usa para predecir) | `id_reserva` |
| Fechas | `fecha_reserva`, `fecha_llegada`, `antelacion_dias` |
| La estancia | `noches`, `adultos`, `ninos`, `tipo_habitacion`, `regimen`, `precio_noche` |
| Cómo se reservó | `canal`, `tarifa`, `deposito`, `peticiones_especiales` |
| El cliente | `pais_origen` (138 vacíos), `cliente_repetidor`, `cancelaciones_previas` |
| **Lo que predecimos** | **`cancelada`** (`1` = se canceló, `0` = no) |

---

## En clase (≈ 100 minutos)

| ✓ | Paso | Qué se hace | Dato que hay que anotar |
|---|---|---|---|
| □ | **Instalación** | Instalar AutoGluon (2–3 min) y, si Colab lo pide, reiniciar el entorno | — |
| □ | **0 · Configuración** | Descargar el CSV y fijar `LIMITE_TIEMPO` (120 s) y la semilla | — |
| □ | **1 · Cargar** | Leer el CSV y ver las primeras filas | Forma de la tabla: **(6000, 18)** |
| □ | **2 · Explorar** | Tipos de dato, nulos, proporción de cancelaciones, resumen numérico | % de cancelaciones y columna con nulos |
| □ | **3 · Partición temporal** | Entrenar con el 80 % más antiguo, probar con el 20 % más reciente | Filas y fechas de cada parte |
| □ | **4 · Entrenar** | `TabularPredictor.fit(...)`: AutoGluon prueba modelos y elige el mejor | Mejor modelo y tiempo de entrenamiento |
| □ | **5 · Leaderboard** | Tabla de candidatos con `score_test`, `score_val` y `fit_time` | `score_test` del mejor |
| □ | **6 · Evaluar** | Precisión, recall, F1, ROC-AUC y matriz de confusión con umbral 0,5 y 0,3 | Precisión y recall de cada umbral |
| □ | **6b · Umbral con costes** | Poner precio a los errores y buscar el umbral más barato | **Vuestros costes** y umbral elegido |
| □ | **7 · Importancia de variables** | Ver qué columnas pesan más | Las tres primeras |
| □ | **8 · Guardar y recargar** | Guardar el modelo en `modelo_cancelaciones` y volver a cargarlo | Probabilidades de ejemplo |
| □ | **9 · Función de predicción** | Predecir **una** reserva suelta | Probabilidad y alerta |
| □ | **10 · API** | Llamar a `/salud` y `/predecir` con `TestClient` | Código de respuesta (200) |
| □ | **11 · Informe de recursos** | Tiempo, tamaño del modelo, coste | Tiempo, MB, 0 € |
| □ | **Cerrar** | *Entorno de ejecución → Desconectar y eliminar entorno* | Captura de la prueba |

## Preguntas del cuaderno (se responden en pareja y se anotan)

| ✓ | Paso | Pregunta |
|---|---|---|
| □ | **2** | ¿Está **desbalanceada** la clase objetivo? ¿Qué métrica conviene? |
| □ | **2** | ¿Qué columnas podrían provocar **fuga de datos** (información posterior al desenlace)? |
| □ | **3** | ¿Por qué se parte **por fechas** y no al azar? |
| □ | **5** | ¿El mejor modelo es un **ensamblado**? ¿Cuánto tarda cada uno? ¿Merece la pena el coste de cómputo? |
| □ | **5** | ¿Por qué `score_val` es **más alto** que `score_test`? |
| □ | **6** | ¿Qué cuesta más, una **cancelación no prevista** o una **alerta falsa**? ¿Qué umbral elegiríais? |
| □ | **6b** | ¿Gana el modelo a **«avisar a todos»**? ¿Y si la alerta falsa costara **5 €** en vez de 40? |
| □ | **7** | ¿Tienen sentido las variables más importantes para el negocio? ¿Alguna **sospechosa de fuga**? |
| □ | **10** | Probad una reserva con datos imposibles (`"noches": 0`): ¿qué error da la API y por qué? |

## En casa (para el informe del reto)

| ✓ | Tarea | Qué piden |
|---|---|---|
| □ | **Cambiar los costes** | En el paso 6b, sustituid 100 € y 40 € por **vuestras hipótesis** (con una frase que las justifique) y volved a ejecutar |
| □ | **Repetir con otro tiempo** | Poned `LIMITE_TIEMPO = 15` y comparad el `score_test` con el de 120 s: ¿cambia algo? |
| □ | **Escribir el informe** | Máximo 4 páginas: planteamiento y datos · modelos y resultados · umbral y negocio · qué pesa en la predicción · evidencia de la API · recursos y costes |
| □ | **Tabla de recursos** | Recurso · cuándo se creó · tiempo usado · coste · cerrado · prueba |

**Total: 15 filas de pasos (instalación, 0 a 11, 6b y cierre) + 9 preguntas + 4 tareas para casa.**
