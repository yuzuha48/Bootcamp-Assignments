from flask_app import app 
from flask import render_template
from flask import jsonify

@app.route('/')
def home():
    return render_template("git.html")

@app.route('/get_data')
def get_data():
    # jsonify will serialize data into JSON format 
    return jsonify(message='Hello World')

