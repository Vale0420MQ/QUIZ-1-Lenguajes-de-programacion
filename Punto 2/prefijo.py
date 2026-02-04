class TrieNode:
    def __init__(self):
        self.nodos = {}     
        self.is_end = False


class AutocompleteTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        word = word.strip().lower()
        if not word:
            return

        node = self.root
        for ch in word:
            if ch not in node.nodos:
                node.nodos[ch] = TrieNode()
            node = node.nodos[ch]
        node.is_end = True

    def autocomplete(self, prefix: str):
        prefix = prefix.strip().lower()
        results = []

        node = self.root
        for ch in prefix:
            if ch not in node.nodos:
                return []
            node = node.nodos[ch]

        def dfs(current_node, path):
            if current_node.is_end:
                results.append(prefix + "".join(path))

            for ch, nxt in current_node.nodos.items():
                path.append(ch)
                dfs(nxt, path)
                path.pop()

        dfs(node, [])
        return results


def main():
    palabras = [
        "Camion", "Carro", "Casa", "Regalo", "Reciclar", "Relampago",
        "Perro", "Pan", "Pato", "Comida", "Corazon", "Coco"
    ]

    sistema = AutocompleteTrie()
    for palabra in palabras:
        sistema.insert(palabra)

    while True:
     
        print("\nSistema de autocompletar ")
        print("Escribe 'salir' para terminar")

        prefijo = input("Ingresa un prefijo: ").strip()

        if prefijo.lower() == "salir":
            print("Saliendo...")
            break

        resultados = sistema.autocomplete(prefijo)
        if resultados:
            print("Coincidencias:")
            for r in resultados:
                print(" -", r)
        else:
            print("No se encontraron coincidencias.")


if __name__ == "__main__":
    main()
