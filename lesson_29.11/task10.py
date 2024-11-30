# Напишите программу, которая принимает две строки и возвращает
# True, если они являются анаграммами (содержат одни и те же буквы в разном порядке).


if __name__ == '__main__':

    input_string_1 = input('Введите строку 1: ')
    input_string_2 = input('Введите строку 2: ')

    input_string_1 = input_string_1.replace(" ", "").lower()
    input_string_2 = input_string_2.replace(" ", "").lower()

    if len(input_string_1) != len(input_string_2):
        print('Длина не равна. Строки не могут быть анаграммами')
    else:

        is_anagram = True
        char_list = []

        for char in input_string_1:
            char_list.append(char)

        for char in input_string_2:
            if char in char_list:
                char_list.remove(char)
            else:
                is_anagram = False
                break

        print(is_anagram)

