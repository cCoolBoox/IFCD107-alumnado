# Plantilla de storytelling · BiciPrevisión · Las Palmeras IA

> Rellenada el 11/12/2026 **antes** de abrir el editor de diapositivas. Todas las cifras son las de la memoria técnica congelada (`sprint-16/docs/memoria_tecnica.pdf`).

## 1. Audiencia
| Pregunta | Respuesta |
|---|---|
| ¿Quién escucha? | El responsable de operaciones de un sistema de bicis compartidas y su equipo (el tribunal): no son técnicos |
| ¿Qué saben ya del tema? ¿Qué **no** saben? | Saben cuántas bicis hay que mover cada día y que hoy se repite lo de la semana pasada. **No** saben qué es un modelo de previsión ni cómo se mide su error |
| ¿Qué decisión tienen que tomar o qué quieren entender? | Si les compensa usar una previsión hora a hora para decidir cuántas bicis recolocar, y cuánto fiarse de ella |
| ¿Qué les preocupa? | Quedarse sin bicis en hora punta, confiar demasiado en una máquina y recortar personal por un error |
| ¿Qué palabras técnicas hay que **traducir**? | MAE, baseline, fuga de datos, validación, subgrupo, intervalo, hora punta |

**Tabla de traducción:**
| Término técnico | Frase que entiende la audiencia |
|---|---|
| MAE de 44,0 | «De media, el modelo se equivoca en 44,0 bicis cada hora» |
| Baseline | «La regla simple que usamos hoy —repetir lo de la semana pasada—, para comparar» |
| Fuga de datos | «El modelo vio la respuesta antes del examen; por eso un resultado demasiado bueno es una señal de alarma (26,7 frente a 40,8)» |
| Validación por fechas | «Probamos con meses que el modelo no había visto, como pasará en la vida real» |
| Intervalo / rango | «La horquilla en la que cabe lo que pasará casi siempre (8 de cada 10 horas)» |
| Subgrupo | «Un tipo de hora o de día: la hora punta, los días cerca de un festivo, los días de lluvia» |

## 2. Mensaje único
**Nuestro mensaje único:** Recomendamos usar BiciPrevisión como borrador diario revisado por una persona, porque falla 44,0 bicis por hora frente a 75,4 con la regla de hoy (−42 %), lo que supone unas 753 bicis menos mal planificadas al día, con la precaución de que en hora punta y cerca de festivos se equivoca más.

**Test del ascensor (20 segundos):** pendiente de hacerlo con una persona ajena al proyecto: ☐ sí ☐ no.

## 3. Pirámide de la comunicación
| Nivel | Contenido | Evidencia (figura / tabla de la memoria) |
|---|---|---|
| **Conclusión** | Recomendamos usar BiciPrevisión como borrador diario revisado por una persona. | Resumen ejecutivo |
| **Argumento 1** (por qué importa) | Hoy se falla 75,4 bicis por hora (140,6 en hora punta) y el operador decide con eso | §1 y figura 2 |
| **Argumento 2** (cómo lo sabemos) | En un examen final con dos meses nuevos, el modelo falla 44,0: un 42 % menos, entre el 31 % y el 50 %; la red neuronal fue peor que la regla de hoy | §4, §5, figuras 4 y 5 |
| **Argumento 3** (límites, riesgos y qué proponemos) | Falla más en hora punta (85,5) y cerca de festivos (69,2); proponemos usarlo como borrador revisado, conectar el tiempo real y medir cada semana | §6, §9, figuras 7 y 8 |

## 4. Arco narrativo
| Momento | Pregunta que responde | Nuestro contenido | Tiempo |
|---|---|---|---|
| **1. Situación** | ¿Cuál es el mundo actual del cliente? | Cada tarde se decide cuántas bicis mover para mañana repitiendo lo de la semana pasada | 1 min |
| **2. Complicación** | ¿Qué problema o coste aparece? | Esa regla falla 75,4 bicis cada hora; en hora punta, 140,6 | 0,5 min |
| **3. Pregunta** | ¿Qué necesitamos saber para decidir? | Cuántas bicis habrá mañana, hora a hora, con lo que se sabe a las 23:00 | 0,5 min |
| **4. Resolución** | ¿Qué hicimos y qué encontramos? | Comparamos ocho modelos con una regla justa: el mejor falla 44,0 (42 % menos); lo que pasó hace 4 semanas es la mejor pista | 3 min |
| **5. Demostración** | ¿Cómo se usa? | Día normal (14/11), rango y aviso; Nochebuena: el aviso de festivo | 2,5 min |
| **6. Límites y riesgos** | ¿De qué **no** fiarse? | Hora punta y festivos; tres riesgos y sus medidas; reponderar la hora punta no funcionó | 1 min |
| **7. Llamada a la acción** | ¿Qué hacer **el lunes**? | Usarlo como borrador revisado, conectar la previsión del tiempo real y medir cada semana | 1,5 min |

**Gancho de apertura:** «Cada hora de ayer, la regla que usáis hoy se equivocó en 75 bicis.»
**Frase de cierre:** Recomendamos usar BiciPrevisión como borrador diario revisado por una persona. Falla 44,0 bicis por hora frente a 75,4 de hoy (−42 %), con la precaución de hora punta y festivos.

## 5. Storyboard (12 diapositivas)
| Nº | Título-conclusión | Elemento visual | Persona que habla | Tiempo |
|---|---|---|---|---|
| 1 | Mensaje único + equipo | Titular con el mensaje único | Marta | 0:45 |
| 2 | Hoy se repite lo de la semana pasada y se falla 75,4 bicis cada hora | Una cifra grande: 75,4 | Marta | 0:45 |
| 3 | Para decidir cuántas bicis recolocar hay que saber cuántas habrá mañana, hora a hora | Esquema en 4 cajas | Marta | 0:30 |
| 4 | Tenemos dos años reales de una ciudad: bastan para aprender, no para festivos | Figura 1 de la memoria (tendencia) | Persona B | 0:30 |
| 5 | Elegimos el modelo con una regla justa: sin trampas y con el examen al final | Tres pasos numerados | Persona B | 0:30 |
| 6 | El modelo falla 44,0 bicis por hora; la regla de hoy, 75,4 | Cifra grande y figura 5 de la memoria | Persona B | 1:00 |
| 7 | La mejor pista para mañana es lo que pasó a esa hora las últimas 4 semanas | Importancia por permutación (fig. 6) | Persona C | 1:00 |
| 8 | En diez segundos, el operador ve mañana hora a hora y cuánto fiarse | Dos capturas del demostrador (fig. 9) y vídeo plan B | Persona C (maneja) y Persona D (narra) | 2:30 |
| 9 | Falla más en hora punta y cerca de festivos | Tres cifras grandes | Persona D | 0:30 |
| 10 | Tres riesgos, tres medidas: el modelo propone y una persona decide | Tabla de 3 riesgos y 3 medidas | Persona D | 0:30 |
| 11 | El lunes: usadlo como borrador, conectad el tiempo real y medid cada semana | Tres acciones numeradas | Marta | 1:00 |
| 12 | Mensaje único + equipo y repositorio | Mensaje único repetido | Marta | 0:30 |

*(Los tiempos suman 10:00. Todas las personas hablan: Marta, 5 diapositivas; Persona B, 3; Persona C, 1 y el manejo de la demo; Persona D, la narración de la demo y 2 más.)*

## 6. El pitch de 3 minutos
| Segundos | Contenido | Nuestra frase |
|---|---|---|
| 0-20 | **Gancho** | «Cada hora de ayer, la regla de hoy se equivocó en 75 bicis.» |
| 20-50 | **Problema** | «Se repite lo de la semana pasada y faltan o sobran bicis, sobre todo en hora punta (140,6 de error).» |
| 50-100 | **Solución** | «Entrenamos un modelo con dos años de datos reales y lo probamos con dos meses que no había visto.» |
| 100-150 | **Resultado** | «Se equivoca en 44,0 bicis por hora: un 42 % menos, unas 753 bicis menos mal planificadas al día.» |
| 150-170 | **Límite** | «En hora punta y cerca de festivos falla más; por eso una persona debe revisarlo.» |
| 170-180 | **Petición** | «Autorizadnos a probarlo como borrador diario con el tiempo real.» |

## 7. Técnicas para que se recuerde
- **Una cifra grande** por diapositiva clave: 75,4, −42 %, 44,0 · 85,5 · 69,2.
- **Comparación** siempre con lo de hoy (la regla de la semana pasada).
- **Analogía:** el baseline es «el parte del tiempo de ayer»; la fuga, «ver la respuesta antes del examen».
- **Regla de tres:** tres pasos, tres cifras de fallo, tres riesgos, tres acciones.
- **Honestidad:** contamos un fallo —reponderar la hora punta empeoró el conjunto— y que Nochebuena salió mal (2.918 previstas, 920 reales).

## 8. Comprobación final
- [ ] ¿Se entiende el mensaje único en 20 segundos? *(pendiente del test con una persona ajena)*
- [x] ¿Cada título de diapositiva se entiende sin oír al orador?
- [x] ¿Las cifras coinciden con la memoria congelada? *(se comprobaron una a una con el PDF de la memoria)*
- [x] ¿Hablan **todas** las personas y el reparto está equilibrado?
- [x] ¿Está la demo probada y el plan B abierto? *(demo lanzada en una carpeta limpia el 10/12; vídeo de 90 s en el ordenador de la defensa)*
- [x] ¿Hay una recomendación accionable y una frase sobre los límites?
- [ ] ¿Cabe en el tiempo del turno con margen de 30 segundos? *(se cronometra en el ensayo general)*

## Revisión con la rúbrica

**Revisado por:** Persona C (no escribió el relato) · **Fecha:** 11/12/2026 (sobre el ensayo general; se completa tras la defensa del 14/12)

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
|---|---|---|
| Corrección técnica | 3 | El PDF tiene 12 diapositivas; comprobé tres cifras (75,4 → 44,0 bicis, 85,5 en hora punta, Nochebuena 2.918 frente a 920) y coinciden con la memoria; la demo salió con una entrada normal y una errónea. Falta un PDF de reserva |
| Reproducibilidad | 3 | Lancé la demo siguiendo solo los pasos escritos y salió lo mismo; el storyboard dice quién habla en cada diapositiva y hablan las cuatro personas |
| Análisis y comunicación al cliente | 3 | La conclusión va primero, el mensaje único está en la 1 y la 12 y hay 6 términos traducidos; falta el test del ascensor con alguien ajeno, por eso no un 4 |
| IA responsable | 4 | Dice dónde falla y para quién, tres riesgos con medidas, qué no hacer, cuenta un fallo (reponderar la hora punta) y declara qué se pidió a la IA y qué se revisó |

**Lo primero que mejoraríamos:** cronometrar el relato con la demo real y hacer el test del ascensor con una persona de fuera; preparar un PDF de reserva con las figuras 7 y 8 de la memoria

**Uso de IA en la preparación de la defensa:** se pidió ordenar los 7 momentos del arco y proponer títulos-conclusión; se revisó cada cifra contra la memoria y se cambió el gancho propuesto («la IA revoluciona la movilidad») por una cifra real del proyecto.
