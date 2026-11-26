# 🚀 El proyecto final, explicado fácil

**Del 26 de noviembre al 14 de diciembre.** Un solo proyecto de IA, en equipo, de principio a fin. Aquí tenéis qué es, qué haréis cada día y **cuándo tenéis que decidir qué hacer y cómo**.

> Versión completa con requisitos y rúbrica: [`briefs_y_rubrica.md`](briefs_y_rubrica.md). Presentación de un vistazo: [`S14_proyecto_presentacion…pdf`](../sprints/S14/1_Teoria/S14_proyecto_presentacion_El_proyecto_final_de_principio_a_fin.pdf).

---

## 1 · En qué consiste

- **Sois una consultora** de 3–4 personas. **El docente es el cliente**: no es técnico y solo quiere saber si vuestro trabajo le sirve para decidir algo.
- **Elegís un encargo (brief)** y lo resolvéis con datos reales:
  - 1 · Demanda turística (series temporales)
  - 2 · Salud de cultivos (imágenes)
  - 3 · Asistente de FP (texto, con RAG)
  - 4 · Demanda eléctrica (series temporales)
  - O un **brief libre**, con ficha antes de las 14:30 del 26/11.
- **Hasta ahora** cada reto traía un guion. **Ahora decidís vosotros**: la pregunta, los datos y el alcance.
- **Al final** defendéis el proyecto ante un cliente que no es técnico.

## 2 · Las cuatro etapas

| Sprint | Fechas | Qué hacéis | Qué queda al final |
|---|---|---|---|
| **14** · Formular | 26–30/11 | Decidir el problema, buscar datos, medir un primer baseline | Ficha, datos con licencia, EDA, baseline, backlog y plan ético |
| **15** · Modelar | 1–3/12 | Probar modelos y compararlos con rigor | Al menos 3 modelos, registro de experimentos y un modelo candidato |
| **16** · Evaluar y entregar | 4–10/12 | Medir sesgos, hacer el demostrador, escribir la memoria | Demostrador, memoria de 10–15 páginas y repositorio reproducible |
| **17** · Contar | 11 y 14/12 | Preparar el relato y ensayarlo | Presentación de 12 diapositivas como máximo y defensa |

**Palabras que saldrán:**

- **Baseline:** el método más simple posible; hay que ganarle para que el modelo valga la pena.
- **EDA:** mirar los datos antes de modelar.
- **Backlog:** lista ordenada de tareas del equipo.
- **Go / no-go:** respuesta del docente a vuestra ficha: «adelante» o «corregid esto».

---

## 3 · Qué haremos cada día

### Sprint 14 · Formular

- **Jueves 26/11**
  - Taller de Design Thinking: del problema al brief.
  - **Elegir brief antes del descanso.**
  - Buscar y validar datos: fuente, licencia y tamaño.
  - **Ficha del proyecto antes de las 14:30**, en la carpeta `sprint-14/` de vuestro repositorio.
- **Viernes 27/11**
  - Leer el **go / no-go** del docente y corregir la ficha si hace falta.
  - EDA, calidad del dato y **primer baseline**.
- **Lunes 30/11**
  - Backlog y reparto en sprints, riesgos éticos y README del repositorio.
  - Entrega en `sprint-14/`, autoevaluación y coevaluación, review (5 min por equipo) y retrospectiva.

### Sprint 15 · Modelar

- **Martes 1/12**
  - Seguimiento de experimentos: un registro donde anotáis cada prueba.
  - Modelo de referencia y primer modelo mejor.
- **Miércoles 2/12**
  - Probar modelos (clásico, red neuronal o LLM/RAG, según vuestro brief).
  - **Tutoría técnica** de 20 min por equipo.
- **Jueves 3/12**
  - Comparativa y **elección del modelo candidato**.
  - **Evaluación única en test**, una sola vez.
  - Entrega en `sprint-15/`, review y retro.

### Sprint 16 · Evaluar y entregar

*No hay clase el 7 ni el 8 de diciembre: dejad el trabajo repartido antes.*

- **Viernes 4/12**
  - Planning del sprint.
  - Demostrador y documentación; **tutoría de sesgos**.
  - Esqueleto de la **memoria** y *model card* (ficha del modelo).
- **Miércoles 9/12**
  - **Mitigar sesgos** y volver a medir.
  - Pulir el demostrador y avanzar la memoria y la *model card*.
- **Jueves 10/12**
  - Clonar el repositorio en un Colab nuevo y comprobar que todo se ejecuta.
  - **Vídeo de reserva** de la demo, por si falla internet el día de la defensa.
  - 🔒 **Congelación a las 14:30:** último *push*. Lo que no esté subido, no cuenta.

### Sprint 17 · Contar

- **Viernes 11/12**
  - Storytelling: estructura del relato y **pitch de 3 minutos**.
  - Ensayos con cronómetro y con preguntas de otro equipo; **ensayo general**.
- **Lunes 14/12**
  - **PDF de la presentación en el repositorio antes de las 8:30.**
  - **Defensa** ante el tribunal. Hablan **todas las personas** del equipo.

---

## 4 · Cuándo tenéis que decidir (y cómo)

| Cuándo | Qué decidís | Cómo decidirlo |
|---|---|---|
| **Jue 26/11, antes del descanso** | **El brief** | Cada persona puntúa de 1 a 5, en silencio: **datos accesibles hoy**, **interés** y **tiempo**. Se suman los puntos por brief. |
| **Jue 26/11, antes de las 14:30** | **La pregunta, los datos, la métrica, el baseline y los modelos previstos** (todo en la ficha) | Una frase: ¿Podemos… para que…? Con datos **reales y con licencia** ya localizados; una métrica de negocio y otra técnica; el baseline antes de ver resultados. |
| **Vie 27/11** | **Corregir o seguir** | Si el docente dice *no-go*, se arregla lo que pide. Si dice *go*, esa ficha es el plan. **Después del 27/11 los cambios grandes se negocian en la review.** |
| **Lun 30/11** | **Qué historias entran en cada sprint** y **quién hace qué** | Backlog de 10–15 historias; un objetivo por sprint; cuatro roles que rotan (Scrum Master, técnico, datos e IA responsable). |
| **Mar 1/12 – Mié 2/12** | **Qué modelos probáis** | Según el brief: clásico, red neuronal o LLM/RAG. Mínimo **3 modelos** y al menos **una red** (o LLM/RAG en el brief 3). |
| **Jue 3/12** | **El modelo candidato** | Se elige con la **validación**, no con el test. Pregunta clave: ¿la mejora frente al baseline compensa la complejidad? El **test se mira una sola vez**. |
| **Mié 9/12** | **Qué medidas tomáis contra los sesgos** | Medid por subgrupos, mitigad lo que podáis y **volved a medir**. Anotad qué queda sin resolver. |
| **Vie 11/12** | **El mensaje único de la defensa** | Cuatro respuestas para el cliente: qué problema, qué habéis encontrado, qué recomendáis y **de qué no debe fiarse**. |

**Regla para decidir en cualquier momento:**

- **Primero el cliente:** ¿qué decisión suya mejora esto?
- **Siempre un rival simple:** ¿le ganamos a un método sencillo?
- **Test una sola vez:** elegid con la validación.
- **Contad vuestros límites,** con cifra.

---

## 5 · Cómo se trabaja

- **Cada sprint:** planning (repartir tareas) → trabajo con tablero → review (5 min de demo por equipo) → retrospectiva (¿qué mantenemos?, ¿qué cambiamos?).
- **Cada día:** unos 50 minutos de **«subid de nivel»**: mejorad el criterio más flojo de la rúbrica.
- **Cada entrega:** en la carpeta `sprint-NN/` de vuestro repositorio, con autoevaluación y coevaluación.
- **Repositorio:** **commits de todas las personas**. Lo que no está en el repositorio no existe para la evaluación.

## 6 · Cómo se evalúa (en resumen)

- **100 puntos.** Los pesos mayores: **modelado (20)** y **defensa (15)**; la memoria vale 5.
- **Para ser Apto:** nota de **50 o más**; modelado e IA responsable al menos en «Suficiente»; presentar y responder a una pregunta individual; contribución verificable.
- **Nota individual:** la del equipo se ajusta entre **0,8 y 1,1** según la coevaluación y vuestros commits.

## 7 · Lo que suele fallar

- **S14:** querer «hacer algo con IA» sin una decisión detrás; buscar los datos tarde.
- **S15:** fugas de datos; mirar el test para elegir el modelo.
- **S16:** dejar la memoria para el último día; no probar el repositorio desde cero.
- **S17:** contar la técnica en vez de la decisión.

## ✅ Hoy, jueves 26/11

- [ ] Elegir brief **antes del descanso**.
- [ ] Buscar y validar los datos (fuente, licencia, tamaño).
- [ ] Entregar la **ficha del proyecto antes de las 14:30**.
