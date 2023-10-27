from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.route import router
from app.database import init_db
from app.middleware import CustomMiddleware

app = FastAPI()

init_db()

app.add_middleware(CustomMiddleware)
app.include_router(router)

app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8888)
