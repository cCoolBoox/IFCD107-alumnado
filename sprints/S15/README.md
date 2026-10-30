# README Sprint S15 · Modelado y experimentos

**Pregunta guía:** ¿qué modelo es el mejor para nuestro problema y cómo lo demostramos sin engañarnos?  
**Fechas:** 1–3/12 · **Horas:** 18 h (1 T · 3 P · 14 PBL) · **Hito:** 3/12 modelo candidato elegido

📄 **Este README en PDF** (para imprimir; descárgalo para que funcionen los enlaces): [a color](pdf/README_Sprint_15.pdf) · [ecofriendly](pdf/README_Sprint_15_ecofriendly.pdf)

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
| ☐ | 🎯 Reto · **Proyecto:** modelo de referencia y primer modelo mejor. Anota todo en el registro de experimentos | [registro de experimentos](3_Reto/4_Plantillas_y_entrega/registro_experimentos_plantilla.csv) | 130 |

**En clase: 3 h 20 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Registro de experimentos con al menos 3 filas.

## Día 2 · Miércoles 2/12

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 🎯 Reto · **Proyecto:** prueba modelos (clásico, red o LLM/RAG, según tu brief) | — | 100 |
| ☐ | 🎯 Reto · Continúa con los experimentos. **Tutoría técnica de 20 min por equipo** (el docente indica tu franja) | — | 100 |

**En clase: 3 h 20 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Registro de experimentos al día.
- [ ] He anotado las dudas para la tutoría.

## Día 3 · Jueves 3/12

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 🎯 Reto · **Comparativa** de modelos y elección del **candidato** | — | 70 |
| ☐ | 🎯 Reto · **Evaluación única en test:** una sola vez, con el candidato elegido | — | 40 |
| ☐ | 🔔 Ceremonia · Entrega en `sprint-15/` de tu repo + autoevaluación y coevaluación | — | 30 |
| ☐ | 🔔 Ceremonia · Review (5 min de demo por equipo) y retro: ¿qué mantenemos?, ¿qué cambiamos? | — | 60 |

**En clase: 3 h 20 min.**

## El reto en pocas palabras

**Qué os pide el cliente.** El cliente (el docente) quiere saber **qué modelo recomendáis y por qué**. No le basta con «el que tiene mejor número». Quiere saber:

**Qué vais a entregar:** el registro de experimentos, el notebook `03_modelos.ipynb`, la justificación de 1 página del candidato, el modelo guardado y una primera explicación (importancia de variables, SHAP o Grad-CAM).

Para trabajar: [reto en una página](3_Reto/1_Reto_en_una_pagina/Reto_Sprint_15_una_pagina.md). Para consultar: [ficha completa del reto](3_Reto/2_Ficha_completa/Reto_Sprint_15.md) (pasos, rúbrica, ayudas y errores frecuentes). Plantillas, datos y autoevaluación: [`3_Reto/4_Plantillas_y_entrega/`](3_Reto/4_Plantillas_y_entrega/).

## ✅ Antes de cerrar el sprint (Definition of Done)

**Archivos subidos en el repositorio del equipo, carpeta `sprint-15/`** (marca cada uno cuando lo veas en GitHub):
- [ ] `registro.csv` · lo creáis a partir de una plantilla
- [ ] `03_modelos.ipynb` · lo creáis
- [ ] `justificacion_candidato.md` · lo creáis
- [ ] `modelo_candidato.joblib` · lo genera el cuaderno
- [ ] `metadatos.json` · lo genera el cuaderno
- [ ] `explicacion_modelo.png` · lo genera el cuaderno
- [ ] `autoevaluacion_nombre.md` · **uno por persona** (la coevaluación va dentro del mismo fichero): [plantilla](3_Reto/4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md)

**Total en `sprint-15/`: 6 ficheros del equipo + 1 hoja por persona** (un equipo de 3 sube 9). Los extras solo si los hacéis. La *review* y la *retro* no se suben.

**Comprobaciones antes de dar el sprint por cerrado:**
- [ ] Baseline + ≥ 3 modelos + 1 neuronal comparados con la misma partición, sin fuga.
- [ ] `experimentos/registro.csv` con al menos una fila por persona.
- [ ] Semilla fija; el notebook se ejecuta de arriba abajo.
- [ ] Modelo candidato elegido y justificado; test evaluado una sola vez.
- [ ] Roles rotados, tablero actualizado y retro con acción concreta.
- [ ] Alguien que **no escribió esa parte** ha revisado el entregable con la [rúbrica](3_Reto/2_Ficha_completa/Reto_Sprint_15.md#rúbrica-del-reto--cómo-se-puntúa-y-cómo-se-revisa) y lo ha anotado en el propio entregable

## En casa (cuando puedas)

- Los ejercicios de cada cuaderno que **no** se hacen en clase. Se autocorrigen, y debajo llevan una «Solución de referencia» plegada por si te quedas atascado.
- Si quieres repasar la teoría con calma: [apuntes del sprint](1_Teoria/apuntes/apuntes_experimentos_y_reproducibilidad.md).

## Si te atascas

1. Lee primero la parte «Si os atascáis» de la [ficha completa del reto](3_Reto/2_Ficha_completa/Reto_Sprint_15.md).
2. Mira el [código explicado]() del cuaderno en el que estás.
3. Pregunta a tu equipo y, después, al docente. Si usas IA, cuenta en el README qué te dijo y qué comprobaste.

## Todo el material, por carpetas

Las carpetas están **numeradas en el orden en que las usas**. Cada documento está en `.md`; sus PDF (color y ecofriendly) están en la subcarpeta `pdf/`.

| Carpeta | Qué hay |
|---|---|
| [`1_Teoria/`](1_Teoria/) | Las presentaciones del sprint y los apuntes para repasar |
| [`2_Practica/`](2_Practica/) | Los cuadernos (Colab) y su explicación línea a línea en `codigo_explicado/` |
| [`3_Reto/`](3_Reto/) | `1_Reto_en_una_pagina` · `2_Ficha_completa` · `3_Laminas` · `4_Plantillas_y_entrega` |
| [`4_Referencia/`](4_Referencia/) | Infografías del sprint |

Cómo se trabaja un reto, en todos los sprints: [método de trabajo](../../material/4.%20Como_se_trabaja_un_reto.md).

## Temario oficial de este sprint

| Unidad | Conceptos que entran |
|---|---|
| M9 · Modelado y experimentos | modelado y experimentos |

**Y ahora:** Sprint 16 · Evaluación, IA responsable y entrega (viernes 4/12).

*.*
