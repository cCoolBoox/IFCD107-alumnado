# Autoevaluación y coevaluación · «Visión artificial para el cliente»

> Hoja de **ejemplo** de una persona (Marta) del equipo de referencia. Cada persona sube la suya con su nombre.

## 1. Autoevaluación

**Nombre:** Marta

**Repaso rápido:**

| Pregunta | Mi respuesta |
|---|---|
| ¿Hay una carpeta por clase con al menos 30 fotos y sin personas reconocibles? | Sí: 60 por clase, sintéticas |
| ¿El cuaderno se ejecuta de arriba abajo con la semilla fija? | Sí: `SEMILLA = 42` y probado con «Reiniciar y ejecutar todo» |
| ¿Hay modelo con *transfer learning* y una referencia «desde cero»? | Sí, y el transfer gana en prueba |
| ¿Hay precisión y recall por clase, matriz de confusión y una frase de lectura? | Sí: casa_rural y camping se confunden |
| ¿Hay al menos 6 errores analizados con una hipótesis que se vea en la foto? | Sí: 8, y vimos que la mayoría parecen etiquetas mal puestas |
| ¿La prueba se usó una sola vez y el umbral se eligió con la validación? | Sí |
| ¿Hay demostrador con «revisar a mano» y al menos dos riesgos con medida? | Sí: `clasificar_foto` y tres riesgos |
| ¿Cada persona ha hecho *commit* de su parte? | Sí |

**Puntúate de 1 a 4:**

| Criterio | Mi puntuación (1–4) | Por qué (una frase) | Qué haría para subir un punto |
|---|---|---|---|
| Corrección técnica | 3 | Todo lo estándar está hecho y el umbral salió de la validación | Corregir las etiquetas y volver a medir (mejora probada) |
| Reproducibilidad | 3 | Otra persona obtuvo la misma exactitud y los mismos errores | Probar el cuaderno también con fotos reales |
| Análisis y comunicación al cliente | 3 | El informe dice que no se fíen todavía y por qué | Dar el coste de revisar a mano el resto de las fotos |
| IA responsable | 3 | Tres riesgos con medida y hipótesis comprobadas en la foto | Medir cuántos errores desaparecen al corregir las etiquetas |

- **Lo que más me costó fue** aceptar que el modelo quizá **no** se equivocaba, **porque** al mirar las fotos vimos casas dentro de la carpeta camping.
- **He usado IA para** proponer hipótesis para los errores, **y lo que he comprobado a mano es** que cada una se ve en la foto: descarté «iluminación» porque son dibujos.

---

## 2. Coevaluación

**Trabajo revisado de (persona o equipo):** equipo «Los Roques» (ejemplo)  **Revisado por (yo):** Marta

| Entregable | ¿Está y se entiende? | Comentario breve |
|---|---|---|
| `analisis_errores.md` | ✘ | Solo hay 3 errores y sin hipótesis; faltan los seis que pide el estándar |
| `reto_vision_cliente.ipynb` | ✔ | Se ejecuta entero; la prueba se usa una sola vez |
| `README.md` | ✔ | Dice de dónde salen las fotos y quién hizo qué |

| Criterio | Puntuación | Comentario breve |
|---|---|---|
| Corrección técnica | 2 | Cumple el mínimo; sin referencia «desde cero» |
| Reproducibilidad | 2 | Se ejecuta, pero sin semilla fija |
| Análisis y comunicación al cliente | 1 | Solo cifras: no dicen qué clases se confunden |
| IA responsable | 2 | Riesgos genéricos, sin medida |

- **Lo que está muy bien:** el demostrador devuelve «revisar a mano» y la matriz de confusión se entiende a la primera.
- **Lo que yo cambiaría, y por qué:** añadiría los seis errores con su hipótesis, porque es lo que dice al cliente si puede fiarse del modelo.

> Se valora el **trabajo**, no a la persona.
