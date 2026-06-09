from app import app, bcrypt, db
from flask import render_template, request, flash, redirect, url_for, session
import random
from app.models.user import User


@app.route('/register', methods=["GET", "POST"])
def register_page():
    if request.method == "POST":
        full_name = request.form['full_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('register_page'))

        if len(password) < 6:
            flash('Password is too short. Please try again', 'danger')
            return redirect(url_for('register_page'))

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('You have an existing account. Please log in', 'danger')
            return redirect(url_for('login'))

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        card_number = ''.join([str(random.randint(0, 9)) for _ in range(16)])
        formatted_card_number = ' '.join(
            [card_number[i:i+4] for i in range(0, len(card_number), 4)]
        )

        new_user = User(
            full_name=full_name,
            email=email,
            password=hashed_password,
            card_number=card_number
        )

        db.session.add(new_user)
        db.session.commit()

        session['user_id'] = new_user.id
        session['card_number'] = formatted_card_number

        flash('Registration successful. Welcome to Bowes Bank.', 'success')
        return redirect(url_for('dashboard'))

    return render_template('root/register.html')
