"""create tables

Revision ID: 1cff14731fc1
Revises:
Create Date: 2025-04-15 13:26:48.100724

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1cff14731fc1"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "departments",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_departments")),
        sa.UniqueConstraint("name", name=op.f("uq_departments_name")),
    )
    op.create_table(
        "job_titles",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_job_titles")),
    )
    op.create_table(
        "roles",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_roles")),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("middle_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.Column("job_title", sa.Integer(), nullable=False),
        sa.Column("department", sa.Integer(), nullable=False),
        sa.Column("role", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["department"],
            ["departments.id"],
            name=op.f("fk_users_department_departments"),
        ),
        sa.ForeignKeyConstraint(
            ["job_title"],
            ["job_titles.id"],
            name=op.f("fk_users_job_title_job_titles"),
        ),
        sa.ForeignKeyConstraint(
            ["role"], ["roles.id"], name=op.f("fk_users_role_roles")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_users")),
        sa.UniqueConstraint("username", name=op.f("uq_users_username")),
    )


def downgrade() -> None:
    op.drop_table("users")
    op.drop_table("roles")
    op.drop_table("job_titles")
    op.drop_table("departments")
