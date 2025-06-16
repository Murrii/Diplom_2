import requests
from data import BASE_URL, ORDER_URL

class OrderMethods:
    def __init__(self):
        self.url = BASE_URL + ORDER_URL

    def create_order_without_auth(self, ingredients):
        response = requests.post(url=self.url, data={"ingredients": ingredients})
        return response.status_code, response.json()

    def create_order_with_auth(self, access_token, ingredients):
        response = requests.post(url=self.url, headers={"authorization": access_token}, data={"ingredients": ingredients})
        return response.status_code, response.json()