# Sprint 9 · Reto «Conocer al huésped»

> **Esta es la ficha completa del reto, explicada paso a paso** para quien nunca ha trabajado con esta metodología ni con IA. Léela entera **antes de empezar** y vuelve a ella cuando tengas dudas.
>
> - Si es tu primer reto, lee antes [Cómo se trabaja un reto](../../../material/4.%20Como_se_trabaja_un_reto.md).
> - Volver al [README del sprint](../README.md) · [Guía del sprint en PDF](../guia/Guia_Sprint_09.pdf) · [versión ecofriendly para imprimir](../guia/Guia_Sprint_09_ecofriendly.pdf).
> - **Este reto en PDF:** [a color](Reto_Sprint_09.pdf) · [ecofriendly, para imprimir](Reto_Sprint_09_ecofriendly.pdf).

## Ficha del reto

### En pocas palabras (léelo primero)

**Qué os pide el cliente.** Lucía, la directora comercial de TurisData, envía **la misma newsletter a sus 1.200 huéspedes** y vende las **25 experiencias** con los mismos banners. Sospecha que hay «tipos» de cliente muy distintos y que cada uno querría cosas diferentes. Os pide: *«Decidme quiénes son mis clientes, cómo los llamo y qué le enseño a cada uno.»*

**Aquí la IA «aprende sin respuestas».** No hay una columna que diga «este cliente es de tipo A». Tenéis que **descubrir los grupos** que se esconden en los datos y luego **ponerles nombre y significado de negocio**. Además, construiréis un **recomendador** sencillo: dado un huésped, sugerir experiencias que probablemente le gusten.

**Qué vais a hacer, en cinco pasos:**
1. **Agrupar a los huéspedes** (segmentación) con la técnica de clustering, eligiendo cuántos grupos (`k`) con un criterio técnico **y** de negocio.
2. **Dibujar un mapa 2D** de los grupos con PCA.
3. **Interpretar cada segmento**: ponerle nombre, tamaño, perfil y una acción comercial.
4. **Construir un recomendador** de experiencias (comparando al menos dos métodos) y una función `recomendar(id_usuario, n)`.
5. **Escribir una nota de IA responsable** (5 líneas).

**Qué vais a entregar:** un cuaderno, una [ficha de segmentos](plantilla_ficha_segmentos.md) de 1 página y una nota de IA responsable (dentro de la ficha).

**Qué vais a aprender haciéndolo:** a **segmentar sin etiquetas**, a **traducir grupos matemáticos a clientes con nombre**, a **comparar recomendadores** y a ver los riesgos de personalizar (discriminación, sesgo de popularidad, privacidad).

**Cuánto tiempo:** unas 2 horas y 20 minutos (días 1 y 2) entre el planning, el reto y la entrega, intercaladas con las prácticas.

**Núcleo y extra.** Núcleo: segmentos con `k` justificado y su ficha, y un recomendador sencillo. Extra: otros algoritmos de agrupación y el aprendizaje por refuerzo (que se ve en demostración).

### Palabras que van a aparecer en este reto

| Palabra | Qué significa, en sencillo |
|---|---|
| **Segmentación** | Dividir a los clientes en grupos parecidos entre sí |
| **Clustering** | La técnica que agrupa automáticamente los datos parecidos. Ejemplo: k-means |
| **k** | El número de grupos que se piden al algoritmo |
| **Silueta** | Un número entre −1 y 1 que dice si los grupos están bien separados (más alto, mejor) |
| **Escalar** | Poner las variables en una escala comparable (si no, la «edad» y el «gasto en euros» no pesan igual) |
| **PCA** | Técnica para «aplastar» muchas columnas en 2 dibujables, conservando lo más importante |
| **Varianza explicada** | Qué parte de la información conserva el dibujo 2D (el % que aparece en los ejes) |
| **Recomendador** | Un sistema que sugiere elementos (experiencias) a cada usuario |
| **RMSE** | Error medio entre la nota que predice el recomendador y la nota real |
| **Precision@3** | De las 3 experiencias que se recomiendan, cuántas le interesaban realmente |
| **Sesgo de popularidad** | El sistema recomienda siempre lo más popular y los demás nunca tienen oportunidad |
| **Arranque en frío** | No saber qué recomendar a un cliente nuevo que aún no ha valorado nada |

### El cliente
Lucía, directora comercial de **TurisData Canarias**, envía la misma newsletter a los 1 200 huéspedes de su base y vende las 25 experiencias con los mismos banners. Sospecha que hay «tipos» de cliente muy distintos y que cada uno querría cosas diferentes. Nos pide: *«Decidme quiénes son mis clientes, cómo los llamo y qué le enseño a cada uno»*.

### Qué se entrega y en qué formato
1. **Notebook** `reto_S09_conocer_al_huesped.ipynb` (versión ejecutable de arriba abajo, con semillas fijas) con:
   - Segmentación de [`huespedes.csv`](../../../datos/huespedes.csv) (método justificado, `k` elegido con silueta y con criterio de negocio) y un **mapa 2D con PCA**.
   - Prototipo de **recomendador de experiencias** (mínimo dos métodos comparados con RMSE y precision@3) y la función `recomendar(id_usuario, n)`.
2. **Ficha de segmentos (1 página, Markdown o PDF)** usando [`plantilla_ficha_segmentos.md`](plantilla_ficha_segmentos.md): por cada segmento, nombre, tamaño, perfil en una frase, **una acción comercial** y **una experiencia estrella** de las que recomienda tu prototipo.
3. **Nota de IA responsable (5 líneas)** dentro de la ficha: qué riesgos tiene segmentar y recomendar (discriminación, sesgo de popularidad, privacidad).

### Restricciones
- Solo numpy, pandas, matplotlib/seaborn y scikit-learn (sin librerías de recomendación especializadas).
- Trabajo en equipos de 3-4; **todas las personas** deben poder explicar cualquier parte.
- Los ficheros de solución del docente no están disponibles: los segmentos se validan con **sentido de negocio** y con métricas internas.

### Criterios de evaluación (rúbrica de retos, de 1 a 4)

| Criterio | 1 · Insuficiente | 2 · Suficiente | 3 · Bueno | 4 · Excelente |
|---|---|---|---|---|
| **Corrección técnica** | Datos sin escalar o `k` al azar; métricas mal calculadas | Segmenta y recomienda con fallos menores | Escalado, `k` justificado y recomendador evaluado con una división de prueba | Además compara varios métodos de clustering y de recomendación con resultados razonados |
| **Reproducibilidad** | No se puede volver a ejecutar | Se ejecuta con ayuda del equipo | Se ejecuta de arriba abajo con semillas fijas | Además incluye README corto, datos o script de descarga y versiones |
| **Análisis y comunicación al cliente** | Solo cifras o gráficos sin interpretar | Nombres de segmentos sin acciones | Segmentos con nombre, tamaño y una acción cada uno | Además recomendación accionable, priorizada por valor y con límites explicados |
| **IA responsable** | No se considera | Menciones genéricas («hay que cuidar la privacidad») | Riesgos específicos: sesgo de popularidad, discriminación por edad o niños | Además propone medidas (p. ej. no segmentar por edad para precios) y comprueba alguna |

### Pasos sugeridos
| Día | Qué hacer |
|---|---|
| **Viernes 13/11 (45 min de PBL tras las prácticas 01 y 02)** | Ya tenéis los segmentos en borrador: elegid método y `k` con silueta **y** con criterio de negocio; haced el mapa PCA. |
| **Lunes 16/11, por la mañana** | Prácticas 03 y 04. Con lo aprendido, arrancad el prototipo de `recomendar` y comparad al menos dos métodos. |
| **Lunes 16/11 (50 min de PBL)** | 1) Comparad recomendadores y probad `recomendar` con 3 usuarios (40 min). 2) Rellenad la ficha de segmentos, nota de IA responsable, repaso de la Definition of Done y ensayo de la review (45 min). |

### Guía paso a paso para principiantes

#### Paso 1 · Preparación y datos (día 1, tras las prácticas 01 y 02, 10 minutos)
1. Abrid un cuaderno nuevo (o el `reto_S09_conocer_al_huesped`) con [`huespedes.csv`](../../../datos/huespedes.csv) y [`valoraciones_experiencias.csv`](../../../datos/valoraciones_experiencias.csv).
2. **Revisad las columnas** de [`huespedes.csv`](../../../datos/huespedes.csv) (edad, gasto, antelación, etc.). ¿Cuáles son números y cuáles categorías?
3. **Escalad** las variables numéricas. Si no, el algoritmo dará más peso a las columnas con números grandes.

#### Paso 2 · Segmentar y elegir k (día 1, 20 minutos)
1. Probad k-means con varios valores de `k` (por ejemplo, de 2 a 8).
2. Calculad la **silueta** para cada `k` y dibujad la curva.
3. **No elijáis `k` solo por la silueta.** Preguntaos también: *¿puede la directora actuar con ese número de grupos?* Entre 3 y 5 segmentos suele ser manejable; 12 serían inmanejables.
4. Anotad la razón de vuestra elección en **una frase con las dos justificaciones** (técnica y de negocio).

#### Paso 3 · Mapa PCA e interpretación (día 1, 15 minutos)
1. Aplicad **PCA** a 2 componentes y dibujad los huéspedes coloreados por segmento. Poned en los ejes el **% de varianza**.
2. Para cada segmento, calculad el **perfil medio**: edad, gasto, antelación, composición del grupo, etc. Comparadlo con la media general.
3. **Ponedle un nombre comercial y una frase** con cifras concretas. Ejemplo (inventado): *«Familias de larga estancia: 410 huéspedes (34 %); 9 de cada 10 viajan con niños, reservan con 110 días de antelación y gastan poco en actividades»*.
4. Proponed **una acción comercial** para cada segmento (qué enseñar, cuándo, por qué canal).

#### Paso 4 · Recomendador (día 2, tras las prácticas 03 y 04, 30 minutos)
1. Montad al menos **dos métodos** (por ejemplo, popularidad y filtrado colaborativo por similitud).
2. **Evaluad con una división de prueba:** esconded algunas valoraciones, dejad que el recomendador las prediga y comparad. Medid **RMSE** y **precision@3**.
3. Programad `recomendar(id_usuario, n)` que devuelva las `n` mejores experiencias que **el usuario aún no ha valorado**.
4. Probadla con **3 usuarios distintos** y comprobad que tiene sentido (¿le sugiere cosas parecidas a las que ya le gustaron?).

#### Paso 5 · Ficha, IA responsable y ensayo (día 2, 30 minutos)
1. Completad la [ficha de segmentos](plantilla_ficha_segmentos.md): por segmento, nombre, tamaño, perfil, **una acción** y **una experiencia estrella** (la que recomienda vuestro prototipo para ese grupo).
2. Nota de IA responsable (5 líneas, al menos **2 riesgos específicos**), por ejemplo:
   - *Discriminar:* si se usa la edad o «viaja con niños» para fijar precios, se puede discriminar. Medida: usar la segmentación para comunicar, no para variar precios.
   - *Sesgo de popularidad:* las experiencias poco conocidas casi no se recomiendan. Medida: reservar un hueco de la recomendación a opciones menos populares.
   - *Privacidad:* se combinan datos de reserva y valoraciones. Medida: usar identificadores y no mostrar datos personales.
3. Repasad la Definition of Done y ensayad 3 minutos de review.

### Cómo usar la IA en este reto

| Para qué | Ejemplo de petición | Qué tenéis que comprobar |
|---|---|---|
| Entender un concepto | «Explícame k-means y la silueta con una analogía de personas en una fiesta» | Que podáis explicarlo con vuestras palabras |
| Entender PCA | «¿Qué significa que PCA conserve el 60 % de la varianza? Dame un ejemplo sin fórmulas» | Que vuestro gráfico dice lo mismo |
| Poner nombres a los segmentos | «Dado este perfil medio: *[tabla]*, dame 5 nombres comerciales cortos y evocadores» | Que el nombre refleja las **cifras** del segmento, no una invención |
| Pensar en riesgos | «¿Qué riesgos tiene recomendar experiencias según la edad?» | Elegid los que aplican a **vuestro** caso y dad una medida real |

**Reglas del reto:**
- Solo `numpy`, `pandas`, `matplotlib/seaborn` y `scikit-learn`: nada de librerías de recomendación especializadas.
- **Todas las personas deben poder explicar cualquier parte.** En la review el docente puede preguntar a cualquiera.
- No hay soluciones del docente: los segmentos se validan con **sentido de negocio** y con **métricas internas** (silueta, RMSE).
- Declarad en el cuaderno dónde habéis usado IA y qué habéis comprobado.

### Errores frecuentes (y cómo evitarlos)

| Error | Por qué ocurre | Cómo evitarlo |
|---|---|---|
| Agrupar sin escalar | Se olvida | Escalad **antes** del clustering |
| Elegir `k` solo con la silueta | «Es lo que dice el número» | Añadid el criterio de negocio |
| Poner nombres sin mirar los datos | Suena bien | Cada nombre debe justificarse con **dos cifras** del perfil |
| Recomendar lo que el usuario ya ha valorado | No se filtra | La función debe excluirlas |
| Evaluar el recomendador con los mismos datos que usó | «Es lo más fácil» | Probad con valoraciones **escondidas** |
| Nota de IA responsable genérica | Prisa | Dos riesgos **concretos** de este caso, con medida |

### Un buen resultado se parece a…

- **Ficha de segmentos** con 3–5 filas, cada una con nombre, tamaño, perfil con cifras, acción y experiencia estrella.
- **Mapa PCA** con título que enuncia una conclusión («Cuatro tipos de huésped claramente separados») y ejes con el % de varianza.
- **Recomendador:** una tabla *método · RMSE · precision@3* y una frase de elección («Elegimos filtrado colaborativo porque mejora un 15 % la precision@3 de la popularidad»). Las cifras son un ejemplo.

### Antes de entregar: autoevaluación rápida

Repasad estas preguntas y rellenad después la hoja [autoevaluacion_y_coevaluacion.md](autoevaluacion_y_coevaluacion.md) (cada persona sube la suya con su entrega).

| Pregunta | Sí / No |
|---|---|
| ¿El cuaderno se ejecuta de arriba abajo, con semillas fijas? | |
| ¿Hemos escalado antes de agrupar y justificado `k` con silueta **y** con negocio? | |
| ¿El mapa PCA tiene segmentos coloreados y el % de varianza en los ejes? | |
| ¿La ficha tiene nombre, tamaño, perfil y acción por segmento? | |
| ¿El recomendador está evaluado con RMSE y precision@3 y comparado con la popularidad? | |
| ¿`recomendar` no propone experiencias ya valoradas? | |
| ¿Hay al menos dos riesgos específicos de IA responsable? | |
| ¿Cada persona ha hecho *commit* de su parte? | |

### Si os atascáis

- **Todos los segmentos se parecen:** revisad que habéis escalado y probad otras columnas; quizá algunas no aportan.
- **PCA nos da un mapa en el que todo está mezclado:** es posible; decidlo en la ficha. Los grupos pueden estar separados en dimensiones que el 2D no recoge.
- **El recomendador recomienda siempre lo mismo:** probablemente es un sesgo de popularidad; comentadlo como riesgo.
- Más ayuda: [Cómo se trabaja un reto](../../../material/4.%20Como_se_trabaja_un_reto.md).

### Qué se enseña en la review
Cada equipo presenta en 3 minutos: **sus segmentos (nombre + acción)** y **una recomendación concreta para un usuario**. Se comparan los `k` elegidos y se discute *¿es el mismo cliente aunque le pongamos otro nombre?*

## Definition of Done (lista de comprobación)

Si queda una casilla sin marcar, **el reto no está terminado**.

- [ ] El notebook se ejecuta de arriba abajo sin errores y con semillas fijas.
- [ ] Variables escaladas antes de agrupar; `k` justificado con silueta **y** con criterio de negocio.
- [ ] Mapa 2D (PCA) con los segmentos coloreados y ejes con el % de varianza.
- [ ] Ficha de segmentos con nombre, tamaño, perfil y acción por segmento.
- [ ] Recomendador evaluado con RMSE y precision@3, comparado con la popularidad.
- [ ] `recomendar(id_usuario, n)` no propone experiencias ya valoradas.
- [ ] Nota de IA responsable con al menos dos riesgos específicos.
- [ ] Cada persona del equipo ha hecho *commit* de su parte.
- [ ] [Autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md) rellenadas (cada persona sube su hoja).
