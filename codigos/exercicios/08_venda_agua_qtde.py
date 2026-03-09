# Altere o exercício 07 para considerar a quantidade de garrafas de água

mineral = 1.50
gas = 2.50

texto = """
Bem vindo!, favor escolha qual água você gostaria de comprar
(1) Água mineral sem gás R$1.50
(2) Água mineral com gás R$2.50
"""

texto2 = """
Quantas você deseja?
"""

opcao = input(texto)

if opcao == "1":
    agua = mineral
    print("A unidade da agua mineral sem gás custa R$1,50")

else:
    agua = gas
    print("A unidade da água com gás custa R$2,50")

qtde = input(texto2)

print("O valor deu: R$", agua * float(qtde))