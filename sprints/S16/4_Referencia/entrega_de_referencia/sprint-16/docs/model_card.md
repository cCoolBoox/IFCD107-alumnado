# Model card · BiciPrevisión v1.0

> Etiqueta nutricional del modelo: para qué sirve, con qué datos, cuánto vale y **cuándo no usarlo**. Coincide con la memoria y con el aviso del demostrador.

## 1. Detalles del modelo
| Campo | Contenido |
|---|---|
| Nombre, versión y equipo | BiciPrevisión · `HGB_prof6` · v1.0 · Las Palmeras IA (Marta, Personas B, C y D) |
| Entrenamiento y repositorio | 03/12/2026 · repositorio privado del equipo, etiqueta `v1.0-entrega` |
| Tipo, librería e hiperparámetros | Boosting de árboles (`HistGradientBoostingRegressor`), scikit-learn 1.9.1, Python 3.13.18 · `max_iter=300`, `learning_rate=0.05`, `max_depth=6` |
| Semilla y reproducción | `SEMILLA = 42` · pasos en el README · huella de los datos `95d6bcad` |
| Licencia | Código MIT · datos CC BY 4.0 (Fanaee-T y Gama, 2013; UCI) |

## 2. Uso previsto
- **Uso principal:** prever las bicis alquiladas en **cada hora de mañana** con lo que se sabe a las 23:00 de hoy. **Usuarios:** responsable de operaciones de un sistema de bicis compartidas.
- **Decisión que apoya:** cuántas bicis recolocar en cada franja. **La decisión sigue siendo humana:** el modelo propone, el operador decide.
- **Usos no permitidos:** decidir sobre personas (contratar, despedir, evaluar a quien redistribuye); recortar servicio o personal **sin revisión humana**; usarlo en otra ciudad sin reentrenar o en días extremos (huracán, nevada); presentarlo como previsión exacta.

## 3. Datos
| | Entrenamiento | Validación | Test |
|---|---|---|---|
| Fuente y licencia | UCI Bike Sharing (`hour.csv`), CC BY 4.0 | la misma | la misma |
| Periodo / tamaño | 01/01/2011–31/08/2012 | sep–oct 2012 | nov–dic 2012 · 1.464 horas (61 días) |
| Cómo se partió | **Por fechas**, sin barajar; el test se evaluó **una sola vez** | | |

- **Sesgos y lo que falta:** una ciudad, un operador y 2 años; solo 3 horas con tormenta; pocos festivos; la demanda crece un 64 % de 2011 a 2012. El modelo final se entrenó con entrenamiento y validación (hasta el 31/10/2012).
- **Datos personales:** **no** (alquileres agregados por hora). Se excluyen `casual` y `registered` porque suman el objetivo (fuga).

## 4. Factores relevantes
Franja (hora punta, resto del día laborable, fin de semana y festivos), **cercanía a un festivo** (el día, su víspera o el siguiente) y **tipo de tiempo**. En producción el clima será una **previsión**, no el real del histórico.

## 5. Métricas (test, nov–dic 2012)
| Métrica | Baseline (misma hora de la semana pasada) | Modelo | Comentario |
|---|---|---|---|
| **MAE** (bicis por hora) | 75,4 | **44,0** | 42 % menos error; cumple el umbral pactado (bajar ≥ 25 %) |
| WAPE | 39,9 % | 23,3 % | error relativo a lo alquilado |
| MAE en hora punta (laborable, 7–9 h y 17–19 h) | 140,6 | 85,5 | mejora 39 %, pero sigue siendo el punto débil |

**Incertidumbre:** intervalo del 95 % por remuestreo de días (2.000 repeticiones): modelo **39,4–49,2**, baseline 62,6–87,6, mejora relativa **31 %–50 %**. En validación cruzada de 5 bloques: 40,6 ± 6,8. Equivale a unas **753 bicis menos mal planificadas al día**.

## 6. Rendimiento por subgrupos
| Subgrupo | Horas | MAE | Dif. con el global | ¿Es aceptable? |
|---|---|---|---|---|
| Laborable, hora punta | 240 | 85,5 | +41,5 | **No del todo**: el error absoluto es el mayor; el relativo (21 %) es normal |
| Laborable, resto del día | 720 | 27,8 | −16,2 | Sí |
| Fin de semana y festivos | 504 | 47,4 | +3,4 | Sí, con más incertidumbre |
| Cerca de festivo | 240 | 69,2 | +25,2 | **No**: error relativo muy alto y sobreprevé |
| Lluvia o nieve | 97 | 47,8 | +3,8 | Con cuidado: pocas horas (97) y error relativo alto |

Sesgo: se queda corto en hora punta (20,6 bicis por hora) y **sobreprevé** cerca de festivos (29,9). **Mitigación medida:** reponderar la hora punta y añadir una variable de festivo no cumplieron la regla de adopción (validación cruzada). Se adoptó un **rango por franja y cercanía a festivo**; cobertura (se buscaba el 80 %): global 77 % → 79 %, hora punta 46 % → 78 %, cerca de festivo 62 % → 64 %.

## 7. Análisis ético y de riesgos
- **Clasificación:** AI Act, riesgo **mínimo** (predice demanda agregada); RGPD: **sin datos personales**, sin EIPD.
- **Riesgos y mitigaciones** (`docs/riesgos_eticos.md`): clima real como previsión (con un 10 % de error, MAE 46,4); fuga de `registered` (excluida); uso sin supervisión (aviso y alerta); festivos y hora punta (**abiertos**).
- **Supervisión humana:** el operador decide; la alerta marca 10 días del test (7 de los 10 peores). **Transparencia:** cada respuesta dice que es una estimación, su error medio y sus límites.

## 8. Limitaciones y recomendaciones
- **No fiarse** en: días cercanos a festivos, lluvia o nieve (solo 97 horas), sucesos extremos (en Sandy previó 2.520 y hubo 22 alquileres), otras ciudades u otros años.
- **Recomendaciones:** usar la previsión como punto de partida revisado por una persona (hora punta y festivos) y alimentarla con una **previsión meteorológica real**.
- **Antes de un despliegue real:** más años de datos, monitorización semanal del error, reevaluación del rango y auditoría de uso.

## 9. Contacto y mantenimiento
Responsable: Persona D (Las Palmeras IA) · Se reevalúa **cada trimestre**, o antes si el error semanal supera los 66 bicis por hora.
