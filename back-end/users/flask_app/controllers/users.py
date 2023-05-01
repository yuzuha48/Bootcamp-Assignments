from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def route():
    return redirect('/users/new')

@app.route('/users/new')
def show_new_users_page():
    return render_template('create.html')

@app.route('/users/new', methods=['POST'])
def create():
    if not User.validate_user(request.form):
        session["first_name"] = request.form["first_name"]
        session["last_name"] = request.form["last_name"]
        session["email"] = request.form["email"]
        return redirect('/users/new')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])   
    print(pw_hash)

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"], 
        "email": request.form["email"],
        "password": pw_hash
    }

    user_id = User.create_new(data)

    # store user id into session 
    session['user_id'] = user_id

    return redirect(f'/users/{user_id}')

@app.route('/users')
def read():
    all_users = User.get_all()
    return render_template("read_all.html", all_users=all_users)

@app.route('/users/<int:user_id>')
def read_one(user_id):
    one_user = User.get_one(user_id)
    return render_template("read_one.html", one_user=one_user)

@app.route('/users/<int:user_id>/edit')
def edit(user_id):
    edit_user = User.get_one(user_id)
    return render_template("edit.html", edit_user=edit_user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def update(user_id):
    User.edit(user_id, request.form)
    return redirect(f"/users/{user_id}")

@app.route('/users/<int:user_id>/delete')
def delete(user_id):
    User.delete(user_id)
    return redirect("/users")


# we don't have a page for the user to login yet
@app.route('/login', methods=['POST'])
def login():
    # see if the username providede exists in the database 
    data = {"email": request.form["email"]}
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password 
        flash('Invalid Email/Password')
        return redirect('/')
    # if the passwords matched, we set the user_id into session 
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect('/users')
