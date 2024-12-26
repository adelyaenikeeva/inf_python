# 12.	Создайте базовый класс Employee, который имеет атрибуты name и salary. Создайте дочерние классы Manager и Developer.
# Требования:
# В классе Employee добавьте метод get_info() для получения имени и зарплаты.
# В классе Manager добавьте атрибут team_size (размер команды) и метод get_team_info(), который возвращает информацию о менеджере и размере его команды.
# В классе Developer добавьте атрибут programming_languages (список языков программирования) и метод get_languages(), который возвращает строку с языками.

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            print('Значение должно быть строкой')

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value > 0 and isinstance(value, (int, float)):
            self.__salary = value
        else:
            print('Недопустимое значение')

    def get_info(self):
        # print(f'Name: {self.__name}, Salary: {self.__salary}')
        return f'Name: {self.__name}, Salary: {self.__salary}'


class Developer(Employee):
    def __init__(self, name, salary, programming_languages):
        super().__init__(name, salary)
        self.__programming_languages = programming_languages

    def get_languages(self):
        return self.__programming_languages

    def get_info(self):
        # super().get_info()
        # print(f'Programming languages: {self.__programming_languages}')

        return f'{super().get_info()}, Programming languages: {self.get_languages()}'

developer = Developer('Developer', 20000, ['java', 'python'])
print(developer.get_info())
print(developer.get_languages())
