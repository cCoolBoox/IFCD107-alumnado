# Sprint 10 · Redes neuronales bien entrenadas

**Pregunta guía:** ¿una red neuronal mejora al aprendizaje automático clásico y a qué precio?
**Fechas:** 13–17 de noviembre · **Horas:** 15 h (5 h teoría · 6 h práctica · 4 h PBL) · **Módulo 4, UD 4.1–4.3**

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_10.pdf`](Guia_Sprint_10.pdf)
- 🖥️ **S10.1 · Fundamentos de redes neuronales:** [`S10.1_Fundamentos_de_redes_neuronales.pdf`](presentaciones/S10.1_Fundamentos_de_redes_neuronales.pdf)
- 🖥️ **S10.2 · Redes densas con Keras:** [`S10.2_Redes_densas_con_Keras.pdf`](presentaciones/S10.2_Redes_densas_con_Keras.pdf)
- 🖥️ **S10.3 · Entrenamiento y regularizacion:** [`S10.3_Entrenamiento_y_regularizacion.pdf`](presentaciones/S10.3_Entrenamiento_y_regularizacion.pdf)

## Qué aprenderás
- Cómo funciona por dentro una red: neurona, capas, activación y *backprop*.
- Entrenar un MLP con Keras (cancelaciones y `precio_noche`).
- Detectar el **sobreajuste** en las curvas y combatirlo (L2, *dropout*, parada temprana).
- Decidir con datos si una red «vale la pena» frente al *boosting*. Hace falta lo de los Sprints 7 y 8; funciona sin internet.

## Prácticas
| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| `S10_01_red_desde_cero` | Una red neuronal con solo NumPy: neurona, activación, *backprop*, entrenamiento | 1 h 15 | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/S10_01_red_desde_cero.ipynb) |
| `S10_02_mlp_keras` | MLP en Keras: cancelaciones (clasificación) y `precio_noche` (regresión) | 1 h 30 | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/S10_02_mlp_keras.ipynb) |
| `S10_03_regularizacion` | Curvas, sobreajuste, L2, *dropout*, parada temprana, lote, tasa, *callbacks*, guardar modelo | 1 h 45 | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/S10_03_regularizacion.ipynb) |
| `S10_04_reto_vale_la_pena` | Esqueleto del reto: MLP frente a boosting con incertidumbre y diagnóstico | 1 h 30 (+ trabajo PBL) | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/S10_04_reto_vale_la_pena.ipynb) |

Cada notebook tiene ejercicios con `assert`: si saltan, el mensaje te dice qué revisar.

## Reto · «¿Vale la pena la red?»
**Contexto:** la dirección de TurisData Canarias oye hablar de redes neuronales y pregunta si debe sustituir su modelo de cancelaciones. No quiere una opinión: quiere evidencias, coste incluido.

**Entregáis** (carpeta `sprint-10/` del repositorio del equipo):
- Notebook ejecutable de principio a fin, basado en `S10_04`, con semillas fijas.
- Informe comparativo de 1–2 páginas (PDF o Markdown) «ML clásico frente a MLP»: tabla de resultados, curvas de aprendizaje y recomendación.

**Reglas:**
- 4 h en equipo; un solo problema (`cancelada` **o** `precio_noche`), misma partición para todos y prueba usada una sola vez.
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
