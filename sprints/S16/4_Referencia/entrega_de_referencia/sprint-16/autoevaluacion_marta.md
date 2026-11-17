# Autoevaluación y coevaluación · «Entrega final: evaluar, demostrar y documentar» (Sprint 16)

> Hoja de **ejemplo** de una persona (Marta) del equipo de referencia. Cada persona sube la suya con su nombre.

## 1. Autoevaluación

**Nombre:** Marta

**Repaso rápido:**

| Pregunta | Mi respuesta |
|---|---|
| ¿La evaluación en test se hizo una sola vez, con gráficos y análisis de errores? | Sí: una vez, con intervalos, 4 gráficos y los 10 peores días |
| ¿Hay rendimiento por subgrupos y una mitigación aplicada **y medida**? | Sí: 8 subgrupos y tres mitigaciones medidas antes y después; solo se adoptó una (intervalos por franja) |
| ¿El registro de riesgos está cerrado y hay clasificación RGPD / AI Act justificada? | Sí: 9 riesgos con estado y evidencia; dos quedan abiertos para un despliegue real |
| ¿El demostrador funciona desde cero, gestiona entradas erróneas y avisa de la incertidumbre? | Sí: lo lancé en una carpeta limpia y probé una fecha imposible y una vacía |
| ¿Hay pruebas (`pytest -q`) y vídeo plan B? | Pruebas sí (10); el vídeo lo grabamos aparte, no está en esta copia |
| ¿`requirements.txt` con versiones y README probado por otra persona del equipo? | Sí: Persona C lo probó con un entorno nuevo |
| ¿Model card y memoria (10–15 páginas) en PDF dentro de `docs/`? | Sí: la *model card* ocupa 2 páginas y la memoria entra en el rango |
| ¿Etiqueta `v1.0-entrega` creada antes de las 14:30? | La creamos justo tras la revisión, antes de la hora |
| ¿Cada integrante ha entregado su coevaluación? | Sí, la mía va al docente |

**Puntúate de 1 a 4:**

| Criterio | Mi puntuación (1–4) | Por qué (una frase) | Qué haría para subir un punto |
|---|---|---|---|
| Corrección técnica | 4 | Elegimos la mitigación con validación cruzada y solo medimos en el test el antes y el después | Está en el máximo |
| Reproducibilidad | 4 | Una persona lo repitió en una carpeta limpia y encontró un aviso que corregimos | Está en el máximo |
| Análisis y comunicación al cliente | 3 | El resumen ejecutivo funciona, pero no sé traducir la mejora a euros porque no tenemos el coste real de una bici mal colocada | Pedir ese coste al cliente y calcular el ahorro |
| IA responsable | 4 | Contamos una mitigación que empeoró y dos riesgos que siguen abiertos | Está en el máximo |

- **Lo que más me costó fue** aceptar que la mitigación no mejoraba el modelo, **porque** esperaba que reponderar la hora punta lo arreglara y la validación cruzada dijo que empeoraba el conjunto.
- **He usado IA para** el código de los gráficos y del esqueleto del demostrador, **y lo que he comprobado a mano es** que el rango agrupado solo en «punta / resto» dejaba el fin de semana infracubierto y que un título de gráfico presumía de una mejora que no ocurre a las 4 h.

---

## 2. Coevaluación

**Trabajo revisado de (persona o equipo):** equipo «Los Roques» (ejemplo)  **Revisado por (yo):** Marta

| Entregable | ¿Está y se entiende? | Comentario breve |
|---|---|---|
| `04_evaluacion.ipynb` | ✔ | Evalúa una sola vez y da los subgrupos, pero no dice cómo eligió la mitigación |
| `demostrador/` | ✘ | Se rompe si la fecha está vacía y no avisa de la incertidumbre |
| `docs/model_card.md` | ✔ | Completa; las cifras no coinciden con las de la memoria |

| Criterio | Puntuación | Comentario breve |
|---|---|---|
| Corrección técnica | 2 | Eligen la mitigación mirando el test |
| Reproducibilidad | 3 | El README funciona, pero no dice la versión de Python |
| Análisis y comunicación al cliente | 2 | Cifras distintas entre documentos |
| IA responsable | 2 | No explican qué revisaron de lo que generó la IA |

- **Lo que está muy bien:** el demostrador es sencillo y el rango se entiende de un vistazo.
- **Lo que yo cambiaría, y por qué:** elegiría la mitigación con validación cruzada del entrenamiento, no con el test, porque si no el test deja de ser una prueba limpia.

> Se valora el **trabajo**, no a la persona.
