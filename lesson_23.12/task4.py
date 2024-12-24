# 4. Инвентаризация склада:
#    - Создайте класс `Warehouse`, который инкапсулирует информацию о товарах: `__product_id`, `__quantity`, `__location`.
#    - Напишите методы для перемещения товаров между локациями и пересчета наличных товаров.
#    - Реализуйте защиту от получения отрицательного количества товаров.

class Warehouse:
    def __init__(self, product_id, quantity, location):
        self.__product_id = product_id
        self.__quantity = quantity
        self.__location = location

    @property
    def product_id(self):
        return self.__product_id

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value > 0:
           self.__quantity = value
        else:
            print('Недопустимое значение')

    @property
    def location(self):
        return self.__location

    def move(self, new_location, amount):
        if amount > self.__quantity:
            print('Недостаточно товаров для перемещения')

        self.__quantity -= amount
        print(f'Перемещено {amount} единиц товара из {self.__location} в {new_location}')

        self.__location = new_location
        print(f'Новая локация: {self.__location}')

    def count_available(self):
        return self.__quantity


warehouse = Warehouse('01', 100, 'Склад 1')

print(warehouse.count_available())

warehouse.move('Склад 2', 50)

print(f'Оставшееся количество на складе: {warehouse.count_available()}')

warehouse.quantity = -5