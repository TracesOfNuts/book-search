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
        print(f"\nSearch by category: {search_string}")
        print("Search Results:")
        for i, book in enumerate(books):
            print(f"  {i}. {book}")
        self.assertEqual(len(books), 2)

    def test_search_books_by_title(self):
        search_string = "book " # Note the trailing space at the end
        self.library.add_book("Book 1", "Author 1", "A")
        self.library.add_book("Book 2", "Author 2", "B")
        self.library.add_book("Another Book", "Author 3", "A")

        books = self.library.search_books(title=search_string)
        print(f"\nSearch by title: {search_string}")
        print("Search Results:")
        for i, book in enumerate(books):
            print(f"  {i}. {book}")        
        self.assertEqual(len(books), 2)

    def test_search_books_by_author(self):
        search_string = "th"
        self.library.add_book("Book 1", "Author 1", "A")
        self.library.add_book("Book 2", "Author 2", "B")
        self.library.add_book("Another Book", "Another Author", "A")

        books = self.library.search_books(author_last_name=search_string)
        print(f"\nSearch by author: {search_string}")
        print("Search Results:")
        for i, book in enumerate(books):
            print(f"  {i}. {book}")
        self.assertEqual(len(books), 3)

    def test_search_books_by_category_and_title(self):
        category = "A"
        title = "book"
        self.library.add_book("Book 1", "Author 1", "A")
        self.library.add_book("Book 2", "Author 2", "B")
        self.library.add_book("Another Book", "Author 3", "A")

        books = self.library.search_books(category=category, title=title)
        print(f"\nSearch by category: {category} and title: {title}")
        print("Search Results:")
        for i, book in enumerate(books):
            print(f"  {i}. {book}")
        self.assertEqual(len(books), 2)

    def test_search_books_by_category_and_author(self):
        category = "A"
        author = "th"
        self.library.add_book("Book 1", "Author 1", "A")
        self.library.add_book("Book 2", "Author 2", "B")
        self.library.add_book("Another Book", "Another Author", "A")

        books = self.library.search_books(category=category, author_last_name=author)
        print(f"\nSearch by category: {category} and author: {author}")
        print("Search Results:")
        for i, book in enumerate(books):
            print(f"  {i}. {book}")
        self.assertEqual(len(books), 2)

    def test_search_books_by_title_and_author(self):
        title = "book"
        author = "th"
        self.library.add_book("Book 1", "Author 1", "A")
        self.library.add_book("Book 2", "Author 2", "B")
        self.library.add_book("Another Book", "Another Author", "A")

        books = self.library.search_books(title=title, author_last_name=author)
        print(f"\nSearch by title: {title} and author: {author}")
        print("Search Results:")
        for i, book in enumerate(books):
            print(f"  {i}. {book}")
        self.assertEqual(len(books), 3)

    def test_search_books_by_category_title_and_author(self):
        category = "A"
        title = "book"
        author = "another"
        self.library.add_book("Book 1", "Author 1", "A")
        self.library.add_book("Book 2", "Author 2", "B")
        self.library.add_book("Another Book", "Another Author", "A")
        
        books = self.library.search_books(category=category, title=title, author_last_name=author)
        print(f"\nSearch by category: {category}, title: {title}, and author: {author}")
        print("Search Results:")
        for i, book in enumerate(books):
            print(f"  {i}. {book}")
        self.assertEqual(len(books), 1)

    def test_search_books_by_no_criteria(self):
        books = self.library.search_books()
        self.assertEqual(len(books), 0)

    def test_search_books_that_do_not_exist(self):
        self.library.add_book("Book 1", "Author 1", "A")
        self.library.add_book("Book 2", "Author 2", "B")
        self.library.add_book("Another Book", "Another Author", "A")
        books = self.library.search_books(category="A", title="book 1", author_last_name="author 2")
        self.assertEqual(len(books), 0)

if __name__ == '__main__':
    unittest.main()