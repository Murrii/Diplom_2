import requests
from data import BASE_URL, LOGOUT_URL


class LogoutMethods:
    def __init__(self):
        self.url = BASE_URL+LOGOUT_URL

    def logout(self, access_token):
        payload = {"authorization": access_token}
        response = requests.post(url = self.url, headers=payload)
        return response.status_code, response.json()
