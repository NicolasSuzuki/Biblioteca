import json

class LivroRepository:
    def __init__(self, file_path='data/livros.json'):
        self.file_path = file_path

    def _load_data(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def _save_data(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def buscar(self, titulo=None, autor=None, categoria=None, isbn=None):
        livros = self._load_data()
        if titulo:
            livros = [livro for livro in livros if titulo.lower() in livro['titulo'].lower()]
        if autor:
            livros = [livro for livro in livros if autor.lower() in livro['autor'].lower()]
        if categoria:
            livros = [livro for livro in livros if categoria.lower() in livro['categoria'].lower()]
        if isbn:
            livros = [livro for livro in livros if livro['isbn'] == isbn]
        return livros

    def emprestar(self, isbn):
        livros = self._load_data()
        for livro in livros:
            if livro['isbn'] == isbn:
                livro['disponivel'] = False
                break
        self._save_data(livros)

    def devolver(self, isbn):
        livros = self._load_data()
        for livro in livros:
            if livro['isbn'] == isbn:
                livro['disponivel'] = True
                break
        self._save_data(livros)

    def adicionar_livro(self, novo_livro):
        livros = self._load_data()
        livros.append(novo_livro)
        self._save_data(livros)

    def remover_livro(self, isbn):
        livros = self._load_data()
        livros = [livro for livro in livros if livro['isbn'] != isbn]
        self._save_data(livros)

    def atualizar_livro(self, livro_atualizado):
        livros = self._load_data()
        for i, livro in enumerate(livros):
            if livro['isbn'] == livro_atualizado['isbn']:
                livros[i] = livro_atualizado
                break
        self._save_data(livros)
