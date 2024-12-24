# 7.	Менеджер задач:
# Создайте класс Task с атрибутами title, description, и completed.
# Реализуйте методы для отметки задачи как выполненной и изменения описания задачи.
# Создайте класс TaskManager, который будет управлять списком задач и предоставлять методы для добавления и поиска задач по названию.

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = 'Не выполнена'

    def completed_task(self):
        self.completed = 'Выполнена'

    def update_description(self, new_description):
        self.description = new_description

    def __str__(self):
        return f'Название: {self.title}, Описание: {self.description}, Статус: {self.completed}'


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if isinstance(task, Task):
            self.tasks.append(task)
            print(f'Задача {task.title} успешно добавлена')

    def find_task_by_title(self, name):
        found_tasks = []
        for task in self.tasks:
            if task.title == name:
                found_tasks.append(task)
        return found_tasks

    def display_info(self):
        return f'{self.tasks}'

task = Task('Купить продукты', 'Купить молоко, хлеб и яйца')
task2 = Task('Сделать домашку', 'Сделать математику и русский')

task.completed_task()
task2.update_description('Сделать математику')

print(task)
print(task2)

manager = TaskManager()
manager.add_task(task)
manager.add_task(task2)

tasks = manager.find_task_by_title('Купить продукты')
for t in tasks:
    print(t)