"""add foreign key to post

Revision ID: 776412fb29a0
Revises: b49947a6db28
Create Date: 2022-06-26 21:01:01.846508

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '776412fb29a0'
down_revision = 'b49947a6db28'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    
    pass


def downgrade() -> None:
    op.drop_constraint('post_user_fk', table_name="posts")

    pass
