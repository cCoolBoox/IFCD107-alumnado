# 🎒 Bolsa de miniretos · S07

## 🔟 El decálogo
1. **No se puede usar IA** (ni chatbots ni asistentes de código): el código lo pegáis de la ficha y lo entendéis entre todos.
2. **5 minutos para elegir** miniapp. Pasado ese tiempo, empieza el reloj.
3. **55 minutos como máximo** para construirla. Si no llegáis a todo, enseñad lo que tengáis.
4. **Un modelo tonto de referencia** (siempre la media o siempre la clase más común). Si no lo superáis, no habéis hecho nada.
5. **Separad train y test antes de nada.** El examen (`test`) se mira **una sola vez**, al final.
6. **Comparad al menos 3 modelos** con validación cruzada sobre `train` y decid el campeón por la tabla.
7. **Medid en unidades reales** (euros, dólares, kWh o personas), no solo con el R² o el AUC.
8. **En clasificación, el umbral se elige con costes** y sobre `train`, nunca mirando el examen.
9. **Probad vuestra app con 3 casos propios** y contad dónde falla.
10. **Rotad el teclado:** en pareja o en trío, quien escribe cambia cada 10 minutos y todos sabéis explicar cada celda.

## 📦 Qué entregar
Una carpeta `sprint-07/miniretos/` en el repositorio de vuestro equipo con **dos archivos**:
- **El cuaderno** de Colab, ejecutado y sin errores (*Archivo → Descargar → .ipynb*).
- **Un `README.md`** con:
  - La miniapp elegida y quién la hizo.
  - La **tarjeta de cierre** (4 frases):
    - **Mi app decide** ______ a partir de ______.
    - **Se equivoca de media** ______ (en euros, dólares o kWh), frente a ______ del modelo tonto.
    - **Falla cuando** ______.
    - **No debe usarse para** ______.
  - La **tabla de modelos** del duelo, con el campeón marcado.
  - Los **3 casos** que probasteis con la app y **dónde falló**.
- Es práctica extra: **no entra en la rúbrica**, pero se puede enseñar en la defensa final.

## 🎤 Qué hacer en la demo (2 minutos por equipo)
- Enseñad el **gráfico clave** (la curva, el umbral o los odds ratios) y explicadlo en una frase.
- Enseñad la app con **un caso que acierta** y **uno que falla**.
- Una pregunta de la clase y, después, la siguiente.

## 🧰 Las miniapps
**Elige una miniapp de IA y enséñasela a la clase.** Sin TurisData: otros datos, solo lo que ya conocéis hasta el Sprint 7 (regresión, clasificación, umbral y métricas).

- **Con quién:** en pareja o en equipo de tres.
- **Dónde:** en Google Colab, con un cuaderno nuevo. Cada ficha trae las celdas para copiar y pegar, **una por paso**. No hay que instalar nada.
- **Qué se ve al final:** un gráfico, una tabla de modelos frente al modelo tonto y una **app** (una función que probáis con casos vuestros).

| | Miniapp | Pregunta | Tipo | Lo que verás | Nivel | Practica |
|---|---|---|---|---|---|---|
| 💳 | [01 · Fraude con tarjeta](01_Fraude_con_tarjeta.md) | ¿Esta compra es un fraude? | Clasificar con **clases muy desiguales** (1,5 %) | El que nunca avisa acierta el 98,5 %; el umbral por coste baja las pérdidas de ≈ 11 150 € a ≈ 3 200 € | ⭐⭐⭐ | Precisión engañosa, ROC y PR, umbral por coste |
| 🎬 | [02 · Abandono de suscripción](02_Abandono_de_suscripcion.md) | ¿Quién va a darse de baja? | Clasificar y **explicar** | Problema **difícil** (AUC ≈ 0,73): contactar a todos pierde dinero, solo a los de riesgo gana | ⭐⭐ | Logística, odds ratios, coste de campaña |
| 💎 | [03 · Precio de diamantes](03_Precio_de_diamantes.md) | ¿Cuánto vale este diamante? | **Regresión** con datos reales | Cambiar a **logaritmo** casi **divide el error por dos**; la recta empata con el bosque | ⭐⭐ | Lineal, `log(precio)`, Ridge, variables de texto |
| ⚡ | [04 · Factura de la luz](04_Factura_de_la_luz.md) | ¿Cuánta luz gastará mi casa? | Regresión **no lineal** | La nube es una **U**: la curva de grado 2 (error 0,60 kWh) gana a la recta (1,17) y al bosque | ⭐⭐ | Curva polinómica, sobreajuste, Ridge, kWh y euros |

## Qué datos hay detrás
- **En el repositorio del curso** (`datos/`): `fraude_tarjeta.csv`, `abandono_streaming.csv` y `consumo_solar.csv`, **inventados**, y `diamantes.csv`, una **muestra real** de 6 000 diamantes (conjunto `diamonds` de ggplot2).

## Y si queréis otra
- Proponed una miniapp con **datos abiertos** (una tabla con una columna que predecir) y una pregunta cerrada. El docente os dice si encaja.
