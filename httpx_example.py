import httpx




data = {
    'title': 'Новая задача',
    'completed': False,
    'UserId': 1
}

response = httpx.post('https://jsonplaceholder.typicode.com/todos', json=data)

print(response.status_code)
print(response.json())
print(response.request.headers)

data = {"username": "test_user", "password": "123456"}

response = httpx.post("https://httpbin.org/post", data=data)
print(response.status_code)
print(response.json())
print(response.request.headers)


with httpx.Client() as client:                                               # Создает сессию дял запросов
    r1 =client.get('https://jsonplaceholder.typicode.com/todos/1')
    r2 =client.get('https://jsonplaceholder.typicode.com/todos/2')
print(r1.json())
print(r2.json())

client = httpx.Client(headers={'autorization': 'bearer 213213123'})
response = client.get('https://httpbin.org/get')
print(response.json())

try:                                                                           # Внутри try выполняется код, который может вызвать ошибку.
    response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f'ошибка {e}')

try:
    response = httpx.get('https://httpbin.org/delay/5', timeout=2)
except httpx.ReadTimeout:
    print('время превышенл')

