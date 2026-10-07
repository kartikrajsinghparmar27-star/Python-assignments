# class Book:
#     def __init__(self, title):
#         self.title = title
#         self.available = True


# class Patron:
#     def __init__(self, name):
#         self.name = name
#         self.borrowed_books = []


# class Library:
#     def __init__(self):
#         self.books = []
#         self.patrons = []

#     def add_book(self, book):
#         self.books.append(book)
#         print("Book added:", book.title)

#     def register_patron(self, patron):
#         self.patrons.append(patron)
#         print("Patron registered:", patron.name)

#     def borrow_book(self, patron, book):
#         if book.available:
#             book.available = False
#             patron.borrowed_books.append(book)
#             print(patron.name, "borrowed", book.title)
#         else:
#             print("Book is not available.")

#     def return_book(self, patron, book):
#         if book in patron.borrowed_books:
#             book.available = True
#             patron.borrowed_books.remove(book)
#             print(patron.name, "returned", book.title)
#         else:
#             print("This book was not borrowed by this patron.")


# # Creating library
# library = Library()

# # Creating books
# book1 = Book("Python Programming")
# book2 = Book("Data Structures")

# # Creating patron
# patron1 = Patron("Kartik")

# # Adding books and registering patron
# library.add_book(book1)
# library.add_book(book2)
# library.register_patron(patron1)

# # Borrowing and returning
# library.borrow_book(patron1, book1)
# library.return_book(patron1, book1)

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







