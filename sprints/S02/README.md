# README Sprint S02 · Las matemáticas y la estadística detrás

**Pregunta guía:** ¿en qué se apoyan los modelos y cuándo no debemos fiarnos de un dato?
**Fechas:** jue 22/10 – vie 23/10 · **Horas:** 12 h (5 h teoría · 4 h práctica · 3 h PBL)
**Módulo:** M1a (UD 1a.4 a 1a.6) · Bloque A: sin Python (papel, calculadora, Desmos/GeoGebra)

📄 **Este README en PDF:** [a color](README_Sprint_02.pdf) · [ecofriendly, para imprimir](README_Sprint_02_ecofriendly.pdf) (descárgalo para que funcionen los enlaces; la vista previa de GitHub no los abre).

## Qué aprenderás
1. Operar con **vectores y matrices** y entender qué hace un modelo cuando "multiplica" datos por pesos.
2. Interpretar una **derivada**, un **gradiente** y el **descenso del gradiente** como la forma en que un modelo mejora poco a poco.
3. Resumir datos con **media, mediana, desviación típica y cuartiles**, y calcular **probabilidades**, incluida la **probabilidad condicionada** y el teorema de **Bayes**.
4. Detectar **muestras sesgadas**, la **confusión entre correlación y causalidad** y la **paradoja de Simpson**.
5. Conocer el **ecosistema de software** de IA (Python, Colab, librerías, GPU) y tener tus cuentas listas.

## Requisitos previos
Sprint 1 terminado. Matemáticas de secundaria (fracciones, potencias, porcentajes). Una calculadora o el móvil.

## 📎 Materiales del sprint

**Documentos del curso** (PDF y .md; las actividades van en la tabla siguiente)

| Material | Tema | Tiempo | Cuándo |
|---|---|---|---|
| [Guía del sprint (PDF)](guia/Guia_Sprint_02.pdf) · [ecofriendly](guia/Guia_Sprint_02_ecofriendly.pdf) | Resumen del sprint: qué aprenderás, temario, material, reto y conclusión | 2 páginas | Antes de empezar |
| [**Carpeta del reto: `Reto_S02/`**](Reto_S02/) | Todo el material del reto junto: ficha (.md y PDF), plantilla del dictamen, rúbrica, datos del informe (`informe_cliente`) y láminas del reto | — | Antes del planning y durante el reto |
| [Reto completo, paso a paso (.md)](Reto_S02/Reto_Sprint_02.md) · [PDF](Reto_S02/Reto_Sprint_02.pdf) · [ecofriendly](Reto_S02/Reto_Sprint_02_ecofriendly.pdf) | Qué pide el cliente, pasos, ayudas y errores frecuentes (la rúbrica va aparte) | — | Antes del planning y durante el reto |
| [Resumen del sprint en una página](infografias/S02_00_resumen_del_sprint.png) | Lámina con la pregunta guía, qué aprenderás, cómo se reparte el sprint (teoría, práctica y reto) y dónde estás en el curso | — | Antes del planning |
| [El reto paso a paso](Reto_S02/S02_03_reto_paso_a_paso.png) · [PDF con enlaces](Reto_S02/S02_03_reto_paso_a_paso.pdf) | Qué pide el cliente, los pasos con su día, minutos, quién los hace y enlaces al material de cada paso, las cartas de error y un bloque del dictamen resuelto | — | Antes del planning y durante el reto |
| [Esquema del contenido y su relación con el reto](infografias/S02_07_esquema_contenido_y_reto.png) | Qué presentación prepara cada pieza del entregable, con el material que se reutiliza después | — | Antes del planning y como guía durante el reto |
| [Infografías del sprint](infografias/) | 2 láminas ilustradas | — | Antes del planning |
| [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md) | El método de trabajo de todos los retos | — | Antes del primer reto |
| [`S02.3_Ecosistema_de_software_para_IA.pdf`](presentaciones/S02.3_Ecosistema_de_software_para_IA.pdf) | Ecosistema de software para IA: Python, Colab, librerías y GPU | 5 min | Teoría · día 1 del S02 |
| [`S02.1_Matematicas_para_IA.pdf`](presentaciones/S02.1_Matematicas_para_IA.pdf) | Matemáticas para IA: álgebra lineal, derivadas y gradiente | 45 min | Teoría · día 1 del S02 |
| [`S02.2_Estadistica_y_probabilidad.pdf`](presentaciones/S02.2_Estadistica_y_probabilidad.pdf) | Estadística y probabilidad: descriptiva, Bayes, correlación y paradoja de Simpson | 35 min | Teoría · día 2 del S02 |
| [Test de conocimientos](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S02/tests/test_M1a.html) | Test corto de M1a · Fundamentos de IA · 12 preguntas · individual, en el navegador, sin penalización por fallo. | 20 min | Solo se abre el vie 23/10 (hora de Canarias) |

**Material de las actividades**

Materiales `.md` para papel o pantalla (sin Colab):

| Material | Contenido |
|---|---|
| [`apuntes_matematicas_y_estadistica.md`](actividades/apuntes_matematicas_y_estadistica.md) | **Apuntes que complementan las diapositivas**: vectores, matrices, derivadas, gradiente, estadística, Bayes, sesgos y Simpson, explicados paso a paso con ejemplos |
| [`alta_cuentas.md`](actividades/alta_cuentas.md) | Alta en Colab y GitHub (**jueves 22/10, a primera hora, en clase**) |
| [`ejercicios_algebra_calculo.md`](actividades/ejercicios_algebra_calculo.md) | 12 ejercicios de vectores, matrices, derivadas y gradiente |
| [`ejercicios_estadistica.md`](actividades/ejercicios_estadistica.md) | 14 ejercicios de estadística, probabilidad, Bayes, sesgo y Simpson |
| [`estadisticas_enganosas.md`](actividades/estadisticas_enganosas.md) | 9 casos de estadísticas engañosas |
| [`plantilla_dictamen.md`](Reto_S02/plantilla_dictamen.md) | Plantilla del dictamen del reto, con la afirmación 1 resuelta como modelo |
| [`autoevaluacion_y_coevaluacion.md`](Reto_S02/autoevaluacion_y_coevaluacion.md) | Hoja de autoevaluación (cada persona) y coevaluación (quien revisa el dictamen en la revisión cruzada) |
| [`rubrica_dictamen.md`](Reto_S02/rubrica_dictamen.md) | Rúbrica del reto: 4 criterios, de 1 a 4 |

Mínimo de ejercicios: **M1, M2 y M7** de la hoja 1 y **E1, E2, E6, E8 y E10** de la hoja 2. El resto son extra (si queréis ir más allá, M10 y M11 sobre el descenso del gradiente son los más recomendables). Escribid cómo lo habéis hecho.

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

**Día 1 del S02**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 1 | 🔔 Ceremonia | Planning del reto: leed el informe y repartid las afirmaciones 3 a 6 (paso 1) | 10 min |
| 2 | 💻 Práctica | [Alta en Colab y GitHub, y primer cuaderno abierto](actividades/alta_cuentas.md) | 25 min |
| 3 | 📖 Teoría | [Ecosistema de software para IA: Python, Colab, librerías y GPU](presentaciones/S02.3_Ecosistema_de_software_para_IA.pdf) | 5 min |
| 4 | 📖 Teoría | [Matemáticas para IA: álgebra lineal, derivadas y gradiente](presentaciones/S02.1_Matematicas_para_IA.pdf) | 45 min |
| 5 | 💻 Práctica | [Ejercicios de matemáticas (hoja 1) con Desmos o GeoGebra](actividades/ejercicios_algebra_calculo.md) | 55 min |
| 6 | 🎯 Reto | [Cartas de error, afirmaciones 1 y 2 guiadas y la vuestra (pasos 2 a 4)](Reto_S02/Reto_Sprint_02.md) | 1 h |

**Día 2 del S02**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 7 | 📖 Teoría | [Estadística y probabilidad: descriptiva, Bayes, correlación y paradoja de Simpson](presentaciones/S02.2_Estadistica_y_probabilidad.pdf) | 35 min |
| 8 | 💻 Práctica | [Estadísticas engañosas](actividades/estadisticas_enganosas.md) (4 de los 9 casos en clase). **Para casa:** el resto y la [hoja 2 de ejercicios de estadística](actividades/ejercicios_estadistica.md) | 45 min |
| 9 | 📝 Test | [**Test corto de M1a** (matemáticas y estadística), solo se abre hoy](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S02/tests/test_M1a.html) | 25 min |
| 10 | 🎯 Reto | [Dictamen, frase de IA responsable y revisión cruzada (paso 5)](Reto_S02/Reto_Sprint_02.md) | 55 min |
| 11 | 🔔 Ceremonia | Entrega en `sprint-02/`, autoevaluación y coevaluación, review y retrospectiva | 40 min |

<!--orden:fin-->

## Reto · «¿Nos fiamos de este informe?»

📄 [Reto en PDF](Reto_S02/Reto_Sprint_02.pdf) · [ecofriendly](Reto_S02/Reto_Sprint_02_ecofriendly.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

👉 **[Ver el reto completo, explicado paso a paso](Reto_S02/Reto_Sprint_02.md)** (qué se pide, cómo hacerlo, cómo usar la IA, errores frecuentes y autoevaluación).


**Contexto:** la dirección de TurisData Canarias va a presentar al consejo un borrador sobre cancelaciones y os pide revisarlo. Los datos están en [`informe_cliente.md`](Reto_S02/informe_cliente.md) y [`informe_cliente.csv`](Reto_S02/informe_cliente.csv) (2.400 reservas por tarifa y canal).

**Reto guiado:** tenéis 6 «cartas de error» (con una pregunta para reconocer cada una), la afirmación 1 resuelta como modelo, la afirmación 2 paso a paso con la hoja de cálculo y una [plantilla del dictamen](Reto_S02/plantilla_dictamen.md) con frases para completar.

**Entregáis** (en la carpeta `sprint-02/` del repositorio del equipo):
- Dictamen de 1-2 páginas con **al menos 4 de las 6 afirmaciones** (la 1, la 2 y dos más): carta del error, veredicto, cálculo rehecho y frase corregida.
- Recomendación de tres líneas sobre el canal (afirmación 2) y una frase de IA responsable.
- La hoja de ejercicios con el mínimo básico.

**Reglas:**
- Unas 2 h de reto en dos sesiones (el núcleo cabe en 1 h 30 min); no hace falta Python y cada cifra debe poder rehacerse con los datos.
- Si no hay datos, no inventéis números: decid que no se puede saber y qué faltaría.
- Si usáis IA, declarad dónde y comprobad a mano las afirmaciones 2 y 6; nunca datos personales.

**Se valora:** corrección técnica, reproducibilidad, comunicación al cliente e IA responsable (qué pasaría al entrenar con estos datos).

## ✅ Antes de cerrar el sprint
- [ ] Test de conocimientos hecho el vie 23/10
- [ ] Dictamen con al menos 4 afirmaciones (la 1, la 2 y dos más), cada una con su carta y su veredicto
- [ ] Cálculos rehechos (1 y 2) y recomendación de tres líneas sobre el canal
- [ ] Hoja de ejercicios con el mínimo básico (M1, M2, M7, E1, E2, E6, E8, E10)
- [ ] Alta en Colab y GitHub hecha (jueves 22/10)
- [ ] Entregable subido a la carpeta `sprint-02/` del repositorio del equipo
- [ ] [Autoevaluación y coevaluación](Reto_S02/autoevaluacion_y_coevaluacion.md) rellenadas
