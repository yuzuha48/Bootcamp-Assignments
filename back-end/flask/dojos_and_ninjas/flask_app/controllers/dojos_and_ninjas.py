from flask_app import app 
from flask import render_template,redirect,request,session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def home():
    return redirect('/dojos')

@app.route('/dojos')
def all_dojos():
    all_dojos = Dojo.get_all()
    return render_template("dojo.html", all_dojos=all_dojos)


@app.route('/dojos', methods=['POST'])
def create_dojo():
    data = {
        "name": request.form["dojo_name"]
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/ninjas')
def new_ninja_page():
    all_dojos = Dojo.get_all()
    return render_template('ninja.html', all_dojos=all_dojos)

@app.route('/ninjas', methods=['POST'])
def add_ninja():
    data = { 
        "first_name": request.form["first_name"], 
        "last_name": request.form["last_name"], 
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    Ninja.save(data)
    return redirect(f'/dojos/{data["dojo_id"]}')

@app.route('/dojos/<int:dojo_id>')
def show_ninjas(dojo_id):
    all_ninjas = Dojo.get_ninjas(dojo_id)
    dojo = Dojo.get_one(dojo_id)
    return render_template("ninjas_in_dojo.html", all_ninjas=all_ninjas, dojo=dojo)

@app.route('/ninjas/delete/<int:dojo_id>/<int:ninja_id>')
def delete(dojo_id, ninja_id):
    Ninja.delete(ninja_id)
    return redirect(f'/dojos/{dojo_id}')

@app.route('/ninjas/edit/<int:dojo_id>/<int:ninja_id>')
def edit_ninja_page(dojo_id, ninja_id):
    dojo = Dojo.get_one(dojo_id)
    ninja = Ninja.get_one(ninja_id)
    return render_template ("edit_ninja.html", dojo=dojo, ninja=ninja)

@app.route('/ninjas/edit/<int:dojo_id>/<int:ninja_id>', methods=['POST'])
def edit(dojo_id, ninja_id):
    Ninja.update(ninja_id, request.form)
    return redirect(f'/dojos/{dojo_id}')