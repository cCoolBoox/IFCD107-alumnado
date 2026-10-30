# README Sprint S16 · Evaluación, IA responsable y entrega

**Pregunta guía:** ¿es nuestro modelo lo bastante bueno, justo y seguro para entregarlo, y puede otra persona reproducirlo?  
**Fechas:** 4–10/12 (clases 4, 9 y 10/12; no hay clase el 7 y el 8) · **Horas:** 18 h (1 T · 3 P · 14 PBL)

📄 **Este README en PDF** (para imprimir; descárgalo para que funcionen los enlaces): [a color](pdf/README_Sprint_16.pdf) · [ecofriendly](pdf/README_Sprint_16_ecofriendly.pdf)

> **Sigue el orden de arriba abajo y abre solo lo que pone en cada fila.** Los demás documentos del sprint son para consultar si te atascas (apartado «Si te atascas»). Si el tiempo aprieta, haz solo los ejercicios marcados «en clase»: el resto es para casa.

## Qué aprenderás

1. **Evaluar a fondo el modelo candidato:** métricas adecuadas, análisis de errores y visualizaciones (curvas, matriz de confusión, importancia, SHAP o Grad-CAM) que comunican incertidumbre (R5).
2. **Analizar sesgos y limitaciones** por subgrupos y **aplicar y medir medidas de mitigación** (R6).
3. **Clasificar el riesgo** del sistema (RGPD y AI Act) y cerrar el registro de riesgos.
4. **Construir un demostrador ejecutable** con validación de entradas, aviso de incertidumbre y plan B (R7).
5. **Documentar:** model card, README reproducible y **memoria técnica de 10-15 páginas** (R8, R10).

## Día 1 · Viernes 4/12

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 🔔 Ceremonia · **Planning del Sprint 16:** lee el README del Sprint 16 y reparte tareas | [README del Sprint 16](README.md) | 10 |
| ☐ | 📖 Teoría · **Despliegue y documentación** | [Presentación S16.1](1_Teoria/S16.1_Pildora_demostrador_y_documentacion.pdf) | 20 |
| ☐ | 💻 Práctica · Práctica del demostrador | [Cuaderno S16_01](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S16/2_Practica/S16_01_demostrador.ipynb) | 45 |
| ☐ | 🎯 Reto · **Tutoría de sesgos y visualización** (franja por equipo) | — | 40 |
| ☐ | 🎯 Reto · **Memoria técnica:** esqueleto y *model card* | [esqueleto](3_Reto/4_Plantillas_y_entrega/plantilla_esqueleto_memoria_tecnica.md) | 85 |
| ☐ | 🎯 Reto · **Subid de nivel:** completad la medición de sesgos por subgrupos y la visualización que la acompaña | — | 50 |

**En clase: 4 h 10 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Demostrador funcionando (aunque sea básico).
- [ ] Esqueleto de la memoria creado.

## Día 2 · Miércoles 9/12

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 🎯 Reto · **Mitigar sesgos** detectados y volver a medir | — | 65 |
| ☐ | 🎯 Reto · Anota los resultados en el registro de experimentos | — | 15 |
| ☐ | 🎯 Reto · **Demostrador:** pulir y probarlo en limpio | — | 40 |
| ☐ | 🎯 Reto · **Model card** del modelo final | — | 35 |
| ☐ | 🎯 Reto · **Memoria técnica** | — | 45 |
| ☐ | 🎯 Reto · **Subid de nivel:** mejorad el criterio más flojo de la rúbrica (la mitigación, el demostrador o la model card) | — | 50 |

**En clase: 4 h 10 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Demostrador y model card casi listos.
- [ ] Memoria con todos los apartados.

## Día 3 · Jueves 10/12

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 🎯 Reto · **Memoria y verificación en limpio:** clona tu repo en un Colab nuevo y comprueba que todo se ejecuta (`checklist_congelacion.md`) | [`checklist_congelacion.md`](3_Reto/4_Plantillas_y_entrega/checklist_congelacion.md) | 60 |
| ☐ | 🎯 Reto · **Subid de nivel:** repasad la rúbrica y corregid lo que aún está en el nivel mínimo antes de la congelación | — | 50 |
| ☐ | 🎯 Reto · Corrige lo que haya fallado | — | 20 |
| ☐ | 🎯 Reto · **Vídeo de reserva** de la demo (por si falla internet el día de la defensa) | — | 30 |
| ☐ | 🎯 Reto · **Checklist de congelación** y coevaluación | [coevaluación](3_Reto/4_Plantillas_y_entrega/plantilla_coevaluacion.md) | 35 |
| ☐ | 🔔 Ceremonia · Review (5 min de demo por equipo) y retro: ¿qué mantenemos?, ¿qué cambiamos? | — | 35 |
| ☐ | 🔔 Ceremonia · 🔒 **Congelación a las 14:30:** último *push*. Lo que no esté subido, no cuenta (los 30 min finales son el margen) | — | 20 |

**En clase: 4 h 10 min.**

## El reto en pocas palabras

**Qué os pide el cliente.** El cliente (el docente) va a **recibir vuestro trabajo como si fuera un entregable real**. Quiere poder:

Para trabajar: [reto en una página](3_Reto/1_Reto_en_una_pagina/Reto_Sprint_16_una_pagina.md). Para consultar: [ficha completa del reto](3_Reto/2_Ficha_completa/Reto_Sprint_16.md) (pasos, rúbrica, ayudas y errores frecuentes). Plantillas, datos y autoevaluación: [`3_Reto/4_Plantillas_y_entrega/`](3_Reto/4_Plantillas_y_entrega/).

## ✅ Antes de cerrar el sprint (Definition of Done)

**Archivos subidos en el repositorio del equipo, carpeta `sprint-16/`** (marca cada uno cuando lo veas en GitHub):
- [ ] `README.md` · lo creáis
- [ ] `notebooks/04_evaluacion.ipynb` · lo creáis a partir de un cuaderno
- [ ] `demostrador/logica.py` · lo modificáis
- [ ] `demostrador/app.py` · lo modificáis
- [ ] `demostrador/tests/test_logica.py` · lo modificáis
- [ ] `demostrador/requirements.txt` · lo modificáis
- [ ] `docs/riesgos_eticos.md` · lo modificáis
- [ ] `docs/model_card.md` · lo creáis a partir de una plantilla
- [ ] `docs/memoria_tecnica.pdf` · lo creáis a partir de una plantilla
- [ ] `autoevaluacion_nombre.md` · **uno por persona** (la coevaluación va dentro del mismo fichero): [plantilla](3_Reto/4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md)

**Total en `sprint-16/`: 9 ficheros del equipo + 1 hoja por persona** (un equipo de 3 sube 12). Aparte: docs/demo.mp4; demostrador/modelo/; demostrador/api.py; Datos del proyecto o script de descarga; los extras solo si los hacéis. La *review* y la *retro* no se suben.

**Comprobaciones antes de dar el sprint por cerrado:**
- [ ] Evaluación en test hecha **una sola vez**, con gráficos y análisis de errores.
- [ ] Rendimiento por subgrupos y mitigación aplicada y medida.
- [ ] Registro de riesgos cerrado; demostrador probado desde cero, con vídeo plan B.
- [ ] README reproducible probado por otra persona; model card y memoria en `docs/`.
- [ ] La **coevaluación confidencial** (anexo B de la memoria) entregada al docente: no se sube al repositorio, a diferencia de la hoja de autoevaluación y coevaluación
- [ ] Alguien que **no escribió esa parte** ha revisado el entregable con la [rúbrica](3_Reto/2_Ficha_completa/Reto_Sprint_16.md#rúbrica-del-reto--cómo-se-puntúa-y-cómo-se-revisa) y lo ha anotado en el propio entregable

## En casa (cuando puedas)

- Los ejercicios de cada cuaderno que **no** se hacen en clase. Se autocorrigen, y debajo llevan una «Solución de referencia» plegada por si te quedas atascado.
- Si quieres repasar la teoría con calma: [apuntes del sprint](1_Teoria/apuntes/apuntes_demostrador_sesgos_y_memoria.md).

## Si te atascas

1. Lee primero la parte «Si os atascáis» de la [ficha completa del reto](3_Reto/2_Ficha_completa/Reto_Sprint_16.md).
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
| M9 · Evaluación, visualización e IA responsable | evaluación, visualización y componente de IA responsable |
| M9 · Despliegue y documentación | despliegue/demostrador, documentación y memoria |

**Y ahora:** Sprint 17 · Storytelling, ensayos y defensa (viernes 11/12).

*.*
