from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import UserRouter
from app.config import Base, engine
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or set your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(UserRouter.router)
