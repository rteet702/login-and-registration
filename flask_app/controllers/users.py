from flask_app import app
from flask_app.models.users import User
from flask import redirect, render_template, session, request, flash
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt(app)


@app.route('/')
def dashboard():
    if 'login_id' in session:
        data = {
            'id': session['login_id']
        }
        user = User.get_by_id(data)
        return render_template('dashboard.html', user=user)
    else:
        return redirect('/login')

@app.route('/login')
def r_login():
    return render_template('login.html')

@app.route('/register')
def r_register():
    return render_template('register.html')

@app.route('/submit', methods=['POST'])
def f_submit():
    inbound = request.form

    if inbound['type'] == 'register':
        if not User.validate_user_register(inbound):
            return redirect('/register')
        pw_hash = bcrypt.generate_password_hash(inbound['password'])
        data = {
            'first_name': inbound['first_name'],
            'last_name': inbound['last_name'],
            'email': inbound['email'],
            'password': pw_hash
        }

        login_id = User.save(data)
        session['login_id'] = login_id
    elif inbound['type'] == 'login':
        print('Entering Login Phase')
        data = {
            'email': inbound['email']
        }
        user_in_db = User.get_by_email(data)
        if not user_in_db:
            flash('Invalid Email/Password!')
            return redirect('/login')

        if not bcrypt.check_password_hash(user_in_db.password_hash, request.form['password']):
            flash('Invalid Email/Password!')
            return redirect('/login')

        print('Login Successful!')
        login_id = user_in_db.id
        session['login_id'] = login_id

    
    return redirect('/')


@app.route('/logout')
def f_logout():
    session.clear()
    return redirect('/')