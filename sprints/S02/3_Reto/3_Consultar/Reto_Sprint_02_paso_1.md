# Paso 1 · Planning (día 1, 10 minutos)

<!--nav-->
> Sprint 2 · Reto «¿Nos fiamos de este informe?» · paso 1 de 5 · [Ficha del reto](Reto_Sprint_02.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_02_una_pagina.md) · [Paso 2 →](Reto_Sprint_02_paso_2.md)
<!--/nav-->

1. Leer el informe del cliente en voz alta.
2. Repartir las afirmaciones: la 1 y la 2, todos juntos; de la 3 a la 6, una por persona.
3. Abrir los datos en una hoja de cálculo y copiar la plantilla del dictamen a `sprint-02/`.

**En sencillo.** Hoy **no se programa** y no hace falta saber estadística. Sois **personas auditoras**: una empresa os da un informe y vosotros decís qué frases se pueden creer y cuáles no. Es como cuando varias personas se reparten la corrección de los exámenes de una clase: antes de empezar hay que ver qué hay que revisar y quién se encarga de qué, para que nadie repita trabajo y ninguna frase se quede sin mirar. Este paso son solo 10 minutos: leer, repartir y dejar preparados los dos ficheros con los que vais a trabajar.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Persona auditora** | Quien revisa el trabajo de otra persona y da su opinión razonada. |
| **Afirmación** | Cada una de las seis frases del informe que hay que revisar. |
| **Dictamen** | El documento con vuestra opinión razonada sobre cada afirmación. Es lo que entregáis. |
| **Tarifa y canal** | La tarifa es el tipo de reserva (flexible o no reembolsable). El canal es por dónde se reserva (directo o intermediaria). |
| **CSV** | Un archivo de texto con una tabla: cada línea es una fila y los valores van separados por comas. |
| **Hoja de cálculo** | Un programa de tablas con fórmulas: Google Sheets, Excel o LibreOffice. Con vuestra cuenta de Google ya tenéis Google Sheets. |
| **Plantilla** | Un documento con huecos que se rellenan, para no partir de una hoja en blanco. |
| **Markdown (`.md`)** | Texto sencillo que GitHub muestra con formato. El dictamen se escribe así. |

**Cómo se hace**

1. **Leer el informe en voz alta (3 minutos).** Abrid [`informe_cliente.md`](../1_Trabajar/plantillas/informe_cliente.md). Una persona lee una afirmación tras otra y las demás siguen el texto. Fijaos en que algunas llevan, después de los dos puntos, de dónde sale lo que dicen (a cuántos datos o a quién se preguntó): es una pista para más adelante. No hace falta resolver nada todavía.

2. **Repartir las afirmaciones (3 minutos).** Se reparten así:

    - **Afirmaciones 1 y 2:** las hace todo el equipo junto y con el docente (pasos 2 y 3).
    - **Afirmaciones 3 a 6:** una por persona (paso 4). Con tres personas, una hace dos; mejor que la 6, que lleva una cuenta, no sea la segunda de nadie.

    Apuntad el reparto en una nota y en el tablero (una tarjeta por afirmación, con su responsable). Ejemplo con cuatro personas (nombres inventados):

    | Persona | Afirmación |
    |---|---|
    | Marta | 3 |
    | Luis | 4 |
    | Ana | 5 |
    | Pablo | 6 |

3. **Abrir los datos (2 minutos).** [`informe_cliente.csv`](../1_Trabajar/plantillas/informe_cliente.csv) tiene solo cuatro filas. Lo más rápido es **escribirlas a mano** en una hoja de cálculo nueva, con los títulos en la fila 1 y los números **sin puntos** (`1000`, no `1.000`):

    ```text
    tarifa           canal          reservas  cancelaciones
    flexible         directo        1000      300
    flexible         intermediaria  200       70
    no_reembolsable  directo        200       20
    no_reembolsable  intermediaria  1000      120
    ```

    Cada título va en una columna: `tarifa` en la A, `canal` en la B, `reservas` en la C y `cancelaciones` en la D. Si preferís importar el archivo, bajadlo con el icono de descarga de GitHub (*Download raw file*) y, en Google Sheets, *Archivo → Importar → Subir*. En el paso 3 se usan estas columnas y estas filas.

4. **Copiar la plantilla del dictamen (2 minutos).** Lo hace una persona; las demás miran. Abrid [`plantilla_dictamen.md`](../1_Trabajar/plantillas/plantilla_dictamen.md), pulsad **Raw**, seleccionad todo (`Ctrl + A`) y copiad (`Ctrl + C`). En el repositorio del equipo, **entrad primero en la carpeta `sprint-02`** y pulsad *Add file → Create new file*; como nombre, `dictamen.md`; pegad (`Ctrl + V`) y completad la primera línea (equipo, fecha y personas). Pulsad **Commit changes** con un mensaje corto, por ejemplo «Copio la plantilla del dictamen». No rellenéis nada más en `dictamen.md` hasta el paso 5: la afirmación 1 ya viene resuelta como modelo, y escribir a la vez varias personas en el mismo archivo hace que se pisen los cambios.

**Qué deberíais ver.** Una nota con el reparto (nombre y afirmación de cada persona), una hoja con cinco filas (los títulos y las cuatro filas de datos) en las columnas A a D, y `dictamen.md` dentro de `sprint-02/` en GitHub, con la afirmación 1 ya resuelta y la primera línea completada.

**Hecho cuando:** cada persona sabe qué afirmación le toca, los datos están en la hoja y `dictamen.md` está en `sprint-02/`.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| Al importar, todo el CSV sale en una sola columna, con comas | La hoja no ha separado por comas. | En Google Sheets: *Datos → Dividir texto en columnas*. Si no, escribid los datos a mano: son 16 valores. |
| Los números quedan pegados a la izquierda de la celda | La hoja los ha tomado por texto (por ejemplo, por escribir `1.000`). | Escribid `1000`, sin punto ni espacio. |
| Somos tres personas y hay cuatro afirmaciones (3 a 6) | Sobra una afirmación. | Una persona hace dos; que sea la que vaya más rápida y que no sea la 6. |
| No hay forma de repartirse las afirmaciones | Ninguna es «la fácil». | Sortead: las cuatro se resuelven con la misma receta (paso 4). |
| `dictamen.md` aparece en la raíz del repositorio, no en `sprint-02/` | Se creó sin escribir la carpeta en el nombre. | Abrid el archivo → icono del lápiz → delante del nombre escribid `sprint-02/` → **Commit changes**. |
| No encontráis la carpeta `sprint-02` | El repositorio del equipo aún no la tiene. | Desde la raíz del repositorio, *Add file → Create new file* y como nombre `sprint-02/dictamen.md`: GitHub crea la carpeta al escribir la barra. |

<!--nav-->
---

[Ficha del reto](Reto_Sprint_02.md) · [Paso 2 →](Reto_Sprint_02_paso_2.md)
<!--/nav-->
