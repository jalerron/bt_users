from sqlalchemy import ForeignKey, Integer
from core.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    first_name: Mapped[str]
    middle_name: Mapped[str]
    last_name: Mapped[str]
    job_title: Mapped[int] = mapped_column(Integer, ForeignKey("job_titles.id"))
    department: Mapped[int] = mapped_column(Integer, ForeignKey("departments.id"))
    role: Mapped[int] = mapped_column(Integer, ForeignKey("roles.id"))


class JobTitle(Base):

    __tablename__ = "job_titles"

    name: Mapped[str]


class Department(Base):

    name: Mapped[str] = mapped_column(unique=True)

class Role(Base):

    name: Mapped[str]
    description: Mapped[str]
