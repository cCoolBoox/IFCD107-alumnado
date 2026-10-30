# ¿Cuántos sprints tiene nuestro proyecto?

**Cuándo:** el 25/11, al cerrar el Sprint 13, o antes del *planning* del 26/11 (Sprint 14). **Tiempo:** 25–30 min. **En equipo.**
**Qué necesitas:** esta guía, la plantilla [`plantilla_backlog_y_sprints.md`](../../../S14/3_Reto/4_Plantillas_y_entrega/plantilla_backlog_y_sprints.md) y lo que sabéis de vuestros retos anteriores.
**Resultado:** una tabla de capacidad, un backlog con tallas y la decisión «cabe / no cabe», que alimenta la tabla de **objetivos por sprint** de la plantilla.

---

## 1. La respuesta corta

**El proyecto final tiene 4 sprints: 14, 15, 16 y 17, del 26/11 al 14/12.** El número lo fija el calendario del curso, no el equipo. Lo que **sí decidís vosotros** es **qué cabe en esos 4 sprints**.

| Sprint | Fechas | Horas de clase | De ellas, de trabajo en equipo (PBL) | Hito |
|---|---|---|---|---|
| 14 · Reto, equipo y datos | 26–30/11 | 18 h | 14 h | 26/11 brief · 27/11 go / no-go |
| 15 · Modelado y experimentos | 1–3/12 | 18 h | 14 h | 3/12 modelo candidato |
| 16 · Evaluación, IA responsable y entrega | 4–10/12 (clases 4, 9 y 10; no hay el 7 ni el 8) | 18 h | 14 h | 10/12, 14:30: congelación |
| 17 · Storytelling, ensayos y defensa | 11 y 14/12 | 8 h | 5 h | 11/12 ensayo · 14/12 defensa |
| **Total** | | **62 h** | **47 h** | |

> **Regla de oro:** el curso tiene **fecha fija**, así que cuando algo no cabe se **recorta el alcance**. Nunca se añade un «sprint 18» ni se cuenta con horas que no están en el calendario.

## 2. ¿Y en un proyecto real? El cálculo va al revés

Fuera del curso, normalmente **no hay un número de sprints dado**: lo calculas.

| Situación | Qué es fijo | Qué se calcula |
|---|---|---|
| **Fecha fija** (como este curso, o una feria, o un contrato) | Fecha y nº de sprints | Qué alcance cabe |
| **Alcance fijo** (el cliente pide todo esto) | Lo que hay que entregar | **Nº de sprints** y fecha final |

La fórmula del segundo caso es esta, y es la que vais a practicar:

> **Nº de sprints = trabajo total estimado (con colchón) ÷ capacidad de un sprint**, redondeado hacia arriba.

Y se **recalcula en cada *review***: con lo que de verdad se ha hecho en el sprint (vuestra velocidad), no con lo que se esperaba hacer. En proyectos reales se da un **rango** («entre 5 y 7 sprints»), no una cifra única.

## 3. Los 5 pasos

### Paso 1 · Fijad el calendario real
Usad la tabla del apartado 1. Contad solo los días con clase y las horas **de trabajo en equipo (PBL)**: las horas de teoría y de práctica guiada no son del proyecto.

### Paso 2 · Calculad la capacidad
**Capacidad del sprint = personas × horas de trabajo × factor de foco.**
El factor de foco descuenta ceremonias (*daily*, *planning*, *review*), bloqueos y esperas. **Empezad con 0,7** (regla práctica) y ajustadlo con lo que visteis en vuestros retos: si siempre acabáis ahogados, bajadlo a 0,6; si os sobra tiempo, subidlo a 0,8.

### Paso 3 · Estimad el backlog con tallas
Cada historia del backlog (10–15 historias, ver la plantilla) recibe una talla: **S, M o L**. Convertidlas a horas de trabajo de equipo con una tabla de partida y **ajustadla con un reto que ya hicisteis** («aquel notebook nos costó una L»):

| Talla | Qué es | Horas de partida |
|---|---|---|
| **S** | Una cosa clara, pocas dudas | 2 h |
| **M** | Varias partes, alguna duda | 5 h |
| **L** | Mucho trabajo o mucha incertidumbre | 10 h |

> Una historia **mayor que una L** no se estima: se **divide** en historias más pequeñas.

### Paso 4 · Calculad si cabe y cuántos sprints son
1. Sumad las horas del backlog.
2. Añadid un **colchón del 20 %** (siempre hay imprevistos).
3. Comparadlo con la capacidad del Sprint 14 al 16, que es donde se hace el trabajo; el 17 es sobre todo defensa.
4. Si **cabe**, perfecto. Si **no cabe**, pasad al paso 5.

### Paso 5 · Si no cabe, recortad con criterio
Ordenad las historias con **MoSCoW** y quitad **de abajo hacia arriba**:

| Categoría | Qué es | ¿Se recorta? |
|---|---|---|
| **Must** (imprescindible) | Los requisitos **R1–R11** de [`briefs_y_rubrica.md`](../../../../proyecto-final/briefs_y_rubrica.md) | **Nunca** |
| **Should** (importante) | Lo que mejora mucho el resultado | Solo si no hay otra salida |
| **Could** (deseable) | Un tercer modelo extra, un demostrador más vistoso… | **Se recorta primero** |
| **Won't** (esta vez no) | Lo apuntáis para «trabajo futuro» en la memoria | Ya recortado |

Los **cambios de alcance después del 27/11** se negocian en la *review* con el docente: no se improvisan.

## 4. Ejemplo resuelto (equipo de 3 personas)

**Capacidad** (3 personas, factor 0,7):

| Sprint | Horas PBL | Capacidad del equipo |
|---|---|---|
| 14 | 14 h | 3 × 14 × 0,7 = **29,4 h** |
| 15 | 14 h | 3 × 14 × 0,7 = **29,4 h** |
| 16 | 14 h | 3 × 14 × 0,7 = **29,4 h** |
| 17 | 5 h | 3 × 5 × 0,7 = **10,5 h** |
| **Total** | 47 h | **98,7 h** |

**Backlog** de la plantilla (12 historias): 4 tallas S (4 × 2 h = 8 h), 4 tallas M (4 × 5 h = 20 h) y 4 tallas L (4 × 10 h = 40 h) → **68 h**. Con el 20 % de colchón: 68 × 1,2 ≈ **82 h**.

**Decisión:** el Sprint 14 al 16 tienen 3 × 29,4 = **88,2 h**. Como 82 h ≤ 88,2 h, **cabe**, con el Sprint 17 libre para ensayo y defensa. Para el reparto: lo más grande y arriesgado (las historias L de modelos y demostrador) no se deja para el último sprint.

> **¿Y si el backlog, con el colchón, hubiera sumado 110 h?** 110 > 88,2: **no cabe**. Se recorta: fuera el tercer modelo extra y el demostrador vistoso (*Could*), y se apuntan como trabajo futuro. Si aun así no cabe, se divide la historia más grande y se reduce su alcance. **Nunca** se quita un requisito R1–R11.

## 5. Plantilla para rellenar

**Equipo:** ______ · **Personas:** ___ · **Factor de foco:** ___ (partimos de 0,7)

**A) Capacidad**

| Sprint | Horas PBL | Personas × horas × factor | Capacidad (h) |
|---|---|---|---|
| 14 | 14 | | |
| 15 | 14 | | |
| 16 | 14 | | |
| 17 | 5 | | |
| **Total** | 47 | | |

**B) Backlog con tallas** (copiad vuestras historias de la plantilla)

| ID | Historia | Talla (S/M/L) | Horas | Must / Should / Could | Sprint |
|---|---|---|---|---|---|
| H1 | | | | | |
| H2 | | | | | |
| H3 | | | | | |
| … | | | | | |
| | **Suma del backlog** | | | | |

**C) Decisión**

| Cálculo | Resultado |
|---|---|
| Suma del backlog (h) | |
| Colchón del 20 % (× 1,2) | |
| Capacidad de los sprints 14 a 16 (h) | |
| **¿Cabe?** (sí / no) | |
| Si no cabe: qué historias *Could* salen | |

Cuando esté claro, **trasladad el resultado a la tabla de «Objetivo de cada sprint»** de la plantilla del backlog y guardadlo en `docs/scrum/` del repositorio del equipo.

## 6. Errores frecuentes
- **Contar 62 h por persona.** Solo son de trabajo en equipo las horas PBL (47 h), y con el factor de foco todavía menos.
- **Sin colchón.** Planificar al 100 % garantiza llegar tarde.
- **Dejar lo difícil para el final.** El modelo candidato se elige el **3/12**; la congelación es el **10/12 a las 14:30**.
- **Dejar la memoria para el último día.** El informe visual del Sprint 13 es su semilla: se escribe en cada sprint.
- **Historias gigantes sin dividir.** Si una historia es «hacer los modelos», no es estimable.
- **No recalcular.** En cada *review* comparad lo previsto con lo hecho y ajustad el sprint siguiente.
- **Estimar solo una persona.** Estimad **todo el equipo a la vez** (cuenta atrás y todos muestran su talla; si hay diferencia, se explica y se repite), como en la simulación del Sprint 0.
