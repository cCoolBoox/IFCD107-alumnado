# Backlog, objetivos por sprint y evidencias Scrum

**Proyecto:** BiciPrevisión · **Product Owner:** el docente · **Scrum Master (rota):** Marta (S14)

> Tablero: columnas *Pendiente · En curso · En revisión · Hecha*, con las 13 historias cargadas el día 1. Capturas al final de cada sprint en `scrum/` dentro de `sprint-NN/`.

## 1. Formato de historia de usuario
> **Como** [rol] **quiero** [acción / resultado] **para** [beneficio]. Criterios de aceptación numerados · tamaño S / M / L · responsable · sprint.

## 2. Backlog inicial (13 historias)
| ID | Historia | Criterios de aceptación | Tam. | Sprint | Responsable | Estado |
|---|---|---|---|---|---|---|
| H1 | Como cliente quiero una pregunta con métrica para saber si el proyecto vale la pena | ① Ficha en 1 página ② *go* del docente ③ umbral de éxito escrito | S | 14 | Marta | Hecha |
| H2 | Como responsable de datos quiero documentar fuente y licencia | ① Fuente con enlace y licencia CC BY 4.0 ② script de descarga que comprueba la huella | S | 14 | Persona C | Hecha |
| H3 | Como equipo queremos un EDA para conocer los datos | ① Informe de calidad ② 4 gráficos ③ un hallazgo que cambia el enfoque | M | 14 | Persona B | Hecha |
| H4 | Como equipo queremos un *baseline* para poder comparar | ① Métrica y partición escritas antes ② MAE, WAPE y hora punta en validación | S | 14 | Persona B | Hecha |
| H5 | Como equipo queremos ≥ 4 modelos comparados con validación temporal | ① `registro.csv` con una fila por prueba ② sin fuga ③ candidato con MAE ≤ 52,1 | L | 15 | Persona B | Pendiente |
| H6 | Como equipo queremos una red neuronal (MLP) comparada con los árboles | ① Entrenada con 3 semillas ② registrada ③ con una frase de diagnóstico | L | 15 | Persona A | Pendiente |
| H7 | Como cliente quiero gráficos claros del error por hora y por día | ① Real frente a previsto ② error por hora ③ título-conclusión | M | 16 | Persona A | Pendiente |
| H8 | Como responsable ético quiero medir los subgrupos y simular una previsión de clima imperfecta | ① MAE por franja, día y clima ② mitigación medida ③ prueba con ruido en el clima | M | 16 | Persona D | Pendiente |
| H9 | Como usuario quiero probar el modelo en un demostrador | ① Formulario con validación ② aviso de incertidumbre ③ `pytest` en verde ④ plan B | L | 16 | Persona C | Pendiente |
| H10 | Como cliente quiero una memoria técnica | ① 10–15 páginas ② *model card* de 2 páginas ③ riesgos cerrados | L | 16 | Persona D | Pendiente |
| H11 | Como equipo queremos una presentación de máx. 12 diapositivas | ① Ensayo general hecho ② una cifra por diapositiva clave | M | 17 | Marta | Pendiente |
| H12 | Como equipo queremos repartir las preguntas de defensa | ① Las 10 preguntas probables con quién responde ② todas las personas hablan | S | 17 | Persona C | Pendiente |
| H13 | Como equipo queremos un test del clima como fuga (modelo con previsión ruidosa) | ① MAE con ruido del 10 % en el clima ② decisión sobre el uso del clima | M | 15 | Persona C | Pendiente |

**Riesgos enlazados a historias:** R-01 y R-02 (clima y fuga) → H13 y H5 · R-04 (tendencia) → H5 · R-05 (uso indebido) → H9 y H10 · R-03 (Sandy) y R-07 (alcance) → H8 y H10.

## 3. Objetivo de cada sprint (Sprint Goal)
| Sprint | Duración | Objetivo (una frase medible) | Hito |
|---|---|---|---|
| 14 | 3 días | Tener la pregunta, los datos con licencia, el EDA y un *baseline* con MAE de 69,5 bicis/hora en validación antes del *go / no-go* del día 2 | día 1 brief y ficha · día 2 go / no-go |
| 15 | 3 días | Un candidato que baje el MAE del *baseline* al menos un 25 % en validación (≤ 52,1), con ≥ 4 modelos registrados y una red | último día: modelo candidato |
| 16 | 3 días | Mirar el test una sola vez, medir subgrupos con una mitigación, demostrador con `pytest` en verde y memoria de 10–15 páginas | último día, 14:30: congelación |
| 17 | 2 días | Defender en 12 diapositivas con ensayo hecho y todas las personas hablando | día 1 ensayo · día 2 defensa |

## 4. Ceremonias (dentro de las horas del sprint)
| Ceremonia | Cuándo | Qué se anota |
|---|---|---|
| Planning | Primeros 30 min | Objetivo del sprint, historias elegidas, capacidad |
| Daily (10 min) | Inicio de cada sesión | ¿Qué hice? ¿Qué haré? ¿Qué me bloquea? |
| Review | Última hora | Qué se enseñó, feedback del cliente, cambios al backlog |
| Retrospectiva (15 min) | Tras la review | 1 cosa que seguir haciendo, 1 que cambiar, 1 acción concreta para el próximo sprint |

## 5. Retrospectivas (una fila por sprint)
| Sprint | Qué fue bien | Qué mejorar | **Acción concreta acordada** | ¿Se cumplió la acción del sprint anterior? |
|---|---|---|---|---|
| 14 | Escribimos la métrica y la partición **antes** de ver resultados y no hubo discusiones después | Tardamos dos horas en elegir brief | Límite de 15 min por decisión en el *planning*; quien se bloquea más de 10 min lo dice en el *daily* | — |
| 15 | *(se rellena al acabar el Sprint 15)* | | | |
| 16 | *(se rellena al acabar el Sprint 16)* | | | |
