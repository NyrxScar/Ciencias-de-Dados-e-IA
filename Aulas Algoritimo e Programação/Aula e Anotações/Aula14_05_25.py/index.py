# vendas = ('Nyrx', '22/03/2025', '18/09/2006', 4500, 'Desenvolvedora de BD Junior')
# nome, data_contratação, data_nascimento, salario, cargo = vendas


# print(nome)

vendas2 = [1000, 2000, 300, 300, 150]
funcionarios = ['João', 'Lira', 'Ana', 'Maria', 'Paula']
for item, word in enumerate(zip(vendas2, funcionarios)):
    print(f" {item} - {word}")

vendas3 = [('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
           ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
           ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
           ('20/08/2020', 'ipad', 'prata', '128gb', 981, 5000),
           ('21/08/2020', 'iphone x', 'azul', '128gb', 397, 4000),
           ('21/08/2020', 'iphone x', 'prata', '128gb', 1017, 4000),
           ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
           ('21/08/2020', 'ipad', 'prata', '128gb', 4000, 5000)]
for item in vendas3:
    data, produto, cor, capacidade, unidades_vendidas, valor_unitario = item

# somaFaturamento = 0
# for item in vendas3:
#     data, produto, cor, capacidade, unidades_vendidas, valor_unitario = item
#     if produto == 'iphone x' and data == '20/08/2020':
#         somaFaturamento += unidades_vendidas * valor_unitario
# print(f"O faturamento do Iphone no dia 20/08/2020 foi de {somaFaturamento}")

somaFaturamento1 = 0
somaFaturamento2 = 0

soma2dias = somaFaturamento1+somaFaturamento2

for item in vendas3:
    data, produto, cor, capacidade, unidades_vendidas, valor_unitario = item
    if produto == 'iphone x' and data == '20/08/2020':
        somaFaturamento1 += unidades_vendidas * valor_unitario
    if produto == 'iphone x' and data =='21/08/2020':
        somaFaturamento2 += unidades_vendidas * valor_unitario

print(f"O faturamento do Iphone no dia 20/08/2020 e 21/08/2020 foi de R$ {somaFaturamento2+somaFaturamento1:.2f}")
 
