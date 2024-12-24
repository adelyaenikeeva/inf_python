# 3.	Оценка студентов:
# Создайте класс Student с атрибутами name и grades (список оценок).
# Реализуйте метод для добавления оценок, а также метод для вычисления среднего балла студента.

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.grades = []

    def add_grades(self, grade):
        self.grades.append(grade)

    def average_grades(self):
        if not self.grades:
            return 0.0
        else:
            return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, grades: {self.grades}'


student = Student(1, 'NAME')
print(student)
student.add_grades(5)
student.add_grades(3)
print(student)
print(student.average_grades())

