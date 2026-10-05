# Checklist de congelación · jueves 10/12 · 14:30

> Imprimidlo o copiadlo al tablero. **Una persona diferente a la que escribió el README** ejecuta la sección B en un ordenador (o en una carpeta) limpio.
> **Regla propuesta:** tras las 14:30 no se cambia código ni memoria. Se permite seguir con la presentación y el vídeo de plan B. Un fallo crítico del demostrador solo se corrige con permiso del docente y quedando documentado.

**Equipo:** ______ · **Persona que verifica:** ______ · **Hora de la verificación:** ______

## A. Repositorio
- [ ] El repositorio del equipo contiene lo que queremos entregar, **todo subido** (nada se queda solo en un ordenador).
- [ ] En la pestaña **Commits** aparecen aportaciones de **todas** las personas.
- [ ] **No hay claves, tokens ni datos personales** en ningún archivo del repositorio.
- [ ] `README.md` completo (problema, resultados, estructura, cómo reproducir, cómo lanzar la demo, datos y licencias, IA responsable, equipo).
- [ ] `requirements.txt` con **versiones fijas** (`pip freeze` recortado a lo que se usa) y versión de Python indicada.
- [ ] Datos incluidos (si pesan poco y la licencia lo permite) **o** script de descarga que funciona, con licencia citada.
- [ ] Estructura de carpetas clara (`notebooks/`, `src/`, `experimentos/`, `modelo/`, `demostrador/`, `tests/`, `docs/`).

## B. Reproducibilidad (prueba en limpio)
- [ ] Descargar el repositorio como ZIP (**Code → Download ZIP**) y abrir el notebook principal en Colab: se ejecuta sin errores siguiendo solo el README.
- [ ] El script de datos / los notebooks se ejecutan **de arriba abajo** con semilla fija y dan los resultados de la memoria (tolerancia razonable).
- [ ] Las pruebas (si las hay) pasan.
- [ ] El tiempo total de reproducción está indicado en el README.
- [ ] El modelo final se genera o se incluye con su `metadatos.json`.

## C. Demostrador
- [ ] Se lanza con **un comando** indicado en el README y se abre sin errores.
- [ ] Probado con 3 entradas normales, 1 entrada errónea y 1 vacía: muestra mensajes claros y no se rompe.
- [ ] Muestra **incertidumbre** (probabilidad, intervalo, «no lo sé») y un aviso de límites.
- [ ] Si es un asistente / chatbot: **indica que es un sistema de IA** y cita fuentes.
- [ ] **Vídeo plan B** de 90 s guardado (`docs/demo.mp4` o enlace estable).

## D. Evaluación e IA responsable
- [ ] Test usado **una sola vez** con el modelo ya elegido.
- [ ] Gráficos: curvas / matriz / importancia (SHAP o Grad-CAM si procede), con títulos-conclusión.
- [ ] Rendimiento **por subgrupos** y medida de mitigación **evaluada**.
- [ ] `docs/riesgos_eticos.md` cerrado (riesgos altos con estado y evidencia) y clasificación RGPD / AI Act justificada.
- [ ] `docs/model_card.md` completa.

## E. Memoria
- [ ] PDF en `docs/memoria_tecnica.pdf`, **10-15 páginas** sin contar anexos.
- [ ] Todas las secciones del esqueleto; figuras con pie y referencias; **cifras coherentes** con el README y con el registro de experimentos.
- [ ] Fuentes, licencias y citas correctas; redacción propia (sin copiar bloques de documentación o de un LLM sin revisar).
- [ ] Conclusiones **accionables** y límites explicados.

## F. Equipo y metodología
- [ ] Tablero exportado (`docs/scrum/`): backlog, planning, review y retro de los sprints 14, 15 y 16.
- [ ] Retro con **acción concreta** y comprobación de la acción anterior.
- [ ] **Coevaluación** rellenada por cada integrante y entregada al docente (no en el repositorio).

## Cierre
Hora de la etiqueta: ______ · Enlace de la etiqueta / versión: ______ · Firma de la persona que verifica: ______
