class LoanLimitHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        if len(request['usuario'].emprestimos) < 5:
            if self.successor:
                return self.successor.handle(request)
            return True
        return False

class BookAvailabilityHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        if request['livro']['disponivel']:
            if self.successor:
                return self.successor.handle(request)
            return True
        return False

class UserEligibilityHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        if request['usuario'].tipo in ['Estudante', 'Professor']:
            if self.successor:
                return self.successor.handle(request)
            return True
        return False