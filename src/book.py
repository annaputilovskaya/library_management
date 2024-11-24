from datetime import datetime


class Book:
    """
    Класс книги.
    """

    STATUS_CHOICE = ("в наличии", "выдана")

    def __init__(self, id, title, author, year, status=STATUS_CHOICE[0]):
        """
        Инициализирует экземпляр класса Book.
        """
        self.id = id
        self.title = title
        self.author = author.title()
        self.year = year
        self.status = status

    def __str__(self) -> str:
        """
        Отображает строковое представление книги пользователю.
        """
        num = str(self.id).rjust(6, "0")
        return f'{num}. "{self.title}" {self.author} - {self.year} ({self.status})'

    def __repr__(self) -> str:
        """
        Отображает строковое представление книги для отладки.
        """
        return f"{self.__class__.__name__}({self.id=},{self.title=},{self.author=}, {self.year=}, {self.status=})"

    def convert_to_dict(self) -> dict[str : int | str]:
        """
        Преобразует атрибуты экземпляра класса Book в словарь.
        """
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        current_year = datetime.now().year
        if 868 <= int(year) <= current_year:
            self.__year = year
        else:
            raise ValueError()
