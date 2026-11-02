# Paso 5 · Cerrar y borrar (día 2, 10 minutos)

<!--nav-->
> Sprint 3 · Reto «Primer modelo en producción» · paso 5 de 6 · [Ficha del reto](Reto_Sprint_03.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_03_una_pagina.md) · [Paso 6 →](Reto_Sprint_03_paso_6.md)
<!--/nav-->

1. Ejecutar el apartado 11 del cuaderno y completar la tabla de recursos (qué se creó, cuánto se usó, cuánto costó).
2. Guardar una copia del cuaderno con sus resultados antes de cerrar nada.
3. Desconectar y eliminar el entorno de ejecución de Colab y hacer la captura que lo demuestra.

**En sencillo.** En una plataforma de pago, lo que se deja encendido se sigue cobrando aunque nadie lo use: es como dejar el grifo abierto al salir de casa. Aquí todo es gratis (0 €), pero el reto os hace practicar el hábito, porque en un trabajo real es lo que más sorprende en la factura. Este paso tiene dos partes: **apuntar** qué habéis usado y **cerrarlo**, con una prueba. Hay una trampa de orden: al cerrar Colab desaparece todo lo que había dentro (las tablas, el modelo, el CSV). Por eso primero se guarda y después se cierra. No hace falta saber nada de nubes ni de facturación.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Recurso** | Todo lo que creáis o consumís al trabajar: la sesión de Colab, el modelo guardado, los datos descargados, el servicio. |
| **Sesión (entorno de ejecución)** | El ordenador prestado en el que Colab ejecuta vuestro cuaderno. Mientras está conectado, está en uso. |
| **Cerrar o eliminar** | Apagar el recurso y borrar lo que contiene, para que no consuma nada. |
| **Prueba de cierre** | Una captura de pantalla que demuestra que ya no queda nada abierto. |
| **MB (megabyte)** | Unidad de tamaño de un archivo. El modelo guardado pesa unos 225 MB y los datos, menos de 1 MB. |
| **Coste real y coste en una plataforma de pago** | Lo que habéis pagado (aquí, 0 €) y lo que se pagaría si el servicio estuviera en una nube de pago. |

**Cómo se hace**

1. **Ejecutar el apartado «11. Informe de recursos».** Es la última celda de código del cuaderno: no hay que escribir nada. Imprime el tiempo de entrenamiento, el tamaño del modelo en disco y un recordatorio. Si Colab se reinició y falla, ejecutad antes desde «0. Configuración» hasta el apartado 4 (ver abajo, «Si algo falla»).

2. **Rellenar la tabla de recursos.** Es una tabla de cuatro filas, una por cosa que habéis creado. Rellenadla en la hoja del equipo y se copiará al apartado 5 del informe:

    ```text
    | Recurso                    | Cuándo se creó | Tiempo usado | Coste | ¿Cerrado? | Prueba            |
    |----------------------------|----------------|--------------|-------|-----------|-------------------|
    | Sesión de Colab            | hh:mm          | n min        | 0 €   | Sí        | captura_cierre.png |
    | Modelo guardado            | hh:mm          | n s          | 0 €   | Sí        |                   |
    | Datos descargados          | hh:mm          | n s          | 0 €   | Sí        |                   |
    | Servicio (API de prueba)   | hh:mm          | n min        | 0 €   | Sí        |                   |
    ```

    De dónde sale cada dato:

    - **Cuándo se creó:** la hora aproximada a la que ejecutasteis la celda que lo creó (la sesión, al abrir el cuaderno; el modelo, en el apartado 4; los datos, en el 0; el servicio, en el 10).
    - **Tiempo usado:** para el modelo, el tiempo de entrenamiento que imprime el apartado 11; para la sesión, desde que abristeis el cuaderno hasta ahora. Si no lo sabéis con exactitud, escribid una estimación y decid que lo es.
    - **Coste:** 0 € en todas las filas, porque Colab gratuito no cobra. El tamaño del modelo (unos 225 MB) y de los datos (0,66 MB) no cuestan nada, pero se apuntan.
    - **¿Cerrado?:** «Sí» solo cuando lo hayáis hecho de verdad (puntos 4 a 6). La API de prueba no es un servidor encendido: la llamó el propio cuaderno, y se apaga al eliminar el entorno.

3. **Escribir una frase sobre una plataforma de pago.** Completad: «En una plataforma de pago, ______ se cobraría ______, y por eso cerrarlo importa porque ______». Ejemplo de redacción (no lo copiéis): un servicio encendido suele cobrarse por hora aunque nadie lo use, mientras que el entrenamiento, que dura segundos, apenas pesa en la factura. **No inventéis precios**: si no tenéis un precio real, hablad solo de cómo se cobra.

4. **Guardar antes de cerrar.** Comprobad que tenéis anotado fuera de Colab todo lo que el informe necesita: la tabla del *leaderboard* (paso 2), la tabla de costes y el umbral (paso 3), la salida del apartado 10 (paso 4) y el apartado 11. Después, en el menú **Archivo → Guardar una copia en Drive**: la copia conserva el cuaderno con las salidas, y si hace falta consultar algo, lo abrís sin volver a entrenar. Si el docente lo pide (o queréis conseguir el nivel 4 de Reproducibilidad), **Archivo → Descargar → Descargar .ipynb** y lo subiréis con el informe. **No subáis** la carpeta `modelo_cancelaciones`: pesa unos 225 MB y no hace falta.

5. **Desconectar y eliminar el entorno.** En el menú **Entorno de ejecución → Desconectar y eliminar entorno de ejecución**, y confirmad. Colab apaga la sesión y borra todo lo que contenía: el modelo, el CSV y las variables.

6. **Hacer la captura de cierre.** Tiene que verse la ventana de Colab con el cuaderno y que **ya no hay sesión conectada** (arriba a la derecha vuelve a aparecer el botón *Conectar*). En Windows pulsad `Windows + Mayús + S` y seleccionad el área; en Mac, `Cmd + Mayús + 4`. Guardadla como `captura_cierre.png`. Antes de guardarla, revisad que no se vea ninguna clave, contraseña ni vuestro correo: si sale, recortad la imagen.

**Qué deberíais ver.** Del apartado 11, estas cuatro líneas: `--- Informe de recursos ---`, `Tiempo de entrenamiento: … s (límite fijado: … s)`, `Tamaño del modelo en disco: … MB` (alrededor de 225) y `Coste económico: 0 EUR (Colab gratuito o equipo local)`, seguidas del recordatorio de cerrar la sesión. La guía da un entrenamiento de unos 36 s; en otros equipos ha salido en torno a 17 s: vuestra cifra será otra, y es la que vale. Después, una tabla con cuatro filas y todos los «Sí», y una captura `captura_cierre.png` con la sesión desconectada.

**Hecho cuando:** tenéis la tabla de recursos completa, la frase sobre la plataforma de pago, una copia del cuaderno guardada en Drive, el entorno eliminado y `captura_cierre.png` guardada sin datos personales.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'tiempo_entrenamiento' is not defined` (o `'CARPETA_MODELO'`) | Se reinició Colab y se perdieron las variables, o no habéis ejecutado antes el apartado 4. | Ejecutad desde «0. Configuración» hasta el apartado 4 y después el 11. Entrenar con `LIMITE_TIEMPO = 15` basta para rellenar la tabla, pero entonces apuntad esos segundos y decidlo en el informe. |
| `FileNotFoundError` o un tamaño de modelo de 0 MB | El modelo guardado no está: falta el apartado 8. | Ejecutad los apartados 4 y 8 y después el 11. |
| Cerrasteis Colab antes de apuntar una cifra | La sesión se borró con sus salidas. | Abrid la copia de Drive: conserva las salidas guardadas. Si no hay copia, hay que volver a entrenar (con `LIMITE_TIEMPO = 15` son unos 15 segundos) y vuestras cifras serán algo distintas: anotad **esas**. |
| No encontráis «Desconectar y eliminar entorno de ejecución» | Está en el menú **Entorno de ejecución**, al final de la lista; si no hay sesión conectada, no aparece activo. | Si arriba a la derecha pone *Conectar*, la sesión ya está cerrada: haced la captura tal cual. |
| Trabajasteis en vuestro ordenador, no en Colab | No hay sesión que desconectar: el recurso es un servicio y una carpeta. | Parad el servicio con `Ctrl + C` en la terminal, borrad la carpeta `modelo_cancelaciones` y haced la captura de la terminal. Preguntad al docente cómo comprobarlo en vuestro sistema. |
| En la captura se ve el correo o la foto de la cuenta | Colab los muestra arriba a la derecha. | Recortad o tapad esa parte y guardad la imagen de nuevo. |
| No sabéis qué poner en «Tiempo usado» | No cronometrasteis la sesión. | Escribid una estimación honesta («unos 70 minutos») y decid que es estimada. |

<!--nav-->
---

[← Paso 4](Reto_Sprint_03_paso_4.md) · [Ficha del reto](Reto_Sprint_03.md) · [Paso 6 →](Reto_Sprint_03_paso_6.md)
<!--/nav-->
