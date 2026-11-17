# Autoevaluación y coevaluación · «¿Vale la pena la red?»

> Hoja de **ejemplo** de una persona (Marta) del equipo de referencia. Cada persona sube la suya con su nombre.

## 1. Autoevaluación

**Nombre:** Marta

**Repaso rápido:**

| Pregunta | Mi respuesta |
|---|---|
| ¿El cuaderno se ejecuta de arriba abajo, con semillas fijas y los cuatro ejercicios pasan? | Sí: probado con «Reiniciar y ejecutar todo» |
| ¿Hay una sola partición, igual para todos los modelos, y el escalador se ajusta solo con entrenamiento? | Sí: 64 / 16 / 20 %, el escalador está dentro del preprocesado ajustado con entrenamiento |
| ¿Referencia y MLP se miden con las mismas métricas y como máximo 40 épocas? | Sí: AUC, AP, F1 y exactitud; 40 épocas con parada temprana |
| ¿Hay curva de aprendizaje y una frase de diagnóstico? | Sí: tres curvas y el diagnóstico en el informe |
| ¿La prueba se mira una sola vez? | Sí, solo en la sección 6 |
| ¿Hay 2–3 variantes elegidas con la validación y una comparación con incertidumbre? | Sí: dos variantes más la base, y *bootstrap* de la diferencia de AUC |
| ¿El informe tiene la recomendación en la primera frase, el coste y al menos dos riesgos? | Sí, con un riesgo medido por canal |
| ¿Cada persona ha hecho *commit* de su parte? | Sí |

**Puntúate de 1 a 4:**

| Criterio | Mi puntuación (1–4) | Por qué (una frase) | Qué haría para subir un punto |
|---|---|---|---|
| Corrección técnica | 3 | Todo lo estándar está hecho y la prueba se usó una vez | Probar más capacidad y la variante de precios para el nivel extra |
| Reproducibilidad | 3 | Otra persona obtuvo el mismo AUC de validación siguiendo el README | Guardar el MLP y probarlo recargado |
| Análisis y comunicación al cliente | 3 | La recomendación y el intervalo están en la primera frase | Pasar el coste del umbral a euros |
| IA responsable | 3 | Dos riesgos con medida y el del canal está medido | Medir también el aviso por país |

- **Lo que más me costó fue** entender que «la red no gana» no significa «la red es peor», **porque** el intervalo incluye el 0 y la diferencia puede ser ruido.
- **He usado IA para** entender el *bootstrap* y revisar la redacción, **y lo que he comprobado a mano es** que las cifras del informe son las de la celda «Cifras para el informe» del último «Reiniciar y ejecutar todo».

---

## 2. Coevaluación

**Trabajo revisado de (persona o equipo):** equipo «Los Roques» (ejemplo)  **Revisado por (yo):** Marta

| Entregable | ¿Está y se entiende? | Comentario breve |
|---|---|---|
| `informe_comparativo.md` | ✔ | La recomendación está al principio con una cifra |
| `reto_vale_la_pena.ipynb` | ✘ | El escalador se ajusta con todos los datos, no solo con entrenamiento |
| `README.md` | ✔ | Dice quién hizo qué y cómo repetirlo; faltan las versiones |

| Criterio | Puntuación | Comentario breve |
|---|---|---|
| Corrección técnica | 1 | Hay fuga: el escalador ve la validación y la prueba |
| Reproducibilidad | 2 | Se ejecuta, pero sin semillas fijas |
| Análisis y comunicación al cliente | 2 | Dicen que la red gana por 0,004 de AUC sin intervalo |
| IA responsable | 2 | Riesgos genéricos, sin medida |

- **Lo que está muy bien:** la tabla del informe es clara y el coste está explicado en una línea.
- **Lo que yo cambiaría, y por qué:** ajustaría el escalador solo con el entrenamiento, porque si no la validación y la prueba ya no son un examen limpio.

> Se valora el **trabajo**, no a la persona.
