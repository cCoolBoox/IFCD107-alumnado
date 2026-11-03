# Apuntes del Sprint 1 · Qué es la IA, cómo aprende y cómo usarla con responsabilidad

Las diapositivas del Sprint 1 (S01_01 a S01_04) son un esquema muy comprimido. Estos apuntes **cuentan lo mismo con calma**, con ejemplos de TurisData y sin dar nada por sabido. Léelos antes de las dinámicas o cuando una palabra te suene rara. No hay que memorizar: hay que **entender para qué sirve cada idea**.

No hace falta saber programar ni matemáticas para seguirlos.

---

## 0. De qué va el sprint (en 1 minuto)

Este sprint responde a cuatro preguntas, una por cada presentación:

| Presentación | Pregunta | Idea clave |
|---|---|---|
| **S01_01** Introducción a la IA | ¿Qué es la IA y qué puede (y no puede) hacer? | IA ≠ magia: aprende patrones de datos |
| **S01_02** Algoritmos y CRISP-DM | ¿Qué tipos de problemas hay y cómo se organiza un proyecto? | Primero el problema, después el algoritmo |
| **S01_03** Tipos de aprendizaje | ¿Cómo aprende un modelo y cómo sé si lo hace bien? | Hay que evaluar con datos que no ha visto |
| **S01_04** IA responsable | ¿Qué puede salir mal con las personas y la ley? | Sesgo, privacidad, RGPD y AI Act |

**El reto:** elegir casos de uso de IA para TurisData y **analizarlos con una lista de comprobación ética**, decidiendo cuáles son recomendables y cuáles no.

---

# DÍA 1 · Qué es la IA y cómo se organiza un proyecto

## 1. ¿Qué es la IA, en lengua normal?

Hay dos formas de definirla:

| Definición | Qué dice |
|---|---|
| **Clásica** | Un sistema que hace tareas que, si las hiciera una persona, requerirían inteligencia (razonar, aprender, percibir, decidir) |
| **Operativa** (la que usaremos) | Algoritmos que **aprenden patrones a partir de datos** para predecir, clasificar o generar contenido, **sin que nadie programe cada caso** |

**Lo que NO es:** no entiende, no siente, no tiene conciencia. Es una herramienta potente con límites claros. Cuando un chatbot dice «lo siento», no lo siente: ha aprendido que esa frase encaja ahí.

### El mapa: muñecas rusas

Los términos se confunden mucho porque **unos están dentro de otros**:

```
IA  (el campo completo, incluye reglas escritas a mano)
 └── Machine Learning  (aprende de ejemplos, no de reglas)
      └── Deep Learning  (redes neuronales profundas, muchos datos)
           └── IA generativa  (crea texto, imagen, audio, código: GPT, etc.)
```

- Un **antivirus con una lista de reglas escritas a mano** es IA, pero **no** es machine learning.
- Un **filtro de spam que aprende de millones de correos** es machine learning.
- **ChatGPT** es deep learning y además generativa.

### Débil, general y superinteligencia

| Tipo | Estado hoy |
|---|---|
| **IA débil** | Es **todo lo que existe**: muy buena en una tarea concreta (traducir, reconocer caras…) |
| **IA general (AGI)** | Hipotética: una IA que haría cualquier tarea intelectual humana |
| **Superinteligencia** | Especulativa |

Cuando oigas «la IA va a dominar el mundo», recuerda: lo que hay hoy es IA débil.

## 2. Veranos e inviernos (por qué importa la historia)

La IA ha vivido ciclos de **entusiasmo (verano)** y **desencanto (invierno)**:

| Época | Qué pasó |
|---|---|
| 1950-60 | Turing, Dartmouth: optimismo sin límites |
| 1970 | **Primer invierno:** poca potencia, se acaba la financiación |
| 1980-90 | Sistemas expertos (reglas a mano); **segundo invierno** al escalar mal |
| 2012 | **Deep learning**: AlexNet gana el concurso ImageNet gracias a las tarjetas gráficas (GPU) y muchos datos |
| 2022-hoy | La IA generativa llega al gran público |

**Para qué sirve saberlo:** para tener **expectativas realistas**. Cada ola prometió más de lo que cumplió a corto plazo.

## 3. Modalidades: qué percibe y qué genera la IA

| Modalidad | Ejemplo |
|---|---|
| **Visión** | Detectar objetos, imagen médica |
| **Lenguaje** | Traducir, resumir, chatbots |
| **Voz** | Transcribir, asistentes |
| **Recomendación** | Netflix, Spotify, actividades para turistas |
| **Datos tabulares y series** | Predecir ocupación o cancelaciones (**lo que más haremos en el curso**) |
| **Generativa** | Crear texto, imagen, audio, código |
| **Robótica** | Percibir el entorno y adaptar la conducta |

Muchos sistemas mezclan varias (un asistente de voz: voz + lenguaje + generativa).

**Casos en Canarias:** chatbots multiidioma y predicción de ocupación en turismo; mantenimiento predictivo en puertos; visión para la calidad del plátano y el tomate; clasificación de expedientes y atención ciudadana en la administración; tutores adaptativos y detección de abandono en educación; diagnóstico asistido por imagen y triaje en salud.

## 4. Tres mitos y los límites reales

| Mito | Realidad |
|---|---|
| «La IA lo entiende todo» | **Asocia patrones**; no comprende el significado |
| «La IA es objetiva» | **Hereda los sesgos de los datos** con los que aprendió |
| «Sustituirá todos los empleos» | **Automatiza tareas**, no profesiones; exige supervisión humana |

**Límites reales:** *alucinaciones* (inventa cosas con mucha seguridad), depende de datos de calidad, es una *caja negra* (a veces no sabemos por qué decide algo), consume mucha energía y **no tiene sentido común** fuera de lo que vio al entrenar.

## 5. Qué necesita un proyecto de IA

No es solo «un modelo»:

| Necesita | Por qué |
|---|---|
| **Datos** suficientes, relevantes, limpios y representativos | Sin ellos el modelo es inútil o sesgado |
| **Personas**: técnicas y expertas del negocio | Hay que entender el problema, no solo programar |
| **Infraestructura** (cómputo, plataformas, MLOps) | Para entrenar, desplegar y vigilar el modelo |
| **Cambio organizativo** (liderazgo, formación, cultura de probar) | Un proyecto técnicamente bueno puede fracasar si nadie lo usa |

## 6. Reglas frente a aprendizaje

La diferencia fundamental:

| Programación tradicional | Aprendizaje automático |
|---|---|
| **Tú escribes las reglas** | **La máquina deduce las reglas** de los ejemplos |
| Entrada + reglas → salida | Entrada + salida esperada → reglas aprendidas |
| Frágil ante lo imprevisto | Se adapta a patrones nuevos |
| «Si el correo contiene *premio*, es spam» | Aprende spam de millones de correos |

La clave es que el sistema **generaliza**: aprende del pasado para predecir casos que **no ha visto**.

## 7. Las familias de algoritmos

| Familia | Cuándo | Ejemplo | ¿Etiquetas? |
|---|---|---|---|
| **Supervisado** | Hay datos con la respuesta conocida y quieres predecir | Cancelaciones, fraude | Sí |
| **No supervisado** | No hay respuestas; buscas estructura | Agrupar clientes | No |
| **Por refuerzo** | Un agente prueba acciones y recibe premios o castigos | Robótica, juegos | Recompensas |
| **Semisupervisado** | Pocas etiquetas y muchos datos sin etiquetar | Texto médico parcial | Pocas |

Dentro de lo supervisado hay **dos tipos de problema**, y confundirlos es el error más frecuente:

| | Pregunta | Salida | Ejemplo TurisData |
|---|---|---|---|
| **Clasificación** | ¿De qué tipo es? ¿Sí o no? | Una **categoría** | ¿Esta reserva se cancelará? (sí/no) |
| **Regresión** | ¿Cuánto? | Un **número** | ¿Cuántos euros ingresará mañana? |

**Truco:** si la respuesta es «sí/no» o una clase → clasificación. Si es una cantidad que puede tener decimales → regresión.

## 8. Instancias, características y etiquetas

Imagina una tabla de reservas de TurisData:

| canal | tarifa | antelacion_dias | **cancelada** |
|---|---|---|---|
| web | flexible | 45 | no |
| agencia | no reembolsable | 3 | no |
| web | flexible | 60 | **sí** |

- **Instancia** = cada **fila** (una reserva).
- **Característica (feature)** = cada **columna** que describe la fila (canal, tarifa, antelación).
- **Etiqueta (label)** = la **respuesta que queremos aprender** (`cancelada`). Solo existe en el aprendizaje supervisado.

**Regla importante:** la calidad de la etiqueta marca el **techo del modelo**. Si las etiquetas están mal, ningún algoritmo lo arregla.

## 9. CRISP-DM: las seis fases de un proyecto de datos

Es el «manual de ruta» estándar:

```
 1. Comprensión del negocio  →  2. Comprensión de los datos  →  3. Preparación
              ↑                                                        ↓
 6. Despliegue  ←  5. Evaluación  ←  4. Modelado
```

| Fase | Qué se hace |
|---|---|
| 1. Negocio | ¿Qué decisión mejorará el modelo? ¿Cómo se mide el éxito? |
| 2. Datos | Recopilar, explorar y comprobar la calidad |
| 3. Preparación | Limpiar, transformar, unir tablas (**60-80 % del tiempo**) |
| 4. Modelado | Elegir, ajustar y comparar algoritmos |
| 5. Evaluación | ¿Cumple los objetivos del **negocio** (no solo la métrica)? |
| 6. Despliegue | Ponerlo en producción y vigilarlo |

**No es lineal**: se vuelve atrás muchas veces. Y es un **ciclo**: el despliegue genera datos y necesidades nuevas.

### Del problema de negocio al problema de ML

Es el paso donde más gente se equivoca. Ejemplo en TurisData:

| Paso | Ejemplo |
|---|---|
| **Problema de negocio** | «Reducir las habitaciones vacías por cancelaciones de última hora» |
| **Traducción a ML** | Clasificación binaria: ¿esta reserva se cancelará? |
| **Variable objetivo** | `cancelada` (0 / 1) |
| **Métrica de éxito** | Detectar las cancelaciones (exhaustividad o *recall*) sin saturar de falsas alarmas |

Una mala traducción **invalida todo el trabajo posterior**, aunque el modelo sea excelente.

### Cómo elegir un algoritmo

Se mira: **cuántos datos** hay (los modelos complejos necesitan más), **explicabilidad** (¿hay que justificar decisiones?), y **coste/tiempo** (¿en tiempo real o por lotes?). Rara vez se maximizan exactitud, explicabilidad y coste a la vez.

> **Regla de oro:** empieza por el modelo **más simple** que pueda resolver el problema.

### Por qué fracasan los proyectos de IA

Según el informe de RAND (2024), **más del 80 %** de los proyectos de IA fracasan: no llegan a producción o no dan el valor esperado, **y casi nunca por motivos técnicos**:

1. Problema mal definido o sin métrica de negocio.
2. Datos insuficientes, sesgados o mal gestionados.
3. El modelo no se integra en el trabajo real; nadie lo adopta.
4. No hay plan de vigilancia tras desplegar.
5. Se usó IA donde bastaban reglas sencillas.

---

# DÍA 1 · Cómo aprenden los modelos y cómo evaluarlos

## 10. Los tipos de aprendizaje

| Tipo | Idea | Algoritmos del curso | Sprint |
|---|---|---|---|
| **Supervisado** | Ejemplos con respuesta conocida | Regresión lineal y logística, k-NN, Naive Bayes, árboles, ensembles, SVM, redes | 7-8, 10 |
| **No supervisado** | Sin etiquetas: busca estructura | k-means, clustering jerárquico, PCA | 9 |
| **Por refuerzo** | Recompensas por actuar bien | Q-learning | 9 |
| **Autosupervisado / preentrenado** | Aprende de datos sin etiquetas (por ejemplo, **adivinar la palabra que falta**) y luego se ajusta | Transformers, LLM | 12 |

**Supervisado, con una imagen:** es como estudiar con **un libro de ejercicios con soluciones**. El modelo ve pares (X, y), predice, compara con la solución y **ajusta sus parámetros para equivocarse menos**.

**No supervisado:** te dan 1.000 fichas de clientes **sin decir nada** y te piden que las ordenes en montones parecidos. Eso es *clustering*. También existe *reducción de dimensión*: resumir muchas variables en pocas.

**Por refuerzo:** como entrenar a un perro con premios. El agente prueba, recibe recompensa o castigo y aprende una *política* (qué hacer en cada situación).

> Si vas a entrenar con datos **vuestros ya etiquetados**, es aprendizaje **supervisado**, aunque el modelo parta de uno preentrenado.

## 11. Entrenamiento, validación y test: el examen justo

Para saber si un modelo aprende **de verdad** (y no solo se ha aprendido las respuestas de memoria) se reparten los datos en tres grupos:

| Conjunto | Para qué | Cuándo se usa |
|---|---|---|
| **Entrenamiento** | El modelo ajusta sus parámetros | Siempre |
| **Validación** | Comparar modelos y ajustar *hiperparámetros* (los «botones» del algoritmo) | Durante el desarrollo |
| **Test** | Medir el rendimiento final | **Una sola vez**, al final |

**Analogía del examen:**

- **Entrenamiento** = los ejercicios con los que estudias.
- **Validación** = los simulacros para ver si vas bien.
- **Test** = el examen real. **Si lo ves antes para decidir cosas, deja de ser un examen**: es un ejercicio que ya has visto.

Con **datos temporales** (reservas por fecha) se entrena con lo **antiguo** y se evalúa con lo **reciente**: no se puede usar el futuro para predecir el pasado.

## 12. Sobreajuste e infraajuste

Son los dos errores clásicos:

| | **Infraajuste** (underfitting) | **Sobreajuste** (overfitting) |
|---|---|---|
| Qué pasa | Modelo demasiado simple | Modelo demasiado ajustado: **memoriza el ruido** |
| En entrenamiento | Va mal | Va **muy bien** |
| Con datos nuevos | Va mal | Va **mal** |
| Remedio | Modelo más flexible, mejores variables | Más datos, simplificar, regularizar, validación cruzada |

**Ejemplo numérico:**

```
Modelo A:  entrenamiento 62 %,  validación 60 %   → infraajuste (flojo en todo)
Modelo B:  entrenamiento 99 %,  validación 70 %   → SOBREAJUSTE (memoriza)
Modelo C:  entrenamiento 85 %,  validación 83 %   → bien equilibrado
```

**La señal de alarma:** una gran diferencia entre entrenamiento y validación (en B: 99 − 70 = **29 puntos**). Se dice también *sesgo alto = infraajuste* y *varianza alta = sobreajuste*.

**Analogía:** un alumno que memoriza las respuestas del libro (sobreajuste) saca 10 en los ejercicios y suspende cuando cambian los números.

## 13. Evaluar: exactitud y matriz de confusión

### La exactitud (accuracy) y su trampa

**Exactitud = aciertos ÷ total.** Parece perfecta, pero **engaña cuando la clase importante es rara**.

Imagina 100 reservas, de las que solo **5 se cancelan**. Un «modelo» que **siempre dice que no cancela**:

```
Aciertos = 95 (las 95 que no cancelan)   →   exactitud = 95/100 = 95 %
Cancelaciones detectadas = 0 de 5
```

Parece excelente (95 %) **y es completamente inútil**: no detecta ninguna cancelación.

### La matriz de confusión

Es una tabla que cuenta **cómo acierta y cómo se equivoca**:

| | Predice: no cancela | Predice: cancela |
|---|---|---|
| **Real: no cancela** | Acierto (VN) | **Falsa alarma** (FP) |
| **Real: cancela** | **Cancelación no detectada** (FN) | Acierto (VP) |

Ejemplo con otro modelo sobre esas mismas 100 reservas (5 cancelan):

```
VP = 4  (cancelaciones detectadas)      FN = 1  (cancelación que se le escapó)
FP = 6  (falsas alarmas)                VN = 89 (no cancelan y acertó)

Total: 4 + 1 + 6 + 89 = 100  ✓
Exactitud = (4 + 89) / 100 = 93 %       ← MENOS que el modelo inútil (95 %)
Recall    = 4 / (4 + 1)    = 80 %       ← detecta 4 de cada 5 cancelaciones
Precisión = 4 / (4 + 6)    = 40 %       ← de cada 10 avisos, 4 son ciertos
```

Fíjate: **tiene peor exactitud (93 % < 95 %) y es muchísimo más útil**. Por eso se mira siempre la matriz y se compara con un **modelo de referencia muy simple** (baseline).

> Métricas más finas (precisión, exhaustividad o *recall*, AUC) se ven en los Sprints 6, 7 y 13. Aquí basta con entender **por qué la exactitud sola no sirve**.

---

# DÍA 2 · IA responsable: ética, sesgo y normativa

## 14. Casos que salieron mal

| Caso | Qué pasó |
|---|---|
| **COMPAS** (EE. UU., 2016) | Software que predecía riesgo de reincidencia. ProPublica comparó sus puntuaciones con lo que pasó después: entre quienes **no** volvieron a delinquir, marcó como riesgo alto al **45 %** de los acusados negros y al **23 %** de los blancos |
| **Amazon, selección de CV** (2018) | Se retiró: **penalizaba a las candidatas** porque aprendió de diez años de contrataciones mayoritariamente masculinas |
| **Reconocimiento facial** | Errores muy distintos según el grupo: **34,7 %** en mujeres de piel oscura frente a **0,8 %** en hombres de piel clara (estudio *Gender Shades*, de Buolamwini y Gebru, 2018, con tres sistemas comerciales: error de **hasta** 34,7 % en un caso y **nunca más de** 0,8 % en el otro) |

**Qué tienen en común:** resultados discriminatorios, con **datos históricos sesgados** y nadie midió la equidad antes de desplegar. El algoritmo no «es racista»: **reproduce lo que había en los datos**.

## 15. Los cuatro pilares éticos

| Principio | En una frase |
|---|---|
| **Beneficencia** | Debe dar un beneficio real y medible |
| **No maleficencia** | Minimizar daños, también los no intencionados |
| **Autonomía** | Sin manipular ni forzar a las personas |
| **Justicia** | Beneficios y riesgos repartidos con equidad |

**¿Quién responde si falla?** La cadena es larga (quien desarrolla, quien vende, quien usa). El AI Act distingue **proveedor** (quien lo crea) y **responsable del despliegue** (quien lo pone en uso). Si la responsabilidad se reparte sin cuidado, **acaba siendo de nadie**.

## 16. Gobernanza de datos: el ciclo de vida

| Etapa | Preguntas clave |
|---|---|
| **1. Recopilación** | ¿De dónde viene? ¿Hay consentimiento? ¿Es legal? ¿Representa a todos? |
| **2. Almacenamiento** | ¿Seguro? ¿Cifrado? ¿Quién accede? |
| **3. Procesamiento** | Limpieza, **anonimización** |
| **4. Uso** | ¿Para la finalidad declarada? ¿Solo los datos necesarios? |
| **5. Eliminación** | ¿Plazos? ¿Derecho al olvido? |

Y siempre: **calidad e integridad**, **privacidad por diseño** (se piensa desde el principio, no al final) y **trazabilidad** (poder saber qué se hizo con cada dato).

## 17. De dónde sale el sesgo

El sesgo **no aparece en un solo sitio**: se acumula a lo largo de todo el proceso.

| Origen | Ejemplo |
|---|---|
| **Datos** | Poca representación de un grupo; datos históricos discriminatorios; *sesgo de supervivencia* (solo vemos a quien «sobrevivió») |
| **Etiquetas** | Quien etiqueta tiene estereotipos; categorías ambiguas |
| **Modelo** | Variables que actúan de **proxy**: el código postal puede «adivinar» el origen o los ingresos aunque no pongas esa variable |
| **Uso** | El modelo decide → cambia el comportamiento → genera datos nuevos sesgados (**bucle de retroalimentación**) |

**Ejemplo del bucle:** un modelo manda más policía a un barrio → se detectan más delitos allí → los datos dicen que ese barrio es «más peligroso» → el modelo manda aún más policía.

## 18. Equidad y explicabilidad

- **Equidad:** hay **varias definiciones** (paridad demográfica, igualdad de oportunidades, calibración) y **no se pueden cumplir todas a la vez** si los grupos tienen tasas distintas. Se elige según el contexto, y esa elección es una decisión humana.
- **Transparencia:** se puede examinar el sistema. **Explicabilidad (XAI):** se puede comunicar **por qué** decidió algo. Técnicas: LIME, SHAP, mapas de saliencia, árboles «sombra».
- **Derechos de las personas:** información y acceso, rectificación y olvido (RGPD, arts. 13 a 17) e **intervención humana** en las decisiones automatizadas (art. 22).

## 19. RGPD y LOPDGDD en lo esencial

| Principio | Qué implica en un proyecto de IA |
|---|---|
| **Limitación de finalidad** | No reutilizar datos para entrenar con otros fines sin base legal |
| **Minimización** | ¿Hace falta **de verdad** cada variable? Si no, no se recoge |
| **Art. 22** | No decidir **solo con automatización** cuando hay efectos jurídicos relevantes |
| **EIPD** | Evaluación de impacto **antes** de desplegar tratamientos de alto riesgo |

En España: figura del **DPD** (delegado de protección de datos), sanciones de hasta **20 M€ o el 4 %** de la facturación mundial anual, la cifra que sea mayor, en las infracciones más graves (RGPD, art. 83), y la **AEPD** como autoridad (guías en aepd.es).

## 20. AI Act: cuatro niveles de riesgo

La norma europea de IA clasifica los sistemas por riesgo:

| Nivel | Qué ocurre | Ejemplos |
|---|---|---|
| **Inaceptable** | **Prohibido** | Puntuación social, manipulación subliminal |
| **Alto** | Obligaciones estrictas | Empleo, educación, crédito, justicia |
| **Limitado** | Transparencia | Un chatbot debe decir que es IA; los *deepfakes* se etiquetan |
| **Mínimo** | Sin obligaciones específicas | Filtros de spam |

Los sistemas de **alto riesgo** necesitan gestión de riesgos, gobernanza de datos, documentación y registros, y **supervisión humana**. Los plazos son escalonados: **consulta siempre el calendario vigente** antes de decidir.

**Calendario (Reglamento (UE) 2024/1689, comprobado en noviembre de 2026; verifícalo antes de citarlo):** entró en vigor el 1/8/2024; las prácticas prohibidas se aplican desde el 2/2/2025; los modelos de IA de uso general, desde el 2/8/2025; la mayoría de las normas, con la transparencia, desde el 2/8/2026 (el 2/12/2026, el marcado de los contenidos generados por sistemas ya comercializados y dos nuevas prohibiciones: imágenes íntimas falsas sin consentimiento y material de abuso sexual infantil); el alto riesgo de uso listado (empleo, educación, crédito…), desde el 2/12/2027, y el de productos regulados (juguetes, máquinas…), desde el 2/8/2028, tras el aplazamiento del «Ómnibus digital de IA» (Reglamento (UE) 2026/1744). Hay excepciones según el tipo de sistema y la fecha en que se comercializó, y las fechas pueden volver a cambiar.

**Multas máximas del AI Act:** 35 M€ o el 7 % de la facturación mundial anual en las prácticas prohibidas, 15 M€ o el 3 % en otras obligaciones y 7,5 M€ o el 1 % por dar información engañosa a las autoridades (siempre la cifra mayor; en las pymes, la menor). En España vigilan la **AEPD** (datos personales) y la **AESIA** (Agencia Española de Supervisión de la Inteligencia Artificial).

**Ejemplo TurisData:** un chatbot de reservas es riesgo **limitado** (avisar de que es IA). Un sistema que **filtra currículums** para contratar personal sería **alto** riesgo.

## 21. La lista de comprobación ética

En el reto rellenaréis `checklist_etico_v1.md` para cada caso de uso. Hay una ficha rápida del caso y diez bloques de preguntas:

1. **Propósito y proporcionalidad:** ¿hace falta IA?
2. **Datos y privacidad**
3. **Sesgo y equidad**
4. **Transparencia**
5. **Supervisión humana**
6. **Robustez y seguridad**
7. **Impacto social y ambiental**
8. **Normativa** (orientación)
9. **Gobernanza**
10. **Resultado:** tabla de riesgos y semáforo (verde, ámbar o rojo)

> **Un caso puede salir en rojo («no avanzar sin cambios») y eso también es un buen resultado.** Detectar a tiempo un proyecto dañino es parte del trabajo.

---

## 22. Dónde practicar cada cosa

| Si no entiendes… | Mira la sección | Practica en |
|---|---|---|
| Qué es IA, modalidades, casos de uso | 1-5 | Dinámica A: `tarjetas_casos_uso.md` |
| Clasificación frente a regresión, features y etiqueta | 7-8 | `ejemplo_clasificacion_caso.md` |
| Del problema de negocio a ML, CRISP-DM | 9 | Reto (pasos 1-2: elegir casos) |
| Entrenamiento / validación / test, sobreajuste | 11-12 | Ejercicio HTML «bueno o malo» |
| Exactitud y matriz de confusión | 13 | Ejercicios HTML de matriz de confusión |
| Sesgo, ética, casos que salieron mal | 14-18 | `casos_debate_ia_responsable.md` |
| RGPD, AI Act, lista de comprobación | 19-21 | Reto (pasos 3-5) y `checklist_etico_v1.md` |

## 23. Chuleta de vocabulario

| Palabra | En lengua normal |
|---|---|
| **Machine learning** | La máquina aprende reglas a partir de ejemplos |
| **Deep learning** | ML con redes neuronales de muchas capas |
| **IA generativa** | IA que crea contenido nuevo (texto, imagen, código…) |
| **IA débil** | Buena en una sola tarea: es toda la IA actual |
| **Alucinación** | Respuesta inventada pero dicha con seguridad |
| **Instancia** | Una fila de la tabla (un ejemplo) |
| **Característica / feature** | Una columna que describe la instancia |
| **Etiqueta / label** | La respuesta que queremos aprender |
| **Supervisado** | Con respuestas conocidas |
| **No supervisado** | Sin respuestas; busca grupos o estructura |
| **Clasificación** | Predecir una categoría |
| **Regresión** | Predecir un número |
| **Sobreajuste** | Memoriza el ruido; falla con datos nuevos |
| **Infraajuste** | Demasiado simple; falla en todo |
| **Baseline** | Modelo muy simple con el que comparar |
| **Matriz de confusión** | Tabla de aciertos y errores por tipo |
| **Sesgo (bias)** | Error sistemático que perjudica a un grupo |
| **Proxy** | Variable que «adivina» un dato sensible sin nombrarlo |
| **RGPD** | Reglamento europeo de protección de datos |
| **AI Act** | Norma europea que regula la IA según su riesgo |
| **DPD** | Delegado de protección de datos |

## 24. Cómo estudiar estos apuntes

1. **Antes de cada presentación**, lee el día correspondiente (1 o 2) a ritmo tranquilo.
2. **Haz los ejemplos numéricos a mano** (matriz de confusión, sobreajuste): son lo que más se pregunta.
3. **Antes del reto**, relee las secciones 7-9 y 14-21: son las que usarás para elegir y analizar los casos.
4. Si una palabra te bloquea, **mira la chuleta** (sección 23) y sigue; se aclara con los ejemplos.
