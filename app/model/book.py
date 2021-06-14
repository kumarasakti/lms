class Book:

    def __init__(self, id, thumbnail, judul_buku, category, author, penerbit, tahun_terbit):
        self.__id = id
        self.__thumbnail = thumbnail
        self.__judul_buku = judul_buku
        self.__category = category
        self.__author = author
        self.__penerbit = penerbit
        self.__tahun_terbit = tahun_terbit

    def getId(self):
        return self.__id

    def getThumbnail(self):
        return self.__thumbnail

    def getJudulBuku(self):
        return self.__judul_buku

    def getCategory(self):
        return self.__category

    def getAuthor(self):
        return self.__author

    def getPenerbit(self):
        return self.__penerbit

    def getTahunTerbit(self):
        return self.__tahun_terbit

    def setId(self, id):
        self.__id = id

    def setThumbnail(self, thumbnail):
        self.__thumbnail = thumbnail

    def setJudulBuku(self, judul_buku):
        self.__judul_buku = judul_buku

    def setCategory(self, category):
        self.__category = category

    def setAuthor(self, author):
        self.__author = author

    def setPenerbit(self, penerbit):
        self.__penerbit = penerbit

    def setTahunTerbit(self, tahun_terbit):
        self.__tahun_terbit = tahun_terbit
