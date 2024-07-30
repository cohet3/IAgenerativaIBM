from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import io

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        dni = request.form['dni']
        localidad = request.form['localidad']

        # Crear el PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Informacion de la Persona", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Nombre: {nombre}", ln=True)
        pdf.cell(200, 10, txt=f"Apellido: {apellido}", ln=True)
        pdf.cell(200, 10, txt=f"Edad: {edad}", ln=True)
        pdf.cell(200, 10, txt=f"DNI: {dni}", ln=True)
        pdf.cell(200, 10, txt=f"Localidad: {localidad}", ln=True)

        # Guardar el PDF en un archivo temporal y luego cargarlo en un objeto BytesIO
        pdf_output = io.BytesIO()
        pdf_output_bytes = pdf.output(dest='S').encode('latin1')
        pdf_output.write(pdf_output_bytes)
        pdf_output.seek(0)

        # Enviar el PDF como descarga
        return send_file(pdf_output, as_attachment=True, download_name='informacion_persona.pdf',
                         mimetype='application/pdf')

    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
