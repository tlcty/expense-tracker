from fastapi import FastAPI
from pydantic import BaseModel
from logic.models import Expense
from logic.services import ExpenseTracker

app = FastAPI()
@app.get("/")
def index():
    return {"message": "ну вроде работает :) ."}
tracker = ExpenseTracker()

class ExpenseIn(BaseModel):
    title: str
    category: str
    amount: float
    date: str  # формат "дд.мм"

@app.post("/expenses")
def add_expense(exp: ExpenseIn):
    ## Добавление новой траты
    tracker.add_expense(Expense(exp.title, exp.category, exp.amount, exp.date))
    return {"status": "ok"}

@app.get("/stats/top_category")
def get_top_category(month: str):
    ## Категория с наибольшими тратами за месяц
    result = tracker.top_category(month)
    return {"category": result[0], "total": result[1]} if result else {"message": "Нет данных"}

@app.get("/stats/max-expense")
def get_max_expense(month: str, category: str = None):
    ## Самая крупная трата в категории за месяц
    e = tracker.max_expense(month, category)
    return {
        "title": e.title,
        "category": e.category,
        "amount": e.amount,
        "date": e.date.strftime("%d.%m")
    } if e else {"message": "Нет данных"}
