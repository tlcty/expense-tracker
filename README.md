# Expense Tracker
Сервис для отслеживания трат по категориям с RESTful API

## Результаты проекта
**Готово**:
- Добавление трат через REST API (`POST /expense`)
- Полная документация API
- Авто (pytest) и CI/CD (GitHub Actions)

**Решённые проблемы**:
- Валидация формата даты ("день.месяц")
- Конфликты слияния Git-веток

## Запуск
**Установка зависимостей**
```
pip install -r requirements.txt
```
**Запуск сервера**
```
uvicorn main:app --reload
```
## Примеры запросов
**Добавить трату**
```
curl -X POST "http://localhost:8008/expense" \
-H "Content-Type: application/json" \
-d '{"name":"Молоко", "amount":100, "category":"Еда", "date":"15.10"}'
```
**Ответ**
```
{
  "status": "ok",
  "expense_id": 1
}
```
## Технологии
Python 3.10+
FastAPI
Pytest
GitHub
