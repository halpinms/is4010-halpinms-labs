class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'"{self.title}" by {self.author} ({self.year})'

    def get_age(self):
        current_year = 2025
        return current_year - self.year

class EBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str} ({self.file_size} MB)"

if __name__ == '__main__':
    # Test Book class
    book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)
    print(book)
    print(f"Age of book: {book.get_age()} years")

    print("-" * 20)

    # Test EBook class
    ebook = EBook("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979, 2)
    print(ebook)
    print(f"Age of ebook: {ebook.get_age()} years")

