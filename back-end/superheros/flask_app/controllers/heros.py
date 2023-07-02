from flask_app import app 
from flask import render_template, jsonify, request
import requests
import os

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/search', methods=['POST'])
def search():
    print(os.environ.get("FLASK_APP_API_KEY"))
    r = requests.get(f"https://superheroapi.com/api/{os.environ.get('FLASK_APP_API_KEY')}/search/{request.form['query']}")
    return jsonify(r.json())