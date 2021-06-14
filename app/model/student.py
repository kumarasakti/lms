from app.model.person import Person


class Student(Person):

    def __init__(self, name, gender, age, person_id, kelas, semester, lended_books):
        super().__init__(name, gender, age, person_id)
        self.__kelas = kelas
        self.__semester = semester
        self.__lended_books = lended_books

    def getKelas(self):
        return self.__kelas

    def getSemester(self):
        return self.__semester

    def setKelas(self, kelas):
        self.__kelas = kelas

    def setSemester(self, semester):
        self.__semester = semester

    def lendBook(self, book):
        return self.__lended_books.append(book)

    def returnBook(self, index):
        return self.__lended_books.pop(index)

    def getLendedBooks(self):
        return self.__lended_books
