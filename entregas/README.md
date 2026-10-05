# Entregas de los equipos

**Cada equipo trabaja en su propio repositorio de GitHub.** En esta carpeta no se sube nada: aquí solo está la tabla [`equipos.md`](equipos.md) con el enlace al repositorio de cada equipo.

## Cómo se entrega

1. En el Sprint 0 hacéis la actividad [Crea el repositorio de tu equipo](../sprints/S00/actividad_repositorio_equipo.md): se crea el repositorio (`ifcd107-equipo-<nombre>`) a partir de la [plantilla](../material/plantilla-equipo.zip) y se añade al resto del equipo y al docente como colaboradores.
2. Cada sprint se entrega en su propia carpeta del repositorio: `sprint-01/`, `sprint-02/`… `sprint-17/`.
3. Abrís un *issue* en este repositorio con el enlace y el docente lo apunta en [`equipos.md`](equipos.md). Si algo no está bien, abre otro *issue*.
4. Entrega = lo que esté en la carpeta `sprint-XX/` a la hora de cierre del sprint (la fecha de cada sprint está en su ficha de reto).

## Estructura del repositorio del equipo

```
README.md          # equipo, problema, cómo ejecutar y enlaces a cada sprint
requirements.txt
data/              # solo datos con licencia y sin datos personales (o script de descarga)
sprint-01/         # entregable del sprint 1 (README.md + notebook o documento)
sprint-02/
...
notebooks/         # trabajo compartido
src/               # código reutilizable
docs/              # ficha de proyecto y memoria técnica (sprints 14-17)
```

Cada carpeta `sprint-XX/` debe incluir un `README.md` corto: qué se entrega, quién hizo qué y cómo reproducirlo.

## Reglas

- Todos los integrantes deben aparecer en el historial de *commits*.
- **Nunca** subas claves, contraseñas ni datos personales.
- Las soluciones de los laboratorios no se publican.
