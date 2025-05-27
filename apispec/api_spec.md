# Дока: Expense Tracker
## Тесты
pytest --cov=logic tests/
coverage report -m  # Проверка покрытия
## Валидация
- `amount` > 0  
- `date` в формате `день.месяц` (например, "15.10")  
## Ошибки
```json
{
  "error": "Invalid date format",
  "details": "Expected 'день.месяц'"
}
```

## POST /expenses
Добавляет трату  
**Body (JSON):**
```json
{
  "title": "Хлеб",
  "category": "Еда",
  "amount": 100,
  "date": "15.05"
}
```

##
