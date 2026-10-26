# Apuntes del Sprint 0 · Cómo trabajar en equipo: Agile, Scrum y Design Thinking

Las diapositivas (S00.1 y S00.2) son un esquema. Estos apuntes cuentan lo mismo **con calma, con ejemplos de TurisData y con las ideas que de verdad usarás en el reto**. Léelos antes de montar el equipo o cuando una palabra en inglés te suene a chino. No hay que memorizar nada: hay que **entender para qué sirve cada cosa**.

Aquí no hay matemáticas ni programación. Lo que se aprende es **una forma de trabajar** que usaréis durante todo el curso.

---

## 0. De qué va el sprint (en 1 minuto)

Antes de construir cualquier modelo de IA hay dos preguntas que casi todo el mundo se salta:

1. **¿Cómo vamos a trabajar juntos?** → Agile y Scrum.
2. **¿Qué problema real tiene la persona a la que queremos ayudar?** → Design Thinking.

| Parte | Pregunta | Herramientas |
|---|---|---|
| **Agile y Scrum** | ¿Cómo nos organizamos para trabajar en equipo sin perdernos? | Sprints, roles, tablero, Definition of Done |
| **Design Thinking** | ¿Qué necesita de verdad el cliente? | Entrevista, mapa de empatía, «¿Cómo podríamos…?» |

**El reto** es **constituir vuestra consultora de IA**: equipo, acuerdo de trabajo, tablero, Definition of Done y una entrevista al cliente (TurisData) para entender su problema antes de tocar un dato.

---

# PARTE 1 · Agile y Scrum

## 1. Por qué no sirve «planificarlo todo al principio» (el modelo en cascada)

Imagina que un cliente te encarga un modelo y tú haces esto: **primero** escribes todos los requisitos, **luego** preparas los datos, **luego** entrenas, **luego** pruebas y **al final** se lo enseñas. A esto se le llama **modelo en cascada**: cada fase cae sobre la siguiente y no se vuelve atrás.

Funciona cuando todo se conoce de antemano (construir un puente). **En datos e IA, casi nada se conoce de antemano**:

| Problema de la cascada | Qué pasa en un proyecto de IA |
|---|---|
| **Requisitos congelados** | El cliente cambia de idea a mitad de proyecto, y tú ya has gastado el presupuesto |
| **Feedback tardío** | Solo ve el resultado al final… y puede que no sea lo que quería |
| **Incertidumbre ignorada** | Hasta que no miras los datos no sabes si están bien; hasta que no pruebas, no sabes si el modelo funciona |

**Ejemplo:** te piden «predecir cancelaciones». Tras tres semanas descubres que el fichero de reservas tiene la mitad de las fechas vacías. En cascada lo descubres al final (desastre). En trabajo ágil lo descubres en la **primera semana** y lo hablas con el cliente.

## 2. El Manifiesto Ágil: la idea en una frase

En 2001, 17 profesionales del software firmaron un manifiesto con cuatro prioridades. Se leen como «**A es más importante que B**» (B no se tira, solo va después):

| Valoramos más… | …que |
|---|---|
| **Personas y su forma de hablar entre ellas** | seguir un proceso o una herramienta |
| **Algo que funciona** | documentación enorme que nadie lee |
| **Colaborar con el cliente** | pelearse por el contrato |
| **Responder a los cambios** | seguir un plan rígido pase lo que pase |

**En una frase:** *trabaja en trozos pequeños, enséñalos pronto, escucha y corrige.*

## 3. Scrum: un marco para trabajar en trozos

**Scrum** es la forma más usada de trabajar con Agile. Su idea central: **dividir el trabajo en ciclos cortos llamados *sprints*** (en este curso, de unos 2-3 días de clase), y al final de cada uno tener **algo terminado y enseñable**: el **incremento**.

```
  Lista de todo lo que se quiere    →   Eliges un trozo   →   Lo haces en un sprint   →   Lo enseñas
        (Product Backlog)               (Sprint Backlog)         (varios días)             (Review)
                                                  ↑                                           |
                                                  └────────── aprendes y mejoras (Retro) ─────┘
```

### Los 3 roles

| Rol | Qué hace | Lo que NO es |
|---|---|---|
| **Product Owner (PO)** | Representa al cliente. Decide **qué** se hace primero (ordena la lista). Acepta o rechaza lo entregado. | No dice *cómo* se hace |
| **Scrum Master (SM)** | **Ayuda** al equipo a trabajar bien: quita obstáculos, cuida que se hagan las reuniones. | **No es el jefe** ni reparte tareas |
| **Equipo de desarrollo** | Hace el trabajo. Se organiza solo (3-9 personas). | No espera órdenes |

> En el curso, **el docente es el cliente y el Product Owner**. Vosotros sois el equipo y **rotáis** el rol de Scrum Master y de responsable técnico en cada sprint.

### Los artefactos (las «listas» de Scrum)

| Artefacto | Qué es | Ejemplo en TurisData |
|---|---|---|
| **Product Backlog** | La lista ordenada de **todo** lo que podría hacerse | «Predecir cancelaciones», «segmentar clientes», «analizar reseñas»… |
| **Sprint Backlog** | Lo que se elige hacer **en este sprint**, con su plan | «Limpiar datos de reservas» y «hacer un baseline» |
| **Incremento** | El trabajo terminado del sprint, **usable** | Un informe y un cuaderno que se ejecuta de principio a fin |
| **Definition of Done (DoD)** | Lista de comprobación: **cuándo algo está de verdad terminado** | «Se ejecuta desde cero, tiene README y está subido a Git» |

La **Definition of Done** es clave. «Ya casi está» **no** es terminado. Si una casilla de la DoD está sin marcar, el trabajo no está acabado. Se acuerda **antes** de empezar, entre todo el equipo.

### Las 4 reuniones (ceremonias)

Son reuniones **con duración fija** y un propósito claro:

| Reunión | Cuándo | Para qué |
|---|---|---|
| **Sprint Planning** | Al empezar el sprint | Elegir qué se hace y repartirse las tareas |
| **Daily Scrum** | Cada día, **15 minutos** | Cada persona cuenta: qué hice, qué haré, qué me bloquea |
| **Sprint Review** | Al terminar | Enseñar el resultado al cliente y recoger su opinión |
| **Retrospectiva** | Después de la review | Hablar de **cómo hemos trabajado**: qué mantener y qué cambiar |

**Ejemplo de retro bien hecha:** «Mantener: repasar la DoD antes de entregar. Cambiar: empezar el informe antes del último día». Una retro sin **una acción concreta** no sirve.

### El tablero Kanban

Es el «mural» donde se ve el trabajo. Cada tarea es una **tarjeta** que se mueve entre columnas. En el curso usaréis siete: *Información · Backlog del curso · Sprint backlog · En curso · En revisión · Hecho*… (así las muestra la guía del tablero).

Regla de oro: **máximo 2 tarjetas «En curso» por persona**. Si todo está «en curso», nada se está terminando.

```
Sprint backlog   |   En curso   |   En revisión   |   Hecho
[Limpiar datos]  |  [Baseline]  |   [Informe]     |  [Planning]
[README]         |              |                 |
```

## 4. Scrum en proyectos de IA: lo que cambia

Un proyecto de IA no produce «funciones» predecibles: produce **hipótesis que se comprueban con datos**. Por eso:

1. **Se reserva tiempo para explorar.** Mirar los datos (EDA) y hacer pruebas pequeñas va **antes** de comprometerse.
2. **Un experimento es una tarea del tablero.** Con una hipótesis, una métrica y un criterio de éxito. Si falla, **también se aprende algo**.
3. **Los datos son una dependencia crítica.** Si no tienes los datos a tiempo, el sprint se bloquea. Hay que **vigilarlo en el backlog**.

## 5. Errores frecuentes con Scrum (y cómo evitarlos)

| Error | Por qué falla | Cómo evitarlo |
|---|---|---|
| **La daily como informe al jefe** | Nadie se coordina con nadie | Habla **a tus compañeros**, no al SM |
| **Backlog con todo «urgente»** | Si todo es prioritario, nada lo es | El PO **ordena** y se atreve a dejar cosas fuera |
| **Sprint sin nada terminado** | No hay incremento, no hay feedback | Mejor **menos cosas, pero acabadas** |
| **Retro vacía o convertida en queja** | No hay mejora | Cierra con **una acción concreta** |
| **SM = encargado de las tareas** | El equipo deja de ser autónomo | El SM **facilita**, no manda |

---

# PARTE 2 · Design Thinking: empezar por las personas

## 6. Qué es y cuándo usarlo

El **Design Thinking** es un método para resolver problemas **empezando por las personas** y no por la tecnología. Es muy útil cuando:

- el problema **no está bien definido**,
- las soluciones actuales **no funcionan**,
- el usuario final es **clave** para el éxito,
- o **antes de desarrollar un modelo de IA**.

**El error típico en IA:** «Tenemos un modelo de lenguaje, ¿qué problema le buscamos?». Design Thinking lo da la vuelta: **primero** entiendes el problema humano y **después** decides si la IA es la solución (a veces una hoja de cálculo lo resuelve mejor).

## 7. Las cinco fases

No son una línea recta: **puedes volver atrás** cuando aprendes algo nuevo.

```
 1. Empatizar → 2. Definir → 3. Idear → 4. Prototipar → 5. Testear
      ↑______________________________________________________|
```

| Fase | Pregunta | Qué haces |
|---|---|---|
| **1. Empatizar** | ¿Quién tiene el problema y cómo lo vive? | Entrevistas, observar, mapa de empatía |
| **2. Definir** | ¿Cuál es **el** problema? | Punto de vista (POV) y «¿Cómo podríamos…?» |
| **3. Idear** | ¿Qué podríamos hacer? | Lluvia de ideas: cantidad primero |
| **4. Prototipar** | ¿Cómo lo probamos barato y rápido? | Boceto en papel, maqueta, flujo simple |
| **5. Testear** | ¿Funciona para las personas? | Probar con usuarios reales y escuchar |

## 8. Fase 1: Empatizar

### La entrevista

El objetivo es **escuchar, no confirmar lo que ya crees**. Reglas:

- **Preguntas abiertas** («¿Puedes contarme la última vez que…?»), no de sí/no.
- **No sugieras la respuesta.** ❌ «¿Verdad que las cancelaciones te molestan mucho?» ✅ «¿Qué pasó la última vez que se canceló una reserva?»
- **Escucha más de lo que hablas.** Observa también el lenguaje no verbal.
- **Pregunta «¿por qué?»** varias veces: de ahí salen las causas reales.

> La empatía **no es intuición**: es **trabajo de campo**. Habla con personas reales antes de escribir una línea de código.

### El mapa de empatía

Es un cuadro donde **organizas lo que has oído**:

| Casilla | Qué anotas | Ejemplo (la directora de TurisData) |
|---|---|---|
| **Dice** | Frases textuales | «No sé por dónde empezar con la IA» |
| **Hace** | Lo que observas | Mira hojas de cálculo cada lunes |
| **Piensa** | Lo que cree (no lo dice) | «Si me equivoco, pierdo dinero» |
| **Siente** | Emociones | Inseguridad, prisa |
| **Dolores (pains)** | Frustraciones | Habitaciones vacías por cancelaciones tardías |
| **Ganancias (gains)** | Lo que desea | Prever cancelaciones para vender esa habitación |

## 9. Fase 2: Definir (POV y «¿Cómo podríamos…?»)

Con lo que has aprendido, escribes el problema de forma **precisa**.

**Punto de vista (POV):**

> **[Usuario] necesita [necesidad] porque [insight revelador].**

Ejemplo: *«La directora de TurisData necesita saber con antelación qué reservas se cancelarán, porque las habitaciones vacías de última hora son dinero perdido.»*

Un buen **insight** es algo que **has descubierto** hablando (no lo que ya sabías).

**«How Might We» (HMW) = «¿Cómo podríamos…?»:** conviertes el POV en una **pregunta creativa**. Ni demasiado estrecha ni demasiado ancha:

| Demasiado estrecha | Bien | Demasiado ancha |
|---|---|---|
| «¿Cómo hacemos un modelo con Random Forest?» (ya diste la solución) | **«¿Cómo podríamos ayudar a la directora a vender las habitaciones que se van a quedar vacías?»** | «¿Cómo podríamos mejorar el turismo?» |

## 10. Fase 3: Idear

El objetivo es **cantidad antes que calidad**. Las reglas del brainstorming:

1. **No juzgues** durante la tormenta (el filtro va después).
2. **«Sí, y…»** en vez de «sí, pero…»: construye sobre las ideas de los demás.
3. **Cantidad:** fija un tiempo y compite por el mayor número.
4. **Foco:** vuelve siempre a la pregunta HMW.

Después se **agrupan y se votan** las mejores ideas.

## 11. Fases 4 y 5: Prototipar y testear

- **Prototipar** es hacer una versión **rápida y barata** de la idea (papel, maqueta, pantalla simple). **Regla de oro: si te da vergüenza enseñarlo, está demasiado elaborado.** Se prototipa para **aprender**, no para impresionar.
- **Testear** es ponerlo en manos de **usuarios reales**, observar dónde se confunden y **escuchar sin defenderte**. De cada test puedes volver atrás: replantear el problema o buscar otras ideas.

## 12. Design Thinking + IA: el problema antes del modelo

Antes de elegir un algoritmo deberías poder responder:

1. **¿Quién sufre este problema y por qué?**
2. **¿Qué necesita realmente esa persona?**
3. **¿Es la IA la solución más adecuada, o hay algo más simple?**

Hacer esto antes de modelar **ahorra semanas** y evita construir cosas que nadie usa.

---

## 13. Qué vais a hacer en el reto (resumen)

| Pieza del reto | Qué parte de estos apuntes usa |
|---|---|
| **Planning y roles** | Sección 3 (roles, rotación del SM) |
| **Acuerdo de trabajo y Definition of Done** | Sección 3 (DoD) y sección 5 (errores) |
| **Tablero y backlog del curso** | Sección 3 (Kanban, backlog) |
| **Entrevista al cliente + mapa de empatía + 3 HMW** | Secciones 8 y 9 |
| **Review y retro** | Sección 3 (ceremonias) |

## 14. Chuleta de vocabulario

| Palabra | En lengua normal |
|---|---|
| **Agile (ágil)** | trabajar en trozos pequeños, enseñarlos pronto y corregir |
| **Cascada** | hacer todo en fases seguidas, sin volver atrás |
| **Sprint** | ciclo corto de trabajo que termina con algo enseñable |
| **Product Owner** | quien representa al cliente y decide qué va primero |
| **Scrum Master** | quien ayuda al equipo a trabajar bien (no es el jefe) |
| **Backlog** | lista ordenada de cosas por hacer |
| **Incremento** | el trabajo terminado y usable de un sprint |
| **Definition of Done** | lista que dice cuándo algo está de verdad terminado |
| **Daily** | reunión diaria de 15 minutos |
| **Review** | enseñar el resultado al cliente |
| **Retrospectiva** | revisar cómo hemos trabajado y decidir qué mejorar |
| **Kanban** | tablero con columnas para ver el flujo de trabajo |
| **Empatizar** | entender a la persona a la que se ayuda |
| **POV** | frase: «[Usuario] necesita [algo] porque [insight]» |
| **HMW** | «¿Cómo podríamos…?»: el problema como pregunta creativa |
| **Prototipo** | versión rápida y barata de una idea para aprender |

## 15. Cómo usar estos apuntes

1. **Antes del planning:** lee las secciones 3 y 5 (roles, artefactos, ceremonias, errores).
2. **Antes de la entrevista al cliente:** lee las secciones 8 y 9 y prepara tus preguntas **abiertas**.
3. **Si te atascas** con una palabra, mira la chuleta (sección 14).
4. **Recuerda:** el objetivo del reto no es «hacerlo perfecto», sino **hacer el recorrido completo y aprender del proceso**.
