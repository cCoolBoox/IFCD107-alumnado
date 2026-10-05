# Memoria técnica · [Título del proyecto]

> **Extensión: 10-15 páginas** (portada, índice, referencias y anexos no cuentan). Formato PDF, tipografía legible (11 pt), figuras con pie y numeradas.
> Escribe **para el cliente y para un compañero técnico**: debe ser autocontenida. El presupuesto de páginas es orientativo (criterio H de la rúbrica: clara, con figuras y referencias; «Excelente» = autocontenida, concisa y con conclusiones accionables).

**Equipo:** ______ · **Brief:** ______ · **Fecha:** 10/12/2026 · **Versión / etiqueta del repositorio:** v1.0-entrega

---

## 0. Resumen ejecutivo (½–1 página) · *R1, R10*
Problema, enfoque, resultado principal con cifras, recomendación al cliente y un límite clave. **Se escribe al final.**
- Problema y decisión del cliente: ______
- Qué hicimos (2 líneas): ______
- Resultado (métrica de negocio y técnica frente al baseline): ______
- Recomendación y límites: ______

## 1. Problema y valor de negocio (1 página) · *R1 · criterio A*
- Contexto del cliente y pregunta de negocio.
- **Decisión** que apoya el resultado y quién la toma.
- **Métrica de negocio** y **métrica técnica**, umbral de éxito y justificación.
- Valor esperado cuantificado (con supuestos explícitos).

## 2. Datos y análisis exploratorio (2 páginas) · *R2 · criterio B*
- Fuentes, **licencias**, tamaño, periodo y linaje (tabla resumida; el plan de datos completo, en anexo).
- Calidad del dato: defectos detectados, causas y tratamiento.
- **Sesgos de muestreo** y limitaciones.
- 2-3 figuras del EDA que cambian el enfoque (con título-conclusión).

## 3. Metodología (1 página) · *R3*
- Partición de los datos (justificación **anti-fuga**; temporal si hay series).
- Baseline, métricas, validación cruzada y semillas.
- Cómo se registraron los experimentos (enlace a `experimentos/registro.csv`).

## 4. Modelado y experimentos (2-3 páginas) · *R3, R4 · criterio C*
- Baseline y ≥ 3 modelos (**al menos uno neuronal**, o LLM/RAG en el brief 3): qué son, por qué se eligieron e hiperparámetros probados.
- **Tabla comparativa** con media ± desviación y tiempo.
- Justificación de la elección con **coste / beneficio** y explicación del **porqué** de los resultados.
- Fugas detectadas y cómo se evitaron.

## 5. Evaluación y resultados (2-3 páginas) · *R5 · criterio D*
- Métricas finales en el test (una sola evaluación), **con incertidumbre** (intervalos o variación).
- Visualizaciones: curvas, matriz de confusión, importancia de variables, SHAP o Grad-CAM según el caso.
- **Análisis de errores**: dónde falla y ejemplos.
- Generalización: rendimiento con datos distintos (otro periodo, fotos reales, preguntas nuevas…).

## 6. IA responsable (2 páginas) · *R6 · criterio E*
- Checklist ético actualizado (resumen) y registro de riesgos (tabla de los riesgos altos).
- **Sesgos por subgrupos**: métricas, hallazgos y **mitigación aplicada y evaluada**.
- Clasificación **RGPD / AI Act** con justificación.
- Limitaciones, usos no permitidos y supervisión humana.

## 7. Demostrador y reproducibilidad (1 página) · *R7, R8 · criterio F*
- Qué hace el demostrador, tecnología, captura de pantalla y **manejo de errores del usuario**.
- Cómo reproducir todo (resumen de los pasos del README), versiones y pruebas.
- Plan B y limitaciones técnicas.

## 8. Gestión del proyecto (½–1 página) · *R9, R11 · criterio G*
- Roles y rotación, backlog y sprints (objetivo y resultado de cada uno).
- **Mejoras entre retrospectivas** (acción → efecto).
- Reparto de trabajo y evidencias (commits, tablero).

## 9. Conclusiones y recomendaciones (1 página) · *criterio H*
- **Qué recomendamos al cliente** (acciones concretas y priorizadas).
- Qué **no** debe hacerse con el modelo.
- Límites del estudio y **trabajo futuro** (3 líneas).

## Referencias y licencias
Citas de datos (fuente, año, licencia), artículos, librerías con versiones, documentación consultada.

## Anexos (no cuentan para las páginas)
A. Ficha de proyecto · B. Plan de datos y licencias · C. Registro de experimentos · D. Model card · E. Registro de riesgos éticos · F. Capturas del tablero y retros · G. Enlace al repositorio y a la etiqueta `v1.0-entrega`.

---

### Mapa de requisitos (comprobad que cada uno tiene su sección)
| Requisito | Dónde se demuestra | ✔ |
|---|---|---|
| R1 Problema y métricas | §1 | |
| R2 Datos con fuente y licencia, EDA | §2 | |
| R3 Baseline + ≥ 3 modelos, validación sin fuga | §3, §4 | |
| R4 Modelo neuronal o LLM/RAG | §4 | |
| R5 Evaluación con visualizaciones | §5 | |
| R6 IA responsable (checklist, sesgos, riesgo) | §6 | |
| R7 Demostrador ejecutable | §7 | |
| R8 Repositorio reproducible | §7 y README | |
| R9 Evidencia Scrum | §8 y anexo F | |
| R10 Memoria de 10-15 páginas | este documento | |
| R11 Defensa con todos los integrantes | Sprint 17 | |

### Presupuesto de páginas (total 10-15)
Resumen 1 · Problema 1 · Datos 2 · Metodología 1 · Modelado 2 · Evaluación 2 · IA responsable 2 · Demostrador 1 · Gestión 0,5 · Conclusiones 1 = **13,5** (holgura de 1,5 páginas).

### Lista de comprobación de calidad
- [ ] Cada figura tiene título-conclusión, ejes con nombre y se cita en el texto.
- [ ] Las cifras coinciden con el README, el registro de experimentos y la presentación.
- [ ] Cada afirmación importante tiene evidencia (tabla, figura o referencia).
- [ ] Sin párrafos genéricos sobre «qué es la IA»: solo lo necesario para entender el proyecto.
- [ ] Revisada por una persona que no la escribió.
