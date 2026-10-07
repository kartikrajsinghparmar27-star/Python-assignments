class Book:
    def __init__(self,title):
        self.title = title
        self.available = True

class patron:
    def __init__(self,name):
        self.name = name
        self.borrowed_books = []

class library:
    def __init__(self):
        self.books = []
        self.patrons = []
    def add_book(self,book):
        self.books.append(book)
        print("book added", book.title)
    def register_patron(self,patron):
        self.patron.append(patron)
        print("patron registered", patron.name)
    def borrow_book(self,patron,book):
        if book.available:
            book.available = False
            patron.borrowed_books.append(book)
            print(patron.name, "borrowed", book.title)
        else:
            print("book not available")
    def return_book(self,patron,book):
        if book.available:
            book.available = True
            patron.borrowed_books.remove(book)
        else:
            print("book was never borrowed")

library = library()

book1 = Book("python programming")
book2 = Book("database management")
patron1 = patron("kartik")
library.borrow_book(patron1,book1)
library.borrow_book(patron1,book2)







