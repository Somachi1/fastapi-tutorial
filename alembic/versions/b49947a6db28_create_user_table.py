"""create_user_table

Revision ID: b49947a6db28
Revises: bc5849cb1d0d
Create Date: 2022-06-26 20:14:52.392449

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b49947a6db28'
down_revision = 'bc5849cb1d0d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                            sa.Column('id', sa.Integer(), nullable=False),
                            sa.Column('email', sa.String(), nullable=False),
                            sa.Column('password', sa.String(), nullable=False),
                            sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
                                        server_default=sa.text('now()'), nullable=False),
                            sa.PrimaryKeyConstraint('id'),
                            sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
