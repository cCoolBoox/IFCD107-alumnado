# Sprint 16 · Reto «Entrega final: evaluar, demostrar y documentar»

> **Ficha completa del reto, para consultar.** Para trabajar, [el reto en una página](../1_Trabajar/Reto_Sprint_16_una_pagina.md). Qué se sube y cómo se evalúa: [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md).
>
> - Volver al [README del sprint](../../README.md).
> - Si es vuestro primer reto: [Cómo se trabaja un reto](../../../../material/4.%20Como_se_trabaja_un_reto.md).

## Ficha del reto

### 1 · 🎯 Qué os pide el cliente

**Qué os pide el cliente.** El cliente (el docente) va a **recibir vuestro trabajo como si fuera un entregable real**. Quiere poder **clonar el repositorio y seguir el README**, **ver funcionar el demostrador**, **leer una memoria de 10–15 páginas** y **entender los riesgos** antes de decidir si adopta vuestro modelo. Para eso tenéis que: evaluar a fondo el modelo candidato del Sprint 15 (una sola vez en el test), buscar sesgos por subgrupos y **aplicar y medir** una medida para reducirlos, cerrar el registro de riesgos y clasificar el sistema según el RGPD y el AI Act, construir un demostrador que no se rompa con entradas erróneas, que avise de la incertidumbre y que tenga **plan B en vídeo**, y documentarlo todo (model card, README y memoria técnica).

**Cómo se trabaja.** Este es el sprint de cierre: no hay una plantilla de código que rellenar (salvo el demostrador), sino **vuestro proyecto de los sprints 14 y 15**, que ahora hay que terminar y dejar listo para que otra persona lo use. Os damos plantillas para el demostrador, la model card, la memoria y la lista de congelación. **Todo lo que haya en la rama principal del repositorio a las 14:30 del 10/12 es lo que se evalúa**; pasada esa hora, se congela. Hay tres días de clase y, **entre el día 1 y el día 2, dos días sin clase**: buen momento para avanzar la memoria. El equipo decide hasta dónde llega: 🟢 mínimo, 🟡 estándar o 🔴 extra.

---

### 2 · 🧰 Recursos del reto

| Recurso | Para qué lo usaréis | Dónde está |
|---|---|---|
| **Vuestro proyecto** (repositorio privado `ifcd107-equipo-…`) | El modelo candidato del Sprint 15, su registro de experimentos, los datos y el registro de riesgos de los sprints 14 y 15 | Vuestro repositorio de GitHub |
| **Cuaderno del S13** [`S13_02`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/2_Practica/S13_02_plantilla_informe_visual.ipynb) | Los gráficos de la evaluación (matriz de confusión, curvas, importancia de variables, SHAP o Grad-CAM) para adaptarlos | Colab |
| **Presentación S16.1** y **apuntes del sprint** | Qué es un demostrador, cómo se documenta y, con ejemplos de números, cómo se miden los sesgos y su mitigación | [Presentación](../../1_Teoria/S16.1_Pildora_demostrador_y_documentacion.pdf) · [apuntes](../../1_Teoria/apuntes/apuntes_demostrador_sesgos_y_memoria.md) |
| **Cuaderno del sprint** [`S16_01`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S16/2_Practica/S16_01_demostrador.ipynb) | Práctica del demostrador: guardar el modelo y sus metadatos, separar la lógica, pruebas, Streamlit, widgets y API | Colab |
| **La carpeta del demostrador** [`demostrador/`](../1_Trabajar/plantillas/demostrador/) | `logica.py`, `app.py`, `api.py` (opcional), `tests/test_logica.py`, `requirements.txt` y `README_demostrador.md`. Es un ejemplo completo con el modelo de TurisData: vosotros lo adaptáis a **vuestro** proyecto. La carpeta `modelo/` no viene hecha: la crea el cuaderno `S16_01` o vuestro script de entrenamiento | En GitHub: *Code → Download ZIP*. Trabajad en una copia |
| **Python y librerías** (`scikit-learn`, `streamlit`, `pytest`…) | Ejecutar el cuaderno de evaluación, lanzar el demostrador y las pruebas | `pip install -r requirements.txt`. Si no podéis instalar Streamlit, la alternativa es el cuaderno con *widgets* de `S16_01` |
| **Model card** | Ficha técnica del modelo de máximo 2 páginas | [`plantilla_model_card.md`](../1_Trabajar/plantillas/plantilla_model_card.md) |
| **Esqueleto de la memoria** | Secciones, presupuesto de páginas y mapa de requisitos R1–R11 | [`plantilla_esqueleto_memoria_tecnica.md`](../1_Trabajar/plantillas/plantilla_esqueleto_memoria_tecnica.md) |
| **Lista de congelación** | Repasar todo antes de las 14:30 | [`checklist_congelacion.md`](../1_Trabajar/plantillas/checklist_congelacion.md) |
| **Coevaluación individual (anexo B)** | Valorar el trabajo de cada persona del equipo. Es **confidencial**: va al docente, no al repositorio | [`plantilla_coevaluacion.md`](../1_Trabajar/plantillas/plantilla_coevaluacion.md) |
| **Cómo entregar en GitHub** | Subir los ficheros a `sprint-16/` | [Guía de entrega](../../../../material/5.%20Como_entregar_en_GitHub.md) |
| **Autoevaluación y coevaluación** | Cada persona rellena su hoja y la sube | [Hoja del sprint](../2_Entregar/autoevaluacion_y_coevaluacion.md) |
| **Un asistente de IA** (opcional) | Entender sesgos, errores de código o revisar la redacción | Con las reglas de la «Ayuda 1» del paso a paso |

---

### 3 · 🪜 Guía paso a paso

Son ocho pasos, de **525 minutos en total** repartidos en tres días. Las jornadas de proyecto duran **6 horas completas (250 minutos de trabajo al día)**: los pasos de esta ficha ocupan unos 200 y los **50 minutos restantes de cada día son «subir de nivel»** (pasar del mínimo al estándar con la rúbrica en la mano). Cada uno dice **qué hacéis** (la lista corta), **cómo se hace** con el detalle, **qué deberíais ver** y **cuándo está hecho**. Las ayudas (IA, errores, atascos) están al final. El día 1 empieza con 10 minutos de planning, la píldora de teoría y la práctica del demostrador (`S16_01`), que no se cuentan en los 525. Si el tiempo aprieta, completad el nivel mínimo y dejad lo demás para los dos días sin clase.

**Cada paso tiene su propia página.** Abrid la que toque y volved aquí cuando acabéis:

- [Paso 1 · Evaluar el modelo en el test y buscar dónde falla (día 1, 40 minutos)](Reto_Sprint_16_paso_1.md)
- [Paso 2 · Abrir la memoria y la model card (día 1, 85 minutos)](Reto_Sprint_16_paso_2.md)
- [Paso 3 · Mitigar el sesgo y volver a medir (día 2, 80 minutos)](Reto_Sprint_16_paso_3.md)
- [Paso 4 · Pulir el demostrador y probarlo en limpio (día 2, 40 minutos)](Reto_Sprint_16_paso_4.md)
- [Paso 5 · Cerrar la model card y completar la memoria (día 2, 80 minutos)](Reto_Sprint_16_paso_5.md)
- [Paso 6 · Verificar en limpio y corregir (día 3, 80 minutos)](Reto_Sprint_16_paso_6.md)
- [Paso 7 · Plan B, riesgos cerrados, lista de congelación y coevaluación (día 3, 65 minutos)](Reto_Sprint_16_paso_7.md)
- [Paso 8 · Revisión con la rúbrica, review, retro y congelación (día 3, 55 minutos)](Reto_Sprint_16_paso_8.md)

#### Ayuda 1 · Cómo usar la IA en este reto

La IA puede ahorrar tiempo, pero **escribe con seguridad cosas que pueden ser falsas** y puede cambiar una cifra sin avisar. Reglas:
- **Todo lo que dé, lo ejecutáis y lo entendéis.** Si el docente pregunta por una parte, tenéis que saber explicarla.
- **La memoria es vuestra:** la IA no la escribe por vosotros. Si la usáis para redactar o corregir, revisadla entera y **declaradlo en la memoria**.
- **Las cifras mandan:** después de que la IA toque un texto, comprobad que no ha cambiado ninguna.
- **Nada de datos personales ni claves** en una IA.

| Para qué | Ejemplo de petición | Qué comprobáis |
|---|---|---|
| Entender sesgos | «Explícame con un ejemplo qué significa que un modelo tenga peor rendimiento en un subgrupo y qué medidas existen» | Que podéis aplicar una medida **y medirla** |
| Crear la app | «Ayúdame a añadir validación de entradas a esta app de Streamlit: *[código]*» | Que **probáis** entradas absurdas |
| Estructurar la memoria | «Dame un guion de las secciones de una memoria técnica de un proyecto de IA» | Que cada sección la redactáis vosotros con **vuestros resultados** |
| Revisar la redacción | «Corrige la ortografía y la claridad de este párrafo sin cambiar el contenido» | Que no se ha cambiado ninguna cifra |

#### Ayuda 2 · Errores frecuentes (y cómo evitarlos)

| Error | Por qué ocurre | Cómo evitarlo |
|---|---|---|
| Dejar la memoria para el último día | «Total, ya está hecho» | Borrador el día 2 (9/12) y revisión el día 3 (10/12) |
| El demostrador solo funciona en el ordenador de una persona | Dependencias sin documentar | `requirements.txt` con versiones y prueba en un entorno limpio |
| Mitigación que se aplica pero no se mide | Se piensa que basta con hacerla | Comparad las métricas **antes y después, por subgrupo** |
| Subir cambios después de las 14:30 | Se siguen retocando cosas | Crear la etiqueta antes y no tocar nada después |
| Coevaluación sin entregar | Se olvida | Cada persona la entrega; cuenta para la nota individual |
| Memoria con más de 15 páginas o con fragmentos copiados | Se llena de relleno | Respetad el presupuesto de páginas; los anexos no cuentan; escribid con vuestras palabras |
| Cifras distintas en la memoria y en el README | Se copian de versiones distintas | Una revisión final de coherencia antes de congelar |
| Solo una persona hace commits | «El resto no sabe Git» | Reparto real: vale que cada persona suba un fichero desde la web |

#### Ayuda 3 · Si os atascáis

1. **El demostrador no arranca en otro ordenador:** faltan dependencias. Generad `requirements.txt` con `pip freeze` (o a mano), recortadlo a lo que usáis y probad en un entorno nuevo.
2. **No sabéis qué sesgo medir:** mirad las columnas con categorías (país, canal, tipo) y calculad la métrica para cada valor.
3. **Falta tiempo:** priorizad lo obligatorio (R1–R11 y la lista de congelación). Es mejor una memoria honesta con límites que una incompleta. Preguntad al equipo y, después, al docente.
