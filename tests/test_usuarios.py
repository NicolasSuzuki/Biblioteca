import unittest
from datetime import datetime
from models.usuario import Usuario, StudentUserType, TeacherUserType, StaffUserType

class TestUsuario(unittest.TestCase):

    def test_student_user_type(self):
        student = StudentUserType(1, "Student Name")
        self.assertEqual(student.tipo, "Estudante")

    def test_teacher_user_type(self):
        teacher = TeacherUserType(2, "Teacher Name")
        self.assertEqual(teacher.tipo, "Professor")

    def test_staff_user_type(self):
        staff = StaffUserType(3, "Staff Name")
        self.assertEqual(staff.tipo, "Funcionário")

    def test_emprestimos_ativos(self):
        usuario = Usuario(4, "Generic User", "Genérico", [])
        usuario.emprestimos = [
            {"livro_isbn": "111", "data_devolucao": None},
            {"livro_isbn": "222", "data_devolucao": datetime.now()},
        ]
        self.assertEqual(len(usuario.emprestimos_ativos()), 1)

if __name__ == "__main__":
    unittest.main()
