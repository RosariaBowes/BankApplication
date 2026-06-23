from app import app, db
from flask import render_template, session, request, redirect, url_for, flash
from app.models.user import User
from app.models.transaction import Transaction


@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    user_id = session.get('user_id')

    if not user_id:
        flash('You need to login', 'danger')
        return redirect(url_for('login'))

    user = User.query.get(user_id)

    if request.method == 'POST':
        card_number = (
            request.form.get('card_number', '')
            .replace(' ', '')
            .replace('-', '')
            .strip()
        )

        amount = float(request.form.get('amount', 0))

        if amount <= 0:
            flash('Please enter a valid amount', 'danger')
            return redirect(url_for('deposit'))

        if card_number != user.card_number:
            flash('Invalid card number', 'danger')
            return redirect(url_for('deposit'))

        user.balance += amount

        transaction = Transaction(
            user_id=user.id,
            recipient_name=user.full_name,
            recipient_card_number=user.card_number,
            amount=amount,
            type="Credit - Deposit"
        )

        db.session.add(transaction)
        db.session.commit()

        flash(f'Successfully deposited £{amount:.2f} to your account.', 'success')
        return redirect(url_for('dashboard'))

    return render_template('user/deposit.html', user=user)

