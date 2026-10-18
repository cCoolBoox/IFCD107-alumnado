#!/usr/bin/env python3
"""Genera el mini dataset SINTÉTICO de tipos de alojamiento (dibujos esquemáticos, NO fotos reales).

Uso:
    python generar_dataset_sintetico.py                       # 60 imágenes por clase en datos_sinteticos/alojamientos
    python generar_dataset_sintetico.py RUTA N RUIDO AMBIGUAS # p. ej. datos_sinteticos/alojamientos 60 40 0.12

Crea la estructura carpeta/<clase>/img_000.png que espera keras.utils.image_dataset_from_directory,
y carpeta/_ambiguas.csv (solo docente: imágenes con etiqueta dudosa a propósito).
NO subir la carpeta generada al repositorio (añadir datos_sinteticos/ al .gitignore).
Requiere numpy y pillow.
"""
import sys
import numpy as np

from PIL import Image, ImageDraw

CLASES_ALOJ = ["hotel", "apartamentos", "casa_rural", "camping", "piscina"]
CLASES_FORMAS = ["rayas_horizontales", "rayas_verticales", "diagonales", "cuadricula", "puntos", "circulo", "rectangulo", "triangulo"]


def _color(rng, base, var=30):
    """Color aleatorio cercano a `base` (tupla RGB)."""
    return tuple(int(np.clip(c + rng.integers(-var, var + 1), 0, 255)) for c in base)


def _final(img, rng, ruido=8):
    """Convierte a uint8 con un poco de ruido y variación de brillo."""
    a = np.asarray(img, dtype="float32") * rng.uniform(0.85, 1.15)
    a = a + rng.normal(0, ruido, a.shape)
    return np.clip(a, 0, 255).astype("uint8")


def _ventanas(d, x0, y0, x1, y1, filas, cols, color, margen):
    """Cuadrícula de ventanas dentro del rectángulo (x0, y0, x1, y1)."""
    ancho, alto = (x1 - x0) / cols, (y1 - y0) / filas
    for f in range(filas):
        for c in range(cols):
            a, b = x0 + c * ancho + margen * ancho, y0 + f * alto + margen * alto
            d.rectangle([a, b, a + ancho * (1 - 2 * margen), b + alto * (1 - 2 * margen)], fill=color)


def dibujar_alojamiento(clase, rng, tam=48, ruido=8):
    """Dibujo esquemático (tam×tam×3, uint8) de un tipo de alojamiento. Datos SINTÉTICOS, no fotos reales."""
    E = 3                                   # supermuestreo para suavizar bordes
    S = tam * E
    img = Image.new("RGB", (S, S), _color(rng, (170, 205, 235), 25))          # cielo
    d = ImageDraw.Draw(img)
    if rng.random() < 0.5:                                                    # sol opcional
        cx, cy, r = rng.uniform(0.1, 0.9) * S, rng.uniform(0.08, 0.25) * S, rng.uniform(0.05, 0.08) * S
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(250, 235, 120))
    hor = rng.uniform(0.62, 0.72) * S                                         # línea del horizonte
    verde = _color(rng, (120, 170, 90), 25)
    if clase == "piscina":
        d.rectangle([0, hor * 0.6, S, S], fill=_color(rng, (225, 210, 170), 15))   # terraza
        x0, x1 = rng.uniform(0.08, 0.2) * S, rng.uniform(0.75, 0.92) * S
        y0, y1 = rng.uniform(0.5, 0.58) * S, rng.uniform(0.82, 0.94) * S
        d.rectangle([x0 - 3, y0 - 3, x1 + 3, y1 + 3], fill=(245, 245, 245))
        d.rectangle([x0, y0, x1, y1], fill=_color(rng, (60, 150, 210), 20))
        for k in range(3):
            yy = y0 + (k + 1) * (y1 - y0) / 4
            d.line([x0 + 6, yy, x1 - 6, yy], fill=(150, 210, 240), width=2)
        for k in range(2):                                                    # tumbonas
            tx = rng.uniform(0.1, 0.8) * S
            d.rectangle([tx, hor * 0.72, tx + 0.1 * S, hor * 0.72 + 0.04 * S], fill=_color(rng, (240, 120, 60), 30))
    else:
        d.rectangle([0, hor, S, S], fill=verde)                                # césped
    if clase == "hotel":
        w, h = rng.uniform(0.30, 0.42) * S, rng.uniform(0.5, 0.66) * S
        x0 = rng.uniform(0.1 * S, 0.9 * S - w); y0 = hor - h + 0.05 * S
        d.rectangle([x0, y0, x0 + w, hor + 0.05 * S], fill=_color(rng, (220, 200, 170)))
        _ventanas(d, x0, y0 + 0.02 * S, x0 + w, hor, int(rng.integers(4, 6)), 3, (60, 90, 140), 0.22)
    elif clase == "apartamentos":
        w, h = rng.uniform(0.7, 0.86) * S, rng.uniform(0.28, 0.38) * S
        x0 = rng.uniform(0.02 * S, 0.98 * S - w); y0 = hor - h + 0.05 * S
        d.rectangle([x0, y0, x0 + w, hor + 0.05 * S], fill=_color(rng, (235, 225, 205)))
        _ventanas(d, x0, y0, x0 + w, hor + 0.05 * S, 2, int(rng.integers(5, 7)), (70, 100, 150), 0.25)
        for k in (1, 2):                                                       # balcones (líneas horizontales)
            yy = y0 + k * (hor + 0.05 * S - y0) / 2
            d.line([x0, yy, x0 + w, yy], fill=(120, 110, 100), width=2)
    elif clase == "casa_rural":
        w, h = rng.uniform(0.32, 0.44) * S, rng.uniform(0.2, 0.28) * S
        x0 = rng.uniform(0.1 * S, 0.9 * S - w); y0 = hor - h + 0.05 * S
        d.rectangle([x0, y0, x0 + w, hor + 0.05 * S], fill=_color(rng, (235, 225, 200)))
        d.polygon([(x0 - 0.04 * S, y0), (x0 + w + 0.04 * S, y0), (x0 + w / 2, y0 - rng.uniform(0.14, 0.2) * S)],
                  fill=_color(rng, (170, 70, 50), 25))
        d.rectangle([x0 + w * 0.42, y0 + h * 0.4, x0 + w * 0.58, hor + 0.05 * S], fill=(110, 70, 40))
        d.rectangle([x0 + w * 0.1, y0 + h * 0.2, x0 + w * 0.3, y0 + h * 0.5], fill=(70, 100, 150))
    elif clase == "camping":
        d.rectangle([0, hor - 0.08 * S, S, S], fill=verde)
        w, h = rng.uniform(0.34, 0.5) * S, rng.uniform(0.28, 0.4) * S
        x0 = rng.uniform(0.05 * S, 0.95 * S - w); base = hor + 0.1 * S
        c = _color(rng, [(240, 140, 40), (60, 120, 200), (230, 200, 60)][int(rng.integers(0, 3))], 20)
        d.polygon([(x0, base), (x0 + w, base), (x0 + w / 2, base - h)], fill=c)
        d.polygon([(x0 + w * 0.4, base), (x0 + w * 0.6, base), (x0 + w / 2, base - h * 0.5)], fill=(50, 40, 40))
    if clase != "piscina" and rng.random() < 0.6:                              # árbol de adorno
        tx = rng.choice([rng.uniform(0.03, 0.12), rng.uniform(0.88, 0.97)]) * S
        d.rectangle([tx - 2, hor - 0.02 * S, tx + 2, hor + 0.12 * S], fill=(100, 70, 40))
        d.ellipse([tx - 0.07 * S, hor - 0.16 * S, tx + 0.07 * S, hor + 0.01 * S], fill=(50, 120, 60))
    return _final(img.resize((tam, tam), Image.LANCZOS), rng, ruido)


def dibujar_forma(clase, rng, tam=48):
    """Formas y texturas abstractas (tarea auxiliar de preentrenamiento). Devuelve tam×tam×3 uint8."""
    fondo, tinta = _color(rng, (rng.integers(20, 235),) * 3, 20), _color(rng, tuple(int(v) for v in rng.integers(0, 256, 3)), 10)
    if np.abs(np.array(fondo, dtype=int) - np.array(tinta, dtype=int)).sum() < 150:      # asegura contraste
        tinta = tuple(255 - c for c in fondo)
    E = 2
    S = tam * E
    img = Image.new("RGB", (S, S), fondo)
    d = ImageDraw.Draw(img)
    paso = int(rng.integers(6, 12)) * E
    off = int(rng.integers(0, paso))
    if clase == "rayas_horizontales":
        for y in range(off, S, paso): d.rectangle([0, y, S, y + paso // 2], fill=tinta)
    elif clase == "rayas_verticales":
        for x in range(off, S, paso): d.rectangle([x, 0, x + paso // 2, S], fill=tinta)
    elif clase == "diagonales":
        for k in range(-S, S, paso): d.line([k + off, 0, k + off + S, S], fill=tinta, width=max(2, paso // 3))
    elif clase == "cuadricula":
        for y in range(off, S, paso): d.line([0, y, S, y], fill=tinta, width=2)
        for x in range(off, S, paso): d.line([x, 0, x, S], fill=tinta, width=2)
    elif clase == "puntos":
        r = max(2, paso // 4)
        for y in range(off, S, paso):
            for x in range(off, S, paso): d.ellipse([x - r, y - r, x + r, y + r], fill=tinta)
    else:
        r = rng.uniform(0.18, 0.38) * S
        cx, cy = rng.uniform(r, S - r), rng.uniform(r, S - r)
        if clase == "circulo": d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=tinta)
        elif clase == "rectangulo": d.rectangle([cx - r, cy - r * rng.uniform(0.5, 1), cx + r, cy + r * rng.uniform(0.5, 1)], fill=tinta)
        else: d.polygon([(cx - r, cy + r), (cx + r, cy + r), (cx, cy - r)], fill=tinta)
    return _final(img.resize((tam, tam), Image.LANCZOS), rng)


def generar_lote(funcion, clases, n_por_clase, semilla=42, tam=48):
    """Devuelve (X uint8 [n, tam, tam, 3], y int [n]) con n_por_clase imágenes por clase, mezcladas."""
    rng = np.random.default_rng(semilla)
    X = np.stack([funcion(c, rng, tam) for c in clases for _ in range(n_por_clase)])
    y = np.repeat(np.arange(len(clases)), n_por_clase)
    orden = rng.permutation(len(y))
    return X[orden], y[orden]


PARECIDAS = {"hotel": "apartamentos", "apartamentos": "hotel", "casa_rural": "camping", "camping": "casa_rural", "piscina": "camping"}


def crear_dataset_carpetas(carpeta, n_por_clase=100, semilla=7, tam=48, ruido=8, prop_ambiguas=0.0):
    """Escribe PNG en carpeta/<clase>/img_000.png (estructura que espera image_dataset_from_directory).

    prop_ambiguas: fracción de imágenes cuyo dibujo corresponde a una clase parecida (PARECIDAS) pero se guarda
    en la carpeta de la otra: simula etiquetas dudosas o erróneas. Se anotan en carpeta/_ambiguas.csv (solo docente).
    """
    import os
    rng = np.random.default_rng(semilla)
    ambiguas = []
    for clase in CLASES_ALOJ:
        os.makedirs(os.path.join(carpeta, clase), exist_ok=True)
        for i in range(n_por_clase):
            dibujo = PARECIDAS[clase] if rng.random() < prop_ambiguas else clase
            if dibujo != clase:
                ambiguas.append(f"{clase}/img_{i:03d}.png,{dibujo}")
            Image.fromarray(dibujar_alojamiento(dibujo, rng, tam, ruido)).save(os.path.join(carpeta, clase, f"img_{i:03d}.png"))
    with open(os.path.join(carpeta, "_ambiguas.csv"), "w") as f:
        f.write("archivo,dibujo_real\n" + "\n".join(ambiguas) + "\n")
    return carpeta


if __name__ == "__main__":
    ruta = sys.argv[1] if len(sys.argv) > 1 else "datos_sinteticos/alojamientos"
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 60
    ruido = float(sys.argv[3]) if len(sys.argv) > 3 else 40
    amb = float(sys.argv[4]) if len(sys.argv) > 4 else 0.12
    crear_dataset_carpetas(ruta, n_por_clase=n, semilla=7, tam=48, ruido=ruido, prop_ambiguas=amb)
    print(f"Dataset sintético creado en {ruta}: {n} imágenes por clase ({', '.join(CLASES_ALOJ)})")
