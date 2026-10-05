# Sprint 2 · Las matemáticas y la estadística detrás

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_02.pdf`](Guia_Sprint_02.pdf)
- 🖥️ **S02.1 · Matematicas para IA:** [`S02.1_Matematicas_para_IA.pdf`](presentaciones/S02.1_Matematicas_para_IA.pdf)
- 🖥️ **S02.2 · Estadistica y probabilidad:** [`S02.2_Estadistica_y_probabilidad.pdf`](presentaciones/S02.2_Estadistica_y_probabilidad.pdf)
- 🖥️ **S02.3 · Ecosistema de software para IA:** [`S02.3_Ecosistema_de_software_para_IA.pdf`](presentaciones/S02.3_Ecosistema_de_software_para_IA.pdf)

**Pregunta guía:** ¿en qué se apoyan los modelos y cuándo no debemos fiarnos de un dato?

| | |
|---|---|
| **Fechas** | mié 21/10 – vie 23/10 (el relevo con el Sprint 3 se hace a mitad de jornada del viernes) |
| **Horas** | 10 h en total: **5 h de teoría (T) · 3 h de práctica (P) · 2 h de reto (PBL)** |
| **Módulo** | M1a (UD 1a.4, 1a.5 y 1a.6) |
| **Bloque** | A · Sin Python: papel, calculadora, Desmos/GeoGebra y (si queréis) una hoja de cálculo |
| **Evaluación** | Test corto de M1a (conceptos, matemáticas y estadística), dictamen del reto y hojas de ejercicios |

## Qué aprenderás
1. Operar con **vectores y matrices** y entender qué hace un modelo cuando "multiplica" datos por pesos.
2. Interpretar una **derivada**, un **gradiente** y el **descenso del gradiente** como la forma en que un modelo mejora poco a poco.
3. Resumir datos con **media, mediana, desviación típica y cuartiles**, y calcular **probabilidades**, incluida la **probabilidad condicionada** y el teorema de **Bayes**.
4. Detectar **muestras sesgadas**, la **confusión entre correlación y causalidad** y la **paradoja de Simpson**.
5. Conocer el **ecosistema de software** de IA (Python, Colab, librerías, GPU) y tener tus cuentas listas.

## Requisitos previos
Sprint 1 terminado. Matemáticas de secundaria (fracciones, potencias, porcentajes). Una calculadora o el móvil.

## Materiales del sprint

| Material | Contenido | Tiempo | Cuándo |
|---|---|---|---|
| [`alta_cuentas.md`](alta_cuentas.md) | Alta en Colab y GitHub (checklist) | 1 h | Práctica (mié 21/10, **antes del 22/10**) |
| [`ejercicios_algebra_calculo.md`](ejercicios_algebra_calculo.md) | 12 ejercicios: vectores, matrices, derivadas, gradiente (papel y Desmos/GeoGebra) | 1 h en clase + resto en el equipo | Práctica |
| [`ejercicios_estadistica.md`](ejercicios_estadistica.md) | 14 ejercicios: estadística, probabilidad, Bayes, muestreo, sesgo, Simpson | dentro de la teoría y en el equipo | Práctica |
| [`estadisticas_enganosas.md`](estadisticas_enganosas.md) | 9 casos de estadísticas engañosas | 40-60 min | Práctica |
| `../../datos/informe_cliente.md` y `../../datos/informe_cliente.csv` | **Informe del cliente** y datos del reto (no se copian aquí: están en la carpeta `datos/` del repositorio) | reto | Reto |

*(Como no hay notebooks en este bloque, no hay enlaces a Colab: los materiales son `.md` para trabajar en papel o pantalla.)*

**Mínimo para el entregable de la hoja de ejercicios:** al menos **8 de los 12** ejercicios de la hoja 1 (con los M7, M10 y M11 obligatorios) y **10 de los 14** de la hoja 2 (con E7, E8, E10 y E14 obligatorios). Escribid **cómo lo habéis hecho**, no solo el resultado.

---

# Ficha del reto · "¿Nos fiamos de este informe?"

## Escena del cliente
La dirección de *TurisData Canarias* ha preparado un **borrador de informe** sobre cancelaciones para presentarlo al consejo. Antes de hacerlo, la directora os lo pasa: *"Un cliente del consejo me dijo que hay que revisar estos números con ojo crítico. Decidme **si nos podemos fiar de cada afirmación**, y si no, qué debemos decir en su lugar. Y cuidado: la decisión de a qué canal dar prioridad depende de esto."*

## Qué tenéis que entregar
1. **Dictamen de auditoría** (2-3 páginas en `.md` o PDF): para cada una de las **seis afirmaciones** del informe, indicad:
   - **Veredicto:** *fiable · parcialmente fiable · no fiable · no se puede saber*.
   - **Problema detectado** (tipo de error estadístico) y **por qué**.
   - **Cálculo rehecho** cuando haya datos (tabla con vuestros números).
   - **Cómo debería decirse** (redacción corregida) y **qué datos faltan**.
2. **Recomendación** para la dirección sobre el canal (afirmación 2): qué decidir y qué cautelas.
3. **La hoja de ejercicios** del sprint (ver mínimo arriba).

## Datos y recursos
- **`datos/informe_cliente.md`**: el borrador del informe con las seis afirmaciones.
- **`datos/informe_cliente.csv`**: datos de **2.400 reservas**, agrupadas por `tarifa` y `canal`, con columnas `reservas` y `cancelaciones`. El archivo tiene 4 filas (una por combinación de tarifa y canal).
- Vuestras hojas de ejercicios, la lista de control de [`estadisticas_enganosas.md`](estadisticas_enganosas.md) y una calculadora u hoja de cálculo. **No hace falta Python.**

## Restricciones
- **Tiempo:** 2 h de reto en clase (dentro de las 10 h del sprint).
- **Extensión:** 2-3 páginas.
- Cada cifra que aparezca en el dictamen debe poder **rehacerse** con los datos entregados (reproducibilidad).
- Cuando no haya datos para comprobar una afirmación, **no inventéis números**: decid qué datos harían falta.
- Si usáis un asistente de IA para redactar o calcular, **declarad dónde** y **comprobad** los cálculos a mano al menos en las afirmaciones 2 y 6.

## Criterios de evaluación
Cada entregable se evalúa de 0 a 4 en los cuatro criterios de la rúbrica de retos.

| Criterio | 1 · Insuficiente | 2 · Suficiente | 3 · Bueno | 4 · Excelente |
|---|---|---|---|---|
| **Corrección técnica** | Cálculos erróneos o errores no detectados | Detecta la mayoría de los errores, con fallos de cálculo o de nombre | Detecta los seis problemas y rehace los cálculos correctamente | Además cuantifica la incertidumbre (p. ej. intervalos) o razona cuándo la diferencia es real |
| **Reproducibilidad** | No se ve cómo se han obtenido las cifras | Cifras sin todos los pasos | Cada cifra se puede rehacer con los datos y los pasos indicados | Además hay tabla de cálculo o hoja adjunta y las fuentes están citadas |
| **Análisis y comunicación al cliente** | Solo dice "está mal" | Explica cada error de forma correcta pero técnica | Explica con lenguaje claro y propone redacciones corregidas | Recomendación accionable sobre el canal, con límites y datos a pedir |
| **IA responsable** | No se considera | Menciona "cuidado con los sesgos" | Relaciona los errores con riesgos de entrenar o decidir con datos así (muestra sesgada, confusión) | Propone comprobaciones concretas antes de usar estos datos para un modelo |

## Pasos sugeridos (2 h de reto)

| Momento | Qué hacer |
|---|---|
| **Mié 21/10 · planning (30 min)** | Leed el informe, repartid las 6 afirmaciones entre las personas del equipo (con revisión cruzada) y preparad el tablero |
| **Jue 22/10 (30 min)** | Primera lectura de cada afirmación con la lista de control; anotad vuestras **hipótesis** de error |
| **Vie 23/10 (30 min)** | Rehaced los cálculos, redactad el dictamen y la recomendación, revisión cruzada y DoD |
| **Vie 23/10 · última media hora** | Review (5 min por equipo) y retro |

## Pistas (sin destriparlo)
- Empezad por comprobar **las cuentas**: ¿las cifras que da el informe salen de los datos?
- En la afirmación 2, **mirad la tabla completa** y comparad canal por canal **dentro de cada tarifa**. Calculad también **cuántas reservas** de cada canal son de cada tarifa.
- En la 5 y la 6, pensad en qué **debería compararse** en lugar de lo que se compara.
- En la 1 y la 3, ¿"la media del sector" y "el depósito reduce" están respaldados por los datos entregados?
- ¡Ojo!: puede haber afirmaciones con cuentas correctas pero conclusión incorrecta.

## Qué se enseña en la review (5 min por equipo)
- **Una afirmación** de las seis y vuestro dictamen (veredicto + por qué).
- **La tabla de cálculo** de la afirmación 2 y vuestra recomendación sobre el canal.
- **El error que más os ha costado** ver.
- Los datos que pediríais a TurisData para cerrar las dudas.

## Checklist Definition of Done
- [ ] Dictamen de 2-3 páginas con **las seis afirmaciones** y su veredicto
- [ ] Cálculos rehechos con los datos (afirmaciones 1, 2 y 6), con los pasos visibles
- [ ] La afirmación 2 tiene tabla por tarifa y canal, y una recomendación con cautelas
- [ ] Cada error tiene su **nombre** (muestreo, correlación/causalidad, Simpson, base...)
- [ ] Redacción corregida de cada afirmación
- [ ] Lista de datos que faltan
- [ ] Al menos una relación con **IA responsable** (qué pasaría si entrenáramos un modelo con estos datos)
- [ ] Hoja de ejercicios con el mínimo exigido
- [ ] Revisión cruzada, subido a Git, tablero actualizado
- [ ] Autoevaluación y coevaluación rellenadas
- [ ] Alta en Colab y GitHub hecha ( **antes del 22/10**)

## Preguntas de la retrospectiva
1. ¿Cómo repartimos las seis afirmaciones? ¿Fue justo?
2. ¿Qué error nos ha resultado más difícil de ver? ¿Por qué?
3. ¿Qué habríamos pedido al cliente antes de empezar?

## Recursos
1. **Desmos** (desmos.com/calculator) y **GeoGebra** (geogebra.org): para dibujar funciones, tangentes y puntos.
2. Un texto divulgativo sobre la **paradoja de Simpson** y otro sobre **cómo mentir con estadísticas** (buscad divulgación de calidad y citad la fuente).
3. **Khan Academy** (en español): álgebra lineal, derivadas y estadística (para repasar).
4. Los apuntes y las presentaciones S2.1, S2.2 y S2.3.
5. [`estadisticas_enganosas.md`](estadisticas_enganosas.md): lista de control para leer una estadística.
