from fractions import Fraction

def converter(expressao: str) -> str:
    """
    Converte entre fração e número misto:
    - Se for fração (ex: "17/5"), vira número misto.
    - Se for misto (ex: "3 2/5"), vira fração imprópria.
    """
    expressao = expressao.strip()

    # Caso seja número misto: "3 2/5"
    if " " in expressao:
        parte_inteira, fracao = expressao.split()
        inteiro = int(parte_inteira)
        numerador, denominador = map(int, fracao.split("/"))
        numerador_total = inteiro * denominador + numerador
        return str(Fraction(numerador_total, denominador))

    # Caso seja fração simples: "17/5"
    elif "/" in expressao:
        fracao = Fraction(expressao)
        inteiro = fracao.numerator // fracao.denominator
        resto = fracao.numerator % fracao.denominator
        if resto == 0:
            return str(inteiro)
        elif inteiro == 0:
            return f"{resto}/{fracao.denominator}"
        else:
            return f"{inteiro} {resto}/{fracao.denominator}"

    else:
        return "Entrada inválida! Use 'a/b' ou 'x y/z'."

# Exemplos de uso
print(converter("11/5"))   # -> "3 2/5"
print(converter("3 2/5"))  # -> "17/5"
print(converter("7/3"))    # -> "2 1/3"
print(converter("2 1/3"))  # -> "7/3"
