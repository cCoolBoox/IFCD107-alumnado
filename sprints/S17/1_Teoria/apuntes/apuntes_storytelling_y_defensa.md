# Apuntes del Sprint 17 · Contar el proyecto: storytelling y defensa

La presentación del Sprint 17 es muy esquemática: un mensaje, una pirámide, un guion de 10 minutos. Estos apuntes **explican cómo se construye de verdad una buena defensa**, con ejemplos de frases «antes y después», para que sepáis **qué hacer con cada ensayo**. Léelos antes de rellenar la plantilla de storytelling y volved a ellos antes del ensayo general.

> Este sprint **no tiene técnicas de IA nuevas**. Se trata de algo que muchos proyectos técnicos hacen mal: **que se entienda y se recuerde**. Un proyecto excelente mal contado **parece mediocre**; uno bien contado **se defiende solo**.

---

## 0. De qué va el sprint (en 1 minuto)

Habéis pasado cuatro sprints construyendo un proyecto. Ahora **lo defendéis ante un tribunal** (el docente y, si procede, personas invitadas) que **no es técnico**: es «el cliente y su equipo directivo».

**El tribunal quiere salir sabiendo cuatro cosas:**

1. **Qué problema resolvéis.**
2. **Qué habéis encontrado.**
3. **Qué recomendáis hacer.**
4. **De qué no deben fiarse.**

Es el **criterio I** de la rúbrica (**15 puntos**, el de mayor peso individual después del modelado). Además, la defensa da **evidencia** de los criterios A (valor de negocio), D (interpretación), E (IA responsable) y G (equipo).

**Para el «Apto» hace falta que cada persona responda al menos una pregunta individual.** Por eso **todas las personas hablan y todas deben conocer todo el proyecto**.

| Fecha | Qué |
|---|---|
| **11/12** | Teoría, plantilla de storytelling, storyboard, pitch y **3 rondas de ensayo** |
| **Antes de las 8:30 del 14/12** | Presentación en PDF (≤ 12 diapositivas) subida al repositorio |
| **14/12** | **Defensa** con demo en directo y plan B |

---

## 1. La audiencia: ¿quién escucha y qué decide?

**Hablas para quien escucha, no para ti.** Antes de escribir nada, responde:

| Pregunta | Para un directivo no técnico… |
|---|---|
| **¿Quién es?** | Alguien que decide **si se usa o no** el modelo |
| **¿Qué le importa?** | **Dinero, tiempo, riesgos y qué hacer mañana** |
| **¿Qué sabe?** | Su negocio **muy bien**; la IA, **poco o nada** |
| **¿Qué le asusta?** | Equivocarse, **que le vendan humo**, riesgos legales |

**Qué implica:** la **jerga se traduce**. Cada término técnico lleva **una frase de explicación**.

| Hablas «para ti» | Hablas «para ellos» |
|---|---|
| «Hemos obtenido un F1 de 0,71 con validación cruzada» | «De cada 10 reservas que se cancelan, **detectamos 7**» |
| «Recall de 0,58 en el subgrupo móvil» | «**En reservas por móvil acertamos menos**: 6 de cada 10» |
| «Hemos mitigado el sesgo con reponderación» | «Hemos **corregido** el modelo para que **trate mejor** al canal móvil» |
| «Usamos un transformer con RAG» | «El asistente **busca primero en los documentos** y responde citando la fuente» |

> **Test:** si tu abuela o tu vecino **no entienden la frase**, el tribunal tampoco la entiende **a la primera** (y no tendrá una segunda).

---

## 2. El mensaje único

### 2.1. La fórmula

La presentación propone una frase con tres huecos:

> **Recomendamos [X], porque [evidencia], con la precaución de [límite].**

| Hueco | Qué pone | Ejemplo |
|---|---|---|
| **X** | La **recomendación** | «usar el modelo para planificar la plantilla» |
| **Evidencia** | **Un dato** que lo sostiene | «porque prevé la ocupación a 3 meses con un error del 7 %» |
| **Límite** | **Dónde no vale** | «pero no sirve para fijar precios» |

**Ejemplo completo del reto:**

> *«Podemos prever la ocupación con 3 meses de antelación con un error del 7 %, suficiente para planificar plantilla, pero no para fijar precios.»*

### 2.2. Por qué «único»

Si solo recuerdan **una frase**, ¿cuál es? **Esa es el mensaje.** Todo lo demás en la presentación **o lo apoya o sobra.** Un proyecto con cinco mensajes **no se recuerda ninguno**.

### 2.3. Un resultado honesto cuenta mejor

La presentación lo dice claramente: *«Un resultado honesto («no compensa», «funciona, pero no para este grupo») cuenta mejor que un número bonito sin contexto.»*

| Mensaje | ¿Convence? |
|---|---|
| «Nuestro modelo es muy bueno: 93 % de acierto» | Poco: **¿frente a qué?** ¿Para quién? ¿Con qué datos? |
| «Con la mayoría de reservas el modelo **acierta 8 de cada 10**; en móvil, **6 de cada 10**. Recomendamos usarlo **con revisión humana** en ese canal» | **Mucho**: es concreto, tiene un límite y **una acción** |

**Los límites dan credibilidad**: quien conoce dónde falla su modelo **parece más fiable, no menos**.

---

## 3. La pirámide de la comunicación

### 3.1. La idea

En clase de lengua se aprendió «introducción, nudo, desenlace». **En comunicación profesional se hace al revés**: **primero la conclusión**, luego los argumentos, al final los datos de apoyo.

```
        ▲  CONCLUSIÓN       «Recomendamos usarlo para X, con la precaución Y»
       ▲▲▲ ARGUMENTOS       3 razones
     ▲▲▲▲▲▲ EVIDENCIAS      datos, gráficos, demo
```

**Por qué:** un directivo tiene **poco tiempo y mucha atención al principio**. Si le cuentas «primero hicimos… luego probamos…» **llega al minuto 8 sin saber adónde vas**.

### 3.2. Ejemplo aplicado

| Nivel | Contenido (ejemplo) |
|---|---|
| **Conclusión** | «Recomendamos usar el modelo para planificar plantilla, no para fijar precios» |
| **Argumento 1** | «Supera al método actual en 9 de 12 meses» |
| **Argumento 2** | «Su error es del 7 %, suficiente para ajustar turnos» |
| **Argumento 3** | «Falla con eventos atípicos y en alojamiento rural; hay que revisarlo a mano» |
| **Evidencias** | Gráfico de errores por mes, tabla frente al baseline, demo |

---

## 4. El arco narrativo

Una **historia** tiene **orden y tensión**. El arco que propone el sprint:

| Etapa | Pregunta | Ejemplo (hotel) |
|---|---|---|
| **1. Contexto** | ¿Cuál es la situación? | «El hotel planifica la plantilla **a ojo**» |
| **2. Complicación** | ¿Qué problema aparece? | «Se equivoca **±20 %** y paga horas extra o deja huéspedes sin servicio» |
| **3. Qué hicimos** | ¿Cómo lo resolvimos? | «Datos de X, un modelo sencillo frente a una referencia» |
| **4. Qué aprendimos** | ¿Qué descubrimos? | «Error del 7 %; **funciona hasta con 3 meses de antelación**» |
| **5. Qué proponemos** | ¿Qué hacer ahora? | «Usarlo así, **con estos límites**» |

> **Pirámide y arco no se contradicen.** La pirámide dice **cómo ordenar la información** (conclusión al principio, en la apertura). El arco dice **cómo se desarrolla el relato** después. En la defensa, **empiezas con el mensaje único** (apertura) y **luego cuentas el arco** que lo justifica.

---

## 5. El guion de 10 minutos

| Min | Bloque | Diapositivas | Qué hay que hacer |
|---|---|---|---|
| 0:00-0:45 | **Apertura** | 1 | Gancho + **mensaje único**; presentar al equipo |
| 0:45-2:00 | **Contexto y problema** | 2-3 | Cliente, situación, **decisión** a tomar |
| 2:00-3:00 | **Qué hicimos** | 4-5 | Datos (fuente y licencia en una línea), enfoque en 3 pasos, baseline, métrica |
| 3:00-5:00 | **Qué aprendimos** | 6-7 | **Una cifra y un gráfico** frente al baseline; por qué funciona |
| 5:00-7:30 | **Demostración** | 8 | Entrada normal → resultado con incertidumbre → entrada errónea |
| 7:30-8:30 | **Límites y riesgos** | 9-10 | Dónde falla y **para quién**; 3 riesgos y medidas |
| 8:30-10:00 | **Qué proponemos** | 11-12 | **3 acciones**; qué **no** hacer; cierre con el mensaje único |

**Reglas:**
- **Máximo 12 diapositivas** (≈ **una por cada 50 segundos**: 10 min = 600 s; 600/12 = 50 s).
- **Todas las personas hablan.**
- **Una persona lleva el cronómetro** y avisa con un cartel a los 8 min y a los 9:30.

### 5.1. Ajustar al tiempo de tu turno

El tiempo total de cada equipo **depende de cuántos equipos haya**: dos horas de defensa menos el tiempo de cambio de equipo, repartido entre todos. **El reparto recomendado es 60 % relato, 20 % demo y 20 % preguntas.**

| Nº de equipos | Turno | Relato (60 %) | Demo (20 %) | Preguntas (20 %) |
|---|---|---|---|---|
| 5 | 22 min | ≈ 13 | ≈ 4,5 | ≈ 4,5 |
| 6 | 18 min | ≈ 11 | ≈ 3,5 | ≈ 3,5 |
| 7 | 15 min | ≈ 9 | ≈ 3 | ≈ 3 |
| 8 | 13 min | ≈ 8 | ≈ 2,5 | ≈ 2,5 |

(Por ejemplo, con 22 minutos: 60 % son **13,2** minutos y cada 20 % son **4,4**.)

> **Si tienes más tiempo del que necesitas, no lo rellenes: acaba antes. Si tienes menos, quita diapositivas, no aceleres.** Hablar deprisa **es peor que hablar de menos**: nadie se entera de nada.

**Una referencia práctica:** al hablar con calma se dicen unas **130 palabras por minuto**. Un pitch de **3 minutos** son **unas 400 palabras**, no 1.000. Si tu guion tiene demasiadas, **recorta ideas, no velocidad**.

---

## 6. Diapositivas que ayudan (no que estorban)

### 6.1. Una idea y un título-conclusión por diapositiva

(Lo trabajasteis en el Sprint 13.)

| Título descriptivo ❌ | Título-conclusión ✅ |
|---|---|
| «Resultados del modelo» | «El modelo supera al método simple en 9 de 12 meses» |
| «Análisis por canal» | «En reservas por móvil, el modelo acierta menos» |
| «Riesgos» | «Tres riesgos altos, todos con medida aplicada» |

### 6.2. Reglas de oro

| Regla | Por qué |
|---|---|
| **Poco texto** | Si lo lees, **no hace falta que lo lean**; si lo leen, **no te escuchan** |
| **Una cifra grande** | Se recuerda más que una tabla de 40 números |
| **Un gráfico claro** | Con título-conclusión y colores con sentido |
| **Diapositivas = apoyo, no guion** | El guion está en tu cabeza (o en tus notas), no en la pantalla |
| **Solo lo que está en la memoria congelada** | **No se presentan resultados nuevos** |

> **Cifras iguales que la memoria.** Antes de subir el PDF, revisad **una por una** que **todas coinciden** con la memoria congelada.

### 6.3. Qué se recuerda

La presentación lo resume: para que se recuerde, **una cifra, una imagen, una frase y una historia concreta**. Por ejemplo, «la **historia** de una reserva concreta que el modelo detectó» recuerda más que cinco métricas.

---

## 7. La demostración

### 7.1. Guion de 2,5 minutos

| Paso | Qué se hace | Qué se dice |
|---|---|---|
| 1 | Abrir la app (**ya lanzada**) | «Esto es lo que usaría [usuario]» |
| 2 | **Entrada típica** | «Con este caso, el sistema estima… con esta incertidumbre» |
| 3 | **Entrada errónea o fuera de lo normal** | «Y si alguien se equivoca, **el sistema lo detecta y avisa**» |
| 4 | Mostrar el **aviso de límites** | «Por eso la salida es orientativa; **una persona decide**» |

**Por qué se enseña una entrada errónea a propósito:** demuestra que el sistema es **robusto** y que **habéis pensado en los límites**. Es lo contrario de lo que se teme (que la demo «solo funcione si todo va bien»).

### 7.2. Antes de subir al escenario

- La demo **se prueba el 11/12** y de nuevo **el día de la defensa**.
- Pantalla en **modo presentación** (**fuente grande**, que se lea desde el fondo).
- **No depender de internet** (para eso está el plan B).
- **Datos de ejemplo preparados**.
- **Notificaciones apagadas** (un aviso de WhatsApp en pleno proyector **es lo que se recuerda**).

### 7.3. El plan B

Si la demo falla, **mantened la calma y pasad al vídeo de 90 segundos** (abierto **en otra pestaña**). **No pidáis perdón ni os pongáis a arreglarlo en directo**: es el motivo por el que existe el plan B. **Un fallo bien gestionado no resta.**

---

## 8. Las preguntas del tribunal

### 8.1. Se pueden dirigir a cualquiera

Por eso **toda persona debe conocer todo el proyecto**. Preparad las **10 preguntas más probables**, con respuesta, dato y quién contesta:

| Pregunta probable | Dato en el que apoyarse |
|---|---|
| ¿Por qué elegisteis ese modelo y no otro? | Tabla comparativa (Sprint 15) |
| ¿Cómo sabéis que no hay fuga de datos? | Lista de comprobación; partición temporal |
| ¿Cuánto mejora frente a lo que se hace hoy y cuánto vale? | Baseline y métrica de negocio |
| ¿En qué casos no debemos fiarnos del modelo? | Análisis de errores, model card |
| ¿Qué sesgos habéis encontrado y qué habéis hecho? | Tabla por subgrupos y mitigación medida |
| ¿Qué datos personales usáis y qué riesgo AI Act tiene? | Registro de riesgos, clasificación |
| ¿Qué pasaría con un suceso atípico o un dato nuevo? | Limitaciones |
| ¿Cómo lo mantendríais y monitorizaríais? | Model card, sección 9 |
| ¿Qué haríais con más tiempo o más datos? | Conclusiones |
| ¿Qué ha aportado cada persona del equipo? | Roles, commits |

### 8.2. El método RESPONDE (20 segundos)

| Letra | Qué hacer | Ejemplo (pregunta: «¿cómo sabéis que no es sobreajuste?») |
|---|---|---|
| **R** | **Repite** o reformula la pregunta | «¿Preguntas si el modelo solo funciona con los datos que vio?» |
| **E** | **Empieza** con la respuesta directa (sí / no / depende) | «Creemos que no» |
| **S** | **Sustenta** con un dato o figura | «Lo evaluamos en un test que no tocamos hasta el final: 0,69 frente a 0,71 en validación» |
| **P** | **Pon** el límite | «Pero solo lo hemos probado con datos de 2022 a 2024» |
| **O** | **Ofrece** el puente | «El detalle está en la sección 5 de la memoria» |

**Y si no lo sabes: dilo.** *«No lo hemos medido; lo haríamos así…»*. **No inventes.** Inventar una respuesta **es el error más caro** (y el tribunal lo detecta).

### 8.3. Técnicas para no quedarte en blanco

- **Pide un segundo** («déjame pensarlo») **es mejor que empezar sin saber adónde vas.**
- **Contesta lo que te preguntan**, no lo que te sabes.
- **Si la pregunta es para otra persona**, puedes pasársela **solo si de verdad no lo sabes** (no como hábito: **para el Apto, cada persona responde**).

---

## 9. Los ensayos del 11/12 (3 horas)

| Ronda | Cómo | Qué se comprueba |
|---|---|---|
| **1 · Cronometrada** (30 min) | Solo el equipo, **con demo** | Tiempo, transiciones, quién habla cuándo |
| **2 · Con preguntas** (45 min) | **Otro equipo hace de tribunal** | Respuestas con datos, método RESPONDE |
| **3 · Ensayo general** (60 min) | **Exactamente como el 14/12**, con el docente | Tiempo, demo, plan B, reparto |
| **Cambios** (45 min) | Ajustar diapositivas y guion | Lista de **3 cambios** y responsable |

**Después de cada ronda, escribid dos cosas que mejorar y arreglad solo eso.** (Intentar cambiarlo todo **empeora** el siguiente ensayo.)

**Ficha de feedback entre equipos** (la rellena quien escucha): lo que **mejor** funcionó · el mensaje que entendí **con mis palabras** · un momento que no entendí o que sobra · una pregunta que haría.

> **La pregunta clave del ensayo:** «¿Cuál es el mensaje que te llevas?». **Si el equipo oyente no repite vuestro mensaje único, no se ha entendido.**

---

## 10. El día de la defensa

1. **Llegad 15 minutos antes**: proyector, demo, plan B abierto.
2. **Hablad para el público no técnico.**
3. **Todas las personas hablan** (con el reparto escrito y ensayado).
4. **Cuidad el tiempo**: **se corta cuando se agota.**
5. **Si la demo falla**: calma y plan B.
6. Al terminar, el docente da **feedback global** y se cierra el curso con una **retrospectiva breve del proyecto**.

---

## 11. Errores frecuentes (y cómo evitarlos)

| Error | Por qué ocurre | Cómo evitarlo |
|---|---|---|
| **Contarlo todo en orden cronológico** («primero hicimos…») | Es lo más fácil | Empezad por la **conclusión** |
| **Diapositivas llenas de texto** | «Para no olvidar» | Una idea y un **título-conclusión** |
| **Una sola persona habla** | Nervios | **Reparto de voces** escrito y ensayado |
| **Pasarse de tiempo** | No se cronometró | Dos ensayos con reloj y un recorte |
| **Jerga sin explicar** | Hábito técnico | Cada término con **una frase de traducción** |
| **Cifras distintas a la memoria** | Se retocan al final | Revisión final contra la memoria congelada |
| **Demo sin plan B** | Confianza | **Vídeo** abierto en otra pestaña |
| **Esconder los límites** | Miedo a quedar mal | Los límites **dan credibilidad** |
| **Inventar una respuesta** | Miedo a decir «no lo sé» | «No lo hemos medido; lo haríamos así…» |

---

## 12. Dónde practicar cada cosa

| Si no entiendes… | Mira la sección | Practica en |
|---|---|---|
| Quién es el público y cómo hablarle | 1 | Primer apartado de `plantilla_storytelling.md` |
| El mensaje único | 2 | Plantilla de storytelling; pitch de 3 minutos |
| Pirámide y arco narrativo | 3 y 4 | Plantilla de storytelling (pirámide y arco) |
| El guion de 10 minutos y el reparto | 5 | `guion_defensa.md` |
| Diapositivas | 6 | Storyboard de 12 diapositivas |
| La demostración | 7 | Guion de demo en `guion_defensa.md` |
| Preguntas del tribunal | 8 | Tabla de preguntas de `guion_defensa.md` |
| Ensayos | 9 | Rondas del 11/12 |

## 13. Chuleta de vocabulario

| Palabra | En lengua normal |
|---|---|
| **Storytelling** | Contar con estructura para que se entienda y se recuerde |
| **Audiencia** | Quién escucha |
| **Mensaje único** | La frase que quieres que recuerden |
| **Pirámide de la comunicación** | Conclusión → argumentos → evidencias |
| **Arco narrativo** | Contexto → complicación → qué hicimos → qué aprendimos → qué proponemos |
| **Pitch** | Presentación breve (3 minutos) |
| **Storyboard** | Esquema de cada diapositiva antes de hacerlas |
| **Título-conclusión** | Título que dice lo que se aprende |
| **Plan B** | Vídeo por si falla la demo |
| **RESPONDE** | Método de 6 pasos para contestar preguntas |
| **Tribunal** | Quien evalúa la defensa |

## 14. Cómo estudiar estos apuntes

1. **Antes de la plantilla de storytelling**, leed las secciones 1 a 4.
2. **Escribid vuestro mensaje único** con la fórmula de la sección 2 **antes** de hacer ninguna diapositiva.
3. **Antes de los ensayos**, leed las secciones 5, 7 y 8, y repartid las 10 preguntas.
4. **Regla final:** si alguien que no ha seguido el proyecto **no es capaz de repetir vuestro mensaje con sus propias palabras** al acabar, **la defensa no ha cumplido su objetivo**, por bueno que sea el trabajo.
