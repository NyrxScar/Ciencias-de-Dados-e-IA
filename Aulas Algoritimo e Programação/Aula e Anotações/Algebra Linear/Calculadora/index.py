import math
import cmath
import numpy as np

def calculadora_avancada():
    print("Calculadora Científica Avançada")
    print("1: Operações Básicas")
    print("2: Funções Científicas")
    print("3: Operações com Matrizes")
    print("4: Sistemas Lineares")
    print("5: Números Complexos")
    print("0: Sair")
    
    while True:
        try:
            categoria = input("\nDigite o número da categoria desejada (ou 0 para sair): ")
            
            if categoria == '0':
                print("Saindo da calculadora...")
                break
                
            elif categoria == '1':  # Operações Básicas
                print("\nOperações Básicas:")
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                print("1: Soma (+)")
                print("2: Subtração (-)")
                print("3: Multiplicação (*)")
                print("4: Divisão (/)")
                print("5: Potência (^)")
                op = input("Escolha a operação: ")
                
                if op == '1':
                    print(f"Resultado: {a} + {b} = {a + b}")
                elif op == '2':
                    print(f"Resultado: {a} - {b} = {a - b}")
                elif op == '3':
                    print(f"Resultado: {a} * {b} = {a * b}")
                elif op == '4':
                    if b == 0:
                        print("Erro: Divisão por zero!")
                    else:
                        print(f"Resultado: {a} / {b} = {a / b}")
                elif op == '5':
                    print(f"Resultado: {a}^{b} = {a ** b}")
                else:
                    print("Operação inválida!")
                    
            elif categoria == '2':  # Funções Científicas
                print("\nFunções Científicas:")
                print("1: Raiz Quadrada (√)")
                print("2: Logaritmo Natural (ln)")
                print("3: Logaritmo Base 10 (log)")
                print("4: Seno (sin)")
                print("5: Cosseno (cos)")
                print("6: Tangente (tan)")
                print("7: Fatorial (!)")
                print("8: Exponencial (e^x)")
                op = input("Escolha a operação: ")
                num = float(input("Digite o número: "))
                
                if op == '1':
                    if num < 0:
                        print(f"Resultado (complexo): √{num} = {cmath.sqrt(num)}")
                    else:
                        print(f"Resultado: √{num} = {math.sqrt(num)}")
                elif op == '2':
                    if num <= 0:
                        print("Erro: Número deve ser positivo!")
                    else:
                        print(f"Resultado: ln({num}) = {math.log(num)}")
                elif op == '3':
                    if num <= 0:
                        print("Erro: Número deve ser positivo!")
                    else:
                        print(f"Resultado: log10({num}) = {math.log10(num)}")
                elif op == '4':
                    print(f"Resultado: sin({num}) = {math.sin(num)}")
                elif op == '5':
                    print(f"Resultado: cos({num}) = {math.cos(num)}")
                elif op == '6':
                    print(f"Resultado: tan({num}) = {math.tan(num)}")
                elif op == '7':
                    if num < 0 or not num.is_integer():
                        print("Erro: Número deve ser inteiro não negativo!")
                    else:
                        print(f"Resultado: {int(num)}! = {math.factorial(int(num))}")
                elif op == '8':
                    print(f"Resultado: e^{num} = {math.exp(num)}")
                else:
                    print("Operação inválida!")
                    
            elif categoria == '3':  # Operações com Matrizes
                print("\nOperações com Matrizes:")
                print("1: Soma de Matrizes")
                print("2: Subtração de Matrizes")
                print("3: Multiplicação de Matrizes")
                print("4: Multiplicação por Escalar")
                print("5: Transposta")
                print("6: Determinante")
                print("7: Inversa")
                print("8: Autovalores e Autovetores")
                op = input("Escolha a operação: ")
                
                if op in ['1', '2', '3']:  # Operações entre duas matrizes
                    print("\nMatriz A:")
                    linhas = int(input("Número de linhas: "))
                    colunas = int(input("Número de colunas: "))
                    A = np.zeros((linhas, colunas))
                    for i in range(linhas):
                        for j in range(colunas):
                            A[i][j] = float(input(f"Elemento A[{i+1}][{j+1}]: "))
                    
                    print("\nMatriz B:")
                    if op == '3':  # Multiplicação requer colunasA = linhasB
                        linhas_b = int(input("Número de linhas: "))
                        colunas_b = int(input("Número de colunas: "))
                    else:
                        linhas_b, colunas_b = linhas, colunas
                    B = np.zeros((linhas_b, colunas_b))
                    for i in range(linhas_b):
                        for j in range(colunas_b):
                            B[i][j] = float(input(f"Elemento B[{i+1}][{j+1}]: "))
                    
                    if op == '1':
                        if A.shape != B.shape:
                            print("Erro: Matrizes devem ter as mesmas dimensões!")
                        else:
                            print("\nA + B =")
                            print(A + B)
                    elif op == '2':
                        if A.shape != B.shape:
                            print("Erro: Matrizes devem ter as mesmas dimensões!")
                        else:
                            print("\nA - B =")
                            print(A - B)
                    elif op == '3':
                        if A.shape[1] != B.shape[0]:
                            print("Erro: Número de colunas de A deve ser igual ao número de linhas de B!")
                        else:
                            print("\nA × B =")
                            print(np.matmul(A, B))
                            
                elif op == '4':  # Multiplicação por escalar
                    print("\nMatriz A:")
                    linhas = int(input("Número de linhas: "))
                    colunas = int(input("Número de colunas: "))
                    A = np.zeros((linhas, colunas))
                    for i in range(linhas):
                        for j in range(colunas):
                            A[i][j] = float(input(f"Elemento A[{i+1}][{j+1}]: "))
                    escalar = float(input("Digite o escalar: "))
                    print("\nEscalar × A =")
                    print(escalar * A)
                    
                elif op in ['5', '6', '7', '8']:  # Operações com uma matriz
                    print("\nMatriz A:")
                    linhas = int(input("Número de linhas: "))
                    colunas = int(input("Número de colunas: "))
                    A = np.zeros((linhas, colunas))
                    for i in range(linhas):
                        for j in range(colunas):
                            A[i][j] = float(input(f"Elemento A[{i+1}][{j+1}]: "))
                    
                    if op == '5':
                        print("\nA^T =")
                        print(A.T)
                    elif op == '6':
                        if A.shape[0] != A.shape[1]:
                            print("Erro: Matriz deve ser quadrada!")
                        else:
                            det = np.linalg.det(A)
                            print(f"\ndet(A) = {det}")
                    elif op == '7':
                        if A.shape[0] != A.shape[1]:
                            print("Erro: Matriz deve ser quadrada!")
                        else:
                            try:
                                inv = np.linalg.inv(A)
                                print("\nA^-1 =")
                                print(inv)
                            except np.linalg.LinAlgError:
                                print("Erro: Matriz é singular (não invertível)!")
                    elif op == '8':
                        if A.shape[0] != A.shape[1]:
                            print("Erro: Matriz deve ser quadrada!")
                        else:
                            autovalores, autovetores = np.linalg.eig(A)
                            print("\nAutovalores:")
                            print(autovalores)
                            print("\nAutovetores (colunas):")
                            print(autovetores)
                    else:
                        print("Operação inválida!")
                        
            elif categoria == '4':  # Sistemas Lineares
                print("\nSistemas Lineares:")
                print("1: Resolver Sistema Ax = b")
                print("2: Verificar consistência")
                op = input("Escolha a operação: ")
                
                n = int(input("Número de variáveis/equações: "))
                
                # Matriz de coeficientes
                print("\nMatriz de coeficientes A:")
                A = np.zeros((n, n))
                for i in range(n):
                    for j in range(n):
                        A[i][j] = float(input(f"Coeficiente A[{i+1}][{j+1}]: "))
                
                # Vetor de termos independentes
                print("\nVetor de termos independentes b:")
                b = np.zeros(n)
                for i in range(n):
                    b[i] = float(input(f"Termo b[{i+1}]: "))
                
                if op == '1':
                    try:
                        x = np.linalg.solve(A, b)
                        print("\nSolução x:")
                        for i in range(n):
                            print(f"x[{i+1}] = {x[i]}")
                    except np.linalg.LinAlgError:
                        print("Erro: Sistema não tem solução única!")
                        
                elif op == '2':
                    # Verificar consistência
                    A_aug = np.column_stack((A, b))
                    rank_A = np.linalg.matrix_rank(A)
                    rank_Aaug = np.linalg.matrix_rank(A_aug)
                    
                    if rank_A == rank_Aaug:
                        if rank_A == n:
                            print("Sistema consistente com solução única!")
                        else:
                            print("Sistema consistente com infinitas soluções!")
                    else:
                        print("Sistema inconsistente (sem solução)!")
                else:
                    print("Operação inválida!")
                    
            elif categoria == '5':  # Números Complexos
                print("\nNúmeros Complexos:")
                print("1: Soma")
                print("2: Subtração")
                print("3: Multiplicação")
                print("4: Divisão")
                print("5: Módulo")
                print("6: Argumento (fase)")
                print("7: Conjugado")
                op = input("Escolha a operação: ")
                
                if op in ['1', '2', '3', '4']:
                    real1 = float(input("Parte real do primeiro número: "))
                    imag1 = float(input("Parte imaginária do primeiro número: "))
                    real2 = float(input("Parte real do segundo número: "))
                    imag2 = float(input("Parte imaginária do segundo número: "))
                    z1 = complex(real1, imag1)
                    z2 = complex(real2, imag2)
                    
                    if op == '1':
                        print(f"Resultado: {z1} + {z2} = {z1 + z2}")
                    elif op == '2':
                        print(f"Resultado: {z1} - {z2} = {z1 - z2}")
                    elif op == '3':
                        print(f"Resultado: {z1} * {z2} = {z1 * z2}")
                    elif op == '4':
                        if z2 == 0:
                            print("Erro: Divisão por zero!")
                        else:
                            print(f"Resultado: {z1} / {z2} = {z1 / z2}")
                elif op in ['5', '6', '7']:
                    real = float(input("Parte real do número: "))
                    imag = float(input("Parte imaginária do número: "))
                    z = complex(real, imag)
                    
                    if op == '5':
                        print(f"Módulo de {z} = {abs(z)}")
                    elif op == '6':
                        print(f"Argumento de {z} = {cmath.phase(z)} radianos")
                    elif op == '7':
                        print(f"Conjugado de {z} = {z.conjugate()}")
                else:
                    print("Operação inválida!")
                    
            else:
                print("Categoria inválida! Tente novamente.")
                
        except ValueError:
            print("Erro: Valor inválido inserido!")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

# Iniciar a calculadora
calculadora_avancada()