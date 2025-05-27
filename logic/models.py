from datetime import datetime

class Expense:
    def __init__(self, title: str, category: str, amount: float, date_str: str):
        self.title = title
        self.category = category
        self.amount = amount
        self.date = datetime.strptime(date_str, "%d.%m")

    def month(self):
        return self.date.strftime("%m")