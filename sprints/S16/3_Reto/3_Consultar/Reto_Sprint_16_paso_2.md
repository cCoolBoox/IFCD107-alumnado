# Paso 2 · Abrir la memoria y la model card (día 1, 85 minutos)

<!--nav-->
> Sprint 16 · Reto «Entrega final: evaluar, demostrar y documentar» · paso 2 de 8 · [Ficha del reto](Reto_Sprint_16.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_16_una_pagina.md) · [Paso 3 →](Reto_Sprint_16_paso_3.md)
<!--/nav-->

1. Repartir las secciones de la memoria entre las personas del equipo.
2. Copiar el esqueleto de la memoria y la plantilla de la model card y rellenar lo que ya sabéis.
3. Dejar el demostrador básico funcionando y anotar lo que falta y quién lo hace.

**En sencillo.** Un proyecto de IA no termina cuando el modelo funciona: otra persona tiene que poder **entenderlo, probarlo y repetirlo**. Para eso entregáis dos documentos (la **memoria**, de 10–15 páginas, y la **model card**, la ficha de 2 páginas del modelo) y una pequeña aplicación (el **demostrador**) donde alguien prueba el modelo. Hoy no escribís la versión final: montáis el **esqueleto** de cada pieza, repartís quién escribe qué y rellenáis lo que ya sabéis de los sprints 14 y 15. Es como construir una casa: antes de pintar las paredes, planos y reparto de tareas. No hace falta programar: casi todo es copiar plantillas y escribir; en el demostrador solo ejecutáis y adaptáis un cuaderno que ya está hecho.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Memoria técnica** | El documento PDF de 10–15 páginas que cuenta el proyecto entero. Portada, índice, referencias y anexos no cuentan. |
| **Esqueleto** | La lista de secciones (0 a 9) con lo que debe ir en cada una, antes de escribir. |
| **Requisito R1–R11** | Los 11 mínimos del proyecto. El esqueleto trae un mapa que dice en qué sección se demuestra cada uno. |
| **Model card** | Ficha de máximo 2 páginas del modelo: para qué sirve, con qué datos, cuánto vale y cuándo no usarlo. Es `docs/model_card.md`. |
| **Demostrador** | App o cuaderno donde alguien prueba el modelo sin saber programar. No reentrena: carga un modelo ya entrenado. |
| **`metadatos.json` del demostrador** | La ficha del modelo en formato que lee el programa: campos, rangos válidos, AUC y limitaciones. **No es el mismo fichero** que el `metadatos.json` del Sprint 15. |
| **Tablero** | El Trello del equipo: *Por hacer → En curso → En revisión → Hecho*. Si no está en el tablero, para el equipo no existe. |

**Cómo se hace**

1. **Repartir las secciones (10 minutos).** Con el [esqueleto de la memoria](../1_Trabajar/plantillas/plantilla_esqueleto_memoria_tecnica.md) delante, cada sección tiene **una persona responsable** (la escribe con **vuestros** resultados) y otra que la revisa. Un reparto posible para 4 personas (con 3, una coge dos bloques):

    | Persona | Secciones | De dónde sale el material |
    |---|---|---|
    | A | 1 Problema · 2 Datos y EDA | `sprint-14/ficha_proyecto.md`, `plan_datos_licencias.md`, `01_eda.ipynb` |
    | B | 3 Metodología · 4 Modelado y experimentos | `sprint-15/registro.csv`, `03_modelos.ipynb`, `justificacion_candidato.md` |
    | C | 5 Evaluación · 6 IA responsable | `04_evaluacion.ipynb` (pasos 1 y 3), `riesgos_eticos.md` |
    | D | 7 Demostrador · 8 Gestión del proyecto | la carpeta `demostrador/`, el tablero, `backlog_y_sprints.md` |

    La sección 9 la escribe el equipo entero y la **0 (resumen ejecutivo) se escribe la última**. Cread en el tablero una tarjeta por sección con su responsable.

2. **Crear la memoria (15 minutos).** En un documento compartido, del programa con el que luego exportaréis el PDF, pegad los títulos de las secciones 0 a 9 del esqueleto. Debajo de cada título, copiad sus viñetas como lista de cosas que hay que contar. Fijaos en el presupuesto de páginas (resumen 1 · problema 1 · datos 2 · metodología 1 · modelado 2 · evaluación 2 · IA responsable 2 · demostrador 1 · gestión 0,5 · conclusiones 1 = 13,5, sobre un máximo de 15). Las secciones 1 a 4 **se cuentan, no se inventan**: salen de los ficheros de la tabla de arriba.
3. **Crear la model card (10 minutos).** Abrid la [plantilla](../1_Trabajar/plantillas/plantilla_model_card.md) en GitHub, pulsad **Raw**, `Ctrl + A` y `Ctrl + C`. En el repositorio del equipo: **Add file → Create new file**, escribid el nombre `sprint-16/docs/model_card.md` (cada barra crea una carpeta), pegad con `Ctrl + V` y pulsad **Commit changes**. Después, en cada apartado del 1 al 5, rellenad así (ejemplo con TurisData):

    | Apartado | Qué se escribe | Ejemplo |
    |---|---|---|
    | 1 · Detalles | Nombre y versión, equipo, fecha y enlace al repositorio, tipo de modelo con la versión de la librería (está en `versiones` del `metadatos.json`), hiperparámetros, semilla, licencia | «Riesgo de cancelación de reservas · TurisData (datos sintéticos) · v1.0». «Regresión logística en scikit-learn 1.9.1». Semilla 42 |
    | 2 · Uso previsto | Uso principal, quién lo usa, **qué decisión sigue siendo humana** y qué usos no se permiten | «Orientar la gestión de disponibilidad. Una persona decide si pide depósito. No usar para decidir sobre personas concretas» |
    | 3 · Datos | La tabla de fuente, tamaño y partición, los sesgos de muestreo y si hay datos personales | «`reservas_turisdata.csv`, 6000 reservas sintéticas; 75 % entrenamiento y 25 % test, estratificado, `random_state=42`. Datos personales: no» |
    | 4 · Factores relevantes | Qué grupos o condiciones cambian el rendimiento | «Canal de reserva (en `directo` se detecta menos), reservas sin país y reservas de última hora» |
    | 5 · Métricas | Baseline frente al modelo, una métrica técnica y otra de negocio, y la incertidumbre | «AUC: baseline 0,50 → modelo 0,744 (intervalo 95 %: 0,719–0,767). Recall 0,828 con umbral 0,35» |

    Lo que aún no sepáis (apartados 6 a 9), dejadlo en blanco: se cierra el día 2. **No escribáis cifras que no estén en vuestro cuaderno.**

4. **Dejar el demostrador funcionando (35 minutos).** Lo hace la persona D con otra de apoyo. Primero **ejecutad el cuaderno [`S16_01`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S16/2_Practica/S16_01_demostrador.ipynb) tal cual** (hasta la línea «🏠 A partir de aquí, en casa»). Con TurisData crea la carpeta `demostrador/` con `modelo/`, `logica.py` y `app.py`; `api.py` solo hace falta si vuestro proyecto lo necesita (sección 6 del cuaderno, en casa). Luego sustituid los datos y el modelo por los vuestros en la celda de la sección 1 (las líneas con `# >>> EDITA`):

    ```python
    reservas = pd.read_csv(dato("reservas_turisdata.csv"))    # >>> EDITA: vuestros datos
    NUMERICAS = ["antelacion_dias", "noches", "adultos", "ninos", "precio_noche", "cliente_repetidor", "cancelaciones_previas"]   # >>> EDITA
    CATEGORICAS = ["tipo_habitacion", "canal", "tarifa", "deposito"]    # >>> EDITA
    X, y = reservas[NUMERICAS + CATEGORICAS], reservas["cancelada"]     # >>> EDITA: "cancelada" es lo que se predice
    ```

    Qué hace cada línea:

    - `NUMERICAS` y `CATEGORICAS` son las columnas con las que se entrenó el modelo, divididas en números y en categorías. **Tienen que ser todas las del candidato, con sus nombres exactos**: `logica.py` pide al usuario justo esas.
    - En la celda de abajo (`meta = {…}`) cambiad `nombre`, la regla `min`/`max` y la `etiqueta` de cada campo, y el texto de `limitaciones` (cuándo no fiarse). Si vuestro candidato es un `Pipeline` de scikit-learn ya guardado, copiadlo con `joblib.dump(modelo, "demostrador/modelo/modelo_cancelaciones.joblib")` en vez de reentrenar.
    - Para imágenes, series o un asistente, mirad el apartado «Qué adaptar en vuestro proyecto» del [`README_demostrador.md`](../1_Trabajar/plantillas/demostrador/) y preguntad al docente.

    La carpeta de plantilla completa está en [`demostrador/`](../1_Trabajar/plantillas/demostrador/): copiadla a `sprint-16/demostrador/` de vuestro repositorio (en el repositorio del curso, *Code → Download ZIP*) y trabajad en la copia. La carpeta `modelo/` no viene hecha: la crea el cuaderno.

5. **Apuntar lo que falta (15 minutos).** Una tarjeta del tablero por cada pieza pendiente, con responsable y día: validaciones y aviso del demostrador (día 2), pruebas con `pytest` (día 2), apartados 6 a 9 de la model card (día 2), borrador de las secciones 1 a 6 de la memoria (**antes del 9/12**, durante los dos días sin clase), vídeo plan B (día 3). Cada persona escribe en el tablero qué avanza en esos dos días.

**Qué deberíais ver.**
- **En el cuaderno `S16_01`:** `AUC en test: 0.746` y `Guardado: ['modelo_cancelaciones.joblib', 'metadatos.json']` (el orden de la lista puede variar). La predicción del ejemplo, `{'errores': [], 'probabilidad': 0.812, 'nivel': 'alto', 'tasa_base': 0.459, 'aviso': '…'}`, y la del ejemplo mal escrito, `{'errores': ["'noches' debe estar entre 1 y 30 (has escrito -3).", "'telepatia' no es un valor válido para 'canal'. Opciones: agencia, directo, empresa, web_intermediaria."]}`.
- **En el repositorio:** `sprint-16/docs/model_card.md` con los apartados 1 a 5 rellenos y el 6 al 9 en blanco; en el documento de la memoria, los 10 títulos con una persona responsable; en el tablero, una tarjeta por sección y por pieza pendiente.

**Hecho cuando:** existe el esqueleto de la memoria con una persona responsable por sección, la model card está empezada y el demostrador básico funciona con vuestro modelo.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `FileNotFoundError: Falta el modelo. Ejecuta primero el notebook S16_01 (o tu script de entrenamiento) para crear la carpeta 'modelo/'.` | `logica.py` no encuentra `demostrador/modelo/`. | Ejecutad la celda de la sección 1 de `S16_01`, que guarda el modelo y `metadatos.json`. |
| `NameError: name 'dato' is not defined` | No se ejecutó la primera celda de código («Preparación»). | Pulsad ▶ por orden desde el principio. |
| `KeyError: 'cancelada'` (con vuestro nombre de columna) | La columna que se predice no se llama así en vuestros datos. | Mirad los nombres con `reservas.columns`. |
| `ModuleNotFoundError: No module named 'logica'` | La celda que crea `logica.py` no se ha ejecutado. | Ejecutad la celda de la sección 2 antes de usar `logica`. |
| `ValueError: columns are missing: {'canal'}` | `meta["campos"]` no incluye una columna con la que se entrenó el modelo. | Añadidla a `NUMERICAS` o `CATEGORICAS` y volved a ejecutar las celdas de la sección 1. |
| El archivo de la model card aparece en la raíz del repositorio | Se creó sin la ruta `sprint-16/docs/`. | Abridlo, pulsad el lápiz ✏️ y escribid la ruta completa delante del nombre: `sprint-16/docs/model_card.md`. |

<!--nav-->
---

[← Paso 1](Reto_Sprint_16_paso_1.md) · [Ficha del reto](Reto_Sprint_16.md) · [Paso 3 →](Reto_Sprint_16_paso_3.md)
<!--/nav-->
