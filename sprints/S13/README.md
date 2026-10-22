# README Sprint S13 · Contar lo que hace el modelo

**Pregunta guía:** ¿cómo enseñamos y defendemos los resultados de un modelo?
**Fecha:** 25/11, dentro del último día del Sprint 12 · **Tiempo:** ≈ 1 h 40 min (20 min de teoría · 40 de práctica · 40 de reto)

📄 **Este README en PDF:** [a color](README_Sprint_13.pdf) · [ecofriendly, para imprimir](README_Sprint_13_ecofriendly.pdf) (descárgalo para que funcionen los enlaces; la vista previa de GitHub no los abre).

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

## 📎 Materiales del sprint

**Documentos del curso** (PDF y .md; las actividades van en la tabla siguiente)

| Material | Tema | Tiempo | Cuándo |
|---|---|---|---|
| [Guía del sprint (PDF)](guia/Guia_Sprint_13.pdf) · [ecofriendly](guia/Guia_Sprint_13_ecofriendly.pdf) | Resumen del sprint: qué aprenderás, temario, material, reto y conclusión | 2 páginas | Antes de empezar |
| [Reto completo, paso a paso (.md)](guia/Reto_Sprint_13.md) · [PDF](guia/Reto_Sprint_13.pdf) · [ecofriendly](guia/Reto_Sprint_13_ecofriendly.pdf) | Qué pide el cliente, pasos, rúbrica, ayudas y errores frecuentes | — | Antes del planning y durante el reto |
| [Infografías del reto](infografias/) | 2 láminas ilustradas del reto | — | Reto |
| [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md) | El método de trabajo de todos los retos | — | Antes del primer reto |
| [`S13.1_Visualizar_y_comunicar_resultados.pdf`](presentaciones/S13.1_Visualizar_y_comunicar_resultados.pdf) | Visualizar y comunicar resultados (Sprint 13, integrado; versión rápida) | 10 min | Teoría · miércoles 25/11 |
| [`guia_cuantos_sprints_tiene_el_proyecto.md`](plantillas/guia_cuantos_sprints_tiene_el_proyecto.md) | ¿Cuántos sprints tiene el proyecto? Capacidad, tallas y qué cabe en los Sprints 14–17 | 25–30 min | Al cerrar el 25/11 o antes del planning del 26/11 |

**Material de las actividades**

| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| `S13_01_visualizacion_resultados` | Matriz de confusión, ROC/PR, importancia, umbral y coste, buenas prácticas | 40 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/notebooks/S13_01_visualizacion_resultados.ipynb) |
| `S13_02_plantilla_informe_visual` | Plantilla ejecutable del panel de una página (para el reto) | 40 min (dentro del reto) | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/notebooks/S13_02_plantilla_informe_visual.ipynb) |

Plantilla en esta carpeta: [`plantilla_informe_visual.md`](plantillas/plantilla_informe_visual.md) (texto del informe de una página).

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

**Miércoles 25/11 · última jornada del Sprint 12 (el Sprint 13 va dentro de ese día)**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 1 | 📖 Teoría | [Visualizar y comunicar resultados (Sprint 13, integrado; versión rápida)](presentaciones/S13.1_Visualizar_y_comunicar_resultados.pdf) | 10 min |
| 2 | 💻 Práctica | [Matriz de confusión, ROC/PR, importancia, umbral y coste](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/notebooks/S13_01_visualizacion_resultados.ipynb) | 35 min |
| 3 | 🎯 Reto | [Reto del Sprint 13](guia/Reto_Sprint_13.md): elegir el modelo y los costes → tres o cuatro gráficos → titular y viñetas. Usad el [cuaderno plantilla](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/notebooks/S13_02_plantilla_informe_visual.ipynb) y la [plantilla del informe](../S13/plantillas/plantilla_informe_visual.md) | 25 min |

<!--orden:fin-->

## Entrega / Reto · «Informe visual para dirección»

📄 [Reto en PDF](guia/Reto_Sprint_13.pdf) · [ecofriendly](guia/Reto_Sprint_13_ecofriendly.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

👉 **[Ver el reto completo, explicado paso a paso](guia/Reto_Sprint_13.md)** (qué se pide, cómo hacerlo, cómo usar la IA, errores frecuentes y autoevaluación).


**Contexto:** Marcos, director de TurisData Canarias, tiene 10 minutos y no sabe qué es un AUC. Pide: *«Una página. ¿Puedo fiarme del modelo, qué mueve las cancelaciones y qué hago el lunes?»*

**Entregáis** (carpeta `sprint-13/` del repositorio del equipo):
- `informe_visual.md` con el PNG del panel (o PDF de una página), siguiendo la plantilla: titular-decisión, 4 gráficos, 3 viñetas y pie con datos y responsables.
- Notebook `S13_02_plantilla_informe_visual` adaptado a vuestro mejor modelo del curso, ejecutable de arriba abajo.
- Es la semilla de la memoria técnica del proyecto final.

**Reglas:**
- Una sola página, máximo 4 gráficos, legible proyectada; sin jerga (explica «AUC», «F1» o «SHAP»).
- Cifras del texto = cifras del gráfico; semillas fijas; métricas sobre el test.
- Equipos de 3-4: modelo, gráficos, texto y revisión cruzada.

**Se valora:** corrección técnica, reproducibilidad, comunicación al cliente (titular-decisión, sin jerga) e IA responsable (rúbrica de retos, 1–4).

## ✅ Antes de cerrar el sprint
- [ ] Una página con titular-decisión, 4 gráficos, 3 viñetas y pie.
- [ ] Cada gráfico tiene título-conclusión y ejes con nombre; barras desde 0, sin 3D.
- [ ] Métricas calculadas sobre el test.
- [ ] Se indica con cuántos datos, qué modelo y qué límites.
- [ ] El notebook se ejecuta de arriba abajo con semillas fijas.
- [ ] Entregable subido a la carpeta `sprint-13/` del repositorio del equipo.
