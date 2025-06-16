import allure
from methods.register_methods import RegisterMethods
import pytest


@pytest.fixture
@allure.step("создаем тестового юзера")
def user():
    user = RegisterMethods()
    user.register_new_user()
    return user