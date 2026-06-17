from app import app
from flask import render_template, session, flash, redirect, url_for
from app.models.user import User

@app.route('/accounts')
def accounts():

    user_id = session.get('user_id')

    if user_id:
        user = User.query.get(user_id)
        return render_template('user/accounts.html', user=user)

    flash('Please log in first', 'danger')
    return redirect(url_for('login'))