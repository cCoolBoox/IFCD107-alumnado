# Ficha de segmentos de huéspedes · TurisData Canarias

**Equipo:** ______ · **Fecha:** ______ · **Método elegido:** k-means / jerárquico / DBSCAN (tacha lo que no) · **k = ___** · **Silueta = ___**

**¿Por qué este método y este k?** (2 líneas: métrica y criterio de negocio)

______________________________________________

## Mapa de segmentos
*(Pega aquí la figura PCA en 2D con los segmentos coloreados. Título con la conclusión, ejes con el % de varianza.)*

## Segmentos

| Segmento | Nombre comercial | Tamaño (n y %) | Perfil en una frase (cifras concretas) | Acción comercial | Experiencia estrella |
|---|---|---|---|---|---|
| 0 | | | | | |
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

*(Ejemplo de fila: «Familias de larga estancia · 410 (34 %) · 9 de cada 10 viajan con niños, reservan con 110 días de antelación y gastan poco en actividades · Pack «Niños gratis en el parque acuático» en la reserva · Parque acuático»)*

## Recomendador
- Métodos comparados: ______ (RMSE ___ / precision@3 ___), ______ (RMSE ___ / precision@3 ___).
- Método elegido y por qué: ______
- Ejemplo: usuario ___ → recomendaciones: ______ (nota prevista ___)
- ¿Qué haría el sistema con un **huésped nuevo sin valoraciones**? ______

## IA responsable (5 líneas)
- Riesgo 1 (segmentar): ______ · Medida: ______
- Riesgo 2 (recomendar): ______ · Medida: ______
- Datos personales implicados y base legal: ______

## Limitaciones
Datos sintéticos, comportamiento de un año, valoraciones escasas (4-11 por usuario)… añade las tuyas: ______

## Revisión con la rúbrica
<Rúbrica completa en la ficha del reto, apartado 3. La rellena quien revisa y **no escribió esa parte**: ejecutar el cuaderno de arriba abajo, leer esta ficha como si fuera Lucía, mirar el cuaderno, poner un nivel con prueba. Esta sección no cuenta en la página de la ficha.>

**Revisado por:** <nombre> · **Fecha:** <dd/mm/aaaa>

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
|---|---|---|
| Corrección técnica | <1–4> | <p. ej. «el cuaderno se ejecuta entero y escala antes de agrupar, pero `recomendar` solo está probada con 1 usuario»> |
| Reproducibilidad | <1–4> | <¿salen el mismo k, los mismos tamaños y la misma tabla RMSE y precision@3 al reiniciar y ejecutar todo?> |
| Análisis y comunicación al cliente | <1–4> | <¿entiende Lucía qué hacer con cada segmento? ¿los tamaños suman 1.200?> |
| IA responsable | <1–4> | <¿hay al menos 2 riesgos de este caso, cada uno con su medida?> |

**Lo primero que mejoraríamos:** <una cosa concreta>
