# Dinámicas con tarjetas · Sprint 1

Tres actividades de práctica (4 h de práctica del sprint, repartidas entre las sesiones). Se imprimen y se recortan; **no hace falta ordenador**. Trabajad en parejas o en grupos de 3-4. Las soluciones las tiene el docente.

| Dinámica | Tiempo | Qué practicáis |
|---|---|---|
| A · Mapa de casos de uso | 1 h | Modalidad, tipo de aprendizaje y datos de 22 casos de IA |
| B · Clasificación "a mano" | 1 h | Cómo se aprende de ejemplos, el **sobreajuste** y por qué existe el conjunto de test |
| C · ¿Qué familia de algoritmos? | 1 h | Elegir una familia de algoritmos en 6 problemas |

---

# Dinámica A · Mapa de casos de uso de IA

## Instrucciones
1. Recortad las 22 tarjetas de la sección siguiente.
2. Para cada tarjeta, rellenad los cuatro campos **a lápiz** (podéis usar los apuntes de la teoría):
   - **Modalidad:** visión · lenguaje (texto) · voz · recomendación · datos tabulares/series · generativa (texto, imagen) · robótica.
   - **Tipo de aprendizaje:** supervisado · no supervisado · por refuerzo · preentrenado + ajuste (autosupervisado).
   - **Datos necesarios:** qué datos concretos harían falta y si tienen que estar **etiquetados**.
   - **¿Hace falta IA?** Sí / No / Quizá (dos tarjetas son "trampa": se resuelven mejor con reglas sencillas).
3. Después, ordenad las tarjetas en una **matriz** de dos ejes: *impacto para TurisData* (bajo-alto) y *facilidad de conseguir los datos* (difícil-fácil). Marcad las 5 candidatas a "primer proyecto".
4. Poned en común: ¿en qué tarjetas no os pusisteis de acuerdo? ¿por qué?

> Pista: un mismo caso puede tener **más de una respuesta razonable**. Lo importante es **justificarla**.

## Tabla de respuestas (hoja para el equipo)

| Nº | Modalidad | Tipo de aprendizaje | Datos necesarios | ¿Hace falta IA? |
|---|---|---|---|---|
| C01 | | | | |
| C02 | | | | |
| C03 | | | | |
| C04 | | | | |
| C05 | | | | |
| C06 | | | | |
| C07 | | | | |
| C08 | | | | |
| C09 | | | | |
| C10 | | | | |
| C11 | | | | |
| C12 | | | | |
| C13 | | | | |
| C14 | | | | |
| C15 | | | | |
| C16 | | | | |
| C17 | | | | |
| C18 | | | | |
| C19 | | | | |
| C20 | | | | |
| C21 | | | | |
| C22 | | | | |

## Tarjetas (recortar por las líneas)

```
┌─────────────────────────────────────────────┐
│ C01 · Predecir cancelaciones                │
│ Avisar a recepción de qué reservas tienen   │
│ más probabilidad de cancelarse en los       │
│ próximos días.                              │
│ Modalidad: ______ Aprendizaje: ______       │
│ Datos: ________________  ¿IA?: __           │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ C02 · Segmentar huéspedes                   │
│ Descubrir grupos de huéspedes con           │
│ comportamientos parecidos (gasto, duración, │
│ país, experiencias) sin saber de antemano   │
│ cuántos grupos hay.                         │
│ Modalidad: ______ Aprendizaje: ______       │
│ Datos: ________________  ¿IA?: __           │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ C03 · Recomendar experiencias               │
│ Sugerir a cada huésped las excursiones que  │
│ probablemente le gusten, según lo que       │
│ valoraron otros huéspedes parecidos.        │
│ Modalidad: ______ Aprendizaje: ______       │
│ Datos: ________________  ¿IA?: __           │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ C04 · Sentimiento de las reseñas            │
│ Clasificar automáticamente 1.500 reseñas    │
│ en positivas, neutras y negativas.          │
│ Modalidad: ______ Aprendizaje: ______       │
│ Datos: ________________  ¿IA?: __           │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ C05 · Temas de las quejas                   │
│ Descubrir de qué se quejan los clientes     │
│ (ruido, limpieza, wifi...) sin haber        │
│ definido antes las categorías.              │
│ Modalidad: ______ Aprendizaje: ______       │
│ Datos: ________________  ¿IA?: __           │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ C06 · Asistente sobre la política           │
│ Un asistente que responde dudas de huéspedes│
│ (mascotas, check-in, cancelación) citando   │
│ el documento oficial de política.           │
│ Modalidad: ______ Aprendizaje: ______       │
│ Datos: ________________  ¿IA?: __           │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ C07 · Clasificar fotos de alojamientos      │
│ Etiquetar automáticamente las fotos del     │
│ catálogo: dormitorio, baño, piscina,        │
│ terraza, vistas.                            │
│ Modalidad: ______ Aprendizaje: ______       │
│ Datos: ________________  ¿IA?: __           │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ C08 · Contar personas en una excursión      │
│ Estimar cuántas personas hay en la foto de  │
│ salida de un grupo para controlar aforos.   │
│ Modalidad: ______ Aprendizaje: ______       │
│ Datos: ________________  ¿IA?: __           │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ C09 · Prever la ocupación                   │
│ Estimar la ocupación de un alojamiento para │
│ cada uno de los próximos 30 días.           │
│ Modalidad: ______ Aprendizaje: ______       │
│ Datos: ________________  ¿IA?: __           │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ C10 · Precio dinámico                       │
│ Proponer el precio por noche que maximice   │
│ los ingresos según la demanda esperada.     │
│ Modalidad: ______ Aprendizaje: ______       │
│ Datos: ________________  ¿IA?: __           │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ C11 · Traducción automática                 │
│ Traducir las descripciones de los           │
│ alojamientos al alemán y al inglés.         │
│ Modalidad: ______ Aprendizaje: ______       │
│ Datos: ________________  ¿IA?: __           │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ C12 · Transcribir llamadas                  │
│ Convertir en texto las llamadas de reserva  │
│ para archivarlas y buscar en ellas.         │
│ Modalidad: ______ Aprendizaje: ______       │
│ Datos: ________________  ¿IA?: __           │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ C13 · Detectar reservas anómalas            │
│ Encontrar reservas "raras" (muchas noches,  │
│ muchas personas, pagos extraños) para       │
│ revisarlas a mano. No hay lista de fraudes  │
│ etiquetada.                                 │
│ Modalidad: ______ Aprendizaje: ______       │
│ Datos: ________________  ¿IA?: __           │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ C14 · Redactar descripciones                │
│ Generar un primer borrador de la ficha de   │
│ un alojamiento a partir de sus datos.       │
│ Una persona lo revisa antes de publicar.    │
│ Modalidad: ______ Aprendizaje: ______       │
│ Datos: ________________  ¿IA?: __           │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ C15 · Qué oferta mostrar                    │
│ Elegir, para cada visita a la web, qué      │
│ oferta enseñar y aprender de si el cliente  │
│ hace clic o no (prueba y error).            │
│ Modalidad: ______ Aprendizaje: ______       │
│ Datos: ________________  ¿IA?: __           │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ C16 · Enviar un recordatorio                │
│ Enviar un correo automático 48 horas antes  │
│ de la llegada con las instrucciones de      │
│ entrada.                                    │
│ Modalidad: ______ Aprendizaje: ______       │
│ Datos: ________________  ¿IA?: __           │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ C17 · Imágenes promocionales                │
│ Generar imágenes de paisajes de las islas   │
│ para las redes sociales.                    │
│ Modalidad: ______ Aprendizaje: ______       │
│ Datos: ________________  ¿IA?: __           │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ C18 · Check-in con reconocimiento facial    │
│ Identificar al huésped con una cámara para  │
│ entrar sin pasar por recepción.             │
│ Modalidad: ______ Aprendizaje: ______       │
│ Datos: ________________  ¿IA?: __           │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ C19 · Puntuar el riesgo del cliente         │
│ Asignar una puntuación a cada cliente para  │
│ decidir si se le pide un depósito mayor.    │
│ Modalidad: ______ Aprendizaje: ______       │
│ Datos: ________________  ¿IA?: __           │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ C20 · Clasificar el correo entrante         │
│ Etiquetar cada correo como "urgente",       │
│ "factura", "queja" o "consulta" para        │
│ repartirlo al equipo adecuado.              │
│ Modalidad: ______ Aprendizaje: ______       │
│ Datos: ________________  ¿IA?: __           │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ C21 · Robot de equipajes                    │
│ Un robot que lleva las maletas desde        │
│ recepción a la habitación por los pasillos  │
│ de un hotel.                                │
│ Modalidad: ______ Aprendizaje: ______       │
│ Datos: ________________  ¿IA?: __           │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ C22 · Calcular el IVA de la factura         │
│ Calcular el impuesto de cada factura según  │
│ el tipo aplicable.                          │
│ Modalidad: ______ Aprendizaje: ______       │
│ Datos: ________________  ¿IA?: __           │
└─────────────────────────────────────────────┘
```

---

# Dinámica B · Clasificación "a mano": aprender de ejemplos y sobreajuste

**Objetivo:** vivir en papel lo que hace un modelo: buscar reglas en unos datos de **entrenamiento** y comprobar si funcionan con datos **nuevos** (test).

**Tarea:** predecir si una reserva **se cancela** (Sí/No).
Variables: **T** = tarifa (F = flexible, NR = no reembolsable) · **A** = antelación de la reserva en días · **N** = noches · **C** = canal (D = directo, I = intermediaria). Los datos son inventados para practicar.

## Paso 1 · Datos de entrenamiento (16 reservas)
Tenéis 8 minutos. Buscad **una regla** que clasifique bien el mayor número posible de reservas.

| Id | T | A | N | C | ¿Cancela? |
|---|---|---|---|---|---|
| E1 | F | 90 | 4 | I | Sí |
| E2 | F | 75 | 7 | D | Sí |
| E3 | F | 60 | 3 | I | Sí |
| E4 | F | 50 | 5 | D | Sí |
| E5 | F | 20 | 4 | D | No |
| E6 | F | 10 | 2 | I | No |
| E7 | F | 30 | 6 | D | No |
| E8 | NR | 90 | 5 | I | No |
| E9 | NR | 70 | 7 | D | No |
| E10 | NR | 40 | 3 | I | No |
| E11 | NR | 15 | 4 | D | No |
| E12 | NR | 120 | 10 | I | Sí |
| E13 | F | 55 | 2 | D | No |
| E14 | F | 80 | 6 | I | Sí |
| E15 | NR | 25 | 3 | I | No |
| E16 | F | 15 | 7 | D | No |

## Paso 2 · Vuestra regla y su nota en entrenamiento
- **Regla A (la más sencilla que se os ocurra):** "Cancela si ______________________________"
- Aciertos de la Regla A en entrenamiento: ____ de 16
- **Regla B (mejorad la anterior hasta acertar las 16, añadiendo excepciones si hace falta):**
  "Cancela si ______________________________, salvo ______________________________"
- Aciertos de la Regla B en entrenamiento: ____ de 16

## Paso 3 · Datos de test (8 reservas nuevas)
**No las miréis hasta terminar el paso 2.** Aplicad **vuestras dos reglas** sin cambiarlas, y comprobad la última columna, que os dará el docente cuando digáis "regla lista".

| Id | T | A | N | C | Predice Regla A | Predice Regla B | Real |
|---|---|---|---|---|---|---|---|
| P1 | F | 100 | 5 | D | | | (docente) |
| P2 | F | 35 | 4 | I | | | (docente) |
| P3 | NR | 80 | 8 | I | | | (docente) |
| P4 | NR | 110 | 10 | D | | | (docente) |
| P5 | F | 52 | 2 | I | | | (docente) |
| P6 | F | 65 | 3 | D | | | (docente) |
| P7 | NR | 12 | 2 | D | | | (docente) |
| P8 | F | 40 | 7 | I | | | (docente) |

**Aciertos en test:** Regla A ____ de 8 · Regla B ____ de 8

## Paso 4 · Reflexión (en grupo)
1. ¿Qué regla funcionó mejor con los datos **nuevos**? ¿La que mejor iba en entrenamiento?
2. ¿Qué habéis hecho al añadir excepciones a la regla B? ¿Qué le pasó a la regla?
3. Aparecen dos reservas "raras" en el entrenamiento (E12 y E13). ¿Merece la pena que la regla las acierte?
4. ¿Cómo se llama en machine learning **memorizar los datos de entrenamiento**? ¿Y **una regla demasiado simple**?
5. ¿Por qué necesitamos un conjunto de **test** que el modelo no haya visto?
6. Si TurisData solo nos hubiera dado los 16 datos de entrenamiento y nada más, ¿cómo podríamos comprobar la regla antes de usarla? (pista: guardar una parte aparte).

---

# Dinámica C · ¿Qué familia de algoritmos elegimos?

Para cada problema, decid: **1)** ¿es predicción de un número, de una categoría, agrupación, recomendación, generación…? **2)** ¿qué familia de algoritmos usaríais (reglas, regresión, clasificación, clustering, árboles, ensembles, redes neuronales)? **3)** ¿qué datos necesitáis? **4)** ¿os importa poder **explicar** la decisión?

| Nº | Problema de TurisData |
|---|---|
| P1 | Estimar el **precio por noche** de un alojamiento nuevo a partir de sus características (tamaño, zona, temporada, plazas). |
| P2 | Decidir si una reserva **se cancelará o no**, con los datos de reservas de los últimos dos años. |
| P3 | Agrupar 1.200 huéspedes en **grupos con hábitos parecidos**, sin etiquetas previas. |
| P4 | Reconocer en una foto si es un **dormitorio, un baño o una piscina**; hay 20.000 fotos sin etiquetar de nadie, pero se pueden etiquetar 1.000. |
| P5 | Detectar si un huésped se ha quejado de **"ruido"** en cualquiera de las 1.500 reseñas en texto libre. |
| P6 | Calcular **cuántas limpiadoras** hacen falta un día según la ocupación prevista, si la regla es "1 por cada 6 apartamentos ocupados". |

## Tabla de respuestas

| Nº | Tipo de problema | Familia elegida | Datos necesarios | ¿Explicabilidad importante? ¿Por qué? |
|---|---|---|---|---|
| P1 | | | | |
| P2 | | | | |
| P3 | | | | |
| P4 | | | | |
| P5 | | | | |
| P6 | | | | |
