"""empty message

Revision ID: 6d6ab6571d71
Revises: 1379d698fb03
Create Date: 2020-04-20 22:12:35.428861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d6ab6571d71'
down_revision = '1379d698fb03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('attack_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lock_id', sa.Integer(), nullable=False),
    sa.Column('attack_time', sa.DateTime(), nullable=True),
    sa.Column('lng', sa.Float(), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('isSafe', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('attack_log')
    # ### end Alembic commands ###
