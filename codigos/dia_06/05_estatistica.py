def soma(a:float, b:float, *args)->float:
    """
    Esta função tem a finalidade de somar dois numeros e
    retornar o resultado desta soma
    """
    valores = [a, b] + list(args)
    return sum(valores)

def media (a:float, b:float, *args)->float:
    """
    Esta função tem a finalidade de calcular a média de dois
    numeros e retornar este resultado
    """
    return soma(a, b, *args) / (len(args) + 2 )

a = float(input("Digite o primeiro numero: "))
b = float(input("Digite o segundo numero: "))
c = float(input("Digite o terceiro numero: "))
d = float(input("Digite o quarto numero: "))

print(f" A soma dos numeros é: {soma(a, b, c, d)}")
print(f" A média dos numeros é: {media(a, b, c, d)}")

