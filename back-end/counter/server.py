from flask import Flask, render_template, request, redirect, session 

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def count():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template("index.html")

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect("/") 

@app.route('/add_two', methods=['POST'])
def add_two():
    session['count'] += 2
    return render_template("index.html")

@app.route('/add_visits', methods=['POST'])
def add_num():
    session['count'] += int(request.form['add_visits'])
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
