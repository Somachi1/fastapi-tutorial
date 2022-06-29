"""create post table

Revision ID: f53b3415613b
Revises: 4c504fb2f2d9
Create Date: 2022-06-26 18:57:33.573798

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f53b3415613b'
down_revision = '4c504fb2f2d9'
branch_labels = None
depends_on = None


def upgrade ()-> None:
    op.create_table('posts', 
    sa.Column('id', sa.Integer(), nullable=False, primary_key=True), 
    sa.Column('title', sa.String(), nullable=False) 
    )
    pass


def downgrade()-> None:
    op.drop_table('posts')
    pass
