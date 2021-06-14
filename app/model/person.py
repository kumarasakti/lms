class Person:

    def __init__(self, name, gender, age, person_id):
        self.__name = name
        self.__gender = gender
        self.__age = age
        self.__person_id = person_id

    def getName(self):
        return self.__name

    def getGender(self):
        return self.__gender

    def getAge(self):
        return self.__age

    def getPersonId(self):
        return self.__person_id

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

    def setGender(self, gender):
        self.__gender = gender

    def setPersonId(self, person_id):
        self.__person_id = person_id
