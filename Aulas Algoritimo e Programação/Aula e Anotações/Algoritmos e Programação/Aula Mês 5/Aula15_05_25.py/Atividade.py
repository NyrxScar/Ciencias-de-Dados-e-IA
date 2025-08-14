# Exercício 1: Crie um dicionário vazio chamado linguagens.

linguagens = {}
print(linguagens)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Exercício 2: Adicione as seguintes informações ao dicionário linguagens:
# Chave: ‘Python’, Valor: ‘Linguagem de programação de alto nível’
# Chave: ‘Java’, Valor: ‘Linguagem de programação orientada a objeto’
# Chave: ‘JavaScript’, Valor: ‘Linguagem de programação interpretada’


linguagens = {'Python': 'Linguagem de programação de alto nível', 'Java':'Linguagem de programação orientada a objeto', 'JavaScript': 'Linguagem de programação interpretada'}
print(linguagens)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Exercício 3: Acesse o valor correspondente à chave ‘Java’ no dicionário linguagens e armazene-o em uma variável chamada descricao_java.

linguagens = {'Python': 'Linguagem de programação de alto nível', 'Java':'Linguagem de programação orientada a objeto', 'JavaScript': 'Linguagem de programação interpretada'}
descricao_java = linguagens['Java']
print(descricao_java)

# capitais = {"Brasil": "Brasília", "Alemanha": "Berlim", "Japão": "Tóquio"}
# capital_brasil = capitais["Brasil"]
# print(capital_brasil)  # Saída: Brasília



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Exercício 4: Verifique se a chave ‘Python’ existe no dicionário linguagens e armazene o resultado em uma variável chamada python_existe.


linguagens = {'Python': 'Linguagem de programação de alto nível', 'Java':'Linguagem de programação orientada a objeto', 'JavaScript': 'Linguagem de programação interpretada'}
print(linguagens)
verificarPython = input("Digite a linguagens que você quer verificar no dicionário: ")

if verificarPython in linguagens:
    valorPython = linguagens[verificarPython]
    print(f"A chave {verificarPython} existe no dicionário Linguagens ")
else:
    print(f"A chave {verificarPython} não existe no dicionário Linguagens")


# pais = "Itália"
# if pais in capitais:
#     capital = capitais[pais]
#     print(f"A capital de {pais} é {capital}.")
# else:
#     print(f"A capital de {pais} não foi encontrada!")



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Exercício 5: Crie um novo dicionário chamado linguagens_populares com as seguintes informações:
# Chave: ‘Python’, Valor: 2
# Chave: ‘Java’, Valor: 1
# Chave: ‘JavaScript’, Valor: 3


linguagens_populares = {'Python': 2, 'Java': 1, 'Javascript': 3}



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Exercício 6: Atualize o valor da chave ‘Python’ no dicionário linguagens_populares para 4.

linguagens_populares = {'Python': 2, 'Java': 1, 'Javascript': 3}

linguagens_populares['Python'] = 4
print(f"Este é o dicionário Linguagens Populares com o valor de Python atualizado - {linguagens_populares}")

# # Modificando valor existente
# capitais["Brasil"] = "Rio de Janeiro"

# print(capitais)
# {'Brasil': 'Rio de Janeiro', 
#  'Alemanha': 'Berlim'}


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Exercício 7: Remova a chave ‘Java’ do dicionário linguagens_populares.

linguagens_populares = {'Python': 2, 'Java': 1, 'Javascript': 3}
del linguagens_populares['Java']
print(f"Este é o dicionário sem o Java - {linguagens_populares}")

# capitais = {"Brasil": "Brasília", 
#            "Alemanha": "Berlim", 
#            "Japão": "Tóquio"}
           
# del capitais["Brasil"]

# print(capitais)
# # {'Alemanha': 'Berlim', 
# #  'Japão': 'Tóquio'}

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Exercício 8: Crie uma variável chamada chaves e atribua a ela uma lista com todas as chaves do dicionário linguagens_populares.


linguagens_populares = {'Python': 2, 'Java': 1, 'Javascript': 3}
chaves = linguagens_populares.keys()
print(f"Estas são as chaves - {list(chaves)}")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Exercício 9: Crie uma variável chamada valores e atribua a ela uma lista com todos os valores do dicionário linguagens_populares.

linguagens_populares = {'Python': 2, 'Java': 1, 'Javascript': 3}
valores = linguagens_populares.values()
print(f"Lista de Valores: {list(valores)}") 

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Exercício 10: Crie uma variável chamada itens e atribua a ela uma lista de tuplas contendo todos os itens do dicionário linguagens_populares.

linguagens_populares = {'Python': 2, 'Java': 1, 'Javascript': 3}
itens = linguagens_populares.items()
print(list(itens))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Exercício 11: Crie um novo dicionário chamado linguagens_duplicadas com as seguintes informações:
# Chave: ‘Python’, Valor: 3
# Chave: ‘Java’, Valor: 3
# Chave: ‘JavaScript’, Valor: 3


linguagens_duplicadas = {'Python': 3, 'Java': 3 , 'Javascript': 3}

# Exercício 12: Verifique se pelo menos um dos valores do dicionário linguagens_duplicadas é igual a 5 e armazene o resultado em uma variável chamada valor_cinco_existe

linguagens_duplicadas = {'Python': 3, 'Java': 3 , 'Javascript': 3}

valor_cinco_existe = False  

for valor in linguagens_duplicadas.values():
    if valor == 5:
        valor_cinco_existe = True
        break  

print(valor_cinco_existe)  
