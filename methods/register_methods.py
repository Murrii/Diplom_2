import allure
import requests
from data import BASE_URL, REGISTER_URL
import random
import string


class RegisterMethods:
    @staticmethod
    def generate_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def __init__(self):
        # чтобы уменьшить количество генераций, генерируем одну строку и вставляем ее во все обязательные параметры
        generated_register_data = "ktrof_" + self.generate_string(4)+"@yandex.ru"
        self.email = generated_register_data
        self.password = generated_register_data
        self.name = generated_register_data
        self.access_token = None
        self.refresh_token = None

        # для удобства обращения сохраняем url как атрибут
        self.url = BASE_URL+REGISTER_URL

        # необходимые для регистрации данные в удобном формате
        self.register_payload = {
            "email": self.email,
            "password": self.password,
            "name": self.name
        }

    @allure.step("отправляем пост-запрос на регистрацию. Опционально - передаем данные для регистрации")
    def register_new_user(self, payload_data = None):
        # если данные для регистрации не получены, берем сгенерированный при создании объекта register_payload
        if payload_data is None:
            payload_data = self.register_payload
        # отправляем пост-запрос на регистрацию
        response = requests.post(url=self.url, data=payload_data)
        # если юзер успешно создан, сохраняем токены зарегистрированного пользователя для дальнейшей работы с ними
        # например, для удаления пользователя при завершении теста
        if response.status_code == 200:
            self.access_token = response.json()["accessToken"]
            self.refresh_token = response.json()["refreshToken"]
        # возвращаем статус-код и текст ответа для дальнейших проверок
        return response.status_code, response.json()


