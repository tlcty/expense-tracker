from logic.models import Expense
from logic.services import ExpenseTracker

def demo():
    tracker = ExpenseTracker()
    tracker.add_expense(Expense("Хлеб", "Еда", 100, "15.05"))
    tracker.add_expense(Expense("Молоко", "Еда", 80, "15.05"))

    print("\nДемонстрация работы ExpenseTracker:")
    top = tracker.top_category("05")
    print(f"Топ категория за май: {top}")

    max_exp = tracker.max_expense("05", "Еда")
    print(f"Максимальная трата в 'Еда': {max_exp.title} — {max_exp.amount}")

if __name__ == "__main__":
    demo()