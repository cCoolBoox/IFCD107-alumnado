# Actividad · Crea el repositorio de tu equipo

**Cuándo:** Sprint 0 · **Duración:** 45 min · **En equipo (3–4 personas)** · Una persona lo crea; las demás lo comprueban y practican.
**Antes de empezar:** todas las personas tenéis cuenta de GitHub (ver [`material/01_Primeros_pasos_con_GitHub.pdf`](../../material/01_Primeros_pasos_con_GitHub.pdf)).

**Resultado:** un repositorio con la estructura del curso, con todo el equipo y el docente dentro, y su enlace anotado en [`entregas/equipos.md`](../../entregas/equipos.md).

---

## Parte 1 · Crear el repositorio (quien tenga el rol de responsable técnico)

1. En GitHub, pulsa **+** (arriba a la derecha) → **New repository**.
2. **Repository name:** `ifcd107-equipo-` + nombre de tu consultora, sin espacios ni tildes (ej. `ifcd107-equipo-atlantico`).
3. Marca **Private** (privado) y **Add a README file**. Pulsa **Create repository**.

## Parte 2 · Subir la estructura

1. Descarga [`plantilla-equipo.zip`](../../material/plantilla-equipo.zip) y descomprímelo.
2. En tu repositorio, pulsa **Add file → Upload files**.
3. Arrastra **el contenido** de la carpeta descomprimida (no la carpeta `plantilla-equipo` en sí): `README.md`, `requirements.txt`, `.gitignore` y las carpetas `sprint-01` … `sprint-17`, `data`, `notebooks`, `src`, `docs`.
4. Abajo, en *Commit changes*, escribe un mensaje claro: `Estructura inicial del equipo`. Pulsa **Commit changes**.

> Si tu navegador no deja arrastrar carpetas, sube primero los archivos sueltos y después usa **Add file → Create new file**, escribiendo `sprint-01/README.md` (la barra `/` crea la carpeta).

## Parte 3 · Invitar al equipo y al docente

1. **Settings → Collaborators → Add people**.
2. Añade a cada integrante y a tu docente (usuario que te dará en clase).
3. Cada persona acepta la invitación (llega por correo y en github.com/notifications).

## Parte 4 · Cada persona hace su primer commit

1. Abre `README.md` → icono del lápiz ✏️.
2. En la tabla **Equipo**, añade tu fila: nombre, usuario de GitHub y rol.
3. **Commit changes** con el mensaje `Añado mi fila al equipo`.

> Si dos personas editan a la vez, GitHub puede avisar de un conflicto: repite la edición sobre la versión actual. Es normal; lo veremos en clase.

## Parte 5 · Registrar el repositorio

Abre un *issue* en el repositorio del curso (pestaña **Issues → New issue**):

- **Título:** `Repositorio del equipo <nombre de la consultora>`
- **Texto:** enlace al repositorio y usuarios de GitHub de todas las personas.

Tu docente lo añade a [`entregas/equipos.md`](../../entregas/equipos.md).

---

## ✅ Lista de comprobación

- [ ] El repositorio es **privado** y se llama `ifcd107-equipo-…`
- [ ] Aparecen las carpetas `sprint-01` a `sprint-17`
- [ ] Todas las personas y el docente son colaboradores
- [ ] Cada persona tiene al menos un commit en el historial
- [ ] El issue con el enlace está abierto

## Cómo se entregará cada sprint

Al terminar cada sprint, subid vuestro entregable a la carpeta `sprint-XX/` (**Add file → Upload files**), rellenad su `README.md` (qué se entrega, quién hizo qué, cómo reproducirlo) y haced el commit antes del cierre. Más detalle en [`entregas/README.md`](../../entregas/README.md).
