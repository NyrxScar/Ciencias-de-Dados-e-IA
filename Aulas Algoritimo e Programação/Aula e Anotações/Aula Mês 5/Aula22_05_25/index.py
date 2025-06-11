# dica:  for i,fruta in enumerate (frutas, start=1): #enumera cada item da lista 'frutas', começando por 1
#             print(f"{i}. {fruta}")

lista_de_compras = []  # Aqui a gente cria a lista onde os itens vão ser guardados
rejeicoes_do_menu = 0  # Contador que vai marcar quantas vezes o usuário tentou algo inválido (tipo item repetido, vazio, ou recusou confirmar)

print("AV2 - Sistema de Cadastro de Itens para Lista de Compras com MENU")


# Esse while True cria um laço infinito, que só vai parar quando o usuário escolher sair (opção 3)
while True:
    # Mostra o menu principal pro usuário com as 3 opções básicas
    print("\n MENU de Opções: 1 - Adicionar item; 2 - Exibir lista de itens; 3 - Sair")

    menu_de_escolha = input("Escolha uma opção: ")
    
    # Se o usuário escolher 1, ele vai adicionar um novo item à lista
    if menu_de_escolha == "1":
        # Primeiro, verifica se já tem 10 itens. Se sim, avisa que não dá pra adicionar mais
        if len(lista_de_compras) >= 10:
            print("\nLimite máximo de 10 itens atingido!")
        else:
            # Pede o nome do item ao usuário e remove espaços em branco nas pontas (tipo "   arroz   " vira "arroz")
            item_da_lista = input("Nome do item: ").strip()
            
            if item_da_lista == "":
                # Se o usuário não digitar nada (ou só espaços), avisa que não pode e aumenta o contador de rejeições
                print("Item vazio não é aceito!")
                rejeicoes_do_menu += 1
            else:
                # Verifica se o item já está na lista. Se sim, não deixa repetir e conta como rejeição
                if item_da_lista in lista_de_compras:
                    print("Item já cadastrado. Evite duplicidades.")
                    rejeicoes_do_menu += 1
                else:
                    # Se passou nas validações, pergunta pro usuário se ele confirma a adição do item
                    confirmacao = input(f"Você confirma o cadastro de '{item_da_lista}'? (sim/não): ").lower()
                    if confirmacao == "sim":
                        # Se o usuário confirmar, o item é adicionado na lista
                        lista_de_compras.append(item_da_lista)
                        print("Item registrado com sucesso.")
                    else:
                        # Se ele desistir, o cadastro é cancelado e conta como rejeição também
                        print("Cadastro cancelado.")
                        rejeicoes_do_menu += 1
    
    else:
        # Se o usuário escolheu a opção 2, o programa exibe os itens da lista
        if menu_de_escolha == "2":
            if not lista_de_compras:
                # Se a lista estiver vazia, avisa pro usuário que não tem nada ainda
                print("\nLista vazia. Adicione itens primeiro.")
            else:
                # Se tiver itens, mostra todos eles em formato de lista
                print("\nLista atual de itens:")
                for item_da_lista in lista_de_compras:
                    print(f"• {item_da_lista}")
        else:
            # Se for a opção 3, o programa exibe um relatório final e sai do loop (termina)
            if menu_de_escolha == "3":
                print("\nRelatório Final:")
                print("Itens cadastrados:")
                for item_da_lista in lista_de_compras:
                    print(f" • {item_da_lista};")
                print(f"Total de itens adicionados: {len(lista_de_compras)}")
                print(f"Total de rejeições: {rejeicoes_do_menu}")
                print("O Programa da 'AV2 - Sistema de Cadastro de Itens para Lista de Compras com MENU' foi finalizado.")
                break  # Aqui é onde o loop infinito é quebrado, ou seja, o programa termina
            
            else:
                # Se o usuário digitar algo que não é 1, 2 ou 3, dá esse aviso
                print("Opção inválida ou Erro. Escolha 1, 2 ou 3 das opções do Menu faladas anteriormente.")
