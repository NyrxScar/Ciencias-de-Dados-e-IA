# Exercício 1: Escreva um programa em Python que imprima a frase “Olá, mundo!” na tela.
# 1. Escrever a função print
# 2. Escrever a string "Olá Mundo"

print("Olá mundo")

# /////////////////////////////////////////////////////////////////////////////////

# Exercício 2: Crie um programa em Python que imprima seu nome completo.

# 1. Escrever a variavel nomeCompleto
# 2. Atribuir a string do nome completo a variável
# 3. Escrever a função print chamando a variavel nome completo

nomeCompleto = "Nyrx Oliveira de Aquino Farias"
print(nomeCompleto)

# /////////////////////////////////////////////////////////////////////////////////

# Exercício 3: : Escreva um programa em Python que atribua um valor inteiro à variável numero e imprima esse valor na tela.


# 1. Escrever a variavel valorInteiro
# 2. Atribuir o numero inteiro a variável numero
# 3. Escrever a função print chamando a variavel numero

numero = int(2)
print(numero)

# /////////////////////////////////////////////////////////////////////////////////

# Exercício 4: Crie um programa em Python que atribua seu nome a uma variável nome e
# imprima na tela a seguinte mensagem: “Olá, [nome]! Seja bem-vindo(a) ao curso de Python!”.

# 1. Escrever a variavel nome
# 2. Atribuir a string do nome a variável
# 3. Escrever a função print chamando a variavel nome na frase “Olá, [nome]! Seja bem-vindo(a) ao curso de Python!”, através do metodo do formatação f

nome = "Nyrx Oliveira de Aquino Farias"
print(f"Olá, {nome}! Seja bem-vinda ao curso de Python!")

# /////////////////////////////////////////////////////////////////////////////////

# Exercício 5: Escreva um programa em Python que atribua um valor do tipo float à variável peso e imprima o valor dela na tela.

# 1. Escrever a variavel peso
# 2. Atribuir o numero decimal a variável float peso
# 3. Escrever a função print chamando a variavel peso

peso = float(35.4)
print(peso)

# /////////////////////////////////////////////////////////////////////////////////

# Exercício 6: Crie um programa em Python que atribua dois valores inteiros às variáveis a e b, e imprima a soma desses valores na tela.

# 1. Escrever a variavel a e b
# 2. Atribuir o numero inteiro 50 e 30 a variável a e b, respectivamente
# 3. Escrever a função print chamando a operação de soma com as variaveis a e b

a = int(50)
b = int(30)

print (a+b)

# /////////////////////////////////////////////////////////////////////////////////

# Exercício 7: Escreva um programa em Python que atribua um valor complexo à variável numero_complexo e imprima esse valor na tela.

# 1. Escrever a variavel j e atribuit um valor 
# 1. Escrever a variavel parte_real e atribuir um valor 
# 1. Escrever a variavel parte_imaginaria e atribuir um coeficiente numerico multiplicando a variavel j
# 1. Escrever a a formula do numero complexo que parte real + parte imaginaria
# 1. Escrever a função print com uma mensagem formatada que chama o resultado do numero complexo
 

j = 21
parte_real = 3
parte_imaginaria = 4*j 
numero_complexo = parte_real + parte_imaginaria
print(f"O valor do número complexo é {numero_complexo}")


# /////////////////////////////////////////////////////////////////////////////////

# Exercício 8: Crie um programa em Python que atribua um valor booleano à variável verdadeiro e imprima o valor dela na tela.

# 1. Escrever a variável idade
# 2. Atribuir um número inteiro à variável idade
# 3. Escrever a variável Maior_Idade com a condição de ser maior ou igual a 18
# 4. Escrever a função print chamando a variável Maior_Idade, verificando se é True ou False

idade = int(17)
Maior_Idade = idade >= 18
print(Maior_Idade)

# /////////////////////////////////////////////////////////////////////////////////

# Exercício 9: Crie um programa em Python que atribua dois valores inteiros às variáveis largura e altura, e imprima a área de um retângulo utilizando esses valores.

# 1. Escrever as variáveis largura e altura
# 2. Atribuir valores inteiros às variáveis
# 3. Criar a variável area_retangulo com a multiplicação de largura e altura
# 4. Escrever a função print chamando a variável area_retangulo

largura = 3
altura = 4
area_retangulo = largura*altura
print("A área do retangulo é", area_retangulo)

# /////////////////////////////////////////////////////////////////////////////////

# Exercício 10: Escreva um programa em Python que atribua um valor do tipo float à variável dolar e imprima o valor do dólar utilizando esse valor. Considere que o valor do dólar hoje é 5.50.

# 1. Escrever as variável dolar atribuindo o valor float 5.10
# 2. Escrever as variável qnt_dolares atribuindo o valor 21
# 3. Chamar a função print através da formatação indicando a quantidade de dólares e o equivalente
# 4. Escrever a função print chamando as variáveis junto com texto contextualizando

dolar = float(5.10)
qnt_dolares = 21
print(f"Você tem {qnt_dolares} dólares, equivalente a R$ {qnt_dolares * dolar:.2f}")

# /////////////////////////////////////////////////////////////////////////////////

# Exercício 11: Crie um programa em Python que atribua dois valores inteiros às variáveis a e b, e imprima o resultado da multiplicação desses valores na tela.

# 1. Escrever as variáveis a e b
# 2. Atribuir valores inteiros às variáveis a e b
# 3. Criar a variável multiplicacao com a operação de multiplicação
# 4. Escrever a função print chamando a variável multiplicacao

a = 11
b = 41
multiplicacao = a*b
print("O valor da multiplicação é", multiplicacao)