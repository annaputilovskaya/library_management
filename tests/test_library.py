import unittest

from src.library import Library


class TestLibray(unittest.TestCase):
    def setUp(self):
        self.library = Library('test.json')
        self.library.books = []

    def test_add_book(self):
        self.library.add_book("Book1", "author1", 2000)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Book1")

    def test_add_book_with_incorrect_year(self):
        self.library.add_book("Book1", "author1", 865)
        self.assertEqual(len(self.library.books), 0)

    def test_get_book_by_id(self):
        self.library.add_book("Book1", "author1", 2000)
        self.assertEqual(self.library.get_book_by_id(1), self.library.books[0])

    def test_get_book_by_wrong_id(self):
        with self.assertRaises(ValueError):
            self.library.get_book_by_id(1)

    def test_delete_book(self):
        self.library.add_book("Book1", "author1", 2000)
        self.library.delete_book(1)
        self.assertEqual(len(self.library.books), 0)

    def test_delete_book_by_wrong_id(self):
        self.library.add_book("Book1", "author1", 2000)
        self.library.delete_book(2)
        self.assertEqual(len(self.library.books), 1)

    def test_get_books_by_query(self):
        self.library.add_book("Book1", "author1", 2000)
        self.library.add_book("Book2", "author1", 2003)
        self.library.add_book("Test", "book_author", 2003)
        result1 = self.library.get_books_by_query("book", "1")
        self.assertEqual(len(result1), 2)
        result2 = self.library.get_books_by_query("book")
        self.assertEqual(len(result2), 3)
        result3 = self.library.get_books_by_query("author1", "2")
        self.assertEqual(len(result3), 2)
        result4 = self.library.get_books_by_query("2000", "3")
        self.assertEqual(len(result4), 1)
        result4 = self.library.get_books_by_query("2000", "1")
        self.assertEqual(len(result4), 0)

    def test_change_status(self):
        self.library.add_book("Book1", "author1", 2000)
        self.library.change_status(1, "выдана")
        self.assertEqual(self.library.books[0].status, "выдана")

    def test_change_to_incorrect_status(self):
        self.library.add_book("Book1", "author1", 2000)
        self.library.change_status(1, "новая")
        self.assertEqual(self.library.books[0].status, "в наличии")
