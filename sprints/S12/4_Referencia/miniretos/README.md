# 🎒 Bolsa de miniretos · S12 · «Crea tu IA»

## 🔟 El decálogo
1. **No se puede usar IA** (ni chatbots ni asistentes de código): el código lo pegáis de la ficha y lo entendéis entre todos.
2. **5 minutos para elegir** miniapp. Pasado ese tiempo, empieza el reloj.
3. **55 minutos como máximo** para construirla. Si no llegáis a todo, enseñad lo que tengáis.
4. **Un modelo de referencia muy simple** (la clase más común, «mañana = hoy», una recta). Si vuestra red no lo supera, **tenéis que explicar por qué**.
5. **Separad antes de nada.** En series, **por fecha** (lo último es el examen). El examen se mira **una sola vez**, al final.
6. **Comparad al menos 3 enfoques, y uno de ellos no neuronal** (regresión, bosque, Naive Bayes…). Una red no es mejor por ser red.
7. **Una red no da siempre el mismo número:** fijad la semilla, repetid **3 veces** y mirad la **curva de aprendizaje** (¿sobreajusta?, ¿cuándo paró?).
8. **Medid en unidades reales** y decidid el umbral (o el «no sé») **con la validación**, nunca con el examen.
9. **Probad vuestra app con 3 casos propios** y contad dónde falla.
10. **Rotad el teclado:** en pareja o en trío, quien escribe cambia cada 10 minutos y todos sabéis explicar cada celda.

## 📦 Qué entregar
Una carpeta `sprint-12/miniretos/` en el repositorio de vuestro equipo con **dos archivos**:
- **El cuaderno** de Colab, ejecutado y sin errores (*Archivo → Descargar → .ipynb*).
- **Un `README.md`** con:
  - La miniapp elegida y quién la hizo.
  - La **tarjeta de cierre** (4 frases):
    - **Mi IA decide** ______ a partir de ______.
    - **Se equivoca** ______ (en unidades reales), frente a ______ del modelo de referencia.
    - **Falla cuando** ______.
    - **No debe usarse para** ______.
  - La **tabla de modelos** del duelo, con el campeón marcado y **si la red ganó o no**.
  - Los **3 casos** que probasteis con la app y **dónde falló**.
- Es práctica extra: **no entra en la rúbrica**, pero se puede enseñar en la defensa final.

## 🎤 Qué hacer en la demo (2 minutos por equipo)
- Enseñad el **gráfico clave** (la curva de aprendizaje, el histograma de errores o la serie) y explicadlo en una frase.
- Enseñad la app con **un caso que acierta** y **uno que falla**.
- Decid en una frase **si la red mereció la pena** frente al modelo sencillo.
- Una pregunta de la clase y, después, la siguiente.

## 🧰 Las miniapps
**Creáis una IA de verdad:** la entrenáis vosotros, la medís y la ponéis a prueba. Aquí se usa todo lo del bloque de redes (S10), visión (S11) y lenguaje, series y modelos generativos (S12).

- **Con quién:** en pareja o en equipo de tres.
- **¿No sabes qué algoritmo elegir?** Mira el [flujograma de decisión](../../../S08/4_Referencia/miniretos/Flujograma_que_algoritmo_uso.pdf) (se imprime en una hoja).
- **Dónde:** en Google Colab, con un cuaderno nuevo. Cada ficha trae las celdas para copiar y pegar, **una por paso**. No hay que instalar nada.
- **Qué se ve al final:** una curva o un gráfico, una tabla de modelos frente al de referencia y una **app** (una función que probáis con casos vuestros).

| | Miniapp | Pregunta | Lo que verás | Nivel | Practica |
|---|---|---|---|---|---|
| 👕 | [01 · De la red a la CNN](01_Ropa_de_la_red_a_la_CNN.md) | ¿Qué red reconoce mejor la ropa? | Cuatro «escalones» (SVM, red, CNN, transfer) **muy parejos** | ⭐⭐⭐ | S10 y S11: red densa, dropout, CNN, transfer learning |
| 📷 | [02 · ¿Qué ves en la foto?](02_Que_ves_en_la_foto.md) | ¿Qué ve una IA en **tu** foto? | Una red famosa que **se equivoca con mucha seguridad**; y la tuya, con 15 fotos | ⭐⭐ | S11: CNN ya entrenada, transfer learning |
| 🚑 | [03 · ¿Gana la red al bosque?](03_Red_contra_bosque_en_el_triaje.md) | ¿Es urgente este paciente? | **La red NO gana al bosque**, pero sí a la logística | ⭐⭐ | S10: red en Keras, curvas, dropout, semillas |
| 💬 | [04 · Mensajes de soporte](04_Mensajes_de_soporte.md) | ¿A qué departamento va este mensaje? | Acierto ≈ 0,88 y **errores en mensajes de dos temas** | ⭐⭐ | S12: TF-IDF, Naive Bayes, logística, LSA |
| 📚 | [05 · Asistente de normas](05_Asistente_de_normas.md) | ¿Qué dice el reglamento? | Un asistente que **cita el apartado** y a veces dice «no lo sé»… o se equivoca | ⭐⭐⭐ | S12: buscar con TF-IDF y coseno, mini-RAG |
| 🚲 | [06 · Bicis de mañana](06_Bicis_de_manana.md) | ¿Cuántas bicis habrá mañana? | **La GRU pierde** contra una recta con los últimos días | ⭐⭐⭐ | S12: series, ventanas, GRU |
| 🕵️ | [07 · Cazar fraude sin verlo](07_Cazar_fraude_sin_ejemplos_de_fraude.md) | ¿Esta compra es rara? | Un autoencoder que **gana a lo simple y pierde contra el supervisado** | ⭐⭐⭐ | S12: autoencoder, error de reconstrucción |

- **Lo normal es que la red no gane siempre.** Eso **no es un fallo**: es lo que hay que aprender a ver y a contar con datos.
- La miniapp 05 **no genera texto**: solo busca y cita frases del reglamento. Por eso no se inventa nada (y puede decir «no sé»).

## Qué datos hay detrás
- **En el repositorio del curso** (`datos/`): `mensajes_soporte.csv`, `normas_biblioteca.md` y `preguntas_biblioteca.csv` (**inventados** para estas fichas), y los ya conocidos `triaje_urgencias.csv`, `fraude_tarjeta.csv` (inventados) y `bicis_horas.csv` (UCI, CC BY 4.0). Más detalle en [`datos/README.md`](../../../../datos/README.md).
- Las imágenes **no están en el repositorio**: la ropa (Fashion-MNIST) y la red de visión se descargan al ejecutar la ficha. La primera vez tarda un poco.

## Y si queréis otra
- Proponed una miniapp con **datos abiertos** y una pregunta cerrada, y la red que queráis. El docente os dice si encaja.
