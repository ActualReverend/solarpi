"""empty message

Revision ID: 146eace7606b
Revises: 3cb99a2244f6
Create Date: 2014-07-28 22:20:06.080864

"""

# revision identifiers, used by Alembic.
revision = '146eace7606b'
down_revision = '201fb4631987'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ## commands auto generated by Alembic - please adjust! ###
    op.create_table('weather_data',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('created_at', sa.Text(), nullable=False),
                    sa.Column('temp', sa.Float(), nullable=True),
                    sa.Column('pressure', sa.Integer(), nullable=True),
                    sa.Column('temp_min', sa.Float(), nullable=True),
                    sa.Column('temp_max', sa.Float(), nullable=True),
                    sa.Column('humidity', sa.Integer(), nullable=True),
                    sa.Column('wind_speed', sa.Float(), nullable=True),
                    sa.Column('wind_gust', sa.Float(), nullable=True),
                    sa.Column('wind_deg', sa.Integer(), nullable=True),
                    sa.Column('clouds', sa.Integer(), nullable=True),
                    sa.Column('rain', sa.Integer(), nullable=True),
                    sa.Column('snow', sa.Integer(), nullable=True),
                    sa.Column('weather_id', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    # ## commands auto generated by Alembic - please adjust! ###
    op.drop_table('weather_data')
    ### end Alembic commands ###