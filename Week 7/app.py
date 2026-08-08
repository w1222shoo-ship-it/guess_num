from flask import Flask, jsonify, request, render_template
import random
import uuid

app = Flask(__name__)

# 簡單的記憶體儲存（示範用，非 persist）
games = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/start', methods=['POST'])
def start():
    gid = uuid.uuid4().hex
    games[gid] = {'target': random.randint(1, 100), 'attempts': 0}
    return jsonify({'game_id': gid})


@app.route('/guess', methods=['POST'])
def do_guess():
    data = request.get_json(force=True, silent=True) or request.form
    gid = data.get('game_id')
    if not gid or gid not in games:
        return jsonify({'error': 'invalid_game_id'}), 400

    try:
        guess = int(data.get('guess'))
    except Exception:
        return jsonify({'error': 'invalid_guess'}), 400

    g = games[gid]
    g['attempts'] += 1

    if guess > g['target']:
        result = 'too_big'
    elif guess < g['target']:
        result = 'too_small'
    else:
        result = 'correct'

    return jsonify({'result': result, 'attempts': g['attempts']})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
