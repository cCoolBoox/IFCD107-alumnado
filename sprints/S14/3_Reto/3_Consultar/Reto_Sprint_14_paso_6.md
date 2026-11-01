# Paso 6 · Backlog, plan ético y repositorio (día 3, 140 minutos)

<!--nav-->
> Sprint 14 · Reto «Proyecto final: definir, tener datos y un punto de partida» · paso 6 de 7 · [Ficha del reto](Reto_Sprint_14.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_14_una_pagina.md) · [Paso 7 →](Reto_Sprint_14_paso_7.md)
<!--/nav-->

1. Hacer el backlog de 10 a 15 historias y fijar el objetivo de cada sprint.
2. Rellenar el plan ético con al menos 5 riesgos específicos.
3. Montar el repositorio: README, `requirements.txt` y *commits* de todas las personas.

**Cómo se hace.** Reparto sugerido de los 140 minutos: 45 el backlog, 45 el plan ético y 50 el repositorio. Cada parte la lidera una persona distinta, y otra la revisa.

## 6.1 · Backlog (45 minutos)

Copiad `plantilla_backlog_y_sprints.md` como `backlog_y_sprints.md`. La plantilla trae doce historias de ejemplo: **adaptadlas** a vuestro proyecto y añadid las vuestras hasta tener entre **10 y 15**.

| Orden | Qué hacéis | Pista |
|---|---|---|
| 1 | Escribir cada historia como «**Como** [rol] **quiero** [qué] **para** [beneficio]» | Una historia = una tarea que cabe en unas horas |
| 2 | Añadir criterios de aceptación, tamaño (S, M o L), sprint y responsable | Si no sabéis cómo comprobarla, no está bien definida |
| 3 | Escribir el **objetivo de cada sprint** (14, 15, 16 y 17) en una frase medible | Con los hitos: 3/12 modelo candidato, 10/12 a las 14:30 congelación y 14/12 defensa |
| 4 | Cargar las historias en el **tablero** | El Scrum Master lo mantiene al día |

## 6.2 · Plan ético (45 minutos)

Copiad `plantilla_registro_riesgos_eticos.md` como `riesgos_eticos.md`. Este documento **actualiza el checklist de IA responsable del Sprint 1** (`checklist_etico_v1.md`): si lo tenéis, pasad vuestras respuestas a la columna S1.
- **Parte A.** Rellenad la columna **S14** del checklist con ✔, ◐, ✘ o n/a y la evidencia (por ejemplo, el plan de datos o el EDA).
- **Parte B.** Contestad si hay datos personales, si haría falta una evaluación de impacto, el **nivel de riesgo del AI Act** y qué obligaciones se derivan.
- **Parte C.** Escribid **al menos 5 riesgos específicos de vuestros datos** (no «cuidado con los sesgos»), con probabilidad y impacto de 1 a 3 (nivel = P × I), la medida y el responsable. Mirad los ejemplos por brief al final de la parte C, pero no los copiéis: ajustadlos con vuestras cifras. Dejad vacía la última columna («cómo se evaluó la mitigación»): se rellena en el sprint 16.

## 6.3 · Repositorio (50 minutos)

- Copiad `plantilla_README_repositorio.md` como `README.md` y rellenad lo que ya sabéis: el problema en tres líneas (apartado 1), la estructura del repositorio (apartado 3: el árbol ya muestra las carpetas `sprint-14/` a `sprint-17/`; hoy solo existe la de este sprint, y las demás se crean en su momento), **cómo reproducirlo** (apartado 4: descargar los datos y ejecutar los cuadernos en orden), los datos y licencias (6), el resumen de IA responsable (7), el equipo (8) y el tablero (9). La tabla de resultados y el demostrador se rellenan en los sprints 15 y 16.
- Escribid `requirements.txt`: una librería por línea con su versión, como `nombre==versión`. La versión sale con `pip show nombre` o, en Colab, con `!pip freeze` y buscando el nombre.
- Comprobad que **todas las personas** tienen al menos un *commit* (mensajes del tipo `docs: añado backlog`, `data: añado plan de datos`). Ningún dato personal ni claves.
- En el apartado 7 del README, **declarad el uso de IA**: qué pedisteis y qué comprobasteis a mano.

**Qué deberíais ver.** `backlog_y_sprints.md` con entre 10 y 15 historias y cuatro objetivos de sprint, `riesgos_eticos.md` con cinco filas rellenas, un `README.md` y un `requirements.txt` en la raíz y un tablero con las historias.

**Hecho cuando:** los cuatro documentos están escritos, el tablero tiene las historias y otra persona podría descargar los datos y ejecutar los cuadernos solo con el README.

<!--nav-->
---

[← Paso 5](Reto_Sprint_14_paso_5.md) · [Ficha del reto](Reto_Sprint_14.md) · [Paso 7 →](Reto_Sprint_14_paso_7.md)
<!--/nav-->
