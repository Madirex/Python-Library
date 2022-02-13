import unittest
from biblioteca import User

class TestUser(unittest.TestCase):
    def test_add_book_on_loan(self):
        user1 = User("29944811F","Manolo","manolo_garcia@hotmail.com","675476346","Madrid, calle asturiana 47")
        user1.add_book_on_loan("testisbn")
        self.assertEqual("testisbn", user1.book_on_loan[len(user1.book_on_loan) - 1])
        
    def test_remove_book_on_loan(self):
        user1 = User("29944811F","Manolo","manolo_garcia@hotmail.com","675476346","Madrid, calle asturiana 47")
        user1.add_book_on_loan("testisbn")
        user1.remove_book_on_loan("testisbn")
        self.assertNotEqual("testisbn", user1.book_on_loan[len(user1.book_on_loan) - 1])

    def test_search_book_on_loan_position(self):
        user1 = User("29944811F","Manolo","manolo_garcia@hotmail.com","675476346","Madrid, calle asturiana 47")
        user1.add_book_on_loan("testisbn")
        user1.add_book_on_loan("testisbn2")
        user1.add_book_on_loan("testisbn3")
        self.assertEqual("testisbn3", user1.search_book_on_loan_position["testisbn3"])

if __name__ == '__main__':
    unittest.main()