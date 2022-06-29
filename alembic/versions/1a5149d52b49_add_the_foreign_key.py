"""add the foreign key

Revision ID: 1a5149d52b49
Revises: 776412fb29a0
Create Date: 2022-06-26 21:15:56.711649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a5149d52b49'
down_revision = '776412fb29a0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", 
    local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE" )
    
    pass


def downgrade() -> None:
    op.drop_column('posts','owner_id')
    pass
