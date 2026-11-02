# Sprint 8 · Reto «Duelo de modelos» · Entrega y rúbrica

> **Qué se sube y cómo se evalúa.** Se lee **una vez**, antes de entregar, y se vuelve a la rúbrica cuando el equipo revisa su trabajo. Mientras trabajáis no hace falta: para eso está [el reto en una página](../1_Trabajar/Reto_Sprint_08_una_pagina.md).
>
> - Volver al [README del sprint](../../README.md) · [ficha del reto](../3_Consultar/Reto_Sprint_08.md), para consultar.
> - Vuestra hoja personal: [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md).
> - Cómo subir a GitHub paso a paso, con capturas: [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md).

Esta hoja responde a **dos preguntas distintas**, una tabla para cada una:

**Tabla A · Los ficheros:** qué ficheros hay, de dónde sale cada uno (ya hecho, lo modificáis, lo creáis o lo genera el cuaderno) y **cuáles se suben y adónde**.

**Tabla B · Los requisitos:** qué tiene que cumplir lo que entregáis y hasta dónde llegar (🟢 mínimo, 🟡 estándar, 🔴 extra). **Es lo que se evalúa.**

**En total, al final del sprint se suben a `sprint-08/`:** **4 ficheros del equipo** (`leaderboard_S08.csv`, `model_card.md`, `reto_S08.ipynb`, `README.md`) **+ 1 autoevaluación y coevaluación por persona**, es decir, **4 + tantos ficheros como personas haya en el equipo** (un equipo de 3 sube 7). «El reto» no es un fichero aparte: son esos cuatro ficheros. Los datos no se suben: el cuaderno los descarga solo. La *review* y la *retro* se hacen de palabra: no se suben.

## 1 · 📦 Tabla A · Los ficheros: de dónde sale cada uno y cuáles se suben

Todo lo que se sube va al repositorio privado del equipo (`ifcd107-equipo-…`), en la carpeta **`sprint-08/`**.

| Fichero | Origen | Qué hacéis vosotros | ¿Se sube? |
|---|---|---|---|
| `leaderboard_S08.csv` | **Lo genera** el cuaderno: cada `registrar(...)` añade o actualiza una fila | Registrar vuestros modelos en el cuaderno y, al acabar, descargar el CSV desde el panel de archivos de Colab. No se escribe a mano | **Sí** · `sprint-08/` |
| `reto_S08.ipynb` | **Lo modificáis.** Parte de `S08_06_leaderboard_plantilla`: las herramientas ya vienen hechas | Rellenar los huecos `TODO`, añadir las búsquedas de hiperparámetros y dejarlo ejecutado de arriba abajo | **Sí** · `sprint-08/` |
| `model_card.md` | **Lo creáis a partir de una plantilla.** Os damos `model_card_plantilla.md` con apartados | Copiarla como `model_card.md` y rellenarla con **vuestros** números | **Sí** · `sprint-08/` |
| `README.md` | **Lo modificáis.** Ya está creado en `sprint-08/` con la plantilla del repositorio del equipo; el paso 5 os da el guion | Escribirlo: qué se entrega, quién hizo qué, cómo se reproduce, uso de IA y revisión con la rúbrica | **Sí** · `sprint-08/` |
| Autoevaluación y coevaluación (`autoevaluacion_nombre.md`) | **Ya hecha, en blanco** | Cada persona copia la plantilla con su nombre y la rellena; la coevaluación va **dentro del mismo fichero** | **Sí**, **una por persona** (no una por equipo) · `sprint-08/` |
| `leaderboard_plantilla.csv` | **Ya hecho.** Solo enseña las columnas de la tabla | Nada: el cuaderno crea el vuestro | **No** |
| `reservas_turisdata.csv` | **Ya hecho.** Los datos (sintéticos) | Nada: el cuaderno los descarga y no se cambian | **No**, ya están en el repositorio del curso |

---

## 2 · ✅ Tabla B · Los requisitos: qué tiene que cumplir y hasta dónde llegar

| Requisito | Qué se pide exactamente | Nivel | Dónde se comprueba |
|---|---|---|---|
| **Pesos de los criterios** | Pesos de rendimiento, explicabilidad y coste que sumen 100 %, acordados con la «voz del cliente» y **escritos con su justificación** | 🟢 Mínimo | `model_card.md` (apartado 3) y `reto_S08.ipynb` |
| **Leaderboard** | Al menos **6 modelos** medidos igual (referencia o *baseline*, logística, árbol, bosque, *boosting* y SVM), de al menos 4 familias y **máximo 8**. Mismos datos, folds y métrica: no se toca la celda de herramientas | 🟢 Mínimo | `leaderboard_S08.csv` y `reto_S08.ipynb` |
| **Campeón elegido** | El campeón sale de `puntuacion_global` con vuestros pesos y se explica con una frase que nombra los tres criterios. La IA no decide | 🟢 Mínimo | `model_card.md` (apartado 3) |
| **Test una sola vez** | El AUC de test se calcula **solo para el campeón y una sola vez**: la columna `auc_test` tiene valor en una única fila | 🟢 Mínimo | `leaderboard_S08.csv` y `reto_S08.ipynb` |
| **Cuaderno ejecutable** | `reto_S08.ipynb` se ejecuta entero con *Reiniciar y ejecutar todo*, sin errores, con `SEMILLA = 42` | 🟢 Mínimo | `reto_S08.ipynb` |
| ***Model card* (versión corta)** | Resumen, campeón, por qué este y no otro, AUC de test y usos previstos y **no** previstos | 🟢 Mínimo | `model_card.md` |
| **README corto** | Qué se entrega, quién hizo qué y cómo abrir y ejecutar el cuaderno | 🟢 Mínimo | `README.md` |
| **Entrega en GitHub** | Los cuatro ficheros dentro de `sprint-08/`, subidos desde las cuentas de personas distintas, con mensaje claro, sin claves ni datos personales | 🟢 Mínimo | Historial del repositorio del equipo |
| **Búsqueda de hiperparámetros** | En **dos familias** de modelos, con `GridSearchCV` o `RandomizedSearchCV`, validación cruzada y **solo sobre train**. Cada búsqueda, 5 minutos como máximo en Colab. Los mejores modelos, en el leaderboard | 🟡 Estándar | `reto_S08.ipynb` |
| **Análisis de sensibilidad** | Probar otros conjuntos de pesos (el cuaderno trae tres de ejemplo) y contar si el campeón cambia | 🟡 Estándar | `reto_S08.ipynb` y `model_card.md` (apartado 3) |
| ***Model card* completa** | Los diez apartados de la plantilla con **vuestros** datos: modelo, por qué, datos y límites, métricas con incertidumbre y test, usos previstos y no previstos, explicabilidad, riesgos (país de origen) y mantenimiento (deriva) | 🟡 Estándar | `model_card.md` |
| **README completo** | Versiones de las librerías, `SEMILLA = 42`, orden de ejecución, y uso de IA (qué pedisteis y qué revisasteis) | 🟡 Estándar | `README.md` |
| **Revisión y autoevaluación** | Alguien que **no escribió esa parte** revisa el cuaderno, la *model card* y el README con la rúbrica (justo debajo de estas tablas) y anota nivel y prueba en el README; cada persona sube su hoja de autoevaluación y coevaluación | 🟡 Estándar | `README.md` (sección «Revisión con la rúbrica») y `sprint-08/` |
| **Extras** | Importancia de variables del campeón explicada al cliente · comparación con incertidumbre (varias semillas) · plan de mantenimiento del modelo | 🔴 Extra | `reto_S08.ipynb` · `model_card.md` |

---

## 3 · 🧭 Rúbrica del reto · cómo se puntúa y cómo se revisa

La usan **dos veces**: el equipo, para revisar su propio trabajo antes de entregar (es lo que dice la *Definition of Done*), y el docente, para puntuar. Se mira **cada criterio por separado** y se pone el nivel de la columna cuyo texto **se cumple entero**: si lo de un nivel se cumple a medias, es el nivel de abajo. **0** significa que no se ha entregado nada de ese criterio.

Orientación: lo que pide el nivel 🟢 mínimo sale en un **2**, el 🟡 estándar en un **3** y los 🔴 extras en un **4**.

| Criterio | 1 · Empezado | 2 · Mínimo | 3 · Estándar | 4 · Extra |
|---|---|---|---|---|
| **Corrección técnica** (¿funciona?) | Hay cuaderno, pero el leaderboard tiene menos de 6 modelos, se ha cambiado la celda de herramientas o no se ejecuta | 6 modelos medidos igual; campeón elegido con `puntuacion_global`; AUC de test calculado una sola vez y solo para el campeón | Además, búsqueda con validación cruzada solo sobre train en dos familias, sensibilidad de los pesos probada, 4 familias o más y cuaderno que se ejecuta entero | Además, comparación con varias semillas o importancia de variables del campeón que cuadra con los resultados |
| **Reproducibilidad** (¿lo puede repetir otra persona?) | Solo funciona en la sesión de Colab de quien lo hizo, o no hay README | El README dice qué se entrega y cómo abrir el cuaderno, pero faltan versiones, semilla u orden de ejecución | Otra persona, siguiendo solo el README, ejecuta *Reiniciar y ejecutar todo* y obtiene **el mismo leaderboard y el mismo campeón**; los ficheros están en `sprint-08/`, subidos por personas distintas y sin claves | Además, el README da las versiones exactas de las librerías, cuánto tarda en Colab y qué ficheros salen |
| **Análisis y comunicación al cliente** (¿lo entiende quien no programa?) | La *model card* está vacía o copiada de la plantilla; solo hay cifras | Dice cuál es el campeón y su AUC de test, pero no explica por qué ganó | Explica por qué ganó y **por qué no ganó otro** con los tres criterios y los pesos justificados, qué pasa si cambian los pesos y los usos previstos y no previstos, sin jerga | Además, explica al gerente en palabras qué variables pesan más, o da una recomendación con sus límites («si el cliente valorara solo el rendimiento, elegiríamos…») |
| **IA responsable** (¿se sabe qué hizo la IA y qué riesgos tiene el modelo?) | No hay apartado de riesgos ni se dice si se ha usado IA | Menciones genéricas («puede haber sesgos») y dice que se ha usado IA, sin detalle | Riesgos concretos de este modelo (el país de origen como variable sensible, la deriva y qué se medirá, quién revisa las decisiones); dice **qué se pidió a la IA, qué se revisó y qué se cambió**; los datos son sintéticos | Además, mide algo (por ejemplo, el AUC por país o canal) o fija un plan de mantenimiento con un umbral para reentrenar y una persona responsable |

**Cómo se revisa** (unos 10 minutos, antes de subir; lo hace **una persona que no escribió esa parte**):

1. **Ejecutar** `reto_S08.ipynb` en Colab con *Entorno de ejecución → Reiniciar y ejecutar todo*, siguiendo solo lo que dice el README. Anotar si algo falla y si sale el mismo leaderboard y el mismo campeón que dice la *model card*. Frase de prueba: «2 · se ejecuta entero, pero el README no dice el orden».
2. **Contar** en `leaderboard_S08.csv`: modelos (6 a 8), familias (4 o más) y filas con `auc_test` (solo una). Buscar en el cuaderno que `X_test` no aparece en las búsquedas. Frase de prueba: «3 · 7 modelos, 5 familias y `auc_test` en una sola fila».
3. **Leer la *model card* como si fuerais el gerente**: ¿se entiende por qué ganó y por qué no ganó otro? ¿Dice para qué no usarlo? Subrayar lo que no se entienda. Frase de prueba: «2 · dice el campeón, pero no por qué no ganó el *boosting*».
4. **Poner un nivel (1 a 4) en cada criterio, con una frase de prueba** (por ejemplo: «3 · busca en dos familias, pero la sensibilidad solo prueba un conjunto de pesos»). Sin prueba escrita, el nivel no vale. Para IA responsable: «¿dice qué se pidió, qué se revisó y qué riesgo concreto tiene este modelo?».
5. **Apuntar el resultado** en la sección «Revisión con la rúbrica» del `README.md` y corregir lo más fácil de arreglar. Lo demás se anota como mejora.

Cada persona, además, se puntúa a sí misma en su hoja de [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md) con **esta misma rúbrica**.
