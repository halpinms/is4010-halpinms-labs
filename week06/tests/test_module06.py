# test_lab06.py
import pytest
from module06 import Book, EBook


# Tests for the base Book class
def test_book_constructor():
    book = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    assert book.title == "The Hobbit"
    assert book.author == "J.R.R. Tolkien"
    assert book.year == 1937


def test_book_str_method():
    book = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    assert "The Hobbit" in str(book)
    assert "J.R.R. Tolkien" in str(book)
    assert "1937" in str(book)


def test_book_get_age():
    # Assuming current year is 2025 as per lab instructions
    book = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    assert book.get_age() == 2025 - 1937


# Tests for the EBook child class
def test_ebook_constructor():
    ebook = EBook("Dune", "Frank Herbert", 1965, 5)  # 5 MB
    assert ebook.title == "Dune"
    assert ebook.author == "Frank Herbert"
    assert ebook.year == 1965
    assert ebook.file_size == 5


def test_ebook_str_method():
    ebook = EBook("Dune", "Frank Herbert", 1965, 5)
    ebook_str = str(ebook)
    assert "Dune" in ebook_str
    assert "Frank Herbert" in ebook_str
    assert "1965" in ebook_str
    assert "5" in ebook_str  # Check for file size
    assert "MB" in ebook_str


def test_ebook_inherits_get_age():
    ebook = EBook("Dune", "Frank Herbert", 1965, 5)
    # 2025 - 1965 = 60
    assert ebook.get_age() == 60
