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

mais_vendido = vendas[0]

for item in vendas:
    data, produto, cor, capacidade, unidades_vendidas, valor_unitario = mais_vendido
    if item[4] > mais_vendido[4]:
         mais_vendido = item


print(f"O item com mais unidades vendidas foi {produto} de {cor} com {capacidade} de armazenamentos e com {unidades_vendidas} unidades.")