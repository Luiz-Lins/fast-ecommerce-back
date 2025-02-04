"""update tables product and adress

Revision ID: 4ed0b67518ec
Revises: e4dd5fb9b8ac
Create Date: 2020-12-02 11:25:18.806594
"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '4ed0b67518ec'
down_revision = 'e4dd5fb9b8ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('address', sa.Column('active', sa.Boolean(), nullable=True))
    op.add_column(
        'product',
        sa.Column('length', sa.Numeric(precision=5, scale=3), nullable=True),
    )
    op.drop_column('product', 'depthe')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'product',
        sa.Column('depthe', sa.INTEGER(), autoincrement=False, nullable=True),
    )
    op.drop_column('product', 'length')
    op.drop_column('address', 'active')
    # ### end Alembic commands ###
