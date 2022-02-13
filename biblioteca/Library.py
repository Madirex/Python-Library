from .User import User
from .Book import Book 
from datetime import datetime
from .Database import Database

class Library:
    def __init__(self):
        self.__users = []
        self.__books = []
        self.__db = Database()

        #Cargar datos de la BD
        self.load_database_data()

        #Cargar datos en caso de que no haya
        self.load_base_data()

    def load_database_data(self):
        self.__books = self.__db.load_data_library_books()
        self.__users = self.__db.load_data_library_users()

    def get_member_by_dni_position(self, dni):
        position = 0
        for u in self.__users:
            if u.dni == dni:
                return position
            position +=1
        return None

    def get_position_by_isbn_book(self, isbn):
        position = 0
        for b in self.__books:
            if b.isbn == isbn:
                return position
            position +=1
        return None

    def get_book_by_isbn(self, isbn):
        for b in self.__books:
            if b.isbn == isbn:
                return b
        return None

    def register_member(self, user) -> bool:
        if self.get_member_by_dni_position(user.dni) == None:
            self.__users.append(user)
            self.__db.insert_user(user)
            return True
        else:
            return False

    def cancel_member(self, dni) -> bool:
        position = self.get_member_by_dni_position(dni)
        if position != None:
            del self.__users[position]
            self.__db.delete_user(dni)
            return True
        else:
            return False

    def register_book(self, book):
        if self.get_position_by_isbn_book(book.isbn) == None:
            self.__books.append(book)
            self.__db.insert_book(book)
            return True
        else:
            return False
    
    def cancel_book(self, isbn) -> bool:
        position = self.get_position_by_isbn_book(isbn)
        if position != None:
            del self.__books[position]
            self.__db.delete_book(isbn)
            return True
        else:
            return False
    
    def assign_book(self, dni, isbn): # Prestar libro
        position_member = self.get_member_by_dni_position(dni)
        position_book = self.get_position_by_isbn_book(isbn)

         #Asignar datos al libro y al miembro
        if position_member == None:
            return -1
        if position_book == None:
            return -2
        if self.__books[position_book].user_assigned == None:
            self.__books[position_book].user_assigned = self.__users[position_member].dni
            self.__books[position_book].loan_date = datetime.now()
            self.__users[position_member].add_book_on_loan(self.__books[position_book].isbn)
            self.__db.update_book(self.__books[position_book])
            self.__db.update_user(self.__users[position_member])
            return True
        else:
            return -3
        
    
    def unassign_book(self, dni, isbn): # Devolver libro
        position_member = self.get_member_by_dni_position(dni)
        position_book = self.get_position_by_isbn_book(isbn)

        if position_member == None:
            return -1
        if position_book == None:
            return -2
        if self.__books[position_book].user_assigned != self.__users[position_member].dni:
            return -3
        else:
            #Desasignar datos al libro
            self.__books[position_book].user_assigned = None
            self.__books[position_book].loan_date = None

            #Desasignar libro al usuario
            self.__users[position_member].remove_book_on_loan(self.__books[position_book].isbn)
            
            self.__db.update_book(self.__books[position_book])
            self.__db.update_user(self.__users[position_member])
            return 1
        
    def consult_books(self):
        return self.__books
    
    def consult_users(self):
        return self.__users
    
    def consult_lend_books(self): # Consultar libros prestados
        lend_books = []
        for b in self.__books:
            if b.user_assigned != None:
                lend_books.append(b)
        return lend_books

    def load_base_data(self):
        if len(self.__books) == 0:
            #Se crean los libros iniciales y se almacenan en la biblioteca
            book1 = Book("979-8704785880","La mansión de las pesadillas","Madirex","Fantasía y misterio","https://images-na.ssl-images-amazon.com/images/I/310lgn6bgyS._SX331_BO1,204,203,200_.jpg","Unos agentes de investigación reciben la orden de ir a investigar el caso de desaparición de una familia en una mansión abandonada a lo lejos de la ciudad. En el proceso de exploración, los agentes se verán involucrados en diferentes situaciones paranormales.Los protagonistas se darán cuenta de que no están solos en la mansión, en ese momento las cosas se empezarán a complicar.¿Lograrán los agentes resolver el caso?",50)
            book2 = Book("979-8523992919","Abre la mente, piensa diferente","Madirex","Desarrollo personal","https://images-na.ssl-images-amazon.com/images/I/41Uv7nfP4zS._SX331_BO1,204,203,200_.jpg","Abre la mente, piensa diferente aborda temas que muy poca gente suele pararse a reflexionar. Temas tan delicados como las religiones, la política, las relaciones sociales o incluso la propia muerte. Muchas personas piensan que creen saber cómo funciona la vida, pero ¿esto realmente es así? Vivimos en un mundo extraordinario con cambios exponenciales e inciertos. El desarrollo tecnológico es cada vez mayor y no sabemos qué nos puede llegar a deparar el futuro. ¿Estás preparado para los cambios que vienen?",5)
            self.register_book(book1)
            self.register_book(book2)

        if len(self.__users) == 0:
            #Se crean los usuarios y se registran en la biblioteca
            user1 = User("29944811F","Manolo","manolo_garcia@hotmail.com","675476346","Madrid, calle asturiana 47")
            user2 = User("67308848S","Gabriela","gabriela_esmeralda@mail.com","653838832","Madrid, calle de la esperanza 42")
            self.register_member(user1)
            self.register_member(user2)