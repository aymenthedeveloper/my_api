import requests


endpoint = "http://127.0.0.1:8000/api/products/update/1"

data = {
    'title': 'hello world',
    'content': '',
    "price": 39.99
}

response = requests.put(endpoint, json=data)

print(response.json())