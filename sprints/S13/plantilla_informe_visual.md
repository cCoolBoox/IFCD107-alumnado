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
