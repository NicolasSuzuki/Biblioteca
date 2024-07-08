import sys
class CLI:
    def __init__(self, library_mediator):
        self.library_mediator = library_mediator

    def run(self):
        while True:
            self.exibir_menu()
            comando = input("Digite um comando: ").strip().lower()
            if comando == "1":
                self.buscar_livro()
            elif comando == "2":
                self.emprestar_livro()
            elif comando == "3":
                self.devolver_livro()
            elif comando == "4":
                self.consultar_usuario()
            elif comando == "5":
                self.exibir_ajuda()
            elif comando == "0":
                print("Saindo do sistema...")
                sys.exit()
            else:
                print("Comando não reconhecido.")

    def exibir_menu(self):
        print("\n--- Menu de Opções ---")
        print("1. Buscar Livro")
        print("2. Emprestar Livro")
        print("3. Devolver Livro")
        print("4. Consultar Usuário")
        print("5. Exibir Ajuda")
        print("0. Sair")
        print("---------------------")

    def buscar_livro(self):
        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        categoria = input("Categoria: ").strip()
        livros = self.library_mediator.executar_operacao("buscar_livro", titulo, autor, categoria)
        if livros:
            for livro in livros:
                print(f"{livro}")
        else:
            print("Nenhum livro encontrado.")

    def emprestar_livro(self):
        usuario_id = input("ID do usuário: ").strip()
        livro_isbn = input("ISBN do livro: ").strip()
        self.library_mediator.executar_operacao("emprestar_livro", usuario_id, livro_isbn)

    def devolver_livro(self):
        usuario_id = input("ID do usuário: ").strip()
        livro_isbn = input("ISBN do livro: ").strip()
        self.library_mediator.executar_operacao("devolver_livro", usuario_id, livro_isbn)

    def consultar_usuario(self):
       usuario_id = input("ID do usuário: ").strip()
       usuario = self.library_mediator.executar_operacao("consultar_usuario", usuario_id)
       print("\nLivros do " + usuario['nome'] + ":")
       if usuario and 'emprestimos' in usuario:
           for emprestimo in usuario['emprestimos']:
               livro = self.library_mediator.executar_operacao("buscar_livro", "", "", "", emprestimo)
               if livro:
                   print(" - Título: " + livro[0]['titulo'])
       else:
           print("Usuário não encontrado.")

    def exibir_ajuda(self):
        print("\n--- Ajuda ---")
        print("1. Buscar Livro: Permite buscar livros por título, autor ou categoria.")
        print("2. Emprestar Livro: Permite emprestar um livro a um usuário.")
        print("3. Devolver Livro: Permite devolver um livro previamente emprestado.")
        print("4. Consultar Usuário: Permite consultar o histórico de empréstimos de um usuário.")
        print("5. Exibir Ajuda: Exibe este menu de ajuda.")
        print("0. Sair: Encerra o sistema.")
        print("---------------------")
