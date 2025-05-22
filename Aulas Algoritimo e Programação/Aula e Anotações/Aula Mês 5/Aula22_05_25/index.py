lista_de_compras = []
rejeicoes = 0
adicionar_itens = []

print("Atualmente sua lista de compras está vazia, Adicione até 10 itens na sua lista!")

while len(lista_de_compras) <= 10:
  for index, word in enumerate(lista_de_compras):
        print(f"Lista de Compras: [ {index+1} - {word} ]")
  adicionar_itens = input("Digite o item que você deseja adicionar a sua lista ou 'Sair' para finalizar o programa: \n   ")
  print(f"\n Rodando o programa novamente, você pode reservar mais {10 - len(lista_de_compras)} item(s)...\n")
  lista_de_compras.append(adicionar_itens)
  if adicionar_itens.lower() == "sair":
    print("Programa encerrado")
    break
  try:
      if adicionar_itens == "":
            print("Itens vazios não são aceitos!")
            rejeicoes += 1
            continue
      else:
        if len(lista_de_compras) == 10:
          print("\n Você já atingiu o número máximo de 10 itens estabelecidos\n")
          print(f"Itens da Lista de Compras: {lista_de_compras};\n")
  except ValueError:
     print("\nEntrada inválida.\n")
