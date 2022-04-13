"""empty message

Revision ID: 0ab003344d9a
Revises: c1b16b361bc2
Create Date: 2022-04-13 13:32:03.371990

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ab003344d9a'
down_revision = 'c1b16b361bc2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cookouts', sa.Column('attendees', sa.String(), nullable=True))
    op.drop_constraint('users_att_cookouts_fkey', 'users', type_='foreignkey')
    op.drop_column('users', 'att_cookouts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('att_cookouts', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('users_att_cookouts_fkey', 'users', 'cookouts', ['att_cookouts'], ['id'])
    op.drop_column('cookouts', 'attendees')
    # ### end Alembic commands ###