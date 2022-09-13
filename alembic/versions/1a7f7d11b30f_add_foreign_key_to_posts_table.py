"""add foreign key to posts table

Revision ID: 1a7f7d11b30f
Revises: c80dbc8d9a62
Create Date: 2022-09-13 14:49:32.571754

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a7f7d11b30f'
down_revision = 'c80dbc8d9a62'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts",
                   sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", source_table='posts', referent_table='users',
    local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')


def downgrade() -> None:
    op.drop_constraint("post_users_fk", table_name='posts')
    op.drop_column('posts', 'owner_id')
