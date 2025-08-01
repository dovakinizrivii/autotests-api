import httpx

auth_payload = {
  "email": " ",
  "password": "string"
}

auth_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=auth_payload)
auth_response_data = auth_response.json()

client = httpx.Client(
    base_url="http://localhost:8000",
    timeout=100,
    headers={"Authorization": f"Bearer {auth_response_data['token']['accessToken']}"}
)

get_user_me_response = client.get('/api/v1/users/me')
get_user_me_response_data = get_user_me_response.json()

print('get user me data:', get_user_me_response_data)
