from fastapi import APIRouter, HTTPException, Form, Request, Depends
from fastapi.responses import RedirectResponse
from app.models import User
from app import db_session
import bcrypt
from pydantic import BaseModel

router = APIRouter()

async def login_handler(email: str, password: str):
    user = db_session.query(User).filter_by(email=email).first()
    if user and bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
        return {"message": "Logged in successfully"}
    else:
        return {"error": "Invalid credentials"}

@router.post("/login_endpoint")
async def login(request: Request, email: str = Form(...), password: str = Form(...)):
    response = await login_handler(email, password)
    if "message" in response:
        return RedirectResponse(url="/dashboard", status_code=302)
    else:
        raise HTTPException(status_code=400, detail="Invalid credentials")
