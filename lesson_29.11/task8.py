# Напишите программу, которая принимает список строк и возвращает строку,
# состоящую из этих строк, разделённых символом, который задаёт пользователь.

if __name__ == '__main__':
    input_string = input('Введите строку: ').split()
    symbol = input('Введите символ: ')

    result = ''

    for i in range(len(input_string)):
        result += input_string[i]

        if i < len(input_string) - 1:
            result += symbol

    print(result)