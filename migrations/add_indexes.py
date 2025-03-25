"""Add indexes for better search performance

This migration adds indexes to frequently searched columns to improve query performance.
"""

from alembic import op

def upgrade():
    # Add indexes for product search
    op.create_index('idx_product_name', 'product', ['name'])
    op.create_index('idx_product_sku', 'product', ['sku'])
    op.create_index('idx_product_barcode', 'product', ['barcode'])
    op.create_index('idx_product_category', 'product', ['category'])
    
    # Add indexes for transaction queries
    op.create_index('idx_transaction_date', 'transaction', ['date'])
    op.create_index('idx_transaction_user', 'transaction', ['user_id'])
    
    # Add index for quick access products
    op.create_index('idx_quick_access_position', 'quick_access_product', ['position'])

def downgrade():
    # Remove indexes
    op.drop_index('idx_product_name')
    op.drop_index('idx_product_sku')
    op.drop_index('idx_product_barcode')
    op.drop_index('idx_product_category')
    op.drop_index('idx_transaction_date')
    op.drop_index('idx_transaction_user')
    op.drop_index('idx_quick_access_position') 