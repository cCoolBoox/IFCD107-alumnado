# Casos de estadísticas engañosas

**Práctica del sprint (≈ 1 h).** Nueve situaciones inspiradas en errores muy habituales al leer informes, noticias y gráficos. **Los datos son inventados.** En parejas o tríos.

## Cómo trabajar cada caso
Para cada uno, responded en 3 líneas:
1. **¿Qué se afirma?** (con vuestras palabras)
2. **¿Qué falla o qué falta?** (tipo de error)
3. **¿Cómo lo dirías bien?** (una frase corregida o el gráfico correcto)

Después, poned nombre al error: *eje truncado · media que oculta · riesgo relativo frente a absoluto · muestra pequeña · periodo elegido a conveniencia · correlación espuria · base distinta · sesgo de supervivencia · falacia de la tasa base*.

---

## Caso 1 · "¡Las reservas se han disparado!"
Un gráfico de barras muestra las reservas anuales. El eje vertical empieza en **1.000**.

```
Reservas
1.060 |            ████
1.040 |            ████
1.020 |  ████      ████
1.000 |__████______████__
        2024      2025
       1.020      1.050
```
Titular: **«Las reservas de 2025 triplican las de 2024».**
- ¿Qué proporción crecen realmente las reservas?
- ¿Qué hace el gráfico con nuestra percepción?

## Caso 2 · "El sueldo medio es de 2.850 €"
Un apartamento hotel promociona empleo: **«Sueldo medio de la plantilla: 2.850 €».** La plantilla son 10 personas: 9 cobran **1.500 €** y la dirección cobra **15.000 €**.
- Comprobad la media.
- ¿Cuánto cobra la persona "típica"? ¿Qué estadístico sería más honesto?

## Caso 3 · "El depósito reduce a la mitad las cancelaciones"
Un estudio dice: **«Con un depósito, el riesgo de cancelación baja un 50 %»**. Los datos: sin depósito, **2 de cada 1.000** reservas se cancelan; con depósito, **1 de cada 1.000**.
- ¿Cuál es la reducción **absoluta**?
- ¿Sería la afirmación igual de llamativa dicha así?
- ¿Qué información falta para decidir si compensa (coste del depósito, otras diferencias entre los grupos)?

## Caso 4 · "El 100 % recomienda la excursión de astronomía"
Un folleto afirma: **«El 100 % de los clientes recomienda nuestra excursión de astronomía»**. Se basa en las respuestas de **5 personas** que rellenaron la encuesta de la web.
- ¿Qué problema hay con el tamaño de muestra?
- ¿Y con quién responde a la encuesta?
- ¿Cómo se debería presentar (o qué haría falta para poder afirmarlo)?

## Caso 5 · "En agosto vendimos un 40 % más que en julio"
El informe destaca: **«¡Crecimiento del 40 % en un mes!»**. En el mismo informe, agosto siempre es el mes más alto del año.
- ¿Qué comparación sería más justa?
- ¿Qué información habría que mostrar para saber si TurisData **crece de verdad**?

## Caso 6 · "Más helados vendidos, más reservas"
Un directivo observa que en los meses en que se venden más helados en la piscina hay más reservas: **«Regalemos helados y subirán las reservas».**
- ¿Qué tercera variable hay detrás de las dos?
- ¿Cómo se podría comprobar si el helado influye de verdad? (piensa en un experimento)

## Caso 7 · "El apartamento A sube un 50 %, el B baja un 10 %"
Ocupación: **A** pasa del **10 % al 15 %**; **B** pasa del **90 % al 81 %**. Titular: **«A crece un 50 %, B cae un 10 %: A es el mejor alojamiento»**.
- Calculad los cambios en **puntos porcentuales** de cada uno.
- ¿Qué pasa con los porcentajes cuando la base es muy distinta?
- ¿Qué alojamiento genera más noches ocupadas?

## Caso 8 · "Los negocios antiguos tienen buenas valoraciones"
Un análisis de los alojamientos con **más de 10 años abiertos** concluye: **«Todos tienen una valoración media superior a 4,5. La buena valoración garantiza sobrevivir»**.
- ¿Qué alojamientos **no** están en el análisis?
- ¿Cómo se llama este sesgo y en qué famoso caso de aviones de la Segunda Guerra Mundial se explica? (Podéis buscarlo.)

## Caso 9 · "Nuestro detector es fiable al 95 %"
El proveedor de un detector de reservas fraudulentas dice: **«Acierta el 95 %; si salta la alarma, hay un 95 % de probabilidad de fraude»**. El fraude real es del **1 %** de las reservas y el detector se equivoca en el **5 %** de las reservas honestas.
- ¿Qué se está confundiendo? (pista: ejercicio E7)
- Estimad qué proporción de las alarmas serán reales si además detecta el 95 % del fraude.

---

## Ficha para el resumen (una por pareja)

| Caso | Tipo de error | Cómo lo diríamos bien |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |
| 6 | | |
| 7 | | |
| 8 | | |
| 9 | | |

## Lista de control para leer una estadística (para usar en el reto)
1. **¿De dónde sale?** (fuente, quién la hizo, cuándo)
2. **¿Cuántos datos hay?** (tamaño de muestra, margen de error)
3. **¿Quién falta?** (cómo se ha elegido la muestra)
4. **¿Con qué se compara?** (base, periodo, grupo de control)
5. **¿Qué gráfico hay?** (ejes, escalas)
6. **¿Media o mediana? ¿Hay valores atípicos?**
7. **¿Absoluto o relativo?**
8. **¿Correlación o causalidad? ¿Hay una tercera variable?**
9. **¿Hay subgrupos que cambien la conclusión?** (paradoja de Simpson)
10. **¿La conclusión se sigue de los datos?**
