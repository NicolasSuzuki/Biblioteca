import json

class UsuarioRepository:
    def __init__(self, file_path='data/usuarios.json'):
        self.file_path = file_path

    def _load_data(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def _save_data(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def buscar_por_id(self, usuario_id):
        usuarios = self._load_data()
        for usuario in usuarios:
            if usuario['id'] == usuario_id:
                if 'emprestimos' not in usuario:
                    usuario['emprestimos'] = []
                return usuario
        return None

    def emprestar_livro(self, usuario_id, livro_isbn):
        usuarios = self._load_data()
        for usuario in usuarios:
            if usuario['id'] == usuario_id:
                usuario['emprestimos'].append(livro_isbn)
                break
        self._save_data(usuarios)

    def devolver_livro(self, usuario_id, livro_isbn):
        usuarios = self._load_data()
        for usuario in usuarios:
            if usuario['id'] == usuario_id:
                usuario['emprestimos'].remove(livro_isbn)
                break
        self._save_data(usuarios)

    def adicionar_usuario(self, novo_usuario):
        usuarios = self._load_data()
        usuarios.append(novo_usuario)
        self._save_data(usuarios)

    def remover_usuario(self, usuario_id):
        usuarios = self._load_data()
        usuarios = [usuario for usuario in usuarios if usuario['id'] != usuario_id]
        self._save_data(usuarios)

    def atualizar_usuario(self, usuario_atualizado):
        usuarios = self._load_data()
        for i, usuario in enumerate(usuarios):
            if usuario['id'] == usuario_atualizado['id']:
                usuarios[i] = usuario_atualizado
                break
        self._save_data(usuarios)
