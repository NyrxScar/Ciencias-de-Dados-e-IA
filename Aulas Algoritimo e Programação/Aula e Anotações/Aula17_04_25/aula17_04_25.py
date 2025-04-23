# lista = ['O carro', 'O peixe', 123, 111]
# nova_lista = ['pedra',lista]
# print(lista+nova_lista)

# # livros = ['Java', 'SqlServer', 'Delphi', 'Python']
# # livros.append("Android")
# # print(livros)
# # livros.insert('Oracle', 0)
# # print(livros)



# lista = []
# for x in range(5):
#     n = int(input("Digite um número inteiro: "))
#     lista.append(n)
#     lista.sort()
#     print(lista)

import pandas as pd
pd.read_excel("/content/controle_de_abacates.xlsx")



# lista = ['O carro', 'O peixe', 123, 111]
# nova_lista = ['pedra',lista]
# print(lista+nova_lista)

# # livros = ['Java', 'SqlServer', 'Delphi', 'Python']
# # livros.append("Android")
# # print(livros)
# # livros.insert('Oracle', 0)
# # print(livros)



# lista = []
# for x in range(5):
#     n = int(input("Digite um número inteiro: "))
#     lista.append(n)
#     lista.sort()
#     print(lista)

import pandas as pd
planilhas_abacate = pd.read_excel("Aulas Algoritimo e Programação\Aula e Anotações\Aula17_04_25\controle_de_abacates.xlsx")
print(planilhas_abacate['preco_medio'])
print(50*"")
print("----------------------------------------------------------------------------------------------")
print(50*"")
planilhas_empresas = pd.read_excel("Aulas Algoritimo e Programação\Aula e Anotações\Aula17_04_25\controle_da_empresa.xlsx", None)
print(planilhas_empresas['Vendas']['Total de Vendas'].sum)
planilhas_empresas.keys()
print(50*"")
print("----------------------------------------------------------------------------------------------")
print(50*"")
vendas = planilhas_empresas["Vendas"]
vendas["Data da Venda"].apply(lambda x: x.weekday()).hist(bins=7)
print(vendas)