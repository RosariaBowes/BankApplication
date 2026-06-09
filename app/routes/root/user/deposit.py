from app import app, db
from flask import render_template, session, request, redirect, url_for, flash
from app.models.user import User, Transaction


@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
     #Retrieve User information 
     user_id = session.get('user_id')
     if user_id:
          user = User.query.get(user_id)

          if request.method == 'POST':
               card_number = request.form['card_number']
               amount = float(request.form['amount'])

               # Check card number is valid 
               if card_number != user.card_number:
                    flash('Invalid card number', 'danger')
                    return redirect(url_for('deposit'))
               
               #Update users balance 
               user.balance += amount 

               #Create Credit transaction record
               Transaction = Transaction(
                    user_id = user.user_id,
                    recipient_name = user.full_name,
                    recipient_card_number = user.card_number
                    amount = amount
                    type - "Credit - Deposit"
               )

               db.session.add(Transaction)
               db.session.commit()

               flash(f'Succesfully Deposited £{amount:.2f} to your account.', 'success')
               return redirect(url_for('dashboard'))
          
          return render_template('user/deposit.html', user=user)
     else:
          flash('You need to login', 'danger')
          return redirect(url_for('login'))

