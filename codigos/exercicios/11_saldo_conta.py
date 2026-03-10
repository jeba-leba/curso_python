# Faça um programa que receba uma quantidade indefinida
#  de valores correspondentes a “saldo em conta”, mas
#  quando o usuário apertar “enter” sem digitar valor
#  algum, o programa para de receber valores, e exibe a
#  soma de todos os valores digitados anteriormente.

soma = 0
vidas = 1

while vidas > 0:
    saldo_conta = input("Quantos reais você quer depositar? ")
    
    if saldo_conta == "":
        break
    else:
        vidas = 1
    soma += float(saldo_conta)

print("Seu saldo em conta é de: ", soma)

