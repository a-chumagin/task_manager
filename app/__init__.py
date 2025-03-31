from fastapi import FastAPI

from app import models
from app.api import tasks
from app.database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API", description="FastAPI Task Manager API application")

# Include API router
app.include_router(tasks.router, tags=["tasks"])


@app.get("/", tags=["root"])
def read_root():
    return {"message": "Welcome to the Task Manager API"}
