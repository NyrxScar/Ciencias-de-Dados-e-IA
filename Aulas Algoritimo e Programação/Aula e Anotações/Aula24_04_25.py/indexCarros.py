#####################

# Fazendo sem o try e except

carrosDisponiveis = ["Gol", "Fusca", "Palio", "Uno", "Vectra"]

carrosReservados = []

while len(carrosReservados) < 5:
    for index, word in enumerate(carrosDisponiveis):
        print(f"Carros disponíveis: {index} - {word}")
    print("\n" )
    IndiceCarroReservar = input("Digite o número(indice) do carro que você deseja reservar ou 'sair' para encerrar o programa: ")
    if IndiceCarroReservar == "sair":
        print("Programa encerrado")
        break

    else:
            if IndiceCarroReservar.isdigit():
                reservarCarro = int(IndiceCarroReservar)
                if reservarCarro in range(len(carrosDisponiveis)) :
                    carro = carrosDisponiveis[reservarCarro]
                    carrosReservados.append(carro) 
                    carrosDisponiveis.remove(carro)
                    print(f"\nCarro reservado com sucesso: {carro}")
                    print(f"Carros disponíveis ainda: {carrosDisponiveis}\n")
                    print(f"Você reservou os seguintes carros: {carrosReservados}\n")
                else:
                    print("\nCarro não disponível\n")
                    print(f"Rodando o programa novamente, você pode reservar mais {5 - len(carrosReservados)} carro(s)...\n")
            else:
                print("\nEntrada inválida. Digite um número ou 'sair'.\n")

if len(carrosReservados) == 5:
    print("\nSem estoque, todos os carros foram reservados e obrigada pela preferência\n")

########################################################

# Com o try e except

carrosDisponiveis = ["Gol", "Fusca", "Palio", "Uno", "Vectra"]
carrosReservados = []

while len(carrosReservados) < 5:
    for index, word in enumerate(carrosDisponiveis):
        print(f"Carros disponíveis: {index} - {word}")
    print("\n")
    
    IndiceCarroReservar = input("Digite o número(indice) do carro que você deseja reservar ou 'sair' para encerrar o programa: ")
   
    if IndiceCarroReservar.lower() == "sair":
        print("Programa encerrado")
        break

    try:
        reservarCarro = int(IndiceCarroReservar)
        
        if reservarCarro in range(len(carrosDisponiveis)):
            carro = carrosDisponiveis[reservarCarro]
            carrosReservados.append(carro)
            carrosDisponiveis.remove(carro)
            print(f"\nCarro reservado com sucesso: {carro}")
            print(f"Carros disponíveis ainda: {carrosDisponiveis}\n")
            print(f"Você reservou os seguintes carros: {carrosReservados}\n")
        else:
            print("\nCarro não disponível\n")
            print(f"Rodando o programa novamente, você pode reservar mais {5 - len(carrosReservados)} carro(s)...\n")
    
    except ValueError:
        print("\nEntrada inválida. Digite um número válido ou 'sair'.\n")

if len(carrosReservados) == 5:
    print("\nSem estoque, todos os carros foram reservados e obrigada pela preferência!\n")


