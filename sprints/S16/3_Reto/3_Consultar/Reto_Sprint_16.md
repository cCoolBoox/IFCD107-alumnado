# Sprint 16 · Reto «Entrega final: evaluar, demostrar y documentar»

> **Ficha completa del reto, para consultar.** Para trabajar, [el reto en una página](../1_Trabajar/Reto_Sprint_16_una_pagina.md). Qué se sube y cómo se evalúa: [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md).
>
> - Volver al [README del sprint](../../README.md).
> - Si es vuestro primer reto: [Cómo se trabaja un reto](../../../../material/4.%20Como_se_trabaja_un_reto.md).

## Ficha del reto

### 1 · 🎯 Qué os pide el cliente

**Qué os pide el cliente.** El cliente (el docente) va a **recibir vuestro trabajo como si fuera un entregable real**. Quiere poder **clonar el repositorio y seguir el README**, **ver funcionar el demostrador**, **leer una memoria de 10–15 páginas** y **entender los riesgos** antes de decidir si adopta vuestro modelo. Para eso tenéis que: evaluar a fondo el modelo candidato del Sprint 15 (una sola vez en el test), buscar sesgos por subgrupos y **aplicar y medir** una medida para reducirlos, cerrar el registro de riesgos y clasificar el sistema según el RGPD y el AI Act, construir un demostrador que no se rompa con entradas erróneas, que avise de la incertidumbre y que tenga **plan B en vídeo**, y documentarlo todo (model card, README y memoria técnica).

**Cómo se trabaja.** Este es el sprint de cierre: no hay una plantilla de código que rellenar (salvo el demostrador), sino **vuestro proyecto de los sprints 14 y 15**, que ahora hay que terminar y dejar listo para que otra persona lo use. Os damos plantillas para el demostrador, la model card, la memoria y la lista de congelación. **Todo lo que haya en la rama principal del repositorio a las 14:30 del 10/12 es lo que se evalúa**; pasada esa hora, se congela. Hay tres días de clase y, **entre el día 1 y el día 2, dos días sin clase**: buen momento para avanzar la memoria. El equipo decide hasta dónde llega: 🟢 mínimo, 🟡 estándar o 🔴 extra.

---

### 2 · 🧰 Recursos del reto

| Recurso | Para qué lo usaréis | Dónde está |
|---|---|---|
| **Vuestro proyecto** (repositorio privado `ifcd107-equipo-…`) | El modelo candidato del Sprint 15, su registro de experimentos, los datos y el registro de riesgos de los sprints 14 y 15 | Vuestro repositorio de GitHub |
| **Cuaderno del S13** [`S13_02`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/2_Practica/S13_02_plantilla_informe_visual.ipynb) | Los gráficos de la evaluación (matriz de confusión, curvas, importancia de variables, SHAP o Grad-CAM) para adaptarlos | Colab |
| **Presentación S16.1** y **apuntes del sprint** | Qué es un demostrador, cómo se documenta y, con ejemplos de números, cómo se miden los sesgos y su mitigación | [Presentación](../../1_Teoria/S16.1_Pildora_demostrador_y_documentacion.pdf) · [apuntes](../../1_Teoria/apuntes/apuntes_demostrador_sesgos_y_memoria.md) |
| **Cuaderno del sprint** [`S16_01`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S16/2_Practica/S16_01_demostrador.ipynb) | Práctica del demostrador: guardar el modelo y sus metadatos, separar la lógica, pruebas, Streamlit, widgets y API | Colab |
| **La carpeta del demostrador** [`demostrador/`](../1_Trabajar/plantillas/demostrador/) | `logica.py`, `app.py`, `api.py` (opcional), `tests/test_logica.py`, `requirements.txt` y `README_demostrador.md`. Es un ejemplo completo con el modelo de TurisData: vosotros lo adaptáis a **vuestro** proyecto. La carpeta `modelo/` no viene hecha: la crea el cuaderno `S16_01` o vuestro script de entrenamiento | En GitHub: *Code → Download ZIP*. Trabajad en una copia |
| **Python y librerías** (`scikit-learn`, `streamlit`, `pytest`…) | Ejecutar el cuaderno de evaluación, lanzar el demostrador y las pruebas | `pip install -r requirements.txt`. Si no podéis instalar Streamlit, la alternativa es el cuaderno con *widgets* de `S16_01` |
| **Model card** | Ficha técnica del modelo de máximo 2 páginas | [`plantilla_model_card.md`](../1_Trabajar/plantillas/plantilla_model_card.md) |
| **Esqueleto de la memoria** | Secciones, presupuesto de páginas y mapa de requisitos R1–R11 | [`plantilla_esqueleto_memoria_tecnica.md`](../1_Trabajar/plantillas/plantilla_esqueleto_memoria_tecnica.md) |
| **Lista de congelación** | Repasar todo antes de las 14:30 | [`checklist_congelacion.md`](../1_Trabajar/plantillas/checklist_congelacion.md) |
| **Coevaluación individual (anexo B)** | Valorar el trabajo de cada persona del equipo. Es **confidencial**: va al docente, no al repositorio | [`plantilla_coevaluacion.md`](../1_Trabajar/plantillas/plantilla_coevaluacion.md) |
| **Cómo entregar en GitHub** | Subir los ficheros a `sprint-16/` | [Guía de entrega](../../../../material/5.%20Como_entregar_en_GitHub.md) |
| **Autoevaluación y coevaluación** | Cada persona rellena su hoja y la sube | [Hoja del sprint](../2_Entregar/autoevaluacion_y_coevaluacion.md) |
| **Un asistente de IA** (opcional) | Entender sesgos, errores de código o revisar la redacción | Con las reglas de la «Ayuda 1» del paso a paso |

---

### 3 · 🪜 Guía paso a paso

Son ocho pasos, de **525 minutos en total** repartidos en tres días. Las jornadas de proyecto duran **6 horas completas (250 minutos de trabajo al día)**: los pasos de esta ficha ocupan unos 200 y los **50 minutos restantes de cada día son «subir de nivel»** (pasar del mínimo al estándar con la rúbrica en la mano). Cada uno dice **qué hacéis** (la lista corta), **cómo se hace** con el detalle, **qué deberíais ver** y **cuándo está hecho**. Las ayudas (IA, errores, atascos) están al final. El día 1 empieza con 10 minutos de planning, la píldora de teoría y la práctica del demostrador (`S16_01`), que no se cuentan en los 525. Si el tiempo aprieta, completad el nivel mínimo y dejad lo demás para los dos días sin clase.

#### Paso 1 · Evaluar el modelo en el test y buscar dónde falla (día 1, 40 minutos)
1. Evaluar el modelo candidato del Sprint 15 en el test, **una sola vez**, y anotar las métricas con su incertidumbre.
2. Adaptar los gráficos de `S13_02` y guardar todo en `notebooks/04_evaluacion.ipynb`.
3. Calcular la métrica por subgrupos y sacar la lista de los errores más frecuentes.

**Cómo se hace**
- **Evaluar.** Cargad el modelo ya elegido y pasadle el test. **Una vez.** Si el resultado no os gusta, no se vuelve a elegir mirando el test: se anota y se explica. Guardad la métrica con su intervalo o su variación.
- **Gráficos.** Abrid [`S13_02`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/2_Practica/S13_02_plantilla_informe_visual.ipynb) y copiad lo que os sirva: matriz de confusión, curvas, importancia de variables, SHAP o Grad-CAM. Cada gráfico con un **título que diga la conclusión** («Las reservas por móvil se cancelan más»), no una descripción.
- **Subgrupos.** Elegid las columnas con categorías (país, canal, tipo de imagen…) y calculad la métrica para cada valor. Ejemplo con cifras inventadas: el *recall* es del 74,8 % en total, pero del 80 % en web y del 58 % en móvil. Eso es un sesgo que el número global esconde. Si el subgrupo tiene pocos casos, decid cuánta incertidumbre hay.
- **Errores.** Sacad la lista de los casos donde más falla (por ejemplo, las 20 cancelaciones que el modelo no detectó), mirad ejemplos reales uno a uno y anotad qué tienen en común. De ahí salen las limitaciones honestas de la memoria.
- **Tutoría.** En estos 40 minutos cada equipo tiene su franja de tutoría de sesgos y visualización: llevad el cuaderno abierto con la métrica por subgrupos.

**Qué deberíais ver.** Una tabla con las métricas del test y su incertidumbre, dos o tres gráficos con título-conclusión, una tabla con la métrica de cada subgrupo (aunque no haya diferencias, se anota) y una lista corta de errores típicos.

**Hecho cuando:** el cuaderno `04_evaluacion.ipynb` tiene la evaluación en test, los gráficos, los subgrupos y la lista de errores, y todo el equipo sabe qué subgrupo va peor.

#### Paso 2 · Abrir la memoria y la model card (día 1, 85 minutos)
1. Repartir las secciones de la memoria entre las personas del equipo.
2. Copiar el esqueleto de la memoria y la plantilla de la model card y rellenar lo que ya sabéis.
3. Dejar el demostrador básico funcionando y anotar lo que falta y quién lo hace.

**Cómo se hace**
- **Repartir.** Abrid [`plantilla_esqueleto_memoria_tecnica.md`](../1_Trabajar/plantillas/plantilla_esqueleto_memoria_tecnica.md): tiene las secciones 0 a 9, un presupuesto de páginas (total 10–15) y un mapa de requisitos R1–R11. Cada persona redacta su parte, con **vuestros** resultados. El resumen ejecutivo (sección 0) se escribe **al final**.
- **Rellenar lo que ya existe.** Las secciones 1 a 4 salen de lo que hicisteis en los sprints 14 y 15 (ficha de proyecto, datos y EDA, comparativa de modelos). Se trata de contar, no de inventar.
- **Model card.** Copiad [`plantilla_model_card.md`](../1_Trabajar/plantillas/plantilla_model_card.md) como `docs/model_card.md` y rellenad los apartados 1 a 5. Los demás se cierran el día 2.
- **Demostrador.** Partid de lo que hicisteis en la práctica `S16_01` y de la carpeta [`demostrador/`](../1_Trabajar/plantillas/demostrador/). Basta con que arranque con vuestro modelo.
- **Los dos días sin clase.** Dejad apuntado en el tablero qué avanza cada persona para el día 2. El borrador de las secciones 1 a 6 debería estar listo ese día.

**Qué deberíais ver.** Un documento de memoria con todas las secciones del esqueleto (aunque algunas estén a medias), una model card con los primeros apartados y un demostrador que arranca.

**Hecho cuando:** existe el esqueleto de la memoria con una persona responsable por sección, la model card está empezada y el demostrador básico funciona.

#### Paso 3 · Mitigar el sesgo y volver a medir (día 2, 80 minutos)
1. Elegir una medida de mitigación para el sesgo que detectasteis.
2. Aplicarla y volver a medir, por subgrupo, antes y después.
3. Anotar los resultados en el cuaderno y en el registro de experimentos.

**Cómo se hace**
- **Elegir (5 minutos).** Una de estas, la que mejor encaje con vuestro sesgo:

| Medida | En qué consiste |
|---|---|
| Reponderar | Dar más peso al entrenar a los ejemplos del subgrupo que va peor |
| Ajustar el umbral por grupo | Decidir «cancelará» con una probabilidad mínima distinta para cada grupo |
| Añadir datos | Conseguir más ejemplos del subgrupo que falta |
| Limitar el uso | Decir en el aviso del demostrador: «no usar el modelo para el grupo X» |

- **Aplicar y medir (60 minutos).** Repetid la medición del paso 1 con la mitigación puesta y comparad **antes y después**, subgrupo a subgrupo. Mirad también el precio que se paga: si el *recall* sube, quizá la precisión baje y haya más falsas alarmas. No hay mitigación gratis; la memoria explica ese equilibrio.
- **Si el sesgo no se puede arreglar.** Faltan datos y no hay forma de conseguirlos: entonces se documenta como limitación, se avisa en el demostrador y se limita el uso. Esconderlo no es una opción.
- **Registro (15 minutos).** Apuntad la medida, las cifras de antes y de después y la decisión en el registro de experimentos del proyecto, y copiad la tabla al cuaderno.

**Qué deberíais ver.** Una tabla con el antes y el después por subgrupo y una frase de lectura honesta, del estilo: «El *recall* de móvil sube del 58 % al 68 % y el de web baja un punto; a cambio hay más falsas alarmas» (cifras de ejemplo).

**Hecho cuando:** hay una mitigación aplicada, medida por subgrupo y anotada en el cuaderno y en el registro de experimentos.

#### Paso 4 · Pulir el demostrador y probarlo en limpio (día 2, 40 minutos)
1. Adaptar `logica.py` a los campos, las validaciones y el aviso de incertidumbre de vuestro proyecto.
2. Probar entradas normales, imposibles y vacías.
3. Escribir las pruebas con `pytest` y fijar las versiones en `requirements.txt`.
4. Lanzarlo en una carpeta nueva siguiendo solo el README.

**Cómo se hace**
- **Adaptar.** En `logica.py` cambiad los campos, los rangos válidos y el texto del aviso (cuándo no fiarse, qué no se debe hacer). Los errores, en español y diciendo qué campo falla, qué se esperaba y qué se recibió. La respuesta **devuelve datos**, no imprime: la interfaz es quien los muestra. Si vuestro demostrador es un asistente o *chatbot*, tiene que decir que es una IA y citar sus fuentes.
- **Probar a propósito.** 3 entradas normales, 1 imposible (una edad de 250) y 1 vacía. Debe salir un mensaje claro, por ejemplo «Introduce una edad entre 0 y 120», y nunca un texto rojo de error. Al predecir, debe mostrar algo como «Riesgo: alto (confianza media)».
- **Pruebas.** En `tests/test_logica.py` cambiad la reserva de ejemplo por una de vuestro proyecto y añadid tres pruebas propias de sentido común (por ejemplo: «una reserva flexible y sin depósito tiene más riesgo que una no reembolsable con depósito total»). Desde la carpeta `demostrador/`: `pytest -q`.
- **Versiones.** Dejad en `requirements.txt` solo lo que usáis, con versión fija, y anotad la versión de Python en el README.
- **Lanzar.** `pip install -r requirements.txt` y `streamlit run app.py` (se abre en `http://localhost:8501`). La API es opcional.

**Qué deberíais ver.** La app abierta en el navegador, mensajes claros con las entradas malas, un aviso de incertidumbre en cada resultado y `pytest -q` sin fallos.

**Hecho cuando:** el demostrador se lanza con un comando, no se rompe con las cinco entradas de prueba y las pruebas pasan.

#### Paso 5 · Cerrar la model card y completar la memoria (día 2, 80 minutos)
1. Terminar la model card con las cifras finales (35 minutos).
2. Clasificar el sistema según el RGPD y el AI Act y actualizar el registro de riesgos.
3. Completar el borrador de la memoria con todos los apartados (45 minutos).

**Cómo se hace**
- **Model card.** Rellenad los apartados que faltan: subgrupos (con las cifras del paso 3), ética y riesgos, limitaciones («cuándo no fiarse») y mantenimiento. Debe coincidir con la memoria y con el aviso del demostrador. Máximo 2 páginas.
- **Riesgos y normativa.** Decidid si el sistema es de riesgo mínimo, limitado o alto y si hay datos personales, y justificadlo. Cada riesgo alto del registro `docs/riesgos_eticos.md` necesita un **estado** (mitigado, aceptado o pendiente) y una **evidencia** (dónde se ve en el repositorio). «Hemos cuidado la privacidad» no vale; «no hay datos personales, ver `docs/plan_datos.md`» sí.
- **Memoria.** Completad todas las secciones del esqueleto, aunque sea en borrador, con las figuras del cuaderno (con pie y numeradas). Respetad el presupuesto de páginas. Escribid con vuestras palabras: si usáis IA para redactar, revisadlo y anotadlo para declararlo.

**Qué deberíais ver.** Una model card sin huecos, un registro de riesgos con estado y evidencia en cada riesgo alto y una memoria con todas las secciones escritas.

**Hecho cuando:** la model card está completa, la clasificación RGPD / AI Act está justificada y la memoria tiene todos los apartados.

#### Paso 6 · Verificar en limpio y corregir (día 3, 80 minutos)
1. Una persona que no escribió el README lo sigue en un Colab nuevo o una carpeta limpia (60 minutos).
2. Mientras tanto, el resto cierra la memoria y la exporta a PDF.
3. Corregir lo que haya fallado (20 minutos).

**Cómo se hace**
- **La prueba en limpio.** Descargad el repositorio como ZIP (*Code → Download ZIP*), abrid el cuaderno principal en Colab y seguid **solo** el README. Si lo prueba quien lo escribió, no vale: ya sabe los trucos que no están anotados. Apuntad cada fallo con su mensaje.
- **La memoria.** Pasad a limpio el texto, comprobad que tiene entre 10 y 15 páginas sin contar portada, índice, referencias ni anexos, y exportadla como `docs/memoria_tecnica.pdf`. Repasad la lista de calidad del final del esqueleto: cada figura con título-conclusión y citada en el texto, cifras iguales que en el README, y revisada por alguien que no la escribió.
- **Corregir.** Lo más habitual: dependencias sin documentar (añadidlas a `requirements.txt`), rutas que solo existen en un ordenador y datos que faltan. Después, repetid la parte que falló.

**Qué deberíais ver.** Una lista de fallos pequeña y ya resuelta, el demostrador funcionando en el entorno limpio y la memoria en PDF.

**Hecho cuando:** otra persona ha reproducido el proyecto con solo el README, lo que falló está corregido y existe `docs/memoria_tecnica.pdf`.

#### Paso 7 · Plan B, riesgos cerrados, lista de congelación y coevaluación (día 3, 65 minutos)
1. Grabar el vídeo plan B del demostrador (30 minutos).
2. Cerrar el registro de riesgos y pasar la lista de congelación (35 minutos).
3. Rellenar vuestra coevaluación individual (anexo B).

**Cómo se hace**
- **Vídeo plan B.** Grabad la pantalla (1–2 minutos, unos 90 segundos) con el demostrador funcionando y una entrada errónea a propósito. Guardadlo como `docs/demo.mp4` si pesa menos de 25 MB; si no, subidlo a un sitio estable y poned el enlace en el README.
- **Lista de congelación.** Abrid [`checklist_congelacion.md`](../1_Trabajar/plantillas/checklist_congelacion.md) y marcad los bloques A (repositorio), B (reproducibilidad), C (demostrador), D (evaluación e IA responsable), E (memoria) y F (equipo y metodología). Debe hacerlo **una persona distinta a la que escribió el README**. Cada casilla sin marcar es un riesgo.
- **Sin claves ni datos personales.** Revisad que no hay ninguno en ningún fichero. Si encontráis uno, avisad al docente.
- **Coevaluación (anexo B).** Cada persona rellena [`plantilla_coevaluacion.md`](../1_Trabajar/plantillas/plantilla_coevaluacion.md): puntúa de 1 a 4 a cada integrante (incluida ella) y estima el reparto del trabajo. Un 1 o un 4 llevan un ejemplo. Se entrega al docente, no al repositorio.

**Qué deberíais ver.** El vídeo guardado, la lista de congelación con todas las casillas marcadas (o con lo pendiente apuntado) y cada persona con su coevaluación hecha.

**Hecho cuando:** el vídeo plan B existe, el registro de riesgos está cerrado, la lista de congelación está pasada y todo el equipo ha entregado la coevaluación.

#### Paso 8 · Revisión con la rúbrica, review, retro y congelación (día 3, 55 minutos)
1. Revisar el trabajo con la rúbrica y anotar el resultado en el README.
2. Hacer la review (unos 5 minutos por equipo) y la retro.
3. Subir todo a `sprint-16/`, crear la etiqueta `v1.0-entrega` y subir las autoevaluaciones, **antes de las 14:30**.

**Cómo se hace**
- **La revisión con la rúbrica (20 minutos, antes de la etiqueta).** Quien revisa sigue los cinco pasos de «Cómo se revisa» de [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md) y rellena al final del `README.md` la sección **«Revisión con la rúbrica»**: un nivel de 1 a 4 por criterio y **una frase de prueba**. Lo más fácil de arreglar se arregla ya; lo demás queda como «lo primero que mejoraríamos».
- **La review.** Unos 5 minutos por equipo, de los que 4 son de demostración del demostrador, con una entrada errónea a propósito. Enseñad también una diapositiva con el análisis de sesgos y la medida aplicada, y la lista de riesgos altos con su estado. El docente propone **una entrada difícil** para probar el demostrador en directo. En la **retro**, una cosa que mantener y una que cambiar, con una acción concreta.
- **Subir los ficheros.** Seguid [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md): (1) abrid el repositorio del equipo; (2) *Add file → Create new file* y escribid la ruta completa, por ejemplo `sprint-16/docs/model_card.md` (la barra crea la carpeta), o *Upload files* arrastrando la carpeta; (3) mensaje corto y **Commit changes**. Los ficheros, **en minúsculas y sin espacios**. Que suban personas distintas: el historial muestra a todo el equipo.
- **La etiqueta.** En la página principal del repositorio, a la derecha, *Releases → Create a new release*; en *Choose a tag* escribid `v1.0-entrega` y elegid *Create new tag*; el destino es `main`; poned un título (por ejemplo «Entrega final») y pulsad *Publish release*. Los nombres de los botones pueden cambiar un poco. Con Git en el terminal: `git tag v1.0-entrega` y `git push origin v1.0-entrega`. Comprobad que la etiqueta aparece. **Después de las 14:30 no se cambia código ni memoria.** Un fallo crítico del demostrador solo se corrige con permiso del docente y dejándolo documentado.
- **Las autoevaluaciones.** Cada persona sube su `autoevaluacion_nombre.md` a `sprint-16/` con su propia cuenta.

**Qué deberíais ver.** En `sprint-16/` los 9 ficheros del equipo y una hoja de autoevaluación por persona (**9 + N**); en el historial, commits de todas las personas; y la etiqueta `v1.0-entrega` con una hora anterior a las 14:30.

**Hecho cuando:** la sección «Revisión con la rúbrica» del README está rellena, todo está subido, la etiqueta existe antes de las 14:30 y cada persona ha subido su autoevaluación y coevaluación.

#### Ayuda 1 · Cómo usar la IA en este reto

La IA puede ahorrar tiempo, pero **escribe con seguridad cosas que pueden ser falsas** y puede cambiar una cifra sin avisar. Reglas:
- **Todo lo que dé, lo ejecutáis y lo entendéis.** Si el docente pregunta por una parte, tenéis que saber explicarla.
- **La memoria es vuestra:** la IA no la escribe por vosotros. Si la usáis para redactar o corregir, revisadla entera y **declaradlo en la memoria**.
- **Las cifras mandan:** después de que la IA toque un texto, comprobad que no ha cambiado ninguna.
- **Nada de datos personales ni claves** en una IA.

| Para qué | Ejemplo de petición | Qué comprobáis |
|---|---|---|
| Entender sesgos | «Explícame con un ejemplo qué significa que un modelo tenga peor rendimiento en un subgrupo y qué medidas existen» | Que podéis aplicar una medida **y medirla** |
| Crear la app | «Ayúdame a añadir validación de entradas a esta app de Streamlit: *[código]*» | Que **probáis** entradas absurdas |
| Estructurar la memoria | «Dame un guion de las secciones de una memoria técnica de un proyecto de IA» | Que cada sección la redactáis vosotros con **vuestros resultados** |
| Revisar la redacción | «Corrige la ortografía y la claridad de este párrafo sin cambiar el contenido» | Que no se ha cambiado ninguna cifra |

#### Ayuda 2 · Errores frecuentes (y cómo evitarlos)

| Error | Por qué ocurre | Cómo evitarlo |
|---|---|---|
| Dejar la memoria para el último día | «Total, ya está hecho» | Borrador el día 2 (9/12) y revisión el día 3 (10/12) |
| El demostrador solo funciona en el ordenador de una persona | Dependencias sin documentar | `requirements.txt` con versiones y prueba en un entorno limpio |
| Mitigación que se aplica pero no se mide | Se piensa que basta con hacerla | Comparad las métricas **antes y después, por subgrupo** |
| Subir cambios después de las 14:30 | Se siguen retocando cosas | Crear la etiqueta antes y no tocar nada después |
| Coevaluación sin entregar | Se olvida | Cada persona la entrega; cuenta para la nota individual |
| Memoria con más de 15 páginas o con fragmentos copiados | Se llena de relleno | Respetad el presupuesto de páginas; los anexos no cuentan; escribid con vuestras palabras |
| Cifras distintas en la memoria y en el README | Se copian de versiones distintas | Una revisión final de coherencia antes de congelar |
| Solo una persona hace commits | «El resto no sabe Git» | Reparto real: vale que cada persona suba un fichero desde la web |

#### Ayuda 3 · Si os atascáis

1. **El demostrador no arranca en otro ordenador:** faltan dependencias. Generad `requirements.txt` con `pip freeze` (o a mano), recortadlo a lo que usáis y probad en un entorno nuevo.
2. **No sabéis qué sesgo medir:** mirad las columnas con categorías (país, canal, tipo) y calculad la métrica para cada valor.
3. **Falta tiempo:** priorizad lo obligatorio (R1–R11 y la lista de congelación). Es mejor una memoria honesta con límites que una incompleta. Preguntad al equipo y, después, al docente.
