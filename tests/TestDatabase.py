import unittest
from biblioteca import Database
from biblioteca import Book
from biblioteca import User
import sqlite3
import os

class TestDatabase(unittest.TestCase):
    def __init__(self):
        PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
        self.__db_name = PROJECT_DIR + '/db/librarytest.db'
        self.__con = sqlite3.connect(self.__db_name)
        self.__cur = self.__con.cursor()
        self.__cur.execute("DROP TABLE IF EXISTS user")
        self.__cur.execute("DROP TABLE IF EXISTS book")
        self.__cur.execute("CREATE TABLE IF NOT EXISTS user (dni TEXT, name TEXT, email TEXT, phone TEXT, address TEXT)")
        self.__cur.execute("CREATE TABLE IF NOT EXISTS book (isbn TEXT, title TEXT, author TEXT, gender TEXT, cover TEXT, synopsis TEXT, copies TEXT, user_assigned TEXT, loan_date DATETIME)")

    def test_init_database(self):
        pass

    def test_query(self):
        pass
    def test_load_data_library_books(self):
        books = []
        books.append()
        self.assertEqual(self.__cur.load_data_library_books())
        pass
    def test_load_data_library_users(self):
        pass
    def test_update_user(self):
        pass
    def test_insert_user(self):
        pass
    def delete_user(self):
        pass
    def update_book(self):
        pass
    def insert_book(self):
        book = Book("4rt3AA","Tai Lai","Claudia", "Terror","https://www.madirex.com/tai_lai.png","Lorem ipsu Tai lai", "23", None, None)
        self.__cur.insert_book()
        pass
    def delete_book(self):
        self.__cur
        pass

if __name__ == '__main__':
    unittest.main()