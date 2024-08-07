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

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"
    def __str__(self):
        return f"'{self.title}' by '{self.author}'"
    def borrow(self):
        if not self._is_borrowed:
            self.is_borrowed = True
            return True
        return False
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False


class Member:
    def __init__(self, name):
        self._name = name
        self._borrowed_books = []

    @property
    def name(self):
        return self._name
    @property
    def borrowed_books(self):
        return self._borrowed_books
    def __repr__(self):
        return f"Member('{self.name}')"

    def __str__(self):
        return self.name

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            return True
        return False


class Library:
    def __init__(self, name):
        self._name = name
        self._books = []
        self._members = []

    @property
    def name(self):
        return self._name

    @property
    def books(self):
        return self._books

    @property
    def members(self):
        return self._members

    def __repr__(self):
        return f"Library('{self.name}'"

    def __str__(self):
        return self.name

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        return None

    def borrow_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        if member and book:
            return member.borrow_book(book)
        return False

    def return_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        if member and book:
            return member.return_book(book)
        return False


# Create library
library = Library("Oxford Library")

# Create books
book1 = Book("Pure in Heart", "J. Kelly")
book2 = Book("Every Good Endeavour", "Tim Keller")
book3 = Book("Corona Virus and Christ", "John Piper")

# Add books to library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Create members
member1 = Member("Isaac")
member2 = Member("Abraham")

# Add members to Library
library.add_member(member1)
library.add_member(member2)

# Borrow books
library.borrow_book("Isaac", "Pure in Heart")
library.borrow_book("Abraham", "Every Good Endeavour")

# Print borrowed books
print(f"Isaac's borrowed books: {[str(book) for book in member1.borrowed_books]}")
print(f"Abraham's borrowed books: {[str(book) for book in member2.borrowed_books]}")

# Return books
library.return_book("Isaac", "Pure in Heart")
library.return_book("Abraham", "Every Good Endeavour")

# Print borrowed books after return
print(f"Isaac's borrowed books after return: {[str(book) for book in member1.borrowed_books]}")
print(f"Abraham's borrowed books after return: {[str(book) for book in member2.borrowed_books]}")
print(f"Abraham's borrowed books after return: {[str(book) for book in member2.borrowed_books]}")
print(f"Abraham's borrowed books after return: {[str(book) for book in member2.borrowed_books]}")
