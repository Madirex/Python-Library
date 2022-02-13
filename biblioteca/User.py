class User:

    def __init__(self,dni,name,email,phone,address):
        self.__dni = str(dni)
        self.__name = str(name)
        self.__email = str(email)
        self.__phone = str(phone)
        self.__address = str(address)
        self.__books_on_loan = [] # Libros en préstamo

    @property
    def dni(self):
        return self.__dni

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def phone(self):
        return self.__phone

    @property
    def address(self):
        return self.__address

    @property
    def books_on_loan(self):
        return self.__books_on_loan

    def add_book_on_loan(self, isbn):
        self.__books_on_loan.append(isbn)
        
    def remove_book_on_loan(self, isbn):
        position = self.search_book_on_loan_position(isbn)
        del self.__books_on_loan[position]

    def search_book_on_loan_position(self, isbn):
        position = 0
        for b in self.__books_on_loan:
            if b == isbn:
                return position
            position +=1
        return None

    def __str__(self):
        user = "\n" + "👤 USUARIO:\n"
        user +="- DNI: " + str(self.dni)  + "\n"
        user +="- Nombre: " + str(self.name) + "\n"
        user +="- Email: " + str(self.email) + "\n"
        user +="- Teléfono: " + str(self.phone) + "\n"
        user +="- Dirección: " + str(self.address) + "\n"
        if len(self.books_on_loan) == 0:
            user += "🔘 Este usuario no tiene libros que devolver"
        else:
            user += "🔴 Estos libros han sido prestados a este usuario y quedan pendientes de devolución:\n"
            num = 1
            for b in self.books_on_loan:
                user +="\t📗 Libro " + str(num) + ": " + str(b)
                num +=1
        return user