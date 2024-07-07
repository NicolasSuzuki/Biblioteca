from repositories.emprestimo_repository import EmprestimoRepository
from repositories.usuario_repository import UsuarioRepository
from repositories.livro_repository import LivroRepository
from services.usuario_service import UsuarioService
from datetime import datetime

class EmprestimoService:
    def __init__(self):
        self.emprestimo_repo = EmprestimoRepository()
        self.usuario_repo = UsuarioRepository()
        self.livro_repo = LivroRepository()
        self.usuario_service = UsuarioService()

    def emprestar_livro(self, usuario_id, livro_isbn):
        usuario = self.usuario_service.consultar_usuario(usuario_id)
        if len(usuario.emprestimos_ativos()) >= 3:
            raise ValueError("Usuário já possui 3 livros emprestados")

        emprestimo = {
            'usuario_id': usuario.id,
            'livro_isbn': livro_isbn,
            'data_emprestimo': datetime.now().isoformat()
        }

        self.usuario_repo.emprestar_livro(usuario.id, livro_isbn)
        self.livro_repo.emprestar(livro_isbn)
        self.emprestimo_repo.adicionar(emprestimo)