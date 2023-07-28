from flask_app import app 
from flask_app.models import user
from flask_app.models import post
from flask_app.models import comment
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def home_page():
    return render_template("login_and_registration.html")

@app.route('/register', methods=['POST'])
def register():
    if not user.User.validate_user(request.form):
        session["first_name"] = request.form["first_name"]
        session["last_name"] = request.form["last_name"]
        session["email"] = request.form["email"]
        return redirect('/')

    user_info = user.User.save(request.form)
    session["user_id"] = user_info.id
    session["first_name"] = user_info.first_name
    session["last_name"] = user_info.last_name
    session["email"] = user_info.email
    return redirect('/wall')

@app.route('/login', methods=['POST'])
def login():
    user_in_db = user.User.get_by_email(request.form)
    if not user_in_db:
        session["login_email"] = request.form["email"]
        flash("Invalid Email.", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        session["login_email"] = request.form["email"]
        flash("Invalid Password.", "login")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/wall')

@app.route('/wall')
def wall():
    if 'user_id' not in session:
        return redirect('/log_out')
    user_info = user.User.get_one(session['user_id'])
    all_posts = post.Post.get_all()
    all_comments = comment.Comment.get_all()
    return render_template("wall.html", user=user_info, all_posts=all_posts, all_comments=all_comments)

@app.route('/wall', methods=['POST'])
def create_post():
    if not post.Post.validate_post(request.form):
        return redirect('/wall')
    post.Post.save(request.form)
    return redirect('/wall')

@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    post.Post.delete(post_id)
    return redirect('/wall')

@app.route('/comment/<int:user_id>/<int:post_id>', methods=['POST'])
def make_comment(user_id, post_id):
    comment.Comment.save_comment(user_id, post_id, request.form)
    return redirect('/wall')

@app.route('/log_out')
def log_out():
    session.clear()
    return redirect('/')