# Escreva um programa com uma lista de números
# e conte quantas vezes um número específico
# aparece na lista. Solicite ao usuário um número e exiba 
# a contagem.

lista = [1,2,3,4,5,6,7,3,9,10,1,2,3,5,7,3,6,4,5,2,3,4,3,4,5,6,7,8,9,10]

numero = input("Entre com um número: ")
numero = int(numero)

contador = 0
for i in lista:
    if i == numero:
        contador += 1

print("Quantidade de", numero, ":", contador)