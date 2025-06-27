from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from app.config import Base
import uuid
import datetime


# User model definition
class UserModel(Base):
    __tablename__ = "users"

    id = Column(
        String(120), primary_key=True, index=True, default=lambda: str(uuid.uuid4())
    )
    fullName = Column(String(50), index=True)
    email = Column(String(120), unique=True, nullable=False, index=True)
    password = Column(String(128), nullable=False)
    avatar = Column(String(255))
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    updated_at = Column(
        DateTime,
        default=datetime.datetime.now(datetime.timezone.utc),
        onupdate=datetime.datetime.now(datetime.timezone.utc),
    )

    def __repr__(self):
        return f"<User(id={self.id}, fullName='{self.fullName}', email='{self.email}')>"
