from prettytable import PrettyTable
from datetime import datetime

class GerenciadorTarefas:
    def __init__(self):
        self.categorias = set()
        self.tarefas = []

    def adicionar_tarefa(self, nome, data, categoria, concluida=False):
        self.categorias.add(categoria)
        tarefa = {"nome": nome, "data": data, "categoria": categoria, "concluida": concluida}
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        table = PrettyTable(["Nome", "Data", "Categoria", "Concluída"])
        for tarefa in self.tarefas:
            table.add_row([tarefa["nome"], tarefa["data"], tarefa["categoria"], "Sim" if tarefa["concluida"] else "Não"])
        print(table)

    def listar_categorias(self):
        print("Categorias disponíveis:")
        for categoria in self.categorias:
            print(f"- {categoria}")

# Exemplo de uso
gerenciador = GerenciadorTarefas()

# Adiciona algumas tarefas de exemplo
gerenciador.adicionar_tarefa("Estudar Python", datetime(2022, 2, 1), "Estudo")
gerenciador.adicionar_tarefa("Fazer compras", datetime(2022, 2, 5), "Compras")
gerenciador.adicionar_tarefa("Exercícios físicos", datetime(2022, 2, 10), "Saúde", concluida=True)

# Lista as tarefas e categorias
gerenciador.listar_tarefas()
gerenciador.listar_categorias()
