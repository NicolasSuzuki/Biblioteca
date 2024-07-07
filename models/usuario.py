class Usuario:
    def __init__(self, user_id, nome, tipo):
        self.id = user_id
        self.nome = nome
        self.tipo = tipo
        self.emprestimos = []

    def emprestar_livro(self, livro_isbn):
        if livro_isbn not in self.emprestimos:
            self.emprestimos.append(livro_isbn)
    
    def devolver_livro(self, livro_isbn):
        if livro_isbn in self.emprestimos:
            self.emprestimos.remove(livro_isbn)

    def emprestimos_ativos(self):
        return self.emprestimos

    def __str__(self):
        return f"{self.tipo}: {self.nome} (ID: {self.id})"

class StudentUserType(Usuario):
    def __init__(self, user_id, nome):
        super().__init__(user_id, nome, "Estudante")

class TeacherUserType(Usuario):
    def __init__(self, user_id, nome):
        super().__init__(user_id, nome, "Professor")