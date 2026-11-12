# 🎒 Bolsa de miniretos · S06

## 🔟 El decálogo
1. **No se puede usar IA** (ni chatbots ni asistentes de código): el código lo pegáis de la ficha y lo entendéis entre todos.
2. **5 minutos para elegir** miniapp. Pasado ese tiempo, empieza el reloj.
3. **55 minutos como máximo** para construirla. Si no llegáis a todo, enseñad lo que tengáis.
4. **Inventario antes de arreglar:** apuntad cada defecto de los datos (qué, cuántas filas, qué decidís).
5. **Lo que aprende de los datos (rellenar huecos, escalar) va dentro de un `Pipeline` y después de separar.** Lo que no aprende nada (arreglar textos, quitar repetidos) puede ir antes.
6. **Un modelo tonto de referencia** (siempre la media o la clase más común). Si no lo superáis, no habéis hecho nada.
7. **Preguntad por cada columna: ¿existirá cuando haya que predecir?** Si no, es una fuga: fuera.
8. **El examen (`test`) se mira una sola vez**, al final.
9. **Probad vuestra app con 3 casos propios**, incluido uno «difícil», y contad dónde falla.
10. **Rotad el teclado:** en pareja o en trío, quien escribe cambia cada 10 minutos y todos sabéis explicar cada celda.

## 📦 Qué entregar
Una carpeta `sprint-06/miniretos/` en el repositorio de vuestro equipo con **dos archivos**:
- **El cuaderno** de Colab, ejecutado y sin errores (*Archivo → Descargar → .ipynb*).
- **Un `README.md`** con:
  - La miniapp elegida y quién la hizo.
  - La **tarjeta de cierre** (4 frases):
    - **Mi app decide** ______ a partir de ______.
    - **Antes de modelar tuve que** ______ (el defecto que más pesó).
    - **Acierta** ______ en el examen, frente a ______ del modelo tonto.
    - **No debe usarse para** ______.
  - La **tabla de modelos** del duelo, con el campeón marcado.
  - Los **3 casos** que probasteis con la app y **dónde falló**.
- Es práctica extra: **no entra en la rúbrica**, pero se puede enseñar en la defensa final.

## 🎤 Qué hacer en la demo (2 minutos por equipo)
- Enseñad el **defecto más tramposo** que encontrasteis y qué pasaba si no se arreglaba.
- Enseñad la app con **un caso que acierta** y **uno que falla**.
- Una pregunta de la clase y, después, la siguiente.

## 🧰 Las miniapps
**Elige una miniapp de IA y enséñasela a la clase.** Sin TurisData: otros datos, sucios o con trampa, y solo lo que ya conocéis hasta el Sprint 6 (preparar datos).

- **Con quién:** en pareja o en equipo de tres.
- **Dónde:** en Google Colab, con un cuaderno nuevo. Cada ficha trae las celdas para copiar y pegar, **una por paso**. No hay que instalar nada.
- **Qué se ve al final:** el inventario de problemas de los datos, una tabla de modelos frente al modelo tonto y una **app** (una función que probáis con casos vuestros).

| | Miniapp | Pregunta | Datos | Nivel | Practica |
|---|---|---|---|---|---|
| 🌫️ | [01 · Calidad del aire](01_Calidad_del_aire.md) | ¿Cuánto benceno hay en el aire? | **Reales**: sensores, fechas, `-200` = «sin dato» | ⭐⭐ | Nulos, fechas, `Pipeline`, partición **temporal** |
| 🎓 | [02 · Aprobar o suspender](02_Aprobar_o_suspender.md) | ¿Aprobará este estudiante? | **Reales**: 395 estudiantes | ⭐⭐ | `ColumnTransformer`, **fuga de datos** |
| 🚗 | [03 · Coches sucios](03_Coches_sucios.md) | ¿Cuánto vale este coche de segunda mano? | Inventados, **muy sucios** | ⭐⭐⭐ | Limpieza, repetidos, línea base, euros |
| 🚲 | [04 · Bicis compartidas](04_Bicis_compartidas.md) | ¿Cuántas bicis se alquilarán a las 8:00? | **Reales**: 17 379 horas | ⭐⭐ | Columna trampa, split por calendario |

## Qué datos hay detrás
- **En el repositorio del curso** (`datos/`): `aire_calidad.csv`, `estudiantes_mates.csv` y `bicis_horas.csv`, **reales de UCI** (licencia CC BY 4.0, sin tocar), y `coches_sucio.csv`, **inventado**.
- Los datos de estudiantes son **de personas reales**: úsalos para aprender y nunca para etiquetar a nadie.

## Y si queréis otra
- Proponed una miniapp con **datos abiertos reales** (una tabla con una columna que predecir) y un defecto que os llame la atención. El docente os dice si encaja.
