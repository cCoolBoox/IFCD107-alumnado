# Paso 4 · Pulir el demostrador y probarlo en limpio (día 2, 40 minutos)

<!--nav-->
> Sprint 16 · Reto «Entrega final: evaluar, demostrar y documentar» · paso 4 de 8 · [Ficha del reto](Reto_Sprint_16.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_16_una_pagina.md) · [Paso 5 →](Reto_Sprint_16_paso_5.md)
<!--/nav-->

1. Adaptar `logica.py` a los campos, las validaciones y el aviso de incertidumbre de vuestro proyecto.
2. Probar entradas normales, imposibles y vacías.
3. Escribir las pruebas con `pytest` y fijar las versiones en `requirements.txt`.
4. Lanzarlo en una carpeta nueva siguiendo solo el README.

**Cómo se hace**
- **Adaptar.** En `logica.py` cambiad los campos, los rangos válidos y el texto del aviso (cuándo no fiarse, qué no se debe hacer). Los errores, en español y diciendo qué campo falla, qué se esperaba y qué se recibió. La respuesta **devuelve datos**, no imprime: la interfaz es quien los muestra. Si vuestro demostrador es un asistente o *chatbot*, tiene que decir que es una IA y citar sus fuentes.
- **Probar a propósito.** 3 entradas normales, 1 imposible (una edad de 250) y 1 vacía. Debe salir un mensaje claro, por ejemplo «Introduce una edad entre 0 y 120», y nunca un texto rojo de error. Al predecir, debe mostrar algo como «Riesgo: alto (confianza media)».
- **Pruebas.** En `tests/test_logica.py` cambiad la reserva de ejemplo por una de vuestro proyecto y añadid tres pruebas propias de sentido común (por ejemplo: «una reserva flexible y sin depósito tiene más riesgo que una no reembolsable con depósito total»). Desde la carpeta `demostrador/`: `pytest -q`.
- **Versiones.** Dejad en `requirements.txt` solo lo que usáis, con versión fija, y anotad la versión de Python en el README.
- **Lanzar.** `pip install -r requirements.txt` y `streamlit run app.py` (se abre en `http://localhost:8501`). La API es opcional.

**Qué deberíais ver.** La app abierta en el navegador, mensajes claros con las entradas malas, un aviso de incertidumbre en cada resultado y `pytest -q` sin fallos.

**Hecho cuando:** el demostrador se lanza con un comando, no se rompe con las cinco entradas de prueba y las pruebas pasan.

<!--nav-->
---

[← Paso 3](Reto_Sprint_16_paso_3.md) · [Ficha del reto](Reto_Sprint_16.md) · [Paso 5 →](Reto_Sprint_16_paso_5.md)
<!--/nav-->
