def initialize():
    exit = False

    while(exit == False):
        print("⚙️  Selecciona el tipo de interfaz:")
        print("(0) -> Salir")
        print("(1) -> CLI")
        print("(2) -> GUI")
        n = 100
        try:
            n = int(input())
        except ValueError:
            print("⛔ No has introducido un número.")
        if n == 0:
            exit = True
        if n == 1:
            import biblioteca.MenuCLI as cli
            cli.menu()
            exit = True
        if n == 2:
            import biblioteca.MenuGUI as gui
            gui.MainApp.init()
            exit = True
        if exit == False:
            print("❓ Introduce 0, 1 o 2")