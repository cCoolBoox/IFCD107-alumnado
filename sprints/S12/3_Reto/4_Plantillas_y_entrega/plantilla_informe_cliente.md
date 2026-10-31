# Informe de reseñas · TurisData Canarias
*Equipo: … · Fecha: … · Datos: `resenas.csv` (sintéticos, 1.500 reseñas)*

> **Qué parte es de qué nivel.** 🟢 **Mínimo** (obligatorio): apartados 1 y 2. 🟡 **Estándar**: además, la exactitud en prueba (apartado 2), el apartado 4 completo (3 recomendaciones) y el 5. 🔴 **Extra**: el apartado 3 (temas con cifras y ejemplos). Máximo 2 páginas. Borrad esta nota al entregar.

## 1. Resumen para la dirección (3 líneas) · 🟢
- Qué opina la clientela en general (cifras): …
- Lo que más se critica y lo que más se valora: …
- Lo que recomendamos hacer primero: …

## 2. Sentimiento · 🟢 (la exactitud en prueba, 🟡)
Gráfico: reparto positivo / neutro / negativo (`grafico_resenas.png`). Porcentajes: … % positivas · … % neutras · … % negativas.

Tres citas reales (con su `id_resena`):
1. «…» (`id_resena`: …)
2. «…» (`id_resena`: …)
3. «…» (`id_resena`: …)

🟡 Exactitud del clasificador en prueba: … (y qué significa para el cliente).

## 3. Temas · 🔴
| Tema | Reseñas negativas | Reseñas positivas | Ejemplo real |
|---|---|---|---|
| … | … | … | «…» |

Gráfico: quejas por tema. Expresiones que se repiten (n-gramas): …

## 4. Recomendaciones (3, accionables) · 🟡
1. **Qué:** … **Quién:** … **Cómo sabremos que funciona:** …
2. …
3. …

*(En el nivel mínimo basta con la recomendación del apartado 1.)*

## 5. Límites y cautelas · 🟡
- Datos sintéticos; reseñas más repetitivas que las reales.
- El método no entiende ironía ni negaciones (ejemplo: …).
- Datos personales: cómo se tratarían en una versión real.
