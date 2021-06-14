from flask import Flask, session, redirect, url_for, escape, request, render_template
from app.helper.auth import verifyCredential, getSession
from app.helper.factory import generateLibraryData, generateDummyBooks
import json

app = Flask(__name__)
app.secret_key = "RrzOv3c2C0"

library = generateLibraryData()


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        student = verifyCredential(request.form['id'])
        if student:
            session['id'] = student.getPersonId()
            return redirect(url_for('book_list'))
        else:
            error = 'NIM Anda tidak valid!'
    elif getSession():
        return redirect(url_for('book_list'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('id', None)
    return redirect(url_for('login'))


@app.route('/book_list')
def book_list():
    student = getSession()
    if student:
        return render_template('list.html', student=student, books=library.getBooks())
    else:
        return redirect(url_for('logout'))


@app.route('/confirmation', methods=['GET', 'POST'])
def confirmation():
    student = getSession()
    if student:
        borrowed_book_ids = []
        if request.method == 'POST':
            if 'borrowed-books' in request.form:
                borrowed_book_ids = json.loads(request.form['borrowed-books'])
        return render_template('confirmation.html', library=library, student=student, borrowed_book_ids=borrowed_book_ids)
    else:
        return redirect(url_for('logout'))


@app.route('/confirm_success', methods=['GET', 'POST'])
def confirm_success():
    student = getSession()
    if student:
        return render_template('confirm-success.html', student=student)
    else:
        return redirect(url_for('logout'))


if __name__ == '__main__':
    app.run()
