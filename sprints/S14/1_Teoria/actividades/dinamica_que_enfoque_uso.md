# Dinámica · ¿Qué enfoque uso? (15 min)

**Sprint 14, jueves 26/11** · Justo antes de rellenar la ficha del proyecto: elegir **el tipo de solución** antes de elegir el modelo.

**Idea clave:** el enfoque no depende de lo moderno que sea el modelo, sino de **tres preguntas**: qué **dato** tienes (tabla, imágenes, texto, serie), **cuántos** hay y si hay que **explicar** cada decisión. Y a veces la respuesta es **«no hace falta IA»**.

## Qué hacéis

| Tiempo | Qué se hace |
|---|---|
| 2 min | Abrid el laboratorio **¿Qué enfoque uso?** del [Diccionario visual de IA](../../../../material/Diccionario_visual_IA.html#lab-enfoque) (también online) y probad los selectores con vuestro brief |
| 6 min | En subgrupos de 2-3, **clasificad los 7 casos** de abajo. Una persona lee, el subgrupo decide y comentáis el porqué antes de elegir |
| 4 min | Corregid en el laboratorio (sección «Repaso»). Para cada fallo, decid **qué pregunta os habéis saltado**: dato, cantidad o explicación |
| 3 min | Aplicad lo mismo a **vuestro brief** y apuntad el enfoque elegido en la **ficha del proyecto** (apartado 6, «Enfoque elegido y por qué») |

## Los 7 casos de TurisData

Opciones: **reglas sencillas (sin IA)** · **ML clásico en tabla** · **red neuronal densa (MLP)** · **CNN con transfer learning** · **no supervisado** · **TF-IDF + modelo clásico** · **Transformer / LLM (con RAG)** · **serie temporal (baseline + SARIMAX)**.

1. Predecir si una reserva se cancelará. Hay 60 000 reservas históricas con su resultado y la dirección quiere saber **por qué** una reserva tiene riesgo.
2. Clasificar fotos de habitaciones como «limpia» o «sucia». Hay 300 fotos etiquetadas.
3. Descubrir perfiles de huéspedes. Hay 8 000 fichas y nadie ha etiquetado nada.
4. Saber si una reseña es positiva o negativa y ver qué palabras pesan. Hay 500 reseñas etiquetadas.
5. Un asistente que conteste a los huéspedes con la política del hotel (un PDF de 40 páginas) y cite la fuente.
6. Prever la ocupación de las próximas 8 semanas con tres años de histórico semanal.
7. Mandar un aviso al huésped 48 horas antes de que caduque la cancelación gratuita.

## Para la ficha

- **Mi dato es…** (tabla, imágenes, texto o serie) y **hay… datos**.
- **Enfoque elegido y por qué:** una frase con las tres preguntas.
- **Baseline con el que empiezo** y **cuándo subiría de nivel** (por ejemplo, de regresión logística a un ensemble, o a un MLP, solo si gana con margen claro).
- Chuleta completa: sección «¿Qué enfoque uso?» del [Atlas de algoritmos](../../../../material/6.%20Atlas_de_algoritmos.md).
