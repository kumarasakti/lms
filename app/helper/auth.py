from flask import session
from app.helper.factory import generateDummyStudents


students = generateDummyStudents()


def verifyCredential(person_id):
    for student in students:
        if student.getPersonId() == person_id:
            return student
    return None


def getSession():
    if 'id' in session:
        return verifyCredential(session['id'])
    return None
