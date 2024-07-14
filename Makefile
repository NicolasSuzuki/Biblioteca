# Nome do programa
PROGRAM = main.py

# Alvo padrão
all: init run

# Inicializa os dados
init:
	@echo "Inicializando os dados..."
	python3 init_data.py

# Executa o programa principal
run: init
	@echo "Executando o programa..."
	python3 $(PROGRAM)

# Limpa os dados
clean:
	@echo "Limpando os dados..."
	rm -f data/usuarios.json data/livros.json data/emprestimos.json

test:
	@echo "Executando os testes..."
	python3 -m unittest discover -s tests

# Alvo de ajuda
help:
	@echo "Makefile para executar operações"
	@echo ""
	@echo "Alvos disponíveis:"
	@echo "  all   - Inicializa os dados e executa o programa"
	@echo "  init  - Inicializa os dados"
	@echo "  run   - Executa o programa principal"
	@echo "  clean - Limpa os dados"
	@echo "  help  - Mostra esta ajuda"
