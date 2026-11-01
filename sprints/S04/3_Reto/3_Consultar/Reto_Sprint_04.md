# Sprint 4 · Reto «Herramientas internas»

> **Ficha del reto, para consultar.** Para trabajar, las [tarjetas de misión](../1_Trabajar/README.md) (una por misión). Para entregar, [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md). Para contrastar lo hecho, el [solucionario de las misiones](Solucionario_misiones.md).
>
> - Volver al [README del sprint](../../README.md) · [README del sprint en PDF](../../pdf/README_Sprint_04.pdf) · [ecofriendly](../../pdf/README_Sprint_04_ecofriendly.pdf)
> - **Esta ficha en PDF:** [a color](pdf/Reto_Sprint_04.pdf) · [ecofriendly, para imprimir](pdf/Reto_Sprint_04_ecofriendly.pdf)
> - Si es vuestro primer reto: [Cómo se trabaja un reto](../../../../material/4.%20Como_se_trabaja_un_reto.md).

## Ficha del reto

### 1 · 🎯 Qué os pide el cliente

**Qué os pide el cliente.** El equipo de reservas de TurisData calcula cada semana sus cifras **a mano en una hoja de cálculo**: es lento y cada persona lo hace distinto. Os pide una **herramienta interna**, un programa en Python que lea el fichero de reservas, calcule **tres KPI** (cifras que resumen cómo va el negocio: la ocupación, el ingreso medio por reserva y la tasa de cancelación por canal), **avise con claridad si el fichero está mal** y guarde el resultado en un fichero JSON que otros sistemas puedan leer.

**Cómo se trabaja.** No hace falta experiencia previa: os damos una **plantilla casi hecha** (funciones vacías y pruebas que os dicen si lo que escribís es correcto) y vuestro trabajo es rellenarla misión a misión, con **Python 3.11 y solo su biblioteca estándar** (`csv`, `json`, `argparse` y `datetime`). La ocupación será solo un *proxy* (una medida aproximada), porque el fichero no trae la capacidad real del hotel. El reto son **seis misiones** en dos días: el **martes**, la lógica con los datos en memoria; el **miércoles**, los ficheros, los errores y la entrega. Cada persona hace además dos *katas* individuales de 10 minutos. El equipo decide hasta dónde llega: 🟢 mínimo, 🟡 estándar o 🔴 extra.

---

### 2 · 🤖 Cómo usar la IA en este reto

La IA puede ahorrar tiempo, pero **da código que parece funcionar y no se entiende**. Reglas:
- **Todo lo que dé, lo ejecutáis y lo entendéis.** Si el docente pregunta por una línea, tenéis que saber explicarla.
- **Las pruebas mandan:** si el código de la IA no las pasa, no vale.
- **Declaradlo** en la sección «Uso de IA y límites» del README: qué pedisteis y qué revisasteis.
- **Nada de datos personales ni claves** en una IA.

| Para qué | Ejemplo de petición | Qué comprobáis |
|---|---|---|
| Entender un error | «Me sale este error: *[mensaje completo]*. Explícame qué significa, sin darme todavía la solución» | Que lo entendéis y lo arregláis vosotros |
| Entender una función | «Explícame línea por línea qué hace esta función: *[código]*» | Ejecutadla con un ejemplo pequeño |
| Pedir una pista | «Quiero calcular el % de cancelaciones por canal con la biblioteca estándar. ¿Qué estructura me conviene? No me des el código» | Que respeta «solo biblioteca estándar» |
| Revisar el estilo | «¿Sigue las normas de estilo de Python (PEP 8) este código? ¿Qué cambiarías?» | Que las pruebas siguen pasando |
