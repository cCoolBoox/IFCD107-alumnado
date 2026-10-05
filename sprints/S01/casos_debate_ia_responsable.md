# Debate guiado de IA responsable · 5 casos

**Práctica de M8 (UD 8.4)** · Casos **ficticios** ambientados en TurisData Canarias, inspirados en problemas reales que han aparecido en empresas y administraciones de todo el mundo. **Duración:** unos 60-75 minutos con un caso por grupo (o dos casos, según tiempo).

## Cómo funciona el debate

| Fase | Tiempo | Qué se hace |
|---|---|---|
| 1. Lectura | 5 min | Cada grupo lee su caso y su rol |
| 2. Preparación | 10 min | Cada persona prepara 3 argumentos desde su rol (usad las preguntas guía) |
| 3. Debate | 20 min | Rondas: exposición (1 min por rol), réplicas y propuesta de medidas |
| 4. Decisión | 5 min | El grupo redacta una **decisión de 5 líneas**: qué se hace, qué no, qué condiciones |
| 5. Puesta en común | 10 min | Un portavoz cuenta la decisión al resto |
| 6. Cierre | 5 min | Rellenad la **checklist ética v1** ([`checklist_etico_v1.md`](checklist_etico_v1.md)) con el caso |

**Roles** (adaptad según el nº de personas; si hay 4, quitad el 5):
1. **Dirección de TurisData:** quiere resultados y ahorrar costes.
2. **Equipo de IA (la consultora):** propone y defiende la solución técnica.
3. **Persona afectada:** huésped, candidata o trabajador afectado.
4. **Asesoría legal / delegado de protección de datos:** aplica RGPD, LOPDGDD y AI Act.
5. **Voz externa:** una asociación de consumidores, un periodista o la Agencia Española de Protección de Datos.

**Reglas:**
- Defended vuestro rol, aunque no penséis lo mismo que él o ella; en la decisión final se piensa con libertad.
- Se argumenta con **hechos y criterios**, no con eslóganes.
- No hay respuesta única: buscamos **riesgos concretos y medidas concretas**.

**Marco mínimo para razonar** (lo veréis en la teoría de M8):
- **RGPD** (Reglamento general de protección de datos) y **LOPDGDD** (ley orgánica española de protección de datos): licitud, finalidad, minimización, transparencia, derechos, evaluación de impacto, decisiones automatizadas (art. 22).
- **Reglamento europeo de IA (AI Act):** clasificación por niveles de riesgo (inaceptable, alto, limitado o de transparencia, mínimo) y obligaciones para cada nivel. **[verificar calendario vigente antes de impartir]**: qué obligaciones se aplican ya y cuáles aún no.
- **Principios:** equidad, transparencia, supervisión humana, seguridad, responsabilidad.

---

## Caso 1 · Sesgo · "El preselector de personal de temporada"

**Contexto.** Cada verano TurisData contrata a unas 60 personas (camareros/as de piso, recepción, guías de excursiones). Recibe 900 currículos. Para ahorrar tiempo, un proveedor le vende un sistema de IA que **puntúa los currículos**. Se ha entrenado con los datos de las **contrataciones de los últimos 8 años**: qué candidaturas pasaron a entrevista y a quiénes se contrató.

**Lo que ocurre.** Una auditoría interna descubre que: 1) las mujeres candidatas a guía puntúan **12 puntos menos** de media que los hombres con el mismo perfil; 2) los currículos con **huecos** de más de un año se descartan casi siempre; 3) el sistema puntúa mejor a quien vive en determinados municipios del norte de Tenerife. La dirección dice: *"El sistema solo refleja lo que hemos hecho siempre; funciona."*

**Preguntas guía**
1. ¿De dónde viene el sesgo: **datos, etiquetas, variables o uso**?
2. ¿Por qué la variable "municipio" puede actuar como **variable proxy**? ¿de qué?
3. ¿Qué pasa si quitamos la variable "sexo" del modelo? ¿desaparece el problema?
4. ¿Se puede medir la equidad? Proponed una comprobación sencilla (por ejemplo, comparar tasas de preselección por grupo).
5. ¿Qué papel debe tener la persona que decide? ¿Qué información debe recibir?
6. ¿Qué derechos tienen las personas candidatas? ¿Y qué obligaciones tiene TurisData?
7. ¿En qué nivel de riesgo del AI Act se situaría un sistema de selección de personal? **[verificar calendario vigente antes de impartir]**

**Lo que buscamos:** identificar que el sesgo nace de los datos históricos y de las variables proxy, proponer auditorías por grupo y supervisión humana real, y valorar si conviene usar el sistema.

---

## Caso 2 · Privacidad y RGPD · "Los correos de los clientes"

**Contexto.** TurisData quiere predecir qué reservas se cancelarán. Para mejorar el modelo, un empleado propone **añadir el texto de los correos** que los clientes han enviado al alojamiento (consultas, quejas, datos de pago accidentales) y las **fotografías de los documentos de identidad** que se escanean al entrar. Además, para "ir más rápido", pega fragmentos de conversaciones reales en un **asistente de IA público** en internet.

**Lo que ocurre.** Entre los clientes hay personas del Reino Unido y de Alemania, y menores de edad que viajan con sus familias. Alguien recuerda que los clientes nunca fueron informados de que sus datos se usarían para **entrenar modelos**. Otro pregunta si el correo debe borrarse tras la estancia.

**Preguntas guía**
1. ¿Qué **datos personales** aparecen? ¿cuáles son especialmente delicados (menores, documentos, datos de pago)?
2. ¿Cuál es la **base legal** para tratar estos datos? ¿sirve la misma para reservar y para entrenar un modelo? (finalidad)
3. ¿Qué principio se vulnera al pegar datos en un asistente público? ¿qué riesgo hay?
4. ¿Qué datos **no hacen falta** para predecir cancelaciones? (minimización)
5. ¿Qué medidas técnicas y organizativas propondríais? (anonimizar o seudonimizar, acceso restringido, plazos de conservación, contrato con el proveedor)
6. ¿Cuándo haría falta una **evaluación de impacto** en protección de datos?
7. ¿Qué información y qué derechos debe tener el cliente (acceso, supresión, oposición)?

**Lo que buscamos:** aplicar finalidad, minimización y transparencia; distinguir datos anonimizados y seudonimizados; proponer un plan realista (empezar con datos de reserva sin texto libre).

---

## Caso 3 · Transparencia · "Lucía, la asistente que no era una persona"

**Contexto.** TurisData lanza en su web un asistente de reservas con nombre humano y foto de una supuesta empleada, "Lucía". Responde por texto en cuatro idiomas. No se indica que es una IA. Marketing celebra que "los clientes piensan que hablan con una persona".

**Lo que ocurre.** Un cliente pregunta si puede cancelar gratis una reserva de tarifa **no reembolsable**. Lucía responde con seguridad: *"Claro, le devolvemos el importe íntegro."* Es falso: el asistente ha **inventado** una respuesta (alucinación). El cliente reclama; el equipo de atención no sabe qué dijo el asistente porque **no se guardan las conversaciones**. Al investigar, descubren que el proveedor tampoco explica cómo genera las respuestas.

**Preguntas guía**
1. ¿Qué información debería recibir el usuario sobre **con quién** está hablando?
2. ¿Qué es una **alucinación** y por qué es un riesgo en atención al cliente?
3. ¿Qué **medidas técnicas** reducen el riesgo? (responder solo con documentos de política, citar la fuente, decir "no lo sé", derivar a una persona)
4. ¿Debe guardarse el historial de conversaciones? ¿con qué límites de privacidad?
5. ¿Quién es **responsable** de lo que dice el asistente? ¿TurisData, el proveedor, el modelo?
6. ¿Qué exige el AI Act en materia de **transparencia** a los sistemas que interactúan con personas? **[verificar calendario vigente antes de impartir]**
7. ¿Qué frase pondríais en la web para presentar al asistente?

**Lo que buscamos:** reconocer el derecho a saber que se habla con una IA, limitar la generación libre, registrar y supervisar, y definir la responsabilidad.

---

## Caso 4 · Deepfakes y desinformación · "La playa perfecta"

**Contexto.** Marketing de TurisData usa IA generativa para crear imágenes de sus playas y apartamentos. Las imágenes son espectaculares: **una playa de arena blanca vacía** que no existe en esa isla, terrazas con vistas al mar que el apartamento no tiene. Además, un becario ha generado **80 reseñas de cinco estrellas** con IA "para arrancar" la web, y un vídeo en el que **la directora "presenta" una promoción** con su voz clonada, sin que ella lo supiera.

**Lo que ocurre.** Un cliente se queja de que la playa "no es como en la foto" y publica una comparación en redes. Un periodista local pide explicaciones y ha detectado que las reseñas tienen un estilo idéntico. La directora se entera del vídeo por un cliente.

**Preguntas guía**
1. ¿Qué diferencia hay entre **usar IA para retocar** una foto y **crear una imagen que engaña**?
2. ¿Qué riesgos hay para los clientes, para TurisData y para el destino?
3. ¿Qué valor tiene una reseña? ¿qué problema legal y de confianza plantean las reseñas falsas?
4. ¿Qué requisitos de consentimiento deben cumplirse para usar la **voz o imagen** de una persona?
5. ¿Cómo podría TurisData usar IA generativa de forma **legítima**? (etiquetar el contenido generado, imágenes reales para el alojamiento, políticas internas)
6. ¿Qué se exige en el AI Act respecto al **contenido sintético** y a los *deepfakes*? **[verificar calendario vigente antes de impartir]**
7. ¿Qué procedimiento de **verificación** propondríais para no caer en desinformación (imágenes, textos, cifras)?

**Lo que buscamos:** distinguir uso legítimo y engañoso, proponer una política de uso de IA generativa en marketing (etiquetado, consentimiento, veracidad), y hablar de daño reputacional.

---

## Caso 5 · Decisiones automatizadas sobre personas · "El semáforo de riesgo"

**Contexto.** Para reducir cancelaciones, un sistema asigna a cada cliente un **semáforo** (verde, ámbar, rojo). Si sale rojo, el sistema **exige automáticamente el pago del 100 %** por adelantado, o **rechaza la reserva** sin intervención humana. Se ha entrenado con el historial de cancelaciones. Entre las variables hay: país de origen, tipo de tarjeta, código postal y si el nombre "suena" extranjero.

**Lo que ocurre.** Un cliente canario reserva una casa rural y recibe un rechazo automático sin explicación. Reclama y descubre que su código postal se asocia con cancelaciones altas. TurisData responde: *"Lo decide el algoritmo; no podemos cambiarlo."* Al revisar, se ve que los clientes de ciertos países reciben con más frecuencia el semáforo rojo y rechazos, aunque su historial individual es bueno.

**Preguntas guía**
1. ¿Qué **decisiones** toma el sistema y cuáles afectan de forma **significativa** al cliente?
2. ¿Qué dice el RGPD (art. 22) sobre decisiones basadas únicamente en tratamiento automatizado? ¿y qué derechos da?
3. ¿Qué variables son **inadmisibles o problemáticas** (país, apellidos, código postal)? ¿por qué?
4. ¿Cómo puede el cliente **entender** y **discutir** la decisión? ¿qué es explicabilidad?
5. ¿Qué **supervisión humana** propondríais para que no sea un "sello de goma" (revisar sin poder cambiar)?
6. ¿Es igual pedir un **depósito** que **rechazar** una reserva? ¿cómo graduaríais la respuesta?
7. ¿Qué **métricas de equidad** o comprobaciones haríais antes de poner el sistema en marcha?

**Lo que buscamos:** distinguir entre apoyo a la decisión y decisión automática, exigir una persona con capacidad real de cambiar el resultado, excluir variables discriminatorias, ofrecer explicación y vía de reclamación, y probar el modelo por grupos.

---

## Ficha de acta del debate (una por grupo)

| Apartado | Respuesta |
|---|---|
| Caso | |
| Riesgo principal detectado | |
| Otros riesgos (2) | |
| Quién puede resultar dañado y cómo | |
| Decisión del grupo (5 líneas) | |
| 3 medidas concretas que exigimos | |
| Qué información pediríamos a TurisData antes de seguir | |
| Duda o desacuerdo que ha quedado abierto | |
