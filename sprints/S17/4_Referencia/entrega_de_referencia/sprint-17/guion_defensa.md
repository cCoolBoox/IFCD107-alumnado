# Guion de defensa · BiciPrevisión · Las Palmeras IA

**Equipo:** Las Palmeras IA · **Turno asignado el 14/12:** 18 min (6 equipos) · **Orden de intervención:** Marta, Persona B, Persona C, Persona D

> Relato en 11 minutos, demostración incluida, y 3,5 minutos de preguntas. **Todas las personas hablan.** Cifras: las de la memoria congelada.

## 1. Guion base (10 minutos de relato)
| Min | Bloque | Diapositivas | Contenido | Voz |
|---|---|---|---|---|
| 0:00-0:45 | **Apertura** | 1 | Gancho («cada hora de ayer, la regla de hoy se equivocó en 75 bicis») y mensaje único | Marta |
| 0:45-2:00 | **Contexto y problema** | 2-3 | La regla de hoy falla 75,4 bicis por hora (140,6 en hora punta); la decisión: cuántas recolocar mañana | Marta |
| 2:00-3:00 | **Qué hicimos** | 4-5 | Dos años de datos abiertos de una ciudad; tres pasos: meta antes, ocho modelos por fechas, examen final una vez | Persona B |
| 3:00-5:00 | **Qué aprendimos** | 6-7 | 44,0 frente a 75,4 (42 % menos, entre el 31 % y el 50 %); la mejor pista es lo de las 4 semanas anteriores | Persona B / Persona C |
| 5:00-7:30 | **Demostración** | 8 | Día normal (14/11): rango y aviso → **Nochebuena (24/12): alerta de festivo** → fecha vacía: mensaje claro. Plan B abierto | Persona C (maneja) / Persona D (narra) |
| 7:30-8:30 | **Límites y riesgos** | 9-10 | Hora punta y festivos; tres riesgos y medidas; el fallo de reponderar | Persona D |
| 8:30-10:00 | **Qué proponemos** | 11-12 | Tres acciones para el lunes; qué **no** hacer; mensaje único | Marta |

**Regla del reloj:** Persona B lleva el cronómetro y avisa con un cartel a los 8 min y a los 9:30.

## 2. Ajuste al tiempo de tu turno (6 equipos, 18 min: 11 de relato, 3,5 de demo, 3,5 de preguntas)
Guion base más 1 minuto de análisis de sesgos en la diapositiva 9 (cobertura del rango por franja, memoria §6).

## 3. Demostración: guion detallado (2,5 minutos)
| Paso | Qué se hace | Qué se dice | Plan B |
|---|---|---|---|
| 1 | Abrir la app (ya lanzada con `streamlit run sprint-16/demostrador/app.py`) | «Esto es lo que vería el responsable de operaciones» | Vídeo de 90 s |
| 2 | Día 14/11/2012 y «Prever el día» | «Mañana habrá unas 5.100 bicis; el pico, a las 17:00; la banda dice cuánto fiarse» | |
| 3 | **Entrada errónea:** fecha vacía (borrar el campo) | «Si alguien se equivoca, la app lo dice sin romperse» | |
| 4 | Día 24/12/2012 | «Nochebuena: avisa de que es un festivo y de lluvia; aquí previó 2.918 y hubo 920: por eso decide una persona» | |

**Antes de subir:** demo probada el 11/12 en una carpeta limpia (`pip install -r requirements.txt`, `pytest -q` en verde); pantalla en modo presentación; sin red; notificaciones apagadas.

## 4. Preguntas del tribunal
**Método RESPONDE (20 segundos):** Repite · Empieza con la respuesta · Sustenta con un dato · Pon el límite · Ofrece el puente a la memoria · Si no lo sabes: no inventes, dilo y explica cómo lo averiguarías.

| # | Pregunta | Quién responde | Respuesta con el dato que la sostiene |
|---|---|---|---|
| 1 | ¿Por qué elegisteis ese modelo y no otro? | Persona B | Boosting de profundidad 6: 40,6 ± 6,8 en validación cruzada; empata con el de profundidad libre (40,8 ± 6,7) y desempatamos por simplicidad. Gana al bosque en 4 de 5 bloques y es 8 veces más rápido; la red neuronal quedó por detrás de la regla de hoy *(memoria §4)* |
| 2 | ¿Cómo sabéis que no hay fuga de datos? | Persona C | Partición por fechas y retrasos de 24 horas o más. Una validación barajada daba 26,7 frente a 40,8 por fechas: la descartamos. Excluimos `casual` y `registered`: suman el objetivo (la prueba con ellas dio 17,0) *(memoria §3 y §4)* |
| 3 | ¿Cuánto mejora frente a lo que se hace hoy y cuánto vale? | Marta | De 75,4 a 44,0 bicis por hora (42 % menos; entre el 31 % y el 50 %), unas 753 bicis menos mal planificadas al día. **En euros no lo hemos medido:** haría falta el coste de una bici mal colocada *(memoria §1 y §5)* |
| 4 | ¿En qué casos no debemos fiarnos del modelo? | Persona D | Hora punta (85,5), cerca de festivos (69,2; sobreprevé 29,9), lluvia o nieve (52 % de error relativo) y sucesos extremos: en Sandy previó 2.520 bicis y hubo 22 *(memoria §5 y §6)* |
| 5 | ¿Qué sesgos habéis encontrado y qué habéis hecho? | Persona D | No hay datos de personas; los subgrupos son franja, festivo y tiempo. Reponderar la hora punta y añadir una variable de festivo no pasaron nuestra regla (validación cruzada). Damos un rango por franja: cobertura de la hora punta 46 % → 78 %; cerca de festivo 62 % → 64 % (se buscaba el 80 %) *(memoria §6)* |
| 6 | ¿Qué datos personales usáis y qué riesgo AI Act tiene? | Persona C | Ninguno: alquileres agregados por hora, sin usuarios ni trayectos. Riesgo mínimo según nuestra lectura del AI Act (predice demanda agregada); no hace falta evaluación de impacto. Lo revisaría una persona del área jurídica antes de desplegar *(memoria §6, riesgos_eticos.md (Parte B))* |
| 7 | ¿Qué pasaría con un suceso atípico o un dato nuevo? | Persona B | Con un 10 % de error en el clima, el error sube de 44,0 a 46,4. Un huracán no lo anticipa; el demostrador avisa si el tiempo previsto es lluvia o tormenta y pide revisión humana *(memoria §5 y §7)* |
| 8 | ¿Cómo lo mantendríais y monitorizaríais? | Marta | Comparar cada semana lo previsto con lo ocurrido; reentrenar si el error semanal supera 66 bicis por hora; reevaluar el rango cada trimestre *(memoria §9; model card §9)* |
| 9 | ¿Qué haríais con más tiempo o más datos? | Persona C | Más años con festivos y lluvia (el punto débil), previsión meteorológica real, un modelo específico para festivos y el coste en euros. **No lo hemos medido:** lo haríamos con un año más de datos y la misma regla de adopción *(memoria §9)* |
| 10 | ¿Qué ha aportado cada persona del equipo? | Marta | Marta: evaluación y gráficos; Persona B: riesgos y README; Persona C: demostrador, pruebas y prueba en limpio; Persona D: mitigación, model card y memoria. Los commits de las cuatro lo reflejan *(memoria §8; README §8)* |

## 5. Ensayos (11/12)
Rondas 1 y 2, ronda extra y ensayo general según el guion del curso. Cambios acordados tras la ronda extra: quitar de la diapositiva 10 una cuarta fila de riesgos (sobraba), poner el 140,6 de la hora punta en la diapositiva 2 y pasar el cronómetro a Persona B.

## 6. Lista del día 14/12
- [x] Presentación en PDF subida antes de las 8:30 y una copia en el ordenador de defensa.
- [ ] Llegada 15 minutos antes; probar proyector, sonido y la demo.
- [ ] Plan B (vídeo) abierto en otra pestaña; memoria USB.
- [ ] Cronómetro y cartel de avisos.
