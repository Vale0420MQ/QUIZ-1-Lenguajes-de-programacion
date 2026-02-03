class WebNavigator:
    def __init__(self):
        self.current = None
        self.back_stack = []
        self.forward_stack = []

    def loadPage(self, url):
        if not url:
            print("La URL no puede estar vacía.")
            return

        if self.current is not None:
            self.back_stack.append(self.current)

        self.current = url
        self.forward_stack.clear()
        print(f"Página cargada: {self.current}")

    def goBack(self):
        if not self.back_stack:
            print("No hay páginas anteriores.")
            return

        self.forward_stack.append(self.current)
        self.current = self.back_stack.pop()
        print(f"Volviste a: {self.current}")

    def goForward(self):
        if not self.forward_stack:
            print("No hay páginas siguientes.")
            return

        self.back_stack.append(self.current)
        self.current = self.forward_stack.pop()
        print(f"Avanzaste a: {self.current}")

    def showState(self):
        print("\n--- ESTADO ACTUAL ---")
        print("Página actual :", self.current)
        print("Atrás         :", self.back_stack)
        print("Adelante      :", self.forward_stack)
        print("--------------------\n")


def main():
    navigator = WebNavigator()

    while True:
        print("Menú de navegación")
        print("1. Cargar página")
        print("2. Ir atrás")
        print("3. Ir adelante")
        print("4. Ver estado")
        print("5. Salir")

        option = input("Elige una opción: ")

        if option == "1":
            url = input("Ingresa la URL: ")
            navigator.loadPage(url)

        elif option == "2":
            navigator.goBack()

        elif option == "3":
            navigator.goForward()

        elif option == "4":
            navigator.showState()

        elif option == "5":
            print("Saliendo del navegador...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
