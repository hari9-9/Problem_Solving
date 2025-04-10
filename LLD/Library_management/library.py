from abc import ABC
from enum import Enum
from datetime import datetime, timedelta

class BookStatus(Enum):
    AVAILABLE = 1
    BORROWED = 2

class Account(ABC):
    def __init__(self, id, password , username):
        self.__id = id
        self.__password = password
        self.__username = username

    def reset_password(self):
        None

class User(Account):
    def __init__(self , username , id ,password):
        super().__init__(id=id , password=password , username=username)
        self.borrowed_books = {} # key: book_id, value: due_date
        
    def can_borrow(self):
        return len(self.borrowed_books) < 5
    def borrow_book(self , book, expiry_date):
        self.borrowed_books[book.book_id] = expiry_date
    
    def has_borrowed(self , book):
        return book.book_id in self.borrowed_books
    
    def return_book(self , book):
        if book.book_id in self.borrowed_books:
            del self.borrowed_books[book.book_id]
        else:
            raise Exception("Book not borrowed by user")
class Book:
    def __init__(self , title , author , book_id , ISBN):
        self.title = title
        self.isbn = ISBN
        self.author = author
        self.book_id = book_id
        self.staus = BookStatus.AVAILABLE
        self.borrower_id = None
    
    def borrow(self , user_id):
        self.status = BookStatus.BORROWED
        self.borrower_id = user_id
    
    def return_book(self):
        self.status = BookStatus.AVAILABLE
        self.borrower_id = None
    
    def is_available(self):
        return self.status == BookStatus.AVAILABLE
    

class Librarian(Account):
    def __init__(self , username , id , password):
        super().__init__(id=id , password=password , username=username)
    
    def add_book(self , book):
        None
    def remove_book(self , book):
        None
    def search_book(self , book):
        None


class LibaryManager():
    def __init__(self):
        self._books = {} #book_id: Book
        self._users = {} #user_id: User
    
    def borrow_book(self , user_id , book_id):
        if user_id not in self._users:
            raise Exception("User not found")
        if book_id not in self._books:
            raise Exception("Book not found")
        user = self._users[user_id]
        book = self._books[book_id]
        if book.status == BookStatus.BORROWED:
            raise Exception("Book is already borrowed")
        if not user.can_borrow():
            raise Exception("User has already borrowed 5 books")
        book.borrow(user_id)
        user.borrow_book(book , datetime.now() + timedelta(days=7))
        

    
    def return_book(self , user_id , book_id):
        if user_id not in self._users:
            raise Exception("User not found")
        if book_id not in self._books:
            raise Exception("Book not found")
        user = self._users[user_id]
        book = self._books[book_id]
        if not user.has_borrowed(book):
            raise Exception("User has not borrowed this book")
        
        book.return_book()
        user.return_book(book)

