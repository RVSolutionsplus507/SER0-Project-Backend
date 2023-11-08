"""empty message

Revision ID: 04ab38f66bd3
Revises: 6d6fd315fd59
Create Date: 2023-11-06 18:15:23.456106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04ab38f66bd3'
down_revision = '6d6fd315fd59'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('payment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=120), nullable=False),
    sa.Column('method', sa.String(length=120), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('amount', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('invoice', sa.String(length=120), nullable=False),
    sa.Column('service', sa.String(length=120), nullable=False),
    sa.Column('description', sa.String(length=20), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('date')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payment')
    # ### end Alembic commands ###