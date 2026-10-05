# Cómo montar el tablero del equipo en Trello

Trello es gratuito para lo que necesitamos. Si el equipo prefiere otra herramienta (Planner, GitHub Projects, Notion, Jira…), vale, siempre que reproduzca lo mismo: **columnas, etiquetas, roles y fechas** y que el docente pueda entrar a verlo.

**Tiempo estimado:** 30 minutos. Lo hace **el Scrum Master** con el equipo a la vista (proyectando o compartiendo pantalla).

## Paso 1 · Crear el tablero
1. Entrad en trello.com con vuestra cuenta (o creadla).
2. Pulsad **Crear tablero**. Nombre: `IFCD107 · [Nombre de la consultora]`.
3. Visibilidad: **Espacio de trabajo** (o privado con invitaciones). **No lo hagáis público**: contiene nombres.
4. Invitad a todas las personas del equipo y al docente (con el correo que os indique).

## Paso 2 · Columnas (listas)
Creadlas **en este orden**, de izquierda a derecha:

| Nº | Columna | Para qué sirve | Regla |
|---|---|---|---|
| 1 | **Información** | Acuerdo de trabajo, DoD, fechas, enlaces, roles del sprint | Una tarjeta por documento |
| 2 | **Backlog del curso** | Todas las épicas/historias del curso, ordenadas por prioridad | Solo el Product Owner reordena la parte de arriba |
| 3 | **Sprint backlog** | Lo que el equipo se compromete a hacer **en este sprint** | Se rellena en el planning |
| 4 | **En curso** | Tareas que alguien está haciendo ahora | Máximo **2 tarjetas por persona** |
| 5 | **En revisión** | Trabajo terminado, pendiente de que otra persona compruebe la DoD | Nadie revisa lo suyo |
| 6 | **Hecho** | Cumple la DoD | Se archiva al terminar el sprint, tras la review |
| 7 | **Impedimentos** | Bloqueos: falta un dato, una cuenta, una decisión del cliente | El Scrum Master los gestiona |

## Paso 3 · Etiquetas (labels)
Creadlas en **Menú → Etiquetas** con estos nombres y colores sugeridos:

| Etiqueta | Color sugerido | Uso |
|---|---|---|
| Reto PBL | Azul | La tarea forma parte del entregable del reto |
| Teoría / estudio | Verde | Repaso de conceptos, ejercicios |
| Práctica / laboratorio | Amarillo | Notebooks y ejercicios |
| Documentación | Naranja | README, informes, memorias |
| IA responsable | Morado | Riesgos, sesgo, privacidad, checklist ético |
| Cliente | Rojo | Preguntas o entregas al cliente |
| Bloqueado | Negro | Se mueve también a *Impedimentos* |
| Sprint 0 · Sprint 1 · … | Gris (una por sprint) | A qué sprint pertenece |

**Etiquetas por persona:** en Trello se asignan **miembros** a las tarjetas (no etiquetas). Cada tarjeta debe tener **una persona responsable** asignada.

## Paso 4 · Cómo es una buena tarjeta
- **Título** en formato de historia o de acción concreta ("Redactar el acuerdo de trabajo"), no "cosas del cliente".
- **Descripción:** qué hay que hacer y cómo sabremos que está hecho (criterios de aceptación).
- **Miembro:** una persona responsable.
- **Fecha límite:** dentro del sprint.
- **Checklist:** pasos pequeños (o la DoD copiada como lista).
- **Estimación:** en el título, entre corchetes, p. ej. `[3] Mapa de empatía` (puntos de historia).
- **Etiqueta** del tipo y del sprint.

## Paso 5 · Roles rotativos

Cada sprint cambian el **Scrum Master** y el **responsable técnico**. Reglas:
1. Nadie repite un rol hasta que hayan pasado por él todas las personas del equipo.
2. Las dos personas de un sprint no pueden ser las mismas que en el anterior.
3. El relevo se hace en la **retro** del sprint anterior, y se anota en la tarjeta *Roles* (columna Información).

**Tarjeta "Roles" en la columna Información** (copiad y rellenad):

| Sprint | Scrum Master | Responsable técnico |
|---|---|---|
| 0 | | |
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

Con un equipo de 4 personas basta una rotación circular: si las personas son A, B, C, D, en el Sprint 0 el SM es A y el técnico B; en el Sprint 1 el SM es B y el técnico C, y así sucesivamente.

**Qué hace cada rol en el tablero**
- *Scrum Master:* prepara la daily, actualiza las columnas al final de cada sesión, mueve los impedimentos, convoca la retro, comprueba que se cumple el acuerdo.
- *Responsable técnico:* decide con el equipo herramientas y estructura, revisa que el entregable se ejecute desde cero y que el README esté completo.

## Paso 6 · Cargar el backlog del curso
Copiad la tabla del **backlog del curso** ([`plantillas_equipo.md`](plantillas_equipo.md), sección 3) en la columna 2: **una tarjeta por sprint**, con el título del reto y el entregable en la descripción. Los sprints 1–3 se detallan en tarjetas de historias (usad las de ejemplo).

## Paso 7 · Añadir las ceremonias como tarjetas recurrentes
En la columna *Información*, una tarjeta **"Calendario de ceremonias"** con:
- **Planning:** primeros 30 min del sprint.
- **Daily:** 10 min al inicio de cada sesión.
- **Review + retro:** última hora del sprint.

## Paso 8 · Comprobación (antes de la review)
- [ ] 7 columnas en el orden indicado
- [ ] Etiquetas creadas
- [ ] Todas las personas y el docente invitados
- [ ] Tarjeta *Roles* rellena
- [ ] Backlog del curso cargado (una tarjeta por sprint)
- [ ] Al menos **10 tarjetas** con responsable, descripción y fecha
- [ ] Tarjetas del reto del Sprint 0 en su columna real

## Consejos y errores frecuentes
- **Tablero bonito pero desactualizado:** peor que uno feo y al día. Actualizadlo en la daily.
- **Tarjetas gigantes ("Hacer el informe"):** dividid en tareas de 1–3 horas.
- **Demasiadas columnas:** con 7 basta.
- **Todo en manos de una persona:** el Scrum Master facilita, no hace todo.
- **Datos personales:** no pongáis en tarjetas ni teléfonos ni datos de clientes reales.
