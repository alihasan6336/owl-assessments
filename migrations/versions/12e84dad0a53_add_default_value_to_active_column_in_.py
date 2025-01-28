"""Add default value to active column in tests table

Revision ID: 12e84dad0a53
Revises: f483d26c1f5a
Create Date: 2025-01-22 07:03:28.967101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12e84dad0a53'
down_revision = 'f483d26c1f5a'
branch_labels = None
depends_on = None


def upgrade():
    # Manually add the command to alter the column
    op.alter_column('tests', 'active',
                    existing_type=sa.Boolean(),
                    server_default=sa.text('false'),
                    existing_nullable=True)

def downgrade():
    # Manually add the command to revert the column change
    op.alter_column('tests', 'active',
                    existing_type=sa.Boolean(),
                    server_default=None,
                    existing_nullable=True)