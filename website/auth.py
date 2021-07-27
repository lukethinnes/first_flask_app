from flask import Blueprint, flash, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html', text='Testing') 

@auth.route('/logout')
def logout():
    return '<p>Logout</p>'

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.moeth == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

    if len(email) < 4:
        flash('Email must be greater than 4 characters.', category='failed') 
    elif len(firstName) < 2:
        flash('First name must be longer than 2 charcters.', category='failed')
    elif password1 != password2:
        flash('Passwords do not match.', category='failed')
    elif len(password1) < 7:
        flash('Password must be longer than 7 characters.', category='failed')
    else:
        flash('Account created!')

    return render_template('sign_up.html') 
