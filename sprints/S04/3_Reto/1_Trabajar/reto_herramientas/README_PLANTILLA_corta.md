# Herramientas internas · TurisData Canarias

> **README corto** para la entrega en nivel mínimo con explicación. Cópialo como `README.md`, sustituye lo que está entre `<...>` y borra este aviso. Si tu equipo llega más lejos, usa `README_PLANTILLA.md`.

**Equipo:** <nombres> · **Fecha:** <dd/mm/aaaa>

## Qué hace
<Dos frases: lee el CSV de reservas, calcula KPIs y exporta un JSON.>

## Cómo se ejecuta y se prueba
```
python kpis.py reservas_turisdata.csv salida.json --capacidad 40
python test_kpis.py
```
Resultado de las pruebas: <n de n superadas>

## Quién hizo qué
| Parte | La escribí yo | La copié y la expliqué |
|---|---|---|
| `tasa_cancelacion_por_canal` e `ingreso_medio_por_reserva` | <nombres o —> | <nombres o —> |
| `_convertir_fila` y `leer_reservas` | <nombres o —> | <nombres o —> |
| `exportar_json` y `main` | <nombres o —> | <nombres o —> |

## Explicación de una función
<Elige una función y explica con tus palabras, línea a línea, qué hace y por qué. Cinco o seis líneas.>

## Errores que controla
<Qué pasa si el fichero no existe, falta una columna o una fila viene mal; qué mensaje da.>

## Uso de IA
<Si has usado un asistente de IA: para qué y qué revisaste tú. Los datos son sintéticos.>

## Qué mejoraríamos
<Una cosa concreta.>
