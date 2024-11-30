# 1.	Дана строка символов; подсчитать сколько раз среди символов строки встречается буква х.

if __name__ == '__main__':

    string = input('Введите строку: ')
    count = 0

    for s in string:
        if s == 'x':
            count +=1

    print(count)