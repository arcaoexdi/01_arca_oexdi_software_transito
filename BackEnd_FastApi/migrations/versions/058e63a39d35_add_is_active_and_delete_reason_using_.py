"""Add is_active and delete_reason using batch_alter_table

Revision ID: 058e63a39d35
Revises: 3013ec254732
Create Date: 2025-11-28 13:54:06.745991

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '058e63a39d35'
down_revision: Union[str, Sequence[str], None] = '3013ec254732'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
