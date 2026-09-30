# Ejemplo resuelto · cómo clasificar un caso de uso de IA

Sirve de **modelo de forma** para el reto. No copiéis el contenido: elegid **vuestros** casos. Aquí clasificamos el caso **C01 · Predecir cancelaciones** (ver tarjetas) y, más abajo, una versión resumida de un segundo caso para contrastar.

## Ficha de caso de uso (plantilla)

| Campo | Contenido |
|---|---|
| **Nombre** | Aviso de riesgo de cancelación |
| **Problema de negocio** | Las cancelaciones de última hora dejan noches vacías que no se pueden volver a vender (dolor citado por la dirección: una semana vacía en La Palma). |
| **Persona usuaria** | Recepción y responsable de reservas de cada alojamiento |
| **Decisión que apoya** | Qué reservas contactar, en qué orden, y cuándo ofrecer un cambio de fechas, antes de que caduque la cancelación gratuita |
| **Modalidad** | **Datos tabulares** (una fila por reserva). No es visión, ni lenguaje, ni voz |
| **Tipo de problema** | **Clasificación binaria** (¿se cancelará? sí/no) que devuelve una **probabilidad** |
| **Tipo de aprendizaje** | **Supervisado**: hay ejemplos históricos con la respuesta correcta (columna `cancelada`) |
| **Familia de algoritmos** (a explorar) | Regresión logística como referencia; árboles y *ensembles* como candidatos; una red neuronal solo si compensa |
| **Datos necesarios** | Reservas de 2 años o más: fecha de reserva, de llegada, antelación, noches, canal, tarifa, depósito, país de origen, importe y **la etiqueta `cancelada`**. Volumen orientativo: varios miles de reservas |
| **¿Los datos están ya?** | En parte. Hay datos de reservas, pero el cliente reconoce que **no siempre están completos ni limpios** (calidad por comprobar) |
| **Métrica de negocio** | Noches vacías evitadas / ingresos recuperados |
| **Métrica técnica** | Recall de las cancelaciones (¿cuántas detectamos?) y precisión (¿cuántos avisos son correctos?) sobre un conjunto de **test** |
| **Fase CRISP-DM** en la que estamos | Comprensión del negocio y de los datos (Sprint 1). El modelado se hará en Sprints 3, 7 y 8 |
| **Riesgos técnicos** | Datos desbalanceados (pocas cancelaciones), cambios de temporada, "fuga de datos" si se usan variables que solo se conocen después de la cancelación |
| **Impacto** (1-5) | 5 |
| **Facilidad** (1-5): datos, complejidad, plazo | 4 |
| **Riesgo ético** (bajo / medio / alto) | **Medio** (ver más abajo) |

## Por qué esas respuestas (razonamiento paso a paso)

1. **¿Qué queremos predecir?** Si una reserva se cancela: una **categoría** de dos valores (sí/no). Eso es *clasificación*, no *regresión* (que predice un número).
2. **¿Tenemos la respuesta correcta en el pasado?** Sí, cada reserva histórica dice si se canceló. Por tanto, **aprendizaje supervisado**. Si no hubiese etiqueta, tendríamos que agrupar o detectar anomalías (no supervisado).
3. **¿Con qué datos?** Datos por filas y columnas (una reserva por fila), es decir, **tabulares**. No hay imágenes ni texto libre.
4. **¿Qué familia?** Con datos tabulares y pocos miles de filas suelen ir bien los modelos clásicos (logística, árboles, *ensembles*). Una red neuronal aporta poco y es más difícil de explicar. Y a la dirección le importa **poder explicar** por qué una reserva tiene riesgo.
5. **¿Qué puede fallar?** Un modelo que dice "nadie cancela" acierta el ~79 % (si cancela el 21 %) y no sirve para nada. Por eso miramos **recall y precisión**, no solo la exactitud.
6. **¿Hace falta IA?** Una regla como "las reservas flexibles con mucha antelación cancelan más" ya da una pista, pero un modelo combina muchas variables a la vez y da una probabilidad. Compensa, y además sirve de base para comparar.

## Checklist ético resumido para este caso (versión 1)

| Punto | Respuesta |
|---|---|
| Datos personales | Hay: país, fechas de estancia. **Minimizar**: no hace falta el nombre ni el correo para predecir |
| Decisión | **Apoya** a una persona; no rechaza reservas ni cambia precios solo |
| Sesgo | **Riesgo**: si se usa "país de origen" el sistema podría tratar peor a ciertas nacionalidades. **Medida**: evaluar por grupos y, si hay diferencias injustificadas, quitar la variable |
| Transparencia | Recepción ve los **motivos** principales (tarifa, antelación...) junto con la probabilidad |
| Supervisión | Una persona decide qué hacer con cada aviso; se puede desactivar |
| Normativa | RGPD/LOPDGDD: sí. AI Act: probablemente riesgo **mínimo** si solo apoya la gestión interna, pero conviene confirmarlo **[verificar calendario vigente antes de impartir]** |
| Semáforo | **Ámbar**: avanzar con la medida de evaluación por grupos |

## Priorización (extracto)

| Caso | Impacto (1-5) | Facilidad (1-5) | Riesgo ético | Prioridad |
|---|---|---|---|---|
| C01 · Predecir cancelaciones | 5 | 4 | Medio | **1** |
| C06 · Asistente sobre la política | 4 | 3 | Medio (alucinaciones) | 2 |
| C04 · Sentimiento de reseñas | 3 | 5 | Bajo | 3 |

Criterio usado: **impacto × facilidad**, y a igualdad, menor riesgo ético primero.

---

## Segundo ejemplo (resumido) · C06 Asistente que responde sobre la política del alojamiento

| Campo | Contenido |
|---|---|
| Modalidad | **Lenguaje** (texto), IA **generativa** |
| Tipo de aprendizaje | Modelo **preentrenado** (autosupervisado sobre mucho texto) + recuperación de fragmentos del documento de política (*RAG*); no se entrena de cero |
| Datos necesarios | El **documento de política** en texto, y ejemplos de preguntas reales de huéspedes para evaluarlo. No hay etiquetas |
| Familia | Modelos de lenguaje (LLM) con recuperación de documentos |
| Riesgo principal | Alucinaciones: inventar políticas que no existen. Medida: responder solo con el documento, citar la fuente y derivar a una persona si no está |
| Ético | Avisar de que es una IA; no guardar datos personales innecesarios; supervisión humana |

## Plantilla vacía (para vuestros casos)

| Campo | Vuestro caso |
|---|---|
| Nombre | |
| Problema de negocio | |
| Persona usuaria y decisión que apoya | |
| Modalidad | |
| Tipo de problema (clasificación, regresión, agrupación, generación...) | |
| Tipo de aprendizaje | |
| Familia de algoritmos | |
| Datos necesarios (fuente, etiquetas, volumen, ¿ya existen?) | |
| Métrica de negocio y métrica técnica | |
| Riesgos técnicos | |
| Impacto (1-5) · Facilidad (1-5) | |
| Riesgo ético y semáforo (checklist v1) | |
| ¿Hace falta IA? ¿Qué alternativa sin IA hay? | |
