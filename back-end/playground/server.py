from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def three():
    return render_template("new_color.html", num=3, color="lightblue")

@app.route('/play/<int:num>')
def num_boxes(num):
    return render_template("new_color.html", num=num, color="lightblue")

@app.route('/play/<int:num>/<string:color>')
def new_color(num, color):
    return render_template("new_color.html", num=num, color=color)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
