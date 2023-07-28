from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "hello_world"

@app.route('/')
def empty_form():
    return render_template("index.html")

@app.route('/result', methods = ['POST'])
def result():
    print(request.form)
    language_list = [request.form['language']]
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form.getlist('language')
    print(session['language'])
    session['comment'] = request.form['comment']
    return render_template("result.html", name=session['name'], location=session['location'], language=session['language'], comment=session['comment'])

if __name__ == "__main__":
    app.run(debug=True)