# Apuntes del Sprint 14 · Cómo formular un proyecto de IA (y no perderse en el intento)

La presentación del Sprint 14 es muy esquemática y **este sprint no enseña técnicas nuevas**: enseña **a decidir qué proyecto hacer, con qué datos y cómo sabréis que habéis acabado**. Estos apuntes **explican cada paso con ejemplos** y con las **trampas más habituales**. Léelos antes del taller de Design Thinking y antes de rellenar la ficha.

> Aquí no hay matemáticas ni código nuevos. Lo que se aprende es **pensar antes de programar**. En los proyectos reales, **la mayoría de los fracasos se deciden en la primera semana**, no al entrenar el modelo.

---

## 0. De qué va el sprint (en 1 minuto)

Hasta ahora hacíais **retos con guion**: alguien os decía qué datos, qué métrica y qué pasos. A partir de ahora, **cuatro sprints (14 a 17) para un proyecto completo, de principio a fin, como una consultora**. **Vosotros decidís el problema, los datos y el alcance.**

| Sprint | Qué se hace |
|---|---|
| **14** | **Formular el proyecto**: brief, datos, EDA, baseline, backlog, riesgos |
| **15** | Experimentos y evaluación única en test |
| **16** | Demostrador, sesgos, model card y memoria técnica |
| **17** | Storytelling y defensa |

> **Lo que decidáis en este sprint condiciona los otros tres.** Dedicad tiempo a **pensar** y **no tengáis prisa por programar**.

**Ya conocéis las herramientas:** Scrum y Design Thinking (Sprint 0), ética (Sprint 1), datos y modelos (Sprints 3 a 12), informe visual (Sprint 13). Aquí se **juntan**.

---

## 1. Sois una consultora; el docente es el cliente

**El docente es el cliente y Product Owner** (Sprint 0). **Los briefs son abiertos a propósito**: dicen *qué pregunta* interesa, pero **no cómo resolverla**. Vosotros decidís el alcance y las técnicas dentro de unos mínimos.

Hay **cuatro briefs** y también un **brief libre**:

| Brief | Pregunta guía (en lengua normal) |
|---|---|
| **1 · Demanda turística** | ¿Podemos prever cuánta gente llegará con 3-6 meses de antelación y qué lo explica? |
| **2 · Salud de cultivos** (visión) | ¿Con qué fiabilidad se distingue una hoja sana de una enferma, y **cuándo no fiarnos**? |
| **3 · Asistente de FP** (LLM/RAG) | ¿Puede un asistente responder **sin inventar**, y cómo lo medimos? |
| **4 · Demanda eléctrica** | ¿Predecimos las próximas 24 h **mejor que un modelo de referencia**? |

**Brief libre:** posible si traéis **datos reales ya identificados**, dificultad comparable y **sin datos personales sensibles**. **Dos equipos pueden elegir el mismo brief**, pero **cada uno define su propia pregunta y su propia métrica**.

**Consejo para elegir:** pensad en **qué disfrutaríais sufriendo durante 4 sprints**, pero también en **riesgos**: ¿hay datos disponibles hoy? ¿necesita GPU? ¿es realista para el tiempo? (La tabla del documento de briefs resume dificultad de datos y carga de cómputo.)

---

## 2. Cómo se formula un proyecto de IA

Un proyecto de IA bien formulado responde a **cuatro cosas**:

| Pieza | Pregunta | Si falta… |
|---|---|---|
| **Pregunta de negocio** | ¿Qué **decisión concreta** tomará alguien con tu modelo? | Construyes algo que nadie usa |
| **Datos** | ¿De dónde salen, con qué **licencia**, cuántos, cómo se accede? | **Si no se pueden usar legalmente, no sirven** |
| **Métrica** | ¿Cómo sabremos que **funciona**? | No sabrás cuándo parar ni si has mejorado |
| **Baseline** | ¿Qué hay que **batir**? | Un resultado sin comparación no significa nada |

> **Métrica y baseline se definen ANTES de ver resultados.** Si las eliges después, es muy fácil (y muy tentador) elegir la métrica que sale mejor.

### 2.1. De una idea vaga a una pregunta de negocio

| ❌ Vaga | ✅ Con decisión concreta |
|---|---|
| «Hacer algo con IA para el turismo» | «**La directora de TurisData decidirá cada lunes qué habitaciones ofrecer con descuento**, según la probabilidad de que se cancelen las reservas de la semana» |
| «Detectar enfermedades en plantas» | «El agricultor fotografía una hoja y **decide si llama al técnico**, según un diagnóstico orientativo con su nivel de confianza» |

**Test de la decisión:** si no puedes decir **quién hace qué distinto gracias al modelo**, **aún no tienes proyecto**.

### 2.2. Métrica de negocio y métrica técnica

**Tenéis que definir las dos** (requisito R1):

| | **Métrica técnica** | **Métrica de negocio** |
|---|---|---|
| Qué mide | Cómo de bien predice el modelo | Cuánto **vale** para el cliente |
| Quién la entiende | Vosotros | El cliente |
| Ejemplo (cancelaciones) | AUC 0,80; recall 75 % | «Evitamos X habitaciones vacías al mes, ≈ Y € de ingresos» |
| Ejemplo (previsión) | MAE de 3 puntos de ocupación | «Planificamos el personal con un margen de ±3 puntos» |

### 2.3. El baseline: «¿qué hay que batir?»

**Baseline** = el método **más simple razonable** (Sprints 1, 6 y 12). Ejemplos de baselines:

| Problema | Baseline |
|---|---|
| Clasificar (¿cancela?) | Predecir siempre la clase más frecuente |
| Predecir un número | Predecir siempre la media |
| Serie temporal | «Mañana igual que hoy» o «igual que la semana pasada» |
| Asistente con documentos | Búsqueda por palabras clave |

**Ejemplo numérico:** vuestra métrica es el MAE de la ocupación. El baseline estacional (la semana pasada) da **5,0 puntos**. Vuestro modelo da **4,0**: **mejora un 20 %** (100·(5 − 4)/5). Sin ese 5,0, el «4,0» **no quiere decir nada**.

> **Un resultado honesto de «no compensa» o «apenas mejora» es una conclusión válida** (y muy valorada). Lo que no vale es **no tener con qué compararse**.

---

## 3. Datos reales: fuente, licencia, linaje, calidad y limitaciones

El requisito **R2** exige **datos reales con fuente y licencia documentadas**. Para cada conjunto de datos, el **plan de datos** (`plantilla_plan_datos_licencias.md`) responde a:

| Campo | Pregunta | Ejemplo |
|---|---|---|
| **Fuente** | ¿Quién publica los datos y dónde? | «ISTAC, estadísticas de turismo» |
| **Licencia** | ¿Qué permite hacer con ellos? | «CC BY 4.0: se puede usar citando la fuente» |
| **Tamaño y acceso** | ¿Cuántos datos y cómo se descargan? | «120 MB, descarga directa» |
| **Linaje** | ¿**De dónde viene cada dato** y qué se le ha hecho? | «Descargado el día X → filtrado a Tenerife → columnas renombradas» |
| **Calidad** | ¿Faltan valores? ¿Hay errores? | «8 % de vacíos en `pais_origen`» |
| **Limitaciones** | ¿Qué **no** puede decir este dato? | «Solo turistas que usan alojamiento reglado» |

### Licencias en una tabla

| Licencia | Qué significa (en corto) |
|---|---|
| **Dominio público / CC0** | Se puede usar casi sin condiciones |
| **CC BY** | Se puede usar **citando la fuente** |
| **CC BY-NC** | Uso **no comercial** (cuidado si el cliente es una empresa) |
| **Datos abiertos de administraciones** | Suelen permitir reutilización **citando la fuente** (revisa los términos) |
| **Sin licencia indicada** | **No asumas que se puede usar.** Pregunta o descarta |

> **Regla práctica:** si no podéis escribir **de dónde viene el dato y qué licencia tiene**, **no lo uséis**.

### Datos personales

Si hay datos de personas (nombres, correos, fotos con caras, ubicaciones precisas…), **aplica el RGPD** (Sprint 1): **minimización** (¿lo necesitas de verdad?), **base legal** y **cuidado con datos sensibles**. **Lo más sencillo: elegir datos que no los tengan.**

---

## 4. EDA orientado a la decisión y baseline

**EDA** = *análisis exploratorio* (Sprint 6). Aquí **no es explorar por explorar**: se explora **para decidir**.

**Preguntas que debe responder vuestro EDA:**

1. **¿Cuántos datos hay y qué forma tienen?** (filas, columnas, tipos).
2. **¿Cómo es la calidad?** (nulos, duplicados, imposibles, outliers) → **informe de calidad del dato**.
3. **¿Está equilibrada la variable objetivo?** (si solo un 3 % de casos son positivos, la exactitud engaña).
4. **¿Quién falta?** (sesgo de muestreo: ¿están todas las islas, todos los meses, todos los cultivos?).
5. **¿Qué relaciones se ven?** (con prudencia: correlación no es causalidad).
6. **¿Hay fuga de datos?** (¿alguna columna que **no se conocería en el momento de predecir**?).

**Después, el baseline** con **la métrica fijada antes**, registrado: será la vara de medir de los Sprints 15 y 16.

---

## 5. Planificar con Scrum

### 5.1. El backlog: 10-15 historias

Una **historia de usuario** describe **qué valor aporta algo, para quién**:

```
Como <quién>, quiero <qué>, para <qué valor>.
```

| Ejemplo de historia | Valor |
|---|---|
| Como **directora de TurisData**, quiero **ver la probabilidad de cancelación de cada reserva**, para **decidir a quién ofrecer un descuento** | Entregable de negocio |
| Como **equipo**, queremos **un baseline documentado**, para **saber qué hay que batir** | Entregable técnico |
| Como **cliente**, quiero **que el demostrador avise cuando falten datos**, para **no fiarme de resultados vacíos** | Robustez |

**Un buen backlog:** entre **10 y 15 historias**, **ordenadas por prioridad** (lo que más valor da primero), y **cada una lo bastante pequeña para terminarse en un sprint** (con su Definition of Done, Sprint 0).

### 5.2. El objetivo de cada sprint

Cada sprint tiene **una frase de objetivo** (Sprint 0):

| Sprint | Objetivo de ejemplo |
|---|---|
| 14 | «Tener la ficha aprobada, los datos documentados y un baseline» |
| 15 | «Elegir un modelo candidato comparando al menos 3 con validación correcta» |
| 16 | «Tener un demostrador funcionando y una memoria completa» |
| 17 | «Defender el proyecto con un relato claro» |

### 5.3. Roles iniciales

En la ficha, el equipo reparte roles (se rotan según el reto):

| Rol | Qué cuida |
|---|---|
| **Scrum Master** | Que se hagan las ceremonias, que no haya bloqueos |
| **Responsable técnico** | La calidad del código y del modelado |
| **Responsable de datos** | Fuentes, licencias, calidad |
| **Responsable de IA responsable** | Plan ético, sesgos, riesgos |

> **Un rol no es «hacer todo ese trabajo tú solo»**: es **cuidar de que se haga bien**.

---

## 6. Riesgos éticos y legales desde el primer día

El requisito **R6** pide un **plan ético** que **actualiza el checklist del Sprint 1**. En este sprint se hace **el plan inicial**; se revisa en el Sprint 15 y se cierra en el 16.

**Seis bloques** (los de la plantilla `plantilla_registro_riesgos_eticos.md`):

| Bloque | Pregunta clave |
|---|---|
| **A1 Propósito** | ¿Hace falta IA? ¿Qué pasa si falla y quién sale perjudicado? |
| **A2 Datos y privacidad** | ¿Hay datos personales? ¿Licencia compatible? |
| **A3 Sesgo y equidad** | ¿Quién falta en los datos? ¿Se mide por subgrupos? |
| **A4 Transparencia** | ¿El usuario sabe que es IA? ¿Se muestra la incertidumbre? |
| **A5 Supervisión y robustez** | ¿Hay revisión humana? ¿Qué pasa con entradas raras? |
| **A6 Impacto** | ¿Se elige el modelo más simple que cumple? |

**Y una clasificación normativa preliminar** (RGPD y **AI Act**: riesgo mínimo, limitado, alto o inaceptable; Sprint 1).

**Ejemplo de riesgo bien escrito:**

| Riesgo | Probabilidad | Impacto | Mitigación | Evidencia |
|---|---|---|---|---|
| Los datos son de laboratorio (fondo uniforme) y el modelo falla con fotos reales | Alta | Alto | Probar con **fotos propias** y medir la caída de rendimiento | Notebook de evaluación |
| El asistente inventa un requisito de acceso | Media | Alto | RAG con citas + respuesta «no consta» + evaluación con 40 preguntas | Informe de evaluación |

> **Cada respuesta debe apoyarse en algo que se pueda comprobar en el repositorio.** «Hemos tenido en cuenta la ética» **no es una evidencia**.

---

## 7. El repositorio y la ficha

### El repositorio

Un buen repositorio de equipo **se puede entender y ejecutar** sin que nadie os lo explique:

| Pieza | Para qué |
|---|---|
| **README** | Qué es el proyecto, cómo se instala y se ejecuta |
| **Carpeta de datos / script de descarga** | Que otro pueda obtener los datos |
| **Carpeta de experimentos** | El registro de pruebas (Sprint 15) |
| **requirements.txt** | Versiones de las librerías |
| **Commits de todas las personas** | Evidencia de que **todos contribuís** |

> **Commits de todas las personas** (requisito R8): **la nota individual depende en parte de ellos**. «Solo lo subía una persona» **no es buena señal**.

### La ficha de proyecto (1 página)

Plantilla `plantilla_ficha_proyecto.md`, con **nueve apartados**:

1. Equipo y roles iniciales
2. Brief elegido y pregunta de negocio
3. Cliente y decisión que se apoyará
4. Datos
5. Métrica de éxito y baseline
6. Modelos previstos (**≥ 3**, incluidas redes o LLM según el brief)
7. Demostrador previsto
8. Riesgos y mitigación
9. Backlog inicial (10-15 historias) y objetivo de cada sprint

**El docente responde con un *go / no-go***: **go** = podéis seguir; **no-go** = **hay que ajustar** (normalmente alcance, datos o métrica). **Pedir cambios es normal**: se corrige la ficha ese mismo día. Lo que mira el docente: ¿**datos accesibles hoy**? ¿**pregunta y métrica claras**? ¿**alcance realista**? ¿**riesgos identificados**?

---

## 8. El taller de Design Thinking (40 minutos)

Es el mismo método del Sprint 0, en pequeño:

1. **Empatía:** ¿qué problema real y cercano os interesa? ¿**quién lo sufre**?
2. **«¿Cómo podríamos…?»:** convertir el problema en **preguntas abiertas**.
3. **Dos briefs candidatos.**
4. **Canvas borrador** del proyecto.
5. **Elegir el brief** antes del descanso (**hito del día 1**).

Si lo hacéis bien, la ficha casi se escribe sola.

---

## 9. Qué se evalúa en este sprint (y cómo prepararlo)

Los criterios de la rúbrica del proyecto final que se empiezan a trabajar aquí:

| Criterio de la rúbrica | Qué hacer ya en el Sprint 14 |
|---|---|
| **A. Problema y valor de negocio** (10) | Pregunta con decisión concreta, métrica de negocio **y** técnica |
| **B. Datos y EDA** (10) | Fuente, licencia, **linaje**, calidad, sesgos de muestreo |
| **E. IA responsable** (10) | Plan ético inicial con riesgos **específicos** |
| **G. Equipo y metodología** (10) | Tablero, backlog, roles, commits de todos |
| **C. Modelado** (20) | Un baseline sólido (la base del resto) |

> **Para llegar a «Apto» en el proyecto se necesita al menos «Suficiente» en los criterios C (modelado) y E (IA responsable).** La IA responsable **no es opcional**.

---

## 10. Errores frecuentes (y cómo evitarlos)

| Error | Por qué es un problema | Cómo evitarlo |
|---|---|---|
| **Elegir los datos después de la pregunta… y no encontrarlos** | Pierdes días | **Validad los datos antes** de cerrar la ficha |
| **Empezar a programar sin ficha** | Acabas con una solución sin problema | Primero **ficha y go**, después el código |
| **Métrica elegida cuando ya ves los resultados** | Es hacer trampa sin querer | **Fijadla antes** y anotadla |
| **Un alcance enorme** («lo hacemos todo») | No acabáis ningún bloque | **Mejor poco y terminado**: nivel básico completo antes que avanzado a medias |
| **Datos sin licencia clara** | No podéis usarlos ni defenderlos | **Sin licencia, no lo uséis** |
| **Plan ético genérico** | No sirve como evidencia | **Riesgos concretos** ligados a vuestros datos y modelo |
| **Una sola persona hace todo** | Nota individual en peligro | **Reparto** y commits de cada integrante |

---

## 11. Dónde practicar cada cosa

| Si no entiendes… | Mira la sección | Practica en |
|---|---|---|
| Qué brief elegir | 1 | Taller de Design Thinking y elección del brief |
| Pregunta de negocio, métricas, baseline | 2 | La ficha del proyecto (apartados 2, 3, 5) |
| Datos, licencias y linaje | 3 | `plantilla_plan_datos_licencias.md` |
| EDA y baseline | 4 | Paso 5 del reto |
| Backlog, objetivos y roles | 5 | `plantilla_backlog_y_sprints.md` |
| Plan ético y riesgos | 6 | `plantilla_registro_riesgos_eticos.md` |
| Repositorio y ficha | 7 | `plantilla_README_repositorio.md` y `plantilla_ficha_proyecto.md` |

## 12. Chuleta de vocabulario

| Palabra | En lengua normal |
|---|---|
| **Brief** | Encargo del cliente, abierto a propósito |
| **Pregunta de negocio** | La decisión concreta que apoyará el modelo |
| **Métrica de negocio / técnica** | Cuánto vale para el cliente / cómo de bien predice |
| **Baseline** | Método simple que hay que batir |
| **Licencia** | Lo que te permite hacer con un dato |
| **Linaje** | De dónde viene cada dato y qué se le ha hecho |
| **Sesgo de muestreo** | Quién falta o sobra en los datos |
| **Backlog / historia** | Lista de tareas / una tarea expresada por su valor |
| **Go / no-go** | Aprobación (o no) de la ficha por el docente |
| **R1-R11** | Los 11 requisitos mínimos del proyecto |
| **Plan ético** | Riesgos de datos, sesgo y normativa, con evidencias |

## 13. Cómo estudiar estos apuntes

1. **Antes del taller**, leed las secciones 1 y 2: son las que os ayudan a elegir.
2. **Antes de rellenar la ficha**, repasad las secciones 2, 3 y 5: **cada apartado de la ficha está explicado ahí**.
3. **Leed el documento `briefs_y_rubrica.md`** y subrayad lo que no entendáis: **la rúbrica de 100 puntos y los requisitos R1-R11 son vuestra guía durante los 4 sprints**.
4. **Regla final:** si no podéis explicar vuestro proyecto en una frase *(«Ayudamos a **[cliente]** a decidir **[decisión]** con un modelo que predice **[qué]**, medido con **[métrica]** frente a **[baseline]**»)*, **aún no está bien formulado**.
