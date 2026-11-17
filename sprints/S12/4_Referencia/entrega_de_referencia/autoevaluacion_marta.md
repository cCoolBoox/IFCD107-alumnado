# Autoevaluación y coevaluación · «Escuchar al cliente»

> Hoja de **ejemplo** de una persona (Marta) del equipo de referencia. Cada persona sube la suya con su nombre.

## 1. Autoevaluación

**Nombre:** Marta

**Repaso rápido:**

| Pregunta | Mi respuesta |
|---|---|
| ¿La serie se parte por fecha y hay baseline en la tabla de resultados? | Sí: entrenamiento hasta el 1/10/2025, prueba los últimos 91 días, y los tres *baselines* están en la misma tabla |
| ¿Escalado y vectorización se ajustan solo con entrenamiento? | Sí: el TF-IDF va dentro del `pipeline` y el escalado de la GRU usa solo el entrenamiento |
| ¿El sentimiento se evalúa en prueba y los temas tienen ejemplos reales? | Sí: exactitud y matriz en prueba; tres temas criticados y tres valorados con su ejemplo |
| ¿El asistente cita la fuente y responde «No consta…» a la pregunta sin respuesta? | Sí, a la del gimnasio y a la de la lavandería |
| ¿La evaluación tiene aciertos, sin fuente y alucinaciones sobre 20 + 5 preguntas? | Sí: 24 aciertos, 0 sin fuente, 0 alucinaciones y 1 fallo de recuperación (25 en total) |
| ¿Probamos 3 ataques y describimos el resultado? | Sí, de tres tipos, con y sin filtro |
| ¿Hemos comprobado que no hay ninguna clave en el código ni en el repositorio? | Sí: ninguna; el generador es un simulador |
| ¿Informe de 2 páginas con 3 recomendaciones y límites? | Sí |
| ¿Todo se ejecuta de arriba abajo, sin errores y sin internet? | Sí, con la carpeta de datos presente |
| ¿La nota de IA responsable está entregada? | Sí, con cifras y con lo que no cubre |

**Puntúate de 1 a 4:**

| Criterio | Mi puntuación (1–4) | Por qué (una frase) | Qué haría para subir un punto |
|---|---|---|---|
| Corrección técnica | 4 | Hay modelo frente al *baseline*, sentimiento evaluado, 25 preguntas y 3 ataques, y dos alternativas comparadas con números | Está en el máximo; lo siguiente sería un modelo de lenguaje real |
| Reproducibilidad | 3 | Otra persona obtuvo los mismos números siguiendo el LEEME | Fijar las versiones también en Colab para llegar al 4 |
| Análisis y comunicación al cliente | 4 | Cada recomendación se apoya en una cifra del informe | Está en el máximo; añadiría el coste en euros de un mal turno |
| IA responsable | 4 | Las medidas se miden y la nota dice qué no cubre | Está en el máximo; repetiría los ataques con otras formulaciones |

- **Lo que más me costó fue** que el asistente contestase «lavandería» con la política de traslados, **porque** solo compartían la palabra «servicio» y el umbral no la frenaba.
- **He usado IA para** entender SARIMAX y redactar el filtro, **y lo que he comprobado a mano es** que cada cifra sale de la última ejecución de los cuadernos y que el umbral de 0,5 que sugirió solo daba 14 aciertos de 25.

---

## 2. Coevaluación

**Trabajo revisado de (persona o equipo):** equipo «Los Roques» (ejemplo)  **Revisado por (yo):** Marta

| Entregable | ¿Está y se entiende? | Comentario breve |
|---|---|---|
| `informe_resenas.md` | ✔ | Las tres recomendaciones se entienden sin programar y dicen quién las hace |
| `asistente_rag.ipynb` | ✘ | Sin umbral: a «¿Tienen gimnasio?» contesta con un fragmento cualquiera |
| `nota_ia_responsable.md` | ✘ | Nombra riesgos, pero no dice qué medida se aplica ni la mide |

| Criterio | Puntuación | Comentario breve |
|---|---|---|
| Corrección técnica | 2 | Hay *baseline* y asistente que cita, pero no responde «No consta…» |
| Reproducibilidad | 2 | El LEEME no dice las versiones ni el orden de los cuadernos |
| Análisis y comunicación al cliente | 3 | Informe claro con tres recomendaciones; falta decir que los datos son sintéticos |
| IA responsable | 1 | La nota no nombra ningún riesgo concreto del reto |

- **Lo que está muy bien:** el informe empieza por lo que hay que hacer y cada recomendación dice cómo sabremos que funciona.
- **Lo que yo cambiaría, y por qué:** pondría un umbral al asistente y probaría la pregunta del gimnasio, porque un asistente que contesta lo que no sabe es peor que uno que dice «No consta».

> Se valora el **trabajo**, no a la persona.
