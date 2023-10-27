from fastapi import APIRouter, Request, Depends, HTTPException, Header
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from typing import Optional, Union
from app.models import User
from app.database import db_session
from starlette.authentication import UnauthenticatedUser

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/about")
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

def get_current_user_or_anonymous(authorization: Optional[str] = Header(None)) -> Union[User, UnauthenticatedUser]:
    if not authorization:
        return UnauthenticatedUser()

@router.get("/login")
async def login_page(request: Request, user: User = Depends(get_current_user_or_anonymous)):
    return templates.TemplateResponse("login.html", {"request": request, "user": user})

def get_current_user_or_anonymous(authorization: Optional[str] = Header(None)) -> Union[User, UnauthenticatedUser]:
    if not authorization:
        return UnauthenticatedUser()
    # Otherwise, retrieve and return the authenticated user based on the "authorization" header.

async def login_handler(email: str, password: str):
    user = db_session.query(User).filter_by(email=email, password=password).first()
    if user:
        return {"message": "Logged in successfully"}
    else:
        raise HTTPException(status_code=400, detail="Invalid credentials")

@router.post("/login_endpoint")
async def login(request: Request, email: str, password: str):
    try:
        response = await login_handler(email, password)
        if "message" in response and response["message"] == "Logged in successfully":
            return RedirectResponse(url="/dashboard", status_code=302)
    except HTTPException:
        return {"message": "Invalid credentials"}

@router.get("/dashboard")
async def dashboard(request: Request):
    user_data = db_session.query(User).all()
    return templates.TemplateResponse("dashboard.html", {"request": request, "user": user_data})

@router.get("/register")
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})
