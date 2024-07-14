import unittest
from unittest.mock import MagicMock
from services.emprestimo_service import EmprestimoService
from repositories.emprestimo_repository import EmprestimoRepository
from repositories.usuario_repository import UsuarioRepository
from repositories.livro_repository import LivroRepository
from services.usuario_service import UsuarioService
from services.notification_service import NotificationService
from datetime import datetime

class TestEmprestimoService(unittest.TestCase):

    def setUp(self):
        self.emprestimo_service = EmprestimoService()
        
        # Mock the repositories and services
        self.emprestimo_service.emprestimo_repo = MagicMock(EmprestimoRepository)
        self.emprestimo_service.usuario_repo = MagicMock(UsuarioRepository)
        self.emprestimo_service.livro_repo = MagicMock(LivroRepository)
        self.emprestimo_service.usuario_service = MagicMock(UsuarioService)
        self.emprestimo_service.notification_service = MagicMock(NotificationService)

    # def test_emprestar_livro_success(self):
    #     usuario = {'id': 1, 'nome': 'User Name', 'tipo': 'Estudante', 'emprestimos': []}
    #     livro = {'isbn': '0262033844', 'titulo': 'Introduction to Algorithms', 'autor': 'Cormen et al.', 'categoria': 'Algoritmos', 'disponivel': True}

    #     # Mock the return values
    #     self.emprestimo_service.usuario_service.consultar_usuario.return_value = usuario
    #     self.emprestimo_service.livro_repo.buscar.return_value = [livro]
    #     self.emprestimo_service.usuario_repo.emprestar_livro.return_value = None
    #     self.emprestimo_service.livro_repo.emprestar.return_value = None
    #     self.emprestimo_service.emprestimo_repo.adicionar.return_value = None

    #     # Call the method
    #     self.emprestimo_service.emprestar_livro(usuario['id'], livro['isbn'])

    #     # Check the calls
    #     self.emprestimo_service.usuario_service.consultar_usuario.assert_called_with(usuario['id'])
    #     self.emprestimo_service.livro_repo.buscar.assert_called_with(isbn=livro['isbn'])
    #     self.emprestimo_service.usuario_repo.emprestar_livro.assert_called_with(usuario['id'], livro['isbn'])
    #     self.emprestimo_service.livro_repo.emprestar.assert_called_with(livro['isbn'])
    #     self.emprestimo_service.emprestimo_repo.adicionar.assert_called()
    #     self.assertIn(livro['isbn'], usuario['emprestimos'])

    def test_devolver_livro_success(self):
        usuario_id = 1
        livro_isbn = '1111111111111'

        # Call the method
        self.emprestimo_service.devolver_livro(usuario_id, livro_isbn)

        # Check the calls
        self.emprestimo_service.usuario_repo.devolver_livro.assert_called_with(usuario_id, livro_isbn)
        self.emprestimo_service.livro_repo.devolver.assert_called_with(livro_isbn)
        self.emprestimo_service.emprestimo_repo.remover.assert_called_with(usuario_id, livro_isbn)
        self.emprestimo_service.notification_service.notificar_disponibilidade.assert_called()

if __name__ == '__main__':
    unittest.main()