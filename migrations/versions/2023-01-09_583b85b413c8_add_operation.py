"""Add Operation

Revision ID: 583b85b413c8
Revises: aebb6023c004
Create Date: 2023-01-09 13:02:20.799311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '583b85b413c8'
down_revision = 'aebb6023c004'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('operation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.String(), nullable=True),
    sa.Column('figi', sa.String(), nullable=True),
    sa.Column('instrument_type', sa.String(), nullable=True),
    sa.Column('date', sa.TIMESTAMP(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('operation')
    # ### end Alembic commands ###
