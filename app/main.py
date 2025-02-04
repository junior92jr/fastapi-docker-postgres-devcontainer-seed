from fastapi import FastAPI

from app.routers import hello, items
from app.database import engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(hello.router)
app.include_router(items.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI project seed!"}
