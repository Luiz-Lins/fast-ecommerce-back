"""add uuid

Revision ID: dbd62ca8b5cd
Revises: 227ee7edf01f
Create Date: 2020-10-28 20:18:27.639200
"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'dbd62ca8b5cd'
down_revision = '227ee7edf01f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('address', sa.Column('uuid', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('address', 'uuid')
    # ### end Alembic commands ###
