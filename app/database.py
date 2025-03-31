import os
import pathlib

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create data directory if it doesn't exist
# Handle both local development and Docker environment
if os.path.exists("/app"):
    # Docker environment
    data_dir = "/app/data"
else:
    # Local development environment
    base_dir = pathlib.Path(__file__).parent.parent
    data_dir = os.path.join(base_dir, "data")

os.makedirs(data_dir, exist_ok=True)

# Define the SQLite database URL
database_path = os.path.join(data_dir, "tasks.db")
SQLALCHEMY_DATABASE_URL = f"sqlite:///{database_path}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
