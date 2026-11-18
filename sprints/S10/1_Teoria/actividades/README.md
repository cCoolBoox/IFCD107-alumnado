# Actividades para entender las redes neuronales (S10)

Para cuando los cuadernos «no acaban de verse». Van **antes** o **en paralelo** a S10_01–S10_03 y no necesitan ordenador (salvo el panel).

| Actividad | Qué es | Tiempo | Qué entiendes |
|---|---|:-:|---|
| [`La_red_humana.pdf`](La_red_humana.pdf) | La clase es la red: cada persona es una neurona con una ficha. 4 rondas a mano | 60–75 min | Neurona, capas (XOR), aprender con una tasa, sobreajuste |
| [`panel_de_mandos.html`](panel_de_mandos.html) | Una red de verdad en el navegador, con un mando por concepto (abrir con doble clic; no necesita internet) | 30 min | Qué cambia cada mando (neuronas, tasa, L2, dropout, ruido…) y cómo se ve en las curvas |
| [`Doctor_de_curvas.pdf`](Doctor_de_curvas.pdf) | 9 pacientes: curvas reales de Keras. Diagnostica y receta | 30–40 min | Leer sobreajuste, tasa mal elegida, parada temprana… |
| [`Reto_expres_infografia.pdf`](Reto_expres_infografia.pdf) + [`Reto_expres_plantilla.ipynb`](Reto_expres_plantilla.ipynb) | **Reto en equipo (4 personas):** elegís un problema, entrenáis una red con el cuaderno plantilla, medís y lo presentáis (4 min) | 100 min | Aplicar todo: línea base, métricas honestas, justificar con pruebas |
| [`Mapa_redes_neuronales.pdf`](Mapa_redes_neuronales.pdf) | Una página con los términos agrupados en 3 preguntas | consulta | Dónde encaja cada palabra |

**Orden recomendado:** Mapa (2 min) → La red humana → Panel de mandos → Doctor de curvas → cuadernos S10_01, S10_02, S10_03 → **Reto exprés** (cuando ya habéis visto los tres).

**Del juego al cuaderno:** cada actividad indica qué se llama así en Keras (`Dense`, `learning_rate`, `val_loss`, `Dropout`, `EarlyStopping`). Las soluciones están en el material docente.

_Nota:_ los datos de «La red humana» (R4) están inventados para el juego; las curvas del «Doctor de curvas» son entrenamientos reales con los datos de reservas del curso; el panel de mandos usa datos sintéticos para que todo se vea en una pantalla.
