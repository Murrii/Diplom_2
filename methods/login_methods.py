import allure
import requests
from data import BASE_URL, LOGIN_URL

class LoginMethods:
    def __init__(self, user_data):
        self.url = BASE_URL + LOGIN_URL
        self.user_data = user_data
        self.access_token = None
        self.refresh_token = None

    @allure.step("Авторизируемся в приложении")
    def login(self):
        # отправляем запрос на авторизацию
        response = requests.post(url=self.url, data = self.user_data)

        # если авторизация прошла успешно, сохраняем access_token, refresh_token для последующей работы с пользователем
        if response.status_code == 200:
            self.refresh_token = response.json()["refreshToken"]
            self.access_token = response.json()["accessToken"]
        return response.status_code, response.json()
