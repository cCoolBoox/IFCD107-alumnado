# BiciPrevisión · Las Palmeras IA

**Brief:** Libre (inspirado en el 4: serie horaria) · **Curso:** IFCD107 · Especialista en IA · **Defensa:** día 2 del Sprint 17

## 1. El problema en 3 líneas
- **Pregunta de negocio:** ¿podemos prever cuántas bicis se alquilarán en cada hora de mañana para que el operador decida cuántas recolocar en cada turno?
- **Decisión que apoya y para quién:** cuántas bicis y personas de redistribución poner en cada franja; responsable de operaciones de un sistema de bicis compartidas.
- **Métrica de éxito:** negocio: evitar al menos 17 bicis de error por hora · técnica: MAE (bicis/hora) · baseline: misma hora de la semana pasada (MAE 69,5); umbral: bajar un 25 % (≤ 52,1).

## 2. Resultados en una tabla
| Modelo | Métrica principal (validación) | Métrica en test | Tiempo | Notas |
|---|---|---|---|---|
| Baseline (semana pasada) | MAE 69,5 | *(se mira una vez, en S16)* | — | WAPE 24 %; hora punta 133 |
| Media de 4 semanas | MAE 57,6 | — | — | segundo baseline |
| Modelo 1 | *(Sprint 15)* | | | |
| **Candidato final** | *(Sprint 15)* | *(Sprint 16)* | | |

## 3. Estructura del repositorio
```
.
├── README.md
├── requirements.txt
├── sprint-14/        # ficha, plan de datos, 01_eda, 02_baseline, backlog, riesgos, descargar_datos.py
├── sprint-15/        # (se rellena en el Sprint 15)
├── sprint-16/        # (se rellena en el Sprint 16)
└── sprint-17/        # (se rellena en el Sprint 17)
```
*(Cada `sprint-NN/` lleva además una hoja `autoevaluacion_nombre.md` por persona.)*

## 4. Cómo reproducirlo (pasos exactos)
**Requisitos:** Python 3.13.18 · Linux (probado) · sin GPU.

```bash
git clone [url-del-repositorio]
cd [carpeta]
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python sprint-14/descargar_datos.py   # descarga la fuente de la UCI en data/ y comprueba filas y huella (unos segundos)
# después, ejecuta los cuadernos en orden: sprint-14/01_eda.ipynb y sprint-14/02_baseline.ipynb
```
Tiempo total aproximado: 2 minutos. **Semilla fija:** `SEMILLA = 42` (primera celda de cada cuaderno). Debe salir **MAE 69,5** del *baseline* en validación.

## 5. Cómo lanzar el demostrador
*(Se rellena en el Sprint 16.)*

## 6. Datos y licencias
| Conjunto | Fuente | Licencia | ¿Incluido en el repo? |
|---|---|---|---|
| Bike Sharing Dataset (`hour.csv`) | https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset | CC BY 4.0 | no (se descarga con el script) |

**No hay datos personales** en el repositorio: alquileres agregados por hora.

## 7. IA responsable (resumen)
- Clasificación de riesgo (AI Act): **mínimo**. Datos personales: **no**.
- Principales riesgos y medidas: clima real usado como previsión (modelo con y sin clima), fuga de `casual`/`registered` (excluidas) y uso sin supervisión humana (aviso de incertidumbre). Detalle en `sprint-14/riesgos_eticos.md`.
- **Limitaciones y usos no permitidos:** una ciudad, un operador, 2011–2012; no usar para recortar servicio sin revisión humana.
- **Uso de IA:** se pidió una primera lista de variables y explicar WAPE; **se comprobó a mano** la licencia (CC BY 4.0 en la página de la UCI, no MIT como dijo la IA al principio) y el tamaño del conjunto; **se cambió** el número de filas: la IA dijo que había 17.544 (todas las horas de dos años) y con `len(horas)` salen 17.379: faltan 165 horas sin alquileres, que creamos con 0.

## 8. Equipo y contribuciones
| Persona | Roles (S14 / S15 / S16) | Contribución principal |
|---|---|---|
| Marta | Scrum Master / Responsable técnica / Responsable de datos | ficha, backlog, tablero |
| Persona B | Responsable técnico / Responsable de datos / Responsable de IA responsable | `02_baseline.ipynb` |
| Persona C | Responsable de datos / Responsable de IA responsable / Scrum Master | plan de datos, `descargar_datos.py` |
| Persona D | Responsable de IA responsable / Scrum Master / Responsable técnico | `riesgos_eticos.md`, README |

Convención de commits: `tipo: descripción` (`feat:`, `fix:`, `docs:`, `data:`, `exp:`). Todas las personas tienen commits propios.

## 9. Evidencias de metodología
- Tablero con las 13 historias (capturas en `sprint-14/scrum/`) · Backlog: `sprint-14/backlog_y_sprints.md` · Retro del Sprint 14 al final del backlog.

## 10. Créditos y licencia del código
Datos: Fanaee-T y Gama (2013), UCI, CC BY 4.0. Librerías: numpy 2.5.3, pandas 2.3.3, matplotlib 3.11.2, scikit-learn 1.9.1. Licencia del código: MIT.

## Revisión con la rúbrica

**Revisado por:** Persona D (no escribió esa parte) · **Fecha:** 30/11/2026

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
|---|---|---|
| Corrección técnica | 4 | Los dos cuadernos se ejecutan de arriba abajo; la métrica y la partición están escritas **antes** del baseline y una aserción comprueba que no hay fuga; el EDA por franja y clima encontró un hallazgo (la hora punta) que cambió la ficha |
| Reproducibilidad | 4 | Seguí solo este README: `descargar_datos.py` bajó los datos de la UCI desde cero, comprobó la huella y el baseline dio el mismo MAE de 69,5; hay versión de Python, semilla y linaje completo |
| Análisis y comunicación al cliente | 4 | La ficha dice qué decisión mejora y qué pasa hoy sin el modelo; cuantifica el valor (al menos 17 bicis de error menos por hora) y explica qué cambió tras el EDA |
| IA responsable | 4 | 7 riesgos específicos con P, I, medida y responsable, los altos enlazados a historias; el uso de IA cuenta un fallo concreto (el número de filas) y cómo se detectó |

**Lo primero que mejoraríamos:** comprobar el modelo con un clima previsto con error y no con el clima real (R-01).
