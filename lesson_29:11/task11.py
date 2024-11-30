# Напишите программу, которая переворачивает строку,
# используя только методы форматирования и манипуляции со строками, без использования срезов

if __name__ == '__main__':

    input_string = input('Введите строку: ')

    reversed_string = ''

    for i in range(len(input_string) - 1, -1, -1):
        reversed_string += input_string[i]

    print(reversed_string)

