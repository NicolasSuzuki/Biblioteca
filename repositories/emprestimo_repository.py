import json
from datetime import datetime
from models.emprestimo import Emprestimo

class EmprestimoRepository:
    def __init__(self, data_file='data/emprestimos.json'):
        self.data_file = data_file
        self.emprestimos = self.carregar_emprestimos()

    def carregar_emprestimos(self):
        try:
            with open(self.data_file, 'r') as file:
                emprestimos_json = json.load(file)
                # Convertendo as datas de string ISO 8601 de volta para datetime
                for emprestimo in emprestimos_json:
                    emprestimo['data_emprestimo'] = emprestimo['data_emprestimo']
                    emprestimo['data_devolucao'] = emprestimo['data_devolucao'] if emprestimo['data_devolucao'] else None
                return emprestimos_json
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o arquivo JSON: {self.data_file}")
            return []

    def salvar_emprestimos(self):
        emprestimos_serializaveis = [emprestimo for emprestimo in self.emprestimos]
        
        with open(self.data_file, 'w') as file:
            json.dump(emprestimos_serializaveis, file, indent=4)

    def adicionar(self, emprestimo):
        self.emprestimos.append(emprestimo)
        self.salvar_emprestimos()