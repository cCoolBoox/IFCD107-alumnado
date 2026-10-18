# Sprint 13 · Reto «Informe visual para dirección»

> **Esta es la ficha completa del reto, explicada paso a paso** para quien nunca ha trabajado con esta metodología ni con IA. Léela entera **antes de empezar** y vuelve a ella cuando tengas dudas.
>
> - Si es tu primer reto, lee antes [Cómo se trabaja un reto](../../../material/4.%20Como_se_trabaja_un_reto.md).
> - Volver al [README del sprint](../README.md) · [Guía del sprint en PDF](Guia_Sprint_13.pdf) · [versión ecofriendly para imprimir](Guia_Sprint_13_ecofriendly.pdf).

## Ficha del reto

### En pocas palabras (léelo primero)

**Qué os pide el cliente.** Marcos, el director general de TurisData, tiene **10 minutos** antes de la reunión de ingresos. **No sabe qué es un AUC y no quiere saberlo.** Os pide: *«Una página. ¿Puedo fiarme del modelo, qué mueve las cancelaciones y qué hago el lunes?»*

**Este reto no trata de entrenar mejores modelos**, sino de **comunicar**. Muchos proyectos de IA fracasan no porque el modelo sea malo, sino porque nadie con capacidad de decidir entiende lo que dice. Aquí aprenderéis a convertir un modelo en **una página que se entiende en 30 segundos**.

**Qué vais a hacer, en cinco pasos:**
1. **Elegir vuestro mejor modelo del curso** y cargarlo en la plantilla (`S13_02_plantilla_informe_visual`).
2. **Acordar el coste de los errores** (¿cuánto cuesta una habitación vacía?).
3. **Ajustar 4 gráficos**, cada uno con un título que **diga una conclusión**.
4. **Escribir el titular-decisión y 3 viñetas** sin jerga.
5. **Probar el informe con otro equipo:** ¿entienden la decisión en 30 segundos?

**Qué vais a entregar:** un informe visual de **una sola página** (`informe_visual.md` con el PNG del panel, o un PDF de una página) y el cuaderno adaptado, guardados en el repositorio del equipo. **Será la semilla de la memoria técnica** del proyecto final.

**Qué vais a aprender haciéndolo:** a **comunicar datos a una persona sin formación técnica**: escribir titulares que sean decisiones, hacer gráficos honestos y eliminar la jerga.

**Cuánto tiempo:** 1 hora. Es corto, así que **llegad con el modelo elegido**.

### Palabras que van a aparecer en este reto

| Palabra | Qué significa, en sencillo |
|---|---|
| **Titular-decisión** | Una frase que dice **qué hay que hacer**, no solo qué pasa. «Llamar a las 30 reservas de mayor riesgo cada lunes» |
| **Título-conclusión** | El título de un gráfico enuncia lo que enseña: «Las reservas flexibles se cancelan el doble», no «Cancelaciones por tarifa» |
| **Jerga** | Palabras técnicas que el público no conoce (AUC, F1, SHAP…). Si aparece, hay que explicarla en una frase |
| **AUC** | Número que resume lo bien que el modelo separa quienes cancelan de quienes no |
| **F1** | Número que combina cuántos avisos acierta y cuántas cancelaciones detecta |
| **SHAP** | Forma de mostrar qué variables empujan más la decisión del modelo |
| **Falso negativo / positivo** | Cancelación no detectada / falsa alarma |
| **Pie del informe** | Línea final con los datos usados, el modelo, los límites y los responsables |
| **Subgrupo** | Una parte de los clientes (por país, canal…). Se mira si el modelo funciona igual en todos |

### El cliente
Marcos, director general de **TurisData Canarias**, tiene 10 minutos antes de la reunión de ingresos. No sabe qué es un AUC y no quiere saberlo. Pide: *«Una página. ¿Puedo fiarme del modelo, qué mueve las cancelaciones y qué hago el lunes?»*

### Qué se entrega y en qué formato
1. **Informe visual de una página** (`informe_visual.md` con el PNG del panel, o un PDF de una página) siguiendo `plantilla_informe_visual.md`: titular-decisión, 4 gráficos, 3 viñetas, pie con datos y responsables.
2. El **notebook** `S13_02_plantilla_informe_visual` adaptado a **vuestro mejor modelo del curso**, ejecutable de arriba abajo.
3. Es la **semilla de la memoria técnica** del proyecto final: guardadlo en el repositorio del equipo.

### Restricciones
- **Una sola página**, legible proyectada. Máximo 4 gráficos.
- Sin jerga: si aparece «AUC», «F1» o «SHAP» debe ir con una frase que lo explique.
- Cifras del texto = cifras del gráfico. Semillas fijas.
- Trabajad en equipos de 3-4 y repartid: modelo, gráficos, texto y revisión cruzada.

### Criterios de evaluación (rúbrica de retos, de 1 a 4)

| Criterio | 1 · Insuficiente | 2 · Suficiente | 3 · Bueno | 4 · Excelente |
|---|---|---|---|---|
| **Corrección técnica** | Gráficos mal calculados (p. ej. métricas sobre entrenamiento) | Gráficos correctos con fallos menores | Métricas sobre el test, umbral explicado y gráficos bien construidos | Además compara dos modelos o umbrales y justifica la elección |
| **Reproducibilidad** | No se puede volver a ejecutar | Se ejecuta con ayuda | Se ejecuta de arriba abajo con semillas fijas | Además incluye datos o script, versiones y el PNG generado |
| **Análisis y comunicación al cliente** | Cifras sin interpretar; título descriptivo | Interpretación básica; algún título-conclusión | Titular-decisión, títulos-conclusión y texto sin jerga | Además cuantifica el valor en euros y una recomendación accionable con límites |
| **IA responsable** | No se considera | Mención genérica de «sesgos» | Riesgos específicos (uso indebido, grupos peor atendidos) | Además comprueba el rendimiento por subgrupos y propone medidas |

### Pasos sugeridos
| Minutos | Qué hacer |
|---|---|
| 0-10 | Elegid el modelo y confirmad que se carga en la plantilla. Fijad costes de FN y FP con el cliente (¿cuánto cuesta una habitación vacía?). |
| 10-30 | Ajustad los cuatro gráficos y su título-conclusión. |
| 30-50 | Redactad el titular y las 3 viñetas; comprobad cifras. |
| 50-60 | Revisión cruzada con otro equipo: *«¿Entiendes la decisión en 30 segundos?»* |

### Guía paso a paso para principiantes

#### Minutos 0–10 · Elegir el modelo y fijar los costes
1. **Elegid vuestro mejor modelo del curso** (el campeón del Sprint 8, por ejemplo) y comprobad que se carga en la plantilla sin errores.
2. **Fijad los costes de los errores con el cliente** (el docente): ¿cuánto cuesta una habitación vacía? ¿y molestar a un cliente que no iba a cancelar? Si no los sabéis, **proponed una hipótesis** y escribidla.

#### Minutos 10–30 · Los cuatro gráficos
Elegid **cuatro gráficos** que respondan a tres preguntas del director:
- **¿Puedo fiarme del modelo?** (por ejemplo, aciertos y errores en datos que no vio).
- **¿Qué mueve las cancelaciones?** (las variables más influyentes).
- **¿Qué hago el lunes?** (a cuántas reservas llamar y cuánto se ahorra).

Para cada gráfico:
- **Título que enuncia una conclusión** («El 70 % de las cancelaciones se concentra en tarifas flexibles»).
- **Ejes con nombre.**
- **Barras que empiezan en 0.** Nada de 3D. Máximo 3–4 colores con sentido.
- **Calculado sobre el test**, no sobre el entrenamiento.

#### Minutos 30–50 · Titular y viñetas
1. **Titular-decisión** (una línea): «Llamar cada lunes a las 25 reservas con más riesgo evitaría unas 8 habitaciones vacías al mes».
2. **Tres viñetas**, una por pregunta del director: fiabilidad, causas, acción.
3. **Pie:** con cuántos datos, qué modelo, qué límites y quién es responsable.
4. **Comprobad que las cifras del texto son las mismas que las del gráfico.**
5. **Traducid la jerga:** si aparece «AUC», añadid «(nota de 0,5 a 1 de lo bien que separa quién cancela)».

#### Minutos 50–60 · Revisión con otro equipo
Pasad vuestra página a otro equipo y preguntad: **«¿Entiendes la decisión en 30 segundos?»** Si no la entienden o entienden otra, **el mensaje no está claro**: reescribid el titular.

### Cómo usar la IA en este reto

| Para qué | Ejemplo de petición | Qué tenéis que comprobar |
|---|---|---|
| Quitar jerga | «Reescribe estas tres viñetas para un director que no sabe estadística. No cambies ninguna cifra: *[viñetas]*» | Que **las cifras son idénticas** |
| Probar titulares | «Dame 5 versiones de este titular, cada una de menos de 15 palabras, que enuncien una decisión: *[titular]*» | Que la elegida siga siendo verdad |
| Mejorar un gráfico | «Este título describe el gráfico pero no concluye: *[título]*. Propón títulos-conclusión» | Que la conclusión **se vea realmente** en el gráfico |
| Simular al director | «Hazte pasar por un director de hotel sin formación técnica. Lee esta página y dime qué no entiendes» | Que tomáis nota y corregís |

**Reglas del reto:**
- **Una sola página**, legible proyectada, **máximo 4 gráficos**.
- Si aparece «AUC», «F1» o «SHAP», **va con una frase que lo explique**.
- **Cifras del texto = cifras del gráfico.** La IA es muy mala copiando cifras: revisadlas.
- Declarad el uso de IA en el pie o en el README.

### Errores frecuentes (y cómo evitarlos)

| Error | Por qué ocurre | Cómo evitarlo |
|---|---|---|
| Un informe lleno de gráficos y sin decisión | Se muestra todo lo que se hizo | Cuatro gráficos, un titular |
| Títulos descriptivos («AUC por modelo») | Es lo que sale por defecto | «El modelo detecta 7 de cada 10 cancelaciones» |
| Barras que no empiezan en 0 | La herramienta lo hace sola | Fijad el eje a 0 |
| Métricas sobre entrenamiento | Se reutiliza el cuaderno sin mirar | Comprobad que usan el test |
| Jerga sin explicar | Se escribe para el docente | La prueba de los 30 segundos con otro equipo |
| Texto con cifras distintas del gráfico | Se edita una y no la otra | Revisión cruzada |

### Un buen resultado se parece a…

**Titular:** *«Llamar cada lunes a las 25 reservas de mayor riesgo evitaría unas 8 habitaciones vacías al mes (≈ 800 €)».*

**Viñetas:**
- **¿Puedo fiarme?** «Detecta 7 de cada 10 cancelaciones; de cada 10 avisos, 6 son correctos».
- **¿Qué las mueve?** «La tarifa flexible y reservar con más de 90 días de antelación».
- **¿Qué hago el lunes?** «Llamar a las 25 reservas con más riesgo y ofrecer cambio de fechas».

**Pie:** «Modelo: bosque aleatorio. Datos: 12.000 reservas sintéticas. Límite: no probado con datos reales. Responsables: equipo X». (Cifras de ejemplo.)

### Antes de entregar: autoevaluación rápida

| Pregunta | Sí / No |
|---|---|
| ¿Es una sola página con titular-decisión, 4 gráficos, 3 viñetas y pie? | |
| ¿Cada gráfico tiene título-conclusión y ejes con nombre? | |
| ¿Las barras empiezan en 0, sin 3D y con 3–4 colores con sentido? | |
| ¿Las métricas están calculadas sobre el test? | |
| ¿Indicamos con cuántos datos, qué modelo y qué límites? | |
| ¿El cuaderno se ejecuta de arriba abajo con semillas fijas? | |
| ¿Otro equipo entendió la decisión en 30 segundos? | |
| ¿Está guardado en el repositorio del equipo como semilla de la memoria? | |

### Si os atascáis

- **El tiempo se acaba:** reducid a tres gráficos y escribid primero el titular y las viñetas; los gráficos se ajustan después.
- **No sabemos qué decisión recomendar:** pensad en una acción con persona y fecha («recepción llama los lunes»).
- **El modelo no carga en la plantilla:** comprobad que usáis el mismo preprocesado con el que se entrenó.
- Más ayuda: [Cómo se trabaja un reto](../../../material/4.%20Como_se_trabaja_un_reto.md).

### Qué se enseña en la review
Cada equipo proyecta su página 30 segundos y **el resto de la clase dice la decisión que entiende**. Si no coincide con la del equipo, el mensaje no está claro. Se comparan los titulares y se elige el más claro.

## Definition of Done (lista de comprobación)

Si queda una casilla sin marcar, **el reto no está terminado**.

- [ ] Una sola página con titular-decisión, 4 gráficos, 3 viñetas y pie.
- [ ] Cada gráfico tiene título que enuncia una conclusión y ejes con nombre.
- [ ] Las barras empiezan en 0; sin 3D; máximo 3-4 colores con sentido.
- [ ] Métricas calculadas **sobre el test**.
- [ ] Se indica con cuántos datos, qué modelo y qué límites.
- [ ] El notebook se ejecuta de arriba abajo con semillas fijas.
- [ ] Guardado en el repositorio del equipo como semilla de la memoria.
