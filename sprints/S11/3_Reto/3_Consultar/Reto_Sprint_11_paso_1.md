# Paso 1 · Preparar los datos (día 1, 25 minutos)

<!--nav-->
> Sprint 11 · Reto «Visión artificial para el cliente» · paso 1 de 5 · [Ficha del reto](Reto_Sprint_11.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_11_una_pagina.md) · [Paso 2 →](Reto_Sprint_11_paso_2.md)
<!--/nav-->

1. Abrir el cuaderno `S11_04` en Colab, hacer una copia y compartirla con el equipo.
2. Decidir si usáis las fotos sintéticas del cuaderno o un conjunto propio.
3. Comprobar cuántas fotos hay por clase y mirarlas.
4. Anotar las etiquetas dudosas y ver cómo se parten los datos.

**Cómo se hace**
- **Copiar el cuaderno.** Abrid [`S11_04_reto_vision_cliente`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/2_Practica/S11_04_reto_vision_cliente.ipynb), *Archivo → Guardar una copia en Drive*, y compartidla con el resto del equipo para que todos puedan editar. Ejecutad **primero la celda de «Preparación»** y después las de los imports y la semilla (`SEMILLA = 42`).
- **Elegir las fotos.** Por defecto (`USAR_DATASET_PROPIO = False`) el cuaderno crea 60 dibujos por clase en `datos_sinteticos/alojamientos`. Si usáis fotos propias, poned `USAR_DATASET_PROPIO = True` y la ruta de vuestra carpeta en `RUTA_PROPIA`: **una carpeta por clase**, nombres sin espacios ni tildes (`casa_rural`), mínimo 30 fotos por clase (mejor 100 o más), hechas por vosotros o con licencia abierta, **sin personas reconocibles**. Apuntad autor y licencia.
- **Contar por clase (ejercicio 1).** Completad `contar_por_clase(ruta)`: devuelve un diccionario `{clase: nº de imágenes}`. Sirve para detectar clases vacías o desequilibradas.
- **Mirar las fotos.** Abrid unas cuantas de cada clase. ¿Hay alguna con la etiqueta dudosa (una piscina en una carpeta de hotel)? Anotadlas: el cuaderno incluye algunas **a propósito**, como pasa con las etiquetas dudosas de los datos reales.
- **Ver la partición.** La celda con `image_dataset_from_directory` reparte las fotos en **entrenamiento (60 %), validación (20 %) y prueba (20 %)** con la misma semilla. La prueba se usa **una sola vez**, al final.

**Qué deberíais ver.** El mensaje `Dataset sintético generado en datos_sinteticos/alojamientos` (solo la primera vez), un diccionario con las cinco clases y 60 fotos en cada una, y una línea como `entrenamiento (180, 48, 48, 3) · validación (60, 48, 48, 3) · prueba (60, 48, 48, 3)`, más una fila de ocho fotos de ejemplo con su clase.

**Hecho cuando:** `contar_por_clase` pasa sus comprobaciones, habéis mirado las fotos y anotado las dudosas, y todo el equipo sabe que la prueba no se toca hasta el paso 3.

<!--nav-->
---

[Ficha del reto](Reto_Sprint_11.md) · [Paso 2 →](Reto_Sprint_11_paso_2.md)
<!--/nav-->
