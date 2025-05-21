# Declaração de variáveis
produto = "Notebook" # String
quantidade = 3 # int
preco = 2999.99 # float
disponivel = False # boolean

# 1
# Impressão utilizando concatenação (sem formatação de alinhamento)
print("Produto: " + produto + " | Quantidade: " + str(quantidade) + " | Preço: " +
str(preco) + " | Disponível: " + str(disponivel))

#2
# # Impressão utilizando o operador %
print("Produto: %10s | Quantidade: %-3d | Preço: %10.2f | Disponível: %5s" %
(produto, quantidade, preco, str(disponivel)))

# 3
# Impressão utilizando o método .format com alinhamento
print("Produto: {:>10} | Quantidade: {:<3} | Preço: {:>10.2f} | Disponível:{:>5}".format(produto, quantidade, preco, disponivel))

# 4
# Impressão utilizando f-string com alinhamento e precisão
print(f"Produto: {produto:>10} | Quantidade: {quantidade:<3} | Preço: {preco:>10.2f} | Disponível: {disponivel:>5}")
