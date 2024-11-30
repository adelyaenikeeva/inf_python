# Напишите программу, которая заменяет неправильные слова
# в строке на правильные (например, "срочня" на "срочно").

if __name__ == '__main__':

    words_dict = {
        'срочня': 'срочно',
        'инфа': 'информация'
    }

    string = input('Введите строку: ').split()
    corrected_words = []

    for s in string:
        if s in words_dict:
            corrected_words.append(words_dict[s])
        else:
            corrected_words.append(s)

    result = ' '.join(corrected_words)

    print(result)