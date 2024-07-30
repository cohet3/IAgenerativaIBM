from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    translated_texts = {
        'english': '',
        'french': '',
        'italian': '',
        'german': ''
    }

    if request.method == 'POST':
        text_to_translate = request.form.get('spanish_text', '')

        if text_to_translate:
            try:
                translator = GoogleTranslator(source='es')
                translated_texts['english'] = translator.translate(text_to_translate, target='en')
                translated_texts['french'] = translator.translate(text_to_translate, target='fr')
                translated_texts['italian'] = translator.translate(text_to_translate, target='it')
                translated_texts['german'] = translator.translate(text_to_translate, target='de')
            except Exception as e:
                print(f"Error during translation: {e}")

    return render_template('index.html', translated_texts=translated_texts)


if __name__ == '__main__':
    app.run(debug=True)
