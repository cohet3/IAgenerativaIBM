# vamos a utilizar la api de APILayer podrias hacerme un ejemplo de conversor de divisas funcionando en un servicio web con FLask donde puedas seleccionar de una lista Euros, Dólares, yuanes y yenes, que todo funcione en una única plantilla index.html

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'RwqUQsXVSegSIauA9C00vNFlTlJnI1a3'  # Reemplaza con tu propia API Key de APILayer
API_URL = 'https://api.apilayer.com/exchangerates_data/latest'

currencies = ['EUR', 'USD', 'CNY', 'JPY']


def obtener_tasa_de_cambio(base, symbols):
    url = f"{API_URL}?symbols={symbols}&base={base}"
    headers = {
        "apikey": API_KEY
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    if 'rates' in data:
        return data['rates'][symbols]
    else:
        return None


@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        cantidad = float(request.form['cantidad'])
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        tasa_de_cambio = obtener_tasa_de_cambio(from_currency, to_currency)
        if tasa_de_cambio:
            resultado = cantidad * tasa_de_cambio

    return render_template('index.html', currencies=currencies, resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)
