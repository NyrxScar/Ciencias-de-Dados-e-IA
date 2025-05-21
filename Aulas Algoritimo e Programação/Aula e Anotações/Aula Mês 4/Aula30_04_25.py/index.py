# import random
# def Criar_lista_aleatoria(tamanho):
#     lista = []
#     for i in range(tamanho):
#         valor = random.randint(0, 100)
#         lista.append(valor)
#     return lista, max(lista), min(lista)
# tam = 5
# list, maxlist, minlist = Criar_lista_aleatoria(tam)
# print(list)
# print(maxlist)
# print(minlist)

############################################

# def soma(a, b, c):
#     print(a + b + c)
# soma(1, 2, 3)
# soma(3, 4, 5)

############################################
# a = int(input("Digite o valor de A: "))
# b = int(input("Digite o valor de B: "))
# c = int(input("Digite o valor de C: "))


# def soma3(parcela1, parcela2, parcela3):
#     return(parcela1 + parcela2 + parcela3)
# print(f"A soma das 3 parcelas é: {soma3(parcela1=a, parcela2=b, parcela3=c)}")

############################################

menuLista = ["Retângulo", "Triângulo", "Círculo", "Sair"]
def area_retangulo(lado1, lado2, area1):
    lado1 = float(input("Digite o valor do lado 1 do retângulo: "))
    lado2 = float(input("Digite o valor do lado 2 do retângulo: "))
    area1 = lado1 * lado2
    return area1

def area_triangulo(base, altura, area3):
    base = float(input("Digite o valor da base do triângulo: "))
    altura = float(input("Digite o valor da altura do triângulo: "))
    area3 = (base * altura) / 2
    return area3

def area_circulo(raio, area2):
    raio = float(input("Digite o valor do raio do círculo: "))
    area2 = 3.14 * (raio ** 2)
    return area2

lado1 = float(input("Digite o valor do lado 1 do retângulo: "))
lado2 = float(input("Digite o valor do lado 2 do retângulo: "))
area1 = lado1 * lado2
base = float(input("Digite o valor da base do triângulo: "))
altura = float(input("Digite o valor da altura do triângulo: "))
area3 = (base * altura) / 2
raio = float(input("Digite o valor do raio do círculo: "))
area2 = 3.14 * (raio ** 2)

def menu():
    while True:
        for index, word in enumerate(menuLista):
            print(f"Carros disponíveis: {index} - {word}")
        opcao = input("Digite a opção desejada: ")
        if opcao.isdigit() == 1 or 'retangulo' in opcao:
            return area_retangulo(lado1, lado2, area1)
        else:
            if opcao.isdigit() == 2 or 'triangulo' in opcao:
                return area_triangulo(base, altura, area3)
            else:
                    if opcao.isdigit() == 3 or 'circulo' in opcao:
                        return area_circulo(raio, area2)
                    else:
                        if opcao.isdigit() == 4 or 'sair' in opcao:
                            print("Saindo...")
                            break
            print(f"Você escolheu a opção {opcao}")
print(menu())









