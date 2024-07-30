from flask import Flask, render_template, request
import speech_recognition as sr
import os

app = Flask(__name__)

# Configuración de la ruta para guardar los archivos subidos
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Asegúrate de que la carpeta de uploads existe
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def convert_audio_to_text(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        try:
            # Usar el reconocimiento en español
            text = recognizer.recognize_google(audio, language='es-ES')
            return text
        except sr.UnknownValueError:
            return "No se pudo entender el audio"
        except sr.RequestError:
            return "Error en la solicitud a Google Speech Recognition"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', text="No se ha subido ningún archivo")

        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', text="No se ha seleccionado ningún archivo")

        if file and file.filename.endswith('.mp3'):
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            text = convert_audio_to_text(file_path)
            return render_template('index.html', text=text)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
