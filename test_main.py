import unittest

from main import EnhancedLibrarySystem

class TestEnhancedLibrarySystem(unittest.TestCase):
    def setUp(self):
        self.library = EnhancedLibrarySystem()

    def test_add_book(self):
        code = self.library.add_book("Book 1", "Author 1", "A")
        self.assertIsNotNone(code)
        self.assertIn(code, self.library.books_by_code)

    def test_add_book_with_invalid_category(self):
        with self.assertRaises(ValueError):
            self.library.add_book("Book 1", "Author 1", "X")

    def test_search_books_by_category(self):
        search_string = "A"
        self.library.add_book("Book 1", "Author 1", "A")
        self.library.add_book("Book 2", "Author 2", "B")
        self.library.add_book("Book 3", "Author 3", "A")

        books = self.library.search_books(category=search_string)
        self.assertEqual(len(books), 2)
        print(f"\nSearch by category: {search_string}")
        print("Search Results:")
        for i, book in enumerate(books):
            print(f"  {i}. {book}")

    def test_search_books_by_title(self):
        search_string = "book " # Note the trailing space at the end
        self.library.add_book("Book 1", "Author 1", "A")
        self.library.add_book("Book 2", "Author 2", "B")
        self.library.add_book("Another Book", "Author 3", "A")

        books = self.library.search_books(title=search_string)
        self.assertEqual(len(books), 2)
        print(f"\nSearch by title: {search_string}")
        print("Search Results:")
        for i, book in enumerate(books):
            print(f"  {i}. {book}")        

    def test_search_books_by_author(self):
        search_string = "th"
        self.library.add_book("Book 1", "Author 1", "A")
        self.library.add_book("Book 2", "Author 2", "B")
        self.library.add_book("Another Book", "Another Author", "A")

        books = self.library.search_books(author_last_name=search_string)
        self.assertEqual(len(books), 3)
        print(f"\nSearch by author: {search_string}")
        print("Search Results:")
        for i, book in enumerate(books):
            print(f"  {i}. {book}")

if __name__ == '__main__':
    unittest.main()