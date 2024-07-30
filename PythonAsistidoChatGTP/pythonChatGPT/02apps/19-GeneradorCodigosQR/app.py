import os

import qrcode
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Directorio para guardar los códigos QR generados
QR_DIRECTORY = 'static/qr_codes'
os.makedirs(QR_DIRECTORY, exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        return redirect(url_for('generate_qr', url=url))
    return render_template('index.html')


@app.route('/generate_qr')
def generate_qr():
    url = request.args.get('url')

    # Generar el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Guardar la imagen en un archivo
    img_path = os.path.join(QR_DIRECTORY, 'qrcode.png')
    img.save(img_path)

    return render_template('qr.html', url=url, img_path=img_path)


if __name__ == '__main__':
    app.run(debug=True)

# Quiero crear un servicio web con Flask Qrcode para generar un código QR a partir de un enlace, el resultado se verá en otra página del servicio donde podremos ver la URL y la imagen del código QR generado. Añadele unos estilos CSS modernos al html
# pip install qrcode -> tuve que instalarlo varias veces pare que funcione.
