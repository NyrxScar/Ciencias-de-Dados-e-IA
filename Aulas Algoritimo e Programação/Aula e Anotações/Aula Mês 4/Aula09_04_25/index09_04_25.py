# 1 a) - IMC, exercício

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
risco = ""
imc = peso/altura**2

if imc < 18.5 :
    risco = "baixo"
else: 
    if imc >= 40:
       risco = "Muito Grave"
    else:
       if (imc>=18.5) and (imc<=24.9):
          risco = "Médio"
       else:
          if (imc>=25) and (imc<=29.9):
             risco = "Aumentado"
          else:
              if (imc>=30) and (imc<=34.9):
                 risco = "Moderado"
              else:
                 if (imc>=35) and (imc<=39.9):
                    risco = "Grave"

print(f"Seu Índice de Massa Corporal(IMC) é : {imc:.1f}, portanto você tem um potencial {risco} de comorbidade ")

# 1 b) - IMC, exercício

print("Digite '1' para sexo biológicamente 'Masculino' e '2' para 'Feminino")
escolha_sexo = str(input("Digite o número correspondente ao seu sexo biológico: "))
risco1 = ""


if escolha_sexo == "1":
    print("Seu sexo biológico é Masculino")
else:
    if escolha_sexo == "2":
        print("Seu sexo biológico é Feminino")
    else:
        print("Desculpe, não temos dados para pessoas intersexo ou outras opções")

print("Meça a circuferência do seu abdômen! ")

circuferencia_abdomen = float(input("Digite sua circufência em centimetros: "))

if (circuferencia_abdomen >= 94) and (circuferencia_abdomen < 102) and ("1"):
    risco1 = "Aumentado"
else:
    if (circuferencia_abdomen >= 102) and ("1"):
         risco1 = "Substancialmente Aumentado"
    else:
        if (circuferencia_abdomen >= 80) and (circuferencia_abdomen < 88) and ("2"):
            risco1 = "Aumentado"
        else:
            if (circuferencia_abdomen >= 88) and ("2"):
                risco1 = "Substancialmente Aumentado"
            else:
                if (circuferencia_abdomen < 94):
                    risco1 = "atualmente nulo"
    
print(f"Seu IMC de acordo com o seu sexo tem potencial {risco1} de comorbidade")

