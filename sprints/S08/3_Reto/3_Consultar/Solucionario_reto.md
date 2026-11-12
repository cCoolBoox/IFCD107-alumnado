# Solucionario del reto · Sprint 8 · «Duelo de modelos»

> **Para contrastar y para entender**, no solo para copiar. El **código** de cada paso ya está en su [página del reto](Reto_Sprint_08_paso_2.md) (con «Qué hace cada línea»). Aquí están las cifras para comprobar y las respuestas de ejemplo de lo que se escribe con palabras propias. **¿Cómo queda una entrega completa?** Mirad la [entrega de ejemplo](Solucionario/README.md): los ficheros que se suben a `sprint-08/`. Volver a la [ficha del reto](Reto_Sprint_08.md).

## Índice

- [Cómo usarlo](#cómo-usarlo)
- [Las cifras que tienen que salir](#las-cifras-que-tienen-que-salir)
- [Paso 1 · Planning y pesos](#paso-1--planning-y-pesos)
- [Paso 2 · Primeros modelos](#paso-2--primeros-modelos)
- [Paso 3 · Boosting, SVM y búsqueda](#paso-3--boosting-svm-y-búsqueda)
- [Paso 4 · Elegir el campeón](#paso-4--elegir-el-campeón)
- [Paso 5 · Model card: respuestas de ejemplo](#paso-5--model-card-respuestas-de-ejemplo)

## Cómo usarlo

- **Primero intentadlo.** Si algo falla: leed el error → «Si algo falla» de la página del paso → equipo → docente → **este solucionario**.
- **Después de mirarlo, cerradlo y volved a escribirlo con vuestras palabras.**
- Los **AUC** son los mismos en cada ejecución (con `SEMILLA = 42`); los **tiempos y tamaños** cambian de un ordenador a otro, así que las notas de coste y la puntuación global pueden variar unas centésimas.

## Las cifras que tienen que salir

| Dónde | Cifra | Qué es |
|---|---|---|
| Paso 2 | `Train: 4800 · Test: 1200` | Partición; el test no se mira hasta el final |
| Paso 2 | `logistica` AUC ≈ `0,755 ± 0,014` · `baseline` `0,500` | Primera tabla |
| Paso 2 | tras el ejercicio 2: `logistica` 0,755 · `random_forest` 0,737 · `arbol_podado` 0,719 · `baseline` 0,500 | Cuatro filas |
| Paso 3 | `lightgbm` 0,745 · `svm_rbf` 0,735 | Los dos modelos nuevos |
| Paso 3 | Búsqueda del bosque: mejor AUC `0.7435` | 8 combinaciones entre 0,741 y 0,744 |
| Paso 3 | Búsqueda de LightGBM: mejor AUC `0.747` | Ajustes con decimales (son sorteos) |
| Paso 3 | `8 modelos de 6 familias` | `lightgbm_ajustado` 0,747 · `random_forest_ajustado` 0,744 |
| Paso 4 | pesos 0,5 / 0,3 / 0,2 → campeón `logistica` (≈ 0,92) · `arbol_podado` ≈ 0,91 | Puntuación global |
| Paso 4 | `AUC en test 0.7623` (solo en la fila del campeón; el resto `NaN`) | Examen final, una sola vez |

## Paso 1 · Planning y pesos

- Pesos de ejemplo: **50 % rendimiento · 30 % explicabilidad · 20 % coste** (suman 100 %).
- Una frase de por qué para cada uno, por ejemplo: «Rendimiento 50 %: el gerente quiere avisar bien. Explicabilidad 30 %: tiene que poder contárselo a recepción. Coste 20 %: el hotel no tiene servidor propio.»

## Paso 2 · Primeros modelos

- El `AssertionError` del ejercicio 2 es **esperado** hasta que hay baseline, logística y al menos cuatro modelos más.
- El bosque es el que más pesa (`tamano_kb` de unos 11 800 KB, frente a menos de 11 KB en los demás).
- `leaderboard_S08.csv` aparece en el panel de archivos de Colab.

## Paso 3 · Boosting, SVM y búsqueda

- Las mejoras de los modelos ajustados son de **milésimas**, menores que la desviación (± 0,014): «no podemos asegurar que sean mejoras reales».
- La SVM es la que más tarda por prueba y la que menos se explica.

## Paso 4 · Elegir el campeón

| Pesos (rendimiento / explicabilidad / coste) | Campeón |
|---|---|
| 0,5 / 0,3 / 0,2 (los de ejemplo) | `logistica` |
| 0,8 / 0,1 / 0,1 (solo rendimiento) | `logistica` |
| 0,4 / 0,4 / 0,2 (equilibrado) | `arbol_podado` (ventaja corta: ≈ 0,93 frente a ≈ 0,90) |
| 0,2 / 0,6 / 0,2 (explicabilidad primero) | `arbol_podado` |

- **El campeón cambia con los pesos:** la recomendación depende de lo que valore el cliente, y así hay que contarlo.
- **Examen final:** `Campeón: logistica · AUC en validación cruzada 0.755 · AUC en test 0.762`. Un test parecido al de validación (aquí unas 0,007 más alto) indica que no hay sobreajuste; uno **mucho** más bajo sí lo sería.
- **Una sola vez:** después de ver el número del test no se cambia el campeón. En `leaderboard_S08.csv`, `auc_test` tiene valor en **una sola fila**.
- Con otros pesos o modelos ajustados vuestro campeón puede ser otro: vale si lo justificáis con vuestras notas.

## Paso 5 · Model card: respuestas de ejemplo

| Apartado | Ejemplo |
|---|---|
| 1. Resumen | «Calcula la probabilidad de que una reserva se cancele, para que el gerente de TurisData sepa a quién avisar.» |
| 2. Modelo campeón | «Regresión logística (familia lineal), `max_iter=1000`, variables escaladas. Versiones de scikit-learn, xgboost y lightgbm de vuestra última celda.» |
| 3. Por qué este campeón | «Pesos 50 / 30 / 20. `logistica`: AUC 0,755 ± 0,014 y explicabilidad 4. Mejor rival, `arbol_podado`: pierde unas 0,035 de AUC, pero se explica mejor (5). Con pesos que priorizan la explicabilidad gana el árbol.» |
| 5. Rendimiento | «Test (una sola evaluación): AUC 0,762. Umbral: el del Sprint 7, justificado por el coste de una cancelación no prevista frente a una falsa alarma.» |
| 6. Uso previsto y NO previsto | «Para priorizar llamadas de recordatorio. **No** para denegar reservas, cobrar más a un país o decidir sin revisión humana.» |
| 8. Riesgos | «País y canal pueden sesgar el aviso; las falsas alarmas molestan a clientes que sí iban a venir. Medimos la tasa de aviso por canal.» |
| 9. Mantenimiento | «Vigilar la tasa de cancelación real frente a la prevista; reentrenar cuando se desvíe de forma sostenida.» |

- Rellenar con **vuestras** cifras, las del último «Reiniciar y ejecutar todo».
- **Error frecuente:** copiar números de una ejecución anterior; la *model card* debe coincidir con el cuaderno entregado.
