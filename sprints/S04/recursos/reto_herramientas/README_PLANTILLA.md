# Herramientas internas · TurisData Canarias

> Plantilla del README de tu repositorio. Sustituye lo que está entre `<...>` y borra este aviso.

**Equipo / autoría:** <nombres>
**Fecha:** <dd/mm/aaaa>

## Qué hace
<Dos o tres frases: lee el CSV de reservas, calcula KPIs, gestiona errores y exporta un JSON.>

## Requisitos
- Python 3.11 (biblioteca estándar; pandas solo para la versión opcional).
- El fichero `reservas_turisdata.csv` en la misma carpeta o en `datos/`.

## Cómo se ejecuta
```
python kpis.py reservas_turisdata.csv salida.json --capacidad 40
```
Salida esperada: `<pega aquí el mensaje que imprime tu script>`

## Cómo se prueban
```
python test_kpis.py
```
Resultado: <n de n pruebas superadas>

## KPIs y decisiones
| KPI | Definición | Decisión o limitación |
|---|---|---|
| Ocupación (proxy) | <fórmula> | <por qué es solo un proxy y qué capacidad supusiste> |
| Ingreso medio por reserva | <fórmula> | <¿por qué solo confirmadas?> |
| Tasa de cancelación por canal | <fórmula> | <cómo se interpreta> |

## Gestión de errores
<Qué errores controla el script (fichero inexistente, columnas que faltan, filas defectuosas), qué mensaje da y qué exit code devuelve.>

## Versión con pandas (opcional)
<Si la has hecho: en qué se parece y qué diferencias has encontrado.>

## Uso de IA y límites
<Indica si has usado un asistente de IA y para qué; qué has revisado tú. Los datos son sintéticos.>
