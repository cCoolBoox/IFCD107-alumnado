# 🎒 Bolsa de miniretos · S07

**Elige una miniapp de IA, constrúyela en 50–60 minutos y enséñasela a la clase.** Sin TurisData: otros datos, otras preguntas y solo lo que ya conocéis hasta el Sprint 7 (regresión, clasificación, umbral y métricas).

- **Cuándo:** al cerrar S07, en casa o cuando acabéis antes. **Opcional**: no entra en la rúbrica del reto. (No sustituye al Día 2 del Sprint.)
- **Con quién:** en pareja o en equipo de tres. Un equipo puede hacer **dos** miniapps.
- **Dónde:** en Google Colab, con un cuaderno nuevo. Cada ficha trae las celdas para copiar y pegar, **una por paso**. No hay que instalar nada.
- **Qué se ve al final:** un gráfico, una tabla de modelos frente al modelo tonto y una **app** (una función que probáis con casos vuestros).

## Las miniapps

| | Miniapp | Pregunta | Tipo | Nivel | Practica |
|---|---|---|---|---|---|
| 💳 | [01 · Fraude con tarjeta](01_Fraude_con_tarjeta.md) | ¿Esta compra es un fraude? | Clasificar con **clases muy desiguales** (1,5 %) | ⭐⭐⭐ | Precisión engañosa, ROC y PR, umbral por coste |
| 🎬 | [02 · Abandono de suscripción](02_Abandono_de_suscripcion.md) | ¿Quién va a darse de baja? | Clasificar y **explicar** | ⭐⭐ | Logística, odds ratios, coste de campaña |
| 💎 | [03 · Precio de diamantes](03_Precio_de_diamantes.md) | ¿Cuánto vale este diamante? | **Regresión** con datos reales | ⭐⭐ | Lineal, `log(precio)`, Ridge, variables de texto |
| ⚡ | [04 · Factura de la luz](04_Factura_de_la_luz.md) | ¿Cuánta luz gastará mi casa? | Regresión **no lineal** | ⭐⭐ | Curva polinómica, sobreajuste, Ridge, kWh y euros |

## Cómo elegir
- **Quiero un reto de verdad:** 💳 fraude con tarjeta.
- **Quiero entender qué dice un modelo:** 🎬 abandono de suscripción.
- **Me gustan los datos reales y los precios:** 💎 diamantes.
- **Quiero ver una curva que se dobla:** ⚡ factura de la luz.

## Las 6 reglas (valen para todas)
1. **Un modelo tonto de referencia** (siempre la media o siempre la clase más común). Si no lo superáis, no habéis hecho nada.
2. **Separad train y test antes de nada.** El examen (`test`) se mira **una sola vez**, al final.
3. **Comparad al menos 3 modelos** con validación cruzada sobre `train` y decid el campeón por la tabla.
4. **Medid en unidades reales** (euros, dólares, kWh o personas), no solo con el R² o el AUC.
5. **En clasificación, el umbral se elige con costes** y sobre `train`, nunca mirando el examen.
6. **Probad vuestra app con 3 casos propios** y contad dónde falla.

## Tarjeta de cierre (4 frases, en la hoja compartida)
- **Mi app decide** ______ a partir de ______.
- **Se equivoca de media** ______ (en euros, dólares o kWh), frente a ______ del modelo tonto.
- **Falla cuando** ______.
- **No debe usarse para** ______.

## La demo (2 minutos por equipo)
- Enseñad el **gráfico clave** (la curva, el umbral o los odds ratios) y explicadlo en una frase.
- Enseñad la app con **un caso que acierta** y **uno que falla**.
- Una pregunta de la clase y, después, la siguiente.

## Qué datos hay detrás
- **En el repositorio del curso** (`datos/`): `fraude_tarjeta.csv`, `abandono_streaming.csv` y `consumo_solar.csv`, **inventados**, y `diamantes.csv`, una **muestra real** de 6 000 diamantes (conjunto `diamonds` de ggplot2).

## Para subirlo (opcional)
- Descargad el cuaderno de Colab (*Archivo → Descargar → .ipynb*) y subidlo a `sprint-07/miniretos/` de vuestro repositorio, con la tarjeta de cierre en un `README.md`.
- Es práctica extra: no se evalúa con la rúbrica, pero se puede enseñar en la defensa final.

## Y si queréis otra
- Proponed una miniapp con **datos abiertos** (una tabla con una columna que predecir) y una pregunta cerrada. El docente os dice si encaja.
