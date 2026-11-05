# Solucionario · cuadernos «en clase» del Sprint 5

- Las soluciones de los ejercicios de los cinco cuadernos «en clase» (`S05_01`, `03`, `04`, `05` y `06`), con lo que tiene que salir.
- Úsalo **después de intentarlo**: copiar sin entender no sirve para aprender.
- Son las mismas soluciones que llevan los cuadernos en «🆘 Soluciones de referencia».
- Las soluciones de los cuadernos completos («para casa») están en [`../para_casa/Solucionario_para_casa.md`](../para_casa/Solucionario_para_casa.md).

---

## S05_01 · NumPy: arrays y vectorización (en clase)

### Paso 2 · Ejercicio 1 · Separar las columnas (8 min)

```python
# 2.3 · TU TURNO: sustituye cada ... por tabla[:, k] (k = número de la columna)
temperatura = tabla[:, 1]
festivo = tabla[:, 2]
precio = tabla[:, 3]
```

**Tiene que salir:**

```text
✅ ocupacion
✅ temperatura
✅ festivo
✅ precio
```

### Paso 4 · Ejercicio 3 · Ingreso diario y estandarización (12 min)

```python
# 4.2 · TU TURNO: la misma cuenta, pero con ocupacion y precio enteros (sin [0])
ingreso_diario = ocupacion / 100 * 120 * precio
```

**Tiene que salir:**

```text
✅ ingreso_diario: un valor por día
✅ ingreso_diario: primer día
[10405.52  9891.6   8345.41]
Ingreso medio diario: 7,237 EUR
```

### Paso 4 · Ejercicio 3 · (segunda celda: estandarización)

```python
# 4.6 · TU TURNO: restar la media y dividir entre la desviación, con la ocupación entera
ocupacion_z = (ocupacion - ocupacion.mean()) / ocupacion.std()
```

**Tiene que salir:**

```text
✅ ocupacion_z: media 0
✅ ocupacion_z: desviación 1
[2.13 1.69 0.32]
```

---

## S05_03 · Descenso del gradiente y regresión desde cero (en clase)

### Paso 3 · Ejercicio 4 · El gradiente (10 min)

```python
# 3.2 · TU TURNO: las mismas dos líneas de la celda 3.1, pero con X, y y w
def gradiente_mse(X, y, w):
    errores = X @ w - y
    return 2 / len(y) * X.T @ errores
```

**Tiene que salir:**

```text
✅ gradiente: un valor por parámetro
✅ gradiente: ejemplo de 2 días
✅ gradiente: coincide con el numérico
[-136.98   12.07]
```

### Paso 5 · Ejercicio 5 · Entrenar (10 min)

```python
# 5.1 · TU TURNO: entrenar = repetir "calcular el gradiente y dar un paso cuesta abajo"
def entrenar(X, y, tasa=0.1, epocas=200):
    w = np.zeros(X.shape[1])             # empezamos con todos los parámetros a 0
    historial = []                       # aquí guardamos el error de cada vuelta
    for epoca in range(epocas):
        gradiente = gradiente_mse(X, y, w)
        w = w - tasa * gradiente
        historial.append(mse(y, X @ w))
    return w, historial
```

**Tiene que salir:**

```text
Error al empezar: 3081.3 · al terminar: 55.95
w final: [68.49 -6.03]
✅ entrenar: un error por vuelta
✅ entrenar: el error baja
✅ entrenar: el error nunca sube
✅ entrenar: llega a la solución exacta
```

---

## S05_04 · Estadística con Python: describir y dar un margen de error (en clase)

### Paso 2 · Ejercicio 1 · Resumen de la ocupación (10 min)

```python
# 2.2 · TU TURNO: lo mismo que en la celda 2.1, pero con serie y redondeado a 2 decimales
resumen = {
    "media": round(serie.mean(), 2),
    "mediana": round(serie.median(), 2),
    "desviacion": round(serie.std(), 2),
    "iqr": round(serie.quantile(0.75) - serie.quantile(0.25), 2),
}
```

**Tiene que salir:**

```text
✅ resumen: media
✅ resumen: mediana
✅ resumen: desviación
✅ resumen: IQR
media: 68.49
mediana: 67.7
desviacion: 9.61
iqr: 13.6
```

### Paso 4 · Ejercicio 5 · IC de la tasa de cancelación (10 min)

```python
# 4.1 · TU TURNO: las mismas cuentas de la celda 3.2, pero con las 6000 reservas
p_hat = reservas["cancelada"].mean()
n_res = len(reservas)
error = np.sqrt(p_hat * (1 - p_hat) / n_res)
ic_tasa = (round(p_hat - 1.96 * error, 4), round(p_hat + 1.96 * error, 4))
```

**Tiene que salir:**

```text
✅ IC: p_hat
✅ IC: n_res
✅ IC: error
✅ IC: intervalo
Tasa de cancelación: 45.9 % (IC 95 %: 44.6 % a 47.2 %)
```

---

## S05_05 · Estadística con Python: ¿los festivos suben la ocupación? ¿y el calor la baja? (en clase)

### Paso 2 · Ejercicio 1 · ¿Los festivos suben la ocupación? (11 min)

```python
# 2.2 · TU TURNO: lo mismo que en la celda 2.1, pero con festivos y normales
resultado = stats.ttest_ind(festivos, normales, equal_var=False)
p_festivo = resultado.pvalue
dif_medias = festivos.mean() - normales.mean()
rechazar_h0 = p_festivo < 0.05
```

**Tiene que salir:**

```text
✅ t de Student: estadístico
✅ t de Student: p-valor
✅ t de Student: diferencia
✅ t de Student: decisión
Diferencia: 16.3 puntos · p = 1.1e-30 → se rechaza H0
```

### Paso 5 · Ejercicio 5 · Quitar el efecto del mes (10 min)

```python
# 5.1 · TU TURNO: el modelo que tiene en cuenta el festivo y el mes
modelo_control = smf.ols("ocupacion_pct ~ temperatura_c + festivo + C(mes)", data=diaria).fit()
coef_temp_simple = modelo_simple.params["temperatura_c"]
coef_temp_control = modelo_control.params["temperatura_c"]
p_temp_control = modelo_control.pvalues["temperatura_c"]
```

**Tiene que salir:**

```text
✅ Confusión: modelo
✅ Confusión: coeficiente simple
✅ Confusión: coeficiente con control
✅ Confusión: p-valor
Sin tener en cuenta el mes: -1.86 puntos por grado
Teniendo en cuenta el mes: -0.09 puntos por grado (p = 0.48)
El efecto del festivo se mantiene: +9.1 puntos (p = 3e-23)
```

---

## S05_06 · CRUD desde Python: leer y cargar datos en una base (en clase)

### Paso 2 · Ejercicio 1 · Leer con pandas (10 min)

```python
# 2.2 · TU TURNO: contar las reservas y lanzar la consulta de la tasa por isla
n_reservas = con.execute("SELECT COUNT(*) FROM reservas").fetchone()[0]

consulta = """
SELECT a.isla,
       ROUND(100.0 * AVG(r.cancelada), 1) AS pct_cancelacion
FROM reservas AS r
JOIN alojamientos AS a ON r.id_alojamiento = a.id_alojamiento
GROUP BY a.isla
ORDER BY a.isla
"""
tasa_por_isla = pd.read_sql_query(consulta, con)
```

**Tiene que salir:**

```text
✅ leer: n_reservas
✅ leer: columnas
✅ leer: una fila por isla
✅ leer: tasa de Tenerife
6000
            isla  pct_cancelacion
0  Fuerteventura             45.6
1   Gran Canaria             46.5
2      La Gomera             46.7
3       La Palma             46.0
4      Lanzarote             45.3
5       Tenerife             46.0
```

### Paso 4 · Ejercicio 3 · Poblar la base con la serie diaria (10 min)

```python
# 4.2 · TU TURNO: leer el CSV, guardarlo en la base y contar las filas desde la base
diaria = pd.read_csv(dato("ocupacion_diaria.csv"))
diaria.to_sql("ocupacion_diaria", con, if_exists="replace", index=False)
n_dias = con.execute("SELECT COUNT(*) FROM ocupacion_diaria").fetchone()[0]
```

**Tiene que salir:**

```text
✅ crear: CSV leído
✅ crear: 1096 filas en la base
✅ crear: columnas
```
