# Datos del curso · TurisData Canarias

Todos los datos son **sintéticos** (inventados para el curso): las relaciones que contienen **no son estadísticas reales** del turismo en Canarias.
Los notebooks los descargan solos con la función `dato("archivo")`; no hace falta que los subas a mano.

| Archivo | Contenido | Se usa en |
|---|---|---|
| `reservas_turisdata.csv` | 6.000 reservas; objetivo `cancelada` | Sprints 3–8, 10, 13 |
| `reservas_sucio.csv` | 1.500 reservas con defectos de calidad | Sprint 6 |
| `turisdata.db` | Base SQLite: `alojamientos`, `clientes`, `reservas` | Sprints 3 y 5 |
| `ocupacion_diaria.csv` | Serie diaria 2023–2025 de un alojamiento | Sprints 5 y 12 |
| `huespedes.csv` | 1.200 huéspedes para segmentar | Sprint 9 |
| `valoraciones_experiencias.csv`, `experiencias.csv` | Valoraciones y catálogo de 25 experiencias | Sprint 9 |
| `resenas.csv` | 1.500 reseñas en español con sentimiento | Sprint 12 |
| `politica_alojamiento.md`, `preguntas_referencia.csv` | Corpus y preguntas del asistente RAG | Sprint 12 |
| `informe_cliente.csv`, `informe_cliente.md` | Informe con errores estadísticos para auditar | Sprint 2 |
