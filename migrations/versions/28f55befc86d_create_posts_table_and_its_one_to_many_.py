"""Create posts table and its one to many relationship with users table

Revision ID: 28f55befc86d
Revises: ac56fc5eb6e5
Create Date: 2017-11-03 15:25:43.826461

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28f55befc86d'
down_revision = 'ac56fc5eb6e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post_title', sa.String(), nullable=True),
    sa.Column('post_content', sa.String(), nullable=True),
    sa.Column('post_date', sa.Time(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    # ### end Alembic commands ###
