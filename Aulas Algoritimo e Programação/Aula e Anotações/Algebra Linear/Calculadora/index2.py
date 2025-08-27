import tkinter as tk
from tkinter import messagebox, simpledialog
import math
import numpy as np

# --- Funções auxiliares para cálculos ---
def calcular():
    try:
        expressao = entrada.get()
        resultado = eval(expressao, {"__builtins__": None}, math.__dict__)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        messagebox.showerror("Erro", f"Expressão inválida!\n{e}")

def adicionar_valor(valor):
    entrada.insert(tk.END, valor)

def limpar():
    entrada.delete(0, tk.END)

def calcular_determinante():
    try:
        ordem = simpledialog.askinteger("Matriz", "Digite a ordem da matriz (ex: 2 para 2x2):")
        matriz = []
        for i in range(ordem):
            linha = simpledialog.askstring("Linha", f"Digite os elementos da linha {i+1} separados por espaço:")
            matriz.append(list(map(float, linha.split())))
        matriz_np = np.array(matriz)
        det = round(np.linalg.det(matriz_np), 4)
        messagebox.showinfo("Determinante", f"O determinante da matriz é: {det}")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao calcular determinante!\n{e}")

def resolver_sistema():
    try:
        n = simpledialog.askinteger("Sistema Linear", "Digite o número de incógnitas:")
        matriz = []
        vetor = []

        for i in range(n):
            linha = simpledialog.askstring("Coeficientes", f"Digite os coeficientes da equação {i+1} separados por espaço:")
            matriz.append(list(map(float, linha.split())))

        for i in range(n):
            termo = simpledialog.askfloat("Termos independentes", f"Digite o termo independente da equação {i+1}:")
            vetor.append(termo)

        matriz_np = np.array(matriz)
        vetor_np = np.array(vetor)
        solucao = np.linalg.solve(matriz_np, vetor_np)
        messagebox.showinfo("Solução", f"Solução do sistema:\n{solucao}")
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível resolver!\n{e}")

# --- Interface Tkinter ---
janela = tk.Tk()
janela.title("Calculadora Completa")
janela.geometry("500x600")

entrada = tk.Entry(janela, width=25, font=("Arial", 18))
entrada.grid(row=0, column=0, columnspan=4, pady=10)

# Botões principais
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (texto, linha, coluna) in botoes:
    if texto == '=':
        tk.Button(janela, text=texto, width=10, height=2, command=calcular).grid(row=linha, column=coluna)
    else:
        tk.Button(janela, text=texto, width=10, height=2, command=lambda t=texto: adicionar_valor(t)).grid(row=linha, column=coluna)

# Linha extra para funções científicas
funcoes = ['sin', 'cos', 'tan', 'sqrt', 'log', '^']
for i, f in enumerate(funcoes):
    tk.Button(janela, text=f, width=10, height=2, command=lambda t=f+"(": adicionar_valor(t)).grid(row=5+i//3, column=i%3)

# Botões extras
tk.Button(janela, text="C", width=10, height=2, command=limpar).grid(row=7, column=0)
tk.Button(janela, text="Determinante", width=15, height=2, command=calcular_determinante).grid(row=7, column=1, columnspan=2)
tk.Button(janela, text="Sistema Linear", width=15, height=2, command=resolver_sistema).grid(row=7, column=3)

janela.mainloop()
