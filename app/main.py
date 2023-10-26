from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.route import router
from app.database import init_db

import uvicorn
import os

app = FastAPI()

# Initialize the database
init_db()

app.include_router(router)

# Serving static files
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8888)
