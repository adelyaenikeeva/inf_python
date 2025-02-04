# 3.	Реализуйте программу, которая открывает файл, указанной пользователем, считывает его содержимое и выводит на экран.
# Если файла не существует, обработайте исключение FileNotFoundError и попросите пользователя ввести корректное имя файла.

while True:
    try:
        file_name = input('Введите имя файла: ')
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
            break
    except FileNotFoundError as e:
        print(e)
        print('Введите корректное имя файла!')