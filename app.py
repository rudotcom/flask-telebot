import os

import openai
from flask import Flask, render_template, request, jsonify
from openai.error import ServiceUnavailableError, InvalidRequestError, RateLimitError

openai.api_key = os.environ.get('OPENAI_API_KEY')
app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/speech-to-text', methods=['POST'])
def speech_to_text():
    transcript = request.json['transcript']
    messages = [{"role": "system", "content": "Ты дружелюбный, но саркастичный бот."},
                {"role": "user", "content": transcript}]
    print('Вопрос:', transcript)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.5,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0,
        )
    except ServiceUnavailableError:
        return jsonify({'response': 'Извините, сервер openAI перегружен и не отвечает.'})
    except InvalidRequestError as e:
        return jsonify({'response': f'Проблема с запросом, {e}'})
    except RateLimitError:
        return jsonify({'response': 'Превышен лимит запросов в минуту.'})
    except BaseException as e:
        return jsonify({'response': f'Неизвестная ошибка: {e}'})

    print('GPT:', response.choices[0].message.content)
    return jsonify({'response': response.choices[0].message.content})


if __name__ == '__main__':
    app.run(debug=True)
