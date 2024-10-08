"""fixing the city name length to be 50 chars

Revision ID: def37c3889db
Revises: 6319d618d049
Create Date: 2024-09-09 14:21:12.580602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'def37c3889db'
down_revision = '6319d618d049'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('companies', schema=None) as batch_op:
        batch_op.alter_column('city',
               existing_type=sa.VARCHAR(length=35),
               type_=sa.String(length=50),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('companies', schema=None) as batch_op:
        batch_op.alter_column('city',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=35),
               existing_nullable=True)

    # ### end Alembic commands ###
