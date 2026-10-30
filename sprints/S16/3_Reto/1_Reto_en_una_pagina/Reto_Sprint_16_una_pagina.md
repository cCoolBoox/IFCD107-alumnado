# Sprint 16 · Reto «Entrega final: evaluar, demostrar y documentar» · en una página

> Versión corta para **trabajar con ella abierta**. La ficha completa (guía paso a paso, uso de la IA, errores frecuentes y rúbrica) sigue en [Reto_Sprint_16.md](../2_Ficha_completa/Reto_Sprint_16.md). Plantillas: [model card](../4_Plantillas_y_entrega/plantilla_model_card.md) · [memoria](../4_Plantillas_y_entrega/plantilla_esqueleto_memoria_tecnica.md) · [lista de congelación](../4_Plantillas_y_entrega/checklist_congelacion.md) · [demostrador](../4_Plantillas_y_entrega/demostrador/).

**El cliente.** El docente recibirá vuestro trabajo como un entregable real: clonará el repositorio, seguirá el README, probará el demostrador, leerá la memoria y querrá entender los riesgos.
**Qué entregáis (no cambia):** evaluación final en test, sesgos con mitigación medida, riesgos cerrados, demostrador con plan B en vídeo, model card y memoria de 10–15 páginas. **Al final se suben a `sprint-16/` del repositorio del equipo: 9 ficheros del equipo + 1 autoevaluación y coevaluación por persona** (`autoevaluacion_nombre.md`). La coevaluación confidencial (anexo B) va al docente.
**Tiempo:** 3 días de clase (525 min de reto) con dos días sin clase entre el 1 y el 2. **Congelación: 10/12 a las 14:30.** Etiqueta `v1.0-entrega` antes.

## Tres niveles: el equipo decide hasta dónde llega

| Nivel | Qué hay que tener | Nota* |
|---|---|---|
| 🟢 **Mínimo** (todos los equipos) | Test usado una vez, con métricas y gráficos · métrica por subgrupos y una mitigación aplicada · riesgos cerrados y RGPD / AI Act clasificado · demostrador que arranca · README y `requirements.txt` · model card · memoria 10–15 págs · commits de todos y etiqueta antes de las 14:30 | 2 |
| 🟡 **Estándar** | Análisis de errores · mitigación **medida antes y después por subgrupo** · entradas erróneas y aviso de incertidumbre · `pytest -q` en verde · vídeo plan B · README probado en limpio por otra persona · cifras coherentes y conclusiones accionables · lista de congelación pasada | 3 |
| 🔴 **Extra** | SHAP o Grad-CAM interpretado · intervalos de incertidumbre · comparar dos mitigaciones o probar con datos distintos · `api.py` | 4 |

\*Orientativo; puntúa el docente con la rúbrica del curso (0–4 en cada criterio). El mínimo es una entrega válida y evaluable; la «Definition of Done» de la ficha completa describe el nivel **estándar**.

## Reparto sugerido de los 525 minutos

| Día | Min | Qué | Se sabe que está hecho cuando… |
|---|---|---|---|
| 1 | 40 | Evaluar en test, subgrupos y errores | `04_evaluacion.ipynb` con métricas y gráficos |
| 1 | 85 | Esqueleto de la memoria y model card | Una persona por sección; demostrador básico arranca |
| 2 | 80 | Mitigar el sesgo y volver a medir | Tabla antes y después por subgrupo |
| 2 | 40 | Pulir el demostrador y `pytest -q` | Cinco entradas de prueba sin romperse |
| 2 | 80 | Model card, riesgos y memoria completa | Todos los apartados escritos |
| 3 | 80 | Prueba en limpio y corrección | Otra persona lo reproduce con solo el README |
| 3 | 65 | Vídeo plan B, lista de congelación, coevaluación | Todo marcado |
| 3 | 55 | Rúbrica, review, retro, subida y etiqueta | `v1.0-entrega` antes de las 14:30 |

## Frases para la memoria y la model card (completad los huecos)
- «El … baja del … % global al … % en el subgrupo …. Aplicamos … y subió al … % (… puntos menos en el resto); a cambio, …»
- «No usar el modelo para …. Con entradas fuera de …, el demostrador responde «…». Los datos son …»
- «Hemos usado IA para …; lo hemos revisado …; no hemos pegado datos personales.»

## Antes de entregar
- **Archivos subidos en `sprint-16/`:** `README.md` · `notebooks/04_evaluacion.ipynb` · `demostrador/logica.py` · `demostrador/app.py` · `demostrador/tests/test_logica.py` · `demostrador/requirements.txt` · `docs/riesgos_eticos.md` · `docs/model_card.md` · `docs/memoria_tecnica.pdf` · `autoevaluacion_nombre.md` (**uno por persona**) = 9 + N ficheros
- [ ] Test usado una sola vez · [ ] mitigación medida por subgrupo · [ ] `pytest -q` pasa · [ ] vídeo plan B (en `docs/` o con enlace en el README)
- [ ] README probado en limpio por otra persona, con «Revisión con la rúbrica» · [ ] ≥ 1 commit de cada persona · [ ] etiqueta `v1.0-entrega` creada antes de las 14:30
- [ ] [Autoevaluación y coevaluación](../4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md): **una por persona**, subida a `sprint-16/` · [ ] coevaluación individual (anexo B) entregada al docente
