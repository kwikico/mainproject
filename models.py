from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    transactions = db.relationship('Transaction', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    category = db.Column(db.String(50))
    barcode = db.Column(db.String(50), unique=True, nullable=True)
    sku = db.Column(db.String(50), unique=True, nullable=True)
    low_stock_threshold = db.Column(db.Integer, default=5)
    transaction_items = db.relationship('TransactionItem', backref='product', lazy=True)
    
    def __repr__(self):
        return f'<Product {self.name}>'

class QuickAccessProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.Integer, nullable=False)  # Position in the grid (1-10)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship('Product', backref='quick_access_positions')
    
    def __repr__(self):
        return f'<QuickAccessProduct {self.position}: {self.product.name if self.product else "None"}>'

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, index=True)
    total_amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    items = db.relationship('TransactionItem', backref='transaction', lazy=True, cascade="all, delete-orphan")
    discount_amount = db.Column(db.Float, default=0.0)
    is_return = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<Transaction {self.id}>'

class TransactionItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.Integer, db.ForeignKey('transaction.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=True)
    quantity = db.Column(db.Integer, nullable=False)
    price_at_time_of_sale = db.Column(db.Float, nullable=False)
    custom_name = db.Column(db.String(100), nullable=True)
    is_custom_product = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<TransactionItem {self.id}>' 