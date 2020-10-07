from flask import render_template, request
from app import app
from app.player import Player

player1 = Player("Tezz", 7, "noodles")

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', player1=player1)

@app.route('/', methods=['POST', 'GET'])
def guess():
    player1.play(request.form['guessChar'])
    return render_template('index.html', player1=player1)