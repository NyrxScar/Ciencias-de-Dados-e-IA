# x = 12
# y = 0
# try:
#     z = x/y
# except ZeroDivisionError:
#     print("Não é possível dividir por zero")
# else:
#     print(z)

################################################

# def ler_int(mensagem, mensagem_erro):
#     while True:
#         try:
#             entrada = int(input(mensagem))
#             return entrada
#         except ValueError:
#             print(mensagem_erro) 
            
################################################

# mensagem = "Digite um número inteiro: "
# mensagem_erro = "Número inválida. "
# x = ler_int(mensagem, mensagem_erro)
# y = ler_int(mensagem, mensagem_erro)
# print(f"A soma de {x} e {y} é {x+y}")

################################################

# print("Vamos dividir dois números inseridos por você\n")
# num1 = input("Digite o primeiro número: ")
# num2 = input("Digite o segundo número: ")
# try:
#     resultado = int(num1) / int(num2)
#     print("O resultado é " + str(resultado))
# except ZeroDivisionError:
#     print("O segundo número não pode ser zero")
# except ValueError:
#     print("Você deve inserir 2 números")
# except Exception:
#     print("Erro geral")


################################################

# try:
#     idade = int(input("Digite sua idade: "))
#     if (idade <= 0) or (idade >= 110):
#         raise ValueError("Idade deve ser um número positivo")
# except ValueError as erro:
#     raise ValueError(f"Erro de entrada: {erro}")

################################################

