"""empty message

Revision ID: 28bbc0d8df8b
Revises: 3e249155ea6f
Create Date: 2019-06-15 16:06:11.867281

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28bbc0d8df8b'
down_revision = '3e249155ea6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('author', sa.Integer(), nullable=False))
    op.add_column('comment', sa.Column('author_username', sa.String(), nullable=False))
    op.create_index(op.f('ix_comment_author'), 'comment', ['author'], unique=False)
    op.create_index(op.f('ix_comment_author_username'), 'comment', ['author_username'], unique=False)
    op.create_foreign_key(None, 'comment', 'user', ['author_username'], ['username'])
    op.create_foreign_key(None, 'comment', 'user', ['author'], ['id'])
    op.add_column('post', sa.Column('author', sa.Integer(), nullable=False))
    op.add_column('post', sa.Column('author_username', sa.String(), nullable=False))
    op.create_index(op.f('ix_post_author'), 'post', ['author'], unique=False)
    op.create_index(op.f('ix_post_author_username'), 'post', ['author_username'], unique=False)
    op.create_foreign_key(None, 'post', 'user', ['author'], ['id'])
    op.create_foreign_key(None, 'post', 'user', ['author_username'], ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_index(op.f('ix_post_author_username'), table_name='post')
    op.drop_index(op.f('ix_post_author'), table_name='post')
    op.drop_column('post', 'author_username')
    op.drop_column('post', 'author')
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_index(op.f('ix_comment_author_username'), table_name='comment')
    op.drop_index(op.f('ix_comment_author'), table_name='comment')
    op.drop_column('comment', 'author_username')
    op.drop_column('comment', 'author')
    # ### end Alembic commands ###