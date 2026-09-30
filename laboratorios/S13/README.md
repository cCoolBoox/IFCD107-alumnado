# Sprint 13 · Contar lo que hace el modelo

> **Pregunta guía:** ¿cómo enseñamos y defendemos los resultados de un modelo?
> **Fecha:** 25 de noviembre · **Horas:** 3 h (1 h teoría · 1 h práctica · 1 h PBL)
> **Módulo:** M5 · Visualización de resultados

## Qué aprenderás
1. Dibujar e interpretar la **matriz de confusión**, la **curva ROC** y la **curva precisión-exhaustividad** de un modelo de clasificación.
2. Explicar **qué variables pesan** en un modelo con la importancia por permutación (y saber que existen SHAP y Grad-CAM para el proyecto).
3. Elegir el **umbral de decisión** con el coste del negocio, no por costumbre.
4. Aplicar **buenas prácticas de comunicación** de datos: un gráfico, un mensaje; ejes honestos; pocos colores.
5. Montar un **informe visual de una página** para dirección.

## Requisitos previos
- Modelo de clasificación con scikit-learn y sus métricas (Sprints 7-8).
- `reservas_turisdata.csv` (los notebooks lo descargan solo).
- Opcional: tu «mejor modelo del curso» de los Sprints 8, 10 o 12 para adaptar la plantilla.

## Prácticas

| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| `S13_01_visualizacion_resultados` | Matriz de confusión, ROC/PR, importancia, umbral y coste, buenas prácticas | 1 h | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/laboratorios/S13/S13_01_visualizacion_resultados.ipynb) |
| `S13_02_plantilla_informe_visual` | Plantilla ejecutable del panel de una página (para el reto) | 1 h (dentro del PBL) | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/laboratorios/S13/S13_02_plantilla_informe_visual.ipynb) |

Además: `plantilla_informe_visual.md` (el texto del informe de una página, en esta carpeta).

---

## Reto PBL · «Informe visual para dirección»  (1 h)

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

### Qué se enseña en la review
Cada equipo proyecta su página 30 segundos y **el resto de la clase dice la decisión que entiende**. Si no coincide con la del equipo, el mensaje no está claro. Se comparan los titulares y se elige el más claro.

### Definition of Done
- [ ] Una sola página con titular-decisión, 4 gráficos, 3 viñetas y pie.
- [ ] Cada gráfico tiene título que enuncia una conclusión y ejes con nombre.
- [ ] Las barras empiezan en 0; sin 3D; máximo 3-4 colores con sentido.
- [ ] Métricas calculadas **sobre el test**.
- [ ] Se indica con cuántos datos, qué modelo y qué límites.
- [ ] El notebook se ejecuta de arriba abajo con semillas fijas.
- [ ] Guardado en el repositorio del equipo como semilla de la memoria.

## Recursos
- Guía de usuario de scikit-learn: *Model evaluation* (matriz de confusión, ROC, PR) y *Permutation feature importance*.
- Galería de matplotlib y de seaborn (para elegir el tipo de gráfico).
- «Storytelling with Data», C. N. Knaflic: ideas de comunicación de datos (consulta capítulos de muestra online).
- Documentación de SHAP (para el proyecto final): <https://shap.readthedocs.io>.
