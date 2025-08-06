# # from random import random
# # notas = [7.5, 8.0, 6.5]
# # # print(notas)
# # # len(notas)
# # nota = 0
# # while nota != "-1":
# #     nota = input("Digite a nota -1 para sair: ")
# #     if nota != "-1":
# #         notas.append(float(nota))
# # for indice in notas:
# #     if indice > 7:
# #         print(indice)

# notas = [7.5, 4.0, 8.2, 6.7, 9.1, 5.5, 3.8, 7.0, 6.3, 8.9, 2.5, 10.0, 7.7, 5.0, 6.8, 9.5, 4.5, 7.2, 8.4, 1.9]
# mediaNotas = sum(notas)/len(notas)
# maiorNota = max(notas)

# maxNota = notas[0]
# for indice in range(len(notas)):
#     if notas[indice] > maxNota:
#         maxNota = notas[indice]
# print(f"Nota Máxima: {maxNota}")

# minNota = notas[0]
# for indice in range(len(notas)):
#     if notas[indice] < minNota:
#         minNota = notas[indice]
# print(f"Nota Menor: {minNota}")

# print(f"Média, Mínima e Máxima: {mediaNotas:.2f}, {maxNota} e {minNota}")



# aluno1 = [7.5, 4.0, 8.2, 6.7, 9.1]
# for indice in aluno1:
#      if indice > 7:
#         print(f"Aluno 1 e suas respectivas notas acima de 7: {indice}")
# aluno2 = [5.5, 3.8, 7.0, 6.3, 8.9]
# for indice in aluno2:
#      if indice > 7:
#         print(f"Aluno 2 e suas respectivas notas acima de 7: {indice}")
# aluno3 = [2.5, 10.0, 7.7, 5.0, 6.8]
# for indice in aluno3:
#      if indice > 7:
#         print(f"Aluno 3 e suas respectivas notas acima de 7: {indice}")
# aluno4 = [9.5, 4.5, 7.2, 8.4, 1.9]
# for indice in aluno4:
#      if indice > 7:
#         print(f"Aluno 4 e suas respectivas notas acima de 7: {indice}")


from dataclasses import dataclass

@dataclass
class Aluna:
    nome:str
    idade:int

Estudante = Aluna("Nyrx", 18)
print(Estudante)
@dataclass
class Livro:
    Título: str
    autor: str
    ano: int
    preço: float

    def media(self2):
        if self2.preço > 86.4:
            return "Livro que está com o preço acima da média dos valores da livraria"
        else:
            return "Livro que está com o preço abaixo da média dos valores da livraria"

    def recente(self):
         if self.ano <= 2000:
            return "Livro de antes dos anos 2000"
         else:
            return "Livro de depois dos anos 2000"


Informacoes_livro = [
    Livro("As vantagens de ser invisível", "Stephen Chbosky", 2012, 70.0),
    Livro("O Segundo Sexo", "Simone de Beauvoir", 1949, 120.0),
    Livro("A Hora do Vermelho", "Clarice Lispector", 1965, 85.0),
    Livro("O Labirinto das Memórias", "Igor Pires", 2020, 65.5),
    Livro("Água Viva: Fragmentos Reencontrados", "Clarice Lispector e Igor Pires", 1973, 92.0)
]
for livro in Informacoes_livro:
    print(f"Desafio 1: {livro.Título} é um: {livro.recente()}")  
    print(f" Desafio 2: {livro.Título} é um: {livro.media()}\n")  



# print(Informacoes_livro)
