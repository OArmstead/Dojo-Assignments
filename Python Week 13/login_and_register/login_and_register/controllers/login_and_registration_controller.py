from flask import render_template, redirect, request, session, flash
from login_and_register import app
from login_and_register.models.registration import Registration
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('register.html')

@app.route('/process',methods=['POST'])
def registration():

    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']

    if not Registration.validate_registration(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    # print(pw_hash)
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password' :pw_hash
    }
    id = Registration.save(data)
    Registration.save(request.form)
    session['id'] = id
    return redirect('/')

@app.route('/login', methods =['POST'])
def login():
    data = {'email': request.form['email']
    }
    registration_in_db = Registration.get_by_email(data)
    if not registration_in_db:
        flash('Invalid Email/Password')
        return redirect('/')
    if not bcrypt.check_password_hash(registration_in_db.password,request.form['password']):
        flash('Invalid Email/Password')
        return redirect('/')

    session['id'] = registration_in_db.id
    session['email'] = request.form['email']
    session['password'] = request.form['password']

    return redirect('/welcome')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html',first_name = session['first_name'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')