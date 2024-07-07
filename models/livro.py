class Livro:
    def __init__(self, isbn, titulo, autor, categoria, disponivel=True):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.disponivel = disponivel

    def __repr__(self):
        return f"{self.titulo} por {self.autor} - {self.categoria} (ISBN: {self.isbn})"
