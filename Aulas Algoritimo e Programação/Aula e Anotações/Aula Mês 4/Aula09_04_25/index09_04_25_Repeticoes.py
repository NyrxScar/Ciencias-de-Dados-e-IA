# numero = int(input("Tabuada de: "))
# multiplicador = 1
# while(multiplicador<=10):
#     print(multiplicador*numero)
#     multiplicador = multiplicador + 1

################################################

# hora = 1
# while hora <= 12:
#     minuto = 1
#     while minuto <= 59:
#         print(f"Agora são {hora}:{minuto} minutos")
#         minuto = minuto + 1

#     print("=================")
#     hora = hora+1


#############################################


# while True:
#     receita = float(input("Digite sua Receita: "))
#     custo = float(input("Digite sua Custo: "))
#     calculo_roi = ((receita - custo)/custo)*100
#     print("Calculando seu investimento de novo")
#     print(f"Seu Retorno de Investimento(ROI) é : {calculo_roi}")
#     falso = str(input("Se quiser parar digite '0' e aperte 'enter' para continuar: "))
#     if falso == "0":
#         break
#     # else: ---- desnecessário
#     #     receita = float(input("Digite sua Receita: "))
#     #     custo = float(input("Digite sua Custo: "))
#     #     calculo_roi = ((receita - custo)/custo)*100
#     #     print(f"Seu Retorno de Investimento(ROI) é : {calculo_roi}")

#############################################

receita = float(input("Digite sua Receita: "))
custo = float(input("Digite sua Custo: "))
calculo_roi = ((receita - custo)/custo)*100
calculo_roi_soma = calculo_roi
while True:
    print(f"Seu Retorno de Investimento(ROI) é : {calculo_roi}")
    falso = str(input("Se quiser parar digite '0' e aperte 'enter' para continuar: "))
    if falso == "0":
        break
    else:
        print(f"O Resultado das somas dos ROI é: {calculo_roi_soma + calculo_roi}")
        print("Recomeçando o cálculo")
            

        


