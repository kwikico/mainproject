# POS System

A comprehensive Point of Sale (POS) system built with Python and Flask, designed for retail stores.

## Features

- **Product Management**: Add, edit, and delete products with details like name, price, quantity, category, barcode, and SKU.
- **Quick Access Products**: Configure 10 customizable product buttons for quick addition to cart.
- **Transaction Processing**: Create and manage transactions with support for both regular and custom products.
- **Custom Product Entry**: Add one-time products directly to the cart without affecting inventory.
- **Price Overrides**: Override standard prices for specific transactions.
- **Payment Options**: Support for cash and card payment methods (card for record-keeping only).
- **Transaction History**: View previous transaction details when the cart is empty.
- **Inventory Management**: Automatic inventory updates when products are sold.
- **User Management**: Support for different user roles (manager, cashier) with appropriate permissions.
- **Reports**: Generate sales and inventory reports.
- **Returns Processing**: Process returns and update inventory accordingly.

## Technology Stack

- **Backend**: Python, Flask
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Dependencies**: See requirements.txt

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/mainproject.git
   cd mainproject
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```
   python init_db.py
   ```

5. Run the application:
   ```
   python run.py
   ```

6. Access the application at http://localhost:5000

## Default Users

- **Manager**: Username: `admin`, Password: `admin123`
- **Cashier**: Username: `cashier`, Password: `cashier123`

## Usage

### Transaction Process

1. **Start a Transaction**: Navigate to "New Transaction" page.
2. **Add Products**: Use quick access buttons, search, or manual entry to add products.
3. **Customize Prices**: Override prices if needed for specific transactions.
4. **Review Cart**: Check the cart contents and make adjustments if necessary.
5. **Checkout**: Proceed to checkout, select payment method, and complete the transaction.
6. **Receipt**: View and optionally print the receipt.

### Custom Products

1. Click "Custom Product" button on the transaction page.
2. Enter product name, price, and quantity.
3. Add to cart.

### Quick Access Products (Managers Only)

1. Navigate to "Quick Access Products" in the sidebar.
2. Configure which products appear in the quick access grid.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Bootstrap for the UI components
- Select2 for enhanced select boxes
- Bootstrap Icons for the icon set

## Heroku Deployment

This application is configured for deployment on Heroku. Follow these steps to deploy:

1. Make sure you have the Heroku CLI installed and are logged in:
   ```
   heroku login
   ```

2. Create a new Heroku app:
   ```
   heroku create your-app-name
   ```

3. Provision a PostgreSQL database:
   ```
   heroku addons:create heroku-postgresql:hobby-dev
   ```

4. Push your code to Heroku:
   ```
   git push heroku main
   ```
   (If your default branch is master, use `git push heroku master`)

5. Initialize the database on Heroku:
   ```
   heroku run python init_heroku_db.py
   ```

6. Open your application:
   ```
   heroku open
   ```

7. Check logs if errors occur:
   ```
   heroku logs --tail
   ```

## Local Development

For local development:

1. Set the FLASK_ENV environment variable to 'development':
   ```
   export FLASK_ENV=development  # Unix/Mac
   set FLASK_ENV=development     # Windows
   ```

2. Run the application:
   ```
   python run.py
   ``` 