"""empty message

Revision ID: 1c0e69c8de4a
Revises: 28bbc0d8df8b
Create Date: 2019-06-15 16:10:34.903684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c0e69c8de4a'
down_revision = '28bbc0d8df8b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('comment_author_username_fkey', 'comment', type_='foreignkey')
    op.drop_constraint('post_author_username_fkey', 'post', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('post_author_username_fkey', 'post', 'user', ['author_username'], ['username'])
    op.create_foreign_key('comment_author_username_fkey', 'comment', 'user', ['author_username'], ['username'])
    # ### end Alembic commands ###
