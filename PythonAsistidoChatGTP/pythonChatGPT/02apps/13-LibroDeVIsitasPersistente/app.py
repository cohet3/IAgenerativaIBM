from flask import Flask, request, render_template, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = 'data.json'


def load_messages():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []


def save_message(name, message):
    messages = load_messages()
    new_message = {
        "name": name,
        "message": message,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    messages.append(new_message)
    with open(DATA_FILE, 'w') as f:
        json.dump(messages, f, indent=4)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        save_message(name, message)
        return redirect(url_for('index'))

    messages = load_messages()
    return render_template('index.html', messages=messages)


if __name__ == '__main__':
    app.run(debug=True)
