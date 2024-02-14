import uuid

class Book:
    def __init__(self, title, author_last_name, category):
        ALLOWED_CATEGORIES = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'}
        self.title = title
        self.author_last_name = author_last_name
        if category.upper() not in ALLOWED_CATEGORIES:
            raise ValueError(f"Invalid category: {category}")
        self.category = category.upper()  # Ensure category is uppercase for consistency
        self.unique_code = uuid.uuid4().hex  # Generates a 32-character hexadecimal unique ID

class EnhancedLibrarySystem:
    def __init__(self):
        self.books_by_code = {}  # Maps unique code to Book
        self.books_by_category = {}  # Maps category to list of unique codes
        self.books_by_title = {}  # Maps title substring to list of unique codes
        self.books_by_author = {}  # Maps author last name substring to list of unique codes


    def add_book(self, title, author_last_name, category):
        '''Adds a new book to the library system and returns the unique code of the book.'''
        new_book = Book(title, author_last_name, category)
        self.books_by_code[new_book.unique_code] = new_book
        self._index_by_category(new_book)
        self._index_by_title_substrings(new_book)
        self._index_by_author_substrings(new_book)
        return new_book.unique_code

    # Helper methods for add_book
    def _index_by_category(self, book):
        '''Indexes a book by its category.'''
        if book.category not in self.books_by_category:
            self.books_by_category[book.category] = []
        self.books_by_category[book.category].append(book.unique_code)

    def _index_by_title_substrings(self, book):
        '''Indexes a book by its title substrings.'''
        for i in range(len(book.title)):
            for j in range(i + 1, len(book.title) + 1):
                substring = book.title[i:j].lower()
                if substring not in self.books_by_title:
                    self.books_by_title[substring] = []
                if book.unique_code not in self.books_by_title[substring]:
                    self.books_by_title[substring].append(book.unique_code)

    def _index_by_author_substrings(self, book):
        '''Indexes a book by its author's last name substrings.'''
        for i in range(len(book.author_last_name)):
            for j in range(i + 1, len(book.author_last_name) + 1):
                substring = book.author_last_name[i:j].lower()
                if substring not in self.books_by_author:
                    self.books_by_author[substring] = []
                if book.unique_code not in self.books_by_author[substring]:
                    self.books_by_author[substring].append(book.unique_code)

    def search_books(self, category=None, title=None, author_last_name=None):
        '''Searches for books based on the given category, title, and/or author last name.'''
        category_results = set()
        title_results = set()
        author_results = set()

        if category:
            category = category.upper()
            category_results.update(self._search_books_by_category(category))

        if title:
            title = title.lower()
            title_results.update(self._search_books_by_title(title))

        if author_last_name:
            author_last_name = author_last_name.lower()
            author_results.update(self._search_books_by_author(author_last_name))

        # intersection of all results
        list_of_sets = [category_results, title_results, author_results]
        non_empties = [x for x in list_of_sets if x]
        results = set.intersection(*non_empties) if non_empties else set()

        return [(self.books_by_code[code].title, code) for code in results]

    # Helper methods for search_books
    def _search_books_by_category(self, category):
        '''Returns the unique codes of books in the given category.'''
        return self.books_by_category.get(category, [])

    def _search_books_by_title(self, title):
        '''Returns the unique codes of books with the given title substring.'''
        codes = set()
        for key in self.books_by_title:
            if title in key.lower():
                codes.update(self.books_by_title[key])
        return codes

    def _search_books_by_author(self, author_last_name):
        '''Returns the unique codes of books with the given author's last name substring.'''
        codes = set()
        for key in self.books_by_author:
            if author_last_name in key.lower():
                codes.update(self.books_by_author[key])
        return codes

