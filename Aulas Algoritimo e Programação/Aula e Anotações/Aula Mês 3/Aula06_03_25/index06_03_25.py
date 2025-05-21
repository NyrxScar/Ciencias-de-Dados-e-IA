minutos = 700
horas = minutos/60
print (minutos, "minutos corresponde a", horas, "horas")
minutos = 500
horas = minutos/60
print (minutos, "minutos corresponde a", horas, "horas")
minutos = 700
horas = minutos//60
print (minutos, "minutos corresponde a", horas, "horas")
minutos = 500
horas = minutos//60
print (minutos, "minutos corresponde a", horas, "horas")
# ////////////////////////////////////////////////////////
num1 = 20
num2 = 30
soma = num1 + num2
print(soma)
# /////////////////////////////////////////////////////////
num1 = int(input("Digite o valor do primeiro número:"))
num2 = int(input("Digite o valor do segundo número:"))
soma = num1 + num2
print("A soma dos dois números é:", soma)
# /////////////////////////////////////////////////////////
nome =input("Digite o seu nome: ")
print("O nome digitado é: ", nome)
# /////////////////////////////////////////////////////////
# Treinando o %s (Posicionador):
nome =input("Digite o seu nome: ")
print("%s é seu nome: " %nome)
# /////////////////////////////////////////////////////////
num1 = float(input("Digite o valor do primeiro número:"))
num2 = float(input("Digite o valor do segundo número:"))
soma = num1 + num2
print("A soma entre %.2f e %.2f é %.2f !"%(num1, num2, soma))
# /////////////////////////////////////////////////////////
nome = "Nyrx"
idade = 18
mensagem = "Meu nome é {} e eu tenho {} anos de idade !" .format(nome, idade)
print(mensagem)
