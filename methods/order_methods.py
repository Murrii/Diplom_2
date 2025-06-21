import allure
import requests
from data import BASE_URL, ORDER_URL

class OrderMethods:
    def __init__(self):
        self.url = BASE_URL + ORDER_URL

    @allure.step("Создаем заказ без авторизации")
    def create_order_without_auth(self, ingredients):
        response = requests.post(url=self.url, data={"ingredients": ingredients})
        return response.status_code, response.json()

    @allure.step("Создаем заказ с авторизацией")
    def create_order_with_auth(self, access_token, ingredients):
        response = requests.post(url=self.url, headers={"authorization": access_token}, data={"ingredients": ingredients})
        return response.status_code, response.json()

    @allure.step("Получаем список заказов пользователя с авторизацией")
    def get_orders_list_with_auth(self, access_token):
        response = requests.get(url=self.url, headers={"authorization": access_token})
        return response.status_code, response.json()

    @allure.step("Получаем список заказов пользователя без авторизации")
    def get_orders_list_without_auth(self):
        response = requests.get(url=self.url)
        return response.status_code, response.json()