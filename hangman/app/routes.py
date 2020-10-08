from flask import render_template, request
from app import app
from app.player import Player

player1 = Player("Tezz", 7, "noodles")

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def submitGame():
    global player1
    player1 = Player(request.form['playerName'], int(request.form['noOfGuesses']), request.form['word'])
    return render_template("game.html", player1=player1)

@app.route('/game/<int:i>')
def gameinit(i):
    return render_template('game.html', i=i, player1=player1)

# @app.route('/', methods=['POST', 'GET'])
@app.route('/game/', methods=['POST', 'GET'])
def game():

    player1.play(request.form['guessChar'].upper())
    return render_template('game.html', player1=player1)