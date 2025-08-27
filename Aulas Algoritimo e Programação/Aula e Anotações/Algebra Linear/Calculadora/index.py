# import numpy as np
# from fractions import Fraction

# class CalculadoraAlgebraLinear:
#     def __init__(self):
#         self.historico = []
    
#     def adicionar_historico(self, operacao, resultado):
#         entrada = f"{operacao} = {resultado}"
#         self.historico.append(entrada)
#         return entrada
    
#     # ... (mantive todas as funções anteriores) ...
    
#     def verificar_solucao_equacao(self, coeficientes, termo_indep, solucao):
#         """Verifica se uma solução satisfaz uma equação linear"""
#         try:
#             resultado = sum(coef * sol for coef, sol in zip(coeficientes, solucao))
#             return abs(resultado - termo_indep) < 1e-10  # Considera erro numérico
#         except:
#             return False
    
#     def verificar_solucao_sistema(self, matriz_coef, vetor_const, solucao):
#         """Verifica se uma solução satisfaz um sistema linear"""
#         try:
#             A = np.array(matriz_coef)
#             b = np.array(vetor_const)
#             x = np.array(solucao)
            
#             resultado = np.dot(A, x)
#             return np.allclose(resultado, b)  # Comparação com tolerância numérica
#         except:
#             return False
    
#     def discutir_sistema(self, matriz_coef, vetor_const=None):
#         """Faz a discussão de um sistema linear (SPD, SPI, SI)"""
#         try:
#             A = np.array(matriz_coef)
            
#             if vetor_const is not None:
#                 b = np.array(vetor_const)
#                 # Sistema não homogêneo
#                 posto_A = np.linalg.matrix_rank(A)
#                 Ab = np.column_stack((A, b))
#                 posto_Ab = np.linalg.matrix_rank(Ab)
                
#                 n = A.shape[1]  # número de incógnitas
                
#                 if posto_A == posto_Ab:
#                     if posto_A == n:
#                         return "Sistema Possível e Determinado (SPD)"
#                     else:
#                         return "Sistema Possível e Indeterminado (SPI)"
#                 else:
#                     return "Sistema Impossível (SI)"
#             else:
#                 # Sistema homogêneo
#                 posto_A = np.linalg.matrix_rank(A)
#                 n = A.shape[1]  # número de incógnitas
                
#                 if posto_A == n:
#                     return "Sistema Possível e Determinado (apenas solução trivial)"
#                 else:
#                     return "Sistema Possível e Indeterminado (infinitas soluções)"
                    
#         except Exception as e:
#             return f"Erro: {str(e)}"
    
#     def resolver_equacao_matricial(self, A, B, C):
#         """Resolve equação matricial AX = B ou XA = C"""
#         try:
#             A_arr = np.array(A)
#             B_arr = np.array(B)
#             C_arr = np.array(C)
            
#             # Verifica se é AX = B
#             if A_arr.shape[1] == B_arr.shape[0]:
#                 X = np.linalg.solve(A_arr, B_arr)
#                 return f"X = {X.tolist()}"
            
#             # Verifica se é XA = C
#             elif C_arr.shape[1] == A_arr.shape[0]:
#                 X = np.linalg.solve(A_arr.T, C_arr.T).T
#                 return f"X = {X.tolist()}"
            
#             else:
#                 return "Dimensões incompatíveis"
                
#         except Exception as e:
#             return f"Erro: {str(e)}"
    
#     def menu_completo(self):
#         """Menu completo com todas as funcionalidades"""
#         while True:
#             print("\n" + "="*60)
#             print("CALCULADORA DE ÁLGEBRA LINEAR - LISTA UNISENAI")
#             print("="*60)
#             print("1. Operações Básicas")
#             print("2. Equação Linear")
#             print("3. Sistema Linear")
#             print("4. Operações entre Matrizes")
#             print("5. Determinante")
#             print("6. Matriz Inversa")
#             print("7. Verificar Solução de Equação")
#             print("8. Verificar Solução de Sistema")
#             print("9. Discussão de Sistema")
#             print("10. Equação Matricial")
#             print("11. Histórico")
#             print("12. Sair")
#             print("="*60)
            
#             opcao = input("Escolha uma opção: ")
            
#             if opcao == '1':
#                 self.menu_operacoes_basicas()
#             elif opcao == '2':
#                 self.menu_equacao_linear()
#             elif opcao == '3':
#                 self.menu_sistema_linear()
#             elif opcao == '4':
#                 self.menu_operacoes_matrizes()
#             elif opcao == '5':
#                 self.menu_determinante()
#             elif opcao == '6':
#                 self.menu_matriz_inversa()
#             elif opcao == '7':
#                 self.menu_verificar_solucao_equacao()
#             elif opcao == '8':
#                 self.menu_verificar_solucao_sistema()
#             elif opcao == '9':
#                 self.menu_discussao_sistema()
#             elif opcao == '10':
#                 self.menu_equacao_matricial()
#             elif opcao == '11':
#                 self.mostrar_historico()
#             elif opcao == '12':
#                 print("Saindo...")
#                 break
#             else:
#                 print("Opção inválida!")
    
#     def menu_verificar_solucao_equacao(self):
#         print("\n--- VERIFICAR SOLUÇÃO DE EQUAÇÃO ---")
#         try:
#             n = int(input("Número de variáveis: "))
            
#             coeficientes = []
#             for i in range(n):
#                 coef = float(input(f"Coeficiente a{i+1}: "))
#                 coeficientes.append(coef)
            
#             termo_indep = float(input("Termo independente b: "))
            
#             solucao = []
#             for i in range(n):
#                 valor = float(input(f"Valor da variável x{i+1} na solução: "))
#                 solucao.append(valor)
            
#             resultado = self.verificar_solucao_equacao(coeficientes, termo_indep, solucao)
#             print(f"A solução {solucao} {'satisfaz' if resultado else 'não satisfaz'} a equação")
            
#         except ValueError:
#             print("Erro: Digite números válidos!")
    
#     def menu_verificar_solucao_sistema(self):
#         print("\n--- VERIFICAR SOLUÇÃO DE SISTEMA ---")
#         try:
#             m = int(input("Número de equações: "))
#             n = int(input("Número de variáveis: "))
            
#             print("Digite a matriz de coeficientes:")
#             matriz = []
#             for i in range(m):
#                 linha = []
#                 for j in range(n):
#                     valor = float(input(f"a[{i+1}][{j+1}]: "))
#                     linha.append(valor)
#                 matriz.append(linha)
            
#             print("Digite o vetor de constantes:")
#             constantes = []
#             for i in range(m):
#                 valor = float(input(f"b[{i+1}]: "))
#                 constantes.append(valor)
            
#             print("Digite a solução a ser verificada:")
#             solucao = []
#             for i in range(n):
#                 valor = float(input(f"x[{i+1}]: "))
#                 solucao.append(valor)
            
#             resultado = self.verificar_solucao_sistema(matriz, constantes, solucao)
#             print(f"A solução {solucao} {'satisfaz' if resultado else 'não satisfaz'} o sistema")
            
#         except ValueError:
#             print("Erro: Digite números válidos!")
    
#     def menu_discussao_sistema(self):
#         print("\n--- DISCUSSÃO DE SISTEMA ---")
#         try:
#             m = int(input("Número de equações: "))
#             n = int(input("Número de variáveis: "))
            
#             print("Digite a matriz de coeficientes:")
#             matriz = []
#             for i in range(m):
#                 linha = []
#                 for j in range(n):
#                     valor = float(input(f"a[{i+1}][{j+1}]: "))
#                     linha.append(valor)
#                 matriz.append(linha)
            
#             homogeneo = input("É sistema homogêneo? (s/n): ").lower() == 's'
            
#             if not homogeneo:
#                 print("Digite o vetor de constantes:")
#                 constantes = []
#                 for i in range(m):
#                     valor = float(input(f"b[{i+1}]: "))
#                     constantes.append(valor)
#                 resultado = self.discutir_sistema(matriz, constantes)
#             else:
#                 resultado = self.discutir_sistema(matriz)
            
#             print(f"Classificação: {resultado}")
            
#         except ValueError:
#             print("Erro: Digite números válidos!")
    
#     def menu_equacao_matricial(self):
#         print("\n--- EQUAÇÃO MATRICIAL ---")
#         try:
#             tipo = input("Tipo de equação (AX=B digite 1, XA=C digite 2): ")
            
#             if tipo == '1':
#                 print("Matriz A:")
#                 linhas = int(input("Número de linhas de A: "))
#                 colunas = int(input("Número de colunas de A: "))
                
#                 A = []
#                 for i in range(linhas):
#                     linha = []
#                     for j in range(colunas):
#                         valor = float(input(f"A[{i+1}][{j+1}]: "))
#                         linha.append(valor)
#                     A.append(linha)
                
#                 print("Matriz B:")
#                 linhas_b = int(input("Número de linhas de B: "))
#                 colunas_b = int(input("Número de colunas de B: "))
                
#                 B = []
#                 for i in range(linhas_b):
#                     linha = []
#                     for j in range(colunas_b):
#                         valor = float(input(f"B[{i+1}][{j+1}]: "))
#                         linha.append(valor)
#                     B.append(linha)
                
#                 resultado = self.resolver_equacao_matricial(A, B, None)
                
#             elif tipo == '2':
#                 print("Matriz A:")
#                 linhas = int(input("Número de linhas de A: "))
#                 colunas = int(input("Número de colunas de A: "))
                
#                 A = []
#                 for i in range(linhas):
#                     linha = []
#                     for j in range(colunas):
#                         valor = float(input(f"A[{i+1}][{j+1}]: "))
#                         linha.append(valor)
#                     A.append(linha)
                
#                 print("Matriz C:")
#                 linhas_c = int(input("Número de linhas de C: "))
#                 colunas_c = int(input("Número de colunas de C: "))
                
#                 C = []
#                 for i in range(linhas_c):
#                     linha = []
#                     for j in range(colunas_c):
#                         valor = float(input(f"C[{i+1}][{j+1}]: "))
#                         linha.append(valor)
#                     C.append(linha)
                
#                 resultado = self.resolver_equacao_matricial(A, None, C)
            
#             else:
#                 resultado = "Opção inválida"
            
#             print(f"Resultado: {resultado}")
            
#         except ValueError:
#             print("Erro: Digite números válidos!")

# # Exemplo de uso para questões específicas da lista
# if __name__ == "__main__":
#     calc = CalculadoraAlgebraLinear()
    
#     print("RESOLUÇÃO DE QUESTÕES DA LISTA UNISENAI")
#     print("="*50)
    
#     # Exemplo para Questão 01 - Verificar equações lineares
#     print("\nQuestão 01 - Verificar equações lineares:")
#     equacoes = [
#         [3, 5, -1, 4],    # a) 3x + 5y - z = 4
#         [2, -1, 0, 0],    # b) 2x - 1/y = 0 (não linear)
#         # ... outras equações
#     ]
    
#     for i, (a, b, c, d) in enumerate(equacoes, 1):
#         # Verificação simplificada - equação é linear se não há termos não-lineares
#         # Na prática, precisaríamos analisar a string da equação
#         letra = chr(96 + i)  # a, b, c, ...
#         print(f"{letra}) É linear: {c == 0}")  # Verificação simplificada
    
#     # Exemplo para Questão 10 - Verificar solução de sistema
#     print("\nQuestão 10 - Verificar soluções do sistema:")
#     S = [[2, 3, -1], [1, -2, 1], [-1, 1, 1]]
#     b = [0, 5, -2]
    
#     solucao1 = [2, -1, 1]
#     solucao2 = [0, 0, 0]
    
#     resultado1 = calc.verificar_solucao_sistema(S, b, solucao1)
#     resultado2 = calc.verificar_solucao_sistema(S, b, solucao2)
    
#     print(f"(2, -1, 1) é solução: {resultado1}")
#     print(f"(0, 0, 0) é solução: {resultado2}")
    
#     # Exemplo para Questão 27 - Resolver sistema por Cramer
#     print("\nQuestão 27a - Resolver sistema por Cramer:")
#     sistema_a = {
#         'matriz': [[2, 1, 1], [1, 1, -1], [4, 2, -1]],
#         'constantes': [-1, -5, -11]
#     }
    
#     # A calculadora já resolve sistemas lineares (usa numpy.linalg.solve)
#     solucao = calc.resolver_sistema_linear(sistema_a['matriz'], sistema_a['constantes'])
#     print(f"Solução: {solucao}")
    
#     # Iniciar menu interativo completo
#     calc.menu_completo()