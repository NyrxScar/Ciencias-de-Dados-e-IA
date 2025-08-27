import random

Gundam_lista = [
    "Wing Gundam (Bird Mode)", "Gundam Heavyarms", "Gundam Sandrock", "Maganac",
    "Leo", "Aries", "Tragos", "RX-78-2 Gundam", "RX-78-2 Gundam (MA Form)",
    "Guncannon", "Guntank", "GM RGM-79", "Gundam Aerial (Permet Score Six)",
    "Gundam Aerial (Bit on Form)", "Demi Trainer MSJ-121", "Zowort F/O-19",
    "Aile Strike Gundam", "Strike Gundam", "Moebius Zero", "Moebius",
    "Strike Dagger", "Aegis Gundam (MA Mode)", "Ginn", "Miguel’s Ginn",
]

class Carta:
    def __init__(self, name):
        self.Name = name
        self.Atk = random.randint(5, 15)
        self.Def = random.randint(3, 10)
        self.Spd = random.randint(0, 13)
        self.life = random.randint(30, 50)

    def __str__(self):
        return f"{self.Name} | ATK: {self.Atk} | DEF: {self.Def} | SPD: {self.Spd} | HP: {self.life}"

# Criando Pilhas
Pilha = [Carta(i) for i in Gundam_lista]
Pilha2 = [Carta(i + " Enemy") for i in Gundam_lista]
random.shuffle(Pilha)
random.shuffle(Pilha2)

# Criando Filas com 5 cartas
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


        while carta1.life > 0 and carta2.life > 0:
            if carta1.Spd >= carta2.Spd:
                # Jogador ataca
                dano = calcular_dano(carta1, carta2)
                carta2.life -= dano
                print(f"{carta1.Name} atacou causando {dano} de dano! (HP inimigo: {carta2.life})")
                if carta2.life <= 0:
                    print("\n🔥 Jogador venceu este round!")
                    placar_jogador += 1
                    break

            # Inimigo ataca
            if carta2.Spd >= carta1.Spd:
                dano = calcular_dano(carta2, carta1)
                carta1.life -= dano
                print(f"{carta2.Name} atacou causando {dano} de dano! (HP jogador: {carta1.life})")
                if carta1.life <= 0:
                    print("\n💀 Inimigo venceu este round!")
                    placar_inimigo += 1
                    break

        print("------------------")

      

    print("\n======= Resultado Final =======")
    print(f"Placar Jogador: {placar_jogador}")
    print(f"Placar Inimigo: {placar_inimigo}")
    if placar_jogador > placar_inimigo:
        print("✅ Jogador venceu a batalha!")
    elif placar_inimigo > placar_jogador:
        print("❌ Inimigo venceu a batalha!")
    else:
        print("🤝 Empate geral!")
    print("===============================")


# Iniciar a batalha
Batalha()
