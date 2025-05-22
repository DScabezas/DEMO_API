from fastapi import FastAPI
from dotenv import load_dotenv
import os

app = FastAPI()

load_dotenv()

@app.get("/")
async def root():
    return {os.getenv("SALUDO") or "No hay variable de entorno"}