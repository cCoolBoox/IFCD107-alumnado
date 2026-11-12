# Sprint 7 · Reto «Precio y cancelación» · Entrega y rúbrica

> **Qué se sube y cómo se evalúa.** Se lee **una vez**, antes de entregar, y se vuelve a la rúbrica cuando el equipo revisa su trabajo. Mientras trabajáis no hace falta: para eso está [el reto en una página](../1_Trabajar/Reto_Sprint_07_una_pagina.md).
>
> - Volver al [README del sprint](../../README.md) · [ficha del reto](../3_Consultar/Reto_Sprint_07.md), para consultar.
> - Vuestra hoja personal: [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md).
> - Para ver cómo queda todo lo que se sube, con cifras reales: la [entrega de ejemplo](../3_Consultar/Solucionario/README.md).
> - Cómo subir a GitHub paso a paso, con capturas: [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md).

Esta hoja responde a **dos preguntas distintas**, una tabla para cada una:

**Tabla A · Los ficheros:** qué ficheros hay, de dónde sale cada uno (ya hecho, lo modificáis, lo creáis o lo genera el programa) y **cuáles se suben y adónde**.

**Tabla B · Los requisitos:** qué tiene que cumplir lo que entregáis y hasta dónde llegar (🟢 mínimo, 🟡 estándar, 🔴 extra). **Es lo que se evalúa.**

**En total, al final del sprint se suben a `sprint-07/`:** **3 ficheros del equipo** (`informe_modelado.md`, `reto_S07.ipynb`, `README.md`) **+ 1 autoevaluación y coevaluación por persona**, es decir, **3 + tantos ficheros como personas haya en el equipo** (un equipo de 3 sube 6). «El reto» no es un fichero aparte: son esos tres ficheros. Además, el CSV va a `data/` si aún no está. La *review* y la *retro* se hacen de palabra, el jueves 12/11 junto con las del Sprint 8: no se suben.

## 1 · 📦 Tabla A · Los ficheros: de dónde sale cada uno y cuáles se suben

Todo lo que se sube va al repositorio privado del equipo (`ifcd107-equipo-…`), en la carpeta **`sprint-07/`**, salvo el CSV.

| Fichero | Origen | Qué hacéis vosotros | ¿Se sube? |
|---|---|---|---|
| `reto_S07.ipynb` | **Lo creáis.** No hay plantilla: es un cuaderno nuevo de Colab | Reutilizáis las celdas de `S07_01` a `S07_04`: un modelo de **precio** y otro de **cancelación**, cada uno con su *baseline*, validación y métricas | **Sí** · `sprint-07/` |
| `informe_modelado.md` (o `.pdf`) | **Lo creáis a partir de una plantilla.** Os damos `informe_modelado_plantilla.md` con huecos | Copiarla como `informe_modelado.md` y rellenarla (2–3 páginas, con euros) | **Sí** · `sprint-07/` |
| `README.md` | **Lo modificáis.** La carpeta `sprint-07/` ya trae un `README.md` (si no, lo creáis) | Abrirlo con el lápiz ✏️ y escribir semilla, versiones, cómo ejecutar, quién hizo qué y el uso de la IA | **Sí** · `sprint-07/` |
| `reservas_turisdata.csv` | **Ya hecho.** Los datos reales (sintéticos) | Nada: se usa sin cambiarlo | **Sí**, sin cambios · `data/` (si aún no está) |
| Autoevaluación y coevaluación (`autoevaluacion_nombre.md`) | **Ya hecha, en blanco** | Cada persona copia la plantilla con su nombre y la rellena; la coevaluación va **dentro del mismo fichero** | **Sí**, **una por persona** (no una por equipo) · `sprint-07/` |
| Segundo modelo de clasificación (extra) | **Lo creáis vosotros**, dentro de `reto_S07.ipynb` | Solo si el equipo llega al nivel extra | Solo si lo hacéis · dentro de `reto_S07.ipynb` |
| Cuadernos de práctica `S07_01`–`S07_05` | **Ya hecho.** Son vuestras copias de trabajo del sprint | Usarlos como pista y copiar las celdas que os sirvan | **No se suben** |

---

## 2 · ✅ Tabla B · Los requisitos: qué tiene que cumplir y hasta dónde llegar

| Requisito | Qué se pide exactamente | Nivel | Dónde se comprueba |
|---|---|---|---|
| **Sin fuga de datos** | Solo variables **conocidas en el momento de reservar**. `cancelada` no se usa para predecir el precio. Lista escrita de variables usadas y excluidas | 🟢 Mínimo | `reto_S07.ipynb` · `informe_modelado.md` (apartado 2) |
| **Precio: referencia y regresión lineal** | *Baseline* (predecir siempre el precio medio de entrenamiento) y regresión lineal, con MAE y RMSE **en euros** sobre datos de test | 🟢 Mínimo | `reto_S07.ipynb` · informe (apartado 3) |
| **Cancelación: referencia y logística** | Partición train/test, *baseline* (siempre «no cancela») y regresión logística, con matriz de confusión | 🟢 Mínimo | `reto_S07.ipynb` · informe (apartado 4) |
| **Hipótesis de coste** | `COSTE_FN` y `COSTE_FP` como variables del cuaderno, cada una con **una frase de razón**. «La IA dijo 200 €» no vale | 🟢 Mínimo | `reto_S07.ipynb` · informe (apartado 5) |
| **Umbral elegido** | Un umbral elegido y justificado en una frase. En el mínimo, puede salir de una tabla corta de umbrales | 🟢 Mínimo | `reto_S07.ipynb` · informe (apartado 5) |
| **Informe** | `informe_modelado.md` con resumen para el gerente (con euros), tabla de métricas de los dos modelos y las hipótesis de coste. En el mínimo, versión corta | 🟢 Mínimo | `informe_modelado.md` |
| **README y reproducibilidad** | `SEMILLA = 42`, versiones de Python y `scikit-learn`, cómo ejecutar el cuaderno de arriba abajo. Cómo se usó la IA: qué pedisteis y qué revisasteis | 🟢 Mínimo | `README.md` |
| **Git** | Todo subido a `sprint-07/` con mensajes de commit claros, de personas distintas, sin claves ni datos personales | 🟢 Mínimo | Historial del repositorio del equipo |
| **Mejora del precio** | Una mejora (interacciones, polinomio, Ridge o Lasso) con MAE, RMSE y **R²**, y una frase sobre si compensa la complejidad. Máximo 3 modelos por problema | 🟡 Estándar | `reto_S07.ipynb` · informe (apartado 3) |
| **Curvas y métricas de la cancelación** | Curvas ROC y PR con AUC y AP, explicados sin jerga en el informe | 🟡 Estándar | `reto_S07.ipynb` · informe (apartado 4) |
| **Umbral que minimiza el coste** | Probar muchos umbrales con **validación cruzada sobre train**, calcular `FN × COSTE_FN + FP × COSTE_FP` y elegir el menor. El test se usa **una sola vez**: coste sin modelo, con umbral 0,5 y con el umbral elegido | 🟡 Estándar | `reto_S07.ipynb` · informe (apartado 5) |
| **Análisis de sensibilidad** | Tabla o gráfico con el umbral óptimo y el coste total cuando cambian `COSTE_FN` y `COSTE_FP` (por ejemplo, FN el doble o FP la mitad) | 🟡 Estándar | `reto_S07.ipynb` · informe (apartado 5) |
| **Recomendación de negocio** | Acción concreta con cifras (umbral, ahorro frente a «no hacer nada») y **límites** (datos sintéticos de un solo hotel…) | 🟡 Estándar | `informe_modelado.md` (apartado 6) |
| **IA responsable** | Riesgos específicos en el informe: quién sufre los falsos positivos, si se penaliza a algún país o canal, qué pasa si se piden depósitos solo a ciertos clientes | 🟡 Estándar | `informe_modelado.md` (apartado 7) |
| **Revisión y autoevaluación** | Alguien que **no escribió esa parte** revisa cuaderno, informe y README con la rúbrica (justo debajo de estas tablas) y anota nivel y prueba en el informe (si va en PDF, en el README); cada persona sube su hoja de autoevaluación y coevaluación | 🟡 Estándar | `informe_modelado.md` (sección «Revisión con la rúbrica») y `sprint-07/` |
| **Extras** | Un segundo modelo de clasificación (por ejemplo, k-NN) comparado · remuestreo solo en train · recomendación de *overbooking* con el ahorro estimado en euros por temporada | 🔴 Extra | `reto_S07.ipynb` · `informe_modelado.md` |

---

## 3 · 🧭 Rúbrica del reto · cómo se puntúa y cómo se revisa

La usan **dos veces**: el equipo, para revisar su propio trabajo antes de entregar (es lo que dice la *Definition of Done*), y el docente, para puntuar. Se mira **cada criterio por separado** y se pone el nivel de la columna cuyo texto **se cumple entero**: si lo de un nivel se cumple a medias, es el nivel de abajo. **0** significa que no se ha entregado nada de ese criterio.

Orientación: lo que pide el nivel 🟢 mínimo sale en un **2**, el 🟡 estándar en un **3** y los 🔴 extras en un **4**.

| Criterio | 1 · Empezado | 2 · Mínimo | 3 · Estándar | 4 · Extra |
|---|---|---|---|---|
| **Corrección técnica** (¿funciona?) | Hay cuaderno, pero faltan los *baselines*, se usa `cancelada` para predecir el precio o no se ejecuta de arriba abajo | Precio y cancelación tienen *baseline* y modelo; MAE y RMSE en euros; matriz de confusión; sin fuga; `COSTE_FN` y `COSTE_FP` definidos y un umbral elegido | Mejora del precio con R²; ROC/PR con AUC y AP; umbral elegido con validación cruzada sobre train minimizando el coste; test usado **una sola vez**; máximo 3 modelos por problema | Además, un segundo modelo de clasificación comparado o remuestreo hecho solo en train, sin fuga, y las cifras del informe coinciden con las del cuaderno |
| **Reproducibilidad** (¿lo puede repetir otra persona?) | Solo funciona en la sesión de quien lo hizo (faltan celdas, rutas propias) | El README dice cómo ejecutar, pero falta la semilla o las versiones | Otra persona ejecuta el cuaderno de arriba abajo y obtiene **las mismas cifras** siguiendo solo el README (`SEMILLA = 42`, versiones, orden); todo en `sprint-07/`, el CSV en `data/` y commits de personas distintas, sin claves | Además, el README indica el orden exacto de ejecución y qué cifras del informe sale de qué celda |
| **Análisis y comunicación al cliente** (¿lo entiende quien no programa?) | El informe solo da métricas técnicas (AUC, RMSE) sin pasarlas a euros | El resumen para el gerente da el error del precio en euros y una hipótesis de coste con razón para cada error, pero sin sensibilidad ni límites | Recomendación con **cifras** (umbral, coste frente a «no hacer nada»), sensibilidad y límites, sin jerga: el gerente entiende qué hacer y cuánto se juega | Además, dice con qué costes la recomendación cambiaría y qué dato del hotel haría falta para afinarla |
| **IA responsable** (¿se sabe qué hizo la IA y qué comprobasteis?) | No dice si se ha usado IA ni habla de riesgos | Dice que se ha usado IA, o nombra riesgos genéricos, sin detalle | El README dice **qué se pidió, qué se revisó y qué se cambió**; los costes y el umbral salen de vuestro cálculo; el informe nombra riesgos **específicos** (falsos positivos, país o canal, depósitos) | Además, comprueba un riesgo con los datos (por ejemplo, la tasa de falsos positivos por canal o país), propone una medida y recuerda que los datos son sintéticos |

**Cómo se revisa** (unos 10 minutos, antes de subir; lo hace **una persona que no escribió esa parte**):

1. **Ejecutar** el cuaderno en una sesión nueva de Colab con *Entorno de ejecución → Reiniciar y ejecutar todo*, copiando solo lo que dice el README. Anotar si algo falla o si alguna cifra cambia respecto al informe.
2. **Leer el informe como si fuera el gerente:** ¿se entiende el resumen sin saber qué es el AUC? ¿La recomendación tiene euros y límites? Subrayar lo que no se entienda.
3. **Mirar el cuaderno:** ¿alguna variable no se conoce al reservar? ¿Se usa `X_test` antes de elegir el umbral? ¿Los costes están en `COSTE_FN` y `COSTE_FP`, con su razón? Que quien lo escribió explique cualquier celda que no entendáis.
4. **Poner un nivel (1 a 4) en cada criterio, con una frase de prueba.** Ejemplos: «Corrección técnica · 2: hay baselines y matriz, pero el umbral se eligió mirando el test en la celda 18»; «Reproducibilidad · 3: mismas cifras siguiendo el README, versiones indicadas»; «Análisis · 2: el resumen da el MAE en euros, pero falta decir qué pasa si el coste de FP se duplica»; «IA responsable · 3: dicen qué pidieron y qué revisaron, y hablan de depósitos por país». Sin prueba escrita, el nivel no vale.
5. **Apuntar el resultado** en la sección «Revisión con la rúbrica» del final de `informe_modelado.md` y corregir lo más fácil de arreglar. Lo demás se anota como mejora.

Cada persona, además, se puntúa a sí misma en su hoja de [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md) con **esta misma rúbrica**.
