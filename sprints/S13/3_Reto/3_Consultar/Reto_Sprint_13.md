# Sprint 13 · Reto «Informe visual para dirección»

> **Ficha completa del reto, para consultar.** Para trabajar, [el reto en una página](../1_Trabajar/Reto_Sprint_13_una_pagina.md). Qué se sube y cómo se evalúa: [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md).
>
> - Volver al [README del sprint](../../README.md).
> - Si es vuestro primer reto: [Cómo se trabaja un reto](../../../../material/4.%20Como_se_trabaja_un_reto.md).

## Ficha del reto

### 1 · 🎯 Qué os pide el cliente

**Qué os pide el cliente.** Marcos, el director general de TurisData Canarias, tiene **10 minutos** antes de la reunión de ingresos. **No sabe qué es un AUC y no quiere saberlo.** Os pide: *«Una página. ¿Puedo fiarme del modelo, qué mueve las cancelaciones y qué hago el lunes?»* Este reto **no trata de entrenar un modelo mejor**, sino de **comunicar**: muchos proyectos de IA fracasan no porque el modelo sea malo, sino porque nadie con capacidad de decidir entiende lo que dice. Vais a convertir **vuestro mejor modelo del curso** en **una página que se entiende en 30 segundos**: un titular que dice qué hacer, cuatro gráficos honestos, tres viñetas sin jerga y un pie con los límites. Será la **semilla de la memoria técnica** del proyecto final.

**Cómo se trabaja.** No hace falta experiencia previa: os damos un **cuaderno plantilla que ya funciona** (al ejecutarlo de arriba abajo dibuja el panel de cuatro gráficos con un modelo de ejemplo) y un **texto de informe con huecos**. Vuestro trabajo es cambiar lo marcado con `# >>> EDITA`, poner títulos que **digan una conclusión** y escribir el texto. En clase tenéis **25 minutos de reto** en el último día del Sprint 12 (por eso es corto: **llegad con el modelo elegido**), y después la franja de entrega y review. El equipo decide hasta dónde llega: 🟢 mínimo, 🟡 estándar o 🔴 extra.

---

### 2 · 🧰 Recursos del reto

| Recurso | Para qué lo usaréis | Dónde está |
|---|---|---|
| **Un navegador y Google Colab** (Python y las librerías ya vienen instaladas) | Ejecutar el cuaderno plantilla y generar el panel | Se abre con el botón de la fila siguiente; no hay que instalar nada |
| **Cuaderno plantilla** [`S13_02_plantilla_informe_visual`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/2_Practica/S13_02_plantilla_informe_visual.ipynb) | Adaptarlo a vuestro modelo: dibuja el panel 2 × 2 y lo guarda como `informe_visual_panel.png` | Colab; su [código explicado](../../2_Practica/codigo_explicado/S13_02_plantilla_informe_visual.md) |
| **Plantilla del informe** [`plantilla_informe_visual.md`](../1_Trabajar/plantillas/plantilla_informe_visual.md) | El texto de la página (titular, gráficos, viñetas, IA responsable, pie), la lista de comprobación y la sección «Revisión con la rúbrica» | En GitHub: *Raw* para copiar el texto. Trabajad en una copia |
| **Vuestro mejor modelo del curso** | Es el que se cuenta en la página (el campeón del Sprint 8, por ejemplo) | Vuestros cuadernos de los Sprints 8, 10 o 12. Si no cargara a tiempo, la plantilla trae un modelo de ejemplo que sí funciona |
| **El CSV** [`reservas_turisdata.csv`](../../../../datos/reservas_turisdata.csv) | Las reservas **sintéticas** con las que se entrenó y se prueba el modelo | El cuaderno lo descarga solo |
| **Cuaderno del sprint** [`S13_01_visualizacion_resultados`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/2_Practica/S13_01_visualizacion_resultados.ipynb) y la [presentación S13.1](../../1_Teoria/S13.1_Visualizar_y_comunicar_resultados.pdf) | Las pistas para los gráficos (matriz de confusión, ROC, importancia, umbral y coste) y las reglas de comunicación | Colab y PDF; lo hicisteis justo antes del reto |
| **Cómo entregar en GitHub** | Subir los ficheros a `sprint-13/` | [Guía de entrega](../../../../material/5.%20Como_entregar_en_GitHub.md) |
| **Autoevaluación y coevaluación** | Cada persona rellena su hoja | [Hoja del sprint](../2_Entregar/autoevaluacion_y_coevaluacion.md) |
| **Un asistente de IA** (opcional) | Quitar jerga, probar titulares y simular al director | Con las reglas de la «Ayuda 1» del paso a paso |

---

### 3 · 🪜 Guía paso a paso

Son cuatro pasos, de **25 minutos en total** (en el último día del Sprint 12). Cada uno dice **qué hacéis** (la lista corta), **cómo se hace** con el detalle, **qué deberíais ver** y **cuándo está hecho**. Las ayudas (IA, errores, atascos) están al final. Si el tiempo aprieta, completad el nivel mínimo (tres gráficos, titular y tres viñetas) y dejad lo demás para la franja de entrega o para casa.

**Cada paso tiene su propia página.** Abrid la que toque y volved aquí cuando acabéis:

- [Paso 1 · Elegir el modelo, cargarlo y fijar los costes (día 1, 4 minutos)](Reto_Sprint_13_paso_1.md)
- [Paso 2 · Ajustar los gráficos con título-conclusión (día 1, 8 minutos)](Reto_Sprint_13_paso_2.md)
- [Paso 3 · Escribir titular, viñetas y pie (día 1, 8 minutos)](Reto_Sprint_13_paso_3.md)
- [Paso 4 · Probar con otro equipo, revisar con la rúbrica y dejarlo listo (día 1, 5 minutos)](Reto_Sprint_13_paso_4.md)

#### Ayuda 1 · Cómo usar la IA en este reto

La IA puede ahorrar tiempo, pero **es muy mala copiando cifras**. Reglas:
- **Todo lo que dé, lo comprobáis.** Si cambia una cifra, no vale.
- **Las cifras mandan:** las del texto tienen que ser las mismas que las del gráfico.
- **Declaradlo** en el pie del informe o en la sección de IA responsable: qué pedisteis y qué revisasteis.
- **Nada de datos personales ni claves** en una IA.

| Para qué | Ejemplo de petición | Qué comprobáis |
|---|---|---|
| Quitar jerga | «Reescribe estas tres viñetas para un director que no sabe estadística. No cambies ninguna cifra: *[viñetas]*» | Que **las cifras son idénticas** |
| Probar titulares | «Dame 5 versiones de este titular, cada una de menos de 15 palabras, que enuncien una decisión: *[titular]*» | Que la elegida siga siendo verdad |
| Mejorar un gráfico | «Este título describe el gráfico pero no concluye: *[título]*. Propón títulos-conclusión» | Que la conclusión **se vea realmente** en el gráfico |
| Simular al director | «Hazte pasar por un director de hotel sin formación técnica. Lee esta página y dime qué no entiendes» | Que tomáis nota y corregís |

#### Ayuda 2 · Errores frecuentes (y cómo evitarlos)

| Error | Por qué ocurre | Cómo evitarlo |
|---|---|---|
| Un informe lleno de gráficos y sin decisión | Se muestra todo lo que se hizo | Cuatro gráficos, un titular |
| Títulos descriptivos («AUC por modelo») | Es lo que sale por defecto | «Detectamos [vuestra cifra] de cada 10 cancelaciones» |
| Barras que no empiezan en 0 | La herramienta lo hace sola | Fijar el eje a 0 |
| Métricas sobre el entrenamiento | Se reutiliza el cuaderno sin mirar | Comprobar que usan `X_test` |
| Jerga sin explicar | Se escribe para el docente | La prueba de los 30 segundos con otro equipo |
| Texto con cifras distintas del gráfico | Se edita una y no la otra | Revisión cruzada, cifra por cifra |
| El PNG no coincide con el texto | Se cambió algo en el cuaderno y no se volvió a ejecutar | Reiniciar y ejecutar todo antes de descargar el PNG |

#### Ayuda 3 · Si os atascáis

1. **El tiempo se acaba:** reducid a tres gráficos y escribid primero el titular y las viñetas; los gráficos se ajustan después.
2. **No sabéis qué decisión recomendar:** pensad en una acción con persona y fecha («recepción llama los lunes»).
3. **El modelo no carga en la plantilla:** comprobad que usáis el mismo preprocesado con el que se entrenó; si no, dejad el modelo de ejemplo y decidlo en el pie. Después, preguntad al equipo y al docente.
