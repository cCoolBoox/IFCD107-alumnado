# 🎒 Bolsa de miniretos · S06

**Elige una miniapp, constrúyela en 50–70 minutos y enséñasela a la clase.** Sin TurisData: datos de otras historias, **sucios o con trampa**, y solo lo que ya conocéis hasta el Sprint 6 (preparar datos).

- **Cuándo:** al cerrar S06, en casa o cuando acabéis antes. **Opcional**: no entra en la rúbrica del reto.
- **Con quién:** en pareja o en equipo de tres.
- **Dónde:** en Google Colab, con un cuaderno nuevo. Cada ficha trae las celdas para copiar y pegar, **una por paso**. No hay que instalar nada.
- **Qué se ve al final:** el inventario de problemas de los datos, una tabla de modelos frente al modelo tonto y una **app** (una función que probáis con casos vuestros).

## Las miniapps

| | Miniapp | Pregunta | Datos | Nivel | Practica |
|---|---|---|---|---|---|
| 🌫️ | [01 · Calidad del aire](01_Calidad_del_aire.md) | ¿Cuánto benceno hay en el aire? | **Reales**: sensores, fechas, `-200` = «sin dato» | ⭐⭐ | Nulos, fechas, `Pipeline`, partición **temporal** |
| 🎓 | [02 · Aprobar o suspender](02_Aprobar_o_suspender.md) | ¿Aprobará este estudiante? | **Reales**: 395 estudiantes | ⭐⭐ | `ColumnTransformer`, **fuga de datos** |
| 🚗 | [03 · Coches sucios](03_Coches_sucios.md) | ¿Cuánto vale este coche de segunda mano? | Inventados, **muy sucios** | ⭐⭐⭐ | Limpieza, repetidos, línea base, euros |
| 🚲 | [04 · Bicis compartidas](04_Bicis_compartidas.md) | ¿Cuántas bicis se alquilarán a las 8:00? | **Reales**: 17 379 horas | ⭐⭐ | Columna trampa, split por calendario |

## Cómo elegir
- **Quiero ensuciarme las manos con datos feos:** 🚗 coches sucios.
- **Quiero descubrir una trampa de verdad:** 🎓 aprobar o suspender o 🚲 bicis.
- **Me interesa el medio ambiente:** 🌫️ calidad del aire.

## Las 6 reglas (valen para todas)
1. **Inventario antes de arreglar:** apuntad cada defecto de los datos (qué, cuántas filas, qué decidís).
2. **Lo que aprende de los datos (rellenar huecos, escalar) va dentro de un `Pipeline` y después de separar.** Lo que no aprende nada (arreglar textos, quitar repetidos) puede ir antes.
3. **Un modelo tonto de referencia** (siempre la media o la clase más común). Si no lo superáis, no habéis hecho nada.
4. **Preguntad por cada columna: ¿existirá cuando haya que predecir?** Si no, es una fuga: fuera.
5. **El examen (`test`) se mira una sola vez**, al final.
6. **Probad vuestra app con 3 casos propios**, incluido uno «difícil», y contad dónde falla.

## Tarjeta de cierre (4 frases, en la hoja compartida)
- **Mi app decide** ______ a partir de ______.
- **Antes de modelar tuve que** ______ (el defecto que más pesó).
- **Acierta** ______ en el examen, frente a ______ del modelo tonto.
- **No debe usarse para** ______.

## La demo (2 minutos por equipo)
- Enseñad el **defecto más tramposo** que encontrasteis y qué pasaba si no se arreglaba.
- Enseñad la app con **un caso que acierta** y **uno que falla**.
- Una pregunta de la clase y, después, la siguiente.

## Qué datos hay detrás
- **En el repositorio del curso** (`datos/`): `aire_calidad.csv`, `estudiantes_mates.csv` y `bicis_horas.csv`, **reales de UCI** (licencia CC BY 4.0, sin tocar), y `coches_sucio.csv`, **inventado**.
- Los datos de estudiantes son **de personas reales**: úsalos para aprender y nunca para etiquetar a nadie.

## Para subirlo (opcional)
- Descargad el cuaderno de Colab (*Archivo → Descargar → .ipynb*) y subidlo a `sprint-06/miniretos/` de vuestro repositorio, con la tarjeta de cierre en un `README.md`.
- Es práctica extra: no se evalúa con la rúbrica, pero se puede enseñar en la defensa final.

## Y si queréis otra
- Proponed una miniapp con **datos abiertos reales** (una tabla con una columna que predecir) y un defecto que os llame la atención. El docente os dice si encaja.
