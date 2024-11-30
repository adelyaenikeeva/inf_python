# Напишите программу, которая проверяет, содержится ли данное слово в строке,
# и если да, то возвращает его индекс.

if __name__ == '__main__':
    input_string = input('Введите строку: ').split()
    input_word = input('Введите слово: ')

    found = False

    for index, value in enumerate(input_string):
        if input_word == value:
            print(index)
            found = True
            break

    if not found:
        print('слово не найдено')
