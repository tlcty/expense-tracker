import requests

def test_add_expense():
    r = requests.post("http://localhost:8008/expenses", json={
        "title": "Кофе",
        "category": "Еда",
        "amount": 100,
        "date": "18.05"
    })
    assert r.status_code == 200
