# Напишите программу, которая создает словарь,
# где ключами являются символы строки, а значениями — число их вхождений.

if __name__ == '__main__':
    string = input('Введите строку: ')

    count_char = {}

    for char in string:
        if char in count_char:
            count_char[char] += 1
        else:
            count_char[char] = 1

    print(count_char)
