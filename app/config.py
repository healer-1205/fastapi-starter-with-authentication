import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from authlib.integrations.starlette_client import OAuth
from dotenv import load_dotenv

load_dotenv()


# Local Database Configuration
DB_USER = os.getenv("DB_USER", "")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "")
DB_PORT = os.getenv("DB_PORT", "")
DB_NAME = os.getenv("DB_NAME", "")

SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# OAuth2 Configuration
oauth = OAuth()
oauth.register(
    name="google",
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    access_token_url="https://oauth2.googleapis.com/token",
    access_token_params=None,
    authorize_url="https://accounts.google.com/o/oauth2/v2/auth",
    authorize_params=None,
    api_base_url="https://www.googleapis.com/oauth2/v2/",
    client_kwargs={"scope": "openid email profile"},
)
