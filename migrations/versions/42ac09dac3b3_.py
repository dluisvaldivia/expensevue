"""empty message

Revision ID: 42ac09dac3b3
Revises: a99c076d3ce5
Create Date: 2024-11-19 20:33:58.719916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42ac09dac3b3'
down_revision = 'a99c076d3ce5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('balances', schema=None) as batch_op:
        batch_op.drop_constraint('balances_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])

    with op.batch_alter_table('budgets', schema=None) as batch_op:
        batch_op.drop_constraint('budgets_category_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'categories', ['category_id'], ['id'])

    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.drop_constraint('categories_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])

    with op.batch_alter_table('connections', schema=None) as batch_op:
        batch_op.drop_constraint('connections_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])

    with op.batch_alter_table('fixed_expenses', schema=None) as batch_op:
        batch_op.drop_constraint('fixed_expenses_category_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'categories', ['category_id'], ['id'])

    with op.batch_alter_table('sources', schema=None) as batch_op:
        batch_op.drop_constraint('sources_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])

    with op.batch_alter_table('transactions', schema=None) as batch_op:
        batch_op.drop_constraint('transactions_source_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'sources', ['source_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transactions', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('transactions_source_id_fkey', 'sources', ['source_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('sources', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('sources_user_id_fkey', 'users', ['user_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('fixed_expenses', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('fixed_expenses_category_id_fkey', 'categories', ['category_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('connections', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('connections_user_id_fkey', 'users', ['user_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('categories_user_id_fkey', 'users', ['user_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('budgets', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('budgets_category_id_fkey', 'categories', ['category_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('balances', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('balances_user_id_fkey', 'users', ['user_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###