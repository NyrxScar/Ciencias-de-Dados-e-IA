import random
import heapq


Gundam_lista_nomes = [
    "Wing Gundam (Bird Mode)", "Gundam Heavyarms", "Gundam Sandrock", "Maganac",
    "Leo", "Aries", "Tragos", "RX-78-2 Gundam", "RX-78-2 Gundam (MA Form)",
    "Guncannon", "Guntank", "GM RGM-79", "Gundam Aerial (Permet Score Six)",
    "Gundam Aerial (Bit on Form)", "Demi Trainer MSJ-121", "Zowort F/O-19",
    "Aile Strike Gundam", "Strike Gundam", "Moebius Zero", "Moebius",
    "Strike Dagger", "Aegis Gundam (MA Mode)", "Ginn", "Miguel’s Ginn",
]

ListaAtributos = [
 {'Atk': 13, 'Def': 6, 'Spd': 4, 'Lif': 40},
 {'Atk': 9, 'Def': 7, 'Spd': 4, 'Lif': 46},
 {'Atk': 7, 'Def': 4, 'Spd': 9, 'Lif': 33},
 {'Atk': 8, 'Def': 6, 'Spd': 0, 'Lif': 46},
 {'Atk': 14, 'Def': 4, 'Spd': 10, 'Lif': 50},
 {'Atk': 10, 'Def': 3, 'Spd': 4, 'Lif': 30},
 {'Atk': 10, 'Def': 7, 'Spd': 13, 'Lif': 41},
 {'Atk': 8, 'Def': 8, 'Spd': 1, 'Lif': 36},
 {'Atk': 8, 'Def': 5, 'Spd': 11, 'Lif': 43},
 {'Atk': 15, 'Def': 10, 'Spd': 2, 'Lif': 42},
 {'Atk': 9, 'Def': 9, 'Spd': 2, 'Lif': 50},
 {'Atk': 15, 'Def': 5, 'Spd': 9, 'Lif': 35},
 {'Atk': 5, 'Def': 8, 'Spd': 4, 'Lif': 35},
 {'Atk': 8, 'Def': 9, 'Spd': 11, 'Lif': 43},
 {'Atk': 11, 'Def': 5, 'Spd': 1, 'Lif': 41},
 {'Atk': 8, 'Def': 5, 'Spd': 4, 'Lif': 48},
 {'Atk': 8, 'Def': 9, 'Spd': 6, 'Lif': 49},
 {'Atk': 9, 'Def': 5, 'Spd': 12, 'Lif': 35},
 {'Atk': 13, 'Def': 7, 'Spd': 12, 'Lif': 35},
 {'Atk': 5, 'Def': 10, 'Spd': 3, 'Lif': 41},
 {'Atk': 9, 'Def': 3, 'Spd': 0, 'Lif': 30},
 {'Atk': 15, 'Def': 10, 'Spd': 11, 'Lif': 30},
 {'Atk': 8, 'Def': 4, 'Spd': 12, 'Lif': 44},
 {'Atk': 6, 'Def': 8, 'Spd': 4, 'Lif': 32}
]
# print(ListaAtributos)

# Faz a mesma coisa do for de baixo mais fácil
# Carta_final = dict(zip(Gundam_lista_nomes,[{"Atributos": list(ListaAtributos)[i]} for i in range(len(Gundam_lista_nomes))]))

# teste = ListaAtributos[1].values()
# print(teste)


class Carta:
    def __init__(self, name, atributos):
        self.Name = name
        self.Atk = atributos['Atk']
        self.Def = atributos['Def']
        self.Spd = atributos['Spd']
        self.Lif = atributos['Lif']
    

    def __str__(self):
        return f"{self.Name} | ATK: {self.Atk} | DEF: {self.Def} | SPD: {self.Spd} | HP: {self.Lif}"

# # Criando Pilhas
Pilha = []
Pilha2 = []

for carta_nome,atributos in zip(Gundam_lista_nomes,ListaAtributos):
    Pilha.append(Carta(carta_nome,atributos))

for carta_nome,atributos in zip(Gundam_lista_nomes,ListaAtributos):
    Pilha2.append(Carta(carta_nome + "Enemy",atributos))

random.shuffle(Pilha)
random.shuffle(Pilha2)
# # Criando Filas com 5 cartas
Fila = [Pilha.pop() for _ in range(5)]
Fila2 = [Pilha2.pop() for _ in range(5)]



def calcular_dano(atacante, defensor):
    """Dano = ATK - DEF do inimigo (mínimo 1)"""
    dano = atacante.Atk - defensor.Def
    return dano if dano > 0 else 1

def Batalha():
    placar_jogador = 0
    placar_inimigo = 0

    while (Fila or Pilha) and (Fila2 or Pilha2):
        if not Fila and Pilha:
         Fila.append(Pilha.pop())  # Recarrega com uma carta da pilha
        if not Fila2 and Pilha2:
         Fila2.append(Pilha2.pop())

        carta1 = Fila.pop(0)
        carta2 = Fila2.pop(0)

        print("\n=== Novo Duelo ===")
        print("Jogador:", carta1)
        print("Inimigo:", carta2)
        print("==================")

        # while carta1.life > 0 and carta2.life > 0:
        #     # Criar heap com ordem baseada no SPD (maior SPD primeiro)
        #     heap = []
        #     heapq.heappush(heap, (-carta1.Spd, carta1, carta2))  # jogador
        #     heapq.heappush(heap, (-carta2.Spd, carta2, carta1))  # inimigo

        #     while heap and carta1.life > 0 and carta2.life > 0:
        #         _, atacante, defensor = heapq.heappop(heap)
        #         dano = calcular_dano(atacante, defensor)
        #         defensor.life -= dano
        #         print(f"{atacante.Name} atacou causando {dano} de dano! (HP {defensor.Name}: {defensor.life})")
        #         if defensor.life <= 0:
        #             if atacante == carta1:
        #                 print("\n Jogador venceu este round!")
        #                 placar_jogador += 1
        #             else:
        #                 print("\n Inimigo venceu este round!")
        #                 placar_inimigo += 1
        #             break


        while carta1.Lif > 0 and carta2.Lif > 0:
            if carta1.Spd >= carta2.Spd:
                # Jogador ataca
                dano = calcular_dano(carta1, carta2)
                carta2.Lif -= dano
                print(f"{carta1.Name} atacou causando {dano} de dano! (HP inimigo: {carta2.Lif})")
                if carta2.Lif <= 0:
                    print("\n Jogador venceu este round!")
                    placar_jogador += 1
                    break

            # Inimigo ataca
            if carta2.Spd >= carta1.Spd:
                dano = calcular_dano(carta2, carta1)
                carta1.Lif -= dano
                print(f"{carta2.Name} atacou causando {dano} de dano! (HP jogador: {carta1.Lif})")
                if carta1.Lif <= 0:
                    print("\n Inimigo venceu este round!")
                    placar_inimigo += 1
                    break

        print("------------------")

      

    print("\n======= Resultado Final =======")
    print(f"Placar Jogador: {placar_jogador}")
    print(f"Placar Inimigo: {placar_inimigo}")
    if placar_jogador > placar_inimigo:
        print(" Jogador venceu a batalha!")
    elif placar_inimigo > placar_jogador:
        print(" Inimigo venceu a batalha!")
    else:
        print(" Empate geral!")
    print("===============================")


# # Iniciar a batalha
Batalha()
