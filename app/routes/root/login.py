from app import app, bcrypt
from flask import render_template, request, redirect, url_for, flash, session
from app.models.user import User 



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        #Get user email from db
        user = User.query.filter_by(email=email).first()

        #Check password
        if user and bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login Sucessful')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid Login', 'Please try again')
            return redirect(url_for('login'))
        

    return render_template('root/login.html')

@app.route('/logout')
def logout():
    #Clear the session (User data)
    session.clear()
    flash('You have been logged out', 'session')
    return redirect(url_for('home_page'))