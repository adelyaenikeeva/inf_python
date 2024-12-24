# 9.	Моделирование магазина:
# Создайте класс Product с атрибутами name, price, и quantity.
# Создайте класс Store, который содержит список продуктов.
# Реализуйте методы для добавления продуктов, продажи (уменьшения количества) и вывода информации о товарах с низким запасом.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}: цена {self.price}, количество {self.quantity}'

class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f'Продукт {product.name} добавлен')

    def sell_product(self, name, quantity):
        for product in self.products:
            if product.name == name:
                product.quantity -= quantity
                print(f'Продано {quantity} единиц товара {name}')
                return

    def low_stock_info(self, threshold=3):
        print('Товары с низким запасом:')
        for product in self.products:
            if product.quantity <= threshold:
                print(product)

product = Product('Молоко', 1.0, 10)
store = Store()

store.add_product(product)
store.add_product(Product('Хлеб', 0.5, 5))
store.add_product(Product('Яблоки', 0.2, 2))

store.sell_product('Молоко', 5)
store.sell_product('Хлеб', 3)

store.low_stock_info()

