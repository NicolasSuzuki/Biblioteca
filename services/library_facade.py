from services.livro_service import LivroService
from services.usuario_service import UsuarioService
from services.emprestimo_service import EmprestimoService
from services.notification_service import NotificationService
from external.catalog_api import buscar_livros_externos

class LibraryFacade:
    def __init__(self):
        self.livro_service = LivroService()
        self.usuario_service = UsuarioService()
        self.emprestimo_service = EmprestimoService()
        self.notification_service = NotificationService()

    def buscar_livro(self, titulo=None, autor=None, categoria=None, isbn=None):
        livros_internos = self.livro_service.buscar_livros(titulo, autor, categoria, isbn)
        livros_externos = buscar_livros_externos(titulo, autor, categoria)
        return livros_internos + livros_externos

    def emprestar_livro(self, usuario_id, livro_isbn):
        return self.emprestimo_service.emprestar_livro(usuario_id, livro_isbn)

    def devolver_livro(self, usuario_id, livro_isbn):
        return self.emprestimo_service.devolver_livro(usuario_id, livro_isbn)

    def consultar_usuario(self, usuario_id):
        return self.usuario_service.consultar_usuario(usuario_id)