# Informe visual · [Nombre del modelo] para TurisData Canarias

**Para:** Dirección · **Equipo:** ______ · **Fecha:** ______ · **Versión:** 1

---

## TITULAR: [La decisión que recomendáis en una frase]
*Ejemplo: «Pedir depósito y avisar a las reservas de riesgo alto ahorra unos 17 000 € por cada 1 500 reservas».*

## Los cuatro gráficos

| ¿Podemos fiarnos del modelo? | ¿Qué falla y cuánto? |
|---|---|
| **[Título-conclusión]** — Gráfico 1: curva ROC o PR | **[Título-conclusión]** — Gráfico 2: matriz de confusión (en %) |
| *Una frase: qué muestra y qué significa.* | *Una frase: qué error es más caro y por qué.* |
| **¿Qué mueve el resultado?** | **¿Cuánto vale?** |
| **[Título-conclusión]** — Gráfico 3: importancia de variables | **[Título-conclusión]** — Gráfico 4: ahorro en € con y sin el modelo |
| *Una frase: la variable líder y su lectura de negocio.* | *Una frase: supuestos de coste (FN = __ €, FP = __ €).* |

*(Panel generado por el notebook: `informe_visual_panel.png`.)*

## Tres viñetas
- **Qué hemos hecho:** [1-2 líneas, sin jerga. Cuántos datos, qué se predice.]
- **Qué recomendamos:** [Acción concreta, para quién, con qué umbral, ahorro esperado y cuándo empezar.]
- **Qué límites tiene:** [Datos (sintéticos/periodo), dónde falla más, qué NO debe usarse para decidir, cuándo se revisa.]

## IA responsable (2 líneas)
[Riesgo específico y medida. Ej.: «El modelo no debe usarse para negar reservas a nadie; solo para priorizar avisos. Se revisará por país de origen cada trimestre.»]

## Pie
Datos: ______ (n = ___, periodo ___) · Modelo: ______ · Umbral: ___ · Semilla: 42 · Notebook: `S13_02_...` · Responsable: ______

---

### Lista de comprobación antes de entregar
- [ ] ¿Entiende la decisión una persona no técnica en 30 segundos?
- [ ] ¿Cada título dice algo que se pueda **discutir** (una conclusión), no solo describe?
- [ ] ¿Barras desde 0, ejes con nombre y unidades, colores con sentido?
- [ ] ¿Métricas del **test**, no del entrenamiento?
- [ ] ¿Las cifras del texto coinciden con las del gráfico?
- [ ] ¿Figura al menos un límite y un riesgo?
- [ ] ¿Cabe en una página y se lee proyectada?

### Reglas de oro de comunicación de datos
1. **Un gráfico, un mensaje.** 2. **El título es la conclusión.** 3. **Ejes honestos** (barras desde 0). 4. **Color con sentido**: uno para destacar, gris para el resto; accesible a daltónicos. 5. **Nada de 3D ni tartas** de más de 3 trozos. 6. **Etiqueta directa** de los valores. 7. **Di lo que no sabes**: tamaño de la muestra, incertidumbre, límites.

---

## Revisión con la rúbrica
*(Esto va **debajo** de la página del informe: no forma parte de la hoja que ve dirección. Lo rellena quien revisa y **no escribió esa parte**: ejecutar el cuaderno, leer la página como si fuerais Marcos, mirar los gráficos, poner nivel con prueba. La rúbrica completa está en la ficha del reto, apartado 3.)*

**Revisado por:** <nombre> · **Fecha:** <dd/mm/aaaa>

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
|---|---|---|
| Corrección técnica | <1–4> | <p. ej. «4 gráficos sobre el test, pero el eje del gráfico 4 no empieza en 0»> |
| Reproducibilidad | <1–4> | <¿sale el mismo PNG y las mismas cifras al reiniciar y ejecutar todo el cuaderno?> |
| Análisis y comunicación al cliente | <1–4> | <¿entiende la decisión una persona de otro equipo en 30 segundos? ¿coinciden las cifras del texto y del gráfico?> |
| IA responsable | <1–4> | <¿hay un riesgo concreto y una medida, y se dice qué se pidió a la IA y qué se revisó?> |

**Lo primero que mejoraríamos:** <una cosa concreta>
