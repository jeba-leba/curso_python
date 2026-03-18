# Escreva um programa que solicite ao usuario frase.
# Para parar de solicitar frases ele pode apenas dar enter
# Seu programa deve apresentar cada frase e a quantidade
# de vezes que ela foi digitada de forma ordenada.

dados = {}

while True:
    frase = input("Digite uma frase: ")
    if frase == "":
        break

    if frase not in dados:
        dados[frase] = 1

    else:
        dados[frase] += 1

for a, b in sorted(dados.items(), key=lambda x: x[1], reverse=True):
    print(f"Frase: '{a}' - Quantidade: {b}")