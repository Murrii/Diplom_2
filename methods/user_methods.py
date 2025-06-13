from data import BASE_URL, USER_URL
import requests
import allure


class UserMethods:
    def __init__(self, access_token):
        self.url = BASE_URL + USER_URL
        self.access_token = access_token
        self.user_payload = {"authorization": self.access_token}

    @allure.step("Удаляем пользователя")
    def delete_user(self):
        response = requests.delete(url=self.url, data=self.user_payload)
        return response.status_code, response.json()

