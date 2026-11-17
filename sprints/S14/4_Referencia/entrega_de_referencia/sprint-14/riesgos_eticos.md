# Plan ético y registro de riesgos

**Proyecto:** BiciPrevisión · **Responsable de IA responsable:** Persona D · **Versión vigente:** S14 (S15 y S16 pendientes)

> Actualiza el checklist del Sprint 1 para el proyecto final (R6). Se rellena en S14, se revisa en S15 y se cierra en S16 con evidencias.

## Parte A · Checklist ético (versión proyecto final)
Estado: **✔** cumplido con evidencia · **◐** parcial · **✘** no cumplido · **n/a** no aplica.

### A1. Propósito y proporcionalidad
| Pregunta | S1 | S14 | S15 | S16 | Evidencia |
|---|---|---|---|---|---|
| ¿Qué problema resolvemos y para quién? ¿Basta una regla simple? | — | ◐ Hay una regla simple (la semana pasada) y se mide si la IA la supera un 25 % |  |  | Ficha, `02_baseline.ipynb` |
| ¿Qué pasa si el modelo falla? ¿Quién sale perjudicado? | — | ◐ Faltarían o sobrarían bicis en una franja; el operador pierde servicio y los usuarios, bicis |  |  | Ficha (riesgos) |
| ¿Usos indebidos previsibles? ¿Qué **no** debe hacerse? | — | ◐ No usar la previsión para recortar servicio sin revisión humana |  |  | Model card (S16) |

### A2. Datos y privacidad (RGPD / LOPDGDD)
| Pregunta | S1 | S14 | S15 | S16 | Evidencia |
|---|---|---|---|---|---|
| ¿Hay **datos personales**? ¿Podemos evitarlos? | — | ✔ No: alquileres agregados por hora, sin usuarios ni trayectos |  |  | Plan de datos (6) |
| ¿Base legal y finalidad claras? | — | n/a no hay datos personales |  |  |  |
| ¿Datos sensibles (salud, biometría, menores, origen…)? | — | ✔ No |  |  | Plan de datos (6) |
| ¿Se pueden reidentificar personas? | — | ✔ No: no hay estaciones ni trayectos |  |  | EDA |
| ¿Licencia compatible y fuente citada? | — | ✔ CC BY 4.0; cita pegada en el plan |  |  | Plan de datos (1 y 7) |
| ¿Se guardan datos de usuarios en el demostrador? | — | ◐ Previsto: no se guarda nada |  |  | Demostrador (S16) |

### A3. Sesgo y equidad
| Pregunta | S1 | S14 | S15 | S16 | Evidencia |
|---|---|---|---|---|---|
| ¿Quién falta o está infrarrepresentado (sesgo de muestreo)? | — | ✔ Una ciudad y un operador; 3 horas de tormenta |  |  | EDA |
| ¿Variables proxy de atributos protegidos? | — | ✔ No hay variables de personas ni de barrios |  |  | Plan de datos (2) |
| ¿Rendimiento **por subgrupos** (franja horaria, día, clima)? | — | ◐ Previsto en S16; en el EDA ya se ve por hora y por clima |  |  | `01_eda.ipynb` |
| ¿Mitigación aplicada y evaluada? | — | ◐ Previsto en S16 (H8) |  |  | Backlog H8 |

### A4. Transparencia y explicabilidad
| Pregunta | S1 | S14 | S15 | S16 | Evidencia |
|---|---|---|---|---|---|
| ¿El usuario sabe que interactúa con IA? | — | ◐ Previsto en el demostrador |  |  | Demostrador |
| ¿Se explica qué variables pesan? | — | ◐ Previsto: importancia por permutación en S15 |  |  | `explicacion_modelo.png` |
| ¿Se muestra la **incertidumbre**? | — | ◐ Previsto: rango y aviso en el demostrador |  |  | Demostrador |
| ¿Existe *model card*? | — | ◐ Se escribe en S16 |  |  | `model_card.md` |

### A5. Supervisión humana y robustez
| Pregunta | S1 | S14 | S15 | S16 | Evidencia |
|---|---|---|---|---|---|
| ¿Una persona revisa las decisiones importantes? | — | ◐ Previsto: el operador decide; el modelo solo propone |  |  | Model card |
| ¿Qué ocurre con eventos atípicos? | — | ◐ Sandy (29/10/2012) tuvo 22 alquileres; se mirará aparte |  |  | EDA, R-03 |
| ¿Se ha probado con datos distintos a los de entrenamiento? | — | ◐ Test por fechas posteriores (S16) |  |  | Plan de datos (5) |
| ¿Riesgo de sobreconfianza? ¿Cómo se avisa? | — | ◐ Aviso de incertidumbre previsto |  |  | R-05 |

### A6. Impacto y sostenibilidad
| Pregunta | S1 | S14 | S15 | S16 | Evidencia |
|---|---|---|---|---|---|
| ¿Impacto social, laboral o ambiental? | — | ◐ Mejor reparto de bicis; riesgo de usarlo para recortar personal |  |  | R-05 |
| ¿Se elige el modelo más simple que cumple el objetivo? | — | ◐ Se comparará con el *baseline* y la regresión lineal |  |  | `registro.csv` (S15) |

## Parte B · Clasificación normativa preliminar
| Cuestión | Respuesta y justificación |
|---|---|
| ¿Trata datos personales? ¿De qué tipo? | No. Solo alquileres agregados por hora, calendario y clima |
| Base legal / finalidad (si aplica) | No aplica (sin datos personales) |
| ¿Necesitaría una evaluación de impacto (EIPD)? | No: no hay datos personales ni decisiones sobre personas |
| **Nivel de riesgo AI Act** | **Mínimo**: predice demanda agregada y apoya una decisión de operaciones |
| Obligaciones que se derivan | Buenas prácticas: documentar (*model card*), aviso de incertidumbre y supervisión humana |
| ¿Apoya **decisiones sobre personas**? | No |

## Parte C · Registro de riesgos
**P** y **I** de 1 a 3. **Nivel = P × I:** 1-2 bajo · 3-4 medio · 6-9 alto.

| ID | Riesgo (qué puede ir mal y a quién afecta) | Tipo | P | I | Nivel | Medida de mitigación | Responsable | Estado | **Cómo se evaluó la mitigación** |
|---|---|---|---|---|---|---|---|---|---|
| R-01 | Se usa el clima **real** como si fuera una previsión: en producción el clima será peor y el error, mayor | datos | 2 | 3 | 6 | Comparar modelo con y sin clima y probar con ruido en la previsión (H13, H8) | Persona C | abierto | Plan: S15 mide con y sin clima; S16 añade un 10 % de error al clima |
| R-02 | Variables de fuga (`casual`, `registered`) inflan el resultado | datos | 2 | 3 | 6 | Excluirlas de las variables y comprobar que el MAE no baja de forma absurda (H5) | Persona B | mitigado | EDA: `cnt = casual + registered` en el 100 % de las filas; excluidas |
| R-03 | El huracán Sandy (29/10/2012) distorsiona la evaluación | datos | 2 | 2 | 4 | Mirarlo aparte y dar el MAE sin ese día (H8) | Persona D | abierto | EDA: 22 alquileres ese día frente a 5.600 de media |
| R-04 | La demanda crece un 64 % de 2011 a 2012: un modelo con el año no extrapola | modelo | 3 | 2 | 6 | Partición temporal y retrasos en vez del año (H5) | Persona B | mitigado | Aserción en `02_baseline.ipynb`: validación y test posteriores al entrenamiento |
| R-05 | Se usa la previsión para recortar servicio o personal sin revisión humana, o se confía demasiado en ella | uso | 2 | 3 | 6 | Aviso de incertidumbre en el demostrador, la *model card* dice qué no hacer y el operador decide (H9, H10) | Persona D | abierto | Plan: revisar el aviso con otro equipo en S16 |
| R-06 | Una sola ciudad y un solo operador: el modelo no sirve en otra ciudad | datos | 3 | 2 | 6 | Declarar el alcance en el README y la *model card* (H10) | Persona C | abierto | Plan: frase de alcance revisada en la review de S16 |
| R-07 | Las 165 horas sin fila se imputan a 0 y subestiman la demanda | datos | 1 | 1 | 1 | Marcarlas con `hueco` y mirar el error sin ellas | Persona C | aceptado | Son madrugadas (0–5 h): el efecto en el MAE es despreciable |

## Parte D · Cierre (se completa en el Sprint 16)
- ¿Qué riesgos altos quedaron mitigados y con qué evidencia? *(pendiente de S16)*
- ¿Qué riesgos **residuales** aceptamos? *(pendiente de S16)*
- Limitaciones y usos no permitidos: *(pasan a la *model card* en S16)*
