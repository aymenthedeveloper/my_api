import requests
from getpass import getpass

# endpoint = "http://127.0.0.1:8000/api/products/"
auth_endpoint = "http://127.0.0.1:8000/api/products/get-token/"
password = getpass("password: ")
data = {
    "username": "aymen",
    "password": password
}

token = requests.post(auth_endpoint, json=data)

print(token.json())


if token.status_code == 200:
    tkn = token.json()["token"]
    headers = {"authorization": f"Token {tkn}"}
    endpoint = "http://127.0.0.1:8000/api/products/list-or-create/"

    response = requests.get(endpoint, headers=headers)

    print(response.json())