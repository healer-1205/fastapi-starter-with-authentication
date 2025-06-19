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
    username = Column(String(50), unique=True, index=True)
    email = Column(String(120), unique=True, nullable=False, index=True)
    password = Column(String(128), nullable=False)
    firstName = Column(String(50), index=True)
    lastName = Column(String(50), index=True)
    role = Column(String(50), index=True)
    avatar = Column(String(255))
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    updated_at = Column(
        DateTime,
        default=datetime.datetime.now(datetime.timezone.utc),
        onupdate=datetime.datetime.now(datetime.timezone.utc),
    )

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}', firstName='{self.firstName}', lastName='{self.lastName}', role='{self.role}')>"
