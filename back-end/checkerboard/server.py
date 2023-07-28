from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def eightbyeight():
    return render_template("checkerboard.html", width=4, height=8, color1="forestgreen", color2="cornsilk")

@app.route('/4')
def eightbyfour():
    return render_template("checkerboard.html", width=4, height=4, color1="forestgreen", color2="cornsilk")

@app.route('/<int:width>/<int:height>')
def x_by_y(width, height):
    width = int(width/2)
    return render_template("checkerboard.html", width=width, height=height, color1="forestgreen", color2="cornsilk")

@app.route('/<int:width>/<int:height>/<string:color1>/<string:color2>')
def choose_size_and_color(width, height, color1, color2):
    width = int(width/2)
    return render_template("checkerboard.html", width=width, height=height, color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=True)