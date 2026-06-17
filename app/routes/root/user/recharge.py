from app import app, db
from flask import render_template, session, redirect, request, flash, url_for
from app.models.user import User
from app.models.transaction import Transaction



@app.route('/recharge', methods=['GET', 'POST'])
def recharge():
     user_id = session.get('user_id')
     if user_id:
          user = User.query.get(user_id)

          if request.method == 'POST':
               amount = float(request.form['amount'])

               #Calaculate Discount
               discount = amount * 0.1
               total_amount = amount - discount

               #Check Users balance 
               if total_amount > user.balance:
                    flash('Insufficient Balance', 'danger')
                    return redirect(url_for('recharge'))
               
               #Update the users balance
               user.balance -= total_amount

               #Update database 
               db.session.commit()

               Transaction = Transaction(
                    user_id = user.id,
                    recipient_name = user.full_name,
                    recipient_card_number = user.card_number,
                    amount = total_amount, 
                    type = "Debit - Airtime Purchase"
               )

               db.session.add(Transaction)
               db.session.commit()

               return render_template('user/recharge_success.html', amount=total_amount, discount=discount)
          return render_template('user/recharge.html', user=user)
     else:
          flash('Please Login First')
          return redirect(url_for('login'))