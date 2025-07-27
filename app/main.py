'''Purpose: to initiate the program'''
from fastapi import FastAPI
from app.routes import router
from app.utils.db import init_db

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def root():
    return {"message": "AI Voice Agent Backend is running"}

