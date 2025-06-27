# урлы для апи-запросов
BASE_URL = "https://stellarburgers.nomoreparties.site/api/"
REGISTER_URL = "auth/register"
LOGIN_URL = "auth/login"
LOGOUT_URL = "auth/logout"
ORDER_URL = "orders"
USER_URL = "auth/user"

# тексты ошибок для невалидных запросов
REGISTER_ERROR_NOT_UNIC_USER = "User already exists"
REGISTER_ERROR_MISSED_REQUIRED_FIELD = "Email, password and name are required fields"

LOGIN_ERROR_NOT_VALID_DATA = "email or password are incorrect"

USER_NOT_AUTH_CHANGE = "You should be authorised"

CREATE_ORDER_WITHOUT_INGREDIENTS = "Ingredient ids must be provided"
CREATE_ORDER_WITH_WRONG_INGREDIENT_ID = "One or more ids provided are incorrect"

GET_ORDER_LIST_WITHOUT_AUTH = "You should be authorised"

# данные существующего пользователя для тестов авторизации с невалидными данными
LOGIN_DATA_WRONG_EMAIL = {
"email": "wrong_ktrof_006@yandex.ru",
"password": "ktrof_006@yandex.ru",
}

LOGIN_DATA_WRONG_PASS = {
"email": "ktrof_006@yandex.ru",
"password": "wrong_ktrof_006@yandex.ru",
}

# значение для тестов на изменение данных пользователя
CHANGE_DATA ="changed_ktrof_012@mail.ru"

# хеши ингредиентов для теста заказов
INGREDIENT_BUN_ID = "61c0c5a71d1f82001bdaaa6d"
INGREDIENT_MAIN_ID = "61c0c5a71d1f82001bdaaa71"
INGREDIENT_SAUCE_ID = "61c0c5a71d1f82001bdaaa72"
INGREDIENT_WRONG_ID = "61c0c5a71d1f82001bdaaa64"

# Данные пользователя для получения заказов пользователя

USER_WITH_ORDERS_DATA = {
"email": "ktrof_006@yandex.ru",
"password": "ktrof_006@yandex.ru"
}