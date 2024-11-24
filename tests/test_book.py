import unittest

from src.book import Book


class TestBook(unittest.TestCase):
    def test_initial_book(self):
        book = Book(1, "Book1", "author1", 2000)
        self.assertEqual(book.title, "Book1")
        self.assertEqual(book.status, "в наличии")

    def test_initial_book_with_incorrect_year(self):
        with self.assertRaises(ValueError):
            Book(2, "Book2", "author2", 865)
        with self.assertRaises(ValueError):
            Book(3, "Book3", "author3", 2026)
        with self.assertRaises(ValueError):
            Book(4, "Book4", "author4", "2023 год")

    def test_str_book(self):
        book = Book(5, "Book5", "author5", 2000)
        self.assertEqual(str(book), '000005. "Book5" Author5 - 2000 (в наличии)')

    def test_repr_book(self):
        book = Book(6, "Book6", "author6", 2000)
        self.assertEqual(
            repr(book),
            "Book(self.id=6,self.title='Book6',self.author='Author6', self.year=2000, self.status='в наличии')",
        )

    def test_convert_to_dict(self):
        book = Book(7, "Book7", "author7", 2000)
        book_dict = {
            "id": 7,
            "title": "Book7",
            "author": "Author7",
            "year": 2000,
            "status": "в наличии",
        }
        self.assertEqual(book.convert_to_dict(), book_dict)
