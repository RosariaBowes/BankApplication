from app import app, db
from flask import render_template, session, request, redirect, url_for, flash
from app.models.user import User, Transaction 
from .reciept import generate_reciept

@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
     #Only for logged in users 
     user_id = session.get('user_id')
     if user_id:
          user = User.query.get(user_id)

          if request.method == 'POST':
              recipient_card_name = request.form['card_name'] 
              recipient_card_number = request.form['card_name'] 
              amount = float(request.form['amount'])

          if amount > user.balance:
               flash('Insufficient Funds', 'danger')
               return redirect(url_for('transfer'))
          
          recipient = User.query.filter_by(card_number=recipient_card_number).first()

          if recipient and recipient.full_name == recipient_card_name:
               #Check recipient isnt the same as the sender
               if recipient.id == user.id:
                    flash('You cannot send funds to yourself', 'danger')
                    return redirect(url_for('transfer'))
               
               # Update senders balance 
               user.balance -= amount

               # Update recievers balance 
               recipient.balance += amount

               # Update Database 
               db.session.commit()

               Transaction_sender = Transaction(
               user_id = user_id,
               recipient_name = recipient.full_name,
               recipient_card_number = recipient.card_number,
               amount = amount,
               type = 'Debit'
               )

               Transaction_recipient = Transaction(
                    user_id = recipient.id,
                    recipient_name = user.full_name,
                    recipient_card_number = user.card_number,
                    amount = amount,
                    type = 'Credit'
               )

               db.session.add(Transaction_sender)
               db.session.add(Transaction_recipient)
               db.session.commit()

               #Generate reciept data 
               reciept_data = {
                    'ender_name': user.full_name,
                    'recipient_name': recipient.full_name,
                    'recipient_card_number': recipient.card_number,
                    'amount': amount 
               }

               reciept_filename = generate_reciept(reciept_data)

               return redirect(url_for('payment', filename=reciept_filename))
          else:
               flash('Invalid recipient card name or number', 'danger')
               return redirect(url_for('transfer'))

          return render_template('user/transfer.html', user=user)
     else:
          flash('Please Login first', 'danger')
          return redirect(url_for('login'))