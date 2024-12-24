# 6. Создание игровых персонажей:
# Создайте класс Character с атрибутами name, health, strength.
# Реализуйте метод attack, который уменьшает здоровье другого
# персонажа на величину strength.
# Создайте несколько экземпляров и проведите между ними битву.

class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self, character):
        if isinstance(character, Character):
            print(f'{self.name} атакует {character.name} и уменьшает силу на {self.strength}')
            character.health -= self.strength

    def __str__(self):
        return f'{self.name}: Здоровье = {self.health}, Сила = {self.strength}'


character1 = Character('Персонаж1', 100, 20)
character2 = Character('Персонаж2', 80, 15)

print(character1)
print(character2)

character1.attack(character2)
character2.attack(character1)

print(character1)
print(character2)
