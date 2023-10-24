from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
import bcrypt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Mock database
users_db = {
    "test@example.com": {
        "password": "$2y$12$..snip..",
        "username": "John Doe"
    }
}

def get_hashed_password(password: str):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password(plain_password: str, hashed_password: str):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def authenticate_user(email: str, password: str):
    if email in users_db and verify_password(password, users_db[email]["password"]):
        return users_db[email]
    raise HTTPException(status_code=401, detail="Incorrect email or password")

def get_current_user(token: str = Depends(oauth2_scheme)):
    if token in users_db:
        return users_db[token]
    raise HTTPException(status_code=401, detail="Invalid token")
