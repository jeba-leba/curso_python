# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50

texto = """
Escolha a sua água para comprar
(1) Água mineral natural
(2) Água mineral com gás
"""

opcao = input(texto)

if opcao == "1":
    print("Sua conta deu R$1,50")

else:
    print("Sua conta deu R$2,50")