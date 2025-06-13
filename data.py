# урлы для апи-запросов
BASE_URL = "https://stellarburgers.nomoreparties.site/api/"
REGISTER_URL = "auth/register"
LOGIN_URL = "auth/login"
LOGOUT_URL = "auth/logout"
ORDER_URL = ""
USER_URL = "auth/user"

# тексты ошибок для невалидных запросов
REGISTER_ERROR_NOT_UNIC_USER = "User already exists"
REGISTER_ERROR_MISSED_REQUIRED_FIELD = "Email, password and name are required fields"

LOGIN_ERROR_NOT_VALID_DATA = "email or password are incorrect"

# данные существующего пользователя для авторизации
LOGIN_DATA = {
"email": "ktrof_002@yandex.ru",
"password": "ktrof_002"
}