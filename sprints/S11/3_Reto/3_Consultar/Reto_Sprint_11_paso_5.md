# Paso 5 · Informe, README y entrega (día 2, 20 minutos)

<!--nav-->
> Sprint 11 · Reto «Visión artificial para el cliente» · paso 5 de 5 · [Ficha del reto](Reto_Sprint_11.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_11_una_pagina.md)
<!--/nav-->

1. Completar `analisis_errores.md` con lo que ya habéis ido apuntando.
2. Crear el `README.md`.
3. Pedir a alguien que no escribió esa parte que revise con la rúbrica y anote el resultado en el README.
4. Reiniciar y ejecutar todo el cuaderno, bajarlo y subir los ficheros a `sprint-11/`.

**Cómo se hace**
- **El informe** (`analisis_errores.md`, 1–2 páginas), con estos seis apartados: (1) **qué se ha hecho y con qué datos** (origen y licencia); (2) **resultados**: tabla de métricas por clase y comparación con la referencia; (3) **la matriz de confusión interpretada**; (4) **los errores** (la tabla del paso 3); (5) **la recomendación al cliente**: qué se automatiza, qué fotos se revisan a mano y con qué umbral; (6) **al menos dos riesgos de IA responsable** con su medida. Para el nivel mínimo bastan los apartados 1, 3 y 4.
- **El README.** No hay plantilla. Para el nivel mínimo, estas secciones en pocas líneas:

| Sección del README | Qué escribís |
|---|---|
| Qué es | Dos o tres frases: el cliente, qué clasifica el modelo y qué se entrega |
| Cómo se ejecuta | Abrir `reto_vision_cliente.ipynb` en Colab, *Entorno de ejecución → Reiniciar y ejecutar todo*, semilla 42. Para el 🔴, las versiones (`print(tf.__version__)`) |
| Datos | Sintéticos (los genera el cuaderno) o propios, con **autor y licencia** de las fotos; cuántas fotos por clase |
| Uso de IA y límites | Qué pedisteis a la IA, qué revisasteis y qué cambiasteis; los dibujos sintéticos **no son fotos reales** |
| Quién hizo qué | Una línea por persona |

- **La revisión con la rúbrica (5 minutos).** Quien revisa sigue los cinco pasos de «Cómo se revisa» de [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md) y añade al final del README esta sección: un nivel de 1 a 4 por criterio y **una frase de prueba**. Si hay tiempo, arreglad lo más fácil; lo demás queda como «lo primero que mejoraríamos».

```
## Revisión con la rúbrica
**Revisado por:** <nombre> · **Fecha:** <dd/mm/aaaa>

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
|---|---|---|
| Corrección técnica | <1–4> | <p. ej. «se ejecuta de arriba abajo; la prueba se usa dos veces»> |
| Reproducibilidad | <1–4> | <¿salen las mismas cifras siguiendo solo este README?> |
| Análisis y comunicación al cliente | <1–4> | <¿se entiende en qué se equivoca y qué se revisa a mano?> |
| IA responsable | <1–4> | <¿dice qué se pidió, qué se revisó y de dónde salen las fotos?> |

**Lo primero que mejoraríamos:** <una cosa concreta>
```

- **Subir los ficheros (la vía del curso, desde el navegador).** Seguid [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md): (1) en Colab, *Entorno de ejecución → Reiniciar y ejecutar todo* y luego *Archivo → Descargar → Descargar .ipynb*; (2) abrid el repositorio del equipo y **entrad primero en la carpeta `sprint-11`**; (3) *Add file → Upload files*, arrastrad el fichero y pulsad **Commit changes**. El `README.md` y el informe se pueden escribir con *Add file → Create new file*. Cada subida es un *commit* con el nombre de quien la hace. Un reparto posible: la persona A sube `reto_vision_cliente.ipynb` («Añado cuaderno con el modelo y el demostrador»), la B sube `analisis_errores.md` («Añado análisis de errores») y la C sube `README.md` («Añado README»). Los nombres de archivo, **en minúsculas y sin espacios**.

**Qué deberíais ver.** En la carpeta `sprint-11` del repositorio, los tres ficheros del equipo y una hoja de autoevaluación por persona (**3 + N**); y en el historial (el icono del reloj), al menos tres *commits* con nombres distintos.

**Hecho cuando:** otra persona podría ejecutar el cuaderno siguiendo solo el README, la sección «Revisión con la rúbrica» está rellena y los tres *commits* están en el repositorio.

**Después, 30 minutos de entrega y review:** cada persona rellena y sube su autoevaluación y coevaluación a `sprint-11/`, y el equipo enseña, en unos 5 minutos, el demostrador funcionando con 2 o 3 fotos, la matriz de confusión y tres errores comentados («el modelo confunde X con Y porque… y propondríamos…»). Después, la retro.

<!--nav-->
---

[← Paso 4](Reto_Sprint_11_paso_4.md) · [Ficha del reto: ayudas, errores frecuentes y qué hacer si os atascáis](Reto_Sprint_11.md)
<!--/nav-->
