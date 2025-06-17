# Дока: Expense Tracker

## Тесты
- `pytest --cov=logic tests/ coverage report -m` - проверка покрытия

## Валидация
- `amount` > 0  
- `date` в формате `день.месяц` (например, "15.10")

## Ошибки
**Ошибка валидации**
```
{
  "error": "validation_error",
  "details": {
    "field": "date",
    "message": "Формат должен быть 'день.месяц'"
  }
}
```
```json
{
  "error": "Invalid date format",
  "details": "Expected 'день.месяц'"
}
```
## Эндпоинты

**POST /expense
Добавление новой траты**
```
{
  "name": "string (обязательно)",
  "amount": "number > 0",
  "category": "string",
  "date": "день.месяц"
}
```
Ответ
```
{
  "status": "ok",
  "message": "Expense added successfully"
}
```

**GET /top-category
Категория с наибольшими тратами за указанный месяц**
```
{
  "category": "Еда",
  "total": 1340
}
```
Ответ
```
{
  "category": "Еда",
  "total": 1340
}
```

**GET /max-expense
Самая крупная трата в категории за месяц**
```
{
  "title": "Икра",
  "category": "Еда",
  "amount": 999,
  "date": "14.05"
}
```
Ответ
```
{
  "title": "Икра",
  "category": "Еда",
  "amount": 999,
  "date": "14.05"
}
```

## Коды ошибок
```
400	Невалидные данные
404	Категория не найдена
500	Ошибка сервера
```
