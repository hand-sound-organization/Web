"""empty message

Revision ID: a7a964a35794
Revises: 76bcbe03a974
Create Date: 2020-05-13 15:40:18.906475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7a964a35794'
down_revision = '76bcbe03a974'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('app_user', sa.Column('member', sa.Integer(), nullable=True))
    op.add_column('app_user', sa.Column('memberlist', sa.String(), nullable=True))
    op.add_column('app_user', sa.Column('safeday', sa.Integer(), nullable=True))
    op.add_column('app_user', sa.Column('safepct', sa.String(), nullable=True))
    op.add_column('app_user', sa.Column('safetimes', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('app_user', 'safetimes')
    op.drop_column('app_user', 'safepct')
    op.drop_column('app_user', 'safeday')
    op.drop_column('app_user', 'memberlist')
    op.drop_column('app_user', 'member')
    # ### end Alembic commands ###
