import allure
import requests
from data import BASE_URL, LOGIN_URL, LOGIN_DATA

class LoginMethods:
    def __init__(self):
        self.url = BASE_URL + LOGIN_URL
        self.refresh_token = None

    @allure.step("Авторизируемся в приложении. Опционально - передаем данные для авторизации")
    def login(self, payload_data=None):
        # Если данные для авторизации не получены, используем данные из data
        if payload_data is None:
            payload_data = LOGIN_DATA

        # отправляем запрос на авторизацию
        response = requests.post(url=self.url, data = payload_data)

        # если авторизация прошла успешно, сохраняем refresh_token для последующего логаута
        if response.status_code == 200:
            self.refresh_token = response.json()["refreshToken"]
        return response.status_code, response.json()
