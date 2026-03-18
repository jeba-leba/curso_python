# Escreva um programa que crie um dicionário com nomes de
# frutas como chaves e seus preços como valores.
# Solicite ao usuário que insira o nome de uma fruta
# e exiba o preço correspondente.

frutas = {"Maça": 1.50,
          "Banana": 2.75,
          "Uva": 1.90,
          "Pera": 1.25,
          "Laranja": 0.65,
          "Limão": 1.25,
          "Goiaba": 2.15,
          "Abacaxi": 3.20,
          "Jaca": 5.80
          }

fruta_usuario = input("Digite o nome de uma fruta: ")

if fruta_usuario in frutas:
    print(f"O preço da {fruta_usuario} é R${frutas[fruta_usuario]:.2f}")
else:
    print(f"Fruta não encontrada no dicionário.")
    