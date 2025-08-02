from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class LoginRequestDict(TypedDict):
    '''
    описание тела запроса на аутентификацию
    '''
    email: str
    password: str

class RefreshRequestDict(TypedDict):
    '''
    описание тела запроса на рефреш токена
    '''
    refreshToken: str

class AuthenticationClient(APIClient):
    '''
    клиент для работы с аутентификацией
    '''
    def login_api(self, request: LoginRequestDict) -> Response:
        return self.post('/api/v1/authentication/login', json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        return self.post('/api/v1/authentication/refresh', json=request)
