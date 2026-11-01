# Paso 4 · Pipeline y baseline (día 2, 15 minutos)

<!--nav-->
> Sprint 6 · Reto «Datos sucios, cliente impaciente» · paso 4 de 5 · [Ficha del reto](Reto_Sprint_06.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_06_una_pagina.md) · [Paso 5 →](Reto_Sprint_06_paso_5.md)
<!--/nav-->

1. Construir un `Pipeline` que impute, escale y codifique.
2. Añadir un modelo de referencia y un `DummyClassifier`.
3. Compararlos con validación cruzada y escribir la frase del resultado.

**Cómo se hace**
- **Columnas.** Separad las numéricas de las de texto (categóricas) de `X`. Ojo: `regimen` es de texto y tiene huecos; irá por la rama categórica, que los rellena con el valor más frecuente.
- **El *pipeline*.** Un `ColumnTransformer` con dos ramas: numéricas con `SimpleImputer(strategy="median")` y `StandardScaler()`; categóricas con `SimpleImputer(strategy="most_frequent")` y `OneHotEncoder(handle_unknown="ignore")`. Después, un `Pipeline` que une el preprocesado con `LogisticRegression(max_iter=1000)`. Como todo va dentro del `Pipeline`, se ajusta **solo con los datos que le pasáis a `fit`**: eso evita la fuga.
- **El modelo «tonto».** El mismo `Pipeline`, pero con `DummyClassifier(strategy="prior")` en el último paso.
- **Validación cruzada.** `cross_val_score(modelo, X_train, y_train, cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=42), scoring=...)`. Elegid una métrica que mire las cancelaciones (`"f1"` o `"roc_auc"`) y decid cuál y por qué. **Con `"roc_auc"`, el baseline debe salir en torno a 0,5**.
- **La frase.** «Nuestro modelo obtiene un F1 medio de … ± …, frente a … del modelo tonto. Eso significa que …». Va en el apartado 4 del informe.
- Pista de cuaderno: [`S06_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/2_Practica/S06_03_preprocesado_pipeline.ipynb) (*pipeline*) y [`S06_04`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/2_Practica/S06_04_metricas_validacion.ipynb) (*baseline* y validación cruzada).

**Qué deberíais ver.** Una tabla de dos filas (modelo tonto y vuestro modelo) con la media y la desviación de la métrica en los 5 *folds*, y vuestro modelo por encima del tonto. Si no lo supera, algo falla: mirad la «Ayuda 2».

**Hecho cuando:** el cuaderno tiene el *pipeline*, la tabla de resultados y la frase con media ± desviación, y sabéis explicar por qué el escalado y la imputación no usan el *test*.

<!--nav-->
---

[← Paso 3](Reto_Sprint_06_paso_3.md) · [Ficha del reto](Reto_Sprint_06.md) · [Paso 5 →](Reto_Sprint_06_paso_5.md)
<!--/nav-->
