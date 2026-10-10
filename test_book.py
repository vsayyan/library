import pytest
from book import Book

def test_book_initial_state():
    book = Book("Clean Code","Robert Martin")
    assert book.title == "Clean Code"
    assert book.author == "Robert Martin"
    assert book.is_available is True

def test_borrow_book():
    book = Book("Clean Code","Robert Martin")
    book.borrow()
    assert book.is_available is False

def test_borrow_already_borrowed_book():
    book = Book("Clean Code","Robert Martin")
    book.borrow()

    with pytest.raises(ValueError):
        book.borrow()

def test_give_back_book():
    book = Book("Clean Code","Robert Martin")
    book.borrow()
    book.give_back()

    assert book.is_available is True

def test_give_back_not_borrowed_book():
    book = Book("Clean Code","Robert Martin")

    with pytest.raises(ValueError):
        book.give_back()

def test_book_string():
    book = Book("Clean Code","Robert Martin")

    assert str(book) == "Clean Code by Robert Martin"
    