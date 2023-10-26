from fastapi import APIRouter, HTTPException, Form, Depends, status, Request
from fastapi.responses import RedirectResponse
from app.models import User
from app import db_session
import bcrypt

router = APIRouter()

async def register_handler(email: str, password: str, fullname: str):
    # Ensure the email isn't already registered
    user_exists = db_session.query(User).filter_by(email=email).first()
    if user_exists:
        return {"error": "Email is already registered."}

    # Hash the password
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Register the new user
    new_user = User(email=email, password=hashed_pw.decode('utf-8'), fullname=fullname)
    db_session.add(new_user)
    db_session.commit()

    return {"message": "Registration successful!"}

@router.post("/register_endpoint")
async def register(request: Request, 
                   email: str = Form(...), 
                   password: str = Form(...),
                   fullname: str = Form(...)):
    response = await register_handler(email, password, fullname)
    if "message" in response:
        return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)
    else:
        raise HTTPException(status_code=400, detail=response["error"])
