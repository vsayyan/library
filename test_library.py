from book import Book
from library import Library


def test_library_initial_state():
    library = Library()

    assert library.books == []


def test_add_book():
    library = Library()
    book = Book("Clean Code", "Robert Martin")

    library.add_book(book)

    assert book in library.books
    assert len(library.books) == 1


def test_find_by_author():
    library = Library()

    book1 = Book("Clean Code", "Robert Martin")
    book2 = Book("The Clean Coder", "Robert Martin")
    book3 = Book("Atomic Habits", "James Clear")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    result = library.find_by_author("Robert Martin")

    assert result == [book1, book2]


def test_find_by_author_no_results():
    library = Library()

    library.add_book(Book("Clean Code", "Robert Martin"))

    result = library.find_by_author("James Clear")

    assert result == []


def test_available_books():
    library = Library()

    book1 = Book("Clean Code", "Robert Martin")
    book2 = Book("Atomic Habits", "James Clear")

    library.add_book(book1)
    library.add_book(book2)

    book1.borrow()

    result = library.available_books()

    assert result == [book2]


def test_available_books_when_all_borrowed():
    library = Library()

    book1 = Book("Clean Code", "Robert Martin")
    book2 = Book("Atomic Habits", "James Clear")

    library.add_book(book1)
    library.add_book(book2)

    book1.borrow()
    book2.borrow()

    assert library.available_books() == []