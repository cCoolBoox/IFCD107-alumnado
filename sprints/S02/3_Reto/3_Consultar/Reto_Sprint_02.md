# Sprint 2 · Reto «¿Nos fiamos de este informe?»

> **Ficha completa del reto, para consultar.** Para trabajar, [el reto en una página](../1_Trabajar/Reto_Sprint_02_una_pagina.md). Qué se sube y cómo se evalúa: [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md).
>
> - Volver al [README del sprint](../../README.md).
> - Si es vuestro primer reto: [Cómo se trabaja un reto](../../../../material/4.%20Como_se_trabaja_un_reto.md).

## Ficha del reto

### 1 · 🎯 Qué os pide el cliente

**Qué os pide el cliente.** La dirección de TurisData ha escrito un borrador de informe con **seis afirmaciones** sobre cancelaciones y lo va a presentar al consejo. Os pide que lo reviséis como una persona auditora (revisar el trabajo de otra persona y dar vuestra opinión razonada en un **dictamen**): *«Decidme si nos podemos fiar de cada frase; y si no, cómo debería decirse»*. La afirmación 2 decide a qué canal de venta dar prioridad.

**Cómo se trabaja.** **No se programa:** basta una calculadora o una hoja de cálculo, y no partís de una hoja en blanco. Tenéis las **cartas de error** (los fallos típicos al leer números, cada uno con la pregunta que lo destapa), la **afirmación 1 ya resuelta** como modelo, las **fórmulas de la hoja con pistas y cifras para comprobar** y la **plantilla del dictamen** con huecos. El equipo hace junto las afirmaciones 1 y 2, y cada persona audita una de la 3 a la 6. En clase tenéis **dos jornadas**: el día 1, planning, cartas, afirmación 2 y la vuestra; el día 2, dictamen, revisión cruzada y entrega. El equipo decide hasta dónde llega: 🟢 mínimo (la 1, la 2 y dos más), 🟡 estándar o 🔴 extra (las seis y la hoja de cálculo adjunta). **Qué aprendéis:** a no creeros una estadística solo porque salga en un informe, porque un modelo entrenado con datos mal interpretados aprende mal.

---

### 2 · 🧰 Recursos del reto

| Recurso | Para qué lo usaréis | Dónde está |
|---|---|---|
| **El informe del cliente**: [`informe_cliente.md`](../1_Trabajar/plantillas/informe_cliente.md) e [`informe_cliente.csv`](../1_Trabajar/plantillas/informe_cliente.csv) | Las seis afirmaciones que auditáis y los datos (2.400 reservas por tarifa y canal) | Paso 1: se lee en voz alta y los datos se copian a una hoja de cálculo |
| **Plantilla del dictamen** [`plantilla_dictamen.md`](../1_Trabajar/plantillas/plantilla_dictamen.md) | El documento que entregáis, con huecos y la afirmación 1 ya resuelta | Copiadla como `sprint-02/dictamen.md` (paso 1) |
| **Cartas de error** y la **afirmación 1 resuelta** | Reconocer el fallo de cada frase y ver cómo queda un bloque del dictamen | [Paso 2](Reto_Sprint_02_paso_2.md) |
| **Presentaciones** [S02_01](../../1_Teoria/S02_01_presentacion_Herramientas_y_matematicas_para_IA.pdf) y [S02_02](../../1_Teoria/S02_02_presentacion_Estadistica_y_probabilidad.pdf) y sus [apuntes](../../1_Teoria/apuntes/apuntes_matematicas_y_estadistica.md) | La estadística que necesitáis: tasas, muestras, sesgo, correlación y paradoja de Simpson | El docente las explica en clase |
| **Hoja de cálculo** (Google Sheets, Excel o LibreOffice) | Calcular las tasas de la afirmación 2 | Con vuestra cuenta de Google ya tenéis Google Sheets |
| **Hojas de práctica** [hoja 1](../../2_Practica/ejercicios_algebra_calculo.md) y [hoja 2](../../2_Practica/ejercicios_estadistica.md), y [estadísticas engañosas](../../2_Practica/estadisticas_enganosas.md) | Los ejercicios del mínimo básico (M1, M2, M7, E1, E2, E6, E8 y E10) van a `ejercicios.md`; los casos engañosos entrenan el ojo para las cartas | Se hacen en las clases del sprint. Soluciones, para comprobar después de intentarlo: [hoja 1](../../2_Practica/soluciones_algebra_calculo.md) y [hoja 2](../../2_Practica/soluciones_estadistica.md) |
| **Alta en Colab** [`alta_cuentas.md`](../../2_Practica/alta_cuentas.md) | Tener Colab operativo (el Sprint 3 lo usa) | Día 1, a primera hora |
| **Entrega y rúbrica** [`entrega_y_rubrica.md`](../2_Entregar/entrega_y_rubrica.md) | Qué se sube y cómo se puntúa (cuatro criterios, de 1 a 4); sirve para revisar vuestro dictamen antes de entregarlo | Leedla una vez antes de entregar |
| **Autoevaluación y coevaluación** | Cada persona se puntúa y valora el dictamen de otra | [Hoja del sprint](../2_Entregar/autoevaluacion_y_coevaluacion.md) (paso 5) |
| **Cómo entregar en GitHub** | Subir los ficheros a `sprint-02/` | [Guía de entrega](../../../../material/5.%20Como_entregar_en_GitHub.md) |
| **Tablero del equipo** (Trello o similar) | Una tarjeta por afirmación, con su responsable, y moverlas a *Hecho* | El del equipo. Si no existe, es lo primero que se crea |
| **Un asistente de IA** (opcional) | Entender conceptos y redactar | Con las reglas de la «Ayuda 1» |

---

### 3 · 🪜 Guía paso a paso

Son cinco pasos, de **125 minutos en total** (70 el día 1 y 55 el día 2). Cada uno dice **qué hacéis** (la lista corta), **cómo se hace** con el detalle, **qué deberíais ver** y **cuándo está hecho**. Las ayudas (IA, errores, atascos) están al final. Después del paso 5, el bloque de cierre del día 2 (40 minutos) sirve para terminar la entrega, la autoevaluación, la review y la retro. Si el tiempo aprieta, completad el nivel mínimo y dejad lo demás para casa.

**Cada paso tiene su propia página.** Abrid la que toque y volved aquí cuando acabéis:

- [Paso 1 · Planning (día 1, 10 minutos)](Reto_Sprint_02_paso_1.md)
- [Paso 2 · Las cartas de error y un ejemplo resuelto (día 1, 15 minutos)](Reto_Sprint_02_paso_2.md)
- [Paso 3 · La afirmación 2, paso a paso (día 1, 25 minutos)](Reto_Sprint_02_paso_3.md)
- [Paso 4 · Vuestra afirmación (día 1, 20 minutos)](Reto_Sprint_02_paso_4.md)
- [Paso 5 · Dictamen y entrega (día 2, 55 minutos)](Reto_Sprint_02_paso_5.md)

#### Ayuda 1 · Cómo usar la IA en este reto

La IA sirve para **entender y redactar**, no para calcular: muchas se equivocan en porcentajes y lo hacen con mucha seguridad. Reglas:
- **Si la IA os hace una cuenta, comprobadla a mano** (afirmaciones 2 y 6).
- **Declarad dónde la habéis usado** en el apartado «Uso de IA» del dictamen.
- **Las cifras no cambian:** las del dictamen salen del informe y de vuestras cuentas, no de la IA.
- **Nada de datos personales reales** en una IA ni en el repositorio.

| Para qué | Ejemplo de petición | Qué comprobáis |
|---|---|---|
| Entender un concepto | «Explícame la paradoja de Simpson con un ejemplo de un hotel, sin fórmulas» | Que lo entendéis vosotros y que sabéis aplicarlo a los datos del informe |
| Redactar | «Reescribe esta frase para que la entienda una directora; no cambies las cifras» | Que **las cifras siguen siendo las mismas** y que la frase no afirma más de lo que dicen los datos |
| Revisar | «¿Qué le falta a esta frase corregida para ser honesta?» | Que ninguna cifra nueva ha aparecido; si no hay datos, el veredicto sigue siendo «no se puede saber» |

#### Ayuda 2 · Errores frecuentes (y cómo evitarlos)

| Error | Por qué ocurre | Cómo evitarlos |
|---|---|---|
| Decir solo «está mal» | Parece suficiente | Cada bloque lleva **carta, veredicto y frase corregida** |
| Dar por buena una cuenta sin rehacerla | Las cifras parecen obvias | Rehaced las cifras con los datos, también las que parecen obvias |
| Mirar solo el total | El informe solo da el total | Separad por tarifa y canal; comparad dentro de cada grupo |
| Dividir por el total equivocado | Es lo primero que se ve | La tasa es cancelaciones ÷ reservas **del mismo grupo** |
| Inventar números cuando no hay datos | La frase corregida parece coja sin una cifra | Decid «no se puede saber» y escribid qué datos faltan |
| Escribir todas las personas a la vez en `dictamen.md` | Es más rápido | Borradores en el paso 4 y pegado de una persona en una en el paso 5 |

#### Ayuda 3 · Si os atascáis

1. **No sabéis qué carta es:** contestad con vuestra afirmación la pregunta de cada carta y quedaos con las que respondéis «sí, pasa aquí».
2. **No sabéis qué veredicto poner:** mirad la cuenta y la conclusión por separado; si faltan datos, «no se puede saber» es una respuesta válida.
3. **La frase no os cuadra:** formuladla de otra manera (con números absolutos, con otra base) y mirad si la conclusión cambia.
4. **Los números no cuadran:** revisad que dividís por las reservas **del grupo**, no por el total.
5. Preguntad primero al equipo y, después, al docente. Más ayuda: [Cómo se trabaja un reto](../../../../material/4.%20Como_se_trabaja_un_reto.md).
