# 1.	Библиотека книг:
# Создайте класс Book с атрибутами title, author, и year.
# Создайте класс Library, который будет содержать список книг.
# Реализуйте методы для добавления книг в библиотеку, поиска книг по автору и вывода всех книг, изданных в определённом году.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # def display_info(self):
    #     return f'Название: {self.title}, Автор: {self.author}, Год: {self.year}'

    def __str__(self):
        return f'Название: {self.title}, Автор: {self.author}, Год: {self.year}'

book = Book('Title', 'Author', '2015')
print(book.year)

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f'Книга {book.title} успешно добавлена')
        else:
            print('Можно добавлять только объекты класса Book')

    def find_books_by_author(self, author):
        found_books = []
        for book in self.books:
            if book.author == author:
                found_books.append(book)
        return found_books

    def find_books_by_year(self, year):
        found_books = []
        for book in self.books:
            if book.year == year:
                found_books.append(book)
        return found_books


# library = Library()
# book1 = Book('1984', 'Джордж Оруэлл', 1949)
# print(book1)
# book2 = Book('Война и мир', 'Лев Толстой', 1867)
#
# library.add_book(book1)
# library.add_book(book2)
#
# books = library.find_books_by_author('Лев Толстой')
# for book in books:
#     print(book)
