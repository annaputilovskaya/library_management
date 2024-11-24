import json
import os

from src.book import Book


class Library:
    """
    Класс библиотеки.
    """

    def __init__(self, filename="library.json"):
        """
        Инициализирует экземпляр класса Library.
        """
        self.file_path = os.path.join("data", filename)
        self.books = self.load_books()

    def load_books(self) -> list[Book]:
        """
        Возвращает список книг библиотеки, сохраненный в файле.
        Если путь к файлу не существует, возвращает пустой список.
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as file:
                return [Book(**data) for data in json.load(file)]
        return []

    def save_books(self):
        """
        Сохраняет список книг библиотеки в файл в виде списка словарей с атрибутами книг.
        """
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(
                [book.convert_to_dict() for book in self.books],
                file,
                ensure_ascii=False,
                indent=4,
            )

    def add_book(self, title, author, year):
        """
        Добавляет файл в библиотеку.
        """
        if not self.books:
            book_id = 1
        else:
            last_book = self.books[-1]
            book_id = last_book.id + 1
        try:
            new_book = Book(book_id, title, author, year)
        except ValueError:
            print(
                f"Невозможно добавить книгу. "
                f"Год издания книги - числовое значение, "
                f"которе не может быть ранее 868 года или позднее текущего."
            )
        else:
            self.books.append(new_book)
            self.save_books()
            print(f"Книга '{new_book}' добавлена в библиотеку.")

    def get_book_by_id(self, book_id) -> Book:
        """
        Получает книгу по ее идентификатору.
        """
        if not book_id.isdigit():
            raise ValueError("Книга не найдена. Идентификатор книги может иметь только числовое значение.")
        else:
            books_list = list(filter(lambda book: book.id == int(book_id), self.books))
            if books_list:
                return books_list[0]
            else:
                raise ValueError(f"Книга с id {book_id} не найдена.")

    def delete_book(self, book_id):
        """
        Удаляет книгу по ее идентификатору.
        """
        try:
            book = self.get_book_by_id(book_id)
        except ValueError as e:
            print(e.args[0])
        else:
            self.books.remove(book)
            self.save_books()
            print(f"Книга {book} удалена.")

    def get_books_by_query(self, query, filter_by=None) -> list[Book]:
        """
        Возвращает результат поиска книг в библиотеке по введенному запросу.
        Возможен поиск по названию, автору, году издания
        и по всем вышеуказанным параметрам одновременно.
        """
        query = query.lower()
        if filter_by == "1":
            results = list(filter(lambda book: query in book.title.lower(), self.books))
        elif filter_by == "2":
            results = list(
                filter(lambda book: query in book.author.lower(), self.books)
            )
        elif filter_by == "3":
            results = list(
                filter(lambda book: str(query) in str(book.year), self.books)
            )
        else:
            results = list(
                filter(
                    lambda book: query in book.title.lower()
                    or query in book.author.lower()
                    or str(query) in str(book.year),
                    self.books,
                )
            )
        return results

    def display_books(self):
        """
        Выводит на экран список всех книг библиотеки.
        """
        [print(book) for book in self.books]

    def change_status(self, book_id, status):
        """
        Меняет статус книги в библиотеке.
        """
        status = status.lower()
        if status not in Book.STATUS_CHOICE:
            print("Некорректный статус. Доступные: 'в наличии', 'выдана'.")
        else:
            try:
                book = self.get_book_by_id(book_id)
            except ValueError as e:
                print(e.args[0])
            else:
                book.status = status
                self.save_books()
                print(f"Статус книги изменен. {book}.")
