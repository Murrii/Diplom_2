from data import BASE_URL, USER_URL
import requests
import allure


class UserMethods:
    def __init__(self, access_token):
        self.url = BASE_URL + USER_URL
        self.access_token = access_token
        # data для изменения/удаления пользователя
        self.access_token_payload = {"authorization": self.access_token}

    @allure.step("Удаляем пользователя")
    def delete_user(self):
        response = requests.delete(url=self.url, headers=self.access_token_payload)
        return response.status_code, response.json()

    @allure.step("Изменяем данные пользователя (с авторизацией)")
    def change_user_with_auth(self, new_data):
        response = requests.patch(url=self.url, headers=self.access_token_payload, data=new_data)
        return response.status_code, response.json()

    @allure.step("Изменяем данные пользователя (без авторизации)")
    def change_user_without_auth(self, new_data):
        response = requests.patch(url=self.url, data=new_data)
        return response.status_code, response.json()
