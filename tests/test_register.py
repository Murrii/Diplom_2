import allure
import pytest

from methods.register_methods import RegisterMethods
from methods.user_methods import UserMethods
from data import REGISTER_ERROR_NOT_UNIC_USER as NOT_UNIC_USER
from data import REGISTER_ERROR_MISSED_REQUIRED_FIELD as MISSED_REQUIRED_FIELD


class TestRegister:
    @allure.title("Создание уникального пользователя с валидными данными")
    def test_create_user_with_valid_unic_data_status_code_200(self):
        new_user = RegisterMethods()
        status_code, json = new_user.register_new_user()
        # проверяем, что статус код 200 и сохранен тот емейл, который мы передали
        assert status_code == 200 and json["user"]["email"] == new_user.email
        # удаляем созданного пользователя перед завершением теста
        UserMethods(new_user.access_token).delete_user()

    @allure.title("Создание не уникального пользователя")
    def test_create_not_unic_user_status_code_403(self):
        new_user = RegisterMethods()
        # создаем уникального пользователя
        new_user.register_new_user()
        # пытаемся создать пользователя с теми же данными еще раз
        status_code, json = new_user.register_new_user()
        assert status_code == 403 and json["message"] == NOT_UNIC_USER

    @allure.title("Создание пользователя с незаполненным обязательным полем (параметризация)")
    @pytest.mark.parametrize("not_valid_payload", [{"email": "ktrof_00001@yandex.ru", "password": "ktrof_00001@yandex.ru"},
                                                   {"email": "ktrof_00001@yandex.ru", "name": "ktrof_00001@yandex.ru"},
                                                   {"password": "ktrof_00001@yandex.ru","name": "ktrof_00001@yandex.ru"}])
    def test_create_user_without_one_required_field_status_code_403(self, not_valid_payload):
        new_user = RegisterMethods()
        status_code, json = new_user.register_new_user(not_valid_payload)
        assert status_code == 403 and json["message"] == MISSED_REQUIRED_FIELD

