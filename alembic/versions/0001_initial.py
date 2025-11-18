"""initial

Revision ID: 0001_initial
Revises:
Create Date: 2025-11-18 00:00:00.000000
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "customers",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("name", sa.String, nullable=True),
        sa.Column("email", sa.String, nullable=True, unique=True, index=True),
        sa.Column("phone", sa.String, nullable=True),
        sa.Column("referrer_id", sa.Integer, sa.ForeignKey("customers.id")),
    )

    op.create_table(
        "offers",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("title", sa.String, nullable=True),
        sa.Column("description", sa.String, nullable=True),
        sa.Column("price", sa.Float, nullable=True),
    )

    op.create_table(
        "orders",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("customer_id", sa.Integer, sa.ForeignKey("customers.id")),
        sa.Column("offer_id", sa.Integer, sa.ForeignKey("offers.id")),
    )

    op.create_table(
        "follow_ups",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("order_id", sa.Integer, sa.ForeignKey("orders.id")),
        sa.Column("date", sa.String, nullable=True),
        sa.Column("notes", sa.String, nullable=True),
    )


def downgrade():
    op.drop_table("follow_ups")
    op.drop_table("orders")
    op.drop_table("offers")
    op.drop_table("customers")
