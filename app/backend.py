from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.route import router
from app.database import Database
import uvicorn
import os

app = FastAPI()
app.include_router(router)

# Serving static files
app.mount("/static", StaticFiles(directory="static"), name="static")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, '../templates')

templates = Jinja2Templates(directory=TEMPLATES_DIR)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8888)
