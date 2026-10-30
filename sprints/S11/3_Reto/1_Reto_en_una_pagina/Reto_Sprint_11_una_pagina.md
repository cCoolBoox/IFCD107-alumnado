# Sprint 11 · Reto «Visión artificial para el cliente» · en una página

> Versión corta para **trabajar con ella abierta**. La ficha completa (pasos, uso de la IA, errores frecuentes y rúbrica) sigue en [Reto_Sprint_11.md](../2_Ficha_completa/Reto_Sprint_11.md); el cuaderno de partida es [`S11_04`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/2_Practica/S11_04_reto_vision_cliente.ipynb).

**El cliente.** TurisData recibe cientos de fotos a la semana y una persona las clasifica a mano. Quiere saber si un modelo puede **pre-clasificarlas** y **en qué se equivoca**. **Lo importante no es el acierto, sino saber cuándo no fiarse.**
**Qué entregáis (no cambia):** el modelo y el **demostrador** (dentro del cuaderno), el **análisis de errores** de 1–2 páginas y un README. **Al final del sprint se suben a `sprint-11/` del repositorio del equipo: 3 ficheros del equipo (esos tres) + 1 autoevaluación y coevaluación por persona.** Las fotos no se suben.
**Tiempo en clase:** planning 10 min · reto 105 min (25 el día 1 y 80 el día 2) · entrega, review y retro 30 min.

## Tres niveles: el equipo decide hasta dónde llega

| Nivel | Qué hay que tener | Nota* |
|---|---|---|
| 🟢 **Mínimo** (todos los equipos) | Una carpeta por clase (el sintético vale) · modelo con *transfer learning* · métricas por clase y matriz de confusión · **3 fotos mal clasificadas** con una hipótesis · README corto · 3 *commits* | 2 |
| 🟡 **Estándar** | Referencia «desde cero» · prueba usada **una sola vez** · **6 fotos mal clasificadas** con hipótesis y mejora · `clasificar_foto` con clase, confianza y «revisar a mano» · origen, licencia y dos riesgos de IA responsable · revisión con la rúbrica | 3 |
| 🔴 **Extra** | Umbral elegido con datos (fotos que revisa una persona frente a fallos evitados) · MobileNetV2 con fotos reales con licencia · mejora propuesta y probada | 4 |

\*Orientativo; puntúa el docente con la rúbrica del curso (0–4 en cada criterio). El mínimo es una entrega válida y evaluable; la «Definition of Done» describe el nivel **estándar**.

## Reparto sugerido de los 105 minutos

| Min | Qué | Se sabe que está hecho cuando… |
|---|---|---|
| 25 (día 1) | Paso 1: elegir las fotos, `contar_por_clase`, mirarlas | Cinco clases contadas y etiquetas dudosas anotadas |
| 25 (día 2) | Paso 2: `modelo_transfer`, ajuste fino y referencia «desde cero» | Tres cifras de validación anotadas |
| 20 | Paso 3: prueba (una vez), matriz, ejercicios 3 y 4, tabla de errores | Matriz interpretada y errores con hipótesis |
| 15 | Paso 4: `clasificar_foto`, ejercicio 5 y umbral | El demostrador responde con 2–3 fotos |
| 20 | Paso 5: informe, README, revisión con la rúbrica y subida | Otra persona podría ejecutarlo con el README |

## Frases para el análisis de errores

- «El modelo acierta un … % en la prueba, pero en la clase … solo un … %. La confunde con … porque …»
- «Foto …: la clasificó como … en vez de …. Creemos que es por … Podríamos mejorarlo con …»
- «Con un umbral de …, el modelo decide solo el … % de las fotos y acierta el … % de ellas; el resto lo revisa una persona.»
- «Las fotos vienen de … con licencia …. Riesgos: … Medida: …»

## Antes de entregar
- **Archivos subidos en `sprint-11/`:** `reto_vision_cliente.ipynb` · `analisis_errores.md` · `README.md` · `autoevaluacion_nombre.md` (**uno por persona**) = 3 + N ficheros
- [ ] Cuaderno con *Reiniciar y ejecutar todo*, semilla fija · [ ] Prueba usada una sola vez · [ ] ≥ 3 *commits* de personas distintas
- [ ] Errores analizados mirando las fotos · [ ] Demostrador con «revisar a mano» · [ ] «Revisión con la rúbrica» en el README
- [ ] [Autoevaluación y coevaluación](../4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md): **una por persona**, subida a `sprint-11/`
