class Book:

    def __init__(self, isbn, title, author, gender, cover, synopsis, copies):
        self.__isbn = str(isbn)
        self.__title = str(title)
        self.__author = str(author)
        self.__gender = str(gender)
        self.__cover = str(cover)
        self.__synopsis = str(synopsis)
        self.__copies = str(copies)
        self.__user_assigned = None
        self.__loan_date = None

    @property
    def isbn(self):
        return self.__isbn

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def gender(self):
        return self.__gender

    @property
    def cover(self):
        return self.__cover

    @property
    def synopsis(self):
        return self.__synopsis

    @property
    def copies(self):
        return self.__copies

    @property
    def user_assigned(self):
        return self.__user_assigned

    @user_assigned.setter
    def user_assigned(self, u):
        self.__user_assigned = u

    @property
    def loan_date(self):
        return self.__loan_date

    @loan_date.setter
    def loan_date(self, d):
        self.__loan_date = d

    def __str__(self):
        book = "\n" + "📕 LIBRO:\n"
        book +="- ISBN: " + str(self.isbn)  + "\n"
        book +="- Título: " + str(self.title) + "\n"
        book +="- Autor: " + str(self.author) + "\n"
        book +="- Género: " + str(self.gender) + "\n"
        book +="- Portada: " + str(self.cover) + "\n"
        book +="- Sinópsis: " + str(self.synopsis) + "\n"
        book +="- Nº de copias: " + str(self.copies) + "\n"

        if self.user_assigned is None:
            book +="🔘 Este libro no está prestado"
        else:
            book +="🔴 Este libro se le ha prestado al siguiente usuario: " + str(self.__user_assigned)
        return book