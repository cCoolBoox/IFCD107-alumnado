# Plan de datos y licencias

**Proyecto:** ______ · **Responsable de datos:** ______ · **Última actualización:** ______

> Sin licencia clara no hay proyecto (R2). Si un dato no tiene licencia, no lo uséis: preguntad al docente.

## 1. Inventario de fuentes
| ID | Nombre del conjunto | Fuente / enlace | Fecha de descarga | Licencia | ¿Permite uso académico / redistribución? | Formato y tamaño | ¿Datos personales? |
|---|---|---|---|---|---|---|---|
| D1 | | | | | | | sí / no |
| D2 | | | | | | | |

**Licencias frecuentes (orientativo, léelas siempre en la fuente):**
- **CC BY 4.0:** libre uso con atribución. **CC BY-SA:** además, misma licencia al redistribuir. **CC BY-NC:** solo uso no comercial. **CC0:** dominio público.
- **Licencias de datos abiertos de administraciones:** normalmente exigen citar la fuente y la fecha.
- **Kaggle / Hugging Face:** cada conjunto tiene su propia licencia; **no asumas** que es libre.

## 2. Descripción de las variables (diccionario de datos)
| Variable | Tipo | Unidad | Significado | Valores válidos | % nulos |
|---|---|---|---|---|---|
| | | | | | |

## 3. Informe de calidad del dato (resumen del EDA)
| Aspecto | Hallazgo | Acción tomada y justificación |
|---|---|---|
| Nulos | | |
| Duplicados | | |
| Valores imposibles / outliers | | |
| Formatos y tipos | | |
| **Sesgo de muestreo** (¿quién o qué falta en los datos?) | | |
| Desequilibrio de clases / periodos | | |
| **Fuga de datos potencial** (variables que no se conocen al decidir) | | |

## 4. Linaje del dato (de dónde viene y qué le hemos hecho)
```
Fuente original → descarga (fecha, versión) → limpieza (script) → variables derivadas (script) → partición train / val / test → modelo
```
- Script de descarga / preparación: `src/datos/preparar.py` *(ruta)*.
- **Huella (hash) del conjunto final:** ______ *(ver notebook S15_01)*.
- ¿Se puede recrear todo desde el README? sí / no.

## 5. Partición de datos
- Estrategia: aleatoria estratificada · por fechas (series) · por grupos (p. ej. por usuario / imagen del mismo objeto).
- Tamaños: entrenamiento ___ · validación ___ · test ___ (**el test no se toca hasta el final**).
- Justificación de por qué evita fugas: ______

## 6. Privacidad y RGPD
- ¿Hay datos personales? sí / no. Si sí: base legal, minimización, anonimización / seudonimización, quién accede: ______
- ¿Hay datos de menores, salud, biometría u otras categorías especiales? sí / no (si sí, **consultad al docente antes de seguir**).
- Datos que **no** subiremos al repositorio: ______ (ponerlos en `.gitignore`).

## 7. Atribución y cita (pegar tal cual en la memoria)
> Fuente, autor / organismo, título, año, versión, enlace, licencia.
