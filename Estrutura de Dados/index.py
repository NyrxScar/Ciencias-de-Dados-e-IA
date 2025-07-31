# from random import random
# notas = [7.5, 8.0, 6.5]
# # print(notas)
# # len(notas)
# nota = 0
# while nota != "-1":
#     nota = input("Digite a nota -1 para sair: ")
#     if nota != "-1":
#         notas.append(float(nota))
# for indice in notas:
#     if indice > 7:
#         print(indice)

notas = [7.5, 4.0, 8.2, 6.7, 9.1, 5.5, 3.8, 7.0, 6.3, 8.9, 2.5, 10.0, 7.7, 5.0, 6.8, 9.5, 4.5, 7.2, 8.4, 1.9]
mediaNotas = sum(notas)/len(notas)
maiorNota = max(notas)

maxNota = notas[0]
for indice in range(len(notas)):
    if notas[indice] > maxNota:
        maxNota = notas[indice]
print(f"Nota Máxima: {maxNota}")

minNota = notas[0]
for indice in range(len(notas)):
    if notas[indice] < minNota:
        minNota = notas[indice]
print(f"Nota Menor: {minNota}")

print(f"Média, Mínima e Máxima: {mediaNotas}, {maxNota} e {minNota}")



aluno1 = [7.5, 4.0, 8.2, 6.7, 9.1]
for indice in aluno1:
     if indice > 7:
        print(f"Aluno 1 e suas respectivas notas acima de 7: {indice}")
aluno2 = [5.5, 3.8, 7.0, 6.3, 8.9]
for indice in aluno2:
     if indice > 7:
        print(f"Aluno 2 e suas respectivas notas acima de 7: {indice}")
aluno3 = [2.5, 10.0, 7.7, 5.0, 6.8]
for indice in aluno3:
     if indice > 7:
        print(f"Aluno 3 e suas respectivas notas acima de 7: {indice}")
aluno4 = [9.5, 4.5, 7.2, 8.4, 1.9]
for indice in aluno4:
     if indice > 7:
        print(f"Aluno 4 e suas respectivas notas acima de 7: {indice}")
