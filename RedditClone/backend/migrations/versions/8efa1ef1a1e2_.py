"""empty message

Revision ID: 8efa1ef1a1e2
Revises: 5935fc62d3c5
Create Date: 2019-06-15 11:42:59.694508

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8efa1ef1a1e2'
down_revision = '5935fc62d3c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'user', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    # ### end Alembic commands ###