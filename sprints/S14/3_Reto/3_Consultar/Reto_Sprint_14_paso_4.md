# Paso 4 · Ficha del proyecto y entrega (día 1, 50 minutos)

<!--nav-->
> Sprint 14 · Reto «Proyecto final: definir, tener datos y un punto de partida» · paso 4 de 7 · [Ficha del reto](Reto_Sprint_14.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_14_una_pagina.md) · [Paso 5 →](Reto_Sprint_14_paso_5.md)
<!--/nav-->

1. Copiar `plantilla_ficha_proyecto.md` como `ficha_proyecto.md` y rellenar los nueve apartados en una página.
2. Revisarla entre todos: ¿se entiende sin explicaciones?
3. Subirla a `sprint-14/` **antes de las 14:30**.

**En sencillo.** La ficha es **la hoja de una página que resume vuestro proyecto**, como el folleto de un servicio: pregunta, para quién, con qué datos y cómo sabréis si ha ido bien. El docente (vuestro cliente) la lee y os contesta *go*, *go con cambios* o *no-go*; sin ella no puede dar el visto bueno. No es un examen: se puede mejorar después, pero tiene que estar hoy. No se programa; se escribe en un archivo de texto con las plantillas que ya existen. Lo único que hay que saber es escribir con claridad.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Ficha de proyecto** | El resumen de una página del proyecto (el «anexo A» de las reglas). |
| **Markdown (`.md`)** | Un archivo de texto con símbolos sencillos (`#` para los títulos, guiones para las listas). GitHub lo muestra bien formateado. |
| **Métrica de negocio** | Lo que mide el valor para el cliente, con sus palabras (euros ahorrados, horas, errores evitados). |
| **Métrica técnica** | Lo que mide cómo de bien predice el modelo (por ejemplo, MAE, F1 o AUC). |
| **Umbral de éxito** | El valor de la métrica a partir del cual diréis «el proyecto vale la pena». |
| **Baseline** | El modelo más simple posible, que habrá que superar (por ejemplo, «igual que la semana pasada»). |
| **AI Act** | El reglamento europeo de IA. Clasifica los sistemas por riesgo: mínimo, limitado, alto o inaceptable. |
| **Commit** | Cada vez que guardáis un cambio en GitHub con un mensaje corto. |

**Cómo se hace**

1. **Copiar la plantilla.** Abrid [`plantilla_ficha_proyecto.md`](../1_Trabajar/plantillas/plantilla_ficha_proyecto.md) y pulsad **Raw**. Seleccionad todo (`Ctrl + A`) y copiad (`Ctrl + C`). En la carpeta `sprint-14` del repositorio del equipo: *Add file → Create new file*, nombre `ficha_proyecto.md`, pegad (`Ctrl + V`). No pulséis aún **Commit changes**: rellenad primero. El nombre, en minúsculas y sin espacios.

2. **Repartir el trabajo (sugerido).** Una persona escribe y el resto aporta, por apartados: el Scrum Master junta el texto final; el responsable de datos escribe el 4; el responsable técnico, el 5, el 6 y el 7; el responsable de IA responsable, el 8; y el 1, el 2, el 3 y el 9 se escriben entre todos. Cuidad que **todo cabe en una página**: si no cabe, resumid.

3. **Rellenar los apartados.** Sustituid los `______` y borrad las notas en cursiva (las que van entre `*( )*` o `*…*`). Cada apartado pide una cosa:

    | Apartado de la ficha | Qué escribís |
    |---|---|
    | Cabecera | Nombre de vuestra consultora, la fecha y `Versión: 1` |
    | 1 · Equipo y roles | La tabla con las cuatro personas, su rol en el sprint 14 y la rotación prevista (copiadla de la nota del paso 1) |
    | 2 · Brief y pregunta | Dejad solo vuestro brief (1 Demanda turística · 2 Cultivos · 3 Asistente FP · 4 Energía · Libre) y la pregunta de negocio en **una frase**: «¿Podemos … para que el cliente pueda …?» |
    | 3 · Cliente y decisión | Quién usará el resultado y qué decisión concreta mejora, **y qué pasa hoy sin el modelo** |
    | 4 · Datos | Una fila por fuente validada en el paso 3: enlace, licencia, tamaño, variables clave y limitaciones previstas |
    | 5 · Métrica y baseline | Métrica de negocio, **métrica técnica**, umbral de éxito, baseline previsto y cómo partiréis los datos (temporal si son series) |
    | 6 · Modelos previstos | Al menos tres modelos, uno de ellos neuronal (o un LLM con RAG en el brief 3). Las técnicas esperadas de cada brief están en `briefs_y_rubrica.md` |
    | 7 · Demostrador | La tecnología (Streamlit, Gradio, cuaderno con widgets o API) y qué hará. El plan B ya viene escrito: un vídeo de 90 segundos |
    | 8 · Riesgos | Tres riesgos con su tipo (datos, cómputo, ética o equipo) y su mitigación; la clasificación preliminar del AI Act y si hay datos personales (sí / no) |
    | 9 · Backlog | Las historias principales (lista corta) y **una frase medible** para el objetivo de cada sprint, del 14 al 17 |

    Para la clasificación del AI Act, tomad esta orientación de la plantilla del plan ético: un sistema que solo predice demanda agregada suele ser de riesgo **mínimo**; un chatbot que informa a personas tiene obligaciones de **transparencia** (riesgo limitado); un sistema que decide sobre el acceso de personas a educación, empleo o servicios esenciales es de **alto riesgo**.

    Dejad la última línea (**Respuesta del docente**) como está: la rellena el docente.

4. **Un buen resultado se parece a esto** (ejemplo de redacción, no lo copiéis):

    - Pregunta: «¿Podemos predecir la ocupación hotelera de Gran Canaria con 3 meses de antelación con un error menor del 8 %, para planificar plantilla y compras?».
    - Decisión que apoya: «Cuándo contratar refuerzo en temporada media».
    - Baseline: «Predecir lo mismo que el año anterior en la misma semana».
    - Un riesgo específico: «Los datos son de hoteles grandes: no representan a pequeños alojamientos rurales».
    - Objetivo del sprint 15: «Comparar al menos tres modelos con un registro y elegir un candidato».

    **La métrica, ahora.** Escribid la métrica técnica y el umbral **ahora** y no los cambiéis cuando veáis los resultados: elegirlos después es la trampa más fácil de caer.

5. **Revisar entre todos (10 minutos).** Que una persona que **no escribió** la ficha la lea en voz alta como si fuera el cliente y conteste: (a) ¿la pregunta cabe en una frase?; (b) ¿dice qué decisión mejora y qué pasa hoy sin el modelo?; (c) ¿el umbral de éxito se entiende sin jerga? Si alguna respuesta es «no», corregid antes de subirla. Comprobad también que no quedan `______` ni notas en cursiva.

6. **Subirla antes de las 14:30.** Pulsad **Commit changes**, escribid un mensaje corto («Subo la ficha de proyecto») y confirmad. El procedimiento completo, con capturas, está en [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md). Recargad la carpeta `sprint-14` y comprobad que aparece `ficha_proyecto.md`. El docente la lee en el repositorio y responde con el *go / no-go* **el día siguiente por la mañana**.

**Qué deberíais ver.** Una ficha de una página, sin notas en cursiva y sin `______`, con la fecha y `Versión: 1`; y `ficha_proyecto.md` dentro de `sprint-14/` en GitHub, con una hora de subida anterior a las 14:30 en el historial (icono del reloj).

**Hecho cuando:** la ficha está subida antes de las 14:30 y el docente puede abrirla.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| La ficha ocupa más de una página | Os habéis extendido. | Resumid: una frase por casilla, tablas con una o dos filas por apartado; los detalles van al plan de datos y al backlog. |
| No sabéis qué poner como métrica de negocio | Falta traducir el modelo a valor para el cliente. | Completad: «reducir X € de coste», «ahorrar N horas» o «evitar N errores por mes», con una cifra aproximada. |
| El archivo quedó en la raíz del repositorio, no en `sprint-14/` | Se subió sin entrar antes en la carpeta. | Abrid el archivo → icono del lápiz → delante del nombre escribid `sprint-14/` → **Commit changes**. |
| GitHub muestra las tablas como texto suelto, con barras verticales | Falta una línea en blanco antes de la tabla o se borró una barra. | Comprobad con **Preview** y volved a poner la línea en blanco o la barra que falta. |
| El nombre se ha subido con mayúsculas o espacios | El nombre no cumple la regla. | Renombradlo en minúsculas y sin espacios: `ficha_proyecto.md`. |
| Son las 14:15 y la ficha no está completa | El plazo es firme. | Subid la versión que tengáis, aunque falte algo: se corrige después del *go / no-go* con una versión 2. |

<!--nav-->
---

[← Paso 3](Reto_Sprint_14_paso_3.md) · [Ficha del reto](Reto_Sprint_14.md) · [Paso 5 →](Reto_Sprint_14_paso_5.md)
<!--/nav-->
