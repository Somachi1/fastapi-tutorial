"""add content column to post table

Revision ID: bc5849cb1d0d
Revises: f53b3415613b
Create Date: 2022-06-26 19:20:33.356901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc5849cb1d0d'
down_revision = 'f53b3415613b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
