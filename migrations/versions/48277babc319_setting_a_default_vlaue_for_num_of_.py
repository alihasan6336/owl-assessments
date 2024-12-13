"""setting a default vlaue for num_of_questions column in test

Revision ID: 48277babc319
Revises: eacae050e16a
Create Date: 2024-12-12 07:44:09.593634

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48277babc319'
down_revision = 'eacae050e16a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tests', schema=None) as batch_op:
        batch_op.alter_column('num_of_questions',
               existing_type=sa.SMALLINT(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tests', schema=None) as batch_op:
        batch_op.alter_column('num_of_questions',
               existing_type=sa.SMALLINT(),
               nullable=True)

    # ### end Alembic commands ###