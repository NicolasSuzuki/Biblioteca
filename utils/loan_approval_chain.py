class BookAvailabilityHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, livro, usuario=None):
        if not livro['disponivel']:
            print(f"O livro {livro['titulo']} não está disponível")
        elif self.next_handler:
            self.next_handler.handle(livro, usuario)


class UserEligibilityHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, livro, usuario):
        if 'emprestimos' not in usuario:
            usuario['emprestimos'] = []
        if len(usuario['emprestimos']) >= 3:
            raise ValueError("Usuário já possui 3 livros emprestados")
        if self.next_handler:
            self.next_handler.handle(livro, usuario)


class LoanLimitHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, livro, usuario):
        # Implementar lógica adicional se necessário
        if self.next_handler:
            self.next_handler.handle(livro, usuario)
