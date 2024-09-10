"""Add active field

Revision ID: b9a443a5f518
Revises: f2e612c1f8e0
Create Date: 2024-07-28 22:29:56.800761

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9a443a5f518'
down_revision = 'f2e612c1f8e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('companies', schema=None) as batch_op:
        batch_op.add_column(sa.Column('active', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('companies', schema=None) as batch_op:
        batch_op.drop_column('active')

    # ### end Alembic commands ###