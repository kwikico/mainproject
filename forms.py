from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, IntegerField, SelectField, HiddenField, BooleanField, SearchField
from wtforms.validators import DataRequired, Length, NumberRange, Optional, ValidationError

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired(), Length(min=1, max=100)])
    price = FloatField('Price', validators=[DataRequired(), NumberRange(min=0.01)])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=0)])
    category = StringField('Category', validators=[Optional(), Length(max=50)])
    barcode = StringField('Barcode', validators=[Optional(), Length(max=50)])
    sku = StringField('SKU', validators=[Optional(), Length(max=50)])
    low_stock_threshold = IntegerField('Low Stock Threshold', validators=[Optional(), NumberRange(min=1)])
    submit = SubmitField('Save')

    def validate_price(self, field):
        if field.data <= 0:
            raise ValidationError('Price must be greater than 0.')

    def validate_barcode(self, field):
        if field.data:
            from models import Product
            product = Product.query.filter_by(barcode=field.data).first()
            if product and (not hasattr(self, 'id') or product.id != self.id.data):
                raise ValidationError('This barcode is already in use.')

    def validate_sku(self, field):
        if field.data:
            from models import Product
            product = Product.query.filter_by(sku=field.data).first()
            if product and (not hasattr(self, 'id') or product.id != self.id.data):
                raise ValidationError('This SKU is already in use.')

class TransactionItemForm(FlaskForm):
    product_id = SelectField('Product', coerce=int, validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)])
    custom_price = FloatField('Custom Price (Optional)', validators=[Optional(), NumberRange(min=0.01)])
    submit = SubmitField('Add to Cart')

    def validate_quantity(self, field):
        from models import Product
        product = Product.query.get(self.product_id.data)
        if product and field.data > product.quantity:
            raise ValidationError(f'Only {product.quantity} available in stock.')

class PaymentForm(FlaskForm):
    payment_method = SelectField('Payment Method', choices=[('cash', 'Cash'), ('card', 'Card')], validators=[DataRequired()])
    amount_tendered = FloatField('Amount Tendered', validators=[DataRequired(), NumberRange(min=0.01)])
    discount_amount = FloatField('Discount Amount', validators=[Optional(), NumberRange(min=0)])
    submit = SubmitField('Complete Transaction')

class ReturnForm(FlaskForm):
    transaction_id = IntegerField('Transaction ID', validators=[DataRequired()])
    submit = SubmitField('Find Transaction')

class ReturnItemForm(FlaskForm):
    transaction_item_id = HiddenField('Transaction Item ID', validators=[DataRequired()])
    return_quantity = IntegerField('Return Quantity', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Return Item')

class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    role = SelectField('Role', choices=[('cashier', 'Cashier'), ('manager', 'Manager')], validators=[DataRequired()])
    submit = SubmitField('Save')

class QuickAddForm(FlaskForm):
    product_code = StringField('Product Code (Barcode/SKU)', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)], default=1)
    submit = SubmitField('Add to Cart')

    def validate_product_code(self, field):
        from models import Product
        product = Product.query.filter((Product.barcode == field.data) | (Product.sku == field.data)).first()
        if not product:
            raise ValidationError('Product not found. Please check the barcode or SKU.')

    def validate_quantity(self, field):
        from models import Product
        product = Product.query.filter((Product.barcode == self.product_code.data) | (Product.sku == self.product_code.data)).first()
        if product and field.data > product.quantity:
            raise ValidationError(f'Only {product.quantity} available in stock.')

class ProductSearchForm(FlaskForm):
    search_term = StringField('Search Products', validators=[Optional()])
    submit = SubmitField('Search')

class QuickAccessProductForm(FlaskForm):
    position = HiddenField('Position', validators=[DataRequired()])
    product_id = SelectField('Product', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Save')

class CustomProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired(), Length(min=1, max=100)])
    price = FloatField('Price', validators=[DataRequired(), NumberRange(min=0.01)])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)], default=1)
    submit = SubmitField('Add to Cart')

    def validate_price(self, field):
        if field.data <= 0:
            raise ValidationError('Price must be greater than 0.')

class DailyReportForm(FlaskForm):
    date = StringField('Date', validators=[DataRequired()])
    opening_cash_balance = FloatField('Opening Cash Balance', validators=[DataRequired(), NumberRange(min=0)])
    closing_cash_balance = FloatField('Closing Cash Balance', validators=[DataRequired(), NumberRange(min=0)])
    cash_sales = FloatField('Cash Sales', validators=[DataRequired(), NumberRange(min=0)])
    card_sales = FloatField('Card Sales', validators=[DataRequired(), NumberRange(min=0)])
    lottery_sales = FloatField('Lottery Sales', validators=[DataRequired(), NumberRange(min=0)])
    confectionery_sales = FloatField('Confectionery Sales', validators=[DataRequired(), NumberRange(min=0)])
    tobacco_sales = FloatField('Tobacco Sales', validators=[DataRequired(), NumberRange(min=0)])
    lottery_payouts = FloatField('Lottery Payouts', validators=[DataRequired(), NumberRange(min=0)])
    lottery_commission = FloatField('Lottery Commission', validators=[DataRequired(), NumberRange(min=0)])
    restocking_costs = FloatField('Restocking Costs', validators=[DataRequired(), NumberRange(min=0)])
    miscellaneous_expenses = FloatField('Miscellaneous Expenses', validators=[DataRequired(), NumberRange(min=0)])
    cash_deposits = FloatField('Cash Deposits', validators=[DataRequired(), NumberRange(min=0)])
    notes = StringField('Notes', validators=[Optional()])
    submit = SubmitField('Save Daily Report')

class LotteryTransactionForm(FlaskForm):
    transaction_type = SelectField('Transaction Type', choices=[('sale', 'Sale'), ('payout', 'Payout')], validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired(), NumberRange(min=0)])
    ticket_number = StringField('Ticket Number', validators=[Optional()])
    commission_rate = FloatField('Commission Rate (%)', validators=[DataRequired(), NumberRange(min=0, max=100)])
    submit = SubmitField('Add Lottery Transaction')

class CashTransactionForm(FlaskForm):
    transaction_type = SelectField('Transaction Type', choices=[
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
        ('expense', 'Expense')
    ], validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired(), NumberRange(min=0)])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Add Cash Transaction') 