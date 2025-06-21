import allure
from methods.register_methods import RegisterMethods
from methods.user_methods import UserMethods
import pytest
import string
import random


@pytest.fixture
@allure.title("генерируем данные для создания пользователя")
def generate_register_data():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(5))
    register_data = "ktrof_" + random_string + "@yandex.ru"
    return register_data

@pytest.fixture
@allure.title("создаем тестового юзера")
def user(generate_register_data):
    user = RegisterMethods(generate_register_data)
    user.register_new_user()
    yield user
    UserMethods(user.access_token).delete_user()


