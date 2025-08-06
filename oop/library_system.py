class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'"{self.title}" by {self.author} ({self.year})'


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            return "No books in the library."
        return "\n".join(str(book) for book in self.books)

    def __str__(self):
        return f'Library: {self.name} with {len(self.books)} book(s)'


# Example usage
if __name__ == "__main__":
    library = Library("City Central Library")
    book1 = Book("1984", "George Orwell", 1949)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

    library.add_book(book1)
    library.add_book(book2)

    print(library)         # Summary of the library
    print(library.list_books())  # Detailed list of books
