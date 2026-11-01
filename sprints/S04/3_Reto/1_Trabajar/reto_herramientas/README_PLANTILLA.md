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

## Revisión con la rúbrica
<Rúbrica completa en la ficha del reto, apartado 3. Rellena quien revisa y **no escribió esa parte**: ejecutar, leer el README como cliente, mirar el código, poner nivel con prueba.>

**Revisado por:** <nombre> · **Fecha:** <dd/mm/aaaa>

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
|---|---|---|
| Corrección técnica | <1–4> | <p. ej. «12 de 12 pruebas, falta el docstring de `main`»> |
| Reproducibilidad | <1–4> | <¿obtienes el mismo JSON siguiendo solo este README?> |
| Análisis y comunicación al cliente | <1–4> | <¿se entiende qué es cada KPI y por qué la ocupación es un proxy?> |
| IA responsable | <1–4> | <¿dice qué se pidió, qué se revisó y qué se cambió?> |

**Lo primero que mejoraríamos:** <una cosa concreta>
