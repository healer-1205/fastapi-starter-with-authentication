import uuid
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.UserModel import UserModel
import jwt
import datetime
from passlib.context import CryptContext
import os


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def create_user(user, db):
    # Check if user already exists
    if db.query(UserModel).filter(UserModel.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    if db.query(UserModel).filter(UserModel.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already taken")

    hashed_password = pwd_context.hash(user.password)

    db_user = UserModel(
        id=str(uuid.uuid4()),
        username=user.username,
        email=user.email,
        password=hashed_password,
        firstName=user.firstName,
        lastName=user.lastName,
        role=user.role,
        avatar=user.avatar,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


async def list_users(skip, limit, db):
    users = db.query(UserModel).offset(skip).limit(limit).all()
    return users


async def get_user(user_id, db):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


async def update_user(user_id, user, db):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    update_data = user.dict(exclude_unset=True)
    if "password" in update_data and update_data["password"]:
        update_data["password"] = pwd_context.hash(update_data["password"])
    for key, value in update_data.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user


async def delete_user(user_id, db):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"detail": "User deleted"}


async def login(user, db: Session):
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Wrong User")
    if not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Wrong Password")

    userId = db_user.id
    email = db_user.email

    payload = {
        "userId": userId,
        "email": email,
        "exp": datetime.datetime.now(datetime.timezone.utc)
        + datetime.timedelta(days=30),
        "iat": datetime.datetime.now(datetime.timezone.utc),
    }

    # Get secret key from environment variables
    secret_key = os.getenv("NABL_ACCESS_TOKEN_SECRET_KEY")

    token = jwt.encode(payload, secret_key, algorithm="HS256")
    return {"nablJwtAccess": token, "userId": userId, "email": email}
