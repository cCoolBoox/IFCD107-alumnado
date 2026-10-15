# 🤖 Cómo usar un modelo de lenguaje gratis en tu proyecto

**Solo para el reto del asistente con IA conversacional (brief 3).** Si tu equipo elige otro reto, no necesitas nada de esto.

Un asistente con IA necesita un **modelo de lenguaje**: el «cerebro» que escribe las respuestas. Lo vamos a usar **por internet, con una clave gratuita**. Esta guía te lleva paso a paso.

---

## Antes de empezar: 3 reglas

1. **La clave es como una contraseña.** No se escribe dentro del cuaderno, no se sube a GitHub y no se comparte por el grupo. Abajo verás dónde guardarla.
2. **Nunca envíes datos personales** (nombres reales, DNI, teléfonos, correos). Usa solo los datos de prueba del reto.
3. **Cada persona crea su propia cuenta y su propia clave.** Los límites gratuitos son por cuenta o proyecto, no por equipo.

---

## Elige una opción

| Opción | Cuenta que necesitas | Tarjeta | Ventaja | Cuidado |
|---|---|---|---|---|
| 🟢 **A · Google Gemini** | La de Google que ya tienes | No | La más fácil de empezar | Límite de peticiones bajo |
| 🟢 **B · Groq** | Alta nueva (gratis) | No | Muy rápido y más peticiones al día | Cuenta nueva |
| 🟡 **C · OpenRouter** | Alta nueva (gratis) | No verificado | Da acceso a muchos modelos, entre ellos DeepSeek y Qwen | Solo 50 peticiones al día en gratis |

**Recomendación:** empieza por la **A**. Si te quedas sin peticiones, pasa a la **B**. La **C** es la tercera opción.

> ⚠️ **Los límites gratuitos pueden cambiar sin aviso.** Si un día no funciona, avisa al docente: puede ser que se haya acabado tu cuota del día, no que hayas hecho algo mal.

---

## Paso previo (para las tres): dónde guardar tu clave en Colab

Colab tiene una «caja fuerte» llamada **Secretos**. La clave se guarda ahí y el cuaderno la lee sin mostrarla.

1. Abre tu cuaderno en Colab.
2. En la barra de la izquierda pulsa el icono de la **llave 🔑** (*Secretos*).
3. Pulsa **«Añadir secreto nuevo»**.
4. En **Nombre** escribe el que te indica la opción (por ejemplo `GEMINI_API_KEY`) y en **Valor** pega tu clave.
5. Activa el interruptor **«Acceso desde el cuaderno»**.

---

## 🟢 Opción A · Google Gemini

**1. Consigue la clave**
1. Entra en <https://aistudio.google.com/api-keys> con tu cuenta de Google.
2. Pulsa **«Create API key»** (Crear clave de API). Si ya aparece una creada, puedes usarla.
3. **Copia la clave** y guárdala en Secretos con el nombre `GEMINI_API_KEY`.

**2. Pruébala en Colab**
```python
!pip install -q -U google-genai

from google import genai
from google.colab import userdata

client = genai.Client(api_key=userdata.get("GEMINI_API_KEY"))

respuesta = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explica en dos frases qué es un modelo de lenguaje."
)
print(respuesta.output_text)
```
Si ves una respuesta en pantalla, **ya funciona**.

**Si falla:** el nombre del modelo cambia con el tiempo. Copia el actual del ejemplo de <https://ai.google.dev/gemini-api/docs/quickstart>.

**Qué debes saber:** el uso gratuito **no necesita tarjeta**. El límite se cuenta **por proyecto de Google**, y se reinicia cada día a medianoche (hora del Pacífico). Los datos que envíes pueden usarse para mejorar productos de Google, salvo en la UE, Reino Unido y Espacio Económico Europeo: por eso, **nada de datos personales**.

---

## 🟢 Opción B · Groq

**1. Crea la cuenta y la clave**
1. Entra en <https://console.groq.com> y regístrate (con tu correo o con tu cuenta de Google).
2. Ve a <https://console.groq.com/keys> y pulsa **«Create API Key»**.
3. Ponle un nombre (por ejemplo `curso-ifcd107`), **copia la clave** (solo se muestra una vez) y guárdala en Secretos como `GROQ_API_KEY`.

**2. Pruébala en Colab**
```python
!pip install -q groq

from groq import Groq
from google.colab import userdata

client = Groq(api_key=userdata.get("GROQ_API_KEY"))

respuesta = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "Explica en dos frases qué es un modelo de lenguaje."}],
)
print(respuesta.choices[0].message.content)
```

**Si falla:** pasa lo mismo que con Gemini: los modelos se renuevan. Mira la lista actual en <https://console.groq.com/docs/models> y cambia el nombre en `model=`.

**Qué debes saber:** el plan gratuito **no pide tarjeta**. Los límites de tu cuenta están en <https://console.groq.com/settings/limits>. Cuando te quedes sin cuota verás un error de «rate limit»: espera un poco o pasa a otra opción.

---

## 🟡 Opción C · OpenRouter (y cómo acceder a DeepSeek y Qwen)

OpenRouter es como una **«centralita»**: con una sola cuenta puedes probar modelos de muchas empresas, **incluidos DeepSeek y Qwen**. Los modelos gratuitos llevan **`:free`** al final del nombre.

**1. Crea la cuenta y la clave**
1. Entra en <https://openrouter.ai> y regístrate.
2. Ve a <https://openrouter.ai/keys>, crea una clave y guárdala en Secretos como `OPENROUTER_API_KEY`.
3. En <https://openrouter.ai/models> filtra por **«Free»** y elige un modelo. Copia su nombre completo (termina en `:free`).

**2. Pruébala en Colab**
```python
!pip install -q openai

from openai import OpenAI
from google.colab import userdata

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=userdata.get("OPENROUTER_API_KEY"),
)

respuesta = client.chat.completions.create(
    model="PEGA_AQUÍ_EL_NOMBRE_DEL_MODELO:free",
    messages=[{"role": "user", "content": "Explica en dos frases qué es un modelo de lenguaje."}],
)
print(respuesta.choices[0].message.content)
```

**Qué debes saber:** el uso gratuito permite **20 peticiones por minuto y 50 al día**. Los modelos gratuitos cambian o desaparecen sin aviso. Si el modelo ya no existe, elige otro de la lista.

---

## ❓ ¿Y DeepSeek y Qwen directamente?

Son modelos muy buenos, pero **no usamos sus servicios oficiales en el curso**:
- **DeepSeek (su propia web y su API):** es de **pago** (se carga saldo) y no hay una opción gratuita clara. Sus servidores están fuera de la UE.
- **Qwen (la nube de Alibaba):** requiere una cuenta de Alibaba Cloud y no se garantiza que el uso gratuito se mantenga.

**Mejor camino:** usa estos modelos **a través de OpenRouter** (opción C), o descarga una versión pequeña y ejecútala **en tu propio Colab**, sin enviar nada fuera. El docente os indicará qué modelos pequeños funcionan bien.

---

## 🛡️ ¿Qué hago con los embeddings (la búsqueda de documentos)?

En un asistente con RAG, el trabajo de **buscar el fragmento correcto** lo hacemos con la librería `sentence-transformers` **en tu propio Colab**, sin gastar ninguna cuota. El servicio en internet **solo escribe la respuesta final**.

---

## 🆘 Si algo no funciona

| Me pasa esto | Qué hago |
|---|---|
| Error «401» o «invalid API key» | La clave está mal copiada o no está activado el interruptor de Secretos |
| Error «429» o «rate limit» | Se acabó la cuota. Espera, o prueba otra opción |
| «Model not found» | El modelo ya no existe. Cambia el nombre por uno de la lista actual |
| Me pide una tarjeta | **No la des.** Avisa al docente |
| No sé si el dato que voy a enviar es personal | Pregunta antes. Si dudas, no lo envíes |
