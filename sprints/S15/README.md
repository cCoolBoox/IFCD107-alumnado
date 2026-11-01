# README Sprint S15 · Modelado y experimentos

**Pregunta guía:** ¿qué modelo es el mejor para nuestro problema y cómo lo demostramos sin engañarnos?  
**Fechas:** 1–3/12 · **Horas:** 18 h (1 T · 3 P · 14 PBL) · **Hito:** 3/12 modelo candidato elegido

📄 **Para imprimir:** todos los documentos del sprint en PDF, a color y ecofriendly, están juntos en la carpeta [`pdf/`](pdf/) (descárgalos para que funcionen los enlaces).

> **Sigue el orden de arriba abajo y abre solo lo que pone en cada fila.** Los demás documentos del sprint son para consultar si te atascas (apartado «Si te atascas»). Si el tiempo aprieta, haz solo los ejercicios marcados «en clase»: el resto es para casa.

## Qué aprenderás

1. **Comparar modelos con rigor:** baseline, ≥ 3 modelos, validación cruzada y test reservado (R3).
2. **Registrar experimentos** para que cualquiera pueda reproducirlos: semillas, versiones, hiperparámetros y métricas.
3. **Detectar y evitar la fuga de datos**, especialmente en series y en imágenes del mismo objeto.
4. Integrar **al menos un modelo neuronal** (o LLM/RAG en el brief 3) y justificar si vale la pena (R4).
5. **Elegir el modelo candidato** con criterios de rendimiento, coste, simplicidad y explicabilidad.

## Día 1 · Martes 1/12

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 📖 Teoría · **Píldora: seguimiento de experimentos** | [Presentación S15.1](1_Teoria/S15.1_Pildora_seguimiento_de_experimentos.pdf) | 20 |
| ☐ | 💻 Práctica · Práctica de seguimiento de experimentos | [Cuaderno S15_01](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S15/2_Practica/S15_01_seguimiento_experimentos.ipynb) | 50 |
| ☐ | 🎯 Reto · **Proyecto:** modelo de referencia y primer modelo mejor. Anota todo en el registro de experimentos | [registro de experimentos](3_Reto/1_Trabajar/plantillas/registro_experimentos_plantilla.csv) | 130 |
| ☐ | 🎯 Reto · **Subid de nivel:** más experimentos con otra semilla o una mejora razonada; el registro sigue limpio y completo | — | 50 |

**En clase: 4 h 10 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Registro de experimentos con al menos 3 filas.

## Día 2 · Miércoles 2/12

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 🎯 Reto · **Proyecto:** prueba modelos (clásico, red o LLM/RAG, según tu brief) | — | 100 |
| ☐ | 🎯 Reto · Continúa con los experimentos. **Tutoría técnica de 20 min por equipo** (el docente indica tu franja) | — | 100 |
| ☐ | 🎯 Reto · **Subid de nivel:** ampliad la comprobación de fugas y dejad el registro sin columnas vacías ni nombres repetidos | — | 50 |

**En clase: 4 h 10 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Registro de experimentos al día.
- [ ] He anotado las dudas para la tutoría.

## Día 3 · Jueves 3/12

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 🎯 Reto · **Comparativa** de modelos y elección del **candidato** | — | 70 |
| ☐ | 🎯 Reto · **Subid de nivel:** ampliad la comparativa sin tocar el test (media ± desviación, coste y complejidad) y escribid la justificación del candidato | — | 50 |
| ☐ | 🎯 Reto · **Evaluación única en test:** una sola vez, con el candidato elegido | — | 40 |
| ☐ | 🔔 Ceremonia · Entrega en `sprint-15/` de tu repo + autoevaluación y coevaluación | — | 30 |
| ☐ | 🔔 Ceremonia · Review (5 min de demo por equipo) y retro: ¿qué mantenemos?, ¿qué cambiamos? | — | 60 |

**En clase: 4 h 10 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Sé comparar varios modelos con la misma partición y validación cruzada, sin fuga de datos.
- [ ] Sé registrar mis experimentos para que otra persona los reproduzca.
- [ ] Sé elegir un modelo candidato justificando rendimiento, coste y explicabilidad.

## El reto en pocas palabras

**Qué os pide el cliente.** El cliente (el docente) quiere saber **qué modelo recomendáis y por qué**. No le basta con «el que tiene mejor número». Quiere saber:

- si **la mejora frente al baseline justifica el coste y la complejidad**,
- si el modelo **generaliza** (funciona con datos que no ha visto),
- y que vuestros resultados **se pueden repetir**.

**Qué vais a entregar:** el registro de experimentos, el notebook `03_modelos.ipynb`, la justificación de 1 página del candidato, el modelo guardado y una primera explicación (importancia de variables, SHAP o Grad-CAM).

Para trabajar: [reto en una página](3_Reto/1_Trabajar/Reto_Sprint_15_una_pagina.md). Para entregar: [qué se sube y rúbrica](3_Reto/2_Entregar/entrega_y_rubrica.md). Para consultar: [ficha del reto](3_Reto/3_Consultar/Reto_Sprint_15.md) (qué pide el cliente, ayudas y errores frecuentes) y [cada paso explicado](3_Reto/3_Consultar/).

## ✅ Antes de cerrar el sprint (Definition of Done)

**Archivos subidos en el repositorio del equipo, carpeta `sprint-15/`** (marca cada uno cuando lo veas en GitHub):
- [ ] `registro.csv` · lo creáis a partir de una plantilla
- [ ] `03_modelos.ipynb` · lo creáis
- [ ] `justificacion_candidato.md` · lo creáis
- [ ] `modelo_candidato.joblib` · lo genera el cuaderno
- [ ] `metadatos.json` · lo genera el cuaderno
- [ ] `explicacion_modelo.png` · lo genera el cuaderno
- [ ] `autoevaluacion_nombre.md` · **uno por persona** (la coevaluación va dentro del mismo fichero): [plantilla](3_Reto/2_Entregar/autoevaluacion_y_coevaluacion.md)

**Total en `sprint-15/`: 6 ficheros del equipo + 1 hoja por persona** (un equipo de 3 sube 9). Los extras solo si los hacéis. La *review* y la *retro* no se suben.

**Comprobaciones antes de dar el sprint por cerrado:**
- [ ] Baseline + ≥ 3 modelos + 1 neuronal comparados con la misma partición, sin fuga.
- [ ] `experimentos/registro.csv` con al menos una fila por persona.
- [ ] Semilla fija; el notebook se ejecuta de arriba abajo.
- [ ] Modelo candidato elegido y justificado; test evaluado una sola vez.
- [ ] Roles rotados, tablero actualizado y retro con acción concreta.
- [ ] Alguien que **no escribió esa parte** ha revisado el entregable con la [rúbrica](3_Reto/2_Entregar/entrega_y_rubrica.md) y lo ha anotado en el propio entregable

## En casa (cuando puedas)

- Los ejercicios de cada cuaderno que **no** se hacen en clase. Se autocorrigen, y debajo llevan una «Solución de referencia» plegada por si te quedas atascado.
- Si quieres repasar la teoría con calma: [apuntes del sprint](1_Teoria/apuntes/apuntes_experimentos_y_reproducibilidad.md).

## Si te atascas

1. Lee primero la parte «Si os atascáis» de la [ficha completa del reto](3_Reto/3_Consultar/Reto_Sprint_15.md).
2. Mira el [código explicado]() del cuaderno en el que estás.
3. Pregunta a tu equipo y, después, al docente. Si usas IA, cuenta en el README qué te dijo y qué comprobaste.

## Todo el material, por carpetas

Las carpetas están **numeradas en el orden en que las usas**. Cada documento está en `.md`.

| Carpeta | Qué hay |
|---|---|
| [`1_Teoria/`](1_Teoria/) | Las presentaciones del sprint y los apuntes para repasar |
| [`2_Practica/`](2_Practica/) | Los cuadernos (Colab) y su explicación línea a línea en `codigo_explicado/` |
| [`3_Reto/`](3_Reto/) | `1_Trabajar` (reto en una página, plantillas y datos) · `2_Entregar` (qué se sube, rúbrica y autoevaluación) · `3_Consultar` (ficha del reto y cada paso explicado) |
| [`4_Referencia/`](4_Referencia/) | Infografías del sprint |

Cómo se trabaja un reto, en todos los sprints: [método de trabajo](../../material/4.%20Como_se_trabaja_un_reto.md).

## Temario oficial de este sprint

| Unidad | Conceptos que entran |
|---|---|
| M9 · Modelado y experimentos | modelado y experimentos |

**Y ahora:** Sprint 16 · Evaluación, IA responsable y entrega (viernes 4/12).

*.*
