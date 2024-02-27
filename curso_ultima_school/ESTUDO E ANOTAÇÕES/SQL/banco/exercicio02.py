from prettytable import PrettyTable

class Organizador:
    def __init__(self, nome, email, cpf):
        self.nome = nome
        self.email = email
        self.cpf = cpf

class Evento:
    def __init__(self, titulo, data, local, organizador):
        self.titulo = titulo
        self.data = data
        self.local = local
        self.organizador = organizador

class GerenciadorEventos:
    def __init__(self):
        self.organizadores = []
        self.eventos = []

    def adicionar_organizador(self, nome, email, cpf):
        organizador = Organizador(nome, email, cpf)
        self.organizadores.append(organizador)
        return organizador

    def adicionar_evento(self, titulo, data, local, organizador):
        evento = Evento(titulo, data, local, organizador)
        self.eventos.append(evento)

    def listar_organizadores(self):
        table = PrettyTable(["Nome", "Email", "CPF"])
        for organizador in self.organizadores:
            table.add_row([organizador.nome, organizador.email, organizador.cpf])
        print(table)

    def listar_eventos(self):
        table = PrettyTable(["Título", "Data", "Local", "Organizador"])
        for evento in self.eventos:
            table.add_row([evento.titulo, evento.data, evento.local, evento.organizador.nome])
        print(table)

# Exemplo de uso
gerenciador = GerenciadorEventos()

# Adiciona alguns organizadores e eventos de exemplo
organizador1 = gerenciador.adicionar_organizador("João Silva", "joao@email.com", "123.456.789-01")
organizador2 = gerenciador.adicionar_organizador("Maria Oliveira", "maria@email.com", "987.654.321-00")

gerenciador.adicionar_evento("Conferência de Tecnologia", "2022-02-15", "Centro de Convenções", organizador1)
gerenciador.adicionar_evento("Festival de Arte", "2022-03-10", "Teatro Municipal", organizador2)

# Lista os organizadores e eventos
gerenciador.listar_organizadores()
gerenciador.listar_eventos()
