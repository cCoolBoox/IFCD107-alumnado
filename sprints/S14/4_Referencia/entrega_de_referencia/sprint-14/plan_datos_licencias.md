# Plan de datos y licencias

**Proyecto:** BiciPrevisión (Las Palmeras IA) · **Responsable de datos:** Persona C · **Última actualización:** 27/11/2026

> Sin licencia clara no hay proyecto (R2). Aquí hay una sola fuente y su licencia es CC BY 4.0.

## 1. Inventario de fuentes
| ID | Nombre del conjunto | Fuente / enlace | Fecha de descarga | Licencia | ¿Permite uso académico / redistribución? | Formato y tamaño | ¿Datos personales? |
|---|---|---|---|---|---|---|---|
| D1 | Bike Sharing Dataset (`hour.csv`) | https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset | 26/11/2026 | CC BY 4.0 | Sí, con atribución | CSV, 17.379 filas × 17 columnas, 1,1 MB; periodo 2011-01-01 → 2012-12-31 | no |

## 2. Descripción de las variables (diccionario de datos)
| Variable | Tipo | Unidad | Significado | Valores válidos | % nulos |
|---|---|---|---|---|---|
| `dteday`, `hr` | fecha, entero | día, hora | Día y hora de la medida | 2011-01-01…2012-12-31; 0–23 | 0 % |
| `season`, `yr`, `mnth` | entero | — | Estación, año (0 = 2011, 1 = 2012), mes | 1–4; 0–1; 1–12 | 0 % |
| `holiday`, `workingday`, `weekday` | entero | — | Festivo, laborable y día de la semana | 0/1; 0/1; 0–6 | 0 % |
| `weathersit` | entero | — | 1 despejado · 2 nublado · 3 lluvia o nieve ligera · 4 tormenta | 1–4 | 0 % |
| `temp`, `atemp`, `hum`, `windspeed` | decimal | normalizado 0–1 (temp ×41 = °C) | Temperatura, sensación térmica, humedad y viento | 0–1 | 0 % |
| `casual`, `registered`, `cnt` | entero | bicis | Alquileres de ocasionales, de registrados y total (`cnt` = suma) | ≥ 0 | 0 % |

## 3. Informe de calidad del dato (resumen del EDA)
| Aspecto | Hallazgo | Acción tomada y justificación |
|---|---|---|
| Nulos | 0 en todo el fichero | Ninguna |
| Duplicados | 0 filas duplicadas | Ninguna |
| Valores imposibles / outliers | Humedad = 0 en 22 filas de un solo día; viento = 0 en 2.180 filas (12 %) | Se dejan y se anotan: no se pueden corregir sin inventar |
| Formatos y tipos | Fecha y hora separadas | Se unen en una marca de tiempo y se crea una fila por hora |
| **Sesgo de muestreo** (¿quién o qué falta en los datos?) | Una ciudad, un operador, 2 años; solo 3 horas de tormenta | Se declara el alcance en README y *model card*; no se promete generalizar |
| Desequilibrio de clases / periodos | La demanda de 2012 es un 64 % mayor que la de 2011 | Partición temporal y variables de retraso en vez del año |
| **Fuga de datos potencial** | `casual` y `registered` suman `cnt`; el clima real no se conoce de antemano | Se excluyen `casual` y `registered`; el clima se usa como previsión y se anota el riesgo |
| Horas que faltan | 165 de 17.544 horas no están en el fichero (madrugada) | Se crean con 0 alquileres y se marcan |

## 4. Linaje del dato (de dónde viene y qué le hemos hecho)
```
UCI Bike Sharing (hour.csv) → descarga (26/11/2026) → data/bicis_horas.csv → serie horaria completa (huecos = 0) → variables (retrasos de 24 h o más) → partición por fechas → modelo
```
- Script de descarga / preparación: `sprint-14/descargar_datos.py` (comprueba filas y huella).
- **Huella (hash) del conjunto final:** `b03a2d02e8c10f43…` (sha256 completo en `descargar_datos.py`).
- ¿Se puede recrear todo desde el README? **sí**.

## 5. Partición de datos
- Estrategia: **por fechas** (hay una serie: nunca se baraja).
- Tamaños: entrenamiento 13.944 horas (hasta 31/8/2012) · validación 1.464 (sep–oct 2012) · test 1.464 (nov–dic 2012). **El test no se toca hasta que haya un modelo candidato** y entonces se mira una sola vez.
- Justificación de por qué evita fugas: todo lo que se usa para predecir una hora de mañana es anterior a las 23:00 de hoy (retrasos de 24 h o más) y los tres tramos están ordenados en el tiempo; se comprueba con una aserción en `02_baseline.ipynb`.

## 6. Privacidad y RGPD
- ¿Hay datos personales? **No**: el fichero tiene alquileres agregados por hora, sin usuarios, estaciones ni trayectos.
- ¿Datos de menores, salud, biometría u otras categorías especiales? **No.**
- Datos que **no** subiremos al repositorio: ninguno; el CSV pesa 1,1 MB y su licencia permite redistribuirlo, pero se sube solo el script de descarga.

## 7. Atribución y cita (pegar tal cual en la memoria)
> Fanaee-T, Hadi, and Gama, Joao, «Event labeling combining ensemble detectors and background knowledge», *Progress in Artificial Intelligence* (2013): pp. 1-15, Springer Berlin Heidelberg. Conjunto «Bike Sharing Dataset», UCI Machine Learning Repository, https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset. Licencia CC BY 4.0.
