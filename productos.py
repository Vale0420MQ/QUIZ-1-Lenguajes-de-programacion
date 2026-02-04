class Recommendar:
    def __init__(self):
        # Usuario -> set de productos comprados
        self.user_to_products = {}
        # Producto -> set de usuarios que lo compraron
        self.product_to_users = {}

    def addPurchase(self, usuario: str, producto: str):
        usuario = usuario.strip().lower()
        producto = producto.strip().lower()

        if not usuario or not producto:
            return

        # Registrar en user_to_products
        if usuario not in self.user_to_products:
            self.user_to_products[usuario] = set()
        self.user_to_products[usuario].add(producto)

        # Registrar en product_to_users
        if producto not in self.product_to_users:
            self.product_to_users[producto] = set()
        self.product_to_users[producto].add(usuario)

    def getRecommendations(self, usuario: str):
        usuario = usuario.strip().lower()

        if usuario not in self.user_to_products:
            return []

        comprados = self.user_to_products[usuario]
        scores = {}  # producto -> contador

        # Para cada producto comprado por el usuario
        for producto in comprados:
            # Usuarios que también compraron ese producto
            otros_usuarios = self.product_to_users.get(producto, set())

            for otro in otros_usuarios:
                if otro == usuario:
                    continue

                # Productos comprados por esos otros usuarios
                for prod_otro in self.user_to_products.get(otro, set()):
                    if prod_otro in comprados:
                        continue
                    scores[prod_otro] = scores.get(prod_otro, 0) + 1

        # Ordenar por mas apariciones
        recomendaciones = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        # Devolver solo los nombres de producto
        return [prod for prod, _ in recomendaciones]


def main():
    sistema = Recommendar()

    # Datos precargados (ropa + comida)
    compras = [
        ("ana", "camiseta"), ("ana", "jeans"), ("ana", "medias"),
        ("luis", "pizza"), ("luis", "helado"), ("luis", "hamburguesa"),
        ("maria", "jeans"), ("maria", "vestido"), ("maria", "camiseta"),
        ("carlos", "pizza"), ("carlos", "pollo"), ("carlos", "tacos"),
        ("sara", "vestido"), ("sara", "camiseta"), ("sara", "medias"),
        ("andres", "helado"), ("andres", "tacos"), ("andres", "pizza"),
        
    ]

    for u, p in compras:
        sistema.addPurchase(u, p)

    print("Sistema de recomendacion de productos (ropa y comida)")
    print("Escribe 'salir' para terminar")
    print("Usuarios disponibles:", ", ".join(sorted(sistema.user_to_products.keys())))

    while True:
        usuario = input("\nIngresa un usuario para recomendar: ").strip()
        if usuario.lower() == "salir":
            print("Saliendo...")
            break

        recomendaciones = sistema.getRecommendations(usuario)

        if not recomendaciones:
            if usuario.strip().lower() not in sistema.user_to_products:
                print("Usuario no encontrado.")
            else:
                print("No hay recomendaciones para este usuario.")
        else:
            print("Recomendaciones:")
            for r in recomendaciones:
                print(" -", r)


if __name__ == "__main__":
    main()
