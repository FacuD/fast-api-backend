"""Initialize analytics table

Revision ID: 52f9f27ab033
Revises: 
Create Date: 2022-11-23 21:13:44.347065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52f9f27ab033'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('analytics',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date', sa.TIMESTAMP(), nullable=False),
    sa.Column('channel', sa.String(), nullable=False),
    sa.Column('country', sa.String(), nullable=False),
    sa.Column('os', sa.String(), nullable=False),
    sa.Column('impressions', sa.Integer(), nullable=False),
    sa.Column('clicks', sa.Integer(), nullable=False),
    sa.Column('installs', sa.Integer(), nullable=False),
    sa.Column('spend', sa.Float(), nullable=False),
    sa.Column('revenue', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('analytics')
    # ### end Alembic commands ###
