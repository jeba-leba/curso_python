# criando uma função de raiz
def sqrt(numero):
    """Calcula a raiz quadrada de um número."""
    if numero < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
    return numero ** 0.5

sqrt(9)

# importa a biblioteca toda
import math

math.sqrt(9)
math.pow(2, 4)
math.pi

# importa apenas uma função da biblioteca
from math import pi, e

# importa a biblioteca com um apelido
import math as mh

