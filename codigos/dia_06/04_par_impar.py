def par_impar(numero:int):
    if numero % 2 == 0:
        print(f" O número {numero} é par. ")
    else:
        print(f" O número {numero} é impar. ")

numero = int(input("Digite um número inteiro: "))

par_impar(numero)
