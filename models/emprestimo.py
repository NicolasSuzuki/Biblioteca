from datetime import datetime

class Emprestimo:
    def __init__(self, usuario_id, livro_isbn):
        self.usuario_id = usuario_id
        self.livro_isbn = livro_isbn
        self.data_emprestimo = datetime.now()
        self.data_devolucao = None  # Inicialmente não definida

    def to_dict(self):
        return {
            'usuario_id': self.usuario_id,
            'livro_isbn': self.livro_isbn,
            'data_emprestimo': self.data_emprestimo.isoformat(),
            'data_devolucao': self.data_devolucao.isoformat() if self.data_devolucao else None
        }