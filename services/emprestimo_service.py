from utils.loan_approval_chain import BookAvailabilityHandler, UserEligibilityHandler, LoanLimitHandler
from repositories.emprestimo_repository import EmprestimoRepository
from repositories.usuario_repository import UsuarioRepository
from repositories.livro_repository import LivroRepository
from services.usuario_service import UsuarioService
from services.notification_service import NotificationService
from datetime import datetime

class EmprestimoService:
    def __init__(self):
        self.emprestimo_repo = EmprestimoRepository()
        self.usuario_repo = UsuarioRepository()
        self.livro_repo = LivroRepository()
        self.usuario_service = UsuarioService()
        self.notification_service = NotificationService()

    def emprestar_livro(self, usuario_id, livro_isbn):
        usuario = self.usuario_service.consultar_usuario(usuario_id)
        livro = self.livro_repo.buscar(isbn=livro_isbn)[0]

        # Configurar a cadeia de handlers
        handler_chain = BookAvailabilityHandler(
            UserEligibilityHandler(
                LoanLimitHandler()
            )
        )

        # Processar a cadeia de handlers
        if not handler_chain.handle(livro, usuario):
            return False

        emprestimo = {
            'usuario_id': usuario['id'],
            'livro_isbn': livro_isbn,
            'data_emprestimo': datetime.now().isoformat()
        }

        # Registrar o empréstimo
        self.usuario_repo.emprestar_livro(usuario['id'], livro_isbn)
        self.livro_repo.emprestar(livro_isbn)
        self.emprestimo_repo.adicionar(emprestimo)

        return True

    def devolver_livro(self, usuario_id, livro_isbn):
        self.usuario_repo.devolver_livro(usuario_id, livro_isbn)
        self.livro_repo.devolver(livro_isbn)
        self.emprestimo_repo.remover(usuario_id, livro_isbn)
        
        livro = self.livro_repo.buscar(isbn=livro_isbn)[0]
        self.notification_service.notificar_disponibilidade(livro['titulo'])
