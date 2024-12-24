# - Создайте класс `Book` с атрибутами `__title`, `__author`, `__isbn`.
#    - Разработайте класс `Library` для управления книгами и пользователями, инкапсулируя операции выдачи и возврата книг.
#    - Реализуйте отчёт о самых популярных книгах.

class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def isbn(self):
        return self.__isbn

    def __str__(self):
        return f'Название: {self.__title}, Автор: {self.__author}, ISBN: {self.__isbn}'

class Library:
    def __init__(self):
        self.books = [] # список всех книг
        self.issue_records = {}  # записи о выданных книгах {ISBN: пользователь}
        self.popularity = {} # популярность книг {ISBN: количество выдач}

    def add_book(self, book):
        self.books.append(book)

    def issue_book(self, isbn, user):
        for book in self.books:
            if book.isbn == isbn:
                self.issue_records[isbn] = user
                self.popularity[isbn] = self.popularity.get(isbn, 0) + 1
                print(f'Книга {book.title} выдана пользователю {user}')
                return

    def return_book(self, isbn):
        if isbn in self.issue_records:
            self.issue_records.pop(isbn)
            print(f'Книга {isbn} возвращена в библиотеку')


    def most_popular_books(self):
        max_popularity_isbn = max(self.popularity, key=self.popularity.get)
        max_popularity_count = self.popularity[max_popularity_isbn]
        most_popular_book = self.find_book_by_isbn(max_popularity_isbn)

        if most_popular_book:
            return f'Самая популярная книга: {most_popular_book.title} (по кол-ву выдач {max_popularity_count})'
        else:
            return 'Книга не найдена'


    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None


book1 = Book('1984', 'Джордж Оруэлл', '12345')
book2 = Book('Война и мир', 'Лев Толстой', '67890')

library = Library()

library.add_book(book1)
library.add_book(book2)

library.issue_book('12345', 'User1')
library.issue_book('67890', 'User2')
library.issue_book('67890', 'User3')
library.return_book('12345')

popular_books = library.most_popular_books()
print(popular_books)
