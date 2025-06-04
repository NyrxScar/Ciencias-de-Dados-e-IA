# lista_de_compras = []
# rejeicoes = 0
# adicionar_itens = []

# print("Atualmente sua lista de compras está vazia, Adicione até 10 itens na sua lista!")

# while len(lista_de_compras) <= 10:
#   for index, word in enumerate(lista_de_compras):
#         print(f"Lista de Compras: [ {index+1} - {word} ]")
#   adicionar_itens = input("Digite o item que você deseja adicionar a sua lista ou 'Sair' para finalizar o programa: \n   ")
#   print(f"\n Rodando o programa novamente, você pode reservar mais {10 - len(lista_de_compras)} item(s)...\n")
#   lista_de_compras.append(adicionar_itens)
#   if adicionar_itens.lower() == "sair":
#     print("Programa encerrado")
#     break
#   try:
#       if adicionar_itens == "":
#             print("Itens vazios não são aceitos!")
#             rejeicoes += 1
#             continue
#       else:
#         if len(lista_de_compras) == 10:
#           print("\n Você já atingiu o número máximo de 10 itens estabelecidos\n")
#           print(f"Itens da Lista de Compras: {lista_de_compras};\n")
#   except ValueError:
#      print("\nEntrada inválida.\n")



# ---------------------------------

# Lista de Variáveis
lista_compras = []  # Variável lista compra para armazenar os itens das compras
rejeicoes = 0       # Variável contador de rejeições que seriam 'vazios, duplicados ou cancelados'

# Menu
while True:
    # Exibição do MENU
    print("\n==== MENU ====")
    print("1. Adicionar item")
    print("2. Exibir lista de itens")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    # Opção 1: Adicionar item
    if opcao == "1":
        if len(lista_compras) >= 10:
            print("\nLimite máximo de 10 itens atingido!")
        else:
            item = input("Nome do item: ").strip()
            
            if item == "":
                print("Item vazio não é aceito!")
                rejeicoes += 1
            else:
                if item in lista_compras:
                    print("Item já cadastrado. Evite duplicidades.")
                    rejeicoes += 1
                else:
                    confirmacao = input(f"Você confirma o cadastro de '{item}'? (sim/não): ").lower()
                    if confirmacao == "sim":
                        lista_compras.append(item)
                        print("Item registrado com sucesso.")
                    else:
                        print("Cadastro cancelado.")
                        rejeicoes += 1
    
    # Opção 2: lista de compras - exibir ela
    else:
        if opcao == "2":
            if not lista_compras:
                print("\nLista vazia. Adicione itens primeiro.")
            else:
                print("\nLista atual de itens:")
                for item in lista_compras:
                    print(f"• {item}")
        else:
            # Opção 3: Sair
            if opcao == "3":
                # SAÍDA - Relatório final
                print("\nRelatório Final:")
                print("Itens cadastrados:")
                for item in lista_compras:
                    print(f"• {item}")
                print(f"Total de itens adicionados: {len(lista_compras)}")
                print(f"Total de rejeições: {rejeicoes}")
                print("Programa encerrado.")
                break
            
            # Opção inválida
            else:
                print("Opção inválida. Escolha 1, 2 ou 3.")
