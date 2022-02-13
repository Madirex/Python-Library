from .Book import Book
from .Library import Library
from .User import User

def __init__(self):
    pass

def menu_msg_confirm(confirm_msg):
    print(confirm_msg)
    print("(0) -> Cancelar")
    print("(1) -> Confirmar")
    confirm = input()
    if str(confirm) == str(1):
        return True
    else:
        return False

def menu():
    library = Library()

    exit_menu = False

    while(exit_menu == False):
        print("\nEscribe (0) para salir del programa")
        print("Escribe (1) para dar de alta a un socio")
        print("Escribe (2) para dar de baja a un socio")
        print("Escribe (3) para dar de alta un libro")
        print("Escribe (4) para dar de baja un libro")
        print("Escribe (5) para prestar un libro")
        print("Escribe (6) para devolver un libro")
        print("Escribe (7) para consultar los libros de la biblioteca")
        print("Escribe (8) para consultar los usuarios de la biblioteca")
        print("Escribe (9) para consultar los libros prestados de la biblioteca\n")

        exit_loop = False
        menu_opt = 0

        while(exit_loop == False):
            try:
                menu_opt = int(input())
                exit_loop = True
            except ValueError:
                print("⛔ Error al introducir el número de selección.")

        if menu_opt == 0: # Salir
            exit_menu = True
        if menu_opt == 1: # Dar de alta socio
            dni = input("Introduce el DNI:")
            name = input("Introduce el nombre:")
            email = input("Introduce el email:")
            phone = input("Introduce el teléfono:")
            address = input("Introduce la dirección:")
            user = User(dni, name, email, phone, address)

            if menu_msg_confirm("¿Deseas agregar a este usuario?"):
                if library.register_member(user):
                    print("\n✅ Socio dado de alta.\n")
                else:
                    print("⛔ Socio ya existente")
            else:
                print("💡 Socio no agregado.")

        if menu_opt == 2: # Dar de baja socio
            dni = input("Introduce el DNI del socio a dar de baja:")
            if menu_msg_confirm("☠ ¿Deseas dar de baja al socio con DNI " + str(dni) + "?\n"):
                if library.cancel_member(dni) == False:
                    print("\nSocio con dni",dni,"no encontrado.\n")
                else:
                    print("\n✅ Socio eliminado.\n")
            else:
                print("\n💡 Socio no eliminado.\n")
        if menu_opt == 3: # Dar de alta libro
            isbn = input("Introduce el ISBN:")
            title = input("Introduce el título:")
            author = input("Introduce el autor:")
            gender = input("Introduce el género:")
            cover = input("Introduce la portada:")
            synopsis = input("Introduce la sinopsis:")
            copies = input("Introduce el número de copias disponibles:")
            book = Book(isbn, title, author, gender, cover, synopsis, copies)
            if menu_msg_confirm("¿Deseas agregar este libro?:"):
                if library.register_book(book):
                    print("\n✅ Libro agregado.\n")
                else:
                    print("⛔ Libro ya existente")
            else:
                print("💡 Libro no agregado.")
        if menu_opt == 4: # Dar de baja libro
            ISBN = input("Introduce el ISBN del libro a eliminar:")
            if menu_msg_confirm("¿Deseas eliminar el libro con el siguiente ISBN?:\n" + ISBN):
                if library.cancel_book(ISBN) == False:
                    print("⛔ Libro con ISBN",ISBN,"no encontrado.")
                else:
                    print("✅ Libro eliminado.")
            else:
                print("💡 Libro no eliminado.")
        if menu_opt == 5: # Prestar libro
            dni = input("Introduce el DNI del socio:")
            ISBN = input("Introduce el ISBN del libro:")

            if menu_msg_confirm("¿Deseas prestar el libro con ISBN " + ISBN + " al usuario con DNI " + dni + "?"):
                pr = library.assign_book(dni, ISBN)
                if pr == -1:
                    print("⛔ No se ha encontrado el usuario")
                if pr == -2:
                    print("⛔ No se ha encontrado el libro")
                if pr == -3:
                    print("⛔ El libro seleccionado ya está siendo prestado a otro usuario.")
                if pr == True:
                    print("✅ Libro prestado al usuario.")
            else:
                print("💡 El libro no se ha prestado.")

        if menu_opt == 6: # Devolver libro
            dni = input("Introduce el DNI del socio:")
            ISBN = input("Introduce el ISBN del libro:")
            n = library.unassign_book(dni, ISBN)
            if n == -1:
                print("⛔ Miembro no encontrado.")
                pass
            if n == -2:
                print("⛔ Libro no encontrado.")
                pass
            if n == -3:
                print("⛔ El usuario no coincide con el libro prestado.")
                pass
            if n == 1:
                print("✅ Libro devuelto.")
        if menu_opt == 7: # Consultar libros
            for l in library.consult_books():
                print(l)
        if menu_opt == 8: # Consultar usuarios
            for u in library.consult_users():
                print(u)
        if menu_opt == 9: # Consultar libros prestados
            lend_books = []
            for l in library.consult_lend_books():
                lend_books.append(l)
            if len(lend_books) == 0:
                print("No hay libros prestados actualmente.")
            else:
                print("Listado de los libros prestados:")
                for b in lend_books:
                    print(b)