# Создайте класс `Product` с приватными атрибутами `__name` (строка, представляющая название товара),
# `__price` (число, представляющее цену товара) и `__quantity` (целое число, представляющее количество товаров).

# Затем создайте класс `ShoppingCart`, который будет содержать приватный атрибут `__items`
# (список словарей, каждый из которых содержит `name`, `price`, `quantity`).
# Реализуйте методы для добавления и удаления товаров, обновления количества товаров,
# а также метод для расчета общей стоимости товаров в корзине.

class Product:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price > 0:
            self.__price = price
        else:
            print('Недопустимое значение')

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if quantity > 0:
            self.__quantity = quantity
        else:
            print('Недопустимое значение')

    def __str__(self):
        return f'{self.__name}, {self.__price}, {self.__quantity}'

class ShoppingCart:
    def __init__(self):
        self.__items = []

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self.__items = value
        else:
            print('Значение должно быть списком')

    def add_product(self, product, quantity):
        for item in self.__items:
            if item['name'] == product.name:
                item['quantity'] += quantity
                return

        self.__items.append({
            'name': product.name,
            'price': product.price,
            'quantity': quantity
        })

    def remove_product(self, product_name):
        self.__items = [item for item in self.__items if item['name'] != product_name]

    def total_cost(self):
        return sum(item['price'] * item['quantity'] for item in self.__items)


product1 = Product('Яблоки', 1.2, 3)
product2 = Product('Бананы', 0.5, 20)
product1.quantity = -2

print(product1)

cart = ShoppingCart()

cart.add_product(product1, 3)
cart.add_product(product2, 5)

cart.remove_product('Бананы')

print(f'Общая стоимость: {cart.total_cost()}')

print(f'Продукты в корзине: {cart.items}')
