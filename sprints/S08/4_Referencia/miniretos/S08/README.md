# 🎒 Bolsa de miniretos · S08

**Elige una miniapp de IA, constrúyela en 40–60 minutos y enséñasela a la clase.** Sin TurisData: otros datos, otras preguntas y solo lo que ya conocéis hasta el Sprint 8.

- **Cuándo:** al cerrar S08, en casa o cuando acabéis antes. **Opcional**: no entra en la rúbrica del reto.
- **Con quién:** en pareja o en equipo de tres. Un equipo puede hacer **dos** miniapps.
- **Dónde:** en Google Colab, con un cuaderno nuevo. Cada ficha trae las celdas para copiar y pegar, **una por paso**. No hay que instalar nada.
- **Qué se ve al final:** un gráfico, una tabla de modelos y una **app** (una función que probáis con casos vuestros).

## Las miniapps

| | Miniapp | Pregunta | Tipo | Nivel | Practica |
|---|---|---|---|---|---|
| 🌸 | [06 · El zoo de fronteras](06_Zoo_de_fronteras.md) | ¿Qué especie de flor es? | Clasificar y **dibujar** cómo decide cada modelo | ⭐ | Árbol, bosque, SVM, k-NN |
| ✍️ | [05 · Números a mano](05_Digitos.md) | ¿Qué número es esta imagen? | Clasificar **imágenes** (0–9) | ⭐ | SVM (`gamma`), k-NN, bosque |
| 🎗️ | [03 · Tumor](03_Tumor.md) | ¿Benigno o maligno? | Clasificar con **umbral** | ⭐ | Umbral, FN frente a FP, los 6 modelos |
| 📧 | [02 · Correo y spam](02_Correo_spam.md) | ¿Spam o correo de verdad? | Clasificar **texto** | ⭐⭐ | Árbol con reglas, Naive Bayes, logística |
| 🩺 | [04 · Diabetes](04_Diabetes.md) | ¿Riesgo de diabetes? | Clasificar con **datos que faltan** | ⭐⭐ | `Pipeline`, ROC, umbral |
| 🏠 | [01 · Precio de vivienda](01_Precio_vivienda.md) | ¿Cuánto vale este piso en Tenerife? | **Regresión** | ⭐⭐ | Lineal frente a bosque y boosting |
| 🎮 | [07 · Tramposos en un videojuego](07_Tramposos_en_un_videojuego.md) | ¿Este jugador hace trampas? | Clasificar con **umbral exigente** | ⭐⭐ | Precisión frente a recall; a veces gana el modelo sencillo |
| 🔥 | [08 · Riesgo de incendio](08_Riesgo_de_incendio.md) | ¿Hoy hay riesgo de incendio forestal? | Suceso **raro** y semáforo | ⭐⭐⭐ | Reglas de un árbol, bosque, boosting, `RandomizedSearchCV` |
| 🚑 | [09 · Triaje de urgencias](09_Triaje_de_urgencias.md) | ¿Este paciente es urgente? | **Explicable frente a potente** | ⭐⭐⭐ | Árbol frente a bosque, recall exigido, grupos de edad |
| 👕 | [10 · Reconocer prendas](10_Reconocer_prendas.md) | ¿Qué prenda de ropa es? | Clasificar **imágenes** | ⭐⭐ | SVM, k-NN, bosque, matriz de confusión |

## Cómo elegir
- **Quiero entender los modelos de un vistazo:** 🌸 el zoo de fronteras.
- **Quiero algo visual y rápido:** ✍️ números a mano.
- **Me interesa la salud:** 🎗️ tumor o 🩺 diabetes.
- **Me interesa el lenguaje:** 📧 correo y spam.
- **Me interesa el negocio:** 🏠 precio de vivienda.
- **Me gustan los videojuegos:** 🎮 tramposos.
- **Me interesa el medio ambiente y las emergencias:** 🔥 incendio forestal o 🚑 triaje.
- **Quiero imágenes más reales que los números:** 👕 prendas de ropa.

## Las 5 reglas (valen para todas)
1. **Un modelo tonto de referencia** (siempre la media o siempre la clase más común). Si no lo superáis, no habéis hecho nada.
2. **Separad train y test antes de nada.** El examen (`test`) se mira **una sola vez**, al final, solo con el campeón.
3. **Comparad al menos 4 modelos** con validación cruzada sobre `train`. Elegid el campeón por la tabla, no por intuición.
4. **Probad vuestra app con 3 casos propios**, incluido uno «difícil».
5. **Contad dónde falla** mirando ejemplos concretos.

## Tarjeta de cierre (4 frases, en la hoja compartida)
- **Mi app decide** ______ a partir de ______.
- **Acierta** ______ en el examen, frente a ______ del modelo tonto.
- **Falla cuando** ______.
- **No debe usarse para** ______.

## La demo (2 minutos por equipo)
- Enseñad la app con **un caso que acierta** y **uno que falla**.
- Decid en una frase **qué modelo ganó y por qué**.
- Una pregunta de la clase y, después, la siguiente.

## Qué datos hay detrás
- **Dentro de scikit-learn** (no se descargan): flores, números a mano y tumores.
- **Se descargan solas al ejecutar** desde OpenML: las fotos de ropa (Fashion-MNIST, muestra de 6 000).
- **En el repositorio del curso** (`datos/`): `correos.csv`, `viviendas_tenerife.csv`, `tramposos_juego.csv`, `incendios_canarias.csv` y `triaje_urgencias.csv`, **inventados**, y `diabetes_pima.csv`, de un estudio real (Pima, dominio público).
- Los datos de salud son **para aprender**: ninguna de estas miniapps diagnostica nada ni decide quién se atiende primero.

## Para subirlo (opcional)
- Descargad el cuaderno de Colab (*Archivo → Descargar → .ipynb*) y subidlo a `sprint-08/miniretos/` de vuestro repositorio, con la tarjeta de cierre en un `README.md`.
- Es práctica extra: no se evalúa con la rúbrica, pero se puede enseñar en la defensa final o contarlo en el muro de ideas del proyecto de cierre.

## Y si queréis otra
- Proponed una miniapp con **datos abiertos** (una tabla con una columna que predecir) y una pregunta cerrada. El docente os dice si encaja.
- Otras ideas posibles: calidad de un vino, supervivencia en el Titanic, tipo de cubierta forestal o reconocimiento de gestos.
- Más miniapps de los sprints anteriores: [S06](../S06/README.md) (datos sucios, fugas) y [S07](../S07/README.md) (fraude, abandono, precios).
