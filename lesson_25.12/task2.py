
# 2.	Создайте базовый класс EducationalInstitution, который будет иметь атрибуты __name и location.
# Создайте дочерние классы School и University.
# Требования:
# В классе EducationalInstitution добавьте метод get_details() для получения информации об учебном заведении.
# В классе School добавьте атрибут number_of_students (количество студентов) и метод get_student_count(),
# который возвращает количество студентов.
# В классе University добавьте атрибут number_of_faculties (количество факультетов) и метод get_faculty_count(),
# который возвращает количество факультетов.


class EducationalInstitution:
    def __init__(self, name, location):
        self.__name = name
        self.__location = location

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            print('Недопустимый тип данных')

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, new_location):
        if isinstance(new_location, str):
            self.__location = new_location
        else:
            print('Недопустимый тип данных')

    # def __str__(self):
    #     return f'Name: {self.__name}, Location: {self.__location}'

    def get_details(self):
        print(f'Name: {self.__name}, Location: {self.__location}')


class School(EducationalInstitution):
    def __init__(self, name, location, number_of_students):
        super().__init__(name, location)
        self.__number_of_students = number_of_students

    @property
    def number_of_students(self):
        return self.__number_of_students

    @number_of_students.setter
    def number_of_students(self, value):
        if value > 0:
            self.__number_of_students = value
        else:
            print('Недопустимое значение')

    def get_students_count(self):
        return f'Кол-во студентов: {self.__number_of_students}'

    def get_details(self):
        super().get_details()
        print(f'Number of students: {self.__number_of_students}')


school = School('KFU', 'Kazan', 30)
# school.number_of_students = -20
school.location = 'KFU 2'
print(school.name)
school.get_details()
