from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.login import login_handler
from fastapi.responses import RedirectResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/about")
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@router.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login_endpoint")
async def login(request: Request, email: str, password: str):
    response = await login_handler(request, email, password)
    if "message" in response and response["message"] == "Logged in successfully":
        return RedirectResponse(url="/dashboard", status_code=302)
    return response

@router.get("/dashboard")
async def dashboard(request: Request):
    # Ideally, you'd fetch the user data here and pass it to the template
    user_data = {"username": "John"}  # Example data, replace with actual logic
    return templates.TemplateResponse("dashboard.html", {"request": request, "user": user_data})

@router.get("/register")
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})
