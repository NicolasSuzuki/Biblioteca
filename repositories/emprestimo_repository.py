import json
from datetime import datetime

class EmprestimoRepository:
    def __init__(self, file_path='data/emprestimos.json'):
        self.file_path = file_path

    def _load_data(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def _save_data(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def adicionar(self, emprestimo):
        emprestimos = self._load_data()
        emprestimos.append(emprestimo)
        self._save_data(emprestimos)

    def remover(self, usuario_id, livro_isbn):
        emprestimos = self._load_data()
        emprestimos = [emprestimo for emprestimo in emprestimos if not (emprestimo['usuario_id'] == usuario_id and emprestimo['livro_isbn'] == livro_isbn)]
        self._save_data(emprestimos)

    def buscar_por_usuario(self, usuario_id):
        emprestimos = self._load_data()
        return [emprestimo for emprestimo in emprestimos if emprestimo['usuario_id'] == usuario_id]

    def existe(self, usuario_id, livro_isbn):
        emprestimos = self._load_data()
        return any(emprestimo['usuario_id'] == usuario_id and emprestimo['livro_isbn'] == livro_isbn for emprestimo in emprestimos)