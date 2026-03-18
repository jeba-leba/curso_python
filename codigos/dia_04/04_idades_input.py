# Como adicionar novos elementos dentro de lista

idades = []

while True:
    idade = input ("Entre com a idade: ")

    if idade == "":
        break

    idades.append(int(idade))


media = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
qtde = len(idades)

print("Média das idades: ", media)
print("Menor idade: ", minimo)
print("Maior idade: ", maximo)
print("Quantidade: ", qtde)