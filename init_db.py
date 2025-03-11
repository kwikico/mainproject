from app import create_app
from models import db, User, Product, QuickAccessProduct
from werkzeug.security import generate_password_hash

# Create the Flask app
app = create_app()

# Push an application context
with app.app_context():
    # Drop all existing tables and create new ones
    db.drop_all()
    db.create_all()
    
    # Create default users
    admin = User(
        username='admin',
        password=generate_password_hash('admin123'),
        role='manager'
    )
    cashier = User(
        username='cashier',
        password=generate_password_hash('cashier123'),
        role='cashier'
    )
    
    # Add sample products
    products = [
        Product(name='Milk', price=2.99, quantity=20, category='Dairy', barcode='7890123456789', sku='DAIRY001'),
        Product(name='Bread', price=1.99, quantity=15, category='Bakery', barcode='7890123456790', sku='BAKERY001'),
        Product(name='Eggs', price=3.49, quantity=30, category='Dairy', barcode='7890123456791', sku='DAIRY002'),
        Product(name='Soda', price=1.49, quantity=50, category='Beverages', barcode='7890123456792', sku='BEV001'),
        Product(name='Chips', price=0.99, quantity=40, category='Snacks', barcode='7890123456793', sku='SNACK001'),
        Product(name='Chocolate Bar', price=1.29, quantity=35, category='Snacks', barcode='7890123456794', sku='SNACK002'),
        Product(name='Water Bottle', price=0.99, quantity=60, category='Beverages', barcode='7890123456795', sku='BEV002'),
        Product(name='Coffee', price=4.99, quantity=25, category='Beverages', barcode='7890123456796', sku='BEV003'),
        Product(name='Yogurt', price=1.79, quantity=20, category='Dairy', barcode='7890123456797', sku='DAIRY003'),
        Product(name='Cereal', price=3.99, quantity=15, category='Breakfast', barcode='7890123456798', sku='BRKFST001'),
    ]
    
    # Add all objects to the session and commit
    db.session.add_all([admin, cashier] + products)
    db.session.commit()
    
    # Add sample quick access products (first 10 products)
    quick_access_products = []
    for i, product in enumerate(products[:10], 1):
        quick_access_products.append(QuickAccessProduct(position=i, product_id=product.id))
    
    # Add quick access products to the session and commit
    db.session.add_all(quick_access_products)
    db.session.commit()
    
    print("Database initialized successfully!") 