# Класс "Температура": Создайте класс Температура с закрытым
# полем для значения температуры в градусах Цельсия. Реализуйте методы
# конвертации температуры в Фаренгейты и обратно, включая доступ к
# изначальному значению.

class Temperature:
    def __init__(self, temperature):
        self.__temperature_c = temperature
        self.__temperature_f = None
        self.convert_to_fahrenheit()

    @property
    def temperature(self):
        return self.__temperature_c

    @temperature.setter
    def temperature(self, new_temperature):
        if isinstance(new_temperature, (int, float)):
            self.__temperature_c = new_temperature
            self.convert_to_fahrenheit()
        else:
            print('Недопустимое значение')

    @property
    def temperature_f(self):
        return self.__temperature_f

    def convert_to_fahrenheit(self):
        self.__temperature_f = (self.__temperature_c * 9/5) + 32
        return self.__temperature_f

    def convert_to_celsius(self):
        self.__temperature_c = (self.__temperature_f - 32) * 5/9
        self.convert_to_fahrenheit()
        return self.__temperature_c

    def __str__(self):
        return f'Celsius: {self.__temperature_c}, Fahrenheit: {self.__temperature_f}'


if __name__ == '__main__':
    temp = Temperature(40)
    # print(temp.temperature)
    #
    # temp.temperature = '20'

    print(temp)
    # print(temp.temperature_f)

    temp.temperature = -20
    print(temp.convert_to_celsius())
    print(temp)
    print(temp.temperature)


