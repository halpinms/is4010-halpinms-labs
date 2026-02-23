# test_lab06.py
import pytest
from lab06 import Book, EBook


# Tests for the base Book class
def test_book_constructor():
    """Test that Book objects are created with correct attributes."""
    book = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    assert book.title == "The Hobbit"
    assert book.author == "J.R.R. Tolkien"
    assert book.year == 1937


def test_book_str_method():
    """Test that Book objects have meaningful string representations."""
    book = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    book_str = str(book)
    assert "The Hobbit" in book_str
    assert "J.R.R. Tolkien" in book_str
    assert "1937" in book_str


def test_book_get_age():
    """Test that Book.get_age() calculates age correctly."""
    book = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    # Assuming current year is 2025 as per lab instructions
    assert book.get_age() == 2025 - 1937


def test_book_get_age_recent():
    """Test age calculation for a more recent book."""
    book = Book("Clean Code", "Robert Martin", 2008)
    assert book.get_age() == 2025 - 2008


# Tests for the EBook child class
def test_ebook_constructor():
    """Test that EBook objects inherit Book attributes and add file_size."""
    ebook = EBook("Dune", "Frank Herbert", 1965, 5)
    assert ebook.title == "Dune"
    assert ebook.author == "Frank Herbert"
    assert ebook.year == 1965
    assert ebook.file_size == 5


def test_ebook_str_method():
    """Test that EBook string representation includes all Book info plus file size."""
    ebook = EBook("Dune", "Frank Herbert", 1965, 5)
    ebook_str = str(ebook)
    # Should contain all Book information
    assert "Dune" in ebook_str
    assert "Frank Herbert" in ebook_str
    assert "1965" in ebook_str
    # Should also contain file size information
    assert "5" in ebook_str
    assert "MB" in ebook_str


def test_ebook_inherits_get_age():
    """Test that EBook inherits the get_age() method from Book."""
    ebook = EBook("Dune", "Frank Herbert", 1965, 5)
    assert ebook.get_age() == 2025 - 1965


def test_ebook_with_different_file_size():
    """Test EBook with different file size values."""
    small_ebook = EBook("Short Story", "Author Name", 2020, 2)
    large_ebook = EBook("Technical Manual", "Expert Author", 2018, 15)

    assert small_ebook.file_size == 2
    assert large_ebook.file_size == 15
    assert "2" in str(small_ebook) and "MB" in str(small_ebook)
    assert "15" in str(large_ebook) and "MB" in str(large_ebook)
