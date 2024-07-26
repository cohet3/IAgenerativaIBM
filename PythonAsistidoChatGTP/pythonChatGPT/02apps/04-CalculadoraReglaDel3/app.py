from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            num3 = float(request.form['num3'])
            resultado = (num2 * num3) / num1
        except ValueError:
            resultado = 'Error: Por favor, ingrese números válidos.'

    return render_template('index.html', resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)
