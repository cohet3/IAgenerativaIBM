from flask import Flask, render_template, request, jsonify
import pyttsx3
import threading
import os

app = Flask(__name__)

# Inicializar el motor de pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Velocidad de la voz
engine.setProperty('volume', 1)  # Volumen de la voz


def speak(text):
    """Función para convertir texto a voz y guardar el audio en un archivo."""
    output_file = 'static/output.mp3'
    engine.save_to_file(text, output_file)
    engine.runAndWait()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text')
        if text:
            # Ejecutar la conversión en un hilo separado
            threading.Thread(target=speak, args=(text,)).start()
            return jsonify({'status': 'success', 'audio_url': '/static/output.mp3'})
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
