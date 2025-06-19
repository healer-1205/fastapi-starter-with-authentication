from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime


class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[str] = None
    username: str | None = None
    email: EmailStr | None = None
    password: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    role: Optional[str] = None
    avatar: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class UserReadSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    email: EmailStr
    username: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    role: Optional[str] = None
    avatar: Optional[str] = None
    created_at: datetime
    updated_at: datetime


class UserCreate(UserSchema):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    firstName: Optional[str] = None
    lastName: Optional[str] = None
    password: Optional[str] = None

class UserLoginSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    email: EmailStr
    password: str
