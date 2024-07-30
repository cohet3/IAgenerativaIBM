from flask import Flask, render_template, abort
import requests

app = Flask(__name__)

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon"
LIMIT = 151


def get_pokemon_list():
    response = requests.get(f"{POKEAPI_URL}?limit={LIMIT}")
    if response.status_code == 200:
        data = response.json()
        return [{"id": i + 1, "name": p["name"].capitalize()} for i, p in enumerate(data["results"])]
    else:
        return []


def get_pokemon_details(pokemon_id):
    response = requests.get(f"{POKEAPI_URL}/{pokemon_id}")
    if response.status_code == 200:
        data = response.json()
        pokemon = {
            "id": data["id"],
            "name": data["name"].capitalize(),
            "type": ", ".join([t["type"]["name"].capitalize() for t in data["types"]]),
            "abilities": [a["ability"]["name"].capitalize() for a in data["abilities"]],
            "image_url": data["sprites"]["front_default"],
            "description": f"A detailed description for {data['name'].capitalize()}."
        }
        return pokemon
    else:
        return None


@app.route('/')
def index():
    pokemon_list = get_pokemon_list()
    return render_template('index.html', pokemon_list=pokemon_list)


@app.route('/pokemon/<int:pokemon_id>')
def pokemon_detail(pokemon_id):
    pokemon = get_pokemon_details(pokemon_id)
    if pokemon is None:
        abort(404)
    return render_template('pokemon.html', pokemon=pokemon)


if __name__ == '__main__':
    app.run(debug=True)
