from app import create_app
from models import db, User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    # Check if admin user already exists
    admin = User.query.filter_by(username='admin').first()
    
    if admin:
        print("Admin user already exists!")
    else:
        # Create admin user
        admin_user = User(
            username='admin',
            password=generate_password_hash('admin123'),
            role='admin'
        )
        
        db.session.add(admin_user)
        db.session.commit()
        print("Admin user created successfully!")
        print("Username: admin")
        print("Password: admin123") 