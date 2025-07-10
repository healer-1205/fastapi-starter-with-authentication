import uuid
from fastapi import HTTPException
from sqlalchemy.orm import Session
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
    # if db.query(UserModel).filter(UserModel.username == user.username).first():
    #     raise HTTPException(status_code=400, detail="Username already taken")

    hashed_password = pwd_context.hash(user.password)

    db_user = UserModel(
        id=str(uuid.uuid4()),
        fullName=user.fullName,
        email=user.email,
        password=hashed_password,
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
    secret_key = os.getenv("ACCESS_TOKEN_SECRET_KEY")

    token = jwt.encode(payload, secret_key, algorithm="HS256")
    return {"accessToken": token, "userId": userId, "email": email}


async def create_user_from_oauth(
    db: Session,
    email: str,
    name: str,
    oauth_provider: str,
    oauth_id: str,
    avatar: str = None,
):
    """
    Create or update user from OAuth provider
    """
    # Check if user already exists by email
    existing_user = db.query(UserModel).filter(UserModel.email == email).first()

    if existing_user:
        # Update existing user with OAuth info
        if oauth_provider == "google":
            existing_user.googleId = oauth_id
        elif oauth_provider == "apple":
            existing_user.appleId = oauth_id
        elif oauth_provider == "facebook":
            existing_user.facebookId = oauth_id
        elif oauth_provider == "x":
            existing_user.xId = oauth_id

        existing_user.fullName = name
        if avatar:
            existing_user.avatar = avatar

        db.commit()
        db.refresh(existing_user)
        return existing_user

    # Check if OAuth ID already exists
    oauth_filter = None
    if oauth_provider == "google":
        oauth_filter = UserModel.googleId == oauth_id
    elif oauth_provider == "apple":
        oauth_filter = UserModel.appleId == oauth_id
    elif oauth_provider == "facebook":
        oauth_filter = UserModel.facebookId == oauth_id
    elif oauth_provider == "x":
        oauth_filter = UserModel.xId == oauth_id

    if oauth_filter:
        existing_oauth_user = db.query(UserModel).filter(oauth_filter).first()
        if existing_oauth_user:
            return existing_oauth_user

    # Create new user
    new_user = UserModel(
        email=email,
        fullName=name,
        avatar=avatar,
        password="",  # OAuth users don't need password
    )

    # Set the appropriate OAuth ID
    if oauth_provider == "google":
        new_user.googleId = oauth_id
    elif oauth_provider == "apple":
        new_user.appleId = oauth_id
    elif oauth_provider == "facebook":
        new_user.facebookId = oauth_id
    elif oauth_provider == "x":
        new_user.xId = oauth_id

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
