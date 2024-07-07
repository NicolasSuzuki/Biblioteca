class LibraryMediator:
    def __init__(self, library_facade):
        self.library_facade = library_facade

    def executar_operacao(self, operacao, *args):
        if operacao == "buscar_livro":
            return self.library_facade.buscar_livro(*args)
        elif operacao == "emprestar_livro":
            return self.library_facade.emprestar_livro(*args)
        elif operacao == "devolver_livro":
            return self.library_facade.devolver_livro(*args)
        elif operacao == "consultar_usuario":
            return self.library_facade.consultar_usuario(*args)
        else:
            raise ValueError(f"Operação desconhecida: {operacao}")