from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)
scores = {"user": 0, "computer": 0}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    user_choice = data.get('choice')
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    winner = "tie"
    if user_choice != computer_choice:
        if (user_choice == 'rock' and computer_choice == 'scissors') or \
           (user_choice == 'scissors' and computer_choice == 'paper') or \
           (user_choice == 'paper' and computer_choice == 'rock'):
            winner = "user"
            scores["user"] += 1
        else:
            winner = "computer"
            scores["computer"] += 1
    return jsonify({"user_choice": user_choice, "computer_choice": computer_choice, "winner": winner, "scores": scores})

if __name__ == '__main__':
    app.run(debug=True)