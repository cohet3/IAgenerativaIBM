from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Configuración de la API de OpenAI
openai.api_key = ''  # Reemplaza con tu propia clave API de OpenAI


def obtener_respuesta(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Modelo GPT-3.5-turbo de OpenAI
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content'].strip()


@app.route('/', methods=['GET', 'POST'])
def index():
    respuesta = None
    if request.method == 'POST':
        mensaje = request.form['mensaje']
        respuesta = obtener_respuesta(mensaje)

    return render_template('index.html', respuesta=respuesta)


if __name__ == '__main__':
    app.run(debug=True)
