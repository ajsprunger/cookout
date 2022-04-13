"""empty message

Revision ID: c1b16b361bc2
Revises: edfed64e2720
Create Date: 2022-04-13 13:20:58.749472

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1b16b361bc2'
down_revision = 'edfed64e2720'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('att_cookouts', sa.Integer(), nullable=True))
    op.drop_constraint('users_cookouts_att_fkey', 'users', type_='foreignkey')
    op.create_foreign_key(None, 'users', 'cookouts', ['att_cookouts'], ['id'])
    op.drop_column('users', 'cookouts_att')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('cookouts_att', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.create_foreign_key('users_cookouts_att_fkey', 'users', 'cookouts', ['cookouts_att'], ['id'])
    op.drop_column('users', 'att_cookouts')
    # ### end Alembic commands ###