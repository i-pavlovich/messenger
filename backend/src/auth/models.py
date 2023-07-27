from datetime import date
from typing import Optional
from sqlalchemy import func, String
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str]
    first_name: Mapped[Optional[str]] = mapped_column(String(70))
    last_name: Mapped[Optional[str]] = mapped_column(String(70))

    creation_data: Mapped[date] = mapped_column(insert_default=func.now)
    is_active: Mapped[bool] = mapped_column(default=True)

    def __repr__(self) -> str:
        return f"<User {self.username} (id={self.id})>"
