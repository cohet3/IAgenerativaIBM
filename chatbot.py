
# Importar las bibliotecas necesarias
from flask import Flask, render_template, request, jsonify, send_file, render_template_string
from ibm_watson import SpeechToTextV1, TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import openai
from dotenv import load_dotenv
from io import BytesIO  # Importación de BytesIO para manejar datos binarios en memoria
import os

# Cargar variables de entorno (claves API) desde el archivo .env
load_dotenv('claves.env')

app = Flask(__name__)

# Credenciales de IBM Watson Speech to Text
stt_authenticator = IAMAuthenticator(os.getenv('SPEECH_TO_TEXT_APIKEY'))
speech_to_text = SpeechToTextV1(authenticator=stt_authenticator)
speech_to_text.set_service_url(os.getenv('SPEECH_TO_TEXT_URL'))

# Credenciales de IBM Watson Text to Speech
tts_authenticator = IAMAuthenticator(os.getenv('TEXT_TO_SPEECH_APIKEY'))
text_to_speech = TextToSpeechV1(authenticator=tts_authenticator)
text_to_speech.set_service_url(os.getenv('TEXT_TO_SPEECH_URL'))

# Credenciales de OpenAI
#client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    # Ruta para la página principal
    # Renderiza el archivo index.html ubicado en el directorio templates
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    # ruta para manejar la transcripcion de audio a texto
    # Recibe un archivo de audio a través de una solicitud POST
    audio = request.files['audio']
    # Utiliza el servicio Speech to Text de IBM Watson para reconocer el audio
    stt_result = speech_to_text.recognize(
        audio=audio, # El archivo de audio recibido
        content_type='audio/wav', # Tipo de contenido del archivo de audio
        model='es-ES_BroadbandModel' # Modelo de idioma utilizado para la transcripción
    ).get_result()

    # Extrae el texto transcrito del resultado de la API
    transcript = stt_result['results'][0]['alternatives'][0]['transcript']

    # Devuelve el texto transcrito en formato JSON
    return jsonify({'transcript': transcript})

@app.route('/chat', methods=['POST'])
def chat():
    # Ruta para manejar las solicitudes de chat
    # Recibe un mensaje de usuario a través de una solicitud POST
    user_input = request.json['message']

    # Mensaje de depuración para verificar la entrada del usuario
    print("Mensaje del usuario:", user_input)

    # Utiliza el servicio de OpenAI para generar una respuesta
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Modelo de GPT-3.5 Turbo utilizado para generar la respuesta
            messages=[{"role": "user", "content": user_input}]  # Mensaje del usuario en formato de chat
        )

        # Mensaje de depuración para verificar la respuesta de OpenAI
        print("Respuesta de OpenAI:", response.choices[0].message['content'].strip())

        # Devuelve la respuesta generada en formato JSON
        return jsonify({'response': response.choices[0].message['content'].strip()})
    except Exception as e:
        print("Error al generar la respuesta de OpenAI:", e)
        return jsonify({'response': 'Lo siento, no puedo procesar tu solicitud en este momento.'})

@app.route('/speak', methods=['POST'])
def speak():
    # Ruta para manejar la conversión de texto a voz
    # Recibe un texto a través de una solicitud POST
    text = request.json['text']
    
    # Mensaje de depuración para verificar el texto recibido
    print("Texto recibido para sintetizar:", text)
    
    # Utiliza el servicio Text to Speech de IBM Watson para sintetizar el texto
    try:
        tts_result = text_to_speech.synthesize(
            text,  # El texto recibido
            voice='es-ES_LauraV3Voice',  # Voz utilizada para la síntesis
            accept='audio/wav'  # Tipo de contenido de la respuesta (archivo de audio OGG) 
        ).get_result()
        
        # Extrae el contenido de audio de la respuesta de la API
        audio = tts_result.content

        # Mensaje de depuración para verificar la longitud del audio
        print("Audio generado, longitud:", len(audio))
        
        # Devuelve el contenido de audio como respuesta
        return send_file(BytesIO(audio), mimetype='audio/wav')
    except Exception as e:
        print("Error al generar el audio:", e)
        return jsonify({'response': 'Lo siento, no puedo procesar tu solicitud en este momento.'})

if __name__ == '__main__':
    # Inicia la aplicación Flask en modo de depuración
    app.run(debug=True)

