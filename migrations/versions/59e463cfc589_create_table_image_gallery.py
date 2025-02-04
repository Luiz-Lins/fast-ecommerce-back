"""create table image gallery

Revision ID: 59e463cfc589
Revises: d9a7b005a2e9
Create Date: 2021-05-27 16:07:31.054508
"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '59e463cfc589'
down_revision = 'd9a7b005a2e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'imagegallery',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('url', sa.String(), nullable=True),
        sa.Column('product_id', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('imagegallery')
    # ### end Alembic commands ###
