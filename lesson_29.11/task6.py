# Напишите программу, которая принимает список строк и выводит каждую строку, повторённую дважды.

if __name__ == '__main__':

    string = input('Введите строку: ').split()

    dict_result = {}
    result = []

    for s in string:
        if s in dict_result:
            dict_result[s] += 1
        else:
            dict_result[s] = 1

    for string, count in dict_result.items():
        if count == 2:
            print(string)