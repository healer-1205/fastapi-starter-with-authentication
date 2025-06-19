from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.controllers import UserController
from app.dependencies import get_db
from app.schemas.UserSchema import UserCreate, UserSchema, UserReadSchema
from app.schemas.UserSchema import  UserLoginSchema
from app.middleware.VerifyToken import verify_token

router = APIRouter(prefix="/api/users", tags=["users"])


@router.post("/", response_model=UserReadSchema)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user
    """
    return await UserController.create_user(user, db)


@router.get("/", response_model=List[UserSchema], dependencies=[Depends(verify_token)])
async def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    List all users
    """
    return await UserController.list_users(skip, limit, db)


@router.get(
    "/{user_id}", response_model=UserSchema, dependencies=[Depends(verify_token)]
)
async def get_user(user_id: str, db: Session = Depends(get_db)):
    """
    Get a user by ID
    """
    user = await UserController.get_user(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put(
    "/{user_id}", response_model=UserReadSchema, dependencies=[Depends(verify_token)]
)
async def update_user(user_id: str, user: UserSchema, db: Session = Depends(get_db)):
    return await UserController.update_user(user_id, user, db)


@router.delete("/{user_id}", dependencies=[Depends(verify_token)])
async def delete_user(user_id: str, db: Session = Depends(get_db)):
    """
    Delete a user by ID
    """
    print(f"Deleting user with ID: {user_id}")
    await UserController.delete_user(user_id, db)
    return {"detail": "User deleted"}


@router.post("/login")
async def login(user: UserLoginSchema, db: Session = Depends(get_db)):
    """
    Authenticate user and return JWT token
    """
    authData = await UserController.login(user, db)
    if not authData:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return authData
