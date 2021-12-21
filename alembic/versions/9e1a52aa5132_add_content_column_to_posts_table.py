"""add content column to posts table

Revision ID: 9e1a52aa5132
Revises: df0a71fa3e46
Create Date: 2021-12-16 19:44:48.762612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e1a52aa5132'
down_revision = 'df0a71fa3e46'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
