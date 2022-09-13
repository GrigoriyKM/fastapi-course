"""add last few columns to posts table

Revision ID: 22ed185881b2
Revises: 1a7f7d11b30f
Create Date: 2022-09-13 14:57:23.571185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22ed185881b2'
down_revision = '1a7f7d11b30f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts",
                   sa.Column("published", sa.Boolean(), nullable=False, server_default=sa.sql.true()))
    op.add_column("posts",
                   sa.Column("created_at",sa.TIMESTAMP(timezone=True),
                   server_default=sa.text('NOW()'), nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    
