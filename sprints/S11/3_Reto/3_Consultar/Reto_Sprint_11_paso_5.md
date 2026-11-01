# Paso 5 · Informe, README y entrega (día 2, 20 minutos)

<!--nav-->
> Sprint 11 · Reto «Visión artificial para el cliente» · paso 5 de 5 · [Ficha del reto](Reto_Sprint_11.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_11_una_pagina.md)
<!--/nav-->

1. Escribir `analisis_errores.md` con lo que ya habéis ido apuntando.
2. Crear el `README.md`.
3. Pedir a alguien que no escribió esa parte que revise con la rúbrica y anote el resultado al final del README.
4. Reiniciar y ejecutar todo el cuaderno, bajarlo y subir los ficheros a `sprint-11/`.

**En sencillo.** Es el paso de **cerrar el trabajo**. Primero, contar a TurisData qué habéis descubierto: en qué se equivoca el modelo, qué fotos puede decidir solo y cuáles tiene que mirar una persona. Ya tenéis casi todo apuntado en los pasos anteriores: ahora se ordena. Segundo, el README, que es la hoja de entrada de la carpeta: sirve para que otra persona pueda repetir vuestro cuaderno sin preguntaros nada. Tercero, alguien que no escribió esa parte lo revisa con la rúbrica y deja su opinión por escrito. Cuarto, subir todo al repositorio del equipo desde el navegador. No hay código nuevo.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Informe de análisis de errores** | El documento de 1–2 páginas (`analisis_errores.md`) que cuenta resultados, errores y recomendación al cliente. |
| **Markdown** (`.md`) | Texto normal con unas pocas marcas: `#` para un título, `**…**` para negrita y barras verticales para las tablas. GitHub lo muestra ya con formato. |
| **README** | La hoja de entrada: qué hay, de dónde salen las fotos, cómo se repite y quién hizo qué. Es lo primero que lee el docente. |
| **Riesgo de IA responsable** | Algo concreto que podría salir mal al usar el modelo (por ejemplo, que los dibujos no sean fotos reales) junto con una **medida** para evitarlo. |
| **Licencia** | El permiso que dice si podéis usar una foto y con qué condiciones. Hay que apuntar autor y licencia de cada foto que no sea vuestra. |
| **Rúbrica** | La tabla con la que se evalúa el reto: cuatro criterios, cada uno de 1 a 4. |
| **Commit** | Cada vez que guardáis un cambio en GitHub con el botón verde **Commit changes**. Queda apuntado con el nombre de quien lo hace. |
| **Reiniciar y ejecutar todo** | Borra la memoria del cuaderno y ejecuta todas las celdas de arriba abajo. Prueba que el cuaderno funciona solo y deja los resultados visibles. |

**Cómo se hace**

1. **Repartir el trabajo.** Cada persona sube lo suyo con su cuenta: así el historial muestra a todo el equipo, que es lo que se evalúa. Un reparto posible: una persona prepara y sube el cuaderno, otra escribe el informe y otra el README. Quien revise con la rúbrica (el punto 4) **no puede ser quien escribió esa parte**.
2. **Escribir el informe** `analisis_errores.md`. No hay plantilla. Esta es la estructura, con seis apartados **en este orden**. Podéis escribirlo directamente en GitHub (*Add file → Create new file*) o en un editor y subirlo después. Copiad el esqueleto y sustituid lo que va entre corchetes por vuestras cifras y frases:

    ```text
    # Análisis de errores · Visión artificial para el cliente (Sprint 11)

    ## 1. Qué se ha hecho y con qué datos
    [Cliente, qué clasifica el modelo, origen y licencia de las fotos, fotos por clase, cómo se partieron.]

    ## 2. Resultados
    | Clase | Precisión | Recall |
    |---|---|---|
    | apartamentos | | |
    | camping | | |
    | casa_rural | | |
    | hotel | | |
    | piscina | | |

    Precisión en prueba: transfer + fine-tuning [..] · desde cero [..]. F1 macro: [..] y [..].

    ## 3. La matriz de confusión
    [Qué clases se confunden y cuántas fotos; una frase.]

    ## 4. Los errores
    | Foto | Verdadera | Predicha | Confianza | Hipótesis de causa | Mejora propuesta |
    |---|---|---|---|---|---|
    | | | | | | |

    ## 5. Recomendación al cliente
    Con un umbral de [..], el modelo decide solo el [..] % de las fotos y acierta el [..] % de ellas; el resto lo revisa una persona.

    ## 6. Riesgos de IA responsable
    1. Riesgo: [..] Medida: [..]
    2. Riesgo: [..] Medida: [..]
    ```

    Casi todo sale de lo que ya apuntasteis: las fotos y la partición (pasos 1 y 2), las cifras por clase y la matriz (paso 3), la tabla de errores (paso 3) y la frase del umbral (paso 4).

    Para el nivel mínimo bastan los apartados 1, 3 y 4. Los riesgos tienen que ser **de este caso**, no frases generales como «la IA puede tener sesgos». Dos ejemplos del tipo que se pide: *«Riesgo: los dibujos son sintéticos, no fotos reales, así que las cifras pueden no valer con fotos de verdad. Medida: repetir la prueba con fotos reales con licencia antes de usar el modelo»*; *«Riesgo: el modelo clasificó con [..] % de confianza una foto de [..] como [..]. Medida: umbral de [..] y revisión de una persona por debajo»*. Pensad también en las etiquetas dudosas: parte de los errores pueden ser fallos de etiquetado y no del modelo.

    **No vale:** un informe sin recomendación, cifras escritas de memoria o copiadas de lo que dijo una IA (todas salen de vuestro cuaderno), hipótesis que no se ven en la foto, ni riesgos genéricos.

3. **Rellenar el README.** No hay plantilla. Para el nivel mínimo bastan estas cinco secciones en pocas líneas. Abrid el repositorio del equipo, entrad en `sprint-11/` y usad *Add file → Create new file* con el nombre `README.md`. Así puede quedar:

    ```text
    # Sprint 11 · Visión artificial para el cliente

    ## Qué es
    Un modelo que clasifica fotos de alojamientos de TurisData en cinco tipos (hotel, apartamentos, casa rural, camping y piscina) y dice cuándo hay que revisar la foto a mano. Se entrega el cuaderno `reto_vision_cliente.ipynb` y el informe `analisis_errores.md`.

    ## Cómo se ejecuta
    Abrir `reto_vision_cliente.ipynb` en Colab y pulsar *Entorno de ejecución → Reiniciar y ejecutar todo*. La semilla es 42 (`SEMILLA = 42`).

    ## Datos
    Dibujos sintéticos que genera el propio cuaderno (60 por clase). No son fotos reales. [Si usáis fotos propias: autor y licencia, y cuántas hay por clase.]

    ## Uso de IA y límites
    Pedimos a la IA [..]; comprobamos a mano [..]; cambiamos [..]. Límite: los datos son sintéticos y con etiquetas dudosas a propósito.

    ## Quién hizo qué
    - Persona 1 (@usuario): cuaderno y ejercicios 1 y 2
    - Persona 2 (@usuario): evaluación y ejercicios 3 y 4
    - Persona 3 (@usuario): umbral, ejercicio 5, informe y README
    ```

    Para el nivel extra, añadid en «Cómo se ejecuta» las versiones de Python y de TensorFlow (`print(tf.__version__)` en una celda del cuaderno, que ya trae `tf` cargado). Después pulsad **Commit changes**.

4. **La revisión con la rúbrica (5 minutos).** Quien revisa **no escribió esa parte**. Sigue los cinco pasos de «Cómo se revisa» de [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md): ejecutar el cuaderno, leer el informe y el README como si fuera el cliente, mirar dos errores con la foto delante, poner un nivel de 1 a 4 por criterio **con una frase de prueba** y apuntar el resultado. Añade al final del `README.md` esta sección rellena:

    ```text
    ## Revisión con la rúbrica

    Revisado por: (nombre) · Fecha: (dd/mm/aaaa)

    | Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
    |---|---|---|
    | Corrección técnica | | |
    | Reproducibilidad | | |
    | Análisis y comunicación al cliente | | |
    | IA responsable | | |

    Lo primero que mejoraríamos: (una cosa concreta)
    ```

    Un ejemplo de frase de prueba: «3 · se ejecuta de arriba abajo y la referencia sale en la misma tabla, pero la prueba se usa dos veces». Sin frase, el nivel no vale. Si hay tiempo, arreglad lo más fácil; lo demás queda como «lo primero que mejoraríamos».

5. **Subir los ficheros (la vía del curso, desde el navegador).** Seguid [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md). Para el cuaderno: en Colab, ponedle el nombre `reto_vision_cliente.ipynb` (*Archivo → Cambiar nombre*), después *Entorno de ejecución → Reiniciar y ejecutar todo*, mirad que ninguna celda dé error y *Archivo → Descargar → Descargar .ipynb*. En el repositorio del equipo: (1) **entrad primero en la carpeta `sprint-11`**; (2) *Add file → Upload files*; (3) arrastrad el fichero; (4) escribid un mensaje corto y pulsad **Commit changes**. Un reparto posible: la persona A sube `reto_vision_cliente.ipynb` («Añado cuaderno con el modelo y el demostrador»), la B sube `analisis_errores.md` («Añado análisis de errores») y la C sube `README.md` («Añado README»). Los nombres de archivo, **en minúsculas y sin espacios**. Las fotos no se suben: el cuaderno vuelve a generarlas.
6. **La autoevaluación.** Cada persona copia la plantilla de [autoevaluación y coevaluación](../2_Entregar/autoevaluacion_y_coevaluacion.md), la guarda con su nombre (`autoevaluacion_nombre.md`, sin espacios ni tildes), la rellena y la sube a `sprint-11/`. La coevaluación va dentro del mismo fichero y se hace durante la *review*.

**Qué deberíais ver.** En la carpeta `sprint-11` del repositorio, los tres ficheros del equipo y una hoja de autoevaluación por persona (**3 + N**); y en el historial (el icono del reloj), al menos tres *commits* con nombres distintos. Al ejecutar todo el cuaderno, la última celda escribe `Dataset sintético eliminado (no debe subirse al repositorio).`: es la limpieza de las fotos generadas, y es normal.

**Hecho cuando:** otra persona podría ejecutar el cuaderno siguiendo solo el README, la sección «Revisión con la rúbrica» está rellena y los tres *commits* están en el repositorio.

**Después, 30 minutos de entrega y review:** cada persona rellena y sube su autoevaluación y coevaluación a `sprint-11/`, y el equipo enseña, en unos 5 minutos, el demostrador funcionando con 2 o 3 fotos, la matriz de confusión y tres errores comentados («el modelo confunde X con Y porque… y propondríamos…»). Después, la retro.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| El archivo ha caído en la raíz del repositorio y no en `sprint-11/` | Se subió sin entrar antes en la carpeta. | Abrid el archivo → icono del lápiz → en la ruta de arriba escribid `sprint-11/` delante del nombre → **Commit changes**. Lo mueve. |
| El archivo no aparece tras subirlo | Falta pulsar el botón verde **Commit changes**: sin él no se guarda nada. | Volved a subirlo y pulsadlo. |
| No veis el botón *Add file* | No sois colaboradores del repositorio o no habéis aceptado la invitación. | Pedid a quien creó el repositorio que os añada y aceptad la invitación. |
| El cuaderno subido no muestra gráficas ni cifras | Se descargó sin haberlo ejecutado. | *Entorno de ejecución → Reiniciar y ejecutar todo* y descargad de nuevo el `.ipynb`. |
| *Reiniciar y ejecutar todo* se para en una celda con `...` | Falta rellenar el hueco de un ejercicio. | Completad los ejercicios 1 a 5, en orden, y repetid. |
| El archivo se llama `Copia de S11_04…ipynb` o lleva espacios | Colab conserva el nombre de la copia. | Renombradlo a `reto_vision_cliente.ipynb` (minúsculas, sin espacios) antes de descargarlo. |
| Las cifras del cuaderno cambian un poco al ejecutar otra vez | El entrenamiento de una red no es idéntico al 100 % entre ejecuciones y ordenadores. | Usad en el informe las cifras de la ejecución final (la de *Reiniciar y ejecutar todo*). |

<!--nav-->
---

[← Paso 4](Reto_Sprint_11_paso_4.md) · [Ficha del reto: ayudas, errores frecuentes y qué hacer si os atascáis](Reto_Sprint_11.md)
<!--/nav-->
