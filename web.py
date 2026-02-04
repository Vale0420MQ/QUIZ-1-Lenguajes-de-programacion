class navegadorweb:
    def __init__(self):
        self.current = None
        self.back_stack = []
        self.forward_stack = []

    def loadPage(self, url):
        if not url:
            print("La URL no puede estar vacia.")
            return

        if self.current is not None:
            self.back_stack.append(self.current)

        self.current = url
        self.forward_stack.clear()
        print(f"Pagina cargada: {self.current}")

    def goBack(self):
        if not self.back_stack:
            print("No hay paginas anteriores.")
            return

        self.forward_stack.append(self.current)
        self.current = self.back_stack.pop()
        print(f"Volviste a: {self.current}")

    def goForward(self):
        if not self.forward_stack:
            print("No hay paginas siguientes.")
            return

        self.back_stack.append(self.current)
        self.current = self.forward_stack.pop()
        print(f"Avanzaste a: {self.current}")

    def showState(self):
        print("\n--- ESTADO ACTUAL ---")
        print("Pagina actual :", self.current)
        print("Atras         :", self.back_stack)
        print("Adelante      :", self.forward_stack)
        print("--------------------\n")


def main():
    navegador = navegadorweb()

    while True:
        print("Menu de navegacion")
        print("1. Cargar pagina nueva")
        print("2. Ir atras")
        print("3. Ir adelante")
        print("4. Ver estado actual")
        print("5. Salir")

        option = input("Elige una opcion: ")

        if option == "1":
            url = input("Ingresa la URL: ")
            navegador.loadPage(url)

        elif option == "2":
            navegador.goBack()

        elif option == "3":
            navegador.goForward()

        elif option == "4":
            navegador.showState()

        elif option == "5":
            print("Saliendo del navegador...")
            break

        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    main()
