from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from app.database import Database
from fastapi.responses import RedirectResponse
import bcrypt

templates = Jinja2Templates(directory="templates")
router = APIRouter()

async def login_handler(email: str = Form(...), password: str = Form(...)):
    conn = Database.get_connection()
    cur = conn.cursor()
    print(email, password)
    cur.execute("SELECT password FROM users WHERE email=%s", (email,))
    record = cur.fetchone()
    
    if record and bcrypt.checkpw(password.encode("utf-8"), record[0].encode("utf-8")):
        return {"message": "Logged in successfully"}
    else:
        return {"error": "Invalid email or password."}

@router.post("/login_endpoint")
async def login(request: Request, email: str = Form(...), password: str = Form(...)):
    response = await login_handler(email, password)
    if "message" in response:
        return RedirectResponse(url="/dashboard", status_code=302)
    return templates.TemplateResponse("login.html", {"request": request, "error": response["error"]})
