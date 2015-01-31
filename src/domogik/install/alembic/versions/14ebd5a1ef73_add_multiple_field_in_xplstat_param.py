"""Add multiple field in xplstat param

Revision ID: 14ebd5a1ef73
Revises: 1840cdc9f1da
Create Date: 2015-01-26 13:02:27.244147

"""

# revision identifiers, used by Alembic.
revision = '14ebd5a1ef73'
down_revision = '1840cdc9f1da'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('core_xplstat_param', sa.Column('multiple', sa.Unicode(length=1), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('core_xplstat_param', 'multiple')
    ### end Alembic commands ###
