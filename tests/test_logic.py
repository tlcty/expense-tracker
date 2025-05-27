from logic.models import Expense
from logic.services import ExpenseTracker

def test_add_and_top_category():
    tracker = ExpenseTracker()
    tracker.add_expense(Expense("Молоко", "Еда", 120, "14.05"))
    tracker.add_expense(Expense("Икра", "Еда", 999, "14.05"))
    tracker.add_expense(Expense("Ноутбук", "Техника", 80000, "14.04"))

    assert tracker.top_category("05")[0] == "Еда"

def test_max_expense():
    tracker = ExpenseTracker()
    tracker.add_expense(Expense("Шашлык", "Еда", 550, "01.05"))
    tracker.add_expense(Expense("Мясо", "Еда", 600, "01.05"))
    assert tracker.max_expense("05", "Еда").title == "Мясо"