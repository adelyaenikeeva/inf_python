# 3. Система управления задачами:
#    - Создайте класс `Task` с атрибутами `__description`, `__deadline`, `__status`.
#    - Напишите методы для изменения статуса задачи и обновления дедлайна.
#    - Создайте класс `TaskManager` для управления несколькими задачами с методами добавления и сортировки задач по дедлайну.
from operator import attrgetter

class Task:
    def __init__(self, description, deadline, status = "Новая"):
        self.__description = description
        self.__deadline = deadline
        self.__status = status

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_description):
        self.__description = new_description

    @property
    def deadline(self):
        return self.__deadline

    @deadline.setter
    def deadline(self, new_deadline):
        self.__deadline = new_deadline

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):
        self.__status = new_status

    def __str__(self):
        return f'Задача: {self.description}, Дедлайн: {self.deadline}, Статус: {self.status}'


class TaskManager:
    def __init__(self):
        self.__tasks = []

    def add_task(self, task):
        self.__tasks.append(task)

    # attrgetter — это функция из модуля operator в Python, которая используется для получения атрибутов объектов.
    # Функция attrgetter('deadline') создаёт объект, который возвращает значение атрибута deadline для каждого элемента в списке self.__tasks.
    # В методе sort, аргумент key принимает функцию, производящую значение, по которому будет происходить сортировка.
    # Таким образом, когда вызывается sort, он применяет функцию, возвращаемую attrgetter('deadline'), к каждому элементу списка self.__tasks.
    # В результате получается список значений deadline, по которым будет происходить сортировка задач.
    def sort_tasks_by_deadline(self):
        self.__tasks.sort(key=attrgetter('deadline'))

    def display_tasks(self):
        for task in self.__tasks:
            print(task)


task_manager = TaskManager()

task1 = Task('Написать отчет', '2024-07-18')
task2 = Task('Купить продукты', '2024-07-20')
task3 = Task('Проверить почту', '2024-07-19', 'В процессе')

task_manager.add_task(task1)
task_manager.add_task(task2)
task_manager.add_task(task3)

task_manager.display_tasks()

print('Сортировка:')
task_manager.sort_tasks_by_deadline()

task_manager.display_tasks()

task1.status = "В процессе"
task1.deadline = "2024-07-17"
print('Обновленная задача')
print(task1)
