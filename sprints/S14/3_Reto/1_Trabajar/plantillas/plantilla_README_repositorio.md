# [Nombre del proyecto] · [Nombre del equipo]

> *Copia este archivo como `README.md` en la raíz del repositorio del equipo y sustituye lo que está entre corchetes. Un compañero de otro equipo debe poder ejecutar el proyecto **solo con este README** (criterio F de la rúbrica). Lo que ya no sepas en el Sprint 14 (resultados, demostrador) lo dejas con corchetes y lo rellenas en los sprints 15 y 16: en el 16 subes la versión final también a `sprint-16/`. Los ficheros de cada sprint van en su carpeta `sprint-NN/`, como en el árbol del apartado 3.*

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

*(Detalle en `sprint-16/docs/memoria_tecnica.pdf` y en `sprint-15/registro.csv`.)*

## 3. Estructura del repositorio
```
.                              # raíz del repositorio del equipo (ifcd107-equipo-…)
├── README.md                  # este archivo (la puerta de entrada)
├── requirements.txt           # versiones fijas
├── sprint-14/                 # definición y punto de partida
│   ├── ficha_proyecto.md
│   ├── plan_datos_licencias.md   # fuente, licencia, cómo descargar los datos
│   ├── 01_eda.ipynb
│   ├── 02_baseline.ipynb
│   ├── backlog_y_sprints.md
│   ├── riesgos_eticos.md
│   └── descargar_datos.py     # solo si no subís los datos
├── sprint-15/                 # experimentos
│   ├── registro.csv           # registro de experimentos
│   ├── 03_modelos.ipynb
│   ├── justificacion_candidato.md
│   ├── modelo_candidato.joblib, metadatos.json, explicacion_modelo.png
├── sprint-16/                 # entrega final
│   ├── README.md              # versión final de este README
│   ├── notebooks/04_evaluacion.ipynb
│   ├── demostrador/           # logica.py, app.py, tests/, requirements.txt
│   └── docs/                  # memoria_tecnica.pdf, model_card.md, riesgos_eticos.md, demo.mp4 (si pesa poco)
└── sprint-17/                 # defensa
    └── presentacion_defensa.pdf, plantilla_storytelling.md
```
*(Cada `sprint-NN/` lleva además una hoja `autoevaluacion_nombre.md` por persona. La coevaluación confidencial del anexo B **no se sube**: se entrega al docente.)*

## 4. Cómo reproducirlo (pasos exactos)
**Requisitos:** Python 3.11 · [Sistema operativo probado] · [GPU si es imprescindible: sí/no]

```bash
git clone [url-del-repositorio]
cd [carpeta]
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python sprint-14/descargar_datos.py   # descarga y prepara los datos (tarda ~[x] min); o el enlace del apartado 6
# después, ejecuta los cuadernos en orden: sprint-14/01_eda.ipynb, sprint-14/02_baseline.ipynb,
# sprint-15/03_modelos.ipynb y sprint-16/notebooks/04_evaluacion.ipynb
```
Tiempo total aproximado: [x] minutos. **Semilla fija:** `SEMILLA = 42` (definida en la primera celda de cada cuaderno).

## 5. Cómo lanzar el demostrador
```bash
cd sprint-16/demostrador
streamlit run app.py               # o: uvicorn api:app --reload
```
Se abre en <http://localhost:8501>. **Plan B:** vídeo en `sprint-16/docs/demo.mp4` [o enlace].
**Qué probar:** [3 entradas de ejemplo y qué resultado se espera].
**Entradas que no admite y qué mensaje muestra:** [ejemplo].

## 6. Datos y licencias
| Conjunto | Fuente | Licencia | ¿Incluido en el repo? |
|---|---|---|---|
| [ ] | [enlace] | [CC BY 4.0 / ...] | sí / no (se descarga con el script) |

**No hay datos personales** en el repositorio: [sí, confirmado / describir tratamiento].

## 7. IA responsable (resumen)
- Clasificación de riesgo (AI Act): [mínimo / limitado / alto]. Datos personales: [sí / no].
- Principales riesgos y medidas: [3 líneas]. Detalle en `sprint-16/docs/riesgos_eticos.md` y `sprint-16/docs/model_card.md`.
- **Limitaciones y usos no permitidos:** [2-3 líneas].

## 8. Equipo y contribuciones
| Persona | Roles (S14 / S15 / S16) | Contribución principal (enlaces a commits / PR) |
|---|---|---|
| | | |

Convención de commits: `tipo: descripción` (`feat:`, `fix:`, `docs:`, `data:`, `exp:`). **Todas las personas** deben tener commits propios.

## 9. Evidencias de metodología
- Tablero: [enlace al tablero, o capturas en una carpeta `scrum/` dentro del `sprint-NN/` que corresponda] · Backlog (`sprint-14/backlog_y_sprints.md`) · Planning / review / retro de cada sprint.

## 10. Créditos y licencia del código
Datos: [atribuciones]. Librerías principales: [lista con versiones]. Licencia del código: [MIT / propia].

## Revisión con la rúbrica
<Sprint 14. Rúbrica completa en la ficha del reto, apartado 3. Rellena quien revisa y **no escribió esa parte**: seguir solo este README para descargar los datos y ejecutar los cuadernos, leer la ficha como cliente, comprobar la fuente y la licencia, poner nivel con prueba.>

**Revisado por:** <nombre> · **Fecha:** <dd/mm/aaaa>

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
|---|---|---|
| Corrección técnica | <1–4> | <p. ej. «los dos cuadernos se ejecutan; la métrica se definió antes, pero falta el informe de duplicados»> |
| Reproducibilidad | <1–4> | <¿obtienes la misma métrica del baseline siguiendo solo este README?> |
| Análisis y comunicación al cliente | <1–4> | <¿se entiende la pregunta, la decisión que apoya y la métrica sin jerga?> |
| IA responsable | <1–4> | <¿hay al menos 5 riesgos específicos, y dice qué se pidió a la IA y qué se comprobó a mano?> |

**Lo primero que mejoraríamos:** <una cosa concreta>
