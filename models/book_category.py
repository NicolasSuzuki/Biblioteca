class BookCategory:
    def __init__(self, nome, subcategorias=None):
        self.nome = nome
        self.subcategorias = subcategorias if subcategorias else []

    def adicionar_subcategoria(self, subcategoria):
        self.subcategorias.append(subcategoria)

    def __str__(self):
        return self.nome