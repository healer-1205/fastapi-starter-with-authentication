from sqlalchemy.orm import Session
from app.config import SessionLocal

# Dependency to get the database session
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
