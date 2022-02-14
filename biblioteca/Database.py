import sqlite3
import os
from .User import User
from .Book import Book

class Database:
    def init_db(self, name):
        PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
        self.__db_name = PROJECT_DIR + '/db/' + name + '.db'

        self.__con = sqlite3.connect(self.__db_name)
        self.__cur = self.__con.cursor()
        self.init_database()
    
    def init_database(self):
        self.__cur.execute("CREATE TABLE IF NOT EXISTS user (dni TEXT, name TEXT, email TEXT, phone TEXT, address TEXT)")
        self.__cur.execute("CREATE TABLE IF NOT EXISTS book (isbn TEXT, title TEXT, author TEXT, gender TEXT, cover TEXT, synopsis TEXT, copies TEXT, user_assigned TEXT, loan_date DATETIME)")

    def query(self, str):
        self.__cur.execute(str)
        self.__con.commit()

    def load_data_library_books(self):
        books = []
        for row in self.__cur.execute('SELECT * FROM book'):
            book = Book(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            if row[7].lower() != "none":
                book.user_assigned = row[7]
            if row[8].lower() != "none":
                book.loan_date = row[8]
            books.append(book)
        return books

    def load_data_library_users(self):
        users = []
        for row in self.__cur.execute('SELECT * FROM user'):
            user = User(row[0], row[1], row[2], row[3], row[4])
            users.append(user)
        for user in users:
            for b in self.__cur.execute("SELECT * FROM book WHERE user_assigned = '" + row[0] + "'"):
                user.add_book_on_loan(b[0])
        return users

    def update_user(self, user):
        q = "UPDATE user SET "
        q += "name = '" + str(user.name) + "', "
        q += "email = '" + str(user.email) + "', "
        q += "phone = '" + str(user.phone) + "', "
        q += "address = '" + str(user.address) + "' "
        q += "WHERE dni = '" + str(user.dni) + "' "
        self.query(q)

    def insert_user(self, user):
        q = "INSERT INTO user VALUES ("
        q += "'" + str(user.dni) + "', "
        q += "'" + str(user.name) + "', "
        q += "'" + str(user.email) + "', "
        q += "'" + str(user.phone) + "', "
        q += "'" + str(user.address) + "' "
        q += ")"
        self.query(q)

    def delete_user(self, dni):
        self.query("DELETE FROM user WHERE dni = '" + dni + "'")

    def update_book(self, book):
        q = "UPDATE book SET "
        q += "title = '" + str(book.title) + "', "
        q += "author = '" + str(book.author) + "', "
        q += "gender = '" + str(book.gender) + "', "
        q += "cover = '" + str(book.cover) + "', "
        q += "synopsis = '" + str(book.synopsis) + "', "
        q += "copies = '" + str(book.copies) + "', "
        q += "user_assigned = '" + str(book.user_assigned) + "', "
        q += "loan_date = '" + str(book.loan_date) + "' "
        q += "WHERE isbn = '" + str(book.isbn) + "'"
        self.query(q)

    def insert_book(self, book):
        q = "INSERT INTO book VALUES ("
        q += "'" + str(book.isbn) + "', "
        q += "'" + str(book.title) + "', "
        q += "'" + str(book.author) + "', "
        q += "'" + str(book.gender) + "', "
        q += "'" + str(book.cover) + "', "
        q += "'" + str(book.synopsis) + "', "
        q += "'" + str(book.copies) + "', "
        q += "'" + str(book.user_assigned) + "', "
        q += "'" + str(book.loan_date) + "'"
        q += ")"
        self.query(q)

    def delete_book(self, isbn):
        self.query("DELETE FROM book WHERE isbn = '" + isbn + "'")

    def __del__(self):
        self.__con.close()