from datetime import datetime

class Usuario:
    def __init__(self, user_id, nome, tipo, emprestimos):
        self.id = user_id
        self.nome = nome
        self.tipo = tipo
        self.emprestimos = emprestimos

    def emprestar_livro(self, livro_isbn):
        if livro_isbn not in self.emprestimos:
            self.emprestimos.append(livro_isbn)
    
    def devolver_livro(self, livro_isbn):
        if livro_isbn in self.emprestimos:
            self.emprestimos.remove(livro_isbn)

    def emprestimos_ativos(self):
        emprestimos_ativos = []
        for item in self.emprestimos:
            if item['data_devolucao'] == None:
                emprestimos_ativos.append(item)
        return emprestimos_ativos

    def __str__(self):
        return f"{self.tipo}: {self.nome} (ID: {self.id})"

class StudentUserType(Usuario):
    def __init__(self, user_id, nome):
        super().__init__(user_id, nome, "Estudante", [])

class TeacherUserType(Usuario):
    def __init__(self, user_id, nome):
        super().__init__(user_id, nome, "Professor", [])
        
class StaffUserType(Usuario):
    def __init__(self, user_id, nome):
        super().__init__(user_id, nome, "Funcionário", [])