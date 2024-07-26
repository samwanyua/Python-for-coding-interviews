# Library system
"""
Project Overview
Library: Manages a collection of books and members.
Book: Represents a book with a title, author, and availability status.
Member: Represents a library member who can borrow and return books.
"""


class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author
        self._is_borrowed = False

    @property
    def title(self):
        return self._title
    @property
    def author(self):
        return self._author
    @property
    def is_borrowed(self):
        return self._is_borrowed

    @is_borrowed.setter
    def is_borrowed(self, value):
        if isinstance(value, bool):  # type checking - checks whether the `value` being passed to the setter is of
            # type `bool`
            self._is_borrowed = value
        else:
            raise ValueError("is_borrowed must be a boolean")