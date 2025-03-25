from app import create_app, db
from models import User, Product, Transaction, TransactionItem, QuickAccessProduct, DailyReport, LotteryTransaction, CashTransaction

app = create_app()

with app.app_context():
    # Create all tables
    db.create_all()
    print("Database tables created successfully!") 