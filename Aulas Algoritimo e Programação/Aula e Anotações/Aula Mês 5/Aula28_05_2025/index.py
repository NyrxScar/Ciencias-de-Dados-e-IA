#Escopo de Pesquisa para a atividade pode ignorar Professor só para fins de base:
# O programa deve:
# •	- Imprimir todos os pets da lista. - Confere
# •	- Imprimir cada serviço da tupla, mostrando nome e preço. - Confere
# •	- Percorrer o dicionário agenda e gerar um relatório formatado. - confere? 
# •	- Calcular o total faturado somando todos os preços em agenda e exibir no final. - confere


# linguagens_populares = {'Python': 2, 'Java': 1, 'Javascript': 3}
# chaves = linguagens_populares.keys()
# print(f"Estas são as chaves - {list(chaves)}")
# linguagens_populares = {'Python': 2, 'Java': 1, 'Javascript': 3}
# valores = linguagens_populares.values()
# print(f"Lista de Valores: {list(valores)}") 
# chaves1 = ['a', 'b', 'c']
# valores1 = [1, 2, 3]
# dicionario = dict(zip(chaves1, valores1))
# print(dicionario)


# Atividade --------------------------------------------------------------------
# 
pets = [ "Anúbis", "Wanreda", "Mitsuki", "Layo", "Iráma"]
print(pets)
servicos = { "Limpeza bocal": 20, "Banho": 95, "Tosa": 110, "Raio x": 300, "Vacina": 120}
servicosChaves = servicos.keys()
servicosPrecos = servicos.values()
nomePreco = dict(zip(pets,[{"Preço": list(servicosPrecos)[i]} for i in range(len(pets))]))
print(nomePreco)
tutor = [ "Tutor A", "Tutor B", "Tutor C", "Tutor D", "Tutor E"]
data = ["21/04/25", "22/04/25",  "23/04/25",  "24/04/25", "25/04/25"]
agenda = dict(zip(pets,[{ "tutor": tutor[i], "servicos": list(servicosChaves)[i],"preço": list(servicosPrecos)[i], "data": data[i]} for i in range(len(pets))]))
print(agenda)
SomaPrecos = sum(servicosPrecos)
print(f"Total Faturado: R$ {SomaPrecos} reais")

#    - valor: outro dicionário com as chaves pets, "tutor", "servico", "preco" e "data". 





