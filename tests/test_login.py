from methods.login_methods import LoginMethods
from data import LOGIN_ERROR_NOT_VALID_DATA, LOGIN_DATA_WRONG_EMAIL, LOGIN_DATA_WRONG_PASS
import allure
import pytest


class TestLogin:
    @allure.title("Логин под существующим пользователем")
    def test_login_with_valid_data_status_code_200(self, user):
        login_user = LoginMethods(user.user_data_payload)
        status_code, json = login_user.login()
        assert status_code == 200 and json["success"] == True

    @allure.title("Логин с неверным логином/паролем (параметризация)")
    @pytest.mark.parametrize("wrong_logout_data", [LOGIN_DATA_WRONG_EMAIL, LOGIN_DATA_WRONG_PASS])
    def test_login_with_wrong_data_status_code_401(self, wrong_logout_data):
        user = LoginMethods(wrong_logout_data)
        status_code, json = user.login()
        assert status_code == 401 and json["message"] == LOGIN_ERROR_NOT_VALID_DATA
