from app import app
from flask import render_template, session, flash, redirect, url_for
from app.models.user import User
from app.models.transaction import Transaction


@app.route('/dashboard')
def dashboard():
    user_id = session.get('user_id')

    if not user_id:
        flash('Please log in first, before you can access your dashboard', 'danger')
        return redirect(url_for('login'))

    user = User.query.get(user_id)

    recent_transactions = Transaction.query.filter_by(
        user_id=user_id
    ).order_by(
        Transaction.timestamp.desc()
    ).limit(5).all()

    all_transactions = Transaction.query.filter_by(user_id=user_id).all()

    total_transactions = len(all_transactions)

    total_credits = sum(
        1 for transaction in all_transactions
        if 'Credit' in transaction.type
    )

    total_debits = sum(
        1 for transaction in all_transactions
        if 'Debit' in transaction.type
    )

    total_deposited = sum(
        t.amount for t in all_transactions
        if t.type == "Credit - Deposit"
    )

    total_sent = sum(
        t.amount for t in all_transactions
        if t.type == "Debit"
    )

    total_airtime = sum(
        t.amount for t in all_transactions
        if t.type == "Debit - Airtime Purchase"
    )

    return render_template(
        'user/index.html',
        user=user,
        recent_transactions=recent_transactions,
        total_transactions=total_transactions,
        total_deposited=total_deposited,
        total_sent=total_sent,
        total_airtime=total_airtime
    )

