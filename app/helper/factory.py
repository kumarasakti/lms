from app.model.student import Student
from app.model.library import Library
from app.model.book import Book
from app.model.person import Person


def generateDummyStudents():
    return [
        Student('Jamal Cleveland', 'Pria', 15, '1148', 'Kelas A', 'Semester 1', []),
        Student('Ferdinand Smith', 'Wanita', 21, '2218', 'Kelas G', 'Semester 5', []),
        Student('Rogan Finley', 'Pria', 21, '3650', 'Kelas F', 'Semester 11', []),
        Student('Nasim Navarro', 'Pria', 25, '8352', 'Kelas Z', 'Semester 3', []),
        Student('Garth Malone', 'Pria', 23, '3344', 'Kelas E', 'Semester 5', []),
        Student('Lee Watkins', 'Wanita', 19, '1361', 'Kelas J', 'Semester 3', []),
        Student('Callum Tillman', 'Pria', 26, '6601', 'Kelas I', 'Semester 13', []),
        Student('Perry Stephenson', 'Wanita', 24, '3344', 'Kelas K', 'Semester 7', []),
        Student('Lee Watkins', 'Wanita', 20, '3601', 'Kelas L', 'Semester 5', []),
        Student('Brady Wooten', 'Pria', 25, '6530', 'Kelas M', 'Semester 7', []),
        Student('Forrest Clemons', 'Wanita', 29, '0809', 'Kelas A', 'Semester 13', []),
        Student('Wing Young', 'Pria', 21, '8329', 'Kelas G', 'Semester 5', []),
        Student('Anthony Norton', 'Pria', 21, '1089', 'Kelas F', 'Semester 11', []),
        Student('Dennis Price', 'Wanita', 25, '4489', 'Kelas Z', 'Semester 3', []),
        Student('Flynn Mosley', 'Pria', 23, '6572', 'Kelas E', 'Semester 5', []),
        Student('Asher Curtis', 'Wanita', 19, '9593', 'Kelas J', 'Semester 3', []),
        Student('Robert Newton', 'Pria', 22, '1092', 'Kelas I', 'Semester 13', []),
        Student('Uriah Knowles', 'Wanita', 24, '9696', 'Kelas K', 'Semester 7', []),
        Student('Jelani Mendez', 'Wanita', 20, '3156', 'Kelas L', 'Semester 5', []),
        Student('E. Lazuardy', 'Pria', 25, '2445', 'Kelas M', 'Semester 7', []),

    ]


def generateLibraryData():
    books = generateDummyBooks()
    librarians = [
        Person('Inggrid Rorez', 'Wanita', 35, '11111'),
        Person('Bintang K', 'Pria', 20, '11112'),
    ]
    return Library('Perpustakaan A', books, librarians)


def generateDummyBooks():
    return [
        Book(0,
             'https://upload.wikimedia.org/wikipedia/id/thumb/8/8e/Laskar_pelangi_sampul.jpg/220px-Laskar_pelangi_sampul.jpg',
             'Laskar Rainbow', 'Slice of life', 'Author 1', 'Penerbit 1', 2021),
        Book(1,
             'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/0dd63854-89ec-458b-bdc6-2a9337cc77f0/d5ov2p8-a44d70de-9b06-4313-8109-26172387f95b.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzBkZDYzODU0LTg5ZWMtNDU4Yi1iZGM2LTJhOTMzN2NjNzdmMFwvZDVvdjJwOC1hNDRkNzBkZS05YjA2LTQzMTMtODEwOS0yNjE3MjM4N2Y5NWIucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.nu-wnjwxcvMGAbw6xsN-Vk1rScpYNuuYuIiFE9r6WSk',
             'Boruto Father Adventure', 'Fiksi', 'Author 2', 'Penerbit 2', 2021),
        Book(2,
             'https://1.bp.blogspot.com/-CYl8DeU8nsc/Xosgzgb529I/AAAAAAAAF3M/6YZeqHziSSYp3P42s-WK1T-UpXxSQXhHgCLcBGAsYHQ/s1600/Kny-vol-20-chapteria.jpg',
             'Demon Slayer', 'Petualangan', 'Author 3', 'Penerbit 3', 2021),
        Book(3,
             'https://upload.wikimedia.org/wikipedia/id/thumb/5/56/Harry_potter_deathly_hallows_US.jpg/220px-Harry_potter_deathly_hallows_US.jpg',
             'Harry Potter And The Deathly Hallows', 'Fiksi', 'Author 4', 'Penerbit 4', 2010),
        Book(4,
             'https://images-na.ssl-images-amazon.com/images/I/71xcuT33RpL._AC_SY679_.jpg',
             'Harry Potter And Order of The Phoenix', 'Fiksi', 'Author 4', 'Penerbit 4', 2009),
        Book(5,
             'https://universe.byu.edu/wp-content/uploads/2015/01/HP4cover.jpg',
             'Harry Potter And The Goblet of Fire', 'Fiksi', 'Author 4', 'Penerbit 4', 2006),
        Book(6,
             'https://i.guim.co.uk/img/static/sys-images/Guardian/Pix/pictures/2014/7/30/1406719264487/fd90e162-93de-41b1-aea5-f8e49227e85b-1360x2040.jpeg?width=700&quality=85&auto=format&fit=max&s=28732c5a7caa1d1249d3f420e247479b',
             'Harry Potter And The Camber of Secret', 'Fiksi', 'Author 4', 'Penerbit 4', 1999),
        Book(7,
             'https://www.bukukita.com/babacms/displaybuku/81937_f.jpg',
             'Budidaya Lele Di Lahan Sempit', 'Panduan', 'Author 5', 'Penerbit 5', 2999),

    ]
