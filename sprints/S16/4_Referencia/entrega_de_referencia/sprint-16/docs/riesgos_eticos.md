# Plan ético y registro de riesgos

**Proyecto:** BiciPrevisión · **Responsable de IA responsable:** Persona D · **Versión vigente:** S16 (cerrada)

> Actualiza el checklist del Sprint 1 para el proyecto final (R6). Se rellenó en S14, se revisó en S15 y se **cierra aquí, en S16**, con evidencias.

## Parte A · Checklist ético (versión proyecto final)
Estado: **✔** cumplido con evidencia · **◐** parcial · **✘** no cumplido · **n/a** no aplica.

### A1. Propósito y proporcionalidad
| Pregunta | S1 | S14 | S15 | S16 | Evidencia |
|---|---|---|---|---|---|
| ¿Qué problema resolvemos y para quién? ¿Basta una regla simple? | — | ◐ Hay una regla simple (la semana pasada) y se mide si la IA la supera un 25 % | ✔ El candidato supera al *baseline* un 39 % en validación | ✔ En el test, 42 % menos error (75,4 → 44,0) | `04_evaluacion.ipynb`, memoria §5 |
| ¿Qué pasa si el modelo falla? ¿Quién sale perjudicado? | — | ◐ Faltarían o sobrarían bicis en una franja; el operador pierde servicio y los usuarios, bicis | ◐ Se mide el error por franja: en hora punta falla más | ✔ Falla más en hora punta (85,5) y cerca de festivos (69,2); lo dicen el aviso y la *model card* | Model card §6 y §8 |
| ¿Usos indebidos previsibles? ¿Qué **no** debe hacerse? | — | ◐ No usar la previsión para recortar servicio sin revisión humana | ◐ Pendiente de la *model card* | ✔ La *model card* (§2) lista los usos no permitidos | Model card §2 |

### A2. Datos y privacidad (RGPD / LOPDGDD)
| Pregunta | S1 | S14 | S15 | S16 | Evidencia |
|---|---|---|---|---|---|
| ¿Hay **datos personales**? ¿Podemos evitarlos? | — | ✔ No: alquileres agregados por hora, sin usuarios ni trayectos | ✔ Sin cambios | ✔ Sin cambios; el demostrador no guarda nada | Plan de datos, `app.py` |
| ¿Base legal y finalidad claras? | — | n/a no hay datos personales | n/a | n/a |  |
| ¿Datos sensibles (salud, biometría, menores, origen…)? | — | ✔ No | ✔ Sin cambios | ✔ Sin cambios | Plan de datos (6) |
| ¿Se pueden reidentificar personas? | — | ✔ No: no hay estaciones ni trayectos | ✔ Sin cambios | ✔ Sin cambios | EDA |
| ¿Licencia compatible y fuente citada? | — | ✔ CC BY 4.0; cita pegada en el plan | ✔ Sin cambios | ✔ CC BY 4.0 citada en README y memoria | README, memoria (referencias) |
| ¿Se guardan datos de usuarios en el demostrador? | — | ◐ Previsto: no se guarda nada | ◐ Previsto: no se guarda nada | ✔ Comprobado: `app.py` no escribe en disco ni usa claves | `demostrador/app.py` |

### A3. Sesgo y equidad
| Pregunta | S1 | S14 | S15 | S16 | Evidencia |
|---|---|---|---|---|---|
| ¿Quién falta o está infrarrepresentado (sesgo de muestreo)? | — | ✔ Una ciudad y un operador; 3 horas de tormenta | ✔ Sin cambios | ✔ Declarado en la *model card* (§3 y §4): una ciudad, 2 años, 3 horas de tormenta, pocos festivos | Model card §3–4 |
| ¿Variables proxy de atributos protegidos? | — | ✔ No hay variables de personas ni de barrios | ✔ Sin cambios | ✔ Sin cambios | Plan de datos (2) |
| ¿Rendimiento **por subgrupos** (franja horaria, día, clima)? | — | ◐ Previsto en S16; en el EDA ya se ve por hora y por clima | ◐ Por franja horaria en la justificación | ✔ 8 subgrupos con n, MAE y sesgo; brecha en hora punta y cerca de festivo | `04_evaluacion.ipynb` §4, model card §6 |
| ¿Mitigación aplicada y evaluada? | — | ◐ Previsto en S16 (H8) | ◐ Previsto | ✔ Tres probadas con validación cruzada; una adoptada (intervalos por franja) y medida antes y después | `04_evaluacion.ipynb` §6, memoria §6 |

### A4. Transparencia y explicabilidad
| Pregunta | S1 | S14 | S15 | S16 | Evidencia |
|---|---|---|---|---|---|
| ¿El usuario sabe que interactúa con IA? | — | ◐ Previsto en el demostrador | ◐ Previsto | ✔ El demostrador lo dice arriba y en cada respuesta | `app.py`, `logica.py` |
| ¿Se explica qué variables pesan? | — | ◐ Previsto: importancia por permutación en S15 | ✔ Importancia por permutación | ✔ Resumida en la memoria con su límite (no es causa) | `explicacion_modelo.png` (S15) |
| ¿Se muestra la **incertidumbre**? | — | ◐ Previsto: rango y aviso en el demostrador | ◐ Previsto | ✔ Rango por franja (cobertura 79 % frente al 80 % buscado); es peor en hora punta y cerca de festivo | `logica.py`, fig. 4 de la memoria |
| ¿Existe *model card*? | — | ◐ Se escribe en S16 | ◐ Se escribe en S16 | ✔ `docs/model_card.md`, 2 páginas | Model card |

### A5. Supervisión humana y robustez
| Pregunta | S1 | S14 | S15 | S16 | Evidencia |
|---|---|---|---|---|---|
| ¿Una persona revisa las decisiones importantes? | — | ◐ Previsto: el operador decide; el modelo solo propone | ◐ Previsto | ✔ Aviso en cada respuesta y alerta «cerca de festivo» (marca 10 días del test, 7 de los 10 peores) | Model card §7 |
| ¿Qué ocurre con eventos atípicos? | — | ◐ Sandy (29/10/2012) tuvo 22 alquileres; se mirará aparte | ◐ Sandy sin medir | ✔ Sandy: real 22, previsto 2.520; el modelo no puede anticipar un huracán; avisa si el tiempo es 3 o 4 | `04_evaluacion.ipynb` §7, R-03 |
| ¿Se ha probado con datos distintos a los de entrenamiento? | — | ◐ Test por fechas posteriores (S16) | ◐ Test por fechas posteriores | ✔ Test nov–dic 2012 (posterior) y clima con un 10 % de error: 46,4 | `04_evaluacion.ipynb` §7 |
| ¿Riesgo de sobreconfianza? ¿Cómo se avisa? | — | ◐ Aviso de incertidumbre previsto | ◐ Aviso previsto | ◐ Aviso hecho y revisado por otra persona; un aviso no garantiza que se lea (residual) | R-05 |

### A6. Impacto y sostenibilidad
| Pregunta | S1 | S14 | S15 | S16 | Evidencia |
|---|---|---|---|---|---|
| ¿Impacto social, laboral o ambiental? | — | ◐ Mejor reparto de bicis; riesgo de usarlo para recortar personal | ◐ Sin cambios | ✔ Uso permitido: apoyar la recolocación; no permitido: recortar personal sin revisión | Model card §2 |
| ¿Se elige el modelo más simple que cumple el objetivo? | — | ◐ Se comparará con el *baseline* y la regresión lineal | ✔ Se prefirió boosting de profundidad 6 y se descartó la red | ✔ Sin cambios; el modelo pesa 1.023 KB | `registro.csv` |

## Parte B · Clasificación normativa (justificada)
| Cuestión | Respuesta y justificación |
|---|---|
| ¿Trata datos personales? ¿De qué tipo? | **No.** El CSV tiene alquileres agregados por hora, calendario y clima: no hay personas, estaciones ni trayectos, y no se pueden reidentificar. El demostrador no guarda lo que escribe la persona usuaria |
| Base legal / finalidad (RGPD) | No aplica: sin datos personales no hay tratamiento al que dar base legal |
| ¿Necesitaría una evaluación de impacto (EIPD)? | No: no hay datos personales ni decisiones automatizadas sobre personas |
| **Nivel de riesgo AI Act** | **Mínimo.** Predice demanda agregada y apoya una decisión de operaciones. No aparece en los ámbitos de alto riesgo del Anexo III (empleo, crédito, educación, justicia…) y no es un componente de seguridad de una infraestructura crítica. *(Es nuestra lectura del reglamento; ante un despliegue real la revisaría una persona del área jurídica.)* |
| Obligaciones que se derivan | Buenas prácticas, no obligaciones: *model card*, aviso de incertidumbre, supervisión humana y registro de riesgos |
| ¿Apoya **decisiones sobre personas**? | No. **Cuidado con un uso futuro:** si el modelo sirviera para decidir cuántas personas de redistribución contratar o despedir, el análisis habría que rehacerlo (R-05) |
| **Supervisión humana** | El operador decide cuántas bicis recolocar; el modelo solo propone. El demostrador lo dice en cada respuesta y marca los días que piden revisión |
| **Transparencia** | El demostrador dice que es una estimación, con qué error medio se equivocó en otro periodo, qué cubre su rango y qué límites tiene; la *model card* y la memoria dicen lo mismo con las mismas cifras |

## Parte C · Registro de riesgos (cerrado)
**P** y **I** de 1 a 3. **Nivel = P × I:** 1-2 bajo · 3-4 medio · 6-9 alto. **Estado final:** mitigado · aceptado (residual explicado) · abierto con acción para antes de un despliegue.

| ID | Riesgo (qué puede ir mal y a quién afecta) | Tipo | P | I | Nivel | Medida de mitigación | Responsable | Estado final | **Evidencia: cómo se evaluó la mitigación** |
|---|---|---|---|---|---|---|---|---|---|
| R-01 | Se usa el clima **real** como si fuera una previsión: en producción el clima será peor y el error, mayor | datos | 2 | 3 | 6 | Modelo con y sin clima (S15); prueba con un 10 % de error en el clima (S16); el demostrador deja elegir el tiempo previsto | Persona C | **mitigado, residual aceptado** | Con un 10 % de error en el clima el MAE en test pasa de 44,0 a **46,4** (5,4 % más): sigue por debajo del umbral. Sin clima no se cumple el umbral (S15), así que el clima es imprescindible y **debe venir de una previsión real** |
| R-02 | Variables de fuga (`casual`, `registered`) inflan el resultado | datos | 2 | 3 | 6 | Excluirlas y comprobar que el MAE no baja de forma absurda | Persona B | **mitigado** | EDA: `cnt = casual + registered` en el 100 % de las filas. La prueba provocada en S15 con `registered` dio un MAE de 17,0: un error así de bajo es la señal de alarma. Ninguna de las 14 variables del modelo contiene `cnt` de mañana |
| R-03 | El huracán Sandy (29/10/2012) distorsiona la evaluación | datos | 2 | 2 | 4 | Mirarlo aparte; avisar si el tiempo previsto es 3 o 4 | Persona D | **aceptado** | Ese día hubo 22 alquileres y el modelo (entrenado solo con el entrenamiento) previó **2.520**: no puede anticipar un huracán. Efecto en la validación: MAE 42,2 con ese día y 41,1 sin él. El test (nov–dic) no tiene ningún suceso así |
| R-04 | La demanda crece un 64 % de 2011 a 2012: un modelo con el año no extrapola | modelo | 3 | 2 | 6 | Partición temporal y retrasos en vez del año | Persona B | **mitigado** | Validación y test son posteriores al entrenamiento (aserción en `02_baseline.ipynb`). En el test el modelo se queda corto 5,3 bicis por hora de media (sesgo pequeño) |
| R-05 | Se usa la previsión para recortar servicio o personal sin revisión humana, o se confía demasiado en ella | uso | 2 | 3 | 6 | Aviso de incertidumbre en cada respuesta, alerta «cerca de festivo», *model card* con usos no permitidos y decisión del operador | Persona D | **mitigado, residual aceptado** | Aviso revisado por otra persona en la *review*. La alerta marca 10 días del test y acierta 7 de los 10 peores, con 3 falsas alarmas. Residual: un aviso no garantiza que se lea |
| R-06 | Una sola ciudad y un solo operador: el modelo no sirve en otra ciudad | datos | 3 | 2 | 6 | Declarar el alcance en README, demostrador y *model card* | Persona C | **aceptado** | La frase de alcance aparece en las tres; no se ha probado en otra ciudad. Habría que reentrenar con sus datos |
| R-07 | Las 165 horas sin fila se imputan a 0 y subestiman la demanda | datos | 1 | 1 | 1 | Marcarlas con `hueco` y mirar el error sin ellas | Persona C | **aceptado** | Solo 4 horas del test son huecos: MAE 44,1 sin ellas frente a 44,0 con ellas |
| R-08 *(nuevo en S16)* | El error se dispara cerca de festivos (el modelo vio pocos): MAE 69,2, error relativo 49 %, y **sobreprevé** 29,9 bicis por hora | datos | 3 | 2 | 6 | Se probaron dos medidas con validación cruzada (variable «cerca de festivo» y reponderar): ninguna cumplió la regla de adopción. Se adopta un **rango más ancho** en esos días y una **alerta** en el demostrador | Persona D | **mitigado a medias; abierto para despliegue** | Con la variable «cerca de festivo» el error en esos días baja un 0,8 % en validación cruzada y sube un 0,4 % el global: no se adopta. El rango cubre el 64 % de esas horas (antes, 62 %), aún lejos del 80 %. **Acción previa a un despliegue:** más años de datos con festivos |
| R-09 *(nuevo en S16)* | La **hora punta** es donde más cuesta equivocarse y donde el error absoluto es mayor (85,5 frente a 44,0 global) | modelo | 2 | 3 | 6 | Reponderar la hora punta ×2 y ×3 (no adoptado) e intervalos propios para esa franja (adoptado) | Persona D | **mitigado a medias** | Reponderar baja el error de la hora punta un 2,0 % en validación cruzada pero sube el global un 2,2 % (regla: baja ≥ 5 % y global ≤ +1 %): no se adopta. Con intervalos por franja la cobertura de la hora punta pasa del 46 % al 78 %. **El error de la previsión central no ha mejorado** |

## Parte D · Cierre (Sprint 16)
- **Riesgos altos mitigados y con qué evidencia:** R-01 (clima con error: 46,4 frente a 44,0), R-02 (fuga: `registered` excluida y prueba provocada), R-04 (tendencia: partición temporal y sesgo de 5,3 bicis) y R-05 (aviso y alerta revisados).
- **Riesgos residuales que aceptamos y por qué:** R-03 (un huracán no se anticipa; se avisa con el tiempo previsto), R-06 (una sola ciudad; alcance declarado) y R-07 (efecto despreciable).
- **Riesgos que quedan abiertos para un despliegue real:** R-08 (festivos) y R-09 (hora punta): hay que reunir más años de datos y reevaluar. Hasta entonces, **una persona revisa** la previsión de esos días y franjas.
- **Una mitigación que no funcionó (y qué decidimos):** reponderar la hora punta bajó el error de esa franja un 2,0 % pero empeoró el conjunto un 2,2 % en validación cruzada. Aplicamos la regla escrita antes (adoptar solo si el grupo baja ≥ 5 % y el global sube ≤ 1 %) y la descartamos; en el test solo se midió el antes y el después (85,5 → 83,4 en hora punta; global 44,0 → 44,1).
- **Limitaciones y usos no permitidos:** pasan a la *model card* (§2 y §8).
