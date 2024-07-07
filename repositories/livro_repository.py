import json

class LivroRepository:
    def __init__(self, data_file='data/livros.json'):
        self.data_file = data_file
        self.livros = self._carregar_livros()

    def _carregar_livros(self):
        with open(self.data_file, 'r') as file:
            return json.load(file)

    def buscar(self, titulo=None, autor=None, categoria=None, isbn=None):
        resultados = [livro for livro in self.livros if
                      (not titulo or titulo.lower() in livro['titulo'].lower()) and
                      (not autor or autor.lower() in livro['autor'].lower()) and
                      (not categoria or categoria.lower() in livro['categoria'].lower()) and
                      (not isbn or isbn == livro['isbn'])]
        return resultados

    def buscar_por_isbn(self, isbn):
        for livro in self.livros:
            if livro['isbn'] == isbn:
                return livro
        return None

    def atualizar(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.livros, file, indent=4)

    def salvar_livros(self):
        livros_serializaveis = [livro for livro in self.livros]
        with open(self.data_file, 'w') as file:
            json.dump(livros_serializaveis, file, indent=4)

    def emprestar(self, livro_isbn):
        livro = self.buscar_por_isbn(livro_isbn)
        livro['disponivel'] = False
        self.salvar_livros()

    def devolver(self, livro_isbn):
        livro = self.buscar_por_isbn(livro_isbn)
        livro['disponivel'] = True
        self.salvar_livros()

