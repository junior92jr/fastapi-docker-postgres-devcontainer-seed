import os
from fastapi import FastAPI
from app.routers import hello

if os.getenv("API_ENV") != "production":
    from dotenv import load_dotenv

    load_dotenv()

app = FastAPI()

app.include_router(hello.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI project seed!"}
