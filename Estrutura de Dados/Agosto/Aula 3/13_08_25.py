# from dataclasses import dataclass
# from datetime import datetime, timedelta
# import queue
# from dataclasses import dataclass, field



# # Hora_atendimento = datetime(None)
# @dataclass
# class Cliente:
#     protocolo:int
#     nome_cliente: list = field(default_factory=list)

#     def Queue(self):
#         self.queue = []
#     def adicionar_item(self, item):
#         self.queue.append(item)
#     # def enqueue(self, element):
#     #     self.queue.append(element)

#     # Hora_de_Chegada: datetime.now
#     # Hora_saida: datetime.now

#     # def tempo(self):
#     #     if self.Hora_saida - self.Hora_de_Chegada:
#     #         return Hora_atendimento
 
# Informacoes_cliente = [ 
#     Cliente("João Silva", 1),
#     Cliente("Maria Souza", 2),
#     Cliente("Carlos Oliveira", 3),
#     Cliente("Ana Santos", 4),
#     Cliente("Pedro Costa", 5),
#     Cliente("Luiza Pereira", 6),
#     Cliente("Fernando Alves", 7),
#     Cliente("Patrícia Lima", 8),
#     Cliente("Ricardo Rocha", 9),
#     Cliente("Amanda Nunes", 10),
#     Cliente("Bruno Carvalho", 11),
#     Cliente("Juliana Ferreira", 12),
#     Cliente("Marcos Dias", 13),
#     Cliente("Vanessa Martins", 14),
#     Cliente("Gustavo Henrique", 15),
#     Cliente("Daniela Campos", 16),
#     Cliente("Roberto Andrade", 17),
#     Cliente("Tatiane Ribeiro", 18),
#     Cliente("Felipe Monteiro", 19),
#     Cliente("Letícia Moreira", 20)
# ]

# Informacoes_cliente[0].adicionar_item("Notebook")
# Informacoes_cliente[1].adicionar_item("Tablet")
# Informacoes_cliente[2].adicionar_item("Smartphone")
# Informacoes_cliente[4].adicionar_item("Impressora")
# Informacoes_cliente[3].adicionar_item("Teclado")
# Informacoes_cliente[5].adicionar_item("Monitor")
# Informacoes_cliente[6].adicionar_item("Fone de ouvido")
# Informacoes_cliente[7].adicionar_item("Webcam")
# Informacoes_cliente[8].adicionar_item("HD Externo")
# Informacoes_cliente[9].adicionar_item("Pendrive")
# Informacoes_cliente[10].adicionar_item("Roteador")
# Informacoes_cliente[11].adicionar_item("Caixa de som")
# Informacoes_cliente[12].adicionar_item("Cabo HDMI")
# Informacoes_cliente[13].adicionar_item("Carregador portátil")
# Informacoes_cliente[14].adicionar_item("Suporte para notebook")
# Informacoes_cliente[15].adicionar_item("Mochila para laptop")
# Informacoes_cliente[16].adicionar_item("Adaptador USB-C")
# Informacoes_cliente[17].adicionar_item("Luminária de mesa LED")
# Informacoes_cliente[18].adicionar_item("Hub USB")
# Informacoes_cliente[19].adicionar_item("Cooler para notebook")



# # Exibindo informações
# for cliente in Informacoes_cliente:
#     print(f"Cliente: {cliente.name} | Protocolo: {cliente.protocolo} | Itens: {cliente.queue}")


# resolução chat:
from dataclasses import dataclass, field
from queue import Queue
from datetime import datetime, timedelta
import random
import string

@dataclass
class Cliente:
    nome_cliente: str
    protocolo: int
    itens: Queue = field(default_factory=Queue)
    hora_chegada: datetime = field(default_factory=datetime.now)
    hora_saida: datetime = None
    atendido: bool = False

    def adicionar_item(self, item):
        self.itens.put(item)

    def atender_cliente(self):
        """Remove itens da fila e marca hora de saída"""
        atendidos = []
        while not self.itens.empty():
            atendidos.append(self.itens.get())
        self.hora_saida = datetime.now()
        self.atendido = True
        return atendidos

    def tempo_atendimento(self):
        if self.hora_saida:
            return self.hora_saida - self.hora_chegada
        return None

    def listar_itens(self):
        return list(self.itens.queue)

# Função para gerar nomes aleatórios
def gerar_nome():
    primeiro = ''.join(random.choices(string.ascii_uppercase, k=1)) + ''.join(random.choices(string.ascii_lowercase, k=random.randint(3,7)))
    sobrenome = ''.join(random.choices(string.ascii_uppercase, k=1)) + ''.join(random.choices(string.ascii_lowercase, k=random.randint(3,7)))
    return f"{primeiro} {sobrenome}"

# Função para gerar itens aleatórios
def gerar_item():
    produtos = ["Notebook", "Tablet", "Smartphone", "Teclado", "Impressora", "Monitor",
                "Fone de ouvido", "Webcam", "HD Externo", "Pendrive", "Roteador",
                "Caixa de som", "Cabo HDMI", "Carregador portátil", "Suporte para notebook",
                "Mochila para laptop", "Adaptador USB-C", "Luminária de mesa LED",
                "Hub USB", "Cooler para notebook"]
    return random.choice(produtos)

# Gerar automaticamente N clientes
N = 20
clientes = []
for i in range(N):
    cliente = Cliente(nome_cliente=gerar_nome(), protocolo=i+1)
    # Adiciona 1 a 3 itens aleatórios
    for _ in range(random.randint(1,3)):
        cliente.adicionar_item(gerar_item())
    clientes.append(cliente)

# Criando fila de atendimento
fila_atendimento = Queue()
for cliente in clientes:
    fila_atendimento.put(cliente)

atendidos = []
nao_atendidos = list(clientes)

# Atender os primeiros M clientes (simulando atendimento parcial)
M = 10
for _ in range(M):
    cliente = fila_atendimento.get()
    itens_atendidos = cliente.atender_cliente()
    atendidos.append(cliente)
    nao_atendidos.remove(cliente)
    print(f"Cliente {cliente.nome_cliente} atendido | Itens: {itens_atendidos} | Tempo: {cliente.tempo_atendimento()}")

# Exibir clientes não atendidos
print("\nClientes não atendidos restantes:")
for cliente in nao_atendidos:
    print(f"{cliente.nome_cliente} | Itens na fila: {cliente.listar_itens()}")

