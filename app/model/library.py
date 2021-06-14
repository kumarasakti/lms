class Library:

    def __init__(self, name, books, librarians):
        self.__name = name
        self.__books = books
        self.__librarians = librarians

    def getBooks(self):
        return self.__books

    def getBook(self, id):
        for book in self.__books:
            if book.getId() == id:
                return book
        return None

    def getLibrarians(self):
        return self.__librarians

    def addBook(self, book):
        self.__books.append(book)

    def removeBook(self, id):
        new_books = []
        for book in self.__books:
            if book.getId() == id:
                continue
            else:
                new_books.append(book)
        self.__books = new_books
        return self.__books
