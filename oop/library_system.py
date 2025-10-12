#!/usr/bin/env python3
"""
A Python module demonstrating inheritance and composition
with a library system consisting of Book, EBook, PrintBook, and Library classes.
"""

class Book:
    """Base class representing a general book."""

    def __init__(self, title: str, author: str):
        """
        Initializes a Book instance.
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """Returns a string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""

    def __init__(self, title: str, author: str, file_size: int):
        """
        Initializes an EBook instance.
        Args:
            title (str): The title of the eBook.
            author (str): The author of the eBook.
            file_size (int): The file size of the eBook in KB.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Returns a string representation of the eBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a printed book."""

    def __init__(self, title: str, author: str, page_count: int):
        """
        Initializes a PrintBook instance.
        Args:
            title (str): The title of the printed book.
            author (str): The author of the printed book.
            page_count (int): The number of pages in the printed book.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Returns a string representation of the printed book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """A class representing a library using composition to manage books."""

    def __init__(self):
        """Initializes the Library with an empty list of books."""
        self.books = []

    def add_book(self, book: Book):
        """
        Adds a book to the library.
        Args:
            book (Book): An instance of Book, EBook, or PrintBook.
        """
        self.books.append(book)

    def list_books(self):
        """Prints details of all books in the library."""
        for book in self.books:
            print(book)
