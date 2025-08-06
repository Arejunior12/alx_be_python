# library_system.py

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"

class EBook(Book):
    def __init__(self, title, author, publication_year, file_size):
        super().__init__(title, author, publication_year)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {super().__str__()} - File Size: {self.file_size}MB"

class PrintBook(Book):
    def __init__(self, title, author, publication_year, weight):
        super().__init__(title, author, publication_year)
        self.weight = weight

    def __str__(self):
        return f"PrintBook: {super().__str__()} - Weight: {self.weight}kg"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("The library has no books.")
        else:
            for book in self.books:
                print(book)


# main.py
from library_system import EBook, PrintBook, Library

library = Library()

ebook = EBook("Python 101", "John Doe", 2020, 5)
printbook = PrintBook("Data Structures", "Jane Smith", 2018, 1.2)

library.add_book(ebook)
library.add_book(printbook)

library.display_books()
