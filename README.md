# 😊 Reconocimiento de Emociones en Tiempo Real (PC + ESP32)

Proyecto que detecta emociones faciales en tiempo real usando la cámara web de la computadora, con **OpenCV** y **DeepFace**.

## 📌 Características

- Captura de video en vivo desde la webcam.
- Detección de la emoción dominante en cada fotograma (feliz, triste, enojado, sorprendido, neutral, miedo, asco).
- Visualización de la emoción sobre la ventana de video y en la consola.
- Ejecución en un entorno virtual de Python.

## 🧰 Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| [Python 3.9 - 3.11](https://www.python.org/) | Lenguaje principal |
| [OpenCV](https://opencv.org/) | Captura y visualización de video |
| [DeepFace](https://github.com/serengil/deepface) | Reconocimiento de emociones con IA |
| [tf-keras](https://pypi.org/project/tf-keras/) | Compatibilidad de TensorFlow con DeepFace |
| ESP32 | Mostrar la emoción en una pantalla |

## ✅ Requisitos previos

- Python 3.9, 3.10 o 3.11 instalado (se recomienda marcar *"Add Python to PATH"* al instalar).
- Una webcam funcional.
- Visual Studio Code (opcional, pero recomendado).
- Conexión a internet en la primera ejecución, ya que DeepFace descarga los modelos de IA.

## 🚀 Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/moonthang/emociones-eps32.git
   cd emociones-esp32
   ```

2. **Crea el entorno virtual:**

   ```bash
   python -m venv venv
   ```

3. **Activa el entorno virtual:**

   - Windows (PowerShell):
     ```powershell
     .\venv\Scripts\Activate
     ```
   - Windows (CMD):
     ```cmd
     venv\Scripts\activate.bat
     ```
   - Linux / macOS:
     ```bash
     source venv/bin/activate
     ```

   Sabrás que funcionó porque aparecerá `(venv)` al inicio de la línea de la terminal.

4. **Instala las dependencias:**

   ```bash
   pip install opencv-python deepface tf-keras
   ```

   > ⏳ La instalación puede tardar unos minutos.

> 💡 **Nota (PowerShell):** si te aparece un error de permisos al activar el entorno, ejecuta una vez:
> `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`

## ▶️ Uso

Con el entorno virtual activado, ejecuta:

```bash
python main.py
```

- Se abrirá una ventana con la imagen de tu cámara.
- La emoción detectada aparecerá en la ventana y en la terminal.
- Presiona **`q`** para salir.

> La primera ejecución puede tardar unos segundos mientras DeepFace descarga y carga los modelos.

## 📁 Estructura del proyecto

```
emociones-esp32/
├── main.py          # Script principal de reconocimiento de emociones
├── README.md        # Documentación del proyecto
├── .gitignore       # Archivos ignorados por Git
└── venv/            # Entorno virtual (no se sube a GitHub)
```

## 🧠 ¿Cómo funciona?

1. OpenCV captura un fotograma de la webcam.
2. DeepFace analiza el fotograma con `DeepFace.analyze(..., actions=['emotion'])`.
3. Se obtiene la emoción dominante (`dominant_emotion`).
4. La emoción se dibuja sobre el video y se imprime en la consola.

## 🛠️ Solución de problemas

| Problema | Posible solución |
|---|---|
| `No se pudo acceder a la webcam` | Cierra otras aplicaciones que usen la cámara o cambia `VideoCapture(0)` por `VideoCapture(1)`. |
| Error al activar el entorno en PowerShell | Revisa la nota de permisos en la sección de instalación. |
| El video va lento | El análisis con IA es pesado; cierra otros programas o analiza un fotograma de cada varios. |
| Error con TensorFlow / Keras | Verifica que `tf-keras` esté instalado y que uses Python 3.9 - 3.11. |

## 🗺️ Roadmap

- [x] Reconocimiento de emociones en la PC con webcam.
- [ ] Enviar la emoción detectada al ESP32 (Serial / WiFi).
- [ ] Mostrar la emoción en una pantalla conectada al ESP32.
- [ ] Optimizar el rendimiento (analizar cada N fotogramas).
