# Necesito crear un gráfico en un servicio con Flask uitilizando Matplotlib y Pandas , a partir de la inflación media de los últimos 20 años en españa.
from flask import Flask, render_template, Response
import pandas as pd
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

# Datos ficticios de inflación para España, Francia, Alemania e Italia
data = {
    'Year': [i for i in range(2004, 2024)],
    'Spain': [3.0, 2.5, 3.5, 1.0, 2.0, 1.5, 0.5, 2.1, 2.7, 1.8, 1.3, 1.0, 0.7, 1.2, 1.6, 1.8, 0.6, 0.9, 1.1, 0.8],
    'France': [2.5, 2.0, 2.8, 0.8, 1.5, 1.3, 0.4, 1.9, 2.4, 1.6, 1.1, 0.9, 0.5, 1.0, 1.4, 1.6, 0.5, 0.7, 0.9, 0.7],
    'Germany': [1.8, 1.6, 2.2, 0.7, 1.2, 1.1, 0.3, 1.5, 2.0, 1.4, 1.0, 0.8, 0.4, 0.9, 1.2, 1.4, 0.4, 0.6, 0.8, 0.6],
    'Italy': [2.1, 1.9, 2.6, 0.9, 1.4, 1.2, 0.4, 1.7, 2.2, 1.5, 1.1, 0.9, 0.6, 1.1, 1.5, 1.7, 0.6, 0.8, 1.0, 0.8]
}
df = pd.DataFrame(data)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/plot.png')
def plot_png():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Graficar la inflación de cada país con diferentes estilos
    ax.plot(df['Year'], df['Spain'], marker='o', linestyle='-', color='blue', label='España')
    ax.plot(df['Year'], df['France'], marker='s', linestyle='--', color='green', label='Francia')
    ax.plot(df['Year'], df['Germany'], marker='^', linestyle='-.', color='red', label='Alemania')
    ax.plot(df['Year'], df['Italy'], marker='D', linestyle=':', color='purple', label='Italia')

    ax.set_title('Inflación Media en España, Francia, Alemania e Italia (Últimos 20 años)')
    ax.set_xlabel('Año')
    ax.set_ylabel('Inflación (%)')
    ax.legend()
    ax.grid(True)

    # Ajuste de márgenes y diseño
    plt.tight_layout()

    # Guardar el gráfico en un objeto bytes
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)

    return Response(img.getvalue(), mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)

# Para agregar la inflación de otros países como Francia, Alemania e Italia y visualizarlas en el mismo gráfico, puedes seguir estos pasos. Modificaré el ejemplo anterior para incluir los datos de inflación de estos países y mostrarlos en el mismo gráfico.
