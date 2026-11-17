# Autoevaluación y coevaluación · «Conocer al huésped»

> Hoja de **ejemplo** de una persona (Marta) del equipo de referencia. Cada persona sube la suya con su nombre.

## 1. Autoevaluación

**Nombre:** Marta

**Repaso rápido:**

| Pregunta | Mi respuesta |
|---|---|
| ¿El cuaderno se ejecuta de arriba abajo, con semillas fijas? | Sí: `SEMILLA = 42` y probado con «Reiniciar y ejecutar todo» |
| ¿Hemos escalado antes de agrupar y justificado `k` con silueta **y** con negocio? | Sí: silueta 0,431 con k = 4 y el grupo más pequeño es el 16 % |
| ¿El mapa PCA tiene segmentos coloreados y el % de varianza en los ejes? | Sí: 43 % y 26 % |
| ¿La ficha tiene nombre, tamaño, perfil y acción por segmento? | Sí, y los tamaños suman 1.200 |
| ¿El recomendador está evaluado con RMSE y precision@3 y comparado con la popularidad? | Sí: item-item gana en las dos medidas |
| ¿`recomendar` no propone experiencias ya valoradas? | Sí: probada con 3 usuarios, conjunto vacío en los tres |
| ¿Hay al menos dos riesgos específicos de IA responsable? | Sí: discriminación por edad o niños y sesgo de popularidad, este último medido |
| ¿Cada persona ha hecho *commit* de su parte? | Sí: A el cuaderno, B el mapa y los perfiles, C la ficha |

**Puntúate de 1 a 4:**

| Criterio | Mi puntuación (1–4) | Por qué (una frase) | Qué haría para subir un punto |
|---|---|---|---|
| Corrección técnica | 3 | Todo lo estándar está hecho y la evaluación usa valoraciones escondidas | Comparar con jerárquico o DBSCAN para el nivel extra |
| Reproducibilidad | 3 | Otra persona obtuvo el mismo k, tamaños y tabla | Añadir arriba del cuaderno cómo ejecutarlo y las versiones (ya están al final) |
| Análisis y comunicación al cliente | 3 | Cada nombre tiene dos cifras y cada segmento una acción | Priorizar los segmentos por valor para Lucía |
| IA responsable | 3 | Dos riesgos con medida y uno comprobado con datos | Probar la medida del hueco para una experiencia menos conocida |

- **Lo que más me costó fue** entender por qué el número de grupo cambia de un ordenador a otro, **porque** los nombres tenían que ponerse mirando el perfil y no copiando la numeración.
- **He usado IA para** entender qué mide la silueta y proponer nombres, **y lo que he comprobado a mano es** que cada nombre cuadra con dos cifras del perfil y que las cifras de la ficha son las del último «Reiniciar y ejecutar todo».

---

## 2. Coevaluación

**Trabajo revisado de (persona o equipo):** equipo «Los Roques» (ejemplo)  **Revisado por (yo):** Marta

| Entregable | ¿Está y se entiende? | Comentario breve |
|---|---|---|
| `ficha_segmentos.md` | ✔ | Tiene nombre, tamaño y acción en los cuatro segmentos |
| Mapa PCA | ✘ | Los ejes no dicen el % de varianza |
| `reto_S09_conocer_al_huesped.ipynb` | ✔ | Se ejecuta entero; falta probar `recomendar` con un tercer usuario |

| Criterio | Puntuación | Comentario breve |
|---|---|---|
| Corrección técnica | 2 | Cumple el mínimo; sin evaluar el recomendador con valoraciones escondidas |
| Reproducibilidad | 2 | Se ejecuta, pero sin semilla fija en el recomendador |
| Análisis y comunicación al cliente | 2 | Hay nombres y acciones, pero los nombres no llevan cifras |
| IA responsable | 1 | Dice que se usó IA, pero no nombra ningún riesgo de este caso |

- **Lo que está muy bien:** los nombres comerciales son claros y las acciones se pueden aplicar mañana.
- **Lo que yo cambiaría, y por qué:** añadiría el % de varianza en los ejes del mapa, porque sin él no se sabe cuánto de los datos se está viendo.

> Se valora el **trabajo**, no a la persona.
