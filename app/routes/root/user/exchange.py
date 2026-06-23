from app import app
from flask import render_template, session, request, redirect, url_for, flash

@app.route('/exchange_rate')
def exchange_rate():
     user_id = session.get('user_id')

     if not user_id:
          flash('Please login first', 'danger')
          return redirect(url_for('login'))
     
     rates = [
          {'currency': 'US Dollar', 'code': 'USD', 'rate': 1.27},
          {'currency': 'Euro', 'code': 'EUR', 'rate': 1.18},
          {'currency': 'Canadian Dollar', 'code': 'CAD', 'rate': 1.72},
          {'currency': 'Australian Dollar', 'code': 'AUD', 'rate': 1.94},
          {'currency': 'Japanese Yen', 'code': 'JPY', 'rate': 199.50},
     ]

     return render_template('user/exchange_rate.html', rates=rates)