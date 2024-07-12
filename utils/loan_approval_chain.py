class BookAvailabilityHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, livro, usuario=None):
        if not livro['disponivel']:
            print(f"\nO livro {livro['titulo']} não está disponível")
            return False
        elif self.next_handler:
            self.next_handler.handle(livro, usuario)
        return True


class UserEligibilityHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, livro, usuario):
        if 'emprestimos' not in usuario:
            usuario['emprestimos'] = []
        if len(usuario['emprestimos']) >= 3:
            print("Usuário já possui 3 livros emprestados")
            return False
        elif self.next_handler:
            self.next_handler.handle(livro, usuario)
        return True


class LoanLimitHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, livro, usuario):
        # Implementar lógica adicional se necessário
        if self.next_handler:
            return self.next_handler.handle(livro, usuario)
        return True
