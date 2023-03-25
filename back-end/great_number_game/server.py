from flask import Flask, render_template, redirect, request, session 
import random

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route('/')
def game():
    session['goal'] = random.randint(1,100)
    print(session['goal'])
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    if 'count' in session:
        session['count'] += 1 
    else:
        session['count'] = 1

    session['guess'] = request.form["guess"]
    if int(session['guess']) < int(session['goal']):
        result = "Too low!"
        if session['count'] >= 5:
            result = "You lose"
    elif int(session['guess']) > int(session['goal']):
        result = "Too high!"
        if session['count'] >= 5:
            result = "You lose"
    else:
        result = "That's correct!"
    return render_template("result.html", result=result, guess=int(session['guess']), goal=int(session['goal']), count=int(session['count']))

@app.route('/destroy_session')
def reset():
    session.pop('count')
    return redirect("/") 

@app.route('/leaderboard', methods=['POST'])
def leaderboard():
    session['name'] = request.form['name']
    return render_template("leaderboard.html", name=session['name'], count=int(session['count']))

if __name__ == "__main__":
    app.run(debug=True)