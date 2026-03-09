# Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
# Apresente o valor a ser pago

preco_casquinha = 1
preco_cascao = 2.50
preco_cestinha = 4
preco_cobertura = 1.50

texto = """
Olá, gostaria de pedir um soverte? Temos 3 opções
(1) Casquinha R$ 1,00
(2) Cascão R$ 2,50
(3) Cestinha R$ 4,00
"""

texto2 = """
Temos 3 sabores de soverte
(1) Morango
(2) Creme
(3) Chocolate
"""

texto3 = """
Gostaria de acrescentar cobertura? Ficaria R$1,50 a mais
(1) Caramelo
(2) Morango
(3) Chocolate
(4) Sem Cobertura
"""

opcao = input(texto)

if opcao == "1":
    sorvete = "casquinha"
    print("Você escolheu",sorvete)
    
elif opcao == "2":
    sorvete = "cascao"
    print("Você escolheu",sorvete)

elif opcao == "3":
    sorvete = "cestinha"
    print("Você escolheu",sorvete)

else:
    print("Opção inválida")

sabor = input(texto2)

if sabor == "1":
    sabor = "morango"
    print("Você escolheu",sorvete,"de",sabor)

elif sabor == "2":
    sabor = "creme"
    print("Você escolheu",sorvete,"de",sabor)

elif sabor == "3":
    sabor = "chocolate"
    print("Você escolheu,",sorvete,"de",sabor)

else:
    print("Opção Inválida")

cobertura = input(texto3)

if cobertura == "1":
    cobertura = "caramelo"
    print("Você escolheu,",sorvete,"de",sabor,"com cobertura de",cobertura)
    

elif cobertura == "2":
    cobertura = "morango"
    print("Você escolheu,",sorvete,"de",sabor,"com cobertura de",cobertura)
    

elif cobertura == "3":
    cobertura = "chocolate"
    print("Você escolheu,",sorvete,"de",sabor,"com cobertura de",cobertura)
    

elif cobertura  == "4":
    cobertura = "sem cobertura"
    print("Você escolheu,",sorvete,"de",sabor,cobertura)
    
else:
    print("Opção Inválida")

if sorvete == "casquinha":
    sorvete = preco_casquinha

elif sorvete == "cascao":
    sorvete = preco_cascao

elif sorvete == "cestinha":
    sorvete = preco_cestinha

if cobertura == "sem cobertura":
    cobertura = 0

else:
    cobertura = preco_cobertura

print("Sua compra deu R$",sorvete + cobertura)