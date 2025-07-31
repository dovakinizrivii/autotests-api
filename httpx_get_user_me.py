import httpx


login_payload = {
  "email": "user23@example.com",
  "password": "string"
}

login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()
accessToken = login_response_data['token']['accessToken']

headers = {
  "Authorization": f"Bearer {accessToken}"
}

response_get = httpx.get('http://localhost:8000/api/v1/users/me', headers=headers)
response_get_data = response_get.json()


print('Ответ на get', response_get_data)
print('код', response_get.status_code)