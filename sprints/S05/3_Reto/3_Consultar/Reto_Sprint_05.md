# Sprint 5 · Reto «¿La ocupación depende de esto?»

> **Ficha completa del reto, para consultar.** Para trabajar, [el reto en una página](../1_Trabajar/Reto_Sprint_05_una_pagina.md). Qué se sube y cómo se evalúa: [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md).
>
> - Volver al [README del sprint](../../README.md).
> - Si es vuestro primer reto: [Cómo se trabaja un reto](../../../../material/4.%20Como_se_trabaja_un_reto.md).

## Ficha del reto

### 1 · 🎯 Qué os pide el cliente

**Qué os pide el cliente.** Al dueño de TurisData le han dicho dos cosas: *«cuando hace calor se llena menos»* y *«los festivos llenan»*. Antes de cambiar personal y precios, quiere saber **cuánto** cambia realmente la ocupación diaria con la temperatura y con los festivos, y **con qué seguridad** se puede afirmar. Os da la serie diaria de **tres años** (1096 días). Vuestra respuesta es un **cuaderno** con el análisis, una **base de datos** con los datos y una **respuesta al cliente de 150 palabras como máximo**.

**Cómo se trabaja.** Es el reto más «de números» hasta ahora, pero no hace falta ser matemático: os damos un **cuaderno plantilla** en Colab con las celdas por rellenar y unos **puntos de control** (`assert`) que os dicen al momento si lo que habéis escrito es correcto. Lo más importante: el **descenso del gradiente** (el método con el que un modelo «aprende» ajustando números poco a poco) lo escribís vosotros, sin usar la función ya hecha de una librería. En clase tenéis 10 minutos de planning (día 1) y, el día 2, la práctica de CRUD (que es el paso 1), **45 minutos de reto + 40 de entrega, review y retro**; lo que no quepa va a casa. El equipo decide hasta dónde llega: 🟢 mínimo, 🟡 estándar o 🔴 extra.

---

### 2 · 🧰 Recursos del reto

| Recurso | Para qué lo usaréis | Dónde está |
|---|---|---|
| **El cuaderno plantilla** [`S05_07_reto_ocupacion`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_07_reto_ocupacion.ipynb) | Es el entregable: lo rellenáis celda a celda. Las celdas con `...` o `# TODO` son vuestras | Colab. Usad *Archivo → Guardar una copia en Drive* y compartidla con el equipo (permiso de edición) |
| **Los datos** [`ocupacion_diaria.csv`](../../../../datos/ocupacion_diaria.csv) | 1096 días, **sintéticos**: `fecha`, `ocupacion_pct`, `temperatura_c`, `festivo` (1 = festivo) y `precio_medio` | El cuaderno los descarga solo con la función `dato("ocupacion_diaria.csv")` |
| **Python y sus bibliotecas**: `sqlite3`, `pandas`, `numpy`, `matplotlib`, `scipy`, `statsmodels` | Base de datos, tablas, gráficos, regresión y contrastes | Colab las trae instaladas; el cuaderno las importa en su celda 3 |
| **Cuadernos del sprint** que son la base del reto: [`S05_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_03_gradiente_regresion.ipynb) (gradiente), [`S05_04`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_04_estadistica_descriptiva_ic.ipynb) (intervalos de confianza), [`S05_05`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_05_contrastes_causalidad.ipynb) (contrastes y `statsmodels`) y [`S05_06`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_06_crud_python.ipynb) (CRUD, que es el paso 1) | Las pistas y el código parecido que podéis reutilizar | Colab. Su [código explicado](../../2_Practica/codigo_explicado/README.md) y el de [`S05_07`](../../2_Practica/codigo_explicado/S05_07_reto_ocupacion.md) |
| **Presentaciones y apuntes** | Repasar el gradiente (S05.2), la estadística y el CRUD (S05.3) | [S05.2](../../1_Teoria/S05.2_Descenso_del_gradiente_y_regresion_desde_cero.pdf) · [S05.3](../../1_Teoria/S05.3_Estadistica_con_Python_y_CRUD.pdf) · [apuntes](../../1_Teoria/apuntes/apuntes_numpy_gradiente_y_estadistica.md) |
| **Cómo entregar en GitHub** | Subir los ficheros a la carpeta `sprint-05/` | [Guía de entrega](../../../../material/5.%20Como_entregar_en_GitHub.md) |
| **Autoevaluación y coevaluación** | Cada persona rellena su hoja | [Hoja del sprint](../2_Entregar/autoevaluacion_y_coevaluacion.md) |
| **Un asistente de IA** (opcional) | Entender ideas y errores y pedir pistas | Con las reglas de la «Ayuda 1» del paso a paso |

---

### 3 · 🪜 Guía paso a paso

Son seis pasos, de **105 minutos en total**. Cada uno dice **qué hacéis** (la lista corta), **cómo se hace** con el detalle, **qué deberíais ver** y **cuándo está hecho**. Las ayudas (IA, errores, atascos) están al final. En el horario del día 2 caben unos 70 minutos (la práctica de CRUD, que es el paso 1, y 45 de reto); los 35 que faltan se hacen en la **consolidación** (13:00–13:30) y en la **6.ª hora** (hasta las 14:30), y la subida puede hacerse hasta esa hora. Completad el nivel mínimo y dejad lo demás para casa. Todo se hace **dentro del cuaderno**, de arriba abajo; ejecutad las celdas en orden.

**Cada paso tiene su propia página.** Abrid la que toque y volved aquí cuando acabéis:

- [Paso 1 · Cargar los datos en una base de datos (día 2, 30 minutos)](Reto_Sprint_05_paso_1.md)
- [Paso 2 · Mirar los datos (día 2, 10 minutos)](Reto_Sprint_05_paso_2.md)
- [Paso 3 · Regresión lineal desde cero (día 2, 35 minutos)](Reto_Sprint_05_paso_3.md)
- [Paso 4 · Comparar con una librería (día 2, 10 minutos)](Reto_Sprint_05_paso_4.md)
- [Paso 5 · Medir la seguridad del resultado (día 2, 10 minutos)](Reto_Sprint_05_paso_5.md)
- [Paso 6 · Responder al cliente en 150 palabras, reiniciar y revisar (día 2, 10 minutos)](Reto_Sprint_05_paso_6.md)

#### Ayuda 1 · Cómo usar la IA en este reto

La IA puede ahorrar tiempo, pero **da código y explicaciones que parecen correctos y no lo son**. Reglas:
- **El descenso del gradiente lo escribís vosotros.** Si se lo pedís a la IA, no podréis explicarlo en la review.
- **Cualquier cifra** que aparezca en la respuesta tiene que salir de vuestro cuaderno, no de la IA.
- **Declarad** en la celda «Uso de IA» qué pedisteis y qué comprobasteis.
- **Nada de datos personales ni claves** en una IA.

| Para qué | Ejemplo de petición | Qué comprobáis |
|---|---|---|
| Entender una idea | «Explícame el descenso del gradiente como si fuera bajar una montaña con niebla, sin fórmulas» | Que podéis explicarlo sin mirar |
| Entender un error de código | «Mi curva de aprendizaje sube en vez de bajar. Este es mi bucle: *[código]*. ¿Qué puede pasar?» | Que probáis la sugerencia y la curva baja |
| Interpretar un resultado | «Tengo un p-valor de 0,03 y un intervalo de confianza de [−1,1; −0,4]. Explícamelo para un directivo, con un ejemplo» | Que la explicación coincide con **vuestros** números |
| Revisar la redacción | «Revisa mi respuesta de 150 palabras: ¿hay jerga o algo ambiguo? No cambies las cifras» | Que las cifras siguen siendo las vuestras |

#### Ayuda 2 · Errores frecuentes (y cómo evitarlos)

| Error | Por qué ocurre | Cómo evitarlo |
|---|---|---|
| La curva de aprendizaje sube o da `NaN` | Tasa de aprendizaje demasiado grande o variables sin estandarizar | Reducir la tasa y estandarizar la temperatura |
| Vuestra recta no coincide con `statsmodels` | Pocas épocas o tasa muy pequeña | Más épocas o ajustar la tasa |
| El punto de control 1 falla por el índice o por `con` | El índice no se llama `idx_ocupacion_fecha` o la conexión no se llama `con` | Usar exactamente esos nombres |
| Error al repetir la celda de la base | Falta `if_exists="replace"` al guardar la tabla | Añadirlo |
| Decir que «el calor provoca…» | Se confunde correlación con causa | Hablar de «se asocia con» y explicar los límites |
| Olvidar la estacionalidad | El verano coincide con calor Y con vacaciones | Incluir `mes` en el modelo con control |
| Dar solo el p-valor | «Es lo que importa» | Dar también el **tamaño** del efecto y el **intervalo** |
| El cuaderno solo funciona en un orden raro | Se ejecutaron celdas sueltas | *Reiniciar y ejecutar todo* antes de entregar |
| La respuesta pasa de 150 palabras | No se ha contado | `len(texto.split())` y recortar |

#### Ayuda 3 · Si os atascáis

1. Leed el mensaje del `assert` que falla: dice qué esperaba y qué recibió. Probad la función con un ejemplo pequeño en una celda aparte.
2. Repasad el cuaderno de esa parte: [`S05_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_03_gradiente_regresion.ipynb) para el gradiente, [`S05_05`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_05_contrastes_causalidad.ipynb) para `statsmodels` y los p-valores, [`S05_06`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_06_crud_python.ipynb) para la base de datos; y el [código explicado](../../2_Practica/codigo_explicado/S05_07_reto_ocupacion.md).
3. Preguntad al equipo y, después, al docente (no más de 15 minutos atascados).
