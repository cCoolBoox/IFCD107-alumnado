# Paso 2 · Construir el relato (día 1, 85 minutos)

<!--nav-->
> Sprint 17 · Reto «La defensa» · paso 2 de 5 · [Ficha del reto](Reto_Sprint_17.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_17_una_pagina.md) · [Paso 3 →](Reto_Sprint_17_paso_3.md)
<!--/nav-->

1. Rellenar la plantilla de storytelling, de arriba abajo: audiencia, mensaje único, pirámide y arco narrativo.
2. Dibujar el storyboard: un máximo de 12 diapositivas, cada una con su título-conclusión.
3. Escribir quién habla en cada parte, de modo que hablen todas las personas.
4. Escribir y ensayar en voz alta el pitch de 3 minutos.

**En sencillo.** Hasta ahora el proyecto se cuenta como un diario: «primero hicimos esto, luego probamos lo otro». Quien escucha necesita lo contrario, como en un aviso de aeropuerto: primero **qué tiene que hacer**, después las razones. En esta hora y media se rellena un documento de texto con ocho apartados **antes de abrir el programa de diapositivas**: si el mensaje no cabe en una frase, no cabrá en 12 diapositivas. No hay código ni hace falta saber diseñar: se escribe, se dice en voz alta y se corrige. Todas las cifras salen de la memoria congelada del Sprint 16, nunca de la memoria de nadie ni de una IA.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Markdown (`.md`)** | Texto normal con marcas sencillas: `#` para un título y barras verticales para separar las columnas de una tabla. GitHub lo enseña ya con formato. |
| **Evidencia** | El dato, gráfico o tabla de la memoria que demuestra una afirmación. Sin evidencia, la afirmación no se dice. |
| **Test del ascensor** | Decir el mensaje único en 20 segundos a alguien que no conoce el proyecto y comprobar si lo repite con sus palabras. |
| **Gancho** | La primera cosa que se dice para que escuchen: una cifra sorprendente, una pregunta o una escena del usuario. |
| **Título-conclusión** | Un título que es una frase y dice lo que se aprende: «El modelo supera al método simple en 9 de 12 meses», no «Resultados». |
| **Storyboard** | El esquema de todas las diapositivas en una tabla, antes de hacerlas: título, imagen, quién habla y cuánto dura. |
| **Pitch** | La presentación ultracorta, de 3 minutos, que debe funcionar sin diapositivas. |
| **Reparto de voces** | Quién cuenta cada parte. Hablan todas las personas, y cualquiera puede recibir una pregunta. |

**Cómo se hace**

1. **Crear `plantilla_storytelling.md` en vuestra carpeta `sprint-17`.** Lo hace una persona; **otra la escribe en el teclado mientras todas dictan, y cambiáis de persona en cada apartado**. Los pasos, como en la [guía de entrega](../../../../material/5.%20Como_entregar_en_GitHub.md):

    - Abrid la [plantilla](../1_Trabajar/plantillas/plantilla_storytelling.md) en GitHub, pulsad **Raw** (arriba a la derecha) y copiad todo con `Ctrl + A` y `Ctrl + C`.
    - En el repositorio del equipo **entrad primero en la carpeta `sprint-17`**, pulsad **Add file → Create new file**, escribid el nombre `plantilla_storytelling.md` (con ese mismo nombre, sin espacios) y pegad con `Ctrl + V`.
    - Cambiad la primera línea: sustituid `[Proyecto]` y `[Equipo]` por el nombre de vuestro proyecto y de vuestro equipo.
    - Para ver cómo queda, pulsad **Preview**; para escribir, **Edit**. Al acabar cada apartado, pulsad **Commit changes…**, escribid un mensaje corto («Añado la audiencia») y confirmad. **Sin ese botón no se guarda nada.** Para volver a editar: abrid el archivo, icono del lápiz, cambiad y **Commit changes**.
    - Las tablas tienen celdas vacías entre dos barras verticales: se rellena **dentro** de ellas, sin borrar ninguna barra. Por ejemplo:

    ```text
    Antes:   | ¿Quién escucha? (cliente, directivos, tribunal, compañeros) | |
    Después: | ¿Quién escucha? (cliente, directivos, tribunal, compañeros) | El director del hotel y su equipo directivo |
    ```

    Reparto orientativo de los 85 minutos (unos 45 para los apartados 1 a 5 y unos 40 para el reparto de voces, el pitch y la comprobación). La primera columna es el número de este punto:

    | Punto | Qué hacéis | Minutos |
    |---|---|---|
    | 2 | Audiencia | 8 |
    | 3 | Mensaje único | 10 |
    | 4 | Pirámide | 8 |
    | 5 | Arco narrativo | 9 |
    | 6 | Storyboard | 10 |
    | 7 | Reparto de voces | 10 |
    | 8 | Pitch de 3 minutos | 25 |
    | 9 | Comprobación final | 5 |

2. **Apartado 1 · Audiencia.** Contestad las cinco preguntas de la tabla con lo que ya dijisteis en el paso 1 (la columna *Respuesta* está vacía). Con el hotel de los apuntes (el vuestro será otro), quedaría así:

    | Pregunta | Respuesta de ejemplo |
    |---|---|
    | ¿Quién escucha? | El director del hotel y su equipo directivo |
    | ¿Qué saben ya del tema? ¿Qué **no** saben? | Su negocio muy bien; la IA, poco o nada |
    | ¿Qué decisión tienen que tomar o qué quieren entender? | Si se usa o no el modelo |
    | ¿Qué les preocupa? | Dinero, tiempo, riesgos y qué hacer mañana; equivocarse y que les vendan humo |
    | ¿Qué palabras técnicas hay que **traducir**? | Las de la tabla de traducción de debajo |

    Después, la **tabla de traducción: al menos 4 términos de vuestro proyecto**, cada uno con una frase que entienda alguien sin formación. La plantilla trae cuatro ejemplos (AUC, sobreajuste, baseline y fuga de datos): **dejad los que aparezcan en vuestro proyecto y sustituid los demás**. Más ejemplos de los apuntes:

    | Término técnico | Frase que entiende la audiencia |
    |---|---|
    | F1 de 0,71 con validación cruzada | De cada 10 reservas que se cancelan, detectamos 7 |
    | Recall de 0,58 en el subgrupo móvil | En reservas por móvil acertamos menos: 6 de cada 10 |
    | Reponderación para mitigar el sesgo | Hemos corregido el modelo para que trate mejor al canal móvil |
    | Transformer con RAG | El asistente busca primero en los documentos y responde citando la fuente |

    **Prueba:** si una persona ajena al curso (vuestra familia, un vecino) no entiende la frase, el tribunal tampoco la entenderá a la primera.

3. **Apartado 2 · Mensaje único.** Una sola frase con la fórmula de la plantilla. Primero buscad en la memoria congelada **la cifra** que la apoya:

    ```text
    Recomendamos [acción] porque [evidencia principal], lo que supone [beneficio cuantificado], con la precaución de [límite clave].
    ```

    Un ejemplo completo de los apuntes es: «Podemos prever la ocupación con 3 meses de antelación con un error del 7 %, suficiente para planificar plantilla, pero no para fijar precios». Si os atascáis, empezad por completar «Gracias a nuestro trabajo, el cliente puede ___, pero no debe ___» y desarrolladla con la fórmula. Escribid la frase en **Nuestro mensaje único**. Un mensaje honesto convence más que uno bonito:

    | Mensaje | ¿Convence? |
    |---|---|
    | «Nuestro modelo es muy bueno: 93 % de acierto» | Poco: ¿frente a qué?, ¿para quién?, ¿con qué datos? |
    | «Con la mayoría de reservas el modelo acierta 8 de cada 10; en móvil, 6 de cada 10. Recomendamos usarlo con revisión humana en ese canal» | Mucho: es concreto, tiene un límite y una acción |

    Haced el **test del ascensor** que pide la plantilla: decid el mensaje en voz alta, en 20 segundos, a alguien de otro equipo que no conozca el proyecto. Si lo repite con otras palabras, marcad «sí». Si no, reescribid **el mensaje**, no al oyente.

4. **Apartado 3 · Pirámide.** La conclusión primero (es el mensaje único), después **tres argumentos** y la evidencia de cada uno. Rellenad la tabla: en *Evidencia* escribid de qué figura o tabla de la memoria sale. Con el ejemplo de los apuntes:

    | Nivel | Contenido de ejemplo | Evidencia de ejemplo |
    |---|---|---|
    | **Conclusión** | Recomendamos usar el modelo para planificar plantilla, no para fijar precios | El mensaje único |
    | **Argumento 1** (por qué importa) | Supera al método actual en 9 de 12 meses | Tabla frente al baseline |
    | **Argumento 2** (cómo lo sabemos) | Su error es del 7 %, suficiente para ajustar turnos | Gráfico de errores por mes |
    | **Argumento 3** (límites y riesgos, y qué proponemos) | Falla con eventos atípicos y en alojamiento rural; hay que revisarlo a mano | La demo y el análisis de errores |

    **Regla:** cada argumento resume su evidencia. Si un dato no sostiene ningún argumento, **se queda fuera** (va a la memoria, no a la presentación).

5. **Apartado 4 · Arco narrativo.** Rellenad los **siete momentos** de la tabla (los apuntes los resumen en cinco: contad los de la plantilla). El protagonista es **el cliente, no el modelo**: «El hotel planificaba la plantilla a ojo» y no «Hemos entrenado un modelo». Orientación con el hotel de los apuntes (las filas 3 y 5 no están en los apuntes: son una propuesta):

    | Momento | Ejemplo |
    |---|---|
    | 1. Situación | El hotel planifica la plantilla a ojo |
    | 2. Complicación | Se equivoca ±20 % y paga horas extra o deja huéspedes sin servicio |
    | 3. Pregunta | ¿Se puede prever la ocupación con tiempo suficiente para planificar? |
    | 4. Resolución | Datos de X y un modelo sencillo frente a una referencia: error del 7 % y funciona hasta con 3 meses de antelación |
    | 5. Demostración | El momento «ajá»: cómo lo usaría el cliente |
    | 6. Límites y riesgos | No sirve para fijar precios; falla con eventos atípicos |
    | 7. Llamada a la acción | Usarlo así y con estos límites |

    Después escribid el **gancho de apertura** y la **frase de cierre** (que repite el mensaje único).

6. **Apartado 5 · Storyboard de 12 diapositivas como máximo.** La tabla ya trae doce filas con un tema en cada una («Los datos que tenemos», «Resultado clave frente al baseline»…). Vuestro trabajo es **convertir cada tema en un título-conclusión** (una frase, no una etiqueta), elegir **un elemento visual** (una figura de la memoria) y comprobar el tiempo. Una diapositiva es una idea, con unas 25 palabras como máximo: el gráfico cuenta y la persona que habla explica. Ejemplos de los apuntes:

    | Nº | Tema de la plantilla | Título-conclusión de ejemplo |
    |---|---|---|
    | 1 | Mensaje único y equipo | El mensaje único, tal cual |
    | 2 | El problema del cliente | El hotel planifica la plantilla a ojo y se equivoca ±20 % |
    | 6 | Resultado clave frente al baseline | El modelo supera al método simple en 9 de 12 meses |
    | 9 | Dónde falla y para quién | En reservas por móvil, el modelo acierta menos |
    | 10 | IA responsable | Tres riesgos altos, todos con medida aplicada |
    | 12 | Cierre | Repite el mensaje único |

    Las demás las escribís vosotros con la misma idea. **Sumad la columna de tiempo**: la que trae la plantilla suma 11 minutos y 45 segundos. Tiene que caber en el relato y la demo de vuestro turno (en el paso 3 y en el paso 5 está la tabla por número de equipos). Si no cabe, **quitad diapositivas, no aceleréis**. No hace falta diapositiva de «Gracias»: la 12 es el cierre. Lo técnico que sobre va a diapositivas de reserva, **después** de la 12.

7. **Reparto de voces.** Rellenad la columna *Persona que habla* del storyboard. Reglas: hablan **todas** las personas, y **cualquiera** puede recibir una pregunta, así que todas deben conocer todo el proyecto. El reparto orientativo del [guion de defensa](../../1_Teoria/actividades/guion_defensa.md) es este (con 3 personas, la persona 1 se queda también los límites):

    | Persona | Con 4 personas | Con 3 personas |
    |---|---|---|
    | P1 | Diapositivas 1 a 3 (apertura, contexto) y 11 a 12 (qué proponemos) | Las mismas y, además, 9 y 10 (límites y riesgos) |
    | P2 | Diapositivas 4 a 6 (qué hicimos y resultado) | Las mismas |
    | P3 | Diapositiva 7 y maneja la demo (8) | Diapositiva 7 y la demo (8); quién la narra lo decidís vosotras, el guion no lo dice |
    | P4 | Narra la demo (8) y diapositivas 9 y 10 | No existe |

    Es solo orientativo: ajustadlo a lo que sabe y prefiere cada persona.

8. **Apartado 6 · Pitch de 3 minutos.** La versión corta, para un directivo con poco tiempo, que debe funcionar **sin diapositivas**. Escribid **una frase por franja**; a ritmo tranquilo se dicen unas 130 palabras por minuto, es decir, **unas 400 palabras** en total, no 1.000. Con el hotel de los apuntes:

    | Segundos | Contenido | Frase de ejemplo |
    |---|---|---|
    | 0-20 | Gancho | El hotel planifica la plantilla a ojo y se equivoca ±20 % |
    | 20-50 | Problema y quién lo sufre | Paga horas extra o deja huéspedes sin servicio |
    | 50-100 | Solución, en lenguaje llano | Hemos probado un modelo sencillo con los datos de X frente a una referencia |
    | 100-150 | Resultado frente a lo de hoy | Error del 7 %; funciona hasta con 3 meses de antelación |
    | 150-170 | Límite honesto | No sirve para fijar precios; falla con eventos atípicos |
    | 170-180 | Petición | Usarlo así y con estos límites |

    Después, **ensayadlo en voz alta con el cronómetro**: una persona lo dice entero y las demás marcan dónde se pierden. Si pasa de 3 minutos, recortad **ideas**, no velocidad.

9. **Apartado 8 · Comprobación final.** Marcad cada casilla `[ ]` con una `x` (`[x]`) solo cuando se cumpla de verdad:

    - ¿Se entiende el mensaje único en 20 segundos?
    - ¿Cada título de diapositiva se entiende sin oír a quien habla?
    - ¿Las cifras coinciden con la memoria congelada?
    - ¿Hablan **todas** las personas y el reparto está equilibrado?
    - ¿Está la demo probada y el plan B abierto? (se hace en el paso 3: dejadlo sin marcar)
    - ¿Hay una recomendación accionable y una frase sobre los límites?
    - ¿Cabe en el tiempo del turno con 30 segundos de margen? (se mide en el paso 3: dejadlo sin marcar)

    Guardad con **Commit changes**. La sección «Revisión con la rúbrica» del final **no se toca ahora**: se rellena el día de la defensa.

**Qué deberíais ver.** Un `plantilla_storytelling.md` guardado en `sprint-17` con los apartados 1 a 6 y el 8 rellenos y ningún hueco vacío; un storyboard de 12 diapositivas o menos con un título-conclusión, un elemento visual y una persona en cada fila; y un pitch que se dice en voz alta en menos de 3 minutos.

**Hecho cuando:** pasáis la comprobación final de la plantilla (apartado 8): el mensaje se entiende en 20 segundos, cada título se entiende sin oír al orador y todas las personas tienen turno. Con eso ya podéis hacer las diapositivas.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| El mensaje único son tres frases, o la otra persona repite algo distinto | El mensaje no está claro | Elegid lo que el cliente hará mañana, completad «el cliente puede ___, pero no debe ___» y reescribid el mensaje, no al oyente |
| La cifra que queréis usar no está en la memoria congelada | No se presentan resultados nuevos | No la uséis. Buscad otra que sí esté; si un argumento se queda sin evidencia, cambiadlo |
| Salen más de 12 diapositivas o el tiempo suma de más | Se quiere contar todo | Fusionad temas o llevad lo técnico a diapositivas de reserva (después de la 12) y quitad diapositivas, no aceleréis |
| Los títulos son etiquetas («Resultados», «Riesgos») | Es lo más fácil de escribir | Pasadlos a frase con un verbo y una cifra: «Tres riesgos altos, todos con medida aplicada» |
| El pitch pasa de 3 minutos | Tiene demasiadas palabras (más de unas 400) | Recortad ideas, no velocidad |
| Una persona no tiene ninguna diapositiva | El reparto no es equilibrado | Dad a cada persona al menos un bloque y una pregunta de la lista del paso 3 |
| En Preview las tablas se ven como líneas de texto, o GitHub avisa de un conflicto al guardar | Falta una barra vertical, o dos personas editaron a la vez | Comparad la fila con la plantilla (mismas barras en todas); recargad la página y repetid vuestro cambio. Escribe una sola persona |

<!--nav-->
---

[← Paso 1](Reto_Sprint_17_paso_1.md) · [Ficha del reto](Reto_Sprint_17.md) · [Paso 3 →](Reto_Sprint_17_paso_3.md)
<!--/nav-->
