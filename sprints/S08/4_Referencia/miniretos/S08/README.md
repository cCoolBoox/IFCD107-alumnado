# 🎒 Bolsa de miniretos · S08

## 🔟 El decálogo
1. **No se puede usar IA** (ni chatbots ni asistentes de código): el código lo pegáis de la ficha y lo entendéis entre todos.
2. **5 minutos para elegir** miniapp. Pasado ese tiempo, empieza el reloj.
3. **55 minutos como máximo** para construirla. Si no llegáis a todo, enseñad lo que tengáis.
4. **Un modelo tonto de referencia** (siempre la media o siempre la clase más común). Si no lo superáis, no habéis hecho nada.
5. **Separad train y test antes de nada.** El examen (`test`) se mira **una sola vez**, al final, solo con el campeón.
6. **Comparad al menos 4 modelos** con validación cruzada sobre `train`. Elegid el campeón por la tabla, no por intuición.
7. **Mirad la métrica que importa, no solo el acierto:** recall, AP o el error en unidades reales (euros, personas…).
8. **Probad vuestra app con 3 casos propios**, incluido uno «difícil».
9. **Contad dónde falla** mirando ejemplos concretos.
10. **Rotad el teclado:** en pareja o en trío, quien escribe cambia cada 10 minutos y todos sabéis explicar cada celda.

## 📦 Qué entregar
Una carpeta `sprint-08/miniretos/` en el repositorio de vuestro equipo con **dos archivos**:
- **El cuaderno** de Colab, ejecutado y sin errores (*Archivo → Descargar → .ipynb*).
- **Un `README.md`** con:
  - La miniapp elegida y quién la hizo.
  - La **tarjeta de cierre** (4 frases):
    - **Mi app decide** ______ a partir de ______.
    - **Acierta** ______ en el examen, frente a ______ del modelo tonto.
    - **Falla cuando** ______.
    - **No debe usarse para** ______.
  - La **tabla de modelos** del duelo, con el campeón marcado.
  - Los **3 casos** que probasteis con la app y **dónde falló**.
- Es práctica extra: **no entra en la rúbrica**, pero se puede enseñar en la defensa final.

## 🎤 Qué hacer en la demo (2 minutos por equipo)
- Enseñad la app con **un caso que acierta** y **uno que falla**.
- Decid en una frase **qué modelo ganó y por qué**.
- Una pregunta de la clase y, después, la siguiente.

## 🧰 Las miniapps
**Elige una miniapp de IA y enséñasela a la clase.** Sin TurisData: otros datos, solo lo que ya conocéis hasta el Sprint 8 (árboles, bosques, boosting, SVM y búsqueda).

- **Con quién:** en pareja o en equipo de tres.
- **Dónde:** en Google Colab, con un cuaderno nuevo. Cada ficha trae las celdas para copiar y pegar, **una por paso**. No hay que instalar nada.
- **Qué se ve al final:** un gráfico, una tabla de modelos frente al modelo tonto y una **app** (una función que probáis con casos vuestros).

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

## Qué datos hay detrás
- **Dentro de scikit-learn** (no se descargan): flores, números a mano y tumores.
- **Se descargan solas al ejecutar** desde OpenML: las fotos de ropa (Fashion-MNIST, muestra de 6 000).
- **En el repositorio del curso** (`datos/`): `correos.csv`, `viviendas_tenerife.csv`, `tramposos_juego.csv`, `incendios_canarias.csv` y `triaje_urgencias.csv`, **inventados**, y `diabetes_pima.csv`, de un estudio real (Pima, dominio público).
- Los datos de salud son **para aprender**: ninguna de estas miniapps diagnostica nada ni decide quién se atiende primero.

## Y si queréis otra
- Proponed una miniapp con **datos abiertos** (una tabla con una columna que predecir) y una pregunta cerrada. El docente os dice si encaja.
- Otras ideas posibles: calidad de un vino, supervivencia en el Titanic, tipo de cubierta forestal o reconocimiento de gestos.
- Más miniapps de los sprints anteriores: [S06](../S06/README.md) (datos sucios, fugas) y [S07](../S07/README.md) (fraude, abandono, precios).
