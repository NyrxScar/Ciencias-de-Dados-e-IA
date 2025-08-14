lucro_1tri = {'Janeiro': 100000, 'Fevereiro': 120000, 'Março': 90000}
lucro_2tri = {'Abril': 88000, 'Maio': 89000, 'Junho': 120000}

del lucro_2tri['Junho']
print(lucro_2tri)

lucro_jun = lucro_2tri.pop('Maio')
print(lucro_2tri)
print(lucro_1tri)
lucro_2tri.clear()
print(lucro_2tri)
