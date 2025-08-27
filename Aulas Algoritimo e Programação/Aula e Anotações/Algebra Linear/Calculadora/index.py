#!/usr/bin/env python3
"""Calculadora de Álgebra Linear (Português)
Salva em: matriz_calculadora.py

Funcionalidades:
- Resolver sistemas lineares por Regra de Cramer (quando aplicável) e por eliminação (Gauss).
- Calcular determinante, inversa, posto (rank), autovalores/autovetores (se numpy disponível).
- Operações com matrizes: soma, subtração, multiplicação, transposta.
- Construção fácil de matrizes a partir de texto (ex: '1 2; 3 4' -> [[1,2],[3,4]]).
- Modo interativo por menu e funções reutilizáveis para integrar em notebooks/avalições.

Observação: requer numpy. Para precisão racional, use entradas inteiras; o resultado é em float por numpy.linalg.
"""

import sys
from fractions import Fraction
import numpy as np
from copy import deepcopy

def parse_matrix(text):
    """Converte uma string como '1 2; 3 4' em numpy.array([[1,2],[3,4]])"""
    try:
        rows = [row.strip() for row in text.strip().split(';') if row.strip()!='']
        mat = [[Fraction(x) for x in row.split()] for row in rows]
        # converter para float numpy array
        return np.array([[float(x) for x in r] for r in mat], dtype=float)
    except Exception as e:
        raise ValueError(f"Erro ao parsear a matriz: {e}")

def parse_vector(text):
    """Converte uma string como '1 2 3' ou '1;2;3' em numpy array coluna"""
    text = text.strip()
    if ';' in text:
        parts = [p.strip() for p in text.split(';') if p.strip()!='']
    else:
        parts = [p for p in text.split() if p!='']
    try:
        vec = [Fraction(x) for x in parts]
        return np.array([float(x) for x in vec], dtype=float)
    except Exception as e:
        raise ValueError(f"Erro ao parsear o vetor: {e}")

def det(A):
    A = np.array(A, dtype=float)
    if A.shape[0] != A.shape[1]:
        raise ValueError("Determinante só definido para matrizes quadradas.")
    return float(np.linalg.det(A))

def inverse(A):
    A = np.array(A, dtype=float)
    if A.shape[0] != A.shape[1]:
        raise ValueError("Inversa só definida para matrizes quadradas.")
    return np.linalg.inv(A)

def rank(A):
    return int(np.linalg.matrix_rank(A))

def solve_cramer(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n, m = A.shape
    if n != m:
        raise ValueError("Regra de Cramer só vale para matrizes quadradas.")
    if b.size != n:
        raise ValueError("Vetor de termos independentes com dimensão incorreta.")
    D = det(A)
    if abs(D) < 1e-12:
        raise ValueError("Determinante zero (ou quase), Regra de Cramer não aplicável.")
    x = np.zeros(n, dtype=float)
    for i in range(n):
        Ai = A.copy()
        Ai[:, i] = b
        x[i] = det(Ai) / D
    return x

def solve_gauss(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    # usa numpy.linalg.solve quando possível (matriz quadrada e não singular)
    try:
        if A.shape[0] == A.shape[1]:
            return np.linalg.solve(A, b)
    except Exception:
        pass
    # Caso retangular ou singular -> usar lstsq para solução mínima (mínimos quadrados)
    sol, residuals, rankA, s = np.linalg.lstsq(A, b, rcond=None)
    return sol

def pretty_print_vector(v):
    return '[ ' + ', '.join(f"{float(x):.6g}" for x in v) + ' ]'

def menu():
    print("\n=== Calculadora de Álgebra Linear ===\n")
    while True:
        print("Escolha uma opção:")
        print("1) Resolver sistema linear (Cramer)" )
        print("2) Resolver sistema linear (Gauss / numpy.linalg.solve)" )
        print("3) Determinante" )
        print("4) Inversa" )
        print("5) Posto (rank)" )
        print("6) Operações: soma/sub/mult/transposta" )
        print("7) Construir matriz a partir de texto" )
        print("0) Sair" )
        opt = input("Opção: ").strip()
        if opt == '0':
            print('Tchau!')
            break
        try:
            if opt == '1' or opt == '2':
                A_text = input("Digite a matriz A (ex: '1 2; 3 4' para 2x2): ") 
                b_text = input("Digite o vetor b (ex: '5 6' ou '5;6'): ")
                A = parse_matrix(A_text)
                b = parse_vector(b_text)
                if opt == '1':
                    try:
                        x = solve_cramer(A,b)
                        print("Solução (Cramer):", pretty_print_vector(x))
                    except Exception as e:
                        print("Cramer falhou:", e)
                        print("Tentando Gauss: ")
                        x = solve_gauss(A,b)
                        print("Solução (Gauss / lstsq):", pretty_print_vector(x))
                else:
                    x = solve_gauss(A,b)
                    print("Solução (Gauss / numpy):", pretty_print_vector(x))
            elif opt == '3':
                A_text = input("Digite a matriz quadrada A: ")
                A = parse_matrix(A_text)
                print("Determinante:", det(A))
            elif opt == '4':
                A_text = input("Digite a matriz quadrada A: ")
                A = parse_matrix(A_text)
                print("Inversa:") 
                print(inverse(A))
            elif opt == '5':
                A_text = input("Digite a matriz A: ")
                A = parse_matrix(A_text)
                print("Posto (rank):", rank(A))
            elif opt == '6':
                op = input("Operação (+, -, *, T para transposta): ").strip()
                if op.upper() == 'T':
                    A_text = input("Digite a matriz A: ")
                    A = parse_matrix(A_text)
                    print("Transposta:") 
                    print(A.T)
                else:
                    A_text = input("Digite a matriz A: ")
                    B_text = input("Digite a matriz B: ")
                    A = parse_matrix(A_text)
                    B = parse_matrix(B_text)
                    if op == '+':
                        print(A + B)
                    elif op == '-':
                        print(A - B)
                    elif op == '*':
                        print("Produto A @ B:") 
                        print(A.dot(B))
                    else:
                        print("Operação desconhecida.")
            elif opt == '7':
                txt = input("Digite a descrição da matriz: ")
                M = parse_matrix(txt)
                print("Matriz resultante:") 
                print(M)
            else:
                print("Opção inválida.")
        except Exception as e:
            print("Erro:", e)


if __name__ == '__main__':
    menu()
