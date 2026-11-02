# Paso 4 · Publicar el servicio y hacer una llamada (día 2, 10 minutos)

<!--nav-->
> Sprint 3 · Reto «Primer modelo en producción» · paso 4 de 6 · [Ficha del reto](Reto_Sprint_03.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_03_una_pagina.md) · [Paso 5 →](Reto_Sprint_03_paso_5.md)
<!--/nav-->

1. Guardar y recargar el modelo (apartados 8 y 9 del cuaderno).
2. Fijar vuestro umbral en el servicio y llamar a la API con una reserva (apartado 10).
3. Probar una reserva con datos imposibles y guardar la petición y la respuesta como evidencia.

**En sencillo.** Hasta ahora el modelo vive dentro del cuaderno, y el equipo de reservas no trabaja con cuadernos. Un **servicio** (una **API**) es una ventanilla: otra aplicación entrega los datos de una reserva y el modelo devuelve su riesgo y si hay alerta, como un camarero que lleva el pedido a la cocina y vuelve con el plato. En Colab no se puede abrir la web del servicio desde vuestro navegador, así que el cuaderno usa una pieza (`TestClient`) que hace la llamada «por dentro», igual que la haría otra aplicación. El código ya está escrito: ejecutáis, añadís una celda de tres líneas y guardáis lo que sale. No hace falta saber qué es FastAPI ni cómo se programa un servicio.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **API (servicio)** | Una puerta por la que otra aplicación pregunta al modelo y recibe una respuesta. |
| **Petición y respuesta** | Lo que se envía (los datos de una reserva) y lo que vuelve (probabilidad, alerta y umbral). |
| **`TestClient`** | La pieza que, dentro del cuaderno, hace la llamada a la API sin necesidad de red. |
| **Código de respuesta** | `200` significa que todo ha ido bien; `422`, que los datos son imposibles y el servicio se niega a calcular. |
| **Variable de entorno (`UMBRAL`)** | Un ajuste que se le pasa al servicio desde fuera. Si no se pone, el servicio usa 0,5. |
| **Evidencia** | La prueba de que la llamada ocurrió: el texto de la salida o una captura de pantalla. |

**Cómo se hace**

1. **Guardar y recargar el modelo.** Ejecutad los apartados «8. Guardar y recargar el modelo» y «9. Función de predicción». El 8 guarda el modelo en la carpeta `modelo_cancelaciones` y lo vuelve a cargar, como haría un servicio; el 9 define `predecir_cancelacion`. No hay que escribir nada. Ojo: esa función usa el umbral 0,5 fijo, no el vuestro, así que **no es la evidencia**; la evidencia sale del apartado 10.

2. **Fijar vuestro umbral.** Antes del apartado 10, añadid una celda nueva (botón **+ Código**), pegad estas tres líneas con **vuestro** umbral y ejecutadla:

    ```python
    import os, sys
    os.environ["UMBRAL"] = "0.2"
    sys.modules.pop("api_cancelaciones", None)
    ```

    Qué hace cada línea:

    - `import os, sys`: trae dos herramientas; `os` maneja los ajustes del sistema y `sys` la lista de piezas ya cargadas.
    - `os.environ["UMBRAL"] = "0.2"`: le dice al servicio qué umbral usar. Cambiad `0.2` por el vuestro, **entre comillas** y con **punto** decimal.
    - `sys.modules.pop("api_cancelaciones", None)`: olvida el servicio si ya lo habíais cargado, para que el apartado 10 lo cargue de nuevo con vuestro umbral. Si no lo habíais cargado, no hace nada.

    Sin esta celda el servicio usa 0,5 y la alerta no reflejaría lo que habéis decidido.

3. **Ejecutar el apartado «10. Servir el modelo por API».** Descarga `api_cancelaciones.py` (necesita internet), pregunta al servicio si está vivo (`/salud`) y le manda una reserva de ejemplo (`/predecir`). La respuesta tiene tres datos: `probabilidad_cancelacion` (el riesgo, de 0 a 1), `alerta` (`True` si el riesgo llega al umbral) y `umbral` (el que usa el servicio).

4. **Probar una reserva con datos imposibles.** El cuaderno lo sugiere en un comentario. Añadid otra celda nueva debajo del apartado 10 y ejecutadla:

    ```python
    reserva_mala = dict(reserva_ejemplo, noches=0)
    respuesta = cliente.post("/predecir", json=reserva_mala)
    print(respuesta.status_code)
    ```

    Qué hace cada línea:

    - `dict(reserva_ejemplo, noches=0)`: copia la reserva de ejemplo cambiando solo `noches` a 0, que es imposible (una estancia tiene al menos una noche).
    - `cliente.post("/predecir", json=reserva_mala)`: la envía al servicio, igual que en el apartado 10.
    - `print(respuesta.status_code)`: escribe el código de respuesta.

    Un servicio bien hecho **se niega a calcular** con datos imposibles en lugar de inventarse una probabilidad.

5. **Guardar la evidencia.** Seleccionad con el ratón el texto de la salida del apartado 10 (las dos líneas) y copiadlo (`Ctrl + C`) para pegarlo en el apartado 4 del informe; o haced una captura de pantalla de esa celda. Tienen que verse la petición y la respuesta. Revisad que no se vea ninguna clave ni contraseña: aquí no hay, pero la regla vale siempre. En Colab esta es la forma de hacer la llamada, la misma que usa el solucionario del docente; si preferís levantar el servicio en vuestro ordenador con `uvicorn`, la [guía en parejas](../../2_Practica/automl/guia_automl_en_parejas.md) (paso 10) explica cómo.

**Qué deberíais ver.** Apartado 8: `Modelo recargado. Probabilidades de ejemplo:` seguido de cinco números entre 0 y 1. Apartado 9: `Ejemplo de predicción: {'probabilidad_cancelacion': …, 'alerta': …}`, con alerta calculada con 0,5. Apartado 10: una línea `{'estado': 'ok', 'modelo': 'modelo_cancelaciones'}` y otra `200 {'probabilidad_cancelacion': …, 'alerta': …, 'umbral': …}`: la probabilidad es un número entre 0 y 1 (la guía da ~0,79 para la reserva de ejemplo), `alerta` es `True` si la probabilidad supera el umbral y `umbral` es **el vuestro**. En la celda de los datos imposibles, un `422`.

**Hecho cuando:** la respuesta del apartado 10 muestra vuestro umbral, tenéis guardado el texto o la captura de la petición y la respuesta, y habéis visto el `422` con `noches` a 0.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `FileNotFoundError` con `modelo_cancelaciones/predictor.pkl` en el mensaje | Falta la carpeta del modelo: no se ejecutó el apartado 8, o la sesión se reinició. | Ejecutad los apartados 4 y 8 y volved al 10. |
| En la respuesta, `'umbral': 0.5` | El servicio se cargó antes de fijar vuestro umbral. | Ejecutad la celda de las tres líneas y **después** volved a ejecutar el apartado 10. |
| `ModuleNotFoundError: No module named 'fastapi'` (o `'httpx'`) | La instalación no se hizo o Colab se reinició. | Ejecutad la celda de instalación del principio y repetid desde «0. Configuración». |
| `NameError: name 'cliente' is not defined` (o `'reserva_ejemplo'`) | No se ha ejecutado el apartado 10 antes de vuestra celda de prueba. | Ejecutad el apartado 10 y después vuestra celda. |
| `422` con la reserva de ejemplo | Habéis cambiado algún dato y ha quedado imposible o mal escrito. | Leed el mensaje (`respuesta.json()` dice qué campo falla) y volved a los valores del cuaderno. |
| Intentáis abrir `http://127.0.0.1:8000/docs` desde Colab y no carga | En Colab el servicio no es visible desde vuestro navegador. | Es normal: por eso el cuaderno usa `TestClient`. |
| El `200` sale con una probabilidad distinta a la de la guía | El modelo se reentrena en cada equipo y varía algo. | Es normal; en el informe van vuestras cifras. |

<!--nav-->
---

[← Paso 3](Reto_Sprint_03_paso_3.md) · [Ficha del reto](Reto_Sprint_03.md) · [Paso 5 →](Reto_Sprint_03_paso_5.md)
<!--/nav-->
