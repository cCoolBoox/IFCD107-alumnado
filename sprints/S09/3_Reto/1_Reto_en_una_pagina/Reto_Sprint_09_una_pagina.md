# Sprint 9 · Reto «Conocer al huésped» · en una página

> Versión corta para **trabajar con ella abierta**. La ficha completa (recursos, tablas de ficheros y requisitos, rúbrica, guía paso a paso, uso de la IA y errores frecuentes) sigue en [Reto_Sprint_09.md](../2_Ficha_completa/Reto_Sprint_09.md); la plantilla de la ficha está en [`plantilla_ficha_segmentos.md`](../4_Plantillas_y_entrega/plantilla_ficha_segmentos.md).

**El cliente.** Lucía, directora comercial de TurisData, envía la misma newsletter a sus 1.200 huéspedes. Pide: *«Decidme quiénes son mis clientes, cómo los llamo y qué le enseño a cada uno.»* Aquí **no hay respuesta correcta en los datos**: hay que descubrir los grupos y darles sentido de negocio.
**Qué entregáis (no cambia):** un cuaderno (`reto_S09_conocer_al_huesped.ipynb`) y una **ficha de segmentos de 1 página** (`ficha_segmentos.md`) con la nota de IA responsable dentro. **Al final del sprint se suben a `sprint-09/` del repositorio del equipo: 2 ficheros del equipo + 1 autoevaluación y coevaluación por persona** (`autoevaluacion_nombre.md`).
**Tiempo en clase:** planning 10 min · reto 95 min (45 el día 1 y 50 el día 2) · entrega, review y retro 40 min. Lo que no quepa, a casa.

## Tres niveles: el equipo decide hasta dónde llega

| Nivel | Qué hay que tener | Nota* |
|---|---|---|
| 🟢 **Mínimo** (todos los equipos) | Variables **escaladas** antes de agrupar · `k` elegido con la silueta y una razón de negocio · mapa 2D con PCA (segmentos coloreados, % de varianza en los ejes) · ficha con **nombre, tamaño, perfil y una acción comercial por segmento** · nota de IA responsable de 5 líneas · IA declarada en el cuaderno | 2 |
| 🟡 **Estándar** | Recomendador con **dos métodos** comparados con RMSE y precision@3 (valoraciones escondidas) · `recomendar(id_usuario, n)` que no propone lo ya valorado, probada con 3 usuarios · experiencia estrella por segmento · 2 riesgos concretos con medida · cuaderno que se ejecuta entero con semillas fijas · un *commit* por persona | 3 |
| 🔴 **Extra** | Comparar k-means con jerárquico o DBSCAN y explicar la diferencia · ejes del PCA interpretados con las cargas · recomendación para un huésped nuevo (sin historial) | 4 |

\*Orientativo; puntúa el docente con la rúbrica del curso (0–4 en cada criterio). El mínimo es una entrega válida y evaluable; la «Definition of Done» describe el nivel **estándar**.

## Reparto sugerido de los 105 minutos (45 el día 1 · 60 el día 2)

| Min | Qué | Se sabe que está hecho cuando… |
|---|---|---|
| 10 | Cuaderno nuevo, datos cargados y variables escaladas | Existe `X` con 1200 filas y 7 columnas |
| 20 | k-means con `k` de 2 a 8, curva de silueta y elección de `k` | Hay una frase con la razón técnica y la de negocio |
| 15 | Mapa PCA, perfil de cada segmento, nombre y acción | Cada segmento tiene nombre, tamaño, cifras y acción |
| 30 | Dos recomendadores, RMSE, precision@3 y `recomendar` | La función no propone nada ya valorado |
| 30 | Ficha, nota de IA, revisión con la rúbrica y subida | Todo está en `sprint-09/` |

## Frases para la ficha de segmentos

- «Segmento … («…»): … huéspedes (… %). Perfil: … Acción comercial: …»
- «Elegimos k = … porque la silueta es … y, para el negocio, … grupos es un número que se puede gestionar.»
- «Nuestro recomendador (…) mejora a la popularidad en precision@3 (… frente a …), aunque su RMSE es …»
- «Riesgos: … (por ejemplo, que un segmento se use para …). Medida: …»

## Antes de entregar
- **Archivos subidos en `sprint-09/`:** `reto_S09_conocer_al_huesped.ipynb` · `ficha_segmentos.md` · `autoevaluacion_nombre.md` (**uno por persona**) = 2 + N ficheros
- [ ] Cuaderno de arriba abajo («Reiniciar y ejecutar todo»), semillas fijas · [ ] Ficha de 1 página con nombre, tamaño, perfil y acción por segmento
- [ ] Mapa 2D con PCA · [ ] Nota de IA responsable y sección «Revisión con la rúbrica» rellena · [ ] ≥ 1 *commit* por persona
- [ ] [Autoevaluación y coevaluación](../4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md): **una por persona**, subida a `sprint-09/`
