from methods.login_methods import LoginMethods
from methods.logout_methods import LogoutMethods
from data import LOGIN_ERROR_NOT_VALID_DATA
import allure
import pytest


class TestLogin:
    @allure.title("Логин под существующим пользователем")
    def test_login_with_valid_data_status_code_200(self):
        user = LoginMethods()
        status_code, json = user.login()
        assert status_code == 200 and json["success"] == True
        LogoutMethods().logout(user.refresh_token)

    @allure.title("Логин с неверным логином/паролем (параметризация)")
    @pytest.mark.parametrize("wrong_logout_data", [{"email": "666_ktrof_002@yandex.ru", "password": "ktrof_002"},
                                                   {"email": "ktrof_002@yandex.ru", "password": "666_ktrof_002"}])
    def test_login_with_wrong_data_status_code_401(self, wrong_logout_data):
        user = LoginMethods()
        status_code, json = user.login(wrong_logout_data)
        assert status_code == 401 and json["message"] == LOGIN_ERROR_NOT_VALID_DATA
