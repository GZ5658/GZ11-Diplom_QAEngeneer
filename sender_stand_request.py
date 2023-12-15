#Гизатуллин Зинур, 11 когорта - Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data

# Создание набора
def create_new_orders(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body, # тело
                         headers=data.headers) # заголовки

order_response = create_new_orders(data.create_orders);
track_number = order_response.json()["track"] # Сохранение номера заказа

# Получение данных о заказе по его номеру
def new_orders_info(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.ORDERS_INFO,
                        params={"t": track_number}, # тело
                        headers=data.headers)
    # Проверяется, что код ответа равен 200
    assert order_response.status_code == 200
    # Проверка, что в теле ответа атрибут "code" равен 200
    assert order_response.json()["code"] == 200
order_code = order_response.status_code
info_response = new_orders_info(track_number)

# Тест 1. Создание заказа (test_create_order)
def test_create_new_order():
    print("\nЗаказ успешно создан\nНомер заказа:", track_number)

# Тест 2. Проверка сохранения номера заказа
def test_save_track_number():

    print ("\nНомер заказа", track_number, "успешно сохранен")

# Тест 3. Выполнение запроса на получения заказа по треку заказа.
def test_new_orders_info():
    print("\n", info_response.json())

# Тест 4. Проверяется, что код = 2xx
def test_code():
    print("\n", order_code)
