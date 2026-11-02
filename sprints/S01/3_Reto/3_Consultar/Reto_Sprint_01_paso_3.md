# Paso 3 · Fichas de los casos (día 2, 25 minutos)

<!--nav-->
> Sprint 1 · Reto «Auditoría de oportunidades de IA» · paso 3 de 5 · [Ficha del reto](Reto_Sprint_01.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_01_una_pagina.md) · [Paso 4 →](Reto_Sprint_01_paso_4.md)
<!--/nav-->

1. Repartir los cinco casos y mirar el ejemplo resuelto.
2. Rellenar la ficha de cada caso: cuatro completas y la del quinto en versión breve.
3. Crear `informe_oportunidades.md` con la plantilla y pasar las fichas a la tabla del apartado 3.

**En sencillo.** Una ficha de caso es como la etiqueta de un producto: en una fila dice qué problema resuelve, con qué tipo de dato trabaja, cómo aprende el sistema, qué método sirve, qué datos hacen falta y cómo sabremos que funciona. No hace falta saber cómo funciona por dentro ningún algoritmo, solo **para qué sirve** cada familia. Lo difícil es no confundir las palabras, y por eso hay dos trucos más abajo.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Tipo de aprendizaje** | Cómo aprende el sistema: **supervisado** (con ejemplos que ya traen la respuesta), **no supervisado** (busca patrones sin respuestas), **por refuerzo** (por prueba y error, con premios) o **preentrenado + ajuste** (parte de un modelo ya entrenado). |
| **Etiqueta** | La respuesta correcta que acompaña a cada ejemplo del pasado, por ejemplo «se canceló: sí / no». |
| **Familia de algoritmos** | Un tipo de método: reglas, regresión, clasificación, agrupamiento, árboles, redes neuronales… |
| **Métrica de éxito** | Cómo se medirá que el caso funciona, con palabras del cliente: «habitaciones vacías evitadas», «horas ahorradas». |
| **Raw** | El botón de GitHub que enseña un archivo como texto sin formato, para copiarlo. |

**Cómo se hace**

1. **Repartir los casos y mirar el modelo (3 minutos).** Cada persona se queda con uno o dos casos, mejor los que propuso. Abrid el [ejemplo resuelto](../../2_Practica/ejemplo_clasificacion_caso.md): es un modelo de **forma**, no de contenido. Os basta con leer la ficha del caso C01 y su apartado «Por qué esas respuestas».

2. **Rellenar los siete campos de la ficha (12 minutos).** Son las columnas de la tabla del informe. Así se responde con el caso «Resumen automático de reseñas» (ejemplo: no lo copiéis):

    | Campo | Cómo se rellena (ejemplo) |
    |---|---|
    | Nombre | Resumen automático de reseñas |
    | Problema de negocio | La dirección recibe cientos de reseñas y no las lee. Se pierden quejas repetidas |
    | Modalidad | **Texto** (lenguaje) |
    | Tipo de aprendizaje | Podría ser **supervisado** (si hay reseñas ya etiquetadas con «positiva/negativa») o usar un modelo de lenguaje ya preentrenado |
    | Familia de algoritmos | Clasificación de texto o modelos de lenguaje |
    | Datos necesarios (¿existen?) | Reseñas de huéspedes (texto + puntuación). **¿Existen?** Sí, el cliente tiene reseñas, pero conviene revisar si incluyen nombres |
    | Métrica de éxito | % de quejas repetidas detectadas; tiempo que ahorra la dirección |

    Dos trucos para no equivocarse:

    - **Modalidad = tipo de dato** (visión, lenguaje, voz, recomendación, datos tabulares o series, generativa, robótica). No es la técnica.
    - **Tipo de aprendizaje:** preguntaos *«¿tengo ya ejemplos del pasado con la respuesta correcta?»*. Si **sí**, supervisado. Si **no** y queréis agrupar o detectar rarezas, no supervisado. Si el sistema prueba y se le premia, por refuerzo. Si usa un modelo ya hecho (un asistente de texto), «preentrenado + ajuste»; pero si entrenáis con datos vuestros ya etiquetados, es supervisado.

    **Qué no vale:** un problema que dice «usar IA para…» (eso es la solución), «datos del cliente» a secas (decid cuáles), una métrica como «que funcione bien» o poner en «tipo de aprendizaje» lo que es una modalidad.

3. **Ficha del caso sin IA (2 minutos).** Se rellena igual. Con el recordatorio de 48 horas antes de que caduque la cancelación gratuita: modalidad, datos tabulares (las fechas de la reserva); tipo de aprendizaje, «ninguno, es una regla»; familia, «reglas»; datos, la fecha en que caduca la cancelación gratuita (y si existe en las reservas). Añadid «(sin IA)» al nombre.

4. **El quinto caso, en versión breve (3 minutos).** Solo nombre, problema en una línea, modalidad, tipo de aprendizaje, familia y datos. La métrica de éxito es del nivel estándar.

5. **Crear el informe y pasar las fichas (5 minutos).** La persona encargada de `informe_oportunidades.md`:

    - Abre [`plantilla_informe_oportunidades.md`](../1_Trabajar/plantillas/plantilla_informe_oportunidades.md), pulsa **Raw**, selecciona todo (`Ctrl + A`) y copia (`Ctrl + C`).
    - En el repositorio del equipo, **entra primero en la carpeta `sprint-01`**, pulsa *Add file → Create new file*, escribe el nombre `informe_oportunidades.md` y pega (`Ctrl + V`).
    - Rellena la tabla del apartado 3 con las fichas de las demás personas, **cada fila en una sola línea** y sin quitar barras. En «Nombre» añade «(propio)» o «(sin IA)» donde toque.
    - Mira la pestaña **Preview** y pulsa **Commit changes** con un mensaje corto («Subo el informe con la tabla de casos»).

**Qué deberíais ver.** En `sprint-01/`, el archivo `informe_oportunidades.md` y, en su apartado 3, una tabla con cinco filas (la quinta sin métrica) que GitHub muestra como tabla, no como texto con barras. Cada fila tiene modalidad, tipo de aprendizaje, familia y datos, y ninguna celda dice solo «datos» o «IA».

**Hecho cuando:** las cinco filas están en la tabla del informe y alguien que no las escribió las ha leído.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| Habéis puesto «texto» como tipo de aprendizaje | Se confunde modalidad con tipo de aprendizaje. | Modalidad = tipo de dato (texto, imágenes, tablas). Aprendizaje = cómo aprende (con respuestas, sin respuestas, con premios, preentrenado). |
| No sabéis qué familia de algoritmos poner | Hay muchas y no hace falta conocerlas por dentro. | Elegid por el tipo de problema (¿un número, una categoría, grupos, texto generado?) y empezad por la más simple. Mirad los apartados 7 (familias) y 10 (tipos de aprendizaje) de los [apuntes](../../1_Teoria/apuntes/apuntes_ia_conceptos_y_etica.md) y preguntad al docente. |
| No sabéis si los datos existen | No siempre está claro qué tiene el cliente. | Mirad la lista de [datos de TurisData](../../../../datos/README.md) y vuestras notas de la entrevista. Si no queda claro, escribid «a confirmar con el cliente» y recogedlo en el apartado 7 (límites). |
| GitHub muestra la tabla como texto con barras verticales | Falta una línea en blanco antes de la tabla, una barra, o hay un salto de línea dentro de una celda. | Comprobad con **Preview**: cada fila, en una sola línea y con las mismas barras que la cabecera. |
| El archivo quedó en la raíz del repositorio | Se creó sin entrar antes en `sprint-01`. | Abrid el archivo → icono del lápiz → delante del nombre escribid `sprint-01/` → **Commit changes**. |
| Aviso de conflicto al guardar | Dos personas editaron el archivo a la vez. | Recargad la página y repetid vuestro cambio sobre la versión actual. Que escriba una persona cada vez. |

<!--nav-->
---

[← Paso 2](Reto_Sprint_01_paso_2.md) · [Ficha del reto](Reto_Sprint_01.md) · [Paso 4 →](Reto_Sprint_01_paso_4.md)
<!--/nav-->
