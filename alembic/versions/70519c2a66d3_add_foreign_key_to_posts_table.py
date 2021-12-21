"""add foreign key to posts table

Revision ID: 70519c2a66d3
Revises: 8c588f11b78e
Create Date: 2021-12-16 20:00:40.758210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70519c2a66d3'
down_revision = '8c588f11b78e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
