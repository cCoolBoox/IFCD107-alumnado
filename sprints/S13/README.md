# Sprint 13 · Contar lo que hace el modelo
**Pregunta guía:** ¿cómo enseñamos y defendemos los resultados de un modelo?
**Fechas:** 25/11 · **Horas:** 3 h (1 T · 1 P · 1 PBL)

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_13.pdf`](Guia_Sprint_13.pdf)
- 🖥️ **S13.1 · Visualizar y comunicar resultados:** [`S13.1_Visualizar_y_comunicar_resultados.pdf`](presentaciones/S13.1_Visualizar_y_comunicar_resultados.pdf)

## Qué aprenderás
- A dibujar e interpretar la **matriz de confusión**, la curva **ROC** y la curva **precisión-exhaustividad**.
- A explicar **qué variables pesan** en un modelo (importancia por permutación).
- A elegir el **umbral de decisión** según el coste del negocio.
- A montar un **informe visual de una página** para dirección: un gráfico, un mensaje.

## Prácticas
| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| `S13_01_visualizacion_resultados` | Matriz de confusión, ROC/PR, importancia, umbral y coste, buenas prácticas | 1 h | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/S13_01_visualizacion_resultados.ipynb) |
| `S13_02_plantilla_informe_visual` | Plantilla ejecutable del panel de una página (para el reto) | 1 h (dentro del PBL) | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/S13_02_plantilla_informe_visual.ipynb) |

Plantilla en esta carpeta: [`plantilla_informe_visual.md`](plantilla_informe_visual.md) (texto del informe de una página).

## Entrega / Reto · «Informe visual para dirección»
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
