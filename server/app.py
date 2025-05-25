# server/app.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Expense Tracker API is running."}