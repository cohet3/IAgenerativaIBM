from flask import Flask, render_template, redirect, request, session
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
import config

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Cambia esto por una clave secreta segura

# Configurar la autenticación de Spotipy
sp = Spotify(auth_manager=SpotifyClientCredentials(
    client_id=config.SPOTIPY_CLIENT_ID,
    client_secret=config.SPOTIPY_CLIENT_SECRET
))


def get_top_tracks():
    results = sp.search(q='genre:"pop"', type='track', limit=20)
    tracks = results['tracks']['items']
    return tracks


@app.route('/')
def index():
    tracks = get_top_tracks()
    return render_template('index.html', tracks=tracks)


if __name__ == '__main__':
    app.run(debug=True)
