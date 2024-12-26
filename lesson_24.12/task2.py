# 2.	Создайте класс "Человек" с приватными полями для хранения имени, возраста и адреса.
# Реализуйте методы, которые позволяют изменять адрес и возраст, но не имя.
# Добавьте метод для вывода полной информации о человеке.

class Person:
     def __init__(self, name, age, address):
         self.__name = name
         self.__age = age
         self.__address = address

     @property
     def name(self):
         return self.__name

     @property
     def age(self):
         return self.__age

     @age.setter
     def age(self, new_age):
         if new_age > 0:
             self.__age = new_age
         else:
             print('Недопустимое значение')

     @property
     def address(self):
         return self.__address

     @address.setter
     def address(self, address):
         if isinstance(address, str):
             self.__address = address
         else:
             print('Значение должно быть строкой')

     def __str__(self):
         return f'Name: {self.__name}, Age: {self.__age}, Address: {self.__address}'

person = Person('Name', 20, 'Address')
# person.address = 'new address'
# person.address = 12345
print(person)


