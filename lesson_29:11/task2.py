# Дано строка символов. Подсчитать:
# а) сколько раз среди данных символов встречается символ + и сколько раз символ *;
# б) общее число вхождений символов +, -, * в строку

if __name__ == '__main__':

    string = input('Введите строку: ')
    count_all, count_plus, count_star = 0, 0, 0

    for s in string:
        if s == '+':
            count_plus += 1

        if s == '*':
            count_star += 1

        if s == '+' or s == '-' or s == '*':
            count_all += 1

    print(f'Символ + встречается {count_plus}')
    print(f'Символ * встречается {count_star}')
    print(count_all)