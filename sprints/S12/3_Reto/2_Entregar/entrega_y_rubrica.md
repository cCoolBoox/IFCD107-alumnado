# Sprint 12 · Reto «Escuchar al cliente» · Entrega y rúbrica

> **Qué se sube y cómo se evalúa.** Se lee **una vez**, antes de entregar, y se vuelve a la rúbrica cuando el equipo revisa su trabajo. Mientras trabajáis no hace falta: para eso está [el reto en una página](../1_Trabajar/Reto_Sprint_12_una_pagina.md).
>
> - Volver al [README del sprint](../../README.md) · [ficha del reto](../3_Consultar/Reto_Sprint_12.md), para consultar.
> - Vuestra hoja personal: [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md).
> - Cómo subir a GitHub paso a paso, con capturas: [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md).

Esta hoja responde a **dos preguntas distintas**, una tabla para cada una:

**Tabla A · Los ficheros:** qué ficheros hay, de dónde sale cada uno (ya hecho, lo modificáis, lo creáis o lo genera el programa) y **cuáles se suben y adónde**.

**Tabla B · Los requisitos:** qué tiene que cumplir lo que entregáis y hasta dónde llegar (🟢 mínimo, 🟡 estándar, 🔴 extra). **Es lo que se evalúa.**

**En total, al final del sprint se suben a `sprint-12/`:** **8 ficheros del equipo** (`informe_resenas.md`, `grafico_resenas.png`, `resenas.ipynb`, `ocupacion.ipynb`, `asistente_rag.ipynb`, `evaluacion_asistente.csv`, `nota_ia_responsable.md`, `LEEME.md`) **+ 1 autoevaluación y coevaluación por persona**, es decir, **8 + tantos ficheros como personas haya en el equipo** (un equipo de 3 sube 11). «El reto» no es un fichero aparte: son los **cuatro entregables del cliente** (el informe de reseñas, el cuaderno de ocupación, el cuaderno del asistente con su tabla de evaluación y la nota de IA responsable) más el `LEEME.md`. El gráfico y el cuaderno de reseñas son el apoyo que hace que las cifras del informe se puedan comprobar. Los datos del curso van a `data/` si aún no están. La *review* y la *retro* se hacen de palabra: no se suben.

## 1 · 📦 Tabla A · Los ficheros: de dónde sale cada uno y cuáles se suben

Todo lo que se sube va al repositorio privado del equipo (`ifcd107-equipo-…`), en la carpeta **`sprint-12/`**, salvo los datos.

| Fichero | Origen | Qué hacéis vosotros | ¿Se sube? |
|---|---|---|---|
| `informe_resenas.md` | **Lo creáis a partir de una plantilla.** Os damos `plantilla_informe_cliente.md` con huecos | Copiarla como `informe_resenas.md` y rellenarla con cifras de vuestro código (2 páginas como máximo) | **Sí** · `sprint-12/` |
| `grafico_resenas.png` | **Lo genera** el cuaderno `resenas.ipynb` | Guardar el gráfico del informe con `plt.savefig` y enlazarlo desde el informe | **Sí** · `sprint-12/` |
| `resenas.ipynb` | **Lo creáis** copiando `S12_03` y quedándoos con lo que necesitáis | Sentimiento, evaluación en prueba, temas, gráfico y citas | **Sí** · `sprint-12/` |
| `ocupacion.ipynb` | **Lo creáis** copiando `S12_01` (o `S12_02` si usáis una red) | Partición por fecha, *baseline*, modelo, tabla de MAE, gráfico a 7 días y una frase para el cliente | **Sí** · `sprint-12/` |
| `asistente_rag.ipynb` | **Lo creáis** copiando `S12_06` | La demo del asistente: trocear, recuperar, citar, umbral, evaluación y ataques | **Sí** · `sprint-12/` |
| `evaluacion_asistente.csv` | **Lo genera** el cuaderno del asistente | Guardar con `to_csv` la tabla de las 25 preguntas (acierto, sin fuente, alucinación) | **Sí** · `sprint-12/` |
| `nota_ia_responsable.md` | **Lo creáis** desde cero | Una página con riesgos concretos y medidas aplicadas y medidas con cifras | **Sí** · `sprint-12/` |
| `LEEME.md` | **Lo creáis** desde cero | Cinco líneas para ejecutar todo (con versiones de las librerías) y, al final, la sección «Revisión con la rúbrica» | **Sí** · `sprint-12/` |
| `resenas.csv`, `ocupacion_diaria.csv`, `politica_alojamiento.md` y `preguntas_referencia.csv` | **Ya hechos.** Los datos del curso (sintéticos) | Nada: se usan sin cambiarlos | **Sí**, sin cambios · `data/` (si aún no están) |
| Autoevaluación y coevaluación (`autoevaluacion_nombre.md`) | **Ya hecha, en blanco** | Cada persona copia la plantilla con su nombre y la rellena; la coevaluación va **dentro del mismo fichero** | **Sí**, **una por persona** (no una por equipo) · `sprint-12/` |
| Cuadernos de práctica `S12_01` a `S12_07` con vuestros ejercicios | **Ya hechos.** Son las prácticas del sprint | Nada: son vuestra base de trabajo | **No** se suben |

---

## 2 · ✅ Tabla B · Los requisitos: qué tiene que cumplir y hasta dónde llegar

| Requisito | Qué se pide exactamente | Nivel | Dónde se comprueba |
|---|---|---|---|
| **Serie partida por fecha y *baseline*** | Se entrena con lo antiguo y se evalúa con lo último (nunca se baraja). El *baseline* («igual que la semana anterior») tiene su MAE y su previsión de los próximos 7 días | 🟢 Mínimo | `ocupacion.ipynb` |
| **Sentimiento de las reseñas** | Porcentaje de reseñas positivas, neutras y negativas, **un gráfico** y **3 citas reales** (con su `id_resena`) | 🟢 Mínimo | `informe_resenas.md` y `grafico_resenas.png` |
| **Asistente que cita y sabe callar** | Trocea la política, recupera el fragmento más parecido, **cita su fuente** y responde «No consta…» a la pregunta que no tiene respuesta (la del gimnasio) | 🟢 Mínimo | `asistente_rag.ipynb` |
| **Nota de IA responsable** | Una página con riesgos **concretos** (pregunta sin respuesta, datos personales en las reseñas, texto que intenta manipular al asistente, sesgos) y qué medida se aplica contra cada uno | 🟢 Mínimo | `nota_ia_responsable.md` |
| **`LEEME.md`** | Cinco líneas: cómo ejecutar todo, con las versiones de las librerías | 🟢 Mínimo | `LEEME.md` |
| **Modelo frente al *baseline*** | Un modelo (SARIMAX o una red GRU) con su MAE en la **misma tabla** que el del *baseline*, la previsión a 7 días en un gráfico, **una frase para el cliente** y un veredicto honesto: si no gana al *baseline*, se dice | 🟡 Estándar | `ocupacion.ipynb` |
| **Sentimiento evaluado** | El clasificador se evalúa **en prueba**: exactitud y matriz de confusión | 🟡 Estándar | `resenas.ipynb` |
| **Evaluación del asistente** | Las 20 preguntas de referencia + **5 propias** (una sin respuesta en la política): para cada una, acierto, sin fuente o alucinación; las cuentas suman 25 | 🟡 Estándar | `evaluacion_asistente.csv` y `asistente_rag.ipynb` |
| **Tres ataques** | **3 intentos de *prompt injection*** de tipos distintos, probados, con qué pasó y qué medida lo frenó | 🟡 Estándar | `asistente_rag.ipynb` y `nota_ia_responsable.md` |
| **Informe de 2 páginas** | Resumen para la dirección, sentimiento, gráfico, **3 recomendaciones** que el cliente pueda ejecutar el lunes (qué, quién, cómo sabremos que funciona) y límites (datos sintéticos, error medio de la previsión) | 🟡 Estándar | `informe_resenas.md` |
| **Ninguna clave** | No hay claves ni datos personales en el código ni en el repositorio; si se usa una clave, se lee de una variable de entorno | 🟡 Estándar | Todos los ficheros |
| **Revisión y autoevaluación** | Alguien que **no escribió esa parte** revisa los entregables con la rúbrica (justo debajo de estas tablas) y anota nivel y prueba en el `LEEME.md`; cada persona sube su hoja de autoevaluación y coevaluación | 🟡 Estándar | `LEEME.md` (sección «Revisión con la rúbrica») y `sprint-12/` |
| **Temas con ejemplos** | Los **3 temas más criticados y los 3 más valorados**, con cifras (cuántas reseñas lo mencionan) y un ejemplo real de cada uno; 5 citas en total | 🔴 Extra | `informe_resenas.md` y `resenas.ipynb` |
| **Sin fuga de datos, y explicado** | Escalado y vectorización se ajustan **solo con el entrenamiento**, con una frase en el cuaderno que explica por qué | 🔴 Extra | `ocupacion.ipynb` y `resenas.ipynb` |
| **Todo de arriba abajo y sin internet** | Cada cuaderno se ejecuta con *Reiniciar sesión y ejecutar todo*, con `SEMILLA = 42`, sin errores y sin conexión; las versiones están fijadas en el `LEEME.md` | 🔴 Extra | Los tres cuadernos y `LEEME.md` |
| **Alternativas comparadas y medidas evaluadas** | Dos opciones comparadas con números (SARIMAX frente a GRU, o varios umbrales del asistente) y la elegida, justificada; la medida de seguridad con cifras («bloqueó 3 de 3 ataques y ninguna de las 25 preguntas legítimas») | 🔴 Extra | `ocupacion.ipynb`, `asistente_rag.ipynb` y `nota_ia_responsable.md` |

---

## 3 · 🧭 Rúbrica del reto · cómo se puntúa y cómo se revisa

La usan **dos veces**: el equipo, para revisar su propio trabajo antes de entregar (es lo que dice la *Definition of Done*), y el docente, para puntuar. Se mira **cada criterio por separado** y se pone el nivel de la columna cuyo texto **se cumple entero**: si lo de un nivel se cumple a medias, es el nivel de abajo. **0** significa que no se ha entregado nada de ese criterio.

Orientación: lo que pide el nivel 🟢 mínimo sale en un **2**, el 🟡 estándar en un **3** y los 🔴 extras en un **4**.

| Criterio | 1 · Empezado | 2 · Mínimo | 3 · Estándar | 4 · Extra |
|---|---|---|---|---|
| **Corrección técnica** (¿funciona?) | Hay código, pero no se ejecuta de arriba abajo o falta el *baseline* o el asistente no devuelve ninguna respuesta | La serie se parte por fecha y el *baseline* tiene su MAE; el asistente recupera un fragmento, lo cita y responde «No consta…» a la pregunta del gimnasio | Hay modelo con su MAE junto al del *baseline*; el sentimiento se evalúa en prueba (exactitud y matriz); las 25 preguntas están evaluadas y las cuentas suman 25; 3 ataques probados | Además, dos alternativas comparadas con números (SARIMAX frente a GRU, o varios umbrales) y la elegida justificada |
| **Reproducibilidad** (¿lo puede repetir otra persona?) | Solo funciona en el ordenador o la sesión de quien lo hizo (rutas propias, datos sin indicar) | El `LEEME.md` dice qué ejecutar, pero faltan versiones, datos u orden de los cuadernos | Otra persona ejecuta cada cuaderno con *Reiniciar sesión y ejecutar todo* y obtiene **los mismos números** (`SEMILLA = 42`), siguiendo solo el `LEEME.md` | Además, funciona sin internet, las versiones están fijadas y los datos (o el script para obtenerlos) van incluidos |
| **Análisis y comunicación al cliente** (¿lo entiende quien no programa?) | Hay cifras y gráficos, pero sin interpretarlos y sin recomendaciones | Da el sentimiento con cifras, un gráfico y 3 citas reales; las recomendaciones son vagas o hay menos de tres | Informe de 2 páginas, cifras interpretadas, **3 recomendaciones ejecutables el lunes** (qué, quién, cómo sabremos que funciona), una frase para el cliente sobre la previsión y límites explicados | Además, 3 temas criticados y 3 valorados con cifras y ejemplos, y cada recomendación apoyada en una cifra concreta del informe |
| **IA responsable** (¿se sabe qué riesgos hay y qué se hizo?) | No hay nota, o no nombra ningún riesgo | La nota nombra riesgos (alucinación, datos personales, *prompt injection*, sesgos) pero sin decir qué medida se aplica | Riesgos **concretos** de este reto, cada uno con su medida (umbral y «No consta», filtro de frases sospechosas…); 3 ataques descritos con qué los frenó; sin claves; datos sintéticos declarados | Además, las medidas **se miden**: «el filtro bloqueó 3 de 3 ataques y ninguna de las 25 preguntas legítimas», y se dice qué no cubre |

**Cómo se revisa** (unos 15 minutos, antes de subir; lo hace **una persona que no escribió esa parte**):

1. **Ejecutar** cada cuaderno con *Reiniciar sesión y ejecutar todo* y siguiendo solo lo que dice el `LEEME.md`. Comparar con el informe los números clave (MAE, exactitud, aciertos). Anotar si algo no funciona o no coincide.
2. **Leer el informe como si fuerais la dirección de TurisData**: ¿se entienden las 3 recomendaciones sin saber programar? ¿Se dice que los datos son sintéticos? Subrayar lo que no se entienda.
3. **Probar el asistente y mirar la nota**: preguntarle algo que no está en la política, repetir uno de los ataques y comprobar que cada riesgo de la nota tiene su medida. Buscar en el código y en los ficheros que no haya ninguna clave.
4. **Poner un nivel (1 a 4) en cada criterio, con una frase de prueba** (por ejemplo: «3 · el MAE del modelo y el del *baseline* están en la misma tabla, pero falta la matriz de confusión»). Sin prueba escrita, el nivel no vale.
5. **Apuntar el resultado** en la sección «Revisión con la rúbrica» del `LEEME.md` y corregir lo más fácil de arreglar. Lo demás se anota como mejora.

Cada persona, además, se puntúa a sí misma en su hoja de [autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md) con **esta misma rúbrica**.
