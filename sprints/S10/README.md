# Sprint 10 · Redes neuronales bien entrenadas

**Pregunta guía:** ¿una red neuronal mejora al aprendizaje automático clásico y a qué precio?
**Fechas:** 16–17 de noviembre · **Horas:** 12 h (4 h teoría · 4 h práctica · 4 h PBL)

> 🎯 **Reto de este sprint: «¿Vale la pena la red?».** 👉 [**Ver el reto completo, explicado paso a paso**](guia/Reto_Sprint_10.md) · [Reto en PDF](guia/Reto_Sprint_10.pdf) ([ecofriendly](guia/Reto_Sprint_10_ecofriendly.pdf)) · [PDF de la guía](guia/Guia_Sprint_10.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

📄 **Este README en PDF:** [a color](README_Sprint_10.pdf) · [ecofriendly, para imprimir](README_Sprint_10_ecofriendly.pdf) (descárgalo para que funcionen los enlaces; la vista previa de GitHub no los abre).

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_10.pdf`](guia/Guia_Sprint_10.pdf) · [versión ecofriendly para imprimir](guia/Guia_Sprint_10_ecofriendly.pdf)
- 🎯 **Reto completo, paso a paso:** [`Reto_Sprint_10.md`](guia/Reto_Sprint_10.md)
- 🖥️ **S10.1 · Fundamentos de redes neuronales:** [`S10.1_Fundamentos_de_redes_neuronales.pdf`](presentaciones/S10.1_Fundamentos_de_redes_neuronales.pdf)
- 🖥️ **S10.2 · Redes densas con Keras:** [`S10.2_Redes_densas_con_Keras.pdf`](presentaciones/S10.2_Redes_densas_con_Keras.pdf)
- 🖥️ **S10.3 · Entrenamiento y regularizacion:** [`S10.3_Entrenamiento_y_regularizacion.pdf`](presentaciones/S10.3_Entrenamiento_y_regularizacion.pdf)

**📁 En esta carpeta:** [`guia/`](guia/) PDF de la guía (normal y para imprimir) y el reto explicado paso a paso · [`presentaciones/`](presentaciones/) diapositivas de cada sesión · [`notebooks/`](notebooks/) prácticas para abrir en Colab

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

📖 teoría (diapositivas) · 💻 práctica (cuaderno de Colab o actividad) · 🎯 reto en equipo · 🔔 ceremonia de Scrum

**Lunes 16/11**

1. 🔔 **Ceremonia**: Planning del reto «¿Vale la pena la red?» y reparto de roles · _15 min_
2. 📖 **Teoría**: [Fundamentos de redes neuronales](presentaciones/S10.1_Fundamentos_de_redes_neuronales.pdf) · _1 h 10 min_
3. 💻 **Práctica**: [Una red neuronal con solo NumPy](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/notebooks/S10_01_red_desde_cero.ipynb) · _50 min_
4. 📖 **Teoría**: [Redes densas con Keras](presentaciones/S10.2_Redes_densas_con_Keras.pdf) · _1 h 5 min_
5. 💻 **Práctica**: [MLP en Keras: clasificación y regresión](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/notebooks/S10_02_mlp_keras.ipynb) · _1 h 20 min_
6. 📖 **Teoría**: [Entrenamiento y regularización (primera parte)](presentaciones/S10.3_Entrenamiento_y_regularizacion.pdf) · _40 min_

**Martes 17/11**

7. 📖 **Teoría**: [Entrenamiento y regularización (final: parada temprana y *callbacks*)](presentaciones/S10.3_Entrenamiento_y_regularizacion.pdf) · _25 min_
8. 💻 **Práctica**: [Sobreajuste, L2, *dropout*, parada temprana y *callbacks*](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/notebooks/S10_03_regularizacion.ipynb) · _1 h 5 min_
9. 🎯 **Reto**: Esqueleto [`S10_04`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/notebooks/S10_04_reto_vale_la_pena.ipynb): elegir el problema y reproducir la referencia (paso 1) → primera red (2) → diagnosticar el sobreajuste (3) → comparación justa (4) → informe y presentación (5) · _3 h 10 min_
10. 🔔 **Ceremonia**: Entrega en `sprint-10/`, autoevaluación y coevaluación, review y retrospectiva · _40 min_

<!--orden:fin-->

## Qué aprenderás
- Cómo funciona por dentro una red: neurona, capas, activación y *backprop*.
- Entrenar un MLP con Keras (cancelaciones y `precio_noche`).
- Detectar el **sobreajuste** en las curvas y combatirlo (L2, *dropout*, parada temprana).
- Decidir con datos si una red «vale la pena» frente al *boosting*. Hace falta lo de los Sprints 7 y 8; funciona sin internet.

## Prácticas
| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| `S10_01_red_desde_cero` | Una red neuronal con solo NumPy: neurona, activación, *backprop*, entrenamiento | 50 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/notebooks/S10_01_red_desde_cero.ipynb) |
| `S10_02_mlp_keras` | MLP en Keras: cancelaciones (clasificación) y `precio_noche` (regresión) | 80 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/notebooks/S10_02_mlp_keras.ipynb) |
| `S10_03_regularizacion` | Curvas, sobreajuste, L2, *dropout*, parada temprana, lote, tasa, *callbacks*, guardar modelo | 65 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/notebooks/S10_03_regularizacion.ipynb) |
| `S10_04_reto_vale_la_pena` | Esqueleto del reto: MLP frente a boosting con incertidumbre y diagnóstico | 1 h 30 (+ trabajo PBL) | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/notebooks/S10_04_reto_vale_la_pena.ipynb) |

Cada notebook tiene ejercicios con `assert`: si saltan, el mensaje te dice qué revisar.

## Reto · «¿Vale la pena la red?»

👉 **[Ver el reto completo, explicado paso a paso](guia/Reto_Sprint_10.md)** (qué se pide, cómo hacerlo, cómo usar la IA, errores frecuentes y autoevaluación).

**Contexto:** la dirección de TurisData Canarias oye hablar de redes neuronales y pregunta si debe sustituir su modelo de cancelaciones. No quiere una opinión: quiere evidencias, coste incluido.

**Entregáis** (carpeta `sprint-10/` del repositorio del equipo):
- Notebook ejecutable de principio a fin, basado en `S10_04`, con semillas fijas.
- Informe comparativo de 1–2 páginas (PDF o Markdown) «ML clásico frente a MLP»: tabla de resultados, curvas de aprendizaje y recomendación.

**Reglas:**
- Unas 4 h en equipo; un solo problema (`cancelada` **o** `precio_noche`), misma partición para todos y prueba usada una sola vez.
- Referencia: tu campeón del Sprint 8; máx. 40 épocas; el escalador se ajusta solo con entrenamiento.
- Nunca claves ni datos personales.

**Se valora:** corrección técnica, reproducibilidad, comunicación al cliente e IA responsable (datos sintéticos, coste de errores, sesgos por país o canal), más comparación con incertidumbre (varias semillas).

## ✅ Antes de cerrar el sprint
- [ ] Notebook ejecutable de principio a fin (`Restart & Run all`)
- [ ] Notebook de arriba abajo con semillas fijas; test usado una sola vez
- [ ] MLP y modelo de árboles/boosting comparados con incertidumbre
- [ ] Curvas de aprendizaje y recomendación concreta con coste y límites
- [ ] Entregable subido a la carpeta `sprint-10/` del repositorio del equipo
- [ ] Autoevaluación y coevaluación rellenadas
