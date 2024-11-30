# Напишите программу, которая извлекает все числа из строки и возвращает их в виде списка

if __name__ == '__main__':
    input_string = input('Введите строку: ')

    numbers = []
    current_number = ''

    for char in input_string:
        if char.isdigit():
            current_number += char
        else:
            if current_number:
                numbers.append(int(current_number))
                current_number = ''

    if current_number:
        numbers.append(int(current_number))

    print(numbers)