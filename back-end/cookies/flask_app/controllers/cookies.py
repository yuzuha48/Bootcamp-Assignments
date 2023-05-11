from flask_app import app 
from flask import render_template, redirect, request, session, flash
from flask_app.models.cookie import Cookie

@app.route('/')
def reroute():
    return redirect('/cookies')

@app.route('/cookies')
def cookie_orders():
    all_orders = Cookie.get_all()
    return render_template("cookie_orders.html", all_orders=all_orders)

@app.route('/cookies/new')
def save_order_page():
    return render_template("new_order.html")

@app.route('/cookies/new', methods=['POST'])
def save_order():
    if not Cookie.validate_order(request.form):
        session["customer_name"] = request.form["customer_name"]
        session["cookie_type"] = request.form["cookie_type"]
        session["num_of_boxes"] = request.form["num_of_boxes"]
        return redirect('/cookies/new')

    Cookie.save(request.form)
    session.pop('customer_name', None)
    session.pop('cookie_type', None)
    session.pop('num_of_boxes', None)
    return redirect('/cookies')

@app.route('/cookies/edit/<int:cookie_id>')
def edit_order_page(cookie_id):
    cookie = Cookie.get_one(cookie_id)
    return render_template("edit_order.html", cookie=cookie)

@app.route('/cookies/edit/<int:cookie_id>', methods=['POST'])
def edit_order(cookie_id):
    if not Cookie.validate_order(request.form):
        return redirect(f'/cookies/edit/{cookie_id}')

    Cookie.edit(cookie_id, request.form)
    return redirect('/cookies')