"""empty message

Revision ID: c5de4d5d2aa6
Revises: 
Create Date: 2021-12-07 15:52:46.735038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5de4d5d2aa6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('street', sa.String(length=100), nullable=True),
    sa.Column('suite', sa.String(length=100), nullable=True),
    sa.Column('city', sa.String(length=150), nullable=True),
    sa.Column('zipcode', sa.String(length=150), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('deleted_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('address')
    # ### end Alembic commands ###
