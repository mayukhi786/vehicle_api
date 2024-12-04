from fastapi import FastAPI
from app import models, database
from app.crud import router

# Initialize FastAPI app
app = FastAPI()

# Connect to database
models.Base.metadata.create_all(bind=database.engine)

# Include CRUD routes
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome"}