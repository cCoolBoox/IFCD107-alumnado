# Sprint 8 · Reto «Duelo de modelos» · Equipo de ejemplo

Entrega de referencia del docente: sirve de modelo de lo que hay que subir a `sprint-08/`. Es una forma correcta de hacerlo, no la única. Para ver las respuestas paso a paso, el [solucionario del reto](../Solucionario_reto.md); para ver qué se pide, [entrega y rúbrica](../../2_Entregar/entrega_y_rubrica.md).

## Qué se entrega
- [`reto_S08.ipynb`](reto_S08.ipynb): el cuaderno, ejecutado de arriba abajo. Ocho modelos de seis familias, dos de ellos ajustados con búsqueda, pesos, sensibilidad y examen final.
- [`leaderboard_S08.csv`](leaderboard_S08.csv): la tabla de modelos. Lo genera el cuaderno; `auc_test` solo tiene valor en la fila del campeón.
- [`model_card.md`](model_card.md): la ficha del modelo campeón, con los diez apartados.
- `README.md`: este fichero.
- [`autoevaluacion_marta.md`](autoevaluacion_marta.md): la hoja de **una** persona (cada persona del equipo sube la suya).

Un equipo de tres personas sube **4 + 3 = 7** ficheros.

## Quién hizo qué
- Persona A: herramientas del *leaderboard*, ejercicios 1 y 2 y gráfico de rendimiento frente a coste.
- Persona B: búsquedas de hiperparámetros (bosque y LightGBM), pesos y sensibilidad.
- Persona C: examen final en test, *model card*, README y subida a GitHub.
- (Reparto de ejemplo; cada equipo pone sus nombres.)

## Cómo se reproduce
1. Abrir `reto_S08.ipynb` en Google Colab (*Archivo → Subir cuaderno*).
2. *Entorno de ejecución → Reiniciar y ejecutar todo* (tarda un par de minutos). La primera celda descarga `reservas_turisdata.csv` del repositorio del curso.
3. Debe salir el mismo leaderboard y el mismo campeón: **`logistica`**, AUC en validación cruzada 0,755 y **AUC en test 0,762**.

Versiones: Python 3.13, scikit-learn 1.9.1, xgboost 3.3.0, lightgbm 4.7.0 (en Colab saldrán otras; los AUC pueden variar en el último decimal y los tiempos cambian siempre). Semilla: `SEMILLA = 42`; partición propia del reto: `SEMILLA_TEST = 7`.

## Uso de IA
- **Qué se pidió:** explicar la diferencia entre `GridSearchCV` y `RandomizedSearchCV`; entender el error de un `assert` del ejercicio 2; revisar si la *model card* contaba la sensibilidad con claridad.
- **Qué se revisó:** cada línea se ejecutó y se entiende; las cifras de la *model card* salen del cuaderno entregado, no de la IA; los pesos 50 / 30 / 20 y su razón los acordó el equipo con la «voz del cliente».
- **Qué se cambió:** la IA propuso mirar el test para comparar el bosque ajustado con el original; se descartó, porque el test es solo para el campeón y se usa una vez. Los datos son sintéticos: no hay datos personales ni claves.
- (Ejemplo de referencia: cada equipo cuenta lo que hizo de verdad, incluidos los fallos concretos de la IA que detecte.)

## Revisión con la rúbrica
**Revisado por:** Persona D (no escribió la *model card*) · **Fecha:** 12/11/2026

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
|---|---|---|
| Corrección técnica | 3 | Ocho modelos de seis familias medidos igual; búsqueda en dos familias solo sobre train; `auc_test` en una sola fila; sensibilidad con tres conjuntos de pesos |
| Reproducibilidad | 3 | Ejecutado en una sesión nueva con solo este README: mismo leaderboard y mismo campeón; versiones y semilla indicadas |
| Análisis y comunicación al cliente | 3 | La *model card* explica por qué gana la logística, que con otros pesos gana el árbol y que la ventaja es corta; falta traducir el AUC a euros |
| IA responsable | 3 | Dice qué se pidió, qué se revisó y qué se cambió; mide la tasa de aviso por canal y país y nombra usos NO previstos |

**Lo primero que mejoraríamos:** repetir el leaderboard con varias semillas para saber si el duelo logística–árbol se mantiene (extra 🔴).
