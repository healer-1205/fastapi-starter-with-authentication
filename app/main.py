import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import UserRouter, OAuthRouter
from app.config import Base, engine
from dotenv import load_dotenv
from starlette.middleware.sessions import SessionMiddleware

# Load environment variables from .env file
load_dotenv()

# Initialize Database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Session middleware (REQUIRED for OAuth)
app.add_middleware(SessionMiddleware, secret_key=os.getenv("ACCESS_TOKEN_SECRET_KEY"))

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or set your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Backend is running"}


app.include_router(UserRouter.router)
app.include_router(OAuthRouter.router)
