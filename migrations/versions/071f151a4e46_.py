"""empty message

Revision ID: 071f151a4e46
Revises: 4a1429f42553
Create Date: 2022-04-09 13:47:10.631368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '071f151a4e46'
down_revision = '4a1429f42553'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cookouts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('creator', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=150), nullable=True),
    sa.Column('food', sa.String(), nullable=True),
    sa.Column('drink', sa.String(), nullable=True),
    sa.Column('attendees', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['attendees'], ['users.id'], ),
    sa.ForeignKeyConstraint(['creator'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cookouts')
    # ### end Alembic commands ###
