import json
from models.usuario import Usuario

class UsuarioRepository:
    def __init__(self, data_file='data/usuarios.json'):
        self.data_file = data_file
        self.usuarios = self.carregar_usuarios()

    def carregar_usuarios(self):
        try:
            with open(self.data_file, 'r') as file:
                usuarios_json = json.load(file)
                usuarios = [Usuario(usuario['id'], usuario['nome'], usuario['tipo'], usuario['emprestimos']) for usuario in usuarios_json]
                return usuarios
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o arquivo JSON: {self.data_file}")
            return []

    def salvar_usuarios(self):
        usuarios_serializaveis = [{
            'id': usuario.id,
            'nome': usuario.nome,
            'tipo': usuario.tipo,
            'emprestimos': usuario.emprestimos
        } for usuario in self.usuarios]
        
        with open(self.data_file, 'w') as file:
            json.dump(usuarios_serializaveis, file, indent=4)

    def emprestar_livro(self, usuario_id, livro_isbn):
        usuario = self.buscar_por_id(usuario_id)
        if livro_isbn not in usuario.emprestimos:
            usuario.emprestimos.append(livro_isbn)
            self.salvar_usuarios()

    def devolver_livro(self, usuario_id, livro_isbn):
        usuario = self.buscar_por_id(usuario_id)
        if livro_isbn in usuario.emprestimos:
            filter(lambda x: x != livro_isbn, usuario.emprestimos)
            self.salvar_usuarios()

    def atualizar(self, usuario):
        for idx, u in enumerate(self.usuarios):
            if u.id == usuario.id:
                self.usuarios[idx] = usuario
                self.salvar_usuarios()
                return True
        return False

    def buscar_por_id(self, usuario_id):
        for usuario in self.usuarios:
            if usuario.id == usuario_id:
                return usuario
        return None