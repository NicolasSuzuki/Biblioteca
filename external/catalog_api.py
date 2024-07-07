class ExternalCatalogSystem:
    def buscar(self, titulo=None, autor=None, categoria=None):
        # Simula a busca em um sistema externo
        livros = [
            {"titulo": "Livro A", "autor": "Autor A", "categoria": "Categoria A", "disponivel": True},
            {"titulo": "Livro B", "autor": "Autor B", "categoria": "Categoria B", "disponivel": False},
        ]
        resultados = [livro for livro in livros if
                      (titulo and titulo in livro['titulo']) or
                      (autor and autor in livro['autor']) or
                      (categoria and categoria in livro['categoria'])]
        return resultados

def buscar_livros_externos(titulo=None, autor=None, categoria=None):
    external_system = ExternalCatalogSystem()
    return external_system.buscar(titulo, autor, categoria)