"""empty message

Revision ID: f5f940af25bc
Revises: a7a964a35794
Create Date: 2020-05-13 21:19:19.706233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5f940af25bc'
down_revision = 'a7a964a35794'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('app_user', sa.Column('datalist', sa.String(), nullable=True))
    op.add_column('app_user', sa.Column('timeend', sa.String(), nullable=True))
    op.add_column('app_user', sa.Column('timestart', sa.String(), nullable=True))
    op.add_column('warning_info', sa.Column('username', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('warning_info', 'username')
    op.drop_column('app_user', 'timestart')
    op.drop_column('app_user', 'timeend')
    op.drop_column('app_user', 'datalist')
    # ### end Alembic commands ###