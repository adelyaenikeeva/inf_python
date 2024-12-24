# 5. Игра "Угадай число":
#    - Создайте класс `GuessingGame` с приватными атрибутами `__secret_number`, `__attempts`.
#    - Напишите методы для угадывания числа пользователем и подсчета попыток.
#    - Добавьте метод `reset_game` для перезапуска игры с новым секретным числом.
import random


class GuessingGame:
    # можно инициализировать случайное число через random
    def __init__(self):
        self.__secret_number = random.randint(1, 100)
        self.__attempts = 0

    # можно установить конкретное значение (например, 10)
    # def __init__(self):
    #     self.__secret_number = 10
    #     self.__attempts = 0

    # можно передать случайное число при создании экземпляра класса
    # (secret_number=10 - значение по умолчанию)
    # (если при создании экземпляра класса не будет указан другой параметр,
    # то secret_number автоматически получит значение 10)
    # def __init__(self, secret_number=10):
    #     self.__secret_number = secret_number
    #     self.__attempts = 0

    @property
    def secret_number(self):
        return self.__secret_number

    @property
    def attempts(self):
        return self.__attempts

    def reset_game(self):
        self.__secret_number = random.randint(1, 100)
        self.__attempts = 0

    def guess(self, user_guess):
        self.__attempts += 1
        if user_guess < self.__secret_number:
            return 'Число больше'
        elif user_guess > self.__secret_number:
            return 'Число меньше'
        else:
            return 'Вы угадали число!'


if __name__ == "__main__":
    game = GuessingGame()
    print(f'Число: {game.secret_number}')

    while True:
        user_input = int(input('Угадайте число от 1 до 100: '))
        result = game.guess(user_input)
        print(result)
        if result == 'Вы угадали число!':
            print(f'Количество попыток: {game.attempts}')
            break

    game.reset_game()
    print(f'Перезапуск игры! Новое число: {game.secret_number}')
