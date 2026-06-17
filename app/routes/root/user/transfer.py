from app import app, db
from flask import render_template, session, request, redirect, url_for, flash
from app.models.user import User
from app.models.transaction import Transaction
from .receipt import generate_receipt


@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    user_id = session.get('user_id')

    if not user_id:
        flash('Please login first', 'danger')
        return redirect(url_for('login'))

    user = User.query.get(user_id)

    if request.method == 'POST':
        recipient_card_name = request.form.get('card_name', '').strip().lower()

        recipient_card_number = (
            request.form.get('card_number', '')
            .replace(' ', '')
            .replace('-', '')
            .strip()
        )

        amount = float(request.form.get('amount', 0))

        if amount <= 0:
            flash('Please enter a valid amount', 'danger')
            return redirect(url_for('transfer'))

        if amount > user.balance:
            flash('Insufficient Funds', 'danger')
            return redirect(url_for('transfer'))

        recipient = User.query.filter_by(card_number=recipient_card_number).first()

        if not recipient:
            flash('Recipient card number not found', 'danger')
            return redirect(url_for('transfer'))

        if recipient.full_name.strip().lower() != recipient_card_name:
            flash('Recipient name does not match card number', 'danger')
            return redirect(url_for('transfer'))

        if recipient.id == user.id:
            flash('You cannot send funds to yourself', 'danger')
            return redirect(url_for('transfer'))

        user.balance -= amount
        recipient.balance += amount

        transaction_sender = Transaction(
            user_id=user.id,
            recipient_name=recipient.full_name,
            recipient_card_number=recipient.card_number,
            amount=amount,
            type='Debit'
        )

        transaction_recipient = Transaction(
            user_id=recipient.id,
            recipient_name=user.full_name,
            recipient_card_number=user.card_number,
            amount=amount,
            type='Credit'
        )

        db.session.add(transaction_sender)
        db.session.add(transaction_recipient)
        db.session.commit()

        receipt_data = {
            'sender_name': user.full_name,
            'recipient_name': recipient.full_name,
            'recipient_card_number': recipient.card_number,
            'amount': amount
        }

        receipt_filename = generate_receipt(receipt_data)

        return redirect(url_for('payment', filename=receipt_filename))

    return render_template('user/transfer.html', user=user)