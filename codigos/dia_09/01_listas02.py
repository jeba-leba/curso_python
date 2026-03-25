# Para adicionar numeros de 1 a 100 na lista x.

x = []

for i in range(1,101):
    x.append(i)

print(x)

# Uma maneira mais fácil de adicionar numeros de 1 a 100:
y = [i for i in range(1,101)]

print(y)

# Função que verifica se o numero é par retornando True ou False
def par(x):
    return x % 2 == 0

# criando uma lista com a função nova que verifica se é par
z = [par(i) for i in range(1,101)]
    
print(z)

# fazendo a lista só que adicionando apenas numeros pares
w = [i for i in range(1,101) if par(i)]
print(w)