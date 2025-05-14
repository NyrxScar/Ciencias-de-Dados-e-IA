# Exercício 1 – Faturamento total de produtos pretos

vendas = [
 ('05/09/2020', 'iPhone 13', 'preto', '256GB', 12, 6000),
 ('05/09/2020', 'iPhone 13', 'azul', '256GB', 8, 6000),
 ('05/09/2020', 'Samsung Galaxy S21', 'preto', '128GB', 15, 4000),
 ('05/09/2020', 'Xiaomi 12', 'preto', '256GB', 20, 3000),
 ('05/09/2020', 'Xiaomi 12', 'azul', '256GB', 10, 3000),
 ('05/09/2020', 'Motorola Edge', 'preto', '128GB', 9, 2800),
 ('05/09/2020', 'LG Wing', 'rosa', '128GB', 7, 2500),
 ('05/09/2020', 'Nokia 6.2', 'preto', '64GB', 11, 1600),
 ('05/09/2020', 'iPhone 11', 'verde', '128GB', 10, 4000),
 ('05/09/2020', 'iPhone SE', 'vermelho', '64GB', 6, 3200),
]
somaFaturamento = 0
for item in vendas:
    data, produto, cor, capacidade, unidades_vendidas, valor_unitario = item
    if cor == 'preto':
        somaFaturamento += unidades_vendidas * valor_unitario
print(f"O faturamento dos produtos pretos foram de R$ {somaFaturamento:.2f}")

# ---------------------------------------------------------------------------------

# Exercício 2 – Total de unidades vendidas por um modelo

somaUnidadesVendidas = 0
for item in vendas:
    data, produto, cor, capacidade, unidades_vendidas, valor_unitario = item
    if produto == 'Xiaomi 12':
        somaUnidadesVendidas += unidades_vendidas
print(f"A soma das unidades vendidas foi de {somaUnidadesVendidas:.2f}")

# ---------------------------------------------------------------------------------

# Exercício 3 – Faturamento de um modelo com cor e capacidade específicas

somaFaturamento2 = 0
for item in vendas:
    data, produto, cor, capacidade, unidades_vendidas, valor_unitario = item
    if cor == 'preto' and produto == 'iPhone 13' and capacidade == '256GB':
        somaFaturamento2 += unidades_vendidas * valor_unitario
print(f"A soma do faturamento total do modelo 'iPhone 13', na cor 'preto' e com '256GB' foi de R$ {somaFaturamento2:.2f}")

# ---------------------------------------------------------------------------------

# Exercício 4 – Produto mais vendido (em unidades)

maximo = 0
for item in vendas:
    data, produto, cor, capacidade, unidades_vendidas, valor_unitario = item
    if maximo == max(unidades_vendidas[0], unidades_vendidas[1], unidades_vendidas[2]):
        print(maximo)




# vendas2 = [1000, 2000, 300, 300, 150]
# funcionarios = ['João', 'Lira', 'Ana', 'Maria', 'Paula']
# for item, word in enumerate(zip(vendas2, funcionarios)):
#     print(f" {item} - {word}")

# vendas3 = [('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
#            ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
#            ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
#            ('20/08/2020', 'ipad', 'prata', '128gb', 981, 5000),
#            ('21/08/2020', 'iphone x', 'azul', '128gb', 397, 4000),
#            ('21/08/2020', 'iphone x', 'prata', '128gb', 1017, 4000),
#            ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
#            ('21/08/2020', 'ipad', 'prata', '128gb', 4000, 5000)]
# for item in vendas3:
#     data, produto, cor, capacidade, unidades_vendidas, valor_unitario = item

# # somaFaturamento = 0
# # for item in vendas3:
# #     data, produto, cor, capacidade, unidades_vendidas, valor_unitario = item
# #     if produto == 'iphone x' and data == '20/08/2020':
# #         somaFaturamento += unidades_vendidas * valor_unitario
# # print(f"O faturamento do Iphone no dia 20/08/2020 foi de {somaFaturamento}")

# somaFaturamento1 = 0
# somaFaturamento2 = 0

# soma2dias = somaFaturamento1+somaFaturamento2

# for item in vendas3:
#     data, produto, cor, capacidade, unidades_vendidas, valor_unitario = item
#     if produto == 'iphone x' and data == '20/08/2020':
#         somaFaturamento1 += unidades_vendidas * valor_unitario
#     if produto == 'iphone x' and data =='21/08/2020':
#         somaFaturamento2 += unidades_vendidas * valor_unitario

# print(f"O faturamento do Iphone no dia 20/08/2020 e 21/08/2020 foi de R$ {somaFaturamento2+somaFaturamento1:.2f}")