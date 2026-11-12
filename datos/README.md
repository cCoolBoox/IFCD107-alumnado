# Datos del curso · TurisData Canarias

Los datos de TurisData son **sintéticos** (inventados para el curso): las relaciones que contienen **no son estadísticas reales** del turismo en Canarias. Los de las bolsas de miniretos son inventados salvo los marcados como reales (UCI, Pima, diamantes), que se citan con su licencia.
Los notebooks los descargan solos con la función `dato("archivo")`; no hace falta que los subas a mano.

| Archivo | Contenido | Se usa en |
|---|---|---|
| `reservas_turisdata.csv` | 6.000 reservas; objetivo `cancelada` | Sprints 3–8, 10, 13 |
| `reservas_sucio.csv` | 1.545 filas con defectos de calidad (1.500 reservas distintas: hay 45 duplicados exactos; nulos en `pais_origen`, `regimen`, `adultos` y `precio_noche`) | Sprint 6 |
| `turisdata.db` | Base SQLite: `alojamientos`, `clientes`, `reservas` | Sprints 3 y 5 |
| **Esquema de `turisdata.db`** | Tablas, campos y relaciones en una imagen: [`esquema_turisdata.md`](../sprints/S03/2_Practica/esquema_turisdata/esquema_turisdata.md) | Sprints 3 y 5 |
| `turisdata.sql` | La misma base en **texto SQL**: se importa en DB Browser si `turisdata.db` no se abre bien | Sprints 3 y 5 |
| `ocupacion_diaria.csv` | Serie diaria 2023–2025 de un alojamiento | Sprints 5 y 12 |
| `correos.csv` | 1.500 correos en español inventados (`asunto`, `texto`, `es_spam`) | Bolsa de miniretos (S08) |
| `viviendas_tenerife.csv` | 1.800 viviendas inventadas (`precio` y 10 variables) | Bolsa de miniretos (S08) |
| `diabetes_pima.csv` | 768 mujeres del estudio Pima (UCI, dominio público); los ceros imposibles son datos que faltan | Bolsa de miniretos (S08) |
| `aire_calidad.csv` | 9 357 horas de sensores de calidad del aire de una ciudad italiana (UCI, CC BY 4.0, tal cual: `;`, coma decimal y `-200` = sin dato) | Bolsa de miniretos (S06) |
| `estudiantes_mates.csv` | 395 estudiantes de dos colegios de Portugal, nota de matemáticas (UCI, CC BY 4.0, tal cual: separado por `;`) | Bolsa de miniretos (S06) |
| `coches_sucio.csv` | 1.245 anuncios de coches inventados y **muy sucios** (45 repetidos, formatos mezclados) | Bolsa de miniretos (S06) |
| `bicis_horas.csv` | 17.379 horas de bicis compartidas de Washington D. C. (UCI, CC BY 4.0, tal cual) | Bolsa de miniretos (S06) |
| `fraude_tarjeta.csv` | 20.000 compras inventadas con un 1,5 % de fraudes | Bolsa de miniretos (S07) |
| `abandono_streaming.csv` | 5.000 clientes inventados de una plataforma de series (`abandona`) | Bolsa de miniretos (S07) |
| `diamantes.csv` | Muestra al azar de 6.000 diamantes reales (conjunto `diamonds` de ggplot2) | Bolsa de miniretos (S07) |
| `consumo_solar.csv` | 1.096 días de consumo eléctrico de una casa inventada con placas solares | Bolsa de miniretos (S07) |
| `tramposos_juego.csv` | 4.000 jugadores inventados, 6 % de tramposos | Bolsa de miniretos (S08) |
| `incendios_canarias.csv` | 5.000 zonas-día inventadas, 6 % con incendio | Bolsa de miniretos (S08) |
| `triaje_urgencias.csv` | 4.000 pacientes inventados, 13 % urgentes | Bolsa de miniretos (S08) |
| `huespedes.csv` | 1.200 huéspedes para segmentar | Sprint 9 |
| `valoraciones_experiencias.csv`, `experiencias.csv` | 2.232 valoraciones (de los huéspedes 1 a 300) y catálogo de 25 experiencias | Sprint 9 |
| `resenas.csv` | 1.500 reseñas en español con sentimiento | Sprint 12 |
| `politica_alojamiento.md`, `preguntas_referencia.csv` | Corpus y preguntas del asistente RAG | Sprint 12 |
| `informe_cliente.csv`, `informe_cliente.md` | Informe con errores estadísticos para auditar. **Ahora están en [`sprints/S02/3_Reto/1_Trabajar/plantillas/`](../sprints/S02/3_Reto/1_Trabajar/plantillas/)**, junto al resto del material del reto | Sprint 2 |
