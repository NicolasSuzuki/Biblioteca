import json
import os

def inicializar_dados():
    data_path = 'data'
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    usuarios = [
        {"id": "1", "nome": "Alice", "tipo": "Estudante", "emprestimos": []},
        {"id": "2", "nome": "Bob", "tipo": "Professor", "emprestimos": []},
        {"id": "3", "nome": "Charlie", "tipo": "Funcionario", "emprestimos": []},
        {"id": "4", "nome": "David", "tipo": "Estudante", "emprestimos": []},
        {"id": "5", "nome": "Eve", "tipo": "Professor", "emprestimos": []},
        {"id": "6", "nome": "Frank", "tipo": "Funcionario", "emprestimos": []}
    ]

    livros = [
        {"isbn": "0262033844", "titulo": "Introduction to Algorithms", "autor": "Cormen et al.", "categoria": "Algoritmos", "disponivel": True},
        {"isbn": "0132350882", "titulo": "Clean Code", "autor": "Robert C. Martin", "categoria": "Desenvolvimento", "disponivel": True},
        {"isbn": "0201633612", "titulo": "Design Patterns", "autor": "Gamma et al.", "categoria": "Desenvolvimento", "disponivel": True},
        {"isbn": "0135957052", "titulo": "The Pragmatic Programmer", "autor": "Hunt e Thomas", "categoria": "Desenvolvimento", "disponivel": True},
        {"isbn": "0134610997", "titulo": "Artificial Intelligence", "autor": "Russell e Norvig", "categoria": "IA", "disponivel": True},
        {"isbn": "113318779X", "titulo": "Theory of Computation", "autor": "Michael Sipser", "categoria": "Teoria da Computação", "disponivel": True},
        {"isbn": "0132126958", "titulo": "Computer Networks", "autor": "Tanenbaum e Wetherall", "categoria": "Redes", "disponivel": True},
        {"isbn": "1118063333", "titulo": "Operating System Concepts", "autor": "Silberschatz et al.", "categoria": "Sistemas Operacionais", "disponivel": True},
        {"isbn": "0131103628", "titulo": "The C Programming Language", "autor": "Kernighan e Ritchie", "categoria": "Programação", "disponivel": True},
        {"isbn": "0735611319", "titulo": "Code", "autor": "Charles Petzold", "categoria": "Hardware e Software", "disponivel": True}
    ]
    
    emprestimos = [
        
    ]

    with open(os.path.join(data_path, 'usuarios.json'), 'w') as f:
        json.dump(usuarios, f, indent=4)

    with open(os.path.join(data_path, 'livros.json'), 'w') as f:
        json.dump(livros, f, indent=4)
        
    with open(os.path.join(data_path, 'emprestimos.json'), 'w') as f:
        json.dump(emprestimos, f, indent=4)

if __name__ == "__main__":
    inicializar_dados()
