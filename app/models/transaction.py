from app import db
from datetime import datetime

class Transaction(db.model):
    id = db.column(db.Integer, primary_key=True)
    user_id = db.column(db.Integer, db.ForeignKey('user.id'))
    recipient_name = db.column(db.String(200))
    recipient_card_number = db.column(db.String(16))
    amount = db.column(db.Float)
    type = db.column(db.String(25))
    timestamp = db.colum(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=('transactions'))