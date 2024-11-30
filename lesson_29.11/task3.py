# Напишите программу, которая удаляет все повторяющиеся символы из строки,
# сохраняя порядок их первого появления.

if __name__ == '__main__':

    string = input('Введите строку: ')

    seen = set()
    result = []

    for char in string:
        if char not in seen:
            seen.add(char)
            result.append(char)

    corrected_result = ''.join(result)
    print(corrected_result)