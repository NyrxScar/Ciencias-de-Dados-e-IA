import numpy as np
from fractions import Fraction
import re
import sympy as sp

class CalculadoraCompleta:
    def __init__(self):
        self.historico = []
    
    def adicionar_historico(self, operacao, resultado):
        """Adiciona operação ao histórico"""
        self.historico.append(f"{operacao} = {resultado}")
    
    def mostrar_historico(self):
        """Mostra o histórico de operações"""
        print("\n" + "="*50)
        print("HISTÓRICO DE OPERAÇÕES")
        print("="*50)
        for i, item in enumerate(self.historico, 1):
            print(f"{i}. {item}")
        print("="*50)
    
    # FUNÇÃO VERIFICAR SOLUÇÃO EM SISTEMA LINEAR (CORRIGIDA)
    def verificar_solucao_sistema(self):
        """Verifica se uma dada solução é válida para um sistema linear"""
        print("\n" + "="*50)
        print("VERIFICAÇÃO DE SOLUÇÃO EM SISTEMA LINEAR")
        print("="*50)
        print("Digite o sistema linear e a solução a ser verificada")
        print("Exemplo: Para verificar (2, -1, 1) no sistema:")
        print("2x + 3y - z = 0")
        print("x - 2y + z = 5") 
        print("-x + y + z = -2")
        print("="*50)
    
        try:
            # Obter número de equações
            n = int(input("Digite o número de equações do sistema: "))
            
            # Coletar as equações do sistema
            sistema = []
            print(f"\nDigite as {n} equações do sistema:")
            for i in range(n):
                eq = input(f"Equação {i+1}: ").strip()
                sistema.append(eq)
            
            # Obter a solução a ser verificada
            solucao_str = input("\nDigite a solução a ser verificada (ex: 2, -1, 1): ").strip()
            solucao = list(map(float, solucao_str.replace('(', '').replace(')', '').split(',')))
            
            # Extrair variáveis do sistema (assumindo x, y, z, w, v...)
            variaveis = []
            for eq in sistema:
                vars_eq = re.findall(r'[a-zA-Z]', eq)
                variaveis.extend(vars_eq)
            
            variaveis = sorted(list(set(variaveis)))
            
            if len(solucao) != len(variaveis):
                print(f" Erro: A solução tem {len(solucao)} valores, mas o sistema tem {len(variaveis)} variáveis!")
                return
            
            print(f"\n Verificando solução {tuple(solucao)} no sistema:")
            for eq in sistema:
                print(f"   {eq}")
            
            # Verificar cada equação do sistema
            todas_validas = True
            resultados = []
            
            for i, eq in enumerate(sistema):
                # CORREÇÃO DEFINITIVA: Substituir variáveis de forma segura
                eq_substituida = eq
                for j, var in enumerate(variaveis):
                    # Usar regex para substituir apenas a variável, não partes de palavras
                    eq_substituida = re.sub(r'\b' + var + r'\b', str(solucao[j]), eq_substituida)
                
                # CORREÇÃO DEFINITIVA: Remover TODOS os espaços
                eq_substituida = eq_substituida.replace(' ', '')
                
                # CORREÇÃO DEFINITIVA: Garantir formato válido para eval
                if '=' in eq_substituida:
                    partes = eq_substituida.split('=')
                    
                    # Garantir que ambos os lados sejam expressões válidas
                    lado_esquerdo = partes[0]
                    lado_direito = partes[1]
                    
                    # Adicionar parênteses para garantir ordem correta das operações
                    lado_esquerdo = f"({lado_esquerdo})"
                    lado_direito = f"({lado_direito})"
                    
                    # Calcular os resultados
                    try:
                        resultado_esquerdo = eval(lado_esquerdo)
                        resultado_direito = eval(lado_direito)
                    except Exception as e:
                        print(f" Erro na equação {i+1}: {e}")
                        return
                else:
                    # Se não há igualdade, assumir que o lado direito é 0
                    lado_esquerdo = f"({eq_substituida})"
                    resultado_esquerdo = eval(lado_esquerdo)
                    resultado_direito = 0
                
                # Verificar se a equação é satisfeita
                valida = abs(resultado_esquerdo - resultado_direito) < 1e-10
                
                resultados.append({
                    'equacao': eq,
                    'lado_esquerdo': resultado_esquerdo,
                    'lado_direito': resultado_direito,
                    'valida': valida
                })
                
                if not valida:
                    todas_validas = False
            
            # Mostrar resultados
            print(f"\n📊 RESULTADOS:")
            for i, resultado in enumerate(resultados):
                status = "✅" if resultado['valida'] else "❌"
                print(f"{status} Equação {i+1}: {resultado['equacao']}")
                print(f"   Substituição: {resultado['lado_esquerdo']} = {resultado['lado_direito']}")
                if not resultado['valida']:
                    print(f"   Diferença: {abs(resultado['lado_esquerdo'] - resultado['lado_direito']):.6f}")
            
            # Conclusão final
            print(f"\n CONCLUSÃO:")
            if todas_validas:
                print(f" A solução {tuple(solucao)} É VÁLIDA para o sistema!")
                self.adicionar_historico(f"Verificar solução {tuple(solucao)}", "É válida")
            else:
                print(f" A solução {tuple(solucao)} NÃO É VÁLIDA para o sistema!")
                self.adicionar_historico(f"Verificar solução {tuple(solucao)}", "Não é válida")
                    
        except ValueError:
            print(" Erro: Formato inválido! Use números separados por vírgula.")
        except Exception as e:
            print(f"❌ Erro ao verificar a solução: {e}")
    
    # OPERAÇÕES BÁSICAS
    def operacoes_basicas(self):
        """Realiza operações básicas"""
        print("\n" + "="*50)
        print("OPERACÕES BÁSICAS")
        print("="*50)
        print("1. Soma (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("5. Potência (^)")
        print("6. Raiz quadrada (√)")
        print("="*50)
        
        try:
            opcao = int(input("Escolha a operação (1-6): "))
            num1 = float(input("Digite o primeiro número: "))
            
            if opcao == 6:
                resultado = num1 ** 0.5
                operacao = f"√{num1}"
            else:
                num2 = float(input("Digite o segundo número: "))
                
                if opcao == 1:
                    resultado = num1 + num2
                    operacao = f"{num1} + {num2}"
                elif opcao == 2:
                    resultado = num1 - num2
                    operacao = f"{num1} - {num2}"
                elif opcao == 3:
                    resultado = num1 * num2
                    operacao = f"{num1} * {num2}"
                elif opcao == 4:
                    if num2 == 0:
                        raise ZeroDivisionError("Divisão por zero!")
                    resultado = num1 / num2
                    operacao = f"{num1} / {num2}"
                elif opcao == 5:
                    resultado = num1 ** num2
                    operacao = f"{num1} ^ {num2}"
                else:
                    print("Opção inválida!")
                    return
            
            print(f"Resultado: {resultado}")
            self.adicionar_historico(operacao, resultado)
            
        except ValueError:
            print("Erro: Digite números válidos!")
        except ZeroDivisionError as e:
            print(f"Erro: {e}")
    
    # OPERAÇÕES COM MATRIZES
    def criar_matriz(self, nome):
        """Cria uma matriz a partir da entrada do usuário"""
        try:
            linhas = int(input(f"Digite o número de linhas da matriz {nome}: "))
            colunas = int(input(f"Digite o número de colunas da matriz {nome}: "))
            
            print(f"Digite os elementos da matriz {nome} (linha por linha):")
            matriz = []
            
            for i in range(linhas):
                linha = list(map(float, input(f"Linha {i+1}: ").split()))
                if len(linha) != colunas:
                    raise ValueError("Número de elementos incorreto!")
                matriz.append(linha)
            
            return np.array(matriz)
        except ValueError as e:
            print(f"Erro: {e}")
            return None
    
    def operacoes_matrizes(self):
        """Realiza operações com matrizes"""
        print("\n" + "="*50)
        print("OPERACÕES COM MATRIZES")
        print("="*50)
        print("1. Soma de matrizes")
        print("2. Subtração de matrizes")
        print("3. Multiplicação de matrizes")
        print("4. Multiplicação por escalar")
        print("5. Transposta")
        print("6. Determinante")
        print("7. Matriz inversa")
        print("="*50)
        
        try:
            opcao = int(input("Escolha a operação (1-7): "))
            
            if opcao in [1, 2, 3]:
                print("\nMatriz A:")
                A = self.criar_matriz("A")
                if A is None: return
                
                print("\nMatriz B:")
                B = self.criar_matriz("B")
                if B is None: return
                
                if opcao == 1:
                    if A.shape != B.shape:
                        raise ValueError("Matrizes devem ter mesma dimensão para soma!")
                    resultado = A + B
                    operacao = "A + B"
                elif opcao == 2:
                    if A.shape != B.shape:
                        raise ValueError("Matrizes devem ter mesma dimensão para subtração!")
                    resultado = A - B
                    operacao = "A - B"
                elif opcao == 3:
                    if A.shape[1] != B.shape[0]:
                        raise ValueError("Número de colunas de A deve ser igual ao número de linhas de B!")
                    resultado = np.dot(A, B)
                    operacao = "A * B"
            
            elif opcao == 4:
                A = self.criar_matriz("A")
                if A is None: return
                escalar = float(input("Digite o escalar: "))
                resultado = escalar * A
                operacao = f"{escalar} * A"
            
            elif opcao == 5:
                A = self.criar_matriz("A")
                if A is None: return
                resultado = A.T
                operacao = "A^T"
            
            elif opcao == 6:
                A = self.criar_matriz("A")
                if A is None: return
                if A.shape[0] != A.shape[1]:
                    raise ValueError("Matriz deve be quadrada para cálculo do determinante!")
                resultado = np.linalg.det(A)
                operacao = "det(A)"
            
            elif opcao == 7:
                A = self.criar_matriz("A")
                if A is None: return
                if A.shape[0] != A.shape[1]:
                    raise ValueError("Matriz deve ser quadrada para inversão!")
                resultado = np.linalg.inv(A)
                operacao = "A⁻¹"
            
            else:
                print("Opção inválida!")
                return
            
            print(f"\nResultado:")
            print(resultado)
            self.adicionar_historico(operacao, "Ver resultado acima")
            
        except Exception as e:
            print(f"Erro: {e}")
    
    # VERIFICAÇÃO DE EQUAÇÃO LINEAR
    def verificar_equacao_linear(self):
        """Verifica se uma equação é linear"""
        print("\n" + "="*50)
        print("VERIFICAÇÃO DE EQUAÇÃO LINEAR")
        print("="*50)
        print("Digite a equação no formato: a1*x1 + a2*x2 + ... + an*xn = b")
        print("Exemplo: 2*x + 3*y - 4*z = 5")
        print("="*50)
        
        equacao = input("Digite a equação: ").strip()
        
        # Remover espaços para facilitar a análise
        equacao_sem_espacos = equacao.replace(" ", "")
        
        # Verificar se há divisão por variável (indicador de não-linearidade)
        if re.search(r'/[a-zA-Z]', equacao_sem_espacos) or re.search(r'[a-zA-Z]/', equacao_sem_espacos):
            print(" NÃO É UMA EQUAÇÃO LINEAR (variável no denominador)")
            self.adicionar_historico(f"Verificar: {equacao}", "Não é linear - variável no denominador")
            return
        
        # Verificar multiplicação entre variáveis (com * explícito)
        if re.search(r'[a-zA-Z]\*[a-zA-Z]', equacao_sem_espacos):
            print(" NÃO É UMA EQUAÇÃO LINEAR (multiplicação entre variáveis)")
            self.adicionar_historico(f"Verificar: {equacao}", "Não é linear - multiplicação entre variáveis")
            return
        
        # Verificar variáveis juntas sem operador (como xy, yz, etc.)
        if re.search(r'[a-zA-Z]{2,}', equacao_sem_espacos):
            # Verificar se não é uma palavra reservada ou função
            palavras_reservadas = ['sin', 'cos', 'tan', 'log', 'exp', 'sqrt', 'ln']
            padrao_variaveis_juntas = re.findall(r'[a-zA-Z]{2,}', equacao_sem_espacos)
            
            for padrao in padrao_variaveis_juntas:
                if padrao not in palavras_reservadas:
                    print(" NÃO É UMA EQUAÇÃO LINEAR (multiplicação implícita entre variáveis)")
                    self.adicionar_historico(f"Verificar: {equacao}", "Não é linear - multiplicação implícita entre variáveis")
                    return
        
        # Verificar potências diferentes de 1 (incluindo frações)
        padrao_potencia = re.compile(r'[a-zA-Z](\*\*|\^)[ ]*([0-9]+([.,][0-9]+)?|\([0-9]+/[0-9]+\))')
        if padrao_potencia.search(equacao):
            # Verificar se é uma raiz quadrada (potência 1/2)
            if re.search(r'[a-zA-Z](\*\*|\^)[ ]*\(?1/2\)?', equacao):
                print(" NÃO É UMA EQUAÇÃO LINEAR (variável com raiz quadrada)")
                self.adicionar_historico(f"Verificar: {equacao}", "Não é linear - raiz quadrada")
            else:
                print(" NÃO É UMA EQUAÇÃO LINEAR (variável com potência diferente de 1)")
                self.adicionar_historico(f"Verificar: {equacao}", "Não é linear - potência diferente de 1")
            return
        
        # Verificar funções não lineares
        funcoes_nao_lineares = ['sin', 'cos', 'tan', 'log', 'exp', 'sqrt', 'ln', '√']
        for funcao in funcoes_nao_lineares:
            if funcao in equacao.lower():
                print(f" NÃO É UMA EQUAÇÃO LINEAR (contém função {funcao})")
                self.adicionar_historico(f"Verificar: {equacao}", f"Não é linear - função {funcao}")
                return
        
        # Verificar se há variáveis dentro de parênteses com operações
        if re.search(r'[a-zA-Z]\^\([^)]+\)', equacao):
            print(" NÃO É UMA EQUAÇÃO LINEAR (variável com operação não linear)")
            self.adicionar_historico(f"Verificar: {equacao}", "Não é linear - operação não linear na variável")
            return
        
        # Verificar se há raiz quadrada representada como potência 1/2
        if re.search(r'[a-zA-Z]\^\(?1/2\)?', equacao):
            print(" NÃO É UMA EQUAÇÃO LINEAR (variável com raiz quadrada)")
            self.adicionar_historico(f"Verificar: {equacao}", "Não é linear - raiz quadrada")
            return
        
        # Se passou por todas as verificações, é linear
        print(" É UMA EQUAÇÃO LINEAR")
        self.adicionar_historico(f"Verificar: {equacao}", "É linear")
    
    # RESOLVER EQUAÇÃO LINEAR INDIVIDUAL
    def resolver_equacao_linear(self):
        """Resolve uma equação linear individual"""
        print("\n" + "="*50)
        print("RESOLUÇÃO DE EQUAÇÃO LINEAR")
        print("="*50)
        print("Digite a equação linear no formato: a1*x1 + a2*x2 + ... + an*xn = b")
        print("Exemplo: 2*x + 3*y = 5")
        print("Exemplo: 4*x - 2*y + z = 10")
        print("="*50)
        
        try:
            equacao = input("Digite a equação: ").strip()
            
            # Verificar se a equação é linear primeiro
            equacao_sem_espacos = equacao.replace(" ", "")
            if (re.search(r'/[a-zA-Z]', equacao_sem_espacos) or 
                re.search(r'[a-zA-Z]/', equacao_sem_espacos) or
                re.search(r'[a-zA-Z]\*[a-zA-Z]', equacao_sem_espacos) or
                re.search(r'[a-zA-Z]{2,}', equacao_sem_espacos) or
                re.search(r'[a-zA-Z](\*\*|\^)', equacao)):
                
                print(" Esta não é uma equação linear! Use apenas operações lineares.")
                return
            
            # Extrair variáveis da equação
            variaveis = sorted(list(set(re.findall(r'[a-zA-Z]', equacao))))
            
            if not variaveis:
                print(" Nenhuma variável encontrada na equação!")
                return
            
            # Criar símbolos para as variáveis
            simbolos = sp.symbols(' '.join(variaveis))
            
            # Resolver a equação
            solucao = sp.solve(equacao, simbolos)
            
            if not solucao:
                print(" A equação não tem solução or é uma identidade!")
                return
            
            print(f"\n Equação: {equacao}")
            print(" SOLUÇÃO:")
            
            # Mostrar a solução de forma organizada
            if len(variaveis) == 1:
                # Equação com uma variável
                var = variaveis[0]
                print(f"{var} = {solucao[0]}")
            else:
                # Equação com múltiplas variáveis
                for var in variaveis:
                    if var in solucao:
                        print(f"{var} = {solucao[var]}")
                    else:
                        print(f"{var} = {var} (variável livre)")
            
            self.adicionar_historico(f"Resolver: {equacao}", f"Solução: {solucao}")
            
        except Exception as e:
            print(f" Erro ao resolver a equação: {e}")
    
    # RESOLUÇÃO DE SISTEMAS LINEARES
    def resolver_sistema_linear(self):
        """Resolve sistemas lineares"""
        print("\n" + "="*50)
        print("RESOLUÇÃO DE SISTEMAS LINEARES")
        print("="*50)
        print("Digite o sistema no formato:")
        print("a11*x1 + a12*x2 + ... + a1n*xn = b1")
        print("a21*x1 + a22*x2 + ... + a2n*xn = b2")
        print("...")
        print("="*50)
        
        try:
            n = int(input("Digite o número de equações: "))
            
            # Coletar matriz dos coeficientes e vetor dos termos independentes
            A = []
            B = []
            
            print("\nDigite cada equação (coeficientes separados por espaço):")
            for i in range(n):
                eq = input(f"Equação {i+1}: ").strip()
                
                # Separar coeficientes e termo independente
                if '=' in eq:
                    partes = eq.split('=')
                    coeficientes = list(map(float, partes[0].split()))
                    termo_independente = float(partes[1])
                else:
                    coeficientes = list(map(float, eq.split()))
                    termo_independente = 0
                
                A.append(coeficientes)
                B.append(termo_independente)
            
            A = np.array(A)
            B = np.array(B)
            
            print(f"\nMatriz dos coeficientes (A):")
            print(A)
            print(f"\nVetor dos termos independentes (B):")
            print(B)
            
            # Verificar se o sistema tem solução única
            if np.linalg.det(A) == 0:
                print("  O sistema pode não ter solução única (det(A) = 0)")
                # Tentar resolver com mínimos quadrados
                solucao = np.linalg.lstsq(A, B, rcond=None)[0]
                print("Solução por mínimos quadrados:")
            else:
                solucao = np.linalg.solve(A, B)
                print("Solução única:")
            
            # Mostrar solução com variáveis
            variaveis = ['x', 'y', 'z', 'w', 'v'][:len(solucao)]
            for i, (var, valor) in enumerate(zip(variaveis, solucao)):
                print(f"{var}{i+1} = {valor:.4f}")
            
            self.adicionar_historico(f"Resolver sistema {n}x{n}", f"Solução: {solucao}")
            
        except Exception as e:
            print(f"Erro ao resolver o sistema: {e}")
    
    # RESOLVER EXPRESSÃO ARITMÉTICA
    def resolver_expressao_aritmetica(self):
        """Resolve expressões aritméticas"""
        print("\n" + "="*50)
        print("RESOLUÇÃO DE EXPRESSÃO ARITMÉTICA")
        print("="*50)
        print("Digite a expressão aritmética:")
        print("Exemplo: 5*1+3*(-1)+2*(9/2)")
        print("Exemplo: (2+3)*4 - 10/2")
        print("Exemplo: 2**3 + 4*5")
        print("="*50)
        
        try:
            expressao = input("Digite a expressão: ").strip()
            
            # Substituir ^ por ** para compatibilidade
            expressao = expressao.replace('^', '**')
            
            # Avaliar a expressão com segurança
            resultado = eval(expressao)
            
            print(f"\n🔍 Expressão: {expressao}")
            print(f" Resultado: {resultado}")
            
            self.adicionar_historico(f"Calcular: {expressao}", resultado)
            
        except ZeroDivisionError:
            print(" Erro: Divisão por zero!")
        except SyntaxError:
            print(" Erro: Expressão inválida!")
        except NameError:
            print(" Erro: Use apenas números e operadores!")
        except Exception as e:
            print(f" Erro ao calcular: {e}")
    
    # RESOLVER EQUAÇÃO ALGÉBRICA GERAL
    def resolver_equacao_geral(self):
        """Resolve equações algébricas gerais (lineares e não-lineares)"""
        print("\n" + "="*50)
        print("RESOLUÇÃO DE EQUAÇÃO ALGÉBRICA GERAL")
        print("="*50)
        print("Digite a equação:")
        print("Exemplo: m - (m + 1) + m + 2 = 7")
        print("Exemplo: x^2 - 5*x + 6 = 0")
        print("Exemplo: 2*y + 5 = 3*y - 1")
        print("="*50)
        
        try:
            equacao = input("Digite a equação: ").strip()
            
            # Verificar se tem sinal de igual
            if '=' not in equacao:
                print(" Erro: A equação deve conter o sinal de igual (=)")
                return
            
            # Substituir ^ por ** para compatibilidade
            equacao = equacao.replace('^', '**')
            
            # Separar os lados da equação
            partes = equacao.split('=')
            if len(partes) != 2:
                print(" Erro: A equação deve ter exatamente um sinal de igual")
                return
            
            lado_esquerdo = partes[0].strip()
            lado_direito = partes[1].strip()
            
            # Extrair variáveis da equação
            variaveis = sorted(list(set(re.findall(r'[a-zA-Z]', equacao))))
            
            if not variaveis:
                print(" Nenhuma variável encontrada na equação!")
                return
            
            # Criar símbolos para as variáveis
            simbolos = sp.symbols(' '.join(variaveis))
            
            # Converter para expressões sympy
            expr_esquerda = sp.sympify(lado_esquerdo)
            expr_direita = sp.sympify(lado_direito)
            
            # Criar a equação: lado_esquerdo - lado_direito = 0
            equacao_sympy = sp.Eq(expr_esquerda, expr_direita)
            
            # Resolver a equação
            solucao = sp.solve(equacao_sympy, simbolos)
            
            print(f"\n Equação: {equacao}")
            
            if not solucao:
                print(" A equação não tem solução real!")
                self.adicionar_historico(f"Resolver geral: {equacao}", "Sem solução real")
                return
            
            print(" SOLUÇÃO:")
            
            # Mostrar soluções de forma organizada
            if len(solucao) == 1:
                if len(variaveis) == 1:
                    print(f"{variaveis[0]} = {solucao[0]}")
                else:
                    for i, sol in enumerate(solucao):
                        print(f"Solução {i+1}: {sol}")
            else:
                for i, sol in enumerate(solucao):
                    print(f"Solução {i+1}: {sol}")
            
            # Mostrar passo a passo para equações lineares simples
            if len(variaveis) == 1:
                var = variaveis[0]
                print(f"\n Passo a passo:")
                
                # Simplificar a equação: lado_esquerdo - lado_direito = 0
                expr_simplificada = sp.simplify(expr_esquerda - expr_direita)
                print(f"   {expr_esquerda} - ({expr_direita}) = 0")
                print(f"   {expr_simplificada} = 0")
                
                # Se for uma expressão linear, mostrar os passos
                if expr_simplificada.is_Add:
                    termos = expr_simplificada.as_ordered_terms()
                    var_term = None
                    const_term = 0
                    
                    for termo in termos:
                        if termo.has(simbolos[0]):
                            var_term = termo
                        else:
                            const_term -= termo
                    
                    if var_term:
                        coeficiente = var_term.as_coefficient(simbolos[0])
                        if coeficiente != 1:
                            print(f"   {var_term} = {-const_term}")
                            print(f"   {simbolos[0]} = {-const_term}/{coeficiente}")
                            print(f"   {simbolos[0]} = {-const_term/coeficiente}")
                        else:
                            print(f"   {simbolos[0]} = {-const_term}")
            
            self.adicionar_historico(f"Resolver geral: {equacao}", f"Solução: {solucao}")
            
        except sp.SympifyError:
            print(" Erro: Expressão inválida! Verifique a sintaxe.")
        except Exception as e:
            print(f" Erro ao resolver a equação: {e}")
    
    # MENU PRINCIPAL (ATUALIZADO)
    def menu_principal(self):
        """Menu principal da calculadora"""
        while True:
            print("\n" + "="*50)
            print("CALCULADORA COMPLETA")
            print("="*50)
            print("1. Operações Básicas")
            print("2. Expressões Aritméticas")
            print("3. Operações com Matrizes")
            print("4. Verificar Equação Linear")
            print("5. Resolver Equação Linear")
            print("6. Resolver Equação Geral")
            print("7. Resolver Sistema Linear")
            print("8. Verificar Solução em Sistema")
            print("9. Mostrar Histórico")
            print("10. Sair")
            print("="*50)
            
            try:
                opcao = int(input("Escolha uma opção (1-10): "))
                
                if opcao == 1:
                    self.operacoes_basicas()
                elif opcao == 2:
                    self.resolver_expressao_aritmetica()
                elif opcao == 3:
                    self.operacoes_matrizes()
                elif opcao == 4:
                    self.verificar_equacao_linear()
                elif opcao == 5:
                    self.resolver_equacao_linear()
                elif opcao == 6:
                    self.resolver_equacao_geral()
                elif opcao == 7:
                    self.resolver_sistema_linear()
                elif opcao == 8:
                    self.verificar_solucao_sistema()
                elif opcao == 9:
                    self.mostrar_historico()
                elif opcao == 10:
                    print("Obrigado por usar a calculadora!")
                    break
                else:
                    print("Opção inválida!")
            
            except ValueError:
                print("Erro: Digite um número válido!")
            except KeyboardInterrupt:
                print("\nPrograma interrompido pelo usuário.")
                break
            
# CLASSIFICAÇÃO DE UM SISTEMА
# 1. Possível Determinado: quando admite uma
# única solução. D ≠ 0 e R* pertence aos reais não nulos e Dx, Dy e Dz são R
# 2. Possível Indeterminado: quando admite mais de uma solução. D=0 e Dx, Dy e Dz são igual a zero
# 3. Impossível: quando não admite nenhuma solução. D=0 e Dx, Dy e Dz são R*(reais não nulos)

# Executar a calculadora
if __name__ == "__main__":
    calculadora = CalculadoraCompleta()
    calculadora.menu_principal()