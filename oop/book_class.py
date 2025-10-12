#!/usr/bin/env python3
"""
Book class demonstrating Python magic methods:
__init__, __del__, __str__, and __repr__
"""

class Book:
    """A class that represents a book."""

    def __init__(self, title: str, author: str, year: int):
        """
        Constructor method to initialize a Book instance.
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor method called when an instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Returns a user-friendly string representation of the Book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Returns an official string representation that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
