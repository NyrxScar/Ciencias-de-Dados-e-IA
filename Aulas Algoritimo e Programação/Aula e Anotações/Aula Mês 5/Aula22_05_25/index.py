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





___________________________________________


lista_compras = []  # Aqui a gente cria a lista onde os itens vão ser guardados
rejeicoes_do_menu = 0  # Contador que vai marcar quantas vezes o usuário tentou algo inválido (tipo item repetido, vazio, ou recusou confirmar)

# Esse while True cria um laço infinito, que só vai parar quando o usuário escolher sair (opção 3)
while True:
    # Mostra o menu principal pro usuário com as 3 opções básicas
    print("\n MENU de Opções: 1 - Adicionar item; 2 - Exibir lista de itens; 3 - Sair")
    menu = input("Escolha uma opção: ")
    
    # Se o usuário escolher 1, ele vai adicionar um novo item à lista
    if menu == "1":
        # Primeiro, verifica se já tem 10 itens. Se sim, avisa que não dá pra adicionar mais
        if len(lista_compras) >= 10:
            print("\nLimite máximo de 10 itens atingido!")
        else:
            # Pede o nome do item ao usuário e remove espaços em branco nas pontas (tipo "   arroz   " vira "arroz")
            item = input("Nome do item: ").strip()
            
            if item == "":
                # Se o usuário não digitar nada (ou só espaços), avisa que não pode e aumenta o contador de rejeições
                print("Item vazio não é aceito!")
                rejeicoes_do_menu += 1
            else:
                # Verifica se o item já está na lista. Se sim, não deixa repetir e conta como rejeição
                if item in lista_compras:
                    print("Item já cadastrado. Evite duplicidades.")
                    rejeicoes_do_menu += 1
                else:
                    # Se passou nas validações, pergunta pro usuário se ele confirma a adição do item
                    confirmacao = input(f"Você confirma o cadastro de '{item}'? (sim/não): ").lower()
                    if confirmacao == "sim":
                        # Se o usuário confirmar, o item é adicionado na lista
                        lista_compras.append(item)
                        print("Item registrado com sucesso.")
                    else:
                        # Se ele desistir, o cadastro é cancelado e conta como rejeição também
                        print("Cadastro cancelado.")
                        rejeicoes_do_menu += 1
    
    else:
        # Se o usuário escolheu a opção 2, o programa exibe os itens da lista
        if menu == "2":
            if not lista_compras:
                # Se a lista estiver vazia, avisa pro usuário que não tem nada ainda
                print("\nLista vazia. Adicione itens primeiro.")
            else:
                # Se tiver itens, mostra todos eles em formato de lista
                print("\nLista atual de itens:")
                for item in lista_compras:
                    print(f"• {item}")
        else:
            # Se for a opção 3, o programa exibe um relatório final e sai do loop (termina)
            if menu == "3":
                print("\nRelatório Final:")
                print("Itens cadastrados:")
                for item in lista_compras:
                    print(f"• {item}")
                print(f"Total de itens adicionados: {len(lista_compras)}")
                print(f"Total de rejeições: {rejeicoes_do_menu}")
                print("Programa encerrado.")
                break  # Aqui é onde o loop infinito é quebrado, ou seja, o programa termina
            
            else:
                # Se o usuário digitar algo que não é 1, 2 ou 3, dá esse aviso
                print("Opção inválida. Escolha 1, 2 ou 3.")
