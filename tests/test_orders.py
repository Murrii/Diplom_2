import allure
import pytest
from methods.order_methods import OrderMethods
from data import INGREDIENT_BUN_ID as BUN, INGREDIENT_MAIN_ID as MAIN, INGREDIENT_SAUCE_ID as SAUCE
from data import INGREDIENT_WRONG_ID as WRONG_ID, CREATE_ORDER_WITH_WRONG_INGREDIENT_ID, CREATE_ORDER_WITHOUT_INGREDIENTS
from data import USER_WITH_ORDERS_DATA
from data import GET_ORDER_LIST_WITHOUT_AUTH
from methods.login_methods import LoginMethods

class TestOrders:
    @allure.title("Создание заказа для авторизированного пользователя")
    @allure.description("Проверяем, что успешно создаются различные комбинации ингредиентов "
                        "и что имя заказчика совпадает с именем авторизованного пользователя")
    @pytest.mark.parametrize("ingredients_list", [BUN, MAIN, SAUCE, [BUN, MAIN, SAUCE]])
    def test_create_order_with_auth_status_code_200(self, user, ingredients_list):
        order = OrderMethods()
        status_code, json = order.create_order_with_auth(user.access_token, ingredients_list)
        assert status_code == 200 and json['order']["owner"]["name"] == user.name

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth_status_code_200(self):
        order = OrderMethods()
        status_code, json = order.create_order_without_auth([BUN, MAIN])
        assert status_code == 200 and json['success']

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients_status_code_400(self):
        order = OrderMethods()
        status_code, json = order.create_order_without_auth([])
        assert status_code == 400 and json["message"] == CREATE_ORDER_WITHOUT_INGREDIENTS

    @allure.title("Создание заказа с невалидным ингредиентом")
    def test_create_order_with_wrong_id_ingredient_status_code_400(self):
        order = OrderMethods()
        status_code, json = order.create_order_without_auth([WRONG_ID])
        assert status_code == 400 and json["message"] == CREATE_ORDER_WITH_WRONG_INGREDIENT_ID

    @allure.title("Получение списка заказов авторизированного пользователя")
    def test_get_order_list_with_auth_status_code_200(self):
        # получаем свежий токен в атрибутах объекта для пользователя из data
        login_user = LoginMethods(USER_WITH_ORDERS_DATA)
        login_user.login()
        # отправляем запрос списка заказов для пользователя из data
        status_code, json = OrderMethods().get_orders_list_with_auth(login_user.access_token)
        assert status_code == 200 and json["success"], print(json)

    @allure.title("Получение списка заказов не авторизированного пользователя")
    def test_get_order_list_without_auth_status_code_200(self):
        # отправляем запрос списка заказов без авторизации
        orders = OrderMethods()
        status_code, json = orders.get_orders_list_without_auth()
        assert status_code == 401 and json["message"] == GET_ORDER_LIST_WITHOUT_AUTH, print(json)
