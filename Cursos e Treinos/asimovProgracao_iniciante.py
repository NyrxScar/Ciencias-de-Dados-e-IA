lista = ["Bem", "vinda", "Nyrx", "!"]
print(len(lista)) # "len" no phyton é o leng do js que diz o tamanho da lista
print(len(lista[0])) # estou verificando o numero de caracteres na palavra bem

print(lista[-1]) # o número negativo inverte a ordem já que a lista começa no 0
print(lista[1:3]) # o ":" vai fazer com que apareça o intervalo sem contar o dado ou seja a posição que você colocou dentro, no caso exemplo agora é 3, tipo um intervalo aberto na direita
#obs: td que fizer com array/lista da para fazer com a string pois ela não deixa de ser um array
booleano = 5 >= 4
print(booleano)
booleano2 = 5 and 3 >= 4 #verifica se pelo menos um dos numeros torna a função verdadeira
print(booleano)
#///////////////////////////////////////////////////////////////
idade = int(input("Digite sua idade: "))
Maior_Idade = idade >= 18
if (Maior_Idade):
    print("Você é maior de idade") 
else:
    print("Você não é maior de idade")



