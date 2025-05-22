import os

from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI()

load_dotenv()


@app.get("/")
async def root():
    return {os.getenv("SALUDO") or "No hay variable de entorno"}
