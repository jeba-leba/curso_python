# Construa um programa que realiza o sorteio de um numero entre 1 e 15. O usuario terá 3 chances de acertar o valor sorteado. A cada tentativa, você deve informar
# se o chute é maior ou menor do que o numero sorteado. Caso o usuario acerte, de os parabéns.

import random


def get_input():
    while True:
        try:
            numero_usuario = int(input("Entre com um numero: "))
        
        except ValueError as err:
            print(f"Valor invalido, entre com um numero inteiro")
            continue
        
        if 1 < numero_usuario <= 15:
            return numero_usuario

        print(f"Valor invalido, entre com um numero entre 1 e 15")

def check_numbers(sorteio, usuario):
    if sorteio == usuario:
        print(f"Parabéns, você acertou o número sorteado!")
        return True

    elif usuario > sorteio:
        print(f"O número sorteado é menor do que {numero_usuario}")
        return False
    
    else:
        print(f"O número sorteado é maior do que {numero_usuario}")
        return False
    
numero_sorteio = random.randint(1, 15)

for i in range(3):
    
    numero_usuario = get_input()
    if check_numbers(sorteio=numero_sorteio, usuario=numero_usuario):
        break

else:
    print(f"Suas tentativas acabaram. O número sorteado era {numero_sorteio}")