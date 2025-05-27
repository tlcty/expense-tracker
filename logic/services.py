from logic.models import Expense

class ExpenseTracker: 
    def __init__(self):
        self.expenses = []

    def add_expense(self, exp: Expense):
        self.expenses.append(exp)

    def top_category(self, month: str):
        totals = {}
        for e in self.expenses:
            if e.month() == month:
                totals[e.category] = totals.get(e.category, 0) + e.amount
        return max (totals.items(), key=lambda x:x[1]) if totals else None
    def max_expense(self, month: str, category: str = None):
        filtered = [e for e in self.expenses if e.month() == month]
        if category:
            filtered = [e for e in filtered if e.category == category]
        return max(filtered, key=lambda e: e.amount) if filtered else None
