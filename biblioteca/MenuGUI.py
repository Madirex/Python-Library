import kivy
import os

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleview import RecycleView

Config.set('graphics', 'width', 800)
Config.set('graphics', 'height', 600)

from .Book import Book
from .Library import Library
from .User import User

min_width = 800
min_height = 600
library = Library()
library.init_data("library")

##MAIN
class WindowManager(ScreenManager):
    pass

class MainWindow(Screen):
    def get_image(self):
        PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
        return PROJECT_DIR + '/layout/logo.png'
    pass

#MANAGERS
class WindowManageUsers(Screen):
    pass

class WindowManageBooks(Screen):
    pass

#USERS
class WindowAddUser(Screen):
    dni = ObjectProperty(None)
    username = ObjectProperty(None)
    email = ObjectProperty(None)
    phone = ObjectProperty(None)
    address = ObjectProperty(None)

    def submit(self):
        user = User(self.dni.text, self.username.text, self.email.text, self.phone.text, self.address.text)

        if library.register_member(user):
            self.valid()
            self.reset()
        else:
            self.invalid("Socio ya existente")

    def invalid(self, str):
            pop = Popup(title='Error',
                    content=Label(text=str),
                    size_hint=(None, None), size=(400, 400))
            pop.open()
        
    def valid(self):
        pop = Popup(title='Socio agregado',
                    content=Label(text='Socio con DNI ' + self.dni.text + ' agregado'),
                    size_hint=(None, None), size=(400, 400))
        pop.open()
    
    def reset(self):
        self.dni.text = ""
        self.username.text = ""
        self.email.text = ""
        self.phone.text = ""
        self.address.text = ""

class WindowRemoveUser(Screen):
    dni = ObjectProperty(None)

    def submit(self):
        
        if library.cancel_member(self.dni.text) == False:
            self.invalid()
        else:
            self.valid()
            self.reset()

    def invalid(self):
        if (self.dni.text == ""):
            pop = Popup(title='DNI no introducido',
                        content=Label(text='No has introducido ningún DNI'),
                        size_hint=(None, None), size=(400, 400))
        else:
            pop = Popup(title='Socio no encontrado',
                        content=Label(text='Socio con dni ' + self.dni.text + ' no encontrado'),
                        size_hint=(None, None), size=(400, 400))
        pop.open()

    def valid(self):
        pop = Popup(title='Socio eliminado',
                    content=Label(text='Socio con dni ' + self.dni.text + ' eliminado'),
                    size_hint=(None, None), size=(400, 400))
        pop.open()

    def reset(self):
        self.dni.text = ""

class WindowGetInfo(Screen):
    def load_users(self):
        content = library.consult_users()
        self.rv.data = [{'text': str(item), 'readonly': True} for item in content]

    def load_books(self):
        content = library.consult_books()
        self.rv.data = [{'text': str(item), 'readonly': True} for item in content]
        
    def load_loanbooks(self):
        content = library.consult_lend_books()
        self.rv.data = [{'text': str(item), 'readonly': True} for item in content]









class SelectableLabel(RecycleDataViewBehavior, Label):
    pass

class WindowUser(Screen):
    pass


#BOOKS
class WindowAddBook(Screen):
    isbn = ObjectProperty(None)
    title = ObjectProperty(None)
    author = ObjectProperty(None)
    gender = ObjectProperty(None)
    cover = ObjectProperty(None)
    synopsis = ObjectProperty(None)
    copies = ObjectProperty(None)

    def submit(self):
        book = Book(self.isbn.text, self.title.text, self.author.text, self.gender.text, self.cover.text, self.synopsis.text, self.copies.text)

        if library.register_book(book):
            self.valid()
            self.reset()
        else:
            self.invalid("Libro ya existente")

    def invalid(self, str):
            pop = Popup(title='Error',
                    content=Label(text=str),
                    size_hint=(None, None), size=(400, 400))
            pop.open()
        
    def valid(self):
        pop = Popup(title='Libro agregado',
                    content=Label(text='Libro con ISBN ' + self.isbn.text + ' agregado'),
                    size_hint=(None, None), size=(400, 400))
        pop.open()
    
    def reset(self):
        self.isbn.text = ""
        self.title.text = ""
        self.author.text = ""
        self.gender.text = ""
        self.cover.text = ""
        self.synopsis.text = ""
        self.copies.text = ""

class WindowRemoveBook(Screen):
    isbn = ObjectProperty(None)

    def submit(self):
        if library.cancel_book(self.isbn.text) == False:
            self.invalid()
        else:
            self.valid()
            self.reset()

    def invalid(self):
        if (self.isbn.text == ""):
            pop = Popup(title='ISBN no introducido',
                        content=Label(text='No has introducido ningún ISBN'),
                        size_hint=(None, None), size=(400, 400))
        else:
            pop = Popup(title='Libro no encontrado',
                    content=Label(text='Libro con ISBN ' + self.isbn.text + ' no encontrado'),
                    size_hint=(None, None), size=(400, 400))
        pop.open()
        

    def valid(self):
        pop = Popup(title='Libro eliminado',
                    content=Label(text='Libro con ISBN ' + self.isbn.text + ' eliminado'),
                    size_hint=(None, None), size=(400, 400))
        pop.open()
    
    def reset(self):
        self.isbn.text = ""

class WindowBook(Screen):
    pass

#LOANS
class WindowManageLoans(Screen):
    pass

class WindowLoanBook(Screen):
    dni = ObjectProperty(None)
    isbn = ObjectProperty(None)

    def submit(self):
        n = library.assign_book(self.dni.text, self.isbn.text)
        if n == -1:
            self.invalid("No se ha encontrado el usuario")
        if n == -2:
            self.invalid("No se ha encontrado el libro")
        if n == -3:
            self.invalid("El libro seleccionado ya está\n siendo prestado a otro usuario")
        if n == True:
            self.valid()
            self.reset()
        else:
            self.invalid("El libro no se ha prestado")

    def invalid(self, str):
            pop = Popup(title='Error',
                    content=Label(text=str),
                    size_hint=(None, None), size=(400, 400))
            pop.open()
        
    def valid(self):
        pop = Popup(title='Libro prestado al usuario',
                    content=Label(text='Libro con ISBN ' + self.isbn.text + '\n prestado al usuario con DNI ' + self.dni.text),
                    size_hint=(None, None), size=(400, 400))
        pop.open()
    
    def reset(self):
        self.isbn.text = ""
        self.dni.text = ""

class WindowReturnBook(Screen):
    dni = ObjectProperty(None)
    isbn = ObjectProperty(None)

    def submit(self):
        n = library.unassign_book(self.dni.text, self.isbn.text)
        if n == -1:
            self.invalid("No se ha encontrado el usuario")
        if n == -2:
            self.invalid("No se ha encontrado el libro")
        if n == -3:
            self.invalid("El usuario no coincide con el libro prestado")
        if n == True:
            self.valid()
            self.reset()
        else:
            self.invalid("El libro no se ha devuelto")

    def invalid(self, str):
            pop = Popup(title='Error',
                    content=Label(text=str),
                    size_hint=(None, None), size=(400, 400))
            pop.open()
        
    def valid(self):
        pop = Popup(title='Libro devuelto',
                    content=Label(text='Libro con ISBN ' + self.isbn.text + '\n ha sido devuelto por el usuario con DNI ' + self.dni.text),
                    size_hint=(None, None), size=(400, 400))
        pop.open()
    
    def reset(self):
        self.isbn.text = ""
        self.dni.text = ""


class MainApp(App):
    title = "Madirex Books"
    def build(self):
        PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
        kv = Builder.load_file(PROJECT_DIR + '/layout/layout.kv')

        from kivy.core.window import Window
        Window.minimum_width = min_width
        Window.minimum_height = min_height
        return kv

    def init():
        MainApp().run()