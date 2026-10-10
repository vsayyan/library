class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_author(self, author):
        return [
            book for book in self.books
            if book.author == author
        ]

    def available_books(self):
        return [
            book for book in self.books
            if book.is_available
        ]