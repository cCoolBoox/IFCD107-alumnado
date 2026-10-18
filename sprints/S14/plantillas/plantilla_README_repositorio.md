# [Nombre del proyecto] · [Nombre del equipo]

> *Copia este archivo como `README.md` en la raíz del repositorio del equipo y sustituye lo que está entre corchetes. Un compañero de otro equipo debe poder ejecutar el proyecto **solo con este README** (criterio F de la rúbrica).*

**Brief:** [1 Demanda turística / 2 Cultivos / 3 Asistente FP / 4 Energía / Libre] · **Curso:** IFCD107 · Especialista en IA · **Defensa:** 14/12/2026

## 1. El problema en 3 líneas
- **Pregunta de negocio:** [una frase]
- **Decisión que apoya y para quién:** [cliente / usuario]
- **Métrica de éxito:** negocio [__] · técnica [__] · baseline [__]

## 2. Resultados en una tabla
| Modelo | Métrica principal (validación) | Métrica en test | Tiempo | Notas |
|---|---|---|---|---|
| Baseline | | | | |
| Modelo 1 | | | | |
| Modelo 2 | | | | |
| **Candidato final** | | | | |

*(Detalle en `docs/memoria_tecnica.pdf` y en `experimentos/registro.csv`.)*

## 3. Estructura del repositorio
```
.
├── README.md                  # este archivo
├── requirements.txt           # versiones fijas
├── .gitignore                 # datos grandes, claves, modelos pesados
├── datos/
│   ├── README_datos.md        # fuente, licencia, cómo descargar (plan de datos)
│   └── descargar_datos.py     # script de descarga o preparación (si los datos no se incluyen)
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_baseline.ipynb
│   ├── 03_modelos.ipynb
│   └── 04_evaluacion.ipynb
├── src/                       # código reutilizable (funciones, entrenamiento)
├── experimentos/registro.csv  # registro de experimentos
├── modelo/                    # modelo final + metadatos.json (o cómo generarlo)
├── demostrador/               # app.py / api.py / logica.py
├── tests/                     # pruebas (pytest -q)
└── docs/
    ├── ficha_proyecto.pdf
    ├── memoria_tecnica.pdf
    ├── model_card.md
    ├── riesgos_eticos.md
    ├── coevaluacion.md        # (solo el docente la recibe: no incluir datos personales de terceros)
    └── scrum/                 # exportación del tablero, retros, planning
```

## 4. Cómo reproducirlo (pasos exactos)
**Requisitos:** Python 3.11 · [Sistema operativo probado] · [GPU si es imprescindible: sí/no]

```bash
git clone [url-del-repositorio]
cd [carpeta]
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python datos/descargar_datos.py    # descarga y prepara los datos (tarda ~[x] min)
python src/entrenar.py             # o ejecuta los notebooks 01 a 04 en orden
```
Tiempo total aproximado: [x] minutos. **Semilla fija:** `SEMILLA = 42` (definida en `src/config.py`).

## 5. Cómo lanzar el demostrador
```bash
cd demostrador
streamlit run app.py               # o: uvicorn api:app --reload
```
Se abre en <http://localhost:8501>. **Plan B:** vídeo en `docs/demo.mp4` [o enlace].
**Qué probar:** [3 entradas de ejemplo y qué resultado se espera].
**Entradas que no admite y qué mensaje muestra:** [ejemplo].

## 6. Datos y licencias
| Conjunto | Fuente | Licencia | ¿Incluido en el repo? |
|---|---|---|---|
| [ ] | [enlace] | [CC BY 4.0 / ...] | sí / no (se descarga con el script) |

**No hay datos personales** en el repositorio: [sí, confirmado / describir tratamiento].

## 7. IA responsable (resumen)
- Clasificación de riesgo (AI Act): [mínimo / limitado / alto]. Datos personales: [sí / no].
- Principales riesgos y medidas: [3 líneas]. Detalle en `docs/riesgos_eticos.md` y `docs/model_card.md`.
- **Limitaciones y usos no permitidos:** [2-3 líneas].

## 8. Equipo y contribuciones
| Persona | Roles (S14 / S15 / S16) | Contribución principal (enlaces a commits / PR) |
|---|---|---|
| | | |

Convención de commits: `tipo: descripción` (`feat:`, `fix:`, `docs:`, `data:`, `exp:`). **Todas las personas** deben tener commits propios.

## 9. Evidencias de metodología
- Tablero: [enlace o exportación en `docs/scrum/`] · Backlog · Planning / review / retro de cada sprint.

## 10. Créditos y licencia del código
Datos: [atribuciones]. Librerías principales: [lista con versiones]. Licencia del código: [MIT / propia].
