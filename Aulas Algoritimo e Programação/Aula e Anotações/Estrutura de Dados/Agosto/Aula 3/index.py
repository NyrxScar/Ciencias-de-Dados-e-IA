
class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        return None

    def esta_vazia(self):
        return len(self.itens) == 0

class VerificadorPalindromo:
    def __init__(self, texto):
        # Normaliza o texto: remove caracteres não alfanuméricos e transforma em minúsculas
        self.texto = ''.join(filter(str.isalnum, texto)).lower()
        self.pilha = Pilha()

    def eh_palindromo(self):
        # Coloca todos os caracteres na pilha
        for caractere in self.texto:
            self.pilha.empilhar(caractere)

        # Verifica cada caractere do texto com o topo da pilha
        for caractere in self.texto:
            if caractere != self.pilha.desempilhar():
                return False
        return True

# Exemplo de uso
texto = "A man a plan a canal Panama"
verificador = VerificadorPalindromo(texto)

if verificador.eh_palindromo():
    print(f'"{texto}" é um palíndromo.')
else:
    print(f'"{texto}" não é um palíndromo.')
