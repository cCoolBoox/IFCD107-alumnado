# Apuntes del Sprint 13 · Contar lo que hace el modelo: visualizar y comunicar resultados

La presentación del Sprint 13 es muy esquemática. Estos apuntes **explican cada idea con ejemplos pequeños** y te dicen **qué hace falta para que una persona que no sabe de IA entienda tu resultado en 30 segundos**. Léelos antes del cuaderno y antes de empezar el reto.

> **Antes de empezar:** este sprint no enseña modelos nuevos. Usa lo que ya sabes: matriz de confusión (Sprints 1 y 7), umbral por coste (Sprints 3 y 7), importancia por permutación (Sprint 8) y un modelo tuyo (Sprints 8, 10 o 12).

---

## 0. De qué va el sprint (en 1 minuto)

**Marcos**, el director general de TurisData, tiene **10 minutos antes de la reunión de ingresos**. **No sabe qué es un AUC y no quiere saberlo.** Quiere saber tres cosas:

> *«¿Puedo fiarme del modelo? ¿Qué mueve las cancelaciones? ¿Qué hago el lunes?»*

**Muchos proyectos de IA no fracasan porque el modelo sea malo, sino porque nadie que decide entiende lo que dice.** Este sprint es sobre **traducir** un modelo a algo que se pueda **usar para decidir**.

| Pieza | Responde a… | Para Marcos |
|---|---|---|
| **Matriz de confusión** | ¿En qué acierta y en qué falla? | «¿Puedo fiarme?» |
| **Curvas ROC y PR** | ¿Cómo funciona con distintos umbrales? | «¿Qué compromiso hay?» |
| **Importancia por permutación** | ¿Qué variables usa el modelo? | «¿Qué mueve las cancelaciones?» |
| **Umbral y coste** | ¿A partir de cuándo actúo? | «¿Qué hago el lunes?» |
| **Un gráfico para dirección** | ¿Cómo lo enseño? | «Que lo entienda en 30 segundos» |

**El reto:** una **página** (un panel de 4 gráficos + un titular + 3 viñetas sin jerga) que **se entiende en 30 segundos**.

---

# PARTE 1 · Lo que el modelo hace

## 1. La matriz de confusión: en qué acierta y en qué falla

La matriz **cruza lo que pasó con lo que el modelo dijo** (con un umbral de 0,5):

| | Dijo: no cancela | Dijo: cancela |
|---|---|---|
| **Pasó: no canceló** | ✅ Acierto | ⚠️ **Falsa alarma** |
| **Pasó: canceló** | ❌ **Falso negativo** (habitación vacía que se pudo revender) | ✅ Acierto |

```python
cm = confusion_matrix(y_test, (prob_lr >= 0.5).astype(int), normalize="true")
recall = cm[1, 1]            # de las que cancelan, ¿cuántas detectamos?
```

`normalize="true"` **convierte los recuentos en porcentajes por fila** (cada fila suma 1), que es lo que entiende un directivo.

**Ejemplo con 10 reservas** (6 no cancelan y 4 sí), con un umbral de 0,5:

| Recuentos | Dijo: no | Dijo: sí |
|---|---|---|
| **No canceló** (6) | 4 | 2 |
| **Canceló** (4) | 1 | 3 |

**Normalizada por filas:**

| | Dijo: no | Dijo: sí |
|---|---|---|
| **No canceló** | 0,67 | 0,33 |
| **Canceló** | 0,25 | **0,75** ← el recall |

**Frase para Marcos:** *«De cada 4 reservas que se van a cancelar, avisamos de 3.»* (Eso es **recall = 75 %**, dicho sin jerga.)

## 2. Curvas ROC y PR

La matriz **depende de un umbral**. Las curvas **resumen todos los umbrales** a la vez.

| Curva | Ejes | Cómo leerla |
|---|---|---|
| **ROC** | **Falsas alarmas** (X) frente a **cancelaciones detectadas** (Y) | La **diagonal es el azar**; cuanto **más arriba a la izquierda**, mejor |
| **PR** (precisión-exhaustividad) | Recall (X) frente a precisión (Y) | **Más honesta cuando la clase importante es rara** (Sprint 7) |

```python
auc_lr, auc_rf = roc_auc_score(y_test, prob_lr), roc_auc_score(y_test, prob_rf)
mejor = "regresión logística" if auc_lr >= auc_rf else "bosque aleatorio"
```

**Para comparar dos modelos**, se dibujan sus curvas **en el mismo gráfico**: el que queda por encima es mejor. Si se cruzan, **depende del umbral que vayas a usar**.

## 3. ¿Qué variables importan? Importancia por permutación

**Idea:** *si una variable es importante, estropearla debería empeorar el modelo*.

1. Se **desordena al azar una variable del test** (rompiendo su relación con el resultado).
2. Se mide **cuánto empeora el modelo**.

**Ejemplo:** el modelo tiene un AUC de 0,80. Si desordenas `tarifa`, baja a 0,70 → **importancia = 0,10**. Si desordenas `canal`, baja a 0,79 → importancia **0,01**. **Conclusión: la tarifa importa 10 veces más que el canal.**

```python
imp = permutation_importance(modelo, X_test, y_test, n_repeats=10, random_state=SEMILLA)
importancias = pd.Series(imp.importances_mean, index=X_test.columns).sort_values()
```

- **Funciona con cualquier modelo** y sobre **las variables originales** (no sobre columnas transformadas).
- `n_repeats=10` **repite el desorden 10 veces** y promedia (para que no dependa de la suerte).

> ⚠️ **Describe lo que usa el modelo, no una relación causal** (Sprints 5 y 7). «La tarifa pesa mucho en el modelo» **no significa** que cambiar la tarifa cambie las cancelaciones.

*Para el proyecto final existen también **SHAP** (explica **cada predicción individual**) y **Grad-CAM** (para imágenes: **qué zona de la foto miró la red**). Aquí solo debes saber que existen.*

## 4. El umbral lo decide el coste del negocio

Los dos errores **no cuestan lo mismo**:

| Error | Qué ocurre | Coste |
|---|---|---|
| **Falso negativo** | No lo vimos venir y canceló: **habitación vacía que ya no se revende** | **50 €** |
| **Falso positivo** | Avisamos y no cancelaba: **compensación o descuento** para que confirme | **30 €** |

```python
costes = [coste_total(y_test, prob_lr, u) for u in umbrales]       # 50·FN + 30·FP
umbral_optimo = umbrales[int(np.argmin(costes))]
```

**Ejemplo con 10 reservas** (probabilidades del modelo y lo que pasó; 4 cancelaron):

| Prob. | 0,90 | 0,80 | 0,70 | 0,60 | 0,50 | 0,40 | 0,30 | 0,20 | 0,10 | 0,05 |
|---|---|---|---|---|---|---|---|---|---|---|
| ¿Canceló? | sí | sí | no | sí | no | sí | no | no | no | no |

| Umbral | FN | FP | **Coste = 50·FN + 30·FP** |
|---|---|---|---|
| 0,70 | 2 | 1 | 100 + 30 = **130 €** |
| **0,50** (el de siempre) | 1 | 2 | 50 + 60 = **110 €** |
| **0,40** | 0 | 2 | 0 + 60 = **60 €** ← el mejor |
| 0,30 | 0 | 3 | 0 + 90 = **90 €** |
| 0,20 | 0 | 4 | 0 + 120 = **120 €** |

(Aviso = probabilidad **igual o mayor** que el umbral.) **Usar 0,40 en lugar de 0,50 ahorra 50 € en estas 10 reservas.**

> **El 0,5 es una convención, no una decisión.** Recorre de 0,05 a 0,95 y **elige el de menor coste total**; **compáralo con `coste_05`** para poder decir: *«con este umbral ahorramos X € al mes frente al de siempre»*. Marcos entiende los euros; no entiende «umbral 0,4».

---

# PARTE 2 · Contarlo bien

## 5. Seis reglas para un gráfico que dirección entienda

| # | Regla | Ejemplo |
|---|---|---|
| 1 | **Un gráfico, un mensaje.** El **título es la conclusión**, no la descripción | ✅ «Sin depósito se cancela el doble» · ❌ «Tasa de cancelación por depósito» |
| 2 | **Ejes con nombre y unidades; barras siempre desde 0** | Una barra de 52 % y otra de 50 % que empiezan en 49 % parecen una el **triple** de la otra: **trampa** |
| 3 | **Pocos colores con sentido:** destaca lo importante y deja el resto en gris | Una barra roja y las demás grises |
| 4 | **Nada de 3D ni tartas con más de 3 trozos;** etiqueta los valores directamente | `ax.bar_label(...)` en vez de obligar a mirar el eje |
| 5 | **Incertidumbre a la vista:** con cuántos datos y qué no se sabe | «Basado en 6.000 reservas; datos sintéticos» |
| 6 | **Accesible:** colores distinguibles y texto legible al proyectar | Letras grandes; no depender solo de rojo/verde |

**La trampa del eje (regla 2) con números:** dos barras de **52 %** y **50 %**. Con eje desde 0, se ve **casi igual** (como es). Con el eje recortado desde 49 %, una mide 3 unidades y la otra 1: **parece el triple, y solo hay 2 puntos de diferencia.** Eso es **engañar** (y es un tema de IA responsable, Sprint 1).

## 6. El panel de una página

```python
fig, ax = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Titular = la decisión que recomendamos")
# 1 matriz de confusión · 2 curva ROC o PR · 3 importancia · 4 tu gráfico de negocio
```

Cuatro gráficos en una cuadrícula 2×2 y **un titular que es la decisión** («Avisar a toda reserva con riesgo ≥ 40 % evita unos 50 € de pérdida por cada 10 reservas»).

**El gráfico 4 (de negocio), ejercicio 5:** tasa de cancelación (%) por `deposito` (sin_deposito, parcial, total), con:

- `ax.bar_label` (valores escritos sobre las barras),
- `ax.set_ylim(0, …)` (**eje desde 0**),
- **un título que sea una conclusión.**

## 7. El texto del informe: para quien no sabe ML

**Qué hemos hecho → qué hemos encontrado → qué hacer el lunes.** Frases cortas y cifras concretas.

| ❌ Con jerga | ✅ Sin jerga |
|---|---|
| «El modelo logra un AUC de 0,78 con recall del 75 % en el umbral 0,4» | «De cada 4 reservas que se cancelan, **avisamos de 3**; por cada aviso falso, **evitamos varias habitaciones vacías**» |
| «La variable `deposito_total` tiene la mayor importancia por permutación» | «**Las reservas sin depósito son las que más se cancelan**; pedir un depósito parcial podría ayudar» |

**Estructura del informe: titular-decisión + 3 viñetas.** Cada viñeta, **una cifra y una acción**. Será **la semilla de la memoria técnica del proyecto final**.

## 8. Pruébalo con otro equipo

Cierra el ciclo: **enséñale tu página a otro equipo durante 30 segundos** y pregunta: *«¿Qué decisión recomendamos? ¿Qué sabemos y qué no?»*. **Si no lo saben decir, el problema no es de ellos: es del informe.** Reescribe y vuelve a probar.

---

## 9. El reto, en 5 pasos

| Paso | Qué hacer |
|---|---|
| 1 | **Elige tu mejor modelo del curso** (Sprints 8, 10 o 12) y cárgalo en la plantilla `S13_02` |
| 2 | **Acuerda el coste de los errores** (cuánto cuesta un FN y un FP) |
| 3 | **Ajusta 4 gráficos**, cada uno con un título que diga una conclusión |
| 4 | **Escribe el titular-decisión y 3 viñetas sin jerga** |
| 5 | **Pruébalo con otro equipo:** ¿entienden la decisión en 30 segundos? |

## 10. Dónde practicar cada cosa

| Si no entiendes… | Mira la sección | Practica en |
|---|---|---|
| Matriz de confusión, ROC, PR, importancia, umbral y coste | 1-4 | `S13_01_visualizacion_resultados` |
| Reglas de gráficos y panel | 5-6 | Ejercicio 5 del cuaderno S13_01 |
| Informe sin jerga | 7-8 | `plantilla_informe_visual.md` y cuaderno `S13_02_plantilla_informe_visual` |

## 11. Chuleta de vocabulario

| Palabra | En lengua normal |
|---|---|
| **Matriz de confusión** | Tabla de aciertos y errores por tipo |
| **Falso negativo / positivo** | Cancelación no vista / falsa alarma |
| **Recall** | De las que cancelan, cuántas detectamos |
| **Curva ROC / PR** | Resumen del modelo con todos los umbrales |
| **Importancia por permutación** | Desordenar una variable y ver cuánto empeora el modelo |
| **SHAP** | Explicar cada predicción individual |
| **Grad-CAM** | Ver qué zona de la foto miró la red |
| **Umbral** | Probabilidad desde la que se da el aviso |
| **Titular-decisión** | Una frase que dice **qué hacer** |
| **Eje desde 0** | Barras honestas: sin recortar el eje |

## 12. Cómo estudiar estos apuntes

1. **Antes del cuaderno**, lee las secciones 1-4 y **haz a mano el ejemplo del umbral** (sección 4).
2. **Antes del reto**, lee las secciones 5-8: son las que decidirán si tu página se entiende.
3. **Para cada gráfico**, escribe primero **el título-conclusión** y luego construye el gráfico que lo demuestre (y no al revés).
4. **Regla final: si Marcos no lo entiende en 30 segundos, no está terminado.**
