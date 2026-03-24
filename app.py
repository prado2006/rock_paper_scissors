import os
import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Возможные ходы
MOVES = ['камень', 'ножницы', 'бумага']

# Кто кого побеждает: ключ побеждает значение
WIN = {'камень': 'ножницы', 'ножницы': 'бумага', 'бумага': 'камень'}

@app.route('/')
def index():
    """Главная страница – отдаём HTML"""
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    """Принимает JSON с ходом игрока, возвращает JSON с результатом"""
    data = request.get_json()
    player = data['move']                     # ход игрока
    bot = random.choice(MOVES)                # случайный ход бота

    if player == bot:
        result = 'draw'
        msg = 'Ничья!'
    elif WIN[player] == bot:
        result = 'win'
        msg = 'Вы выиграли!'
    else:
        result = 'lose'
        msg = 'Бот выиграл!'

    return jsonify({
        'player': player,
        'bot': bot,
        'result': result,
        'message': msg
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
