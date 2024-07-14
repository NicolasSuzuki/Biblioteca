from repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self):
        self.usuario_repo = UsuarioRepository()

    def consultar_usuario(self, usuario_id):
        return self.usuario_repo.buscar_por_id(usuario_id)

