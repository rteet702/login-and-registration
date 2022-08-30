from flask_app import app
from flask import redirect, render_template, session, request

@app.route('/')
def dashboard():
    if 'login_id' in session:
        return render_template('dashboard.html')
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
    print('test')
    print(inbound)
    
    if inbound['type'] == 'register':
        pass
    elif inbound['type'] == 'login':
        pass
    session['login_id'] = 'test'
    return redirect('/')