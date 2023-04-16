from flask import Flask, render_template, session, redirect, request 
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = "coding_dojo"

@app.route('/')
def game():
    if 'total_gold' not in session:
        session['total_gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    if 'moves' not in session:
        session['moves'] = 0
    if 'result' not in session:
        session['result'] = ""

    reversed_activities = []
    for i in session['activities']:
        reversed_activities.insert(0, i)

    return render_template("index.html", total_gold=session['total_gold'], moves=session['moves'], activities=reversed_activities, result=session['result'])

@app.route('/process_money', methods=['POST'])
def process_money():
    session["building"] = request.form["building"]

    if session["building"] == "farm":
        gold = random.randint(10,20)
    elif session["building"] == "cave":
        gold = random.randint(5,10)
    elif session["building"] == "house":
        gold = random.randint(2,5)
    elif session["building"] == "casino":
        gold = random.randint(-50,50)

    session['moves'] += 1 
    session['total_gold'] += gold

    session['activities'].append({
        "location": session["building"],
        "gold": gold,
        "date": datetime.now()
    })

    if session['moves'] < 15 and session['total_gold'] >= 500:
        session['result'] = "You Win!"
    elif session['moves'] >= 15 and session['total_gold'] < 500:
        session['result'] = "You Lose"

    return redirect("/") 

@app.route('/destroy_session')
def reset():
    session.pop('total_gold')
    session.pop('activities')
    session.pop('moves')
    session.pop('result')
    return redirect("/") 

if __name__ == "__main__":
    app.run(debug=True)
