"""add content column

Revision ID: e99dfe1d0847
Revises: 7a5c4c9fc295
Create Date: 2022-09-13 14:31:38.539631

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e99dfe1d0847'
down_revision = '7a5c4c9fc295'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts",
                   sa.Column("content", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")
