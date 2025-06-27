from methods.user_methods import UserMethods
from data import CHANGE_DATA, USER_NOT_AUTH_CHANGE
import allure
import pytest


class TestUser:
    @allure.title("Изменение параметров авторизированного пользователя (Параметризация)")
    @pytest.mark.parametrize("change_param", ["email", "password", "name"])
    def test_change_login_user_status_code_200(self, user, change_param):
        test_user = UserMethods(user.access_token)
        status_code, json = test_user.change_user_with_auth({change_param: CHANGE_DATA})
        assert status_code == 200 and json["success"] == True, print(status_code, json)

    @allure.title("Изменение параметров не авторизированного пользователя (Параметризация)")
    @pytest.mark.parametrize("change_param", ["email", "password", "name"])
    def test_change_not_login_user_status_code_401(self, user, change_param):
        test_user = UserMethods(user.access_token)
        status_code, json = test_user.change_user_without_auth({change_param: CHANGE_DATA})
        assert status_code == 401 and json["message"] == USER_NOT_AUTH_CHANGE, print(status_code, json)
