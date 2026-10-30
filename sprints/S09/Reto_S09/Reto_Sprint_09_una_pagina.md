# Sprint 9 · Reto «Conocer al huésped» · en una página

> Versión corta para **trabajar con ella abierta**. La ficha completa sigue en [Reto_Sprint_09.md](Reto_Sprint_09.md); la plantilla de la ficha de segmentos está en [`plantilla_ficha_segmentos.md`](plantilla_ficha_segmentos.md).

**El cliente.** Lucía, la directora comercial, envía la misma newsletter a sus 1.200 huéspedes y vende las 25 experiencias con los mismos banners. Pide: *«Decidme quiénes son mis clientes, cómo los llamo y qué le enseño a cada uno.»* Aquí **no hay respuesta correcta en los datos**: hay que descubrir los grupos y darles sentido de negocio.
**Qué entregáis (no cambia):** un cuaderno, una **ficha de segmentos de 1 página** y una nota de IA responsable (dentro de la ficha).
**Tiempo en clase:** planning 10 min · reto 95 min (45 el 13/11 y 50 el 16/11) · entrega, review y retro 40 min.

## Tres niveles: el equipo decide hasta dónde llega

| Nivel | Qué hay que tener | Nota* |
|---|---|---|
| 🟢 **Mínimo** (todos los equipos) | Variables **escaladas** antes de agrupar · `k` elegido con la silueta y una razón de negocio · mapa 2D con PCA (segmentos coloreados) · ficha con **nombre, tamaño, perfil y una acción comercial por segmento** · nota de IA responsable de 5 líneas | 2 |
| 🟡 **Estándar** | Recomendador de experiencias comparando **dos métodos** con RMSE y precision@3, frente a la popularidad · `recomendar(id_usuario, n)` que no propone experiencias ya valoradas · nota de IA con dos riesgos concretos · un *commit* por persona | 3 |
| 🔴 **Extra** | Comparar k-means con jerárquico o DBSCAN y explicar la diferencia · ejes del PCA con su % de varianza interpretados · recomendación para un huésped nuevo (sin historial) | 4 |

\*Orientativo; puntúa el docente con la rúbrica del curso (0–4 en cada criterio). El mínimo es una entrega válida y evaluable; la «Definition of Done» de la ficha completa describe el nivel **estándar**.

## Frases para la ficha de segmentos

- «Segmento … («…»): … huéspedes (…  %). Perfil: … Acción comercial: …»
- «Elegimos k = … porque la silueta es … y, para el negocio, … grupos es un número que se puede gestionar.»
- «Nuestro recomendador (…) mejora a la popularidad en precision@3 (… frente a …), aunque su RMSE es …»
- «Riesgos: … (por ejemplo, que un segmento se use para …). Medida: …»

## Antes de entregar
- [ ] Cuaderno de arriba abajo, semillas fijas · [ ] Ficha de 1 página con nombre, tamaño, perfil y acción por segmento
- [ ] Mapa 2D con PCA · [ ] Nota de IA responsable · [ ] [Autoevaluación y coevaluación](autoevaluacion_y_coevaluacion.md) rellenadas
