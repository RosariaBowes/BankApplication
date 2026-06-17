from app import app, db
from app.models.transaction import Transaction

with app.app_context():
    db.create_all()
    print("Transaction table created")