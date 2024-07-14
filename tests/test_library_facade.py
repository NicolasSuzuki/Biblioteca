import unittest
from services.library_facade import LibraryFacade
from services.emprestimo_service import EmprestimoService
from services.livro_service import LivroService
from models.usuario import Usuario
from models.livro import Livro

class TestLibraryFacade(unittest.TestCase):

    def setUp(self):
        self.library_facade = LibraryFacade()

    def test_buscar_livro(self):
        livros = self.library_facade.buscar_livro("Book Title", "Author Name", "Category")
        self.assertIsInstance(livros, list)

    def test_emprestar_livro(self):
        usuario = Usuario(1, "User Name", "Estudante", [])
        livro = Livro("0262033844", "Introduction to Algorithms", "Cormen et al.", "Algoritmos", True)
        result = self.library_facade.emprestar_livro(usuario.id, livro.isbn)
        self.assertTrue(result)
        result = self.library_facade.devolver_livro(usuario.id, livro.isbn)


if __name__ == "__main__":
    unittest.main()
