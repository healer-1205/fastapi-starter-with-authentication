from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime


class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[str] = None
    email: EmailStr | None = None
    password: Optional[str] = None
    fullName: Optional[str] = None
    avatar: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class UserReadSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    email: EmailStr
    fullName: Optional[str] = None
    avatar: Optional[str] = None
    created_at: datetime
    updated_at: datetime


class UserCreate(UserSchema):
    fullName: str
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    fullName: Optional[str] = None
    password: Optional[str] = None

class UserLoginSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    email: EmailStr
    password: str
